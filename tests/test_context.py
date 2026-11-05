from datetime import UTC, datetime

from conftest import load_post

from patchwhisperer.analysis import context as ctx
from patchwhisperer.parse.models import Change, Direction, EntityType, Patch
from patchwhisperer.parse.patch_parser import parse_patch


def test_format_changes_groups_by_entity(entity_index):
    patch = parse_patch(load_post("09-16-2026"), entity_index)
    out = ctx.format_changes(ctx.hero_changes(patch))
    assert "Wraith:" in out
    assert "- [nerf] Card Trick: Wraith: Card Trick heart heal reduced" in out


def test_section_split(entity_index):
    patch = parse_patch(load_post("09-16-2026"), entity_index)
    assert len(ctx.system_changes(patch)) == 17
    assert len(ctx.item_changes(patch)) == 36
    assert len(ctx.hero_changes(patch)) == 69


def test_snapshot_table():
    snap = {
        "B": {"hero_id": 2, "matches": 50, "win_rate": 0.5, "pick_rate": 0.1},
        "A": {"hero_id": 1, "matches": 100, "win_rate": 0.6, "pick_rate": 0.2},
    }
    out = ctx.snapshot_table(snap)
    lines = out.splitlines()
    assert lines[0] == "hero | WR% | PR% | matches"
    assert lines[1].startswith("A | 60.0 | 20.0 | 100")
    assert lines[2].startswith("B | 50.0 | 10.0 | 50")


def test_items_kb_unknown(tmp_path):
    from patchwhisperer.kb.store import KBStore

    kb = KBStore(tmp_path)
    (tmp_path / "items.yaml").write_text("{}\n")
    out = ctx.items_kb(kb, ["Veil Walker"])
    assert "(not in KB yet)" in out


def test_change_counts(entity_index):
    patch = parse_patch(load_post("09-16-2026"), entity_index)
    assert ctx.change_counts(patch) == "General 17, Items 36, Heroes 69, total 122"


def test_heroes_kb_omits_empty_fields(tmp_path):
    from patchwhisperer.kb.schema import HeroState
    from patchwhisperer.kb.store import KBStore

    kb = KBStore(tmp_path)
    kb.save_heroes({"Wraith": HeroState(name="Wraith", tier="A")})
    out = ctx.heroes_kb(kb)
    assert "notes" not in out
    assert "enabled_by" not in out
    assert "tier: A" in out
    assert "name: Wraith" in out


def test_unresolved_general_entity_goes_to_systems_not_heroes():
    mid_boss = Change(
        section="General",
        entity_type=EntityType.unknown,
        entity_name="Mid-Boss",
        raw="Mid-Boss: Health increased by 20%",
        direction=Direction.neutral,
        resolved=False,
    )
    patch = Patch(gid="1", title="T", date="2026-10-30T00:00:00Z", url="u", author="a", changes=[mid_boss])
    assert ctx.hero_changes(patch) == []
    assert ctx.system_changes(patch) == [mid_boss]


def test_mode_only_lines_stay_out_of_main_game_stages():
    def change(section, entity_type, name):
        return Change(
            section=section, entity_type=entity_type, entity_name=name,
            raw=f"{name}: x", direction=Direction.nerf, resolved=True,
        )

    patch = Patch(
        gid="1", title="t", date=datetime(2026, 1, 1, tzinfo=UTC), url="u", author="a",
        changes=[
            change("Heroes", EntityType.hero, "Abrams"),
            change("Street Brawl", EntityType.hero, "Baba"),
            change("Street Brawl", EntityType.item, "Decay"),
            change("Street Brawl", EntityType.system, "Souls"),
        ],
    )
    assert [c.entity_name for c in ctx.hero_changes(patch)] == ["Abrams"]
    assert ctx.item_changes(patch) == []
    assert ctx.system_changes(patch) == []
