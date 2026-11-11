"""Pure page-model construction: analysis + patch + art -> template-ready views."""

import re
from datetime import UTC, date, datetime
from functools import partial

from pydantic import BaseModel

from patchwhisperer.analysis.schemas import (
    AnalysisBundle,
    ChangeRow,
    ResetStep,
    SeasonBundle,
    SeasonRule,
    SeasonVerdict,
)
from patchwhisperer.analysis.tiers import HeroTier, TierBand, TierSnapshot
from patchwhisperer.kb.store import slugify
from patchwhisperer.parse.models import Change, Direction, EntityType, Patch

_MAGNITUDE_RANK = {"major": 0, "moderate": 1, "minor": 2, "none": 3}
_VERDICT_RANK = {"keep": 0, "watch": 1, "bench": 2}
_DIRECTION_RANK = {"up": 0, "neutral": 1, "down": 2}
_DIRECTION_EFFECT = {
    Direction.buff: "good",
    Direction.nerf: "bad",
}
_CATEGORY_ORDER = ["weapon", "spirit", "vitality", "other"]
_CHEVRONS = {"major": 3, "moderate": 2, "minor": 1}
_HERO_GROUPS = [
    ("buff", "Buffed", "▲"),
    ("nerf", "Nerfed", "▼"),
    ("rework", "Reworked", "↻"),
    ("adjusted", "Adjusted", "≈"),
    ("indirect", "Not in the notes, still affected", "◆"),
    ("unchanged", "No direct or major changes", "·"),
]
_KIND_WORD = {
    "buff": "Buffed",
    "nerf": "Nerfed",
    "rework": "Reworked",
    "adjusted": "Adjusted",
}
_TIER_ORDER = ["S", "A", "B", "C", "D", "F"]
_TIER_RANK = {tier: i for i, tier in enumerate(_TIER_ORDER)}
_MOVED_RANK = {"up": 0, None: 1, "down": 2}
_BIG_KIND_LABEL = {"hero": "Hero", "item": "Item", "system": "Map & economy"}
_SHEET_PREFIX = {"hero": "hero", "item": "item", "system": "sys"}
_TEMPO = {
    "toward_tempo": ("Games shift toward early tempo", -1),
    "toward_scaling": ("Games shift toward late scaling", 1),
    "neutral": ("No clear shift in game pace", 0),
}
_DELTA_RE = re.compile(
    r"^(?P<label>.+?)\s+(?P<verb>increased|reduced|decreased|lowered|raised|rises?|drops?)\s+"
    r"(?:from\s+(?:a max of\s+)?(?P<old>\S+)\s+to\s+(?P<new>\S+)|by\s+(?P<by>\S+))",
    re.IGNORECASE,
)
_UP_VERBS = ("increased", "raised", "rise", "rises")


class RowView(BaseModel):
    label: str
    old: str | None = None
    new: str | None = None
    text: str | None = None
    effect: str = "neutral"


class RowGroupView(BaseModel):
    ability: str | None = None
    icon: str | None = None
    rows: list[RowView] = []


class TierStatView(BaseModel):
    label: str
    tier: str
    win_rate: str
    games: str
    delta: str | None = None
    delta_effect: str = "neutral"


class HeroCardView(BaseModel):
    slug: str
    name: str
    initials: str
    portrait: str | None = None
    verdict: str | None = None
    direction: str = "neutral"
    badge_word: str = ""
    badge_class: str = "v-neutral"
    pool_rank: int = 1
    magnitude: str = "none"
    in_notes: bool = False
    one_liner: str = ""
    tier_chip: str | None = None
    tier_stats: list[TierStatView] = []
    tier_after: str = "?"
    tier_before: str = "?"
    groups: list[RowGroupView] = []
    indirect_reasons: list[str] = []
    build_changes: list[str] = []
    board_group: str | None = None
    chevrons: int = 0
    kind_word: str = ""


class HeroGroupView(BaseModel):
    key: str
    label: str
    glyph: str
    heroes: list[HeroCardView] = []


class AffectedHeroView(BaseModel):
    slug: str
    name: str
    initials: str
    portrait: str | None = None
    effect: str = "neutral"
    why: str = ""


