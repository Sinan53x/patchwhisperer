import shutil
from unittest.mock import MagicMock

import pytest
from conftest import FIXTURES, load_post

from patchwhisperer.analysis.llm import FakeLLMClient, stage_marker
from patchwhisperer.bot import jobs, state
from patchwhisperer.bot.jobs import analyze_and_post
from patchwhisperer.kb.store import KBStore
from patchwhisperer.sources.steam_news import SteamPost


class FakeMessage:
    def __init__(self, mid=100):
        self.id = mid
        self.reactions = []
        self.thread = None

    def add_reaction(self, emoji):
        self.reactions.append(emoji)

    def create_thread(self, name):
        self.thread = FakeThread(name)
        return self.thread


class FakeThread:
    def __init__(self, name, tid=200):
        self.id = tid
        self.name = name
        self.sent = []

    def send(self, content):
        self.sent.append(content)


class FakeChannel:
    def __init__(self, cid=50):
        self.id = cid
        self.sent = []
        self.messages = []

    def send(self, content):
        self.sent.append(content)
        m = FakeMessage()
        self.messages.append(m)
        return m


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
    channel = FakeChannel()
    commit = MagicMock(return_value="abc123")
    result = analyze_and_post(
        env["post"].gid,
        pool=["Wraith"],
        channel=channel,
        llm=env["llm"],
        kb=env["kb"],
        index=env["index"],
        api=env["api"],
        db=env["db"],
        repo_root=tmp_path,
        commit_fn=commit,
    )
    assert result.kind == "analyzed"
    # TL;DR sent first, then reactions, then thread
    assert channel.sent[0].startswith("**[SIGNIFICANT]**")
    msg = channel.messages[0]
    assert msg.reactions == ["👍", "👎"]
    assert msg.thread is not None
    assert len(msg.thread.sent) >= 1
    # db rows
    seen = state.seen_get(env["post"].gid, env["db"])
    assert seen["kind"] == "analyzed"
    rec = state.post_get(result.patch_id, env["db"])
    assert rec["thread_id"] == "200"
    # git commit invoked once with KB files + the patch dir
    assert result.kb_updated is True
    commit.assert_called_once()
    paths = commit.call_args[0][1]
    assert env["kb"].patch_dir(result.patch_id) in paths
    assert env["kb"].heroes_path in paths


def test_hotfix_no_thread(env, tmp_path, entity_index):
    channel = FakeChannel()
    commit = MagicMock()
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
        channel=channel,
        llm=env["llm"],
        kb=env["kb"],
        index=env["index"],
        api=env["api"],
        db=env["db"],
        repo_root=tmp_path,
        commit_fn=commit,
    )
    assert result.kind == "hotfix"
    assert channel.messages[0].thread is None
    commit.assert_called_once()
    assert commit.call_args[0][1] == [env["kb"].patch_dir(result.patch_id)]
    assert commit.call_args[0][2].endswith("(analysis artifacts only)")
    assert state.seen_get("hf1", env["db"])["kind"] == "hotfix"


def test_default_llm_constructed(env, tmp_path, monkeypatch):
    channel = FakeChannel()
    constructed = []
    monkeypatch.setattr(jobs, "LLMClient", lambda: constructed.append(1) or env["llm"])
    analyze_and_post(
        env["post"].gid,
        pool=[],
        channel=channel,
        llm=None,
        kb=env["kb"],
        index=env["index"],
        api=env["api"],
        db=env["db"],
        repo_root=tmp_path,
        commit_fn=MagicMock(),
    )
    assert len(constructed) == 1


def test_latest_dedupes_on_resolved_gid(env, tmp_path, monkeypatch):
    monkeypatch.setattr(jobs, "fetch_patch_posts", lambda count: [env["post"]])
    channel = FakeChannel()
    kwargs = {
        "pool": [],
        "channel": channel,
        "llm": env["llm"],
        "kb": env["kb"],
        "index": env["index"],
        "api": env["api"],
        "db": env["db"],
        "repo_root": tmp_path,
        "commit_fn": MagicMock(),
    }
    assert analyze_and_post("latest", **kwargs).kind == "analyzed"
    assert analyze_and_post("latest", **kwargs) is None


def test_kb_update_failure_still_posts(env, tmp_path, monkeypatch):
    channel = FakeChannel()
    commit = MagicMock()

    def boom(*a, **kw):
        raise RuntimeError("output truncated")

    monkeypatch.setattr(jobs, "run_kb_update", boom)
    result = analyze_and_post(
        env["post"].gid,
        pool=["Wraith"],
        channel=channel,
        llm=env["llm"],
        kb=env["kb"],
        index=env["index"],
        api=env["api"],
        db=env["db"],
        repo_root=tmp_path,
        commit_fn=commit,
    )
    assert result.kind == "analyzed"
    assert result.kb_updated is False
    msg = channel.messages[0]
    assert msg.reactions == ["👍", "👎"]
    assert msg.thread is not None
    assert len(msg.thread.sent) >= 1
    assert "knowledge-base update failed (output truncated)" in channel.sent[-1]
    seen = state.seen_get(env["post"].gid, env["db"])
    assert seen["kind"] == "analyzed"
    assert seen["attempts"] == 0
    commit.assert_called_once()
    assert commit.call_args[0][1] == [env["kb"].patch_dir(result.patch_id)]
    assert commit.call_args[0][2].endswith("(analysis artifacts only)")


def test_failure_attempts_and_skip(env, tmp_path, monkeypatch):
    channel = FakeChannel()

    def boom(*a, **kw):
        raise RuntimeError("llm exploded")

    monkeypatch.setattr(jobs, "run_analysis", boom)
    for i in range(3):
        with pytest.raises(RuntimeError):
            analyze_and_post(
                env["post"].gid,
                pool=[],
                channel=channel,
                llm=env["llm"],
                kb=env["kb"],
                index=env["index"],
                api=env["api"],
                db=env["db"],
                repo_root=tmp_path,
                commit_fn=MagicMock(),
            )
    row = state.seen_get(env["post"].gid, env["db"])
    assert row["attempts"] == 3
    assert row["kind"] == "skipped"
    assert "Will retry on next poll (attempt 1/3)" in channel.sent[0]
    assert "giving up" in channel.sent[-1]


def test_commit_failure_still_returns(env, tmp_path):
    channel = FakeChannel()
    commit = MagicMock(side_effect=RuntimeError("git exploded"))
    result = analyze_and_post(
        env["post"].gid,
        pool=[],
        channel=channel,
        llm=env["llm"],
        kb=env["kb"],
        index=env["index"],
        api=env["api"],
        db=env["db"],
        repo_root=tmp_path,
        commit_fn=commit,
    )
    assert result.kind == "analyzed"
    assert result.kb_updated is True
    commit.assert_called_once()
    assert state.seen_get(env["post"].gid, env["db"])["kind"] == "analyzed"


def test_failure_notify_failures_false(env, tmp_path, monkeypatch):
    channel = FakeChannel()

    def boom(*a, **kw):
        raise RuntimeError("llm exploded")

    monkeypatch.setattr(jobs, "run_analysis", boom)
    with pytest.raises(RuntimeError):
        analyze_and_post(
            env["post"].gid,
            pool=[],
            channel=channel,
            llm=env["llm"],
            kb=env["kb"],
            index=env["index"],
            api=env["api"],
            db=env["db"],
            repo_root=tmp_path,
            commit_fn=MagicMock(),
            notify_failures=False,
        )
    assert channel.sent == []
    assert state.seen_get(env["post"].gid, env["db"])["attempts"] == 1
