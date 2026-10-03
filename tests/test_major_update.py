import json
import shutil
from datetime import UTC, date, datetime
from unittest.mock import MagicMock

import httpx
import pytest
import respx
from conftest import FIXTURES, load_post

from patchwhisperer.analysis import context as ctx
from patchwhisperer.analysis.digest import digest_to_changes, prepare_patch
from patchwhisperer.analysis.llm import FakeLLMClient, stage_marker
from patchwhisperer.analysis.pipeline import patch_id_of, run_analysis
from patchwhisperer.analysis.schemas import ContentDigest, DistilledSource
from patchwhisperer.bot import jobs, state
from patchwhisperer.bot.jobs import analyze_and_post
from patchwhisperer.kb.store import KBStore
from patchwhisperer.parse.models import Change, Direction, EntityType, Patch
from patchwhisperer.sources.steam_news import (
    PostKind,
    SteamPost,
    classify_post,
)
from patchwhisperer.sources.update_page import (
    fetch_update_page_text,
    update_page_slug,
)


@pytest.fixture
def kb(tmp_path):
    root = tmp_path / "kb"
    root.mkdir()
    for f in ("heroes.yaml", "items.yaml", "meta.md"):
        shutil.copy(f"kb/{f}", root / f)
    return KBStore(root)


@pytest.fixture
def fake_llm():
    llm_dir = FIXTURES / "llm"
    names = {
        "stage1": "stage1_systems",
        "stage2": "stage2_items",
        "stage3": "stage3_heroes",
        "stage4": "stage4_synthesis",
        "stage5": "stage5_pool",
        "stage6": "stage6_kb_update",
        "stage6h": "stage6_kb_heroes",
    }
    return FakeLLMClient(
        {
            stage_marker(v): (llm_dir / f"{k}.json").read_text()
            for k, v in names.items()
        }
    )


# -- classification ---------------------------------------------------------


def test_classify_balance():
    assert classify_post(load_post("09-16-2026")) == PostKind.balance


def test_classify_major():
    post = load_post("2026-09-29")
    assert classify_post(post) == PostKind.major
    assert post.kind == PostKind.major


def test_classify_hero_release():
    assert classify_post(load_post("2026-10-02")) == PostKind.hero_release


def test_classify_other():
    post = SteamPost(
        gid="x",
        title="Community Spotlight",
        date=datetime(2026, 10, 1, tzinfo=UTC),
        url="",
        author="",
        contents="[p]fan art roundup[/p]",
    )
    assert classify_post(post) == PostKind.other


# -- update page fetcher -----------------------------------------------------


def _mock_page(respx_mock, chunk_body: str):
    respx_mock.get("https://www.playdeadlock.com/testslug").mock(
        return_value=httpx.Response(
            200,
            text='<html><script src="https://www.playdeadlock.com/'
            'public/javascript/react/main.js?v=7"></script></html>',
        )
    )
    respx_mock.get(
        "https://www.playdeadlock.com/public/javascript/react/main.js"
    ).mock(
        return_value=httpx.Response(
            200, text='{"./testslug_english.json":[1234,99],"./main_english.json":[5,6]}'
        )
    )
    respx_mock.get(
        "https://www.playdeadlock.com/public/javascript/react/99.js"
    ).mock(return_value=httpx.Response(200, text=chunk_body))


@respx.mock
def test_fetch_update_page_text_json_parse():
    payload = json.dumps(
        {
            "K1": "Hello <span>brave</span> World &amp; more",
            "K2": "visitor’s welcome",
            "language": "en",
        }
    )
    _mock_page(respx, f"e.exports = JSON.parse('{payload}')")
    text = fetch_update_page_text("testslug")
    lines = text.splitlines()
    assert "K1: Hello brave World & more" in lines
    assert "K2: visitor’s welcome" in lines
    assert not any(line.startswith("language") for line in lines)


@respx.mock
def test_fetch_update_page_text_literal_object():
    _mock_page(respx, 'e.exports = {"A1": "value <br>one", "language": "en"};')
    assert fetch_update_page_text("testslug") == "A1: value one"