class ItemCardView(BaseModel):
    slug: str
    name: str
    initials: str
    direction: str = "neutral"
    magnitude: str = "minor"
    category: str = ""
    icon: str | None = None
    summary: str = ""
    build_shift: str = ""
    groups: list[RowGroupView] = []
    chevrons: int = 0
    affected: list[AffectedHeroView] = []
    hero_slugs: str = ""


class ItemGroupView(BaseModel):
    category: str
    items: list[ItemCardView] = []


class DeltaView(BaseModel):
    label: str
    value: str
    direction: str = "neutral"


class SystemView(BaseModel):
    slug: str
    name: str
    change_summary: str = ""
    effect_on_play: str = ""
    magnitude: str = "minor"
    chevrons: int = 0
    deltas: list[DeltaView] = []
    lines: list[str] = []
    groups: list[RowGroupView] = []


class ArchetypeView(BaseModel):
    name: str
    direction: str
    chevrons: int = 0
    why: str = ""


class TempoView(BaseModel):
    label: str
    position: int = 50
    why: str = ""



class TierHeroView(BaseModel):
    slug: str
    name: str
    initials: str
    portrait: str | None = None
    verdict: str | None = None
    badge_word: str = ""
    badge_class: str = "v-neutral"
    moved: str | None = None
    was: str | None = None
    win_rate: str | None = None
    sort_win_rate: float = 0.0


class TierRowView(BaseModel):
    tier: str
    heroes: list[TierHeroView] = []


class TierBoardView(BaseModel):
    key: str
    label: str
    note: str
    rows: list[TierRowView] = []


class BigChangeView(BaseModel):
    kind: str
    kind_label: str
    name: str
    title: str
    why: str = ""
    effect: str = "neutral"
    sheet: str | None = None
    portrait: str | None = None
    icon: str | None = None
    initials: str = ""


class PatchPageModel(BaseModel):
    patch_id: str
    title: str
    date_display: str
    url: str
    headline: str
    patch_size: str
    size_why: str = ""
    hero_groups: list[HeroGroupView] = []
    heroes: list[HeroCardView] = []
    biggest_changes: list[BigChangeView] = []
    tier_boards: list[TierBoardView] = []
    picker: list[dict] = []  # plain dicts so Jinja's tojson can serialize safely
    item_groups: list[ItemGroupView] = []
    small_items: list[ItemCardView] = []
    systems: list[SystemView] = []
    small_systems: list[SystemView] = []
    tempo: TempoView | None = None
    archetypes: list[ArchetypeView] = []
    game_plan: str = ""
    counts_line: str = ""


class ArchiveEntry(BaseModel):
    patch_id: str
    title: str
    date_display: str
    headline: str
    label: str


class RungView(BaseModel):
    name: str
    color: str
    icon: str | None = None
    no_shield: bool = False
    cap_before: bool = False
    cap_after: bool = False
    in_stretch: bool = False


class RuleView(BaseModel):
    label: str
    category: str
    category_label: str
    before: str | None = None
    after: str
    effect: str
    effect_label: str
    note: str = ""
    viz: str = "text"  # pips | bars | text
    pips: list[str] = []  # keep | lost | gained
    bar_before: int = 0  # percent widths
    bar_after: int = 0


class SeasonPageModel(BaseModel):
    patch_id: str
    title: str
    season_name: str
    date_display: str
    starts_display: str
    ends_display: str
    ends_line: str
    left_line: str
    elapsed_pct: int
    url: str
    headline: str
    reset_steps: list[ResetStep] = []
    soft_reset: str = ""
    cap_before: str | None = None
    cap_after: str | None = None
    cap_stretch: str | None = None
    no_shield_ranks: list[str] = []
    rungs: list[RungView] = []
    rules: list[RuleView] = []
    tally: dict[str, int] = {}
    winners: list[SeasonVerdict] = []
    losers: list[SeasonVerdict] = []


