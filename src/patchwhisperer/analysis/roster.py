import logging
import re
import time
from dataclasses import dataclass
from datetime import UTC, date, datetime, timedelta
from html import unescape
from pathlib import Path

from patchwhisperer.analysis import context as ctx
from patchwhisperer.analysis.enrich import enrich_hero, merge_enrichment
from patchwhisperer.analysis.pipeline import _run_stage
from patchwhisperer.analysis.render import (
    render_checkin_card,
    render_hero_card,
)
from patchwhisperer.analysis.schemas import NewHeroCard, NewHeroEvaluation
from patchwhisperer.kb.git import git_commit_kb, git_sync
from patchwhisperer.kb.schema import HeroState
from patchwhisperer.kb.store import KBStore, slugify
from patchwhisperer.parse.bbcode import bbcode_to_lines
from patchwhisperer.parse.entities import EntityIndex
from patchwhisperer.sources.deadlock_api import DeadlockAPI
from patchwhisperer.sources.steam_news import (
    PostKind,
    SteamPost,
    fetch_patch_posts,
)

log = logging.getLogger(__name__)

_TAG_RE = re.compile(r"<[^>]+>")
_SKIP_ABILITIES = {"melee", "jump"}
_PHASE_LABELS = {
    "early_game": "early",
    "mid_game": "mid",
    "late_game": "late",
}


@dataclass
class RosterResult:
    added: list[str]
    checked_in: list[str]
    index: EntityIndex


def new_heroes(active: list[dict], kb_heroes: dict[str, HeroState]) -> list[dict]:
    return [h for h in active if h["name"] not in kb_heroes]


def find_release_post(name: str, posts: list[SteamPost]) -> SteamPost | None:
    """Newest hero_release post whose title or body mentions `name`."""
    pats = [name.lower()]
    stripped = name.lower().removeprefix("the ")
    if stripped != name.lower():
        pats.append(stripped)
    for p in sorted(posts, key=lambda p: p.date, reverse=True):
        if p.kind != PostKind.hero_release:
            continue
        hay = f"{p.title} {p.contents}".lower()
        if any(pat in hay for pat in pats):
            return p
    return None


def upcoming_heroes(all_heroes: list[dict]) -> list[str]:
    return [
        h["name"]
        for h in all_heroes
        if not h.get("player_selectable", True) and not h.get("disabled")
    ]


def _stat(stats: dict, key: str) -> str:
    v = stats.get(key)
    if isinstance(v, dict):
        v = v.get("value")
    return str(v) if v is not None else "?"


def _strip_html(text: str) -> str:
    return re.sub(r"\s+", " ", unescape(_TAG_RE.sub("", text or ""))).strip()


def hero_kit_text(
    hero: dict, abilities: list[dict], index: EntityIndex
) -> str:
    lines = [
        (
            f"type: {hero.get('hero_type', '?')} | gun: {hero.get('gun_tag', '?')} | "
            f"tags: {', '.join(hero.get('tags') or []) or '?'} | "
            f"complexity: {hero.get('complexity', '?')}"
        )
    ]
    s = hero.get("starting_stats") or {}
    lines.append(
        "base stats: "
        f"hp {_stat(s, 'max_health')} | move {_stat(s, 'max_move_speed')} | "
        f"sprint {_stat(s, 'sprint_speed')} | stamina {_stat(s, 'stamina')} | "
        f"light melee {_stat(s, 'light_melee_damage')} | "
        f"heavy melee {_stat(s, 'heavy_melee_damage')} | "
        f"regen {_stat(s, 'base_health_regen')}"
    )
    item_by_id = {it["id"]: it["name"] for it in index.items}
    for a in abilities:
        if a.get("type") != "ability" or a.get("name", "").lower() in _SKIP_ABILITIES:
            continue
        desc = _strip_html((a.get("description") or {}).get("desc", ""))
        lines.append(f"**{a.get('name', '?')}** — {desc}")
        for tier, up in enumerate(a.get("upgrades") or [], start=1):
            parts = [
                f"{p.get('name', '?')} {p.get('bonus', '')}".strip()
                for p in up.get("property_upgrades") or []
            ]
            if parts:
                lines.append(f"  T{tier}: {', '.join(parts)}")
    popular = hero.get("popular_items") or {}
    for key, entries in popular.items():
        if not isinstance(entries, list) or not entries:
            continue
        names = []
        for e in entries[:8]:
            item_name = item_by_id.get(e.get("item_id"), e.get("class_name", "?"))
            names.append(
                f"{item_name} (pick {e.get('pick_pct', 0):.0f}%, "
                f"win {e.get('winrate_pct', 0):.0f}%)"
            )
        label = _PHASE_LABELS.get(key, key)
        lines.append(f"popular items ({label}): {', '.join(names)}")
    return "\n".join(lines)


