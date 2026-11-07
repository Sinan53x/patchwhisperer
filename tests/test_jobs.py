import json
import shutil
from unittest.mock import MagicMock

import pytest
from conftest import FIXTURES, load_post

from patchwhisperer.analysis.llm import FakeLLMClient, stage_marker
from patchwhisperer.bot import jobs, state
from patchwhisperer.bot.jobs import analyze_and_post
from patchwhisperer.kb.store import KBStore
from patchwhisperer.sources.steam_news import SteamPost


@pytest.fixture
def kb(tmp_path):
    root = tmp_path / "kb"
    root.mkdir()
    for f in ("heroes.yaml", "items.yaml", "meta.md"):
        shutil.copy(f"kb/{f}", root / f)
    return KBStore(root)


@pytest.fixture
def env(tmp_path, kb, entity_index, monkeypatch):
    db = tmp_path / "s.db"
    state.init_db(db)
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
    canned = {
        stage_marker(v): (llm_dir / f"{k}.json").read_text() for k, v in names.items()
    }
    llm = FakeLLMClient(canned)
    post = load_post("09-16-2026")
    monkeypatch.setattr(jobs, "fetch_post", lambda gid: post)
    api = MagicMock()
    api.hero_stats.return_value = []
    api.heroes.return_value = entity_index.heroes
    return {
        "db": db,
        "kb": kb,
        "llm": llm,
        "api": api,
        "index": entity_index,
        "post": post,
    }


def test_analyze_and_post(env, tmp_path):
    commit = MagicMock(return_value="abc123")
    sync = MagicMock(return_value=True)
    result = analyze_and_post(
        env["post"].gid,
        pool=["Wraith"],
        llm=env["llm"],
        kb=env["kb"],
        index=env["index"],
        api=env["api"],
        db=env["db"],
        repo_root=tmp_path,
        commit_fn=commit,
        sync_fn=sync,
    )
    assert result.kind == "analyzed"
    seen = state.seen_get(env["post"].gid, env["db"])
    assert seen["kind"] == "analyzed"
    # git commit invoked twice: early patch-dir publish, then KB files + dir
    assert result.kb_updated is True
    assert commit.call_count == 2
    early = commit.call_args_list[0]
    assert early[0][1] == [env["kb"].patch_dir(result.patch_id)]
    paths = commit.call_args[0][1]
    assert env["kb"].patch_dir(result.patch_id) in paths
    assert env["kb"].heroes_path in paths
    sync.assert_called_once_with(tmp_path)


def test_hotfix(env, tmp_path, entity_index):
    commit = MagicMock()
    sync = MagicMock(return_value=True)
    small_post = SteamPost(
        gid="hf1",
        title="hotfix",
        date=env["post"].date,
        url="",
        author="",
        contents="[p][b]\\[ Heroes ][/b][/p][p]- Wraith: Card Trick heal reduced from 75 to 60[/p]",
    )
    jobs.fetch_post = lambda gid: small_post
    result = analyze_and_post(
        "hf1",
        pool=[],
        llm=env["llm"],
        kb=env["kb"],
        index=env["index"],
        api=env["api"],
        db=env["db"],
        repo_root=tmp_path,
        commit_fn=commit,
        sync_fn=sync,
    )
    assert result.kind == "hotfix"
    assert commit.call_count == 2
    assert commit.call_args[0][1] == [env["kb"].patch_dir(result.patch_id)]
    assert commit.call_args[0][2].endswith("(analysis artifacts only)")
    assert state.seen_get("hf1", env["db"])["kind"] == "hotfix"


def test_default_llm_constructed(env, tmp_path, monkeypatch):
    constructed = []
    monkeypatch.setattr(jobs, "LLMClient", lambda: constructed.append(1) or env["llm"])
    analyze_and_post(
        env["post"].gid,
        pool=[],
        llm=None,
        kb=env["kb"],
        index=env["index"],
        api=env["api"],
        db=env["db"],
        repo_root=tmp_path,
        commit_fn=MagicMock(),
        sync_fn=MagicMock(),
    )
    assert len(constructed) == 1