_CATEGORY_LABEL = {
    "climbing": "Climbing",
    "protection": "Loss protection",
    "draft": "Draft",
    "unlocks": "Placement & unlocks",
    "leaderboards": "Leaderboards",
    "other": "Other",
}
_AMOUNT_RE = re.compile(r"^\s*(\d+)\s*(.*)$")
_PIP_MAX = 10


def _amount(value: str | None, unit_hint: str = "") -> tuple[int, str] | None:
    if value is None:
        return None
    if value.strip().lower() == "none":
        return 0, unit_hint
    m = _AMOUNT_RE.match(value)
    return (int(m.group(1)), m.group(2).strip().lower()) if m else None


def _rule_view(rule: SeasonRule) -> RuleView:
    view = RuleView(
        label=rule.label,
        category=rule.category,
        category_label=_CATEGORY_LABEL[rule.category],
        before=rule.before,
        after=rule.after,
        effect=rule.effect,
        effect_label=rule.effect_label,
        note=rule.note,
    )
    before = _amount(rule.before)
    after = _amount(rule.after, before[1] if before else "")
    if not (before and after) or before[1][:3] != after[1][:3]:
        return view
    b, a = before[0], after[0]
    if max(a, b) <= _PIP_MAX:
        lo = min(a, b)
        view.viz = "pips"
        view.pips = [
            "keep" if i < lo else ("gained" if a > b else "lost")
            for i in range(max(a, b))
        ]
    elif a and b:
        top = max(a, b)
        view.viz = "bars"
        view.bar_before = round(100 * b / top)
        view.bar_after = round(100 * a / top)
    return view


def _rank_name(value: str | None) -> str:
    return (value or "").split(" ")[0].lower()


def _rungs(ranks: list[dict], bundle: SeasonBundle) -> list[RungView]:
    ladder = bundle.ladder
    no_shield = {n.lower() for n in ladder.no_shield_ranks}
    before = _rank_name(ladder.placement_cap_before)
    after = _rank_name(ladder.placement_cap_after)
    stretch = _rank_name(ladder.placement_cap_stretch)
    names = [r["name"].lower() for r in ranks]
    lo = names.index(after) if after in names else -1
    hi = names.index(stretch) if stretch in names else lo
    return [
        RungView(
            name=r["name"],
            color=r["color"],
            icon=r.get("icon"),
            no_shield=n in no_shield,
            cap_before=n == before,
            cap_after=n == after,
            in_stretch=lo >= 0 and lo <= i <= hi,
        )
        for i, (r, n) in enumerate(zip(ranks, names, strict=True))
    ]


def fmt_date(iso: str) -> str:
    """'2026-11-05' -> 'Nov 5, 2026'; passes through anything unparseable."""
    try:
        d = date.fromisoformat(iso.strip())
    except ValueError:
        return iso
    return f"{d:%b} {d.day}, {d:%Y}"


def _parse_date(iso: str | None) -> date | None:
    if not iso:
        return None
    try:
        return date.fromisoformat(iso.strip())
    except ValueError:
        return None


def _season_left(starts: date | None, ends: date | None, today: date) -> tuple[str, int]:
    """('17 weeks left', percent of the season elapsed)."""
    if ends is None:
        return "no end date announced", 0
    if ends <= today:
        return "season over", 100
    days = (ends - today).days
    left = f"{days // 7} weeks left" if days >= 14 else f"{days} days left"
    if starts is None or ends <= starts:
        return left, 0
    total = (ends - starts).days
    return left, max(0, min(100, round(100 * (today - starts).days / total)))


