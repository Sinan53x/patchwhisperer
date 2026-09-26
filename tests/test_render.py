import json
from pathlib import Path

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


def test_tldr_overflow_uses_extra_chunks():
    from patchwhisperer.analysis.schemas import PoolVerdict

    verdicts = PoolVerdicts(
        verdicts=[
            PoolVerdict(hero=f"Hero{i}", verdict="watch", one_liner="y" * 180)
            for i in range(13)
        ]
    )
    s = Synthesis(
        patch_size="major",
        size_why="s",
        headline="h",
        meta_thesis={"new": "meta " * 100},
    )
    bundle = _bundle(synthesis=s, pool=verdicts)
    post = render_discord(bundle)
    assert len(post.tldr) <= DISCORD_LIMIT
    assert post.tldr_extra
    chunks = [post.tldr] + post.tldr_extra
    assert all(len(c) <= DISCORD_LIMIT for c in chunks)
    joined = "\n".join(chunks)
    for i in range(13):
        assert f"Hero{i} — WATCH" in joined
    # no line was split: every line survives intact
    assert all(len(line) <= DISCORD_LIMIT for line in joined.split("\n"))


def test_pack_splits_on_line_boundaries():
    from patchwhisperer.analysis.render import _pack

    bullets = [f"- bullet {i}: " + "x" * 60 for i in range(60)]
    text = "\n".join(bullets)  # one paragraph of single-newline lines
    assert len(text) > DISCORD_LIMIT
    chunks = _pack(text)
    assert all(len(c) <= DISCORD_LIMIT for c in chunks)
    joined = "\n".join(chunks)
    for b in bullets:
        assert b in joined


def test_pack_long_line_splits_on_words():
    from patchwhisperer.analysis.render import _pack

    words = [f"word{i}" for i in range(500)]
    line = " ".join(words)
    assert len(line) > DISCORD_LIMIT
    chunks = _pack(line)
    assert all(len(c) <= DISCORD_LIMIT for c in chunks)
    joined = " ".join(chunks)
    for w in words:
        assert w in joined.split(" ")


def test_pack_hard_cut_only_for_giant_token():
    from patchwhisperer.analysis.render import _pack

    chunks = _pack("x" * (DISCORD_LIMIT + 10))
    assert chunks == ["x" * DISCORD_LIMIT, "x" * 10]


def test_demo_bundle_tldr_covers_pool():
    import tempfile

    from conftest import load_post

    from patchwhisperer.analysis.llm import ReplayLLMClient, stage_marker
    from patchwhisperer.analysis.pipeline import run_analysis
    from patchwhisperer.kb.store import KBStore
    from patchwhisperer.parse.entities import EntityIndex
    from patchwhisperer.parse.patch_parser import parse_patch

    demo = FIXTURES.parent.parent / "demo" / "2026-09-16"
    if not demo.exists():
        import pytest

        pytest.skip("demo fixtures not present")
    post = load_post("09-16-2026")
    assets = demo / "assets"
    index = EntityIndex(
        json.loads((assets / "heroes.json").read_text()),
        json.loads((assets / "items.json").read_text()),
        {
            int(k): v
            for k, v in json.loads((assets / "abilities.json").read_text()).items()
        },
    )
    patch = parse_patch(post, index)
    pool = [
        p.strip() for p in (demo / "pool.txt").read_text().splitlines() if p.strip()
    ]
    canned = {}
    for stem, name in {
        "stage1": "stage1_systems",
        "stage2": "stage2_items",
        "stage3": "stage3_heroes",
        "stage4": "stage4_synthesis",
        "stage5": "stage5_pool",
    }.items():
        canned[stage_marker(name)] = [(demo / f"{stem}.json").read_text()]
    import shutil

    kb_dir = Path(tempfile.mkdtemp()) / "kb"
    shutil.copytree(demo / "kb", kb_dir)
    bundle = run_analysis(
        patch, KBStore(kb_dir), {}, pool, ReplayLLMClient(canned),
        update_kb=False,
    )
    post_render = render_discord(bundle)
    chunks = [post_render.tldr] + post_render.tldr_extra
    assert all(len(c) <= DISCORD_LIMIT for c in chunks)
    assert "Billy" in "\n".join(chunks)


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