@respx.mock
def test_fetch_update_page_text_missing_chunk():
    respx.get("https://www.playdeadlock.com/testslug").mock(
        return_value=httpx.Response(200, text="<html>no scripts</html>")
    )
    with pytest.raises(RuntimeError, match="main.js"):
        fetch_update_page_text("testslug")


def test_update_page_slug():
    assert update_page_slug("see [url=https://www.playdeadlock.com/forums]f[/url]") is None
    assert (
        update_page_slug(
            "chat at playdeadlock.com/forums then "
            "[url=https://www.playdeadlock.com/cityneversleeps]x[/url]"
        )
        == "cityneversleeps"
    )
    assert update_page_slug("no links here") is None


# -- digest ------------------------------------------------------------------


def test_digest_to_changes(entity_index):
    digest = ContentDigest(
        summary="s",
        sections={
            "Map": ["Bell Tower: new objective on Chinatown roof"],
            "General": ["Respawn time: increased from 35s to 40s"],
            "Heroes": ["Rat King: new hero — summons rats", "Wraith: cards buffed"],
            "Items": ["Monster Rounds: bonus damage increased"],
        },
        new_heroes=["Rat King"],
    )
    changes = {c.raw: c for c in digest_to_changes(digest, entity_index)}
    m = changes["Bell Tower: new objective on Chinatown roof"]
    assert m.entity_type == EntityType.system and m.resolved and m.section == "Map"
    g = changes["Respawn time: increased from 35s to 40s"]
    assert g.entity_type == EntityType.system and g.entity_name == "Respawn time"
    rk = changes["Rat King: new hero — summons rats"]
    assert rk.direction == Direction.rework
    if entity_index.resolve("Rat King") is None:
        assert rk.entity_type == EntityType.unknown and not rk.resolved
        assert rk.entity_name == "Rat King"
    else:
        assert rk.entity_type == EntityType.hero and rk.resolved
    w = changes["Wraith: cards buffed"]
    assert w.entity_type == EntityType.hero and w.entity_name == "Wraith"
    it = changes["Monster Rounds: bonus damage increased"]
    assert it.entity_type == EntityType.item


def test_prepare_patch_major(kb, entity_index):
    canned = {
        stage_marker("stage0_digest"): {
            "summary": "a map overhaul",
            "sections": {"Map": ["Bell Tower: new objective"]},
            "new_heroes": ["Rat King"],
        }
    }
    llm = FakeLLMClient(canned)
    post = load_post("2026-09-29")
    patch = prepare_patch(post, entity_index, kb, llm, notes="manual notes")
    assert patch.kind == PostKind.major
    assert not patch.is_hotfix()
    assert patch.digest_summary == "a map overhaul"
    assert patch.new_heroes == ["Rat King"]
    map_changes = [c for c in patch.changes if c.section == "Map"]
    assert len(map_changes) == 1 and map_changes[0].resolved
    pdir = kb.patch_dir(patch_id_of(patch))
    assert (pdir / "stage0.json").exists()
    assert (pdir / "stage0.prompt.md").exists()
    assert (pdir / "update_page.txt").read_text() == "manual notes"


def _map_patch() -> Patch:
    return Patch(
        gid="m1",
        title="City Never Sleeps",
        date=datetime(2026, 9, 29, tzinfo=UTC),
        url="",
        author="",
        raw_bbcode="",
        kind=PostKind.major,
        changes=[
            Change(
                section="Map",
                entity_type=EntityType.system,
                entity_name="Bell Tower",
                raw="Bell Tower: new objective",
                direction=Direction.neutral,
                resolved=True,
            )
        ],
    )


def test_stage2_skipped_without_items(kb, fake_llm):
    bundle = run_analysis(_map_patch(), kb, {}, [], fake_llm, update_kb=False)
    assert stage_marker("stage2_items") not in fake_llm.calls
    assert bundle.items is not None and bundle.items.items == []
    assert bundle.synthesis.headline
    assert bundle.usage["stage_seconds"]["2"] == 0.0


def test_creator_sources_in_stage1_prompt(kb, fake_llm):
    bundle = run_analysis(
        _map_patch(),
        kb,
        {},
        [],
        fake_llm,
        update_kb=False,
        creator_sources="### vegas (2026-10-01)\nmap claim here",
    )
    prompt = (kb.patch_dir(bundle.patch_id) / "stage1.prompt.md").read_text()
    assert "map claim here" in prompt