def build_season_model(
    bundle: SeasonBundle, patch_id: str, today: date, ranks: list[dict] | None = None
) -> SeasonPageModel:
    starts = _parse_date(bundle.starts or bundle.date)
    ends = _parse_date(bundle.ends)
    left, elapsed = _season_left(starts, ends, today)
    rules = [_rule_view(r) for r in bundle.rules]
    return SeasonPageModel(
        patch_id=patch_id,
        title=bundle.title,
        season_name=bundle.season_name or bundle.title,
        date_display=fmt_date(bundle.date or bundle.starts),
        starts_display=fmt_date(bundle.starts or bundle.date),
        ends_display=fmt_date(bundle.ends) if bundle.ends else "",
        ends_line=(
            f"ended {fmt_date(bundle.ends)}"
            if ends and ends <= today
            else f"ends {fmt_date(bundle.ends)} · {left}" if ends else left
        ),
        left_line=left,
        elapsed_pct=elapsed,
        url=bundle.url,
        headline=bundle.headline,
        reset_steps=bundle.reset_steps,
        soft_reset=bundle.ladder.soft_reset,
        cap_before=bundle.ladder.placement_cap_before,
        cap_after=bundle.ladder.placement_cap_after,
        cap_stretch=bundle.ladder.placement_cap_stretch,
        no_shield_ranks=bundle.ladder.no_shield_ranks,
        rungs=_rungs(ranks or [], bundle),
        rules=rules,
        tally={e: sum(r.effect == e for r in rules) for e in ("easier", "harsher", "neutral")},
        winners=bundle.winners,
        losers=bundle.losers,
    )


def _initials(name: str) -> str:
    parts = [p for p in name.replace("&", " ").split() if p]
    if not parts:
        return "?"
    return "".join(p[0] for p in parts[:2]).upper()


def _badge(verdict: str | None, direction: str) -> tuple[str, str, int]:
    """Return (word, css class, pool rank) for a hero badge."""
    if verdict:
        return (
            verdict,
            f"v-{verdict}",
            _VERDICT_RANK.get(verdict, 1),
        )
    word = {"up": "up", "down": "down"}.get(direction, "neutral")
    css = {"up": "v-keep", "down": "v-bench"}.get(direction, "v-neutral")
    return word, css, _DIRECTION_RANK.get(direction, 1)


def _no_icon(ability: str | None) -> None:
    return None


def _row_groups(
    rows: list[ChangeRow],
    icon_for,
) -> list[RowGroupView]:
    groups: list[RowGroupView] = []
    by_key: dict[str | None, RowGroupView] = {}
    for row in rows:
        key = row.ability
        group = by_key.get(key)
        if group is None:
            group = RowGroupView(ability=key, icon=icon_for(key))
            by_key[key] = group
            groups.append(group)
        group.rows.append(
            RowView(
                label=row.label,
                old=row.old,
                new=row.new,
                text=row.text,
                effect=row.effect,
            )
        )
    return groups


def _fallback_groups(
    entity_name: str,
    entity_type: EntityType,
    patch: Patch,
    icon_for,
) -> list[RowGroupView]:
    groups: list[RowGroupView] = []
    by_key: dict[str | None, RowGroupView] = {}
    for change in patch.changes:
        if (
            change.mode_only
            or change.entity_type != entity_type
            or change.entity_name != entity_name
        ):
            continue
        key = change.ability
        group = by_key.get(key)
        if group is None:
            group = RowGroupView(ability=key, icon=icon_for(key))
            by_key[key] = group
            groups.append(group)
        group.rows.append(
            RowView(
                label="Change",
                text=_note_text(change),
                effect=_DIRECTION_EFFECT.get(change.direction, "neutral"),
            )
        )
    return groups


def _note_text(change: Change) -> str:
    text = change.raw.removeprefix(f"{change.entity_name}: ")
    if change.ability:
        text = text.removeprefix(f"{change.ability} - ")
    return text


def _driving_deltas(lines: list[str]) -> list[DeltaView]:
    deltas = []
    for line in lines:
        m = _DELTA_RE.match(line)
        if not m:
            continue
        up = m["verb"].lower() in _UP_VERBS
        if m["old"]:
            value = f"{m['old']} → {m['new'].rstrip('.,;')}"
        else:
            by = m["by"].rstrip(".,;")
            value = by if by[0] in "+-" else f"{'+' if up else '-'}{by}"
        deltas.append(
            DeltaView(
                label=re.sub(r"\s*\(.*?\)", "", m["label"]),
                value=value,
                direction="up" if up else "down",
            )
        )
    return deltas


def _group_deltas(groups: list[RowGroupView]) -> list[DeltaView]:
    return [
        DeltaView(label=r.label, value=f"{r.old} → {r.new}")
        for g in groups
        for r in g.rows
        if r.old and r.new
    ]


