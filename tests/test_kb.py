import yaml

from patchwhisperer.kb.schema import HeroState
from patchwhisperer.kb.store import KBStore


def test_hero_round_trip(tmp_path):
    store = KBStore(tmp_path)
    hero = HeroState(
        name="Wraith",
        role="carry",
        archetypes=["gun"],
        tier="A",
        trend="falling",
        why="nerfed 09-16",
        core_items=["Tesla Bullets"],
        build_variants=["spirit"],
        enabled_by=["Ivy"],
        countered_by=["Holliday"],
        last_changed_patch="09-16-2026",
        notes="watch card trick",
    )
    store.save_heroes({"Wraith": hero})
    loaded = store.load_heroes()
    assert loaded["Wraith"] == hero
    raw = yaml.safe_load((tmp_path / "heroes.yaml").read_text())
    assert list(raw["Wraith"].keys()) == list(HeroState.model_fields)
