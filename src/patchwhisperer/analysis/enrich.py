from datetime import UTC, datetime

import yaml

from patchwhisperer import config
from patchwhisperer.analysis.context import _non_empty
from patchwhisperer.analysis.llm import SYSTEM_PROMPT, render_prompt
from patchwhisperer.analysis.schemas import HeroEnrichment
from patchwhisperer.kb.schema import Build, HeroState, Matchups


def enrich_hero(
    name: str,
    *,
    kb,
    index,
    api,
    llm,
    claims: dict[str, list[str]],
    counters,
    snap: dict,
    meta_md: str,
    corrections: str,
    tiers: str,
    latest_title: str,
    days: int,
) -> HeroEnrichment:
    """One data-driven re-evaluation of a hero (item usage, counters, snapshot)."""
    h = kb.load_heroes()[name]
    hero_id = next(x["id"] for x in index.heroes if x["name"] == name)
    usage = api.hero_item_usage(hero_id, index, days=days)
    usage_txt = "\n".join(
        f"{u.item} | {u.share * 100:.0f}% | {u.win_rate * 100:.1f}% | "
        f"{u.avg_buy_min:.1f} | {u.slot or '?'} T{u.tier or '?'}"
        for u in usage
    )
    c = counters.get(hero_id)
    beats = (
        ", ".join(f"{n} ({wr * 100:.0f}% over {m})" for n, wr, m in c.beats)
        if c
        else "(none)"
    )
    loses = (
        ", ".join(f"{n} ({wr * 100:.0f}% over {m})" for n, wr, m in c.loses_to)
        if c
        else "(none)"
    )
    hsnap = snap.get(name, {})
    snap_txt = (
        f"WR {hsnap.get('win_rate', 0) * 100:.1f}% | "
        f"PR {hsnap.get('pick_rate', 0) * 100:.1f}% | "
        f"matches {hsnap.get('matches', 0)}"
    )
    prompt = render_prompt(
        "enrich_hero",
        hero=name,
        as_of_date=f"{datetime.now(tz=UTC):%Y-%m-%d}",
        latest_patch_title=latest_title,
        hero_entry=yaml.safe_dump(_non_empty(h.model_dump()), sort_keys=False),
        abilities=", ".join(index.abilities.get(hero_id, [])),
        days=str(days),
        item_usage=usage_txt or "(no data)",
        beats=beats,
        loses_to=loses,
        hero_snapshot=snap_txt,
        creator_claims="\n".join(claims.get(name, [])) or "(none)",
        tier_list=tiers,
        corrections=corrections or "(none)",
        meta_md=meta_md,
    )
    return llm.complete_json(
        SYSTEM_PROMPT,
        prompt,
        HeroEnrichment,
        max_tokens=config.STAGE_MAX_TOKENS["enrich"],
    )


def merge_enrichment(h: HeroState, r: HeroEnrichment) -> HeroState:
    """Apply a HeroEnrichment to a HeroState, preserving name/last_changed_patch."""
    h.role = r.role or h.role
    h.archetypes = r.archetypes or h.archetypes
    h.tier = r.tier
    h.trend = r.trend
    h.why = r.why or h.why
    h.builds = [Build(**b.model_dump()) for b in r.builds]
    h.core_items = r.core_items or h.core_items
    h.build_variants = [b.name for b in r.builds]
    if r.matchups:
        h.matchups = Matchups(**r.matchups.model_dump())
    h.matchup_notes = r.matchup_notes
    h.enabled_by = r.enabled_by
    h.countered_by = r.countered_by
    h.notes = r.notes or h.notes
    h.confidence = r.confidence
    return h
