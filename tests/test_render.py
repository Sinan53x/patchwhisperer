import json
from pathlib import Path

from conftest import FIXTURES

from patchwhisperer.analysis.render import render_markdown
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


def test_demo_bundle_markdown_covers_pool():
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
        "stage4": "stage4_synthesis",
        "stage5": "stage5_pool",
    }.items():
        canned[stage_marker(name)] = [(demo / f"{stem}.json").read_text()]
    import shutil

    kb_dir = Path(tempfile.mkdtemp()) / "kb"
    shutil.copytree(demo / "kb", kb_dir)
    kb_store = KBStore(kb_dir)
    # stage 3 runs in batches: split the recorded analysis to match
    from patchwhisperer import config
    from patchwhisperer.analysis import context as ctx

    s3_heroes = {
        h["hero"]: h
        for h in json.loads((demo / "stage3.json").read_text())["heroes"]
    }
    expected = ctx.expected_hero_names(kb_store, ctx.hero_changes(patch))
    canned[stage_marker("stage3_heroes")] = [
        json.dumps(
            {
                "heroes": [
                    s3_heroes[n]
                    for n in expected[i : i + config.STAGE3_HERO_BATCH]
                    if n in s3_heroes
                ]
            }
        )
        for i in range(0, len(expected), config.STAGE3_HERO_BATCH)
    ]
    bundle = run_analysis(
        patch, kb_store, {}, pool, ReplayLLMClient(canned),
        update_kb=False,
    )
    md = render_markdown(bundle)
    assert "Billy" in md
