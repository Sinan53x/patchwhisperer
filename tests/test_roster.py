import asyncio
import math
import shutil
from datetime import UTC, date, datetime, timedelta
from unittest.mock import MagicMock

import pytest
from conftest import load_post

from patchwhisperer.analysis import roster
from patchwhisperer.analysis.llm import FakeLLMClient, stage_marker
from patchwhisperer.analysis.render import (
    render_checkin_card,
    render_hero_card,
)
from patchwhisperer.analysis.roster import (
    apply_new_hero,
    checkins_due,
    evaluate_new_hero,
    find_release_post,
    hero_kit_text,
    new_heroes,
    sync_roster,
    upcoming_heroes,
)
from patchwhisperer.analysis.schemas import NewHeroCard
from patchwhisperer.bot import poller
from patchwhisperer.bot import state as bot_state
from patchwhisperer.kb.schema import Build, HeroState
from patchwhisperer.kb.store import KBStore
from patchwhisperer.parse.entities import EntityIndex
from patchwhisperer.sources.steam_news import SteamPost

TODAY = date(2026, 10, 9)


@pytest.fixture
def kb(tmp_path):
    root = tmp_path / "kb"
    root.mkdir()
    for f in ("heroes.yaml", "items.yaml", "meta.md"):
        shutil.copy(f"kb/{f}", root / f)
    return KBStore(root)


def _rat_king() -> dict:
    return {
        "id": 84,
        "name": "Rat King",
        "class_name": "hero_ratking",
        "player_selectable": True,
        "hero_type": "brawler",
        "gun_tag": "Spreadshot",
        "tags": ["Scrappy", "Regal"],
        "complexity": 3,
        "starting_stats": {"max_health": {"value": 800}, "stamina": 3},
        "popular_items": {
            "early_game": [
                {
                    "item_id": 1,
                    "class_name": "upgrade_x",
                    "pick_pct": 23.9,
                    "winrate_pct": 63.6,
                }
            ]
        },
    }


def _api(entity_index, heroes=None):
    api = MagicMock()
    api.heroes.return_value = (
        heroes if heroes is not None else entity_index.heroes
    )
    api.all_heroes.return_value = api.heroes.return_value
    api.hero_abilities.return_value = []
    api.hero_stats.return_value = [{"hero_id": 84, "matches": 100, "wins": 60}]
    api.hero_item_usage.return_value = []
    api.hero_counters.return_value = {}
    api.snapshot.return_value = {}
    return api


def _canned_enrichment(tier="A"):
    return {
        "enrichment": {
            "role": "brawler frontline",
            "tier": tier,
            "trend": "rising",
            "why": "rat swarm oppresses lanes",
            "builds": [
                {
                    "name": "rat gun",
                    "damage": "gun",
                    "core_items": ["Monster Rounds"],
                    "popularity": "primary",
                }
            ],
            "core_items": ["Monster Rounds"],
            "confidence": 0.4,
        },
        "card": {
            "headline": "rat king summons the sewers",
            "kit_read": ["grenade poke", "rat swarm", "damage soak"],
            "meta_fit": "brawls well in the new map",
            "provisional_tier": "A",
            "confidence": 0.4,
            "what_to_watch": ["day-3 win rate"],
        },
    }


# -- pure helpers -------------------------------------------------------------


def test_new_and_upcoming_heroes():
    active = [{"id": 1, "name": "Wraith"}, {"id": 84, "name": "Rat King"}]
    assert [h["name"] for h in new_heroes(active, {"Wraith": HeroState(name="Wraith")})] == [
        "Rat King"
    ]
    all_heroes = [
        {"name": "Rat King", "player_selectable": True},
        {"name": "Deadman Danny", "player_selectable": False},
        {"name": "Baba", "player_selectable": False, "disabled": True},
    ]
    assert upcoming_heroes(all_heroes) == ["Deadman Danny"]


def test_checkins_due_date_math():
    heroes = {
        "A": HeroState(
            name="A", provisional=True, released_on=str(TODAY - timedelta(days=7))
        ),
        "B": HeroState(
            name="B", provisional=True, released_on=str(TODAY - timedelta(days=6))
        ),
        "C": HeroState(name="C", released_on=str(TODAY - timedelta(days=30))),
        "D": HeroState(name="D", provisional=True),
    }
    assert checkins_due(heroes, TODAY) == ["A"]


def test_hero_kit_text(entity_index):
    item_id = entity_index.items[0]["id"]
    hero = _rat_king()
    hero["popular_items"]["early_game"][0]["item_id"] = item_id
    abilities = [
        {
            "type": "ability",
            "name": "Scrap Grenade",
            "description": {
                "desc": "Throws a <svg><img/></svg><span>bomb</span> that bites"
            },
            "upgrades": [{"property_upgrades": [{"name": "AbilityCharges", "bonus": "1"}]}],
        },
        {"type": "ability", "name": "Melee"},
        {"type": "weapon", "name": "Gun"},
    ]
    text = hero_kit_text(hero, abilities, entity_index)
    assert "brawler" in text and "Spreadshot" in text and "hp 800" in text
    assert "**Scrap Grenade** — Throws a bomb that bites" in text
    assert "<svg" not in text and "<span" not in text
    assert "T1: AbilityCharges 1" in text
    assert "Melee" not in text and "Gun" not in text
    assert f"{entity_index.items[0]['name']} (pick 24%, win 64%)" in text