def test_latest_dedupes_on_resolved_gid(env, tmp_path, monkeypatch):
    monkeypatch.setattr(jobs, "fetch_patch_posts", lambda count: [env["post"]])
    kwargs = {
        "pool": [],
        "llm": env["llm"],
        "kb": env["kb"],
        "index": env["index"],
        "api": env["api"],
        "db": env["db"],
        "repo_root": tmp_path,
        "commit_fn": MagicMock(),
        "sync_fn": MagicMock(),
    }
    assert analyze_and_post("latest", **kwargs).kind == "analyzed"
    assert analyze_and_post("latest", **kwargs) is None


def test_kb_update_failure_still_commits(env, tmp_path, monkeypatch):
    commit = MagicMock()
    sync = MagicMock(return_value=True)

    def boom(*a, **kw):
        raise RuntimeError("output truncated")

    monkeypatch.setattr(jobs, "run_kb_update", boom)
    result = analyze_and_post(
        env["post"].gid,
        pool=["Wraith"],
        llm=env["llm"],
        kb=env["kb"],
        index=env["index"],
        api=env["api"],
        db=env["db"],
        repo_root=tmp_path,
        commit_fn=commit,
        sync_fn=sync,
    )
    assert result.kind == "analyzed"
    assert result.kb_updated is False
    seen = state.seen_get(env["post"].gid, env["db"])
    assert seen["kind"] == "analyzed"
    assert seen["attempts"] == 0
    assert commit.call_count == 2
    assert commit.call_args[0][1] == [env["kb"].patch_dir(result.patch_id)]
    assert commit.call_args[0][2].endswith("(analysis artifacts only)")


def test_failure_attempts_and_skip(env, tmp_path, monkeypatch):
    def boom(*a, **kw):
        raise RuntimeError("llm exploded")

    monkeypatch.setattr(jobs, "run_analysis", boom)
    for i in range(3):
        with pytest.raises(RuntimeError):
            analyze_and_post(
                env["post"].gid,
                pool=[],
                llm=env["llm"],
                kb=env["kb"],
                index=env["index"],
                api=env["api"],
                db=env["db"],
                repo_root=tmp_path,
                commit_fn=MagicMock(),
                sync_fn=MagicMock(),
            )
    row = state.seen_get(env["post"].gid, env["db"])
    assert row["attempts"] == 3
    assert row["kind"] == "skipped"


def test_commit_failure_still_returns(env, tmp_path):
    commit = MagicMock(side_effect=RuntimeError("git exploded"))
    sync = MagicMock(return_value=True)
    result = analyze_and_post(
        env["post"].gid,
        pool=[],
        llm=env["llm"],
        kb=env["kb"],
        index=env["index"],
        api=env["api"],
        db=env["db"],
        repo_root=tmp_path,
        commit_fn=commit,
        sync_fn=sync,
    )
    assert result.kind == "analyzed"
    assert result.kb_updated is True
    assert commit.call_count == 2
    assert state.seen_get(env["post"].gid, env["db"])["kind"] == "analyzed"


def test_creator_sources_fn_lands_in_stage1(env, tmp_path):
    analyze_and_post(
        env["post"].gid,
        pool=[],
        llm=env["llm"],
        kb=env["kb"],
        index=env["index"],
        api=env["api"],
        db=env["db"],
        repo_root=tmp_path,
        commit_fn=MagicMock(),
        sync_fn=MagicMock(),
        creator_sources_fn=lambda post: "### vegas (2026-09-20)\nmarker claim xyz",
    )
    patch_id = f"{env['post'].date:%Y-%m-%d}-{env['post'].gid}"
    prompt = (env["kb"].patch_dir(patch_id) / "stage1.prompt.md").read_text()
    assert "marker claim xyz" in prompt


SEASON_CONTENTS = (
    "[p]The points for a game has been increased from 300 to 350.[/p]"
    "[p]On average, players can expect to see their rank decrease by "
    "around 1 badge.[/p]"
)

