import asyncio
from datetime import UTC, datetime

from patchwhisperer.bot import poller, state
from patchwhisperer.sources.steam_news import SteamPost


def _post(gid):
    return SteamPost(
        gid=gid,
        title=f"Update {gid}",
        date=datetime(2026, 9, 16, tzinfo=UTC),
        url="",
        author="",
        contents="",
        tags=["patchnotes"],
    )


def test_first_run_marks_backlog(tmp_path, monkeypatch):
    db = tmp_path / "s.db"
    state.init_db(db)
    posts = [_post("1"), _post("2")]
    monkeypatch.setattr(poller, "fetch_patch_posts", lambda count: posts)
    ran = []
    asyncio.run(poller.poll_once(lambda g: ran.append(g), db))
    assert ran == []
    assert state.seen_count(db) == 2
    assert all(r["kind"] == "skipped" for r in state.seen_recent(10, db))


def test_new_gid_triggers_job(tmp_path, monkeypatch):
    db = tmp_path / "s.db"
    state.init_db(db)
    state.seen_mark("1", "t", "d", "analyzed", db)
    monkeypatch.setattr(
        poller, "fetch_patch_posts", lambda count: [_post("1"), _post("3")]
    )
    ran = []
    asyncio.run(poller.poll_once(lambda g: ran.append(g), db))
    assert ran == ["3"]


def test_async_job_is_awaited(tmp_path, monkeypatch):
    db = tmp_path / "s.db"
    state.init_db(db)
    state.seen_mark("1", "t", "d", "analyzed", db)
    monkeypatch.setattr(
        poller, "fetch_patch_posts", lambda count: [_post("1"), _post("9")]
    )
    ran = []

    async def async_job(gid):
        ran.append(gid)

    asyncio.run(poller.poll_once(async_job, db))
    assert ran == ["9"]
