import json
import shutil
from datetime import UTC, datetime

import pytest
from conftest import FIXTURES, load_post

from patchwhisperer.analysis.llm import (
    FakeLLMClient,
    ReplayLLMClient,
    stage_marker,
)
from patchwhisperer.analysis.pipeline import (
    apply_kb_update,
    guard_rows,
    run_analysis,
    uncovered_heroes,
)
from patchwhisperer.analysis.schemas import (
    ChangeRow,
    HeroAnalysis,
    HeroEntry,
    KBUpdate,
)
from patchwhisperer.kb.schema import HeroState
from patchwhisperer.kb.store import KBStore
from patchwhisperer.parse.models import Change, Direction, EntityType, Patch
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
        "stage6h": "stage6_kb_heroes",
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
    for n in (1, 2, 4, 5, 6):
        assert (pdir / f"stage{n}.json").exists()
        assert (pdir / f"stage{n}.prompt.md").exists()
    # stage 3 runs in batches; the merged analysis is still stage3.json
    assert (pdir / "stage3.json").exists()
    assert (pdir / "stage3b1.prompt.md").exists()
    assert (pdir / "stage3b1.json").exists()
    assert (pdir / "analysis.json").exists()
    pj = json.loads((pdir / "patch.json").read_text())
    assert "raw_bbcode" not in pj
    assert pj["gid"] == patch.gid


def test_kb_update_hero_batches(kb, fake_llm, entity_index, monkeypatch):
    from patchwhisperer import config

    monkeypatch.setattr(config, "STAGE6_HERO_BATCH", 1)
    patch = parse_patch(load_post("09-16-2026"), entity_index)
    bundle = run_analysis(patch, kb, {}, [], fake_llm, update_kb=True)
    hero_marker = stage_marker("stage6_kb_heroes")
    # stage3 fixture has 2 movers -> 2 batch calls at batch size 1
    assert fake_llm.calls.count(hero_marker) == 2
    pdir = kb.patch_dir(bundle.patch_id)
    assert (pdir / "stage6h1.json").exists()
    assert (pdir / "stage6h2.json").exists()
    assert (pdir / "stage6h1.prompt.md").exists()
    upd = bundle.kb_update
    assert "Wraith" in upd.hero_updates
    assert upd.meta_md
    assert upd.item_updates
    assert "Wraith: tier update (batch)" in upd.change_log


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


def test_invalid_item_tier_dropped(kb, caplog):
    before_tier = kb.load_items()["Veil Walker"].tier
    update = KBUpdate(item_updates={"Veil Walker": {"tier": "B", "role": "new role"}})
    with caplog.at_level("WARNING"):
        apply_kb_update(kb, update)
    items = kb.load_items()
    assert items["Veil Walker"].tier == before_tier
    assert items["Veil Walker"].role == "new role"
    assert "dropping invalid" in caplog.text


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
        SeedKB,
        Synthesis,
    )

    with _pytest.raises(ValidationError):
        DistilledSource()  # empty hero_claims
    with _pytest.raises(ValidationError):
        SeedKB()  # <30 heroes
    with _pytest.raises(ValidationError):
        Synthesis()  # empty headline
    with _pytest.raises(ValidationError):
        KBUpdate()  # all empty
    KBUpdate(meta_md="x")  # ok


# -- stage 3 batching, coverage gate, row guard ------------------------------


def _small_kb(tmp_path):
    root = tmp_path / "kb"
    root.mkdir()
    store = KBStore(root)
    store.save_heroes(
        {n: HeroState(name=n) for n in ("Wraith", "Warden", "Abrams")}
    )
    return store


def _hero_patch() -> Patch:
    """3 heroes x 3 changes; large enough to not classify as a hotfix."""
    changes = []
    for hero in ("Wraith", "Warden", "Abrams"):
        for i in range(3):
            changes.append(
                Change(
                    section="Heroes",
                    entity_type=EntityType.hero,
                    entity_name=hero,
                    raw=f"{hero}: stat {i} reduced from 10 to 5",
                    direction=Direction.nerf,
                    resolved=True,
                )
            )
    return Patch(
        gid="t1",
        title="test patch",
        date=datetime(2026, 11, 1, tzinfo=UTC),
        url="",
        author="",
        raw_bbcode="",
        changes=changes,
    )


def _hero_entry(name: str, **kw) -> dict:
    return {"hero": name, "one_liner": "x", "verdict": "keep", **kw}


def _llm_for(stage3_payloads: list[dict]) -> ReplayLLMClient:
    return ReplayLLMClient(
        {
            stage_marker("stage1_systems"): ["{}"],
            stage_marker("stage3_heroes"): [
                json.dumps(p) for p in stage3_payloads
            ],
            stage_marker("stage4_synthesis"): ['{"headline": "h"}'],
        }
    )


def test_stage3_batches_write_merged(tmp_path, monkeypatch):
    from patchwhisperer import config

    monkeypatch.setattr(config, "STAGE3_HERO_BATCH", 2)
    kb = _small_kb(tmp_path)
    payloads = [
        {"heroes": [_hero_entry("Wraith"), _hero_entry("Warden")]},
        {"heroes": [_hero_entry("Abrams")]},
    ]
    llm = _llm_for(payloads)
    bundle = run_analysis(
        _hero_patch(), kb, {}, [], llm, update_kb=False
    )
    assert [h.hero for h in bundle.heroes.heroes] == [
        "Wraith",
        "Warden",
        "Abrams",
    ]
    pdir = kb.patch_dir(bundle.patch_id)
    for f in ("stage3b1.json", "stage3b2.json", "stage3.json"):
        assert (pdir / f).exists()
    prompt = (pdir / "stage3b1.prompt.md").read_text()
    assert "Wraith, Warden" in prompt
    assert "Abrams" not in prompt.split("## Heroes to analyze")[-1].split(
        "##"
    )[0]


