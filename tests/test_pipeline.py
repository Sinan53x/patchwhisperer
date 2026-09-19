import json
import shutil

import pytest
from conftest import FIXTURES, load_post

from patchwhisperer.analysis.llm import FakeLLMClient, stage_marker
from patchwhisperer.analysis.pipeline import apply_kb_update, run_analysis
from patchwhisperer.analysis.schemas import KBUpdate
from patchwhisperer.kb.store import KBStore
from patchwhisperer.parse.patch_parser import parse_patch


@pytest.fixture
def kb(tmp_path):
    root = tmp_path / "kb"
    root.mkdir()
    shutil.copy("kb/heroes.yaml", root / "heroes.yaml")
    shutil.copy("kb/items.yaml", root / "items.yaml")
    shutil.copy("kb/meta.md", root / "meta.md")
    return KBStore(root)


@pytest.fixture
def fake_llm():
    llm_dir = FIXTURES / "llm"
    canned = {}
    names = {
        "stage1": "stage1_systems",
        "stage2": "stage2_items",
        "stage3": "stage3_heroes",
        "stage4": "stage4_synthesis",
        "stage5": "stage5_pool",
        "stage6": "stage6_kb_update",
    }
    for stem, prompt_name in names.items():
        canned[stage_marker(prompt_name)] = (llm_dir / f"{stem}.json").read_text()
    return FakeLLMClient(canned)


def test_full_run(kb, fake_llm, entity_index):
    patch = parse_patch(load_post("09-16-2026"), entity_index)
    bundle = run_analysis(patch, kb, {}, ["Wraith", "Warden"], fake_llm, update_kb=True)
    assert bundle.synthesis.patch_size == "significant"
    assert bundle.pool.verdicts[0].verdict == "watch"
    pdir = kb.patch_dir(bundle.patch_id)
    for n in (1, 2, 3, 4, 5, 6):
        assert (pdir / f"stage{n}.json").exists()
        assert (pdir / f"stage{n}.prompt.md").exists()
    assert (pdir / "analysis.json").exists()


def test_apply_kb_update(kb):
    update = KBUpdate.model_validate(
        json.loads((FIXTURES / "llm" / "stage6.json").read_text())
    )
    changed = apply_kb_update(kb, update)
    assert kb.heroes_path in changed
    heroes = kb.load_heroes()
    assert heroes["Wraith"].tier == "B"
    assert heroes["Wraith"].trend == "falling"
    items = kb.load_items()
    assert items["Veil Walker"].role == "invis defensive"
    meta = kb.load_meta()
    assert "Last patch: Minor Update - 09-16-2026" in meta


def test_invalid_tier_dropped(kb, caplog):
    before = kb.load_heroes()["Wraith"].tier
    update = KBUpdate(hero_updates={"Wraith": {"tier": "SS", "bogus": 1}})
    with caplog.at_level("WARNING"):
        apply_kb_update(kb, update)
    assert kb.load_heroes()["Wraith"].tier == before
    assert "invalid tier" in caplog.text


def test_hotfix_path(kb, fake_llm, entity_index):
    patch = parse_patch(load_post("08-22-2026"), entity_index)
    # 08-22 has 12 General changes -> not a hotfix by rule; craft a tiny one
    from patchwhisperer.parse.models import Change, Direction, EntityType, Patch

    small = Patch(
        gid="x",
        title="hotfix",
        date=patch.date,
        url="",
        author="",
        raw_bbcode="",
        changes=[
            Change(
                section="Heroes",
                entity_type=EntityType.hero,
                entity_name="Wraith",
                raw="Wraith: x",
                direction=Direction.nerf,
                resolved=True,
            )
        ],
    )
    assert small.is_hotfix()
    bundle = run_analysis(small, kb, {}, [], fake_llm, update_kb=True)
    assert bundle.systems is None
    assert bundle.kb_update is None
    pdir = kb.patch_dir(bundle.patch_id)
    assert (pdir / "stage4.json").exists()
    assert "(hotfix: stage skipped)" in (pdir / "stage4.prompt.md").read_text()


def test_schema_nonempty_validators():
    import pytest as _pytest
    from pydantic import ValidationError

    from patchwhisperer.analysis.schemas import (
        DistilledSource,
        HeroAnalysis,
        SeedKB,
        Synthesis,
    )

    with _pytest.raises(ValidationError):
        DistilledSource()  # empty hero_claims
    with _pytest.raises(ValidationError):
        SeedKB()  # <30 heroes
    with _pytest.raises(ValidationError):
        HeroAnalysis()  # <30 heroes
    with _pytest.raises(ValidationError):
        Synthesis()  # empty headline
    with _pytest.raises(ValidationError):
        KBUpdate()  # all empty
    KBUpdate(meta_md="x")  # ok