# -- day-0 evaluation ---------------------------------------------------------


def test_find_release_post():
    posts = [load_post("09-16-2026"), load_post("2026-10-02")]
    hit = find_release_post("Rat King", posts)
    assert hit is not None and hit.gid == "1845383656387709"
    assert find_release_post("Wraith", posts) is None
    assert find_release_post("The Doorman", posts) is None


def test_evaluate_new_hero(kb, entity_index):
    post = load_post("2026-10-02")
    llm = FakeLLMClient({stage_marker("new_hero"): _canned_enrichment()})
    api = _api(entity_index)
    state, card = evaluate_new_hero(
        "Rat King",
        _rat_king(),
        kb=kb,
        index=entity_index,
        api=api,
        llm=llm,
        release_post=post,
        sources_dir=kb.root / "sources",
        today=TODAY,
    )
    assert state.provisional is True
    # released_on comes from the release post's date, not evaluation day
    assert state.released_on == "2026-10-02"
    assert state.tier == "A"
    assert state.last_changed_patch == post.title
    assert state.notes.startswith("Day-0 kit read (2026-10-09), provisional")
    assert "check-in due 2026-10-09" in state.notes
    assert card.headline == "rat king summons the sewers"
    pdir = kb.root / "patches" / "hero-rat-king-2026-10-02"
    assert (pdir / "day0.json").exists()
    assert (pdir / "day0.prompt.md").exists()


def test_evaluate_new_hero_no_post(kb, entity_index):
    llm = FakeLLMClient({stage_marker("new_hero"): _canned_enrichment()})
    api = _api(entity_index)
    state, _ = evaluate_new_hero(
        "Rat King",
        _rat_king(),
        kb=kb,
        index=entity_index,
        api=api,
        llm=llm,
        release_post=None,
        sources_dir=kb.root / "sources",
        today=TODAY,
    )
    assert state.released_on == "2026-10-09"
    assert state.last_changed_patch == "Released 2026-10-09"
    assert (kb.root / "patches" / "hero-rat-king-2026-10-09" / "day0.json").exists()


def test_apply_new_hero_bought_by(kb):
    state = HeroState(
        name="Rat King",
        builds=[
            Build(
                name="rat gun",
                damage="gun",
                core_items=["Monster Rounds"],
                popularity="primary",
            )
        ],
    )
    changed = apply_new_hero(kb, state)
    assert kb.heroes_path in changed and kb.items_path in changed
    assert "Rat King" in kb.load_heroes()
    assert "Rat King" in kb.load_items()["Monster Rounds"].bought_by


# -- sync_roster ---------------------------------------------------------------


def test_sync_roster_adds_hero(kb, entity_index, monkeypatch):
    api = _api(entity_index, heroes=entity_index.heroes + [_rat_king()])
    llm = FakeLLMClient({stage_marker("new_hero"): _canned_enrichment()})
    sentinel = object()
    monkeypatch.setattr(
        EntityIndex, "fetch", classmethod(lambda cls, client=None: sentinel)
    )
    monkeypatch.setattr(
        roster, "fetch_patch_posts", lambda count: [load_post("2026-10-02")]
    )
    posts, commits = [], []
    result = sync_roster(
        kb=kb,
        index=entity_index,
        api=api,
        llm=llm,
        sources_dir=kb.root / "sources",
        today=TODAY,
        post_fn=lambda t, pid: posts.append((t, pid)),
        commit_fn=lambda root, paths, msg: commits.append(msg),
        sync_fn=MagicMock(),
        repo_root=kb.root,
    )
    assert result.added == ["Rat King"]
    assert result.index is sentinel
    assert len(posts) == 1 and posts[0][1] == "hero-rat-king-2026-10-02"
    assert "New hero: Rat King" in posts[0][0]
    assert commits == ["kb: new hero Rat King (day-0 read)"]
    rk = kb.load_heroes()["Rat King"]
    assert rk.provisional is True
    assert rk.released_on == "2026-10-02"
    assert rk.last_changed_patch == "Listen up, Crumbums! Your King is here."


def test_sync_roster_day0_idempotent(kb, entity_index, monkeypatch):
    pdir = kb.root / "patches" / "hero-rat-king-2026-10-02"
    pdir.mkdir(parents=True)
    (pdir / "day0.json").write_text("{}")
    api = _api(entity_index, heroes=entity_index.heroes + [_rat_king()])
    monkeypatch.setattr(roster, "fetch_patch_posts", lambda count: [])
    llm = FakeLLMClient({})
    result = sync_roster(
        kb=kb,
        index=entity_index,
        api=api,
        llm=llm,
        sources_dir=kb.root / "sources",
        today=TODAY,
        commit_fn=MagicMock(),
        sync_fn=MagicMock(),
        repo_root=kb.root,
    )
    assert llm.calls == []
    assert result.added == []
    assert "Rat King" in kb.load_heroes()