def hero_early_stats(api: DeadlockAPI, hero_id: int, days: int = 7) -> dict | None:
    stats = api.hero_stats(min_unix=int(time.time()) - days * 86400)
    row = next((s for s in stats if s["hero_id"] == hero_id), None)
    if not row or not row.get("matches"):
        return None
    total = sum(s["matches"] for s in stats) or 1
    return {
        "matches": row["matches"],
        "win_rate": row["wins"] / row["matches"],
        "pick_rate": row["matches"] / (total / 12),
    }


def _bbcode_text(contents: str) -> str:
    return "\n".join(line for _, line in bbcode_to_lines(contents))


def evaluate_new_hero(
    name: str,
    hero: dict,
    *,
    kb: KBStore,
    index: EntityIndex,
    api: DeadlockAPI,
    llm,
    release_post: SteamPost | None,
    sources_dir: Path,
    today: date,
) -> tuple[HeroState, NewHeroCard]:
    abilities = api.hero_abilities(hero["id"])
    kit = hero_kit_text(hero, abilities, index)
    stats = hero_early_stats(api, hero["id"])
    if stats:
        early = (
            f"WR {stats['win_rate'] * 100:.1f}% | PR "
            f"{stats['pick_rate'] * 100:.1f}% | matches {stats['matches']} "
            "(first 7 days)"
        )
    else:
        early = "(no ranked data yet)"
    release = _bbcode_text(release_post.contents) if release_post else "(none)"
    claims = ctx.creator_claims(sources_dir)
    all_heroes = api.all_heroes()
    released = release_post.date.date() if release_post else today
    patch_id = f"hero-{slugify(name)}-{released:%Y-%m-%d}"
    result: NewHeroEvaluation = _run_stage(
        llm,
        kb,
        patch_id,
        "hero",
        "new_hero",
        NewHeroEvaluation,
        tag="day0",
        budget_key="hero",
        prefix="",
        hero=name,
        today=f"{today:%Y-%m-%d}",
        kit=kit,
        early_stats=early,
        release_post=release or "(none)",
        meta_md=kb.load_meta() if kb.meta_path.exists() else "(empty)",
        tier_list=ctx.tier_list(kb),
        corrections=kb.load_corrections() or "(none)",
        creator_claims="\n".join(claims.get(name, [])) or "(none)",
        upcoming=", ".join(upcoming_heroes(all_heroes)) or "(none)",
        item_names=", ".join(sorted(i["name"] for i in index.items)),
    )
    state = merge_enrichment(HeroState(name=name), result.enrichment)
    state.released_on = f"{released:%Y-%m-%d}"
    state.provisional = True
    state.last_changed_patch = (
        release_post.title if release_post else f"Released {today}"
    )
    state.confidence = result.enrichment.confidence
    due = released + timedelta(days=7)
    prefix = (
        f"Day-0 kit read ({today}), provisional — data check-in due {due}."
    )
    state.notes = f"{prefix}\n{state.notes}" if state.notes else prefix
    return state, result.card


def apply_new_hero(kb: KBStore, state: HeroState) -> list[Path]:
    heroes = kb.load_heroes()
    heroes[state.name] = state
    kb.save_heroes(heroes)
    changed = [kb.heroes_path]
    item_names = [i for b in state.builds for i in b.core_items]
    if kb.add_bought_by(state.name, item_names):
        changed.append(kb.items_path)
    return changed


def checkins_due(
    kb_heroes: dict[str, HeroState], today: date, days: int = 7
) -> list[str]:
    due = []
    for name, h in kb_heroes.items():
        if not h.provisional or not h.released_on:
            continue
        if date.fromisoformat(h.released_on) + timedelta(days=days) <= today:
            due.append(name)
    return due


