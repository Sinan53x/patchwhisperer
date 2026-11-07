import json
import os
import sqlite3
from datetime import UTC, datetime
from pathlib import Path

DB_PATH = os.getenv("STATE_DB", "./state.db")

_SCHEMA = """
CREATE TABLE IF NOT EXISTS seen_posts(
    gid TEXT PRIMARY KEY,
    title TEXT,
    date TEXT,
    processed_at TEXT,
    kind TEXT,
    attempts INT DEFAULT 0
);
CREATE TABLE IF NOT EXISTS pools(
    user_id TEXT PRIMARY KEY,
    heroes TEXT,
    updated_at TEXT
);
"""


def _conn(db: Path | str | None = None) -> sqlite3.Connection:
    conn = sqlite3.connect(str(db or DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn


def init_db(db: Path | str | None = None) -> None:
    with _conn(db) as c:
        c.executescript(_SCHEMA)


def _now() -> str:
    return datetime.now(tz=UTC).isoformat()


# -- seen_posts -----------------------------------------------------------


def seen_get(gid: str, db=None) -> dict | None:
    with _conn(db) as c:
        row = c.execute("SELECT * FROM seen_posts WHERE gid=?", (gid,)).fetchone()
        return dict(row) if row else None


def seen_mark(gid: str, title: str, date: str, kind: str, db=None) -> None:
    with _conn(db) as c:
        c.execute(
            "INSERT INTO seen_posts(gid,title,date,processed_at,kind,attempts) "
            "VALUES(?,?,?,?,?,COALESCE((SELECT attempts FROM seen_posts WHERE gid=?),0)) "
            "ON CONFLICT(gid) DO UPDATE SET processed_at=excluded.processed_at, kind=excluded.kind",
            (gid, title, date, _now(), kind, gid),
        )


def seen_bump_attempt(gid: str, title: str = "", date: str = "", db=None) -> int:
    with _conn(db) as c:
        c.execute(
            "INSERT INTO seen_posts(gid,title,date,processed_at,kind,attempts) VALUES(?,?,?,?,?,1) "
            "ON CONFLICT(gid) DO UPDATE SET attempts=attempts+1",
            (gid, title, date, _now(), "pending"),
        )
        return c.execute(
            "SELECT attempts FROM seen_posts WHERE gid=?", (gid,)
        ).fetchone()["attempts"]


def seen_count(db=None) -> int:
    with _conn(db) as c:
        return c.execute("SELECT COUNT(*) n FROM seen_posts").fetchone()["n"]


def seen_recent(limit: int = 10, db=None) -> list[dict]:
    with _conn(db) as c:
        return [
            dict(r)
            for r in c.execute(
                "SELECT * FROM seen_posts ORDER BY processed_at DESC LIMIT ?",
                (limit,),
            )
        ]


# -- pools ----------------------------------------------------------------


def pool_get(user_id: int | str, db=None) -> list[str]:
    with _conn(db) as c:
        row = c.execute(
            "SELECT heroes FROM pools WHERE user_id=?", (str(user_id),)
        ).fetchone()
        return json.loads(row["heroes"]) if row else []


def pool_set(user_id: int | str, heroes: list[str], db=None) -> None:
    with _conn(db) as c:
        c.execute(
            "INSERT INTO pools(user_id,heroes,updated_at) VALUES(?,?,?) "
            "ON CONFLICT(user_id) DO UPDATE SET heroes=excluded.heroes, updated_at=excluded.updated_at",
            (str(user_id), json.dumps(heroes), _now()),
        )


def pool_all(db=None) -> list[str]:
    with _conn(db) as c:
        out: list[str] = []
        for row in c.execute("SELECT heroes FROM pools"):
            for h in json.loads(row["heroes"]):
                if h not in out:
                    out.append(h)
        return out