def test_stage3_retry_covers_omitted(tmp_path, monkeypatch):
    from patchwhisperer import config

    monkeypatch.setattr(config, "STAGE3_HERO_BATCH", 2)
    kb = _small_kb(tmp_path)
    payloads = [
        {"heroes": [_hero_entry("Wraith")]},  # batch 1 omits Warden
        {"heroes": [_hero_entry("Abrams")]},
        {"heroes": [_hero_entry("Warden")]},  # retry supplies it
    ]
    llm = _llm_for(payloads)
    bundle = run_analysis(
        _hero_patch(), kb, {}, [], llm, update_kb=False
    )
    assert {h.hero for h in bundle.heroes.heroes} == {
        "Wraith",
        "Warden",
        "Abrams",
    }
    assert (kb.patch_dir(bundle.patch_id) / "stage3r.json").exists()
    assert llm.calls.count(stage_marker("stage3_heroes")) == 3


def test_stage3_uncovered_raises(tmp_path):
    kb = _small_kb(tmp_path)
    payloads = [
        {"heroes": [_hero_entry("Wraith"), _hero_entry("Abrams")]},
        {"heroes": [_hero_entry("Wraith")]},  # retry still no Warden
    ]
    llm = _llm_for(payloads)
    with pytest.raises(RuntimeError, match="did not cover"):
        run_analysis(_hero_patch(), kb, {}, [], llm, update_kb=False)
    assert llm.calls.count(stage_marker("stage3_heroes")) == 2


def test_uncovered_heroes_gate():
    expected = ["A", "B", "C"]
    changed = {"B"}
    a = HeroAnalysis(
        heroes=[
            HeroEntry(hero="A"),
            HeroEntry(hero="A"),  # duplicate ignored
            HeroEntry(hero="Ghost"),  # outside expected, ignored
            HeroEntry(hero="B", one_liner="", verdict=None),  # incomplete
        ]
    )
    assert uncovered_heroes(a, expected, changed) == ["B", "C"]
    b = HeroAnalysis(
        heroes=[
            HeroEntry(hero="A"),
            HeroEntry(hero="B", one_liner="x", verdict="watch"),
            HeroEntry(hero="C"),
        ]
    )
    assert uncovered_heroes(b, expected, changed) == []


def test_guard_rows_keeps_matching_numbers():
    raw = ["Shadow Weave: Cooldown reduced from 45s to 37s"]
    rows = [
        ChangeRow(label="Cooldown", old="45s", new="37s", effect="good")
    ]
    assert guard_rows(rows, raw) == rows


def test_guard_rows_signed_token_matches():
    raw = ["Traveler: T3 reduced from -65s cooldown to -90s"]
    rows = [ChangeRow(label="T3", old="-65s", new="-90s", effect="bad")]
    assert guard_rows(rows, raw) == rows


def test_guard_rows_drops_invented_number(caplog):
    raw = ["Shadow Weave: Cooldown reduced from 45s to 37s"]
    good = ChangeRow(label="Cooldown", old="45s", new="37s", effect="good")
    bad = ChangeRow(label="Duration", old="10s", new="99s", effect="bad")
    with caplog.at_level("WARNING"):
        out = guard_rows([good, bad], raw)
    assert out == [good]
    assert "not in the notes" in caplog.text


def test_guard_rows_all_dropped_falls_back_to_raw():
    raw = ["Shadow Weave: Cooldown reduced from 45s to 37s"]
    bad = ChangeRow(label="Duration", old="10s", new="99s", effect="bad")
    out = guard_rows([bad], raw)
    assert out == [ChangeRow(label="Change", text=raw[0])]


def test_pool_verdict_matches_stage3(tmp_path):
    kb = _small_kb(tmp_path)
    canned = {
        stage_marker("stage1_systems"): ["{}"],
        stage_marker("stage3_heroes"): [
            json.dumps(
                {
                    "heroes": [
                        _hero_entry("Wraith", verdict="bench"),
                        _hero_entry("Warden"),
                        _hero_entry("Abrams"),
                    ]
                }
            )
        ],
        stage_marker("stage4_synthesis"): ['{"headline": "h"}'],
        stage_marker("stage5_pool"): [
            json.dumps(
                {
                    "verdicts": [
                        {"hero": "Wraith", "verdict": "keep", "one_liner": "x"}
                    ]
                }
            )
        ],
    }
    bundle = run_analysis(
        _hero_patch(),
        kb,
        {},
        ["Wraith"],
        ReplayLLMClient(canned),
        update_kb=False,
    )
    assert bundle.pool.verdicts[0].verdict == "bench"


def test_guard_rows_rejects_number_that_is_only_a_substring_of_a_note_number():
    rows = [ChangeRow(label="Cooldown", old="5s", new="9s", effect="bad")]
    kept = guard_rows(rows, ["Cooldown increased from 15s to 19s"], owner="X")
    assert all(r.old != "5s" for r in kept)
