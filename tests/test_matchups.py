import httpx

from patchwhisperer.analysis.matchups import sync_kb_matchups
from patchwhisperer.kb.schema import HeroState, Matchups
from patchwhisperer.kb.store import KBStore
from patchwhisperer.sources.deadlock_api import Counters


class FakeAPI:
    def __init__(self, counters=None, error=None):
        self.counters, self.error = counters, error

    def hero_counters(self, *, days):
        if self.error:
            raise self.error
        return self.counters

    def heroes(self):
        return [{"id": 1, "name": "Holliday"}]


def _kb(tmp_path):
    kb = KBStore(tmp_path)
    kb.save_heroes(
        {
            "Holliday": HeroState(
                name="Holliday",
                matchups=Matchups(loses_to=["Mo & Krill"]),
                matchup_notes="Mo & Krill is her hard loss (42%).",
            )
        }
    )
    return kb


def test_measured_matchups_replace_stored_claims(tmp_path):
    kb = _kb(tmp_path)
    counters = {
        1: Counters(
            beats=[("Mo & Krill", 0.523, 560), ("Silver", 0.5, 200)],
            loses_to=[("Drifter", 0.42, 300), ("Silver", 0.5, 200)],
        )
    }
    sync_kb_matchups(kb, FakeAPI(counters))
    h = kb.load_heroes()["Holliday"]
    assert h.matchups.beats == ["Mo & Krill"]
    assert h.matchups.loses_to == ["Drifter"]
    assert "Mo & Krill 52%" in h.matchup_notes
    assert "hard loss" not in h.matchup_notes


def test_api_failure_keeps_existing_matchups(tmp_path):
    kb = _kb(tmp_path)
    sync_kb_matchups(kb, FakeAPI(error=httpx.ConnectError("down")))
    assert kb.load_heroes()["Holliday"].matchups.loses_to == ["Mo & Krill"]


def test_hero_without_enough_games_loses_old_claims(tmp_path):
    kb = _kb(tmp_path)
    heroes = kb.load_heroes()
    heroes["Billy"] = HeroState(name="Billy", matchup_notes="Beats everyone (90%).")
    kb.save_heroes(heroes)
    sync_kb_matchups(kb, FakeAPI({1: Counters(beats=[("Silver", 0.6, 200)])}))
    billy = kb.load_heroes()["Billy"]
    assert billy.matchups.beats == []
    assert "90%" not in billy.matchup_notes
