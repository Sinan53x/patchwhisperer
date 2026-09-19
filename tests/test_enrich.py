from typing import ClassVar

from patchwhisperer.analysis.enrich import merge_enrichment
from patchwhisperer.analysis.llm import FakeLLMClient, stage_marker
from patchwhisperer.analysis.schemas import HeroEnrichment
from patchwhisperer.kb.schema import Build, HeroState, Matchups
from patchwhisperer.kb.store import KBStore
from patchwhisperer.sources.deadlock_api import DeadlockAPI


def _api(item_rows, hero_matches=1000, counter_rows=None):
    api = DeadlockAPI.__new__(DeadlockAPI)
    api.client = None
    api._own = False
    api._get_cached = lambda key, path, **kw: (
        item_rows if "item-stats" in path else counter_rows
    )
    api.hero_stats = lambda **kw: [{"hero_id": 1, "matches": hero_matches, "wins": 500}]
    api.heroes = lambda: [
        {"id": 1, "name": "Haze"},
        {"id": 2, "name": "Wraith"},
        {"id": 3, "name": "Abrams"},
    ]
    return api


class _Idx:
    items: ClassVar = [
        {"id": 10, "name": "Tesla Bullets", "item_slot_type": "weapon", "item_tier": 4},
        {"id": 11, "name": "Lucky Shot", "item_slot_type": "weapon", "item_tier": 4},
    ]
    heroes: ClassVar = []


def test_item_usage_math():
    api = _api(
        [
            {
                "item_id": 10,
                "wins": 300,
                "losses": 300,
                "matches": 600,
                "avg_buy_time_s": 900,
            },
            {
                "item_id": 11,
                "wins": 60,
                "losses": 60,
                "matches": 120,
                "avg_buy_time_s": 1800,
            },
            {"item_id": 99, "wins": 1, "losses": 1, "matches": 2, "avg_buy_time_s": 0},
        ]
    )
    usage = api.hero_item_usage(1, _Idx())
    assert [u.item for u in usage] == ["Tesla Bullets", "Lucky Shot"]
    u = usage[0]
    assert u.share == 0.6
    assert u.win_rate == 0.5
    assert u.avg_buy_min == 15
    assert u.slot == "weapon" and u.tier == 4
    assert usage[1].share == 0.12


def test_counters_top_bottom():
    api = _api(
        [],
        counter_rows=[
            {"hero_id": 1, "enemy_hero_id": 2, "wins": 160, "matches_played": 200},
            {"hero_id": 1, "enemy_hero_id": 3, "wins": 80, "matches_played": 200},
            {
                "hero_id": 1,
                "enemy_hero_id": 2,
                "wins": 1,
                "matches_played": 1,
            },  # filtered
        ],
    )
    out = api.hero_counters()
    c = out[1]
    assert c.beats[0][0] == "Wraith" and c.beats[0][1] == 0.8
    assert c.loses_to[0][0] == "Abrams" and c.loses_to[0][1] == 0.4
    # the low-sample duplicate is excluded by min_matches
    assert all(n >= 150 for _, _, n in c.beats)


def test_build_matchups_yaml_roundtrip(tmp_path):
    kb = KBStore(tmp_path)
    h = HeroState(
        name="Infernus",
        builds=[
            Build(
                name="Dashfernus",
                damage="spirit",
                core_items=["Divine Barrier"],
                popularity="primary",
            )
        ],
        matchups=Matchups(beats=["Wraith"], loses_to=["Silver"]),
        matchup_notes="grounded by bola",
        confidence=0.7,
    )
    kb.save_heroes({"Infernus": h})
    loaded = kb.load_heroes()["Infernus"]
    assert loaded == h
    assert loaded.builds[0].damage == "spirit"


def test_apply_kb_update_builds(tmp_path):
    from patchwhisperer.analysis.pipeline import apply_kb_update
    from patchwhisperer.analysis.schemas import KBUpdate

    kb = KBStore(tmp_path)
    kb.save_heroes({"Haze": HeroState(name="Haze")})
    upd = KBUpdate(
        hero_updates={
            "Haze": {
                "builds": [
                    {
                        "name": "gun",
                        "damage": "gun",
                        "core_items": ["Tesla Bullets"],
                        "popularity": "primary",
                    },
                    {
                        "name": "bad",
                        "damage": "VOID",
                        "core_items": [],
                        "popularity": "primary",
                    },
                ],
                "matchups": {"beats": ["Wraith"], "loses_to": []},
            }
        }
    )
    apply_kb_update(kb, upd)
    h = kb.load_heroes()["Haze"]
    # invalid damage entry dropped wholesale (whole builds field dropped on error)
    assert h.matchups.beats == ["Wraith"]


def test_merge_enrichment():
    h = HeroState(name="Infernus", tier="B", last_changed_patch="Old Patch")
    r = HeroEnrichment.model_validate(
        {
            "role": "flex carry",
            "tier": "A",
            "trend": "rising",
            "why": "two real builds",
            "builds": [
                {
                    "name": "gun",
                    "damage": "gun",
                    "core_items": ["Tesla Bullets"],
                    "popularity": "primary",
                },
                {
                    "name": "Dashfernus",
                    "damage": "spirit",
                    "core_items": ["Divine Barrier"],
                    "popularity": "primary",
                },
            ],
            "core_items": ["Tesla Bullets", "Divine Barrier"],
            "matchups": {"beats": ["Abrams"], "loses_to": ["Silver"]},
            "confidence": 0.8,
        }
    )
    out = merge_enrichment(h, r)
    assert out.tier == "A"
    assert out.build_variants == ["gun", "Dashfernus"]
    assert out.last_changed_patch == "Old Patch"
    assert out.matchups.loses_to == ["Silver"]


def test_enrich_fake_llm_marker():
    llm = FakeLLMClient(
        {stage_marker("enrich_hero"): {"tier": "A", "trend": "rising", "builds": []}}
    )
    out = llm.complete_json(
        "s", "# Task: enrich one hero's knowledge-base entry", HeroEnrichment
    )
    assert out.tier == "A"
