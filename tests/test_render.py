import json

from conftest import FIXTURES

from patchwhisperer.analysis.render import (
    DISCORD_LIMIT,
    render_discord,
    render_markdown,
)
from patchwhisperer.analysis.schemas import (
    AnalysisBundle,
    ItemAnalysis,
    KBUpdate,
    PoolVerdicts,
    Synthesis,
)


def _bundle(**kw) -> AnalysisBundle:
    base = {
        "patch_id": "2026-09-16-x",
        "patch_title": "Minor Update - 09-16-2026",
        "synthesis": Synthesis.model_validate(
            json.loads((FIXTURES / "llm" / "stage4.json").read_text())
        ),
    }
    base.update(kw)
    return AnalysisBundle(**base)


def test_markdown_sections():
    bundle = _bundle(
        pool=PoolVerdicts.model_validate(
            json.loads((FIXTURES / "llm" / "stage5.json").read_text())
        ),
        items=ItemAnalysis.model_validate(
            json.loads((FIXTURES / "llm" / "stage2.json").read_text())
        ),
        kb_update=KBUpdate.model_validate(
            json.loads((FIXTURES / "llm" / "stage6.json").read_text())
        ),
    )
    md = render_markdown(bundle)
    assert "[SIGNIFICANT]" in md
    assert "Wraith — WATCH" in md
    assert "Warden — KEEP" in md
    assert "## Winners" in md and "(indirect)" in md
    assert "55%" in md  # non-obvious call confidence
    assert "## Notable items" in md
    assert "## What to watch" in md
    assert "## KB changes" in md


def test_discord_split_under_limit():
    big_call = "## What to watch\n\n" + "\n\n".join(
        f"- watch item {i} " + "x" * 300 for i in range(30)
    )
    s = Synthesis(
        patch_size="minor",
        size_why="s",
        headline="h",
        what_to_watch=[big_call],
    )
    bundle = _bundle(synthesis=s)
    post = render_discord(bundle)
    assert len(post.tldr) <= DISCORD_LIMIT
    assert post.thread
    assert all(len(m) <= DISCORD_LIMIT for m in post.thread)
