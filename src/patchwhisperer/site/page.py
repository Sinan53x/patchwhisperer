"""Pure page-model construction: analysis + patch + art -> template-ready views."""

import re
from functools import partial

from pydantic import BaseModel

from patchwhisperer.analysis.schemas import AnalysisBundle, ChangeRow
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
]
_KIND_WORD = {
    "buff": "Buffed",
    "nerf": "Nerfed",
    "rework": "Reworked",
    "adjusted": "Adjusted",
}
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


class WatchView(BaseModel):
    lead: str
    rest: str = ""


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
    picker: list[dict] = []  # plain dicts so Jinja's tojson can serialize safely
    item_groups: list[ItemGroupView] = []
    systems: list[SystemView] = []
    tempo: TempoView | None = None
    archetypes: list[ArchetypeView] = []
    what_to_watch: list[WatchView] = []


class ArchiveEntry(BaseModel):
    patch_id: str
    title: str
    date_display: str
    headline: str
    patch_size: str


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
        if change.entity_type != entity_type or change.entity_name != entity_name:
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


def _board_group(direct: bool, kind: str, direction: str) -> str | None:
    if direct:
        if kind != "none":
            return kind
        return {"up": "buff", "down": "nerf"}.get(direction, "adjusted")
    return "indirect" if direction != "neutral" else None


def _watch(line: str) -> WatchView:
    lead, sep, rest = line.partition(" — ")
    return WatchView(lead=lead, rest=rest if sep else "")


def build_page_model(analysis: AnalysisBundle, patch: Patch, art) -> PatchPageModel:
    heroes: list[HeroCardView] = []
    non_hero_systems: list[SystemView] = []
    direct = {c.entity_name for c in patch.changes if c.entity_type == EntityType.hero}
    not_heroes = {
        c.entity_name for c in patch.changes if c.entity_type == EntityType.unknown
    } - direct
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
            word, css, rank = _badge(entry.verdict, entry.direction)
            icon_for = partial(art.ability_icon, entry.hero)
            groups = _row_groups(entry.rows, icon_for)
            if not groups:
                groups = _fallback_groups(
                    entry.hero, EntityType.hero, patch, icon_for
                )
            tier_chip = None
            if (
                entry.tier_before != entry.tier_after
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
                    verdict=entry.verdict,
                    direction=entry.direction,
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
                icon=art.item_icon(entry.item),
                summary=entry.summary,
                build_shift=entry.build_shift,
                groups=groups,
                chevrons=_CHEVRONS.get(entry.magnitude, 0),
                affected=affected,
                hero_slugs=" ".join(a.slug for a in affected),
            )
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
        tempo = TempoView(
            label=label,
            position=round(50 + sign * 45 * max(shift.confidence, 0.2)),
            why=shift.why,
        )
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
    systems.sort(key=lambda s: _MAGNITUDE_RANK.get(s.magnitude, 4))

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
        picker=picker,
        item_groups=item_groups,
        systems=systems,
        what_to_watch=[_watch(w) for w in analysis.synthesis.what_to_watch],
    )