def test_sync_roster_checkin(kb, entity_index, monkeypatch):
    wraith_id = next(h["id"] for h in entity_index.heroes if h["name"] == "Wraith")
    heroes = kb.load_heroes()
    heroes["Wraith"] = heroes["Wraith"].model_copy(
        update={
            "provisional": True,
            "released_on": str(TODAY - timedelta(days=7)),
        }
    )
    kb.save_heroes(heroes)
    api = _api(entity_index)
    api.hero_stats.return_value = [
        {"hero_id": wraith_id, "matches": 100, "wins": 55}
    ]
    llm = FakeLLMClient(
        {
            stage_marker("enrich_hero"): {
                "tier": "B",
                "trend": "stable",
                "why": "settled in",
                "builds": [],
                "confidence": 0.6,
            }
        }
    )
    post = load_post("09-16-2026")
    monkeypatch.setattr(roster, "fetch_patch_posts", lambda count: [post])
    posts, commits = [], []
    result = sync_roster(
        kb=kb,
        index=entity_index,
        api=api,
        llm=llm,
        sources_dir=kb.root / "sources",
        today=TODAY,
        post_fn=lambda t, pid: posts.append((t, pid)),
        commit_fn=lambda root, paths, msg: commits.append(msg),
        sync_fn=MagicMock(),
        repo_root=kb.root,
    )
    assert result.checked_in == ["Wraith"]
    assert llm.calls == [stage_marker("enrich_hero")]
    assert commits == ["kb: Wraith 7-day check-in"]
    after = kb.load_heroes()["Wraith"]
    assert after.provisional is False and after.tier == "B"
    assert "7-day check-in" in posts[0][0]


# -- rendering -----------------------------------------------------------------


def test_render_hero_card_truncates():
    card = NewHeroCard(
        headline="h" * 200,
        kit_read=["k" * 500] * 5,
        meta_fit="m" * 500,
        threatens=["t" * 300] * 6,
        threatened_by=["t" * 300] * 6,
        build_read="b" * 300,
        provisional_tier="A",
        confidence=0.4,
        what_to_watch=["w" * 300] * 5,
    )
    text = render_hero_card("Rat King", card, HeroState(name="Rat King"))
    assert len(text) <= 1900
    assert "**New hero: Rat King**" in text


def test_render_checkin_card():
    before = HeroState(name="Rat King", tier="A")
    after = HeroState(
        name="Rat King",
        tier="B",
        trend="falling",
        why="novelty wore off",
        builds=[
            Build(
                name="rat gun",
                damage="gun",
                core_items=["Monster Rounds"],
                popularity="primary",
            )
        ],
    )
    after.matchups.loses_to = ["Haze", "Silver", "Warden", "Abrams"]
    text = render_checkin_card(
        "Rat King", before, after, {"matches": 29096, "win_rate": 0.594, "pick_rate": 0.17}
    )
    assert "tier A -> B" in text and "59.4%" in text
    assert "loses to: Haze, Silver, Warden" in text
    assert len(text) <= 1900


# -- poller gating --------------------------------------------------------------


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


def test_poll_loop_roster_gating(tmp_path, monkeypatch):
    db = tmp_path / "s.db"
    bot_state.init_db(db)
    bot_state.seen_mark("1", "t", "d", "analyzed", db)
    fetches = []
    monkeypatch.setattr(
        poller,
        "fetch_patch_posts",
        lambda count: fetches.append(1) or [_post("1")],
    )
    monkeypatch.setattr(poller, "POLL_INTERVAL_S", 0.001)
    roster_calls = []

    async def main():
        shutdown = asyncio.Event()
        task = asyncio.create_task(
            poller.poll_loop(
                lambda g: None,
                db,
                shutdown,
                roster_job=lambda: roster_calls.append(1),
                roster_every=3,
            )
        )
        await asyncio.sleep(0.3)
        shutdown.set()
        await asyncio.wait_for(task, 5)

    asyncio.run(main())
    iters = len(fetches)
    assert iters >= 4
    # roster_job runs when iteration % 3 == 0 -> i = 0, 3, 6, ...
    assert len(roster_calls) == math.ceil(iters / 3)


def test_poll_once_calls_roster_on_first_run(tmp_path, monkeypatch):
    db = tmp_path / "s.db"
    bot_state.init_db(db)
    monkeypatch.setattr(
        poller, "fetch_patch_posts", lambda count: [_post("1")]
    )
    roster_calls = []
    asyncio.run(
        poller.poll_once(lambda g: None, db, roster_job=lambda: roster_calls.append(1))
    )
    assert roster_calls == [1]