def checkin_hero(
    name: str,
    *,
    kb: KBStore,
    index: EntityIndex,
    api: DeadlockAPI,
    llm,
    today: date,
    sources_dir: Path | None = None,
) -> tuple[HeroState, HeroState, str]:
    heroes = kb.load_heroes()
    state = heroes[name]
    before = state.model_copy(deep=True)
    claims = ctx.creator_claims(sources_dir or kb.root / "sources")
    try:
        latest = fetch_patch_posts(count=1)
        latest_title = latest[0].title if latest else "unknown"
    except Exception:  # noqa: BLE001 - title is cosmetic context
        latest_title = "unknown"
    result = enrich_hero(
        name,
        kb=kb,
        index=index,
        api=api,
        llm=llm,
        claims=claims,
        counters=api.hero_counters(days=7),
        snap=api.snapshot(days=7),
        meta_md=kb.load_meta() if kb.meta_path.exists() else "",
        corrections=kb.load_corrections(),
        tiers=ctx.tier_list(kb),
        latest_title=latest_title,
        days=7,
    )
    state = merge_enrichment(state, result)
    state.provisional = False
    hero_id = next((x["id"] for x in index.heroes if x["name"] == name), None)
    stats = hero_early_stats(api, hero_id) if hero_id is not None else None
    note = f"7-day check-in ({today}): tier {before.tier} -> {state.tier}"
    if stats:
        note += (
            f", WR {stats['win_rate'] * 100:.0f}%, PR "
            f"{stats['pick_rate'] * 100:.0f}% over {stats['matches']} matches."
        )
    else:
        note += ", no ranked data."
    state.notes = f"{note}\n{state.notes}" if state.notes else note
    apply_new_hero(kb, state)
    card = render_checkin_card(name, before, state, stats)
    return before, state, card


def _day0_done(kb: KBStore, name: str) -> bool:
    slug = slugify(name)
    return any((kb.root / "patches").glob(f"hero-{slug}-*/day0.json"))


def sync_roster(
    *,
    kb: KBStore,
    index: EntityIndex,
    api: DeadlockAPI,
    llm,
    sources_dir: Path,
    today: date | None = None,
    release_post: SteamPost | None = None,
    post_fn=None,
    commit_fn=git_commit_kb,
    sync_fn=git_sync,
    repo_root: Path = Path("."),
) -> RosterResult:
    """Add new heroes to the KB (day-0 read) and run due 7-day check-ins."""
    today = today or datetime.now(tz=UTC).date()
    added: list[str] = []
    checked_in: list[str] = []
    sync_fn(repo_root)

    kb_heroes = kb.load_heroes()
    posts: list[SteamPost] | None = None
    for hero in sorted(new_heroes(api.heroes(), kb_heroes), key=lambda h: h["id"]):
        name = hero["name"]
        try:
            if release_post is not None and name.lower() in (
                release_post.title + release_post.contents
            ).lower():
                rp = release_post
            else:
                if posts is None:
                    try:
                        posts = fetch_patch_posts(count=12)
                    except Exception:  # noqa: BLE001 - release post is optional
                        posts = []
                rp = find_release_post(name, posts)
            released = rp.date.date() if rp else today
            patch_id = f"hero-{slugify(name)}-{released:%Y-%m-%d}"
            if _day0_done(kb, name):
                # another machine already evaluated this hero; kb is git-synced
                if name not in kb.load_heroes():
                    apply_new_hero(kb, HeroState(name=name))
                continue
            state, card = evaluate_new_hero(
                name,
                hero,
                kb=kb,
                index=index,
                api=api,
                llm=llm,
                release_post=rp,
                sources_dir=sources_dir,
                today=today,
            )
            changed = apply_new_hero(kb, state)
            if post_fn is not None:
                post_fn(render_hero_card(name, card, state), patch_id)
            commit_fn(
                repo_root,
                changed + [kb.patch_dir(patch_id)],
                f"kb: new hero {name} (day-0 read)",
            )
            added.append(name)
        except Exception:
            log.exception("roster sync failed for %s", name)
    if added:
        index = EntityIndex.fetch()

    for name in checkins_due(kb.load_heroes(), today):
        try:
            _, state, card = checkin_hero(
                name, kb=kb, index=index, api=api, llm=llm, today=today,
                sources_dir=sources_dir,
            )
            if post_fn is not None:
                post_fn(card, f"hero-{slugify(name)}-{today:%Y-%m-%d}-checkin")
            commit_fn(
                repo_root,
                [kb.heroes_path, kb.items_path],
                f"kb: {name} 7-day check-in",
            )
            checked_in.append(name)
        except Exception:
            log.exception("roster check-in failed for %s", name)
    return RosterResult(added=added, checked_in=checked_in, index=index)
