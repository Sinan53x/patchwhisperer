from patchwhisperer.analysis.schemas import AnalysisBundle, NewHeroCard
from patchwhisperer.kb.schema import HeroState

CARD_LIMIT = 1900


def render_markdown(bundle: AnalysisBundle) -> str:
    s = bundle.synthesis
    parts = []

    badge = s.patch_size.upper()
    tldr = [f"**[{badge}]** {s.headline}", "", s.size_why]
    parts.append("\n".join(tldr))

    mt = s.meta_thesis
    parts.append(
        "## Meta thesis\n\n"
        f"**Before:** {mt.previous}\n\n"
        f"**Now:** {mt.new}\n\n"
        f"*{mt.relationship.capitalize()}* — {mt.why}"
    )

    if bundle.pool and bundle.pool.verdicts:
        lines = ["## Your pool"]
        for v in bundle.pool.verdicts:
            lines.append(f"\n### {v.hero} — {v.verdict.upper()}")
            lines.append(v.one_liner)
            lines.append(f"- **Direct:** {v.direct}")
            lines.append(f"- **Indirect:** {v.indirect}")
            if v.build_adjustments:
                lines.append("- **Build:** " + "; ".join(v.build_adjustments))
        parts.append("\n".join(lines))

    def _movers(title, movers):
        lines = [f"## {title}"]
        for m in movers:
            tag = " (indirect)" if m.indirect else ""
            lines.append(f"- **{m.hero}**{tag}: {m.why}")
        return "\n".join(lines)

    if s.winners:
        parts.append(_movers("Winners", s.winners))
    if s.losers:
        parts.append(_movers("Losers", s.losers))

    if s.non_obvious_calls:
        lines = ["## Non-obvious calls"]
        for c in s.non_obvious_calls:
            lines.append(f"- {c.claim} ({c.confidence:.0%}) — {c.why}")
        parts.append("\n".join(lines))

    if bundle.items and bundle.items.items:
        pool_heroes = {v.hero for v in bundle.pool.verdicts} if bundle.pool else set()
        mag_rank = {"major": 0, "moderate": 1, "minor": 2}
        ordered = sorted(bundle.items.items, key=lambda i: mag_rank.get(i.magnitude, 3))
        top = ordered[:6]
        extra = [
            i
            for i in ordered[6:]
            if any(a.hero in pool_heroes for a in i.affected_heroes)
        ]
        lines = ["## Notable items"]
        for i in top + extra:
            lines.append(f"- **{i.item}** ({i.direction}, {i.magnitude}): {i.summary}")
        if bundle.items.notable_item_stories:
            lines.append("")
            lines += [f"- {st}" for st in bundle.items.notable_item_stories]
        parts.append("\n".join(lines))

    if s.what_to_watch or s.uncertainties:
        lines = ["## What to watch"]
        lines += [f"- {w}" for w in s.what_to_watch]
        lines += [f"- _(unsure)_ {u}" for u in s.uncertainties]
        parts.append("\n".join(lines))

    if bundle.kb_update and bundle.kb_update.change_log:
        lines = ["## KB changes"]
        lines += [f"- {c}" for c in bundle.kb_update.change_log]
        parts.append("\n".join(lines))

    return "\n\n".join(parts)


def render_hero_card(name: str, card: NewHeroCard, state: HeroState) -> str:
    def build(watch_n: int, threat_n: int) -> str:
        lines = [
            (
                f"**New hero: {name}** — provisional **{card.provisional_tier}** "
                f"({card.confidence:.0%})"
            ),
            card.headline,
            "",
            "**Kit**",
        ]
        lines += [f"- {b}" for b in card.kit_read]
        if card.meta_fit:
            lines += ["", f"**Meta fit** {card.meta_fit}"]
        if card.threatens:
            lines.append("**Threatens**")
            lines += [f"- {t}" for t in card.threatens[:threat_n]]
        if card.threatened_by:
            lines.append("**Threatened by**")
            lines += [f"- {t}" for t in card.threatened_by[:threat_n]]
        if card.build_read:
            lines.append(f"**Build** {card.build_read}")
        if card.what_to_watch:
            lines.append("**Watch before the 7-day check-in**")
            lines += [f"- {w}" for w in card.what_to_watch[:watch_n]]
        lines.append(
            "_Day-0 read from the kit and early data; a data-driven "
            "re-evaluation posts automatically after 7 days._"
        )
        return "\n".join(lines)

    for watch_n, threat_n in (
        (len(card.what_to_watch), max(len(card.threatens), len(card.threatened_by))),
        (2, 3),
        (1, 2),
        (0, 1),
    ):
        text = build(watch_n, threat_n)
        if len(text) <= CARD_LIMIT:
            return text
    return text[: CARD_LIMIT - 1] + "…"


def render_checkin_card(
    name: str, before: HeroState, after: HeroState, stats: dict | None
) -> str:
    lines = [
        (
            f"**7-day check-in: {name}** — tier {before.tier} -> {after.tier} "
            f"({after.trend})"
        ),
    ]
    if stats:
        lines.append(
            f"WR {stats['win_rate'] * 100:.1f}% | PR "
            f"{stats['pick_rate'] * 100:.1f}% | matches {stats['matches']}"
        )
    else:
        lines.append("(no ranked data)")
    if after.why:
        lines.append(after.why)
    for b in after.builds:
        items = ", ".join(b.core_items) or "?"
        lines.append(f"- {b.name} ({b.popularity}): {items}")
    if after.matchups.loses_to:
        lines.append(f"loses to: {', '.join(after.matchups.loses_to[:3])}")
    text = "\n".join(lines)
    if len(text) > CARD_LIMIT:
        text = text[: CARD_LIMIT - 1] + "…"
    return text
