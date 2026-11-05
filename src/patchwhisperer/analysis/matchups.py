import logging

import httpx

from patchwhisperer.kb.schema import Matchups
from patchwhisperer.kb.store import KBStore
from patchwhisperer.sources.deadlock_api import DeadlockAPI

log = logging.getLogger(__name__)

WINDOW_DAYS = 14


def _rates(pairs: list[tuple[str, float, int]]) -> str:
    return ", ".join(f"{name} {rate * 100:.0f}%" for name, rate, _ in pairs)


def sync_kb_matchups(kb: KBStore, api: DeadlockAPI) -> None:
    """Replace stored matchups with measured ones, so old claims can't resurface."""
    try:
        counters = api.hero_counters(days=WINDOW_DAYS)
        name_by_id = {h["id"]: h["name"] for h in api.heroes()}
    except httpx.HTTPError as e:
        log.warning("matchups not refreshed: %s", e)
        return
    if not counters:
        log.warning("matchups not refreshed: no data")
        return
    id_by_name = {name: hero_id for hero_id, name in name_by_id.items()}
    heroes = kb.load_heroes()
    for name, hero in heroes.items():
        c = counters.get(id_by_name.get(name))
        beats = [p for p in c.beats if p[1] > 0.5] if c else []
        loses = [p for p in c.loses_to if p[1] < 0.5] if c else []
        hero.matchups = Matchups(
            beats=[p[0] for p in beats], loses_to=[p[0] for p in loses]
        )
        hero.matchup_notes = (
            f"Measured win rate over {WINDOW_DAYS} days at Ascendant and up. "
            f"Best: {_rates(beats)}. Worst: {_rates(loses)}."
            if c
            else "Too few high-rank games to measure matchups right now."
        )
    kb.save_heroes(heroes)