SEASON_BUNDLE = {
    "season_name": "Beta Season 2",
    "starts": "2026-11-05",
    "ends": "2027-03-11",
    "headline": "Ranks soft reset for the new season.",
    "reset_steps": [{"title": "Soft reset", "detail": "About 1 badge."}],
    "rules": [
        {
            "label": "Points per match",
            "before": "300",
            "after": "350",
            "note": "",
        },
        {
            "label": "Imagined rule",
            "before": "999",
            "after": "888",
            "note": "",
        },
    ],
    "winners": [{"who": "Grinders", "why": "More points per game."}],
}


def _season_post(env) -> SteamPost:
    return SteamPost(
        gid="s1",
        title="Ranked - Beta Season 2",
        date=env["post"].date,
        url="https://example.com/season",
        author="valve",
        contents=SEASON_CONTENTS,
    )


def _season_llm() -> FakeLLMClient:
    return FakeLLMClient({stage_marker("season_extract"): SEASON_BUNDLE})


def test_ranked_season(env, tmp_path, monkeypatch):
    post = _season_post(env)
    monkeypatch.setattr(jobs, "fetch_post", lambda gid: post)
    commit = MagicMock()
    sync = MagicMock(return_value=True)
    kwargs = {
        "llm": _season_llm(),
        "kb": env["kb"],
        "index": env["index"],
        "api": env["api"],
        "db": env["db"],
        "repo_root": tmp_path,
        "commit_fn": commit,
        "sync_fn": sync,
    }
    result = analyze_and_post("s1", **kwargs)
    assert result.kind == "ranked_season"
    patch_id = result.patch_id
    data = json.loads(
        (env["kb"].patch_dir(patch_id) / "season.json").read_text()
    )
    assert data["gid"] == "s1"
    assert data["title"] == "Ranked - Beta Season 2"
    assert data["url"] == "https://example.com/season"
    assert data["season_name"] == "Beta Season 2"
    assert data["ends"] == "2027-03-11"
    # the rule whose numbers are not in the post was dropped
    assert [r["label"] for r in data["rules"]] == ["Points per match"]
    assert state.seen_get("s1", env["db"])["kind"] == "ranked_season"
    commit.assert_called_once_with(
        tmp_path,
        [env["kb"].patch_dir(patch_id)],
        "kb: Ranked - Beta Season 2 (ranked season)",
    )
    sync.assert_called_once_with(tmp_path)
    # second run short-circuits on the seen row
    assert analyze_and_post("s1", **kwargs) is None


def test_season_json_present_skips(env, tmp_path, monkeypatch):
    post = _season_post(env)
    monkeypatch.setattr(jobs, "fetch_post", lambda gid: post)
    patch_id = f"{post.date:%Y-%m-%d}-{post.gid}"
    (env["kb"].patch_dir(patch_id) / "season.json").write_text("{}")
    result = analyze_and_post(
        "s1",
        llm=_season_llm(),
        kb=env["kb"],
        index=env["index"],
        api=env["api"],
        db=env["db"],
        repo_root=tmp_path,
        commit_fn=MagicMock(),
        sync_fn=MagicMock(),
    )
    assert result is None
    assert state.seen_get("s1", env["db"])["kind"] == "ranked_season"


def test_season_ingest_rejects_non_season(env, tmp_path, monkeypatch):
    monkeypatch.setattr(jobs, "fetch_post", lambda gid: env["post"])
    with pytest.raises(RuntimeError, match="not a ranked season"):
        jobs.season_ingest(
            env["post"].gid,
            llm=env["llm"],
            kb=env["kb"],
            db=env["db"],
            repo_root=tmp_path,
            commit_fn=MagicMock(),
            sync_fn=MagicMock(),
        )


def test_no_creator_sources_fn_prompt_shows_none(env, tmp_path):
    analyze_and_post(
        env["post"].gid,
        pool=[],
        llm=env["llm"],
        kb=env["kb"],
        index=env["index"],
        api=env["api"],
        db=env["db"],
        repo_root=tmp_path,
        commit_fn=MagicMock(),
        sync_fn=MagicMock(),
    )
    patch_id = f"{env['post'].date:%Y-%m-%d}-{env['post'].gid}"
    prompt = (env["kb"].patch_dir(patch_id) / "stage1.prompt.md").read_text()
    assert "(none)" in prompt