def _board_group(direct: bool, kind: str, direction: str) -> str:
    if direct:
        if kind != "none":
            return kind
        return {"up": "buff", "down": "nerf"}.get(direction, "adjusted")
    return "indirect" if direction != "neutral" else "unchanged"


def _tier_hero(h: HeroCardView, moved: str | None, was: str | None) -> TierHeroView:
    return TierHeroView(
        slug=h.slug,
        name=h.name,
        initials=h.initials,
        portrait=h.portrait,
        verdict=h.verdict,
        badge_word=h.badge_word,
        badge_class=h.badge_class,
        moved=moved,
        was=was,
    )


def _tier_rows(heroes: list[HeroCardView]) -> list[TierRowView]:
    by_tier: dict[str, list[TierHeroView]] = {}
    for h in heroes:
        moved = was = None
        if h.tier_before in _TIER_RANK and h.tier_after in _TIER_RANK:
            if _TIER_RANK[h.tier_after] < _TIER_RANK[h.tier_before]:
                moved, was = "up", h.tier_before
            elif _TIER_RANK[h.tier_after] > _TIER_RANK[h.tier_before]:
                moved, was = "down", h.tier_before
        bucket = h.tier_after if h.tier_after in _TIER_RANK else "?"
        by_tier.setdefault(bucket, []).append(
            _tier_hero(h, moved, was)
        )
    rows = [
        TierRowView(tier=tier, heroes=by_tier[tier])
        for tier in _TIER_ORDER
        if tier in by_tier
    ]
    if "?" in by_tier:
        rows.append(TierRowView(tier="Unrated", heroes=by_tier["?"]))
    for row in rows:
        row.heroes.sort(key=lambda h: (_MOVED_RANK[h.moved], h.name))
    return rows


def _measured_verdict(tier: str) -> str:
    return {"S": "keep", "A": "keep", "D": "bench"}.get(tier, "watch")


def _pct(value: float) -> str:
    return f"{value * 100:.1f}%"


def _tier_stat(band: TierBand, stat: HeroTier) -> TierStatView:
    delta = effect = None
    if stat.delta is not None:
        delta = f"{stat.delta * 100:+.1f} since the patch"
        effect = "good" if stat.delta > 0 else "bad" if stat.delta < 0 else "neutral"
    return TierStatView(
        label=band.label,
        tier=stat.tier,
        win_rate=_pct(stat.win_rate),
        games=f"{stat.matches:,} games",
        delta=delta,
        delta_effect=effect or "neutral",
    )


def _measured_rows(heroes: list[HeroCardView], band: TierBand) -> list[TierRowView]:
    by_tier: dict[str, list[TierHeroView]] = {}
    for h in heroes:
        stat = band.heroes.get(h.name)
        if stat is None:
            by_tier.setdefault("?", []).append(_tier_hero(h, None, None))
            continue
        moved = None
        if stat.prev_tier and stat.prev_tier != stat.tier:
            rising = _TIER_RANK[stat.tier] < _TIER_RANK[stat.prev_tier]
            moved = "up" if rising else "down"
        view = _tier_hero(h, moved, stat.prev_tier if moved else None)
        view.win_rate = _pct(stat.win_rate)
        view.sort_win_rate = stat.win_rate
        by_tier.setdefault(stat.tier, []).append(view)
    rows = [
        TierRowView(tier=tier, heroes=by_tier[tier])
        for tier in _TIER_ORDER
        if tier in by_tier
    ]
    if "?" in by_tier:
        rows.append(TierRowView(tier="Unrated", heroes=by_tier["?"]))
    for row in rows:
        row.heroes.sort(key=lambda h: (-h.sort_win_rate, h.name))
    return rows


EARLY_SAMPLE_MATCHES = 30_000


