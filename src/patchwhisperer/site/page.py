"""Pure page-model construction: analysis + patch + art -> template-ready views."""

from functools import partial

from pydantic import BaseModel

from patchwhisperer.analysis.schemas import AnalysisBundle, ChangeRow
from patchwhisperer.kb.store import slugify
from patchwhisperer.parse.models import Direction, EntityType, Patch

_MAGNITUDE_RANK = {"major": 0, "moderate": 1, "minor": 2, "none": 3}
_VERDICT_RANK = {"keep": 0, "watch": 1, "bench": 2}
_DIRECTION_RANK = {"up": 0, "neutral": 1, "down": 2}
_DIRECTION_EFFECT = {
    Direction.buff: "good",
    Direction.nerf: "bad",
}
_CATEGORY_ORDER = ["weapon", "spirit", "vitality", "other"]


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


class ItemGroupView(BaseModel):
    category: str
    items: list[ItemCardView] = []


class SystemView(BaseModel):
    name: str
    change_summary: str = ""
    effect_on_play: str = ""
    magnitude: str = "minor"


class ChipView(BaseModel):
    key: str
    label: str


class PatchPageModel(BaseModel):
    patch_id: str
    title: str
    date_display: str
    url: str
    headline: str
    patch_size: str
    size_why: str = ""
    chips: list[ChipView] = []
    heroes: list[HeroCardView] = []
    picker: list[dict] = []  # plain dicts so Jinja's tojson can serialize safely
    item_groups: list[ItemGroupView] = []
    systems: list[SystemView] = []
    what_to_watch: list[str] = []


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
                label=change.field or change.ability or "Note",
                text=change.raw,
                effect=_DIRECTION_EFFECT.get(change.direction, "neutral"),
            )
        )
    return groups


def build_page_model(analysis: AnalysisBundle, patch: Patch, art) -> PatchPageModel:
    heroes: list[HeroCardView] = []
    if analysis.heroes:
        for entry in analysis.heroes.heroes:
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
                    in_notes=entry.in_notes,
                    one_liner=entry.one_liner,
                    tier_chip=tier_chip,
                    groups=groups,
                    indirect_reasons=entry.indirect_reasons,
                    build_changes=entry.build_changes,
                )
            )
    heroes.sort(key=lambda h: (_MAGNITUDE_RANK.get(h.magnitude, 4), h.name))

    chips = [ChipView(key="all", label="All")]
    for verdict in ("keep", "watch", "bench"):
        if any(h.verdict == verdict for h in heroes):
            chips.append(ChipView(key=verdict, label=verdict.capitalize()))
    if any(h.direction == "up" for h in heroes):
        chips.append(ChipView(key="up", label="Buffed"))
    if any(h.direction == "down" for h in heroes):
        chips.append(ChipView(key="down", label="Nerfed"))

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

    systems = []
    if analysis.systems:
        systems = [
            SystemView(
                name=s.system,
                change_summary=s.change_summary,
                effect_on_play=s.effect_on_play,
                magnitude=s.magnitude,
            )
            for s in analysis.systems.systems_changed
        ]

    return PatchPageModel(
        patch_id=analysis.patch_id,
        title=analysis.patch_title or patch.title,
        date_display=f"{patch.date:%b} {patch.date.day}, {patch.date:%Y}",
        url=patch.url,
        headline=analysis.synthesis.headline,
        patch_size=analysis.synthesis.patch_size,
        size_why=analysis.synthesis.size_why,
        chips=chips,
        heroes=heroes,
        picker=picker,
        item_groups=item_groups,
        systems=systems,
        what_to_watch=analysis.synthesis.what_to_watch,
    )
