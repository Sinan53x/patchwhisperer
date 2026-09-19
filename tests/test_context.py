from conftest import load_post

from patchwhisperer.analysis import context as ctx
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