def _band_note(band: TierBand, updated: str, reset_on: str | None = None) -> str:
    who = "ranked games" if band.key == "ranked" else "Ascendant and Eternus games"
    if band.post_patch:
        early = (
            " Still an early sample, so expect tiers to move."
            if band.matches < EARLY_SAMPLE_MATCHES
            else ""
        )
        reset = (
            f" Ranks were reset on {reset_on}."
            if reset_on and band.key == "high"
            else ""
        )
        return (
            f"Measured from {band.matches:,} {who} since the patch, updated {updated}."
            f"{early}{reset} Ring: green is strong right now, yellow is average, red is weak."
        )
    return (
        f"Too few games since the patch so far, so this shows {who} from "
        "before it. It updates every few hours as games are played."
    )


def _tier_boards(
    heroes: list[HeroCardView],
    tiers: TierSnapshot | None,
    reset_on: str | None = None,
) -> list[TierBoardView]:
    if tiers is None:
        return [
            TierBoardView(
                key="estimate",
                label="Estimate",
                note="No match data yet. This is an AI estimate from the patch notes.",
                rows=_tier_rows(heroes),
            )
        ]
    updated = f"{datetime.fromtimestamp(tiers.generated_at, UTC):%b} " + str(
        datetime.fromtimestamp(tiers.generated_at, UTC).day
    )
    return [
        TierBoardView(
            key=band.key,
            label=band.label,
            note=_band_note(band, updated, reset_on),
            rows=_measured_rows(heroes, band),
        )
        for band in tiers.bands
    ]


def _lookup_subject(lookup: dict, subject_slug: str):
    if subject_slug in lookup:
        return lookup[subject_slug]
    return next(
        (v for k, v in lookup.items() if f"-{subject_slug}-" in f"-{k}-"), None
    )


def _big_changes(
    analysis: AnalysisBundle,
    heroes: list[HeroCardView],
    item_groups: list[ItemGroupView],
    small_items: list[ItemCardView],
    systems: list[SystemView],
    small_systems: list[SystemView],
) -> list[BigChangeView]:
    lookups = {
        "hero": {h.slug: h for h in heroes},
        "item": {
            it.slug: it
            for it in small_items + [i for g in item_groups for i in g.items]
        },
        "system": {s.slug: s for s in systems + small_systems},
    }
    views = []
    for change in analysis.synthesis.biggest_changes:
        hit = None
        kind = change.kind
        for candidate in (change.kind, *(k for k in lookups if k != change.kind)):
            hit = _lookup_subject(lookups[candidate], slugify(change.subject))
            if hit is not None:
                kind = candidate
                break
        views.append(
            BigChangeView(
                kind=kind,
                kind_label=_BIG_KIND_LABEL[kind],
                name=hit.name if hit else change.subject,
                title=change.title,
                why=change.why,
                effect=change.effect,
                sheet=f"{_SHEET_PREFIX[kind]}-{hit.slug}" if hit else None,
                portrait=getattr(hit, "portrait", None),
                icon=getattr(hit, "icon", None),
                initials=_initials(hit.name if hit else change.subject),
            )
        )
    return views





def _counts_line(
    heroes: list[HeroCardView],
    item_groups: list[ItemGroupView],
    small_items: list[ItemCardView],
    systems: list[SystemView],
    small_systems: list[SystemView],
) -> str:
    parts = []
    for key, label, _ in _HERO_GROUPS:
        if key in ("indirect", "unchanged"):
            continue
        n = sum(1 for h in heroes if h.board_group == key)
        if n:
            parts.append(f"{n} {label.lower()}")
    n_items = len(small_items) + sum(len(g.items) for g in item_groups)
    if n_items:
        parts.append(f"{n_items} item{'s' if n_items != 1 else ''}")
    n_systems = len(systems) + len(small_systems)
    if n_systems:
        parts.append(f"{n_systems} map & economy")
    return " · ".join(parts)


def _mode_only_systems(patch: Patch) -> list[SystemView]:
    by_section: dict[str, list[str]] = {}
    for c in patch.changes:
        if c.mode_only:
            by_section.setdefault(c.section, []).append(c.raw)
    return [
        SystemView(
            slug=slugify(section),
            name=f"{section} only",
            change_summary=f"These {len(lines)} changes apply only in {section}.",
            magnitude="minor",
            lines=lines,
        )
        for section, lines in by_section.items()
    ]


