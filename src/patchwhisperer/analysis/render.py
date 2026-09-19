from pydantic import BaseModel

from patchwhisperer.analysis.schemas import AnalysisBundle

DISCORD_LIMIT = 1900


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


class DiscordPost(BaseModel):
    tldr: str
    thread: list[str]


def _split_section(text: str, limit: int = DISCORD_LIMIT) -> list[str]:
    if len(text) <= limit:
        return [text]
    chunks, cur = [], ""
    for para in text.split("\n\n"):
        if cur and len(cur) + len(para) + 2 > limit:
            chunks.append(cur)
            cur = para
        else:
            cur = f"{cur}\n\n{para}" if cur else para
    if cur:
        chunks.append(cur)
    # last resort: hard-wrap paragraphs that still exceed the limit
    out = []
    for c in chunks:
        while len(c) > limit:
            out.append(c[:limit])
            c = c[limit:]
        out.append(c)
    return out


def render_discord(bundle: AnalysisBundle) -> DiscordPost:
    s = bundle.synthesis
    tldr_lines = [
        f"**[{s.patch_size.upper()}]** {s.headline}",
        s.size_why,
        "",
        f"**Meta:** {s.meta_thesis.new}",
    ]
    if bundle.pool:
        for v in bundle.pool.verdicts:
            tldr_lines.append(f"{v.hero} — {v.verdict.upper()} — {v.one_liner}")
    tldr = "\n".join(tldr_lines)

    full = render_markdown(bundle)
    sections = full.split("\n\n## ")
    # first chunk is the TL;DR block (already sent as tldr); thread = the rest
    rest = ["## " + sec for sec in sections[1:]]
    thread: list[str] = []
    cur = ""
    for sec in rest:
        if cur and len(cur) + len(sec) + 2 > DISCORD_LIMIT:
            thread.extend(_split_section(cur))
            cur = sec
        else:
            cur = f"{cur}\n\n{sec}" if cur else sec
    if cur:
        thread.extend(_split_section(cur))
    return DiscordPost(tldr=tldr[:DISCORD_LIMIT], thread=thread)