def test_creator_sources_none_when_empty(kb, fake_llm):
    bundle = run_analysis(_map_patch(), kb, {}, [], fake_llm, update_kb=False)
    prompt = (kb.patch_dir(bundle.patch_id) / "stage1.prompt.md").read_text()
    assert "(none)" in prompt


# -- context.creator_sources_since -------------------------------------------


def test_creator_sources_since_filters_dates(tmp_path):
    src = tmp_path / "sources"
    src.mkdir()
    (src / "vegas-20261001-aaa.json").write_text(
        json.dumps(
            {
                "meta_thesis": "thesis",
                "map_claims": [
                    {"topic": "objectives", "claim": "bell rings", "numbers": "30s"}
                ],
                "patch_calls": {"size": "major", "headline": "map patch"},
                "hero_claims": [
                    {"hero": "Wraith", "tier": "A", "direction": "rising", "why": "x"}
                ],
            }
        )
    )
    (src / "old-20260901-bbb.json").write_text(json.dumps({"meta_thesis": "old"}))
    out = ctx.creator_sources_since(src, date(2026, 9, 15))
    assert "### vegas (2026-10-01)" in out
    assert "bell rings" in out
    assert "map patch" in out
    assert "Wraith" in out
    assert "old" not in out
    assert ctx.creator_sources_since(src, date(2026, 10, 2)) == ""


# -- jobs --------------------------------------------------------------------


def _job_env(tmp_path, kb, entity_index, monkeypatch, post):
    db = tmp_path / "s.db"
    state.init_db(db)
    monkeypatch.setattr(jobs, "fetch_post", lambda gid: post)
    api = MagicMock()
    api.hero_stats.return_value = []
    api.heroes.return_value = entity_index.heroes
    return {"db": db, "api": api, "kb": kb, "index": entity_index}


def test_analysis_json_guard_returns_none(tmp_path, kb, entity_index, monkeypatch):
    post = load_post("09-16-2026")
    env = _job_env(tmp_path, kb, entity_index, monkeypatch, post)
    patch_id = f"{post.date:%Y-%m-%d}-{post.gid}"
    pdir = kb.patch_dir(patch_id)
    (pdir / "analysis.json").write_text("{}")
    llm = FakeLLMClient({})
    result = analyze_and_post(
        post.gid,
        pool=[],
        llm=llm,
        kb=kb,
        index=entity_index,
        api=env["api"],
        db=env["db"],
        repo_root=tmp_path,
        commit_fn=MagicMock(),
        sync_fn=MagicMock(),
    )
    assert result is None
    assert llm.calls == []
    assert state.seen_get(post.gid, env["db"])["kind"] == "analyzed"


def test_hero_release_skips_pipeline(tmp_path, kb, entity_index, monkeypatch):
    post = load_post("2026-10-02")
    env = _job_env(tmp_path, kb, entity_index, monkeypatch, post)
    llm = FakeLLMClient({})
    hook = MagicMock()
    result = analyze_and_post(
        post.gid,
        pool=[],
        llm=llm,
        kb=kb,
        index=entity_index,
        api=env["api"],
        db=env["db"],
        repo_root=tmp_path,
        commit_fn=MagicMock(),
        sync_fn=MagicMock(),
        on_hero_release=hook,
    )
    assert result.kind == "hero_release"
    assert llm.calls == []
    hook.assert_called_once_with(post)
    assert state.seen_get(post.gid, env["db"])["kind"] == "hero_release"


# -- distill markdown writer ---------------------------------------------------


def test_source_md_includes_map_claims():
    from patchwhisperer.cli import _source_md

    result = DistilledSource.model_validate(
        {
            "meta_thesis": "t",
            "hero_claims": [{"hero": "Wraith", "tier": "A", "why": "w"}],
            "map_claims": [
                {"topic": "Haunts", "claim": "camps grouped", "numbers": "4 per camp"}
            ],
            "reasoning_patterns": ["r"],
        }
    )
    md = _source_md({"title": "v", "author": "vegas"}, "20261001", "vid", result)
    assert "## Map claims" in md
    assert "**Haunts**: camps grouped (4 per camp)" in md