def build_page_model(
    analysis: AnalysisBundle,
    patch: Patch,
    art,
    tiers: TierSnapshot | None = None,
    reset_on: str | None = None,
) -> PatchPageModel:
    heroes: list[HeroCardView] = []
    non_hero_systems: list[SystemView] = _mode_only_systems(patch)
    live_changes = [c for c in patch.changes if not c.mode_only]
    direct = {c.entity_name for c in live_changes if c.entity_type == EntityType.hero}
    not_heroes = {
        c.entity_name for c in live_changes if c.entity_type == EntityType.unknown
    } - direct
    primary = tiers.bands[0].heroes if tiers and tiers.bands else {}
    if analysis.heroes:
        for entry in analysis.heroes.heroes:
            if entry.hero in not_heroes:
                groups = _row_groups(entry.rows, _no_icon) or _fallback_groups(
                    entry.hero, EntityType.unknown, patch, _no_icon
                )
                non_hero_systems.append(
                    SystemView(
                        slug=slugify(entry.hero),
                        name=entry.hero,
                        change_summary=entry.one_liner,
                        magnitude=entry.magnitude,
                        chevrons=_CHEVRONS.get(entry.magnitude, 0),
                        deltas=_group_deltas(groups),
                        groups=groups,
                    )
                )
                continue
            measured = primary.get(entry.hero)
            verdict = _measured_verdict(measured.tier) if measured else entry.verdict
            word, css, rank = _badge(verdict, entry.direction)
            icon_for = partial(art.ability_icon, entry.hero)
            groups = _row_groups(entry.rows, icon_for)
            if not groups:
                groups = _fallback_groups(
                    entry.hero, EntityType.hero, patch, icon_for
                )
            tier_chip = None
            if (
                not tiers
                and entry.tier_before != entry.tier_after
                and entry.tier_before != "?"
                and entry.tier_after != "?"
            ):
                tier_chip = f"{entry.tier_before} → {entry.tier_after}"
            heroes.append(
                HeroCardView(
                    slug=slugify(entry.hero),
                    name=entry.hero,
                    initials=_initials(entry.hero),
                    portrait=art.hero_portrait(entry.hero),
                    verdict=verdict,
                    direction=entry.direction,
                    tier_stats=[
                        _tier_stat(band, band.heroes[entry.hero])
                        for band in (tiers.bands if tiers else [])
                        if entry.hero in band.heroes
                    ],
                    badge_word=word,
                    badge_class=css,
                    pool_rank=rank,
                    magnitude=entry.magnitude,
                    in_notes=entry.hero in direct,
                    board_group=_board_group(
                        entry.hero in direct, entry.change_kind, entry.direction
                    ),
                    chevrons=_CHEVRONS.get(
                        entry.change_size
                        if entry.change_kind != "none"
                        else entry.magnitude,
                        0,
                    ),
                    kind_word=_KIND_WORD.get(entry.change_kind, ""),
                    one_liner=entry.one_liner,
                    tier_chip=tier_chip,
                    tier_after=entry.tier_after,
                    tier_before=entry.tier_before,
                    groups=groups,
                    indirect_reasons=entry.indirect_reasons,
                    build_changes=entry.build_changes,
                )
            )
    heroes.sort(key=lambda h: (-h.chevrons, h.name))

    hero_groups = [
        HeroGroupView(
            key=key,
            label=label,
            glyph=glyph,
            heroes=[h for h in heroes if h.board_group == key],
        )
        for key, label, glyph in _HERO_GROUPS
    ]
    hero_groups = [g for g in hero_groups if g.heroes]
    by_name = {h.name: h for h in heroes}

    picker = [
        {
            "slug": h.slug,
            "name": h.name,
            "initials": h.initials,
            "portrait": h.portrait,
            "badge_word": h.badge_word,
            "badge_class": h.badge_class,
            "pool_rank": h.pool_rank,
        }
        for h in sorted(heroes, key=lambda h: h.name)
    ]

    item_groups: list[ItemGroupView] = []
    small_items: list[ItemCardView] = []
    if analysis.items:
        by_cat: dict[str, list[ItemCardView]] = {}
        for entry in analysis.items.items:
            groups = _row_groups(entry.rows, _no_icon)
            if not groups:
                groups = _fallback_groups(
                    entry.item, EntityType.item, patch, _no_icon
                )
            category = art.item_category(entry.item)
            if category not in _CATEGORY_ORDER:
                category = "other"
            affected = [
                AffectedHeroView(
                    slug=by_name[a.hero].slug,
                    name=a.hero,
                    initials=by_name[a.hero].initials,
                    portrait=by_name[a.hero].portrait,
                    effect=a.effect,
                    why=a.why,
                )
                for a in entry.affected_heroes
                if a.hero in by_name
            ]
            card = ItemCardView(
                slug=slugify(entry.item),
                name=entry.item,
                initials=_initials(entry.item),
                direction=entry.direction,
                magnitude=entry.magnitude,
                category=category,
                icon=art.item_icon(entry.item),
                summary=entry.summary,
                build_shift=entry.build_shift,
                groups=groups,
                chevrons=_CHEVRONS.get(entry.magnitude, 0),
                affected=affected,
                hero_slugs=" ".join(a.slug for a in affected),
            )
            if entry.magnitude == "minor":
                small_items.append(card)
            else:
                by_cat.setdefault(category, []).append(card)
        for category in _CATEGORY_ORDER:
            cards = by_cat.get(category)
            if cards:
                cards.sort(
                    key=lambda c: (_MAGNITUDE_RANK.get(c.magnitude, 4), c.name)
                )
                item_groups.append(
                    ItemGroupView(category=category, items=cards)
                )
    small_items.sort(key=lambda c: c.name)

    systems: list[SystemView] = list(non_hero_systems)
    tempo = None
    archetypes: list[ArchetypeView] = []
    if analysis.systems:
        systems += [
            SystemView(
                slug=slugify(s.system),
                name=s.system,
                change_summary=s.change_summary,
                effect_on_play=s.effect_on_play,
                magnitude=s.magnitude,
                chevrons=_CHEVRONS.get(s.magnitude, 0),
                deltas=_driving_deltas(s.driving_changes),
                lines=s.driving_changes,
            )
            for s in analysis.systems.systems_changed
        ]
        shift = analysis.systems.tempo_shift
        label, sign = _TEMPO[shift.direction]
        archetypes = [
            ArchetypeView(
                name=a.archetype,
                direction=a.direction,
                chevrons=_CHEVRONS.get(a.magnitude, 0),
                why=a.why,
            )
            for a in sorted(
                analysis.systems.archetype_effects,
                key=lambda a: (
                    _DIRECTION_RANK.get(a.direction, 1),
                    _MAGNITUDE_RANK.get(a.magnitude, 4),
                ),
            )
            if a.direction != "neutral"
        ]
        tempo = TempoView(
            label=label,
            position=round(50 + sign * 45 * max(shift.confidence, 0.2)),
            why=shift.why,
        )
    systems.sort(key=lambda s: _MAGNITUDE_RANK.get(s.magnitude, 4))
    small_systems = [s for s in systems if s.magnitude in ("minor", "none")]
    systems = [s for s in systems if s.magnitude not in ("minor", "none")]

    return PatchPageModel(
        patch_id=analysis.patch_id,
        title=analysis.patch_title or patch.title,
        date_display=f"{patch.date:%b} {patch.date.day}, {patch.date:%Y}",
        url=patch.url,
        headline=analysis.synthesis.headline,
        patch_size=analysis.synthesis.patch_size,
        size_why=analysis.synthesis.size_why,
        hero_groups=hero_groups,
        tempo=tempo,
        archetypes=archetypes,
        heroes=heroes,
        biggest_changes=_big_changes(
            analysis, heroes, item_groups, small_items, systems, small_systems
        ),
        tier_boards=_tier_boards(heroes, tiers, reset_on),
        picker=picker,
        item_groups=item_groups,
        small_items=small_items,
        systems=systems,
        small_systems=small_systems,
        game_plan=analysis.synthesis.meta_thesis.new,
        counts_line=_counts_line(
            heroes, item_groups, small_items, systems, small_systems
        ),
    )
