from patchwhisperer.bot import state


def test_pools_crud(tmp_path):
    db = tmp_path / "s.db"
    state.init_db(db)
    assert state.pool_get(1, db) == []
    state.pool_set(1, ["Wraith", "Warden"], db)
    assert state.pool_get(1, db) == ["Wraith", "Warden"]
    state.pool_set(1, ["Wraith"], db)
    assert state.pool_get(1, db) == ["Wraith"]
    state.pool_set(2, ["Lash"], db)
    assert state.pool_all(db) == ["Wraith", "Lash"]


def test_seen_posts(tmp_path):
    db = tmp_path / "s.db"
    state.init_db(db)
    assert state.seen_get("g1", db) is None
    assert state.seen_bump_attempt("g1", "t", "d", db) == 1
    assert state.seen_bump_attempt("g1", "t", "d", db) == 2
    state.seen_mark("g1", "t", "d", "analyzed", db)
    row = state.seen_get("g1", db)
    assert row["kind"] == "analyzed"
    assert row["attempts"] == 2
    assert state.seen_count(db) == 1
    assert state.seen_recent(10, db)[0]["gid"] == "g1"


def test_feedback(tmp_path):
    db = tmp_path / "s.db"
    state.init_db(db)
    state.feedback_add("p1", 42, "text", "nice", db)
    state.feedback_add("p1", 43, "reaction_up", db=db)
    rows = state.feedback_list("p1", db)
    assert len(rows) == 2
    assert rows[0]["kind"] == "text"
    assert rows[1]["kind"] == "reaction_up"
