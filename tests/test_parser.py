import pytest
from conftest import load_post

from patchwhisperer.parse.models import Direction, EntityType
from patchwhisperer.parse.patch_parser import parse_patch

DATES = ("09-16-2026", "08-22-2026", "05-22-2026", "03-06-2026")


@pytest.fixture(scope="module")
def patch_0916(entity_index):
    return parse_patch(load_post("09-16-2026"), entity_index)


def _find(patch, prefix: str):
    return [c for c in patch.changes if c.raw.startswith(prefix)]


def test_wraith_counts(patch_0916):
    wraith = [c for c in patch_0916.changes if c.entity_name == "Wraith"]
    assert len(wraith) == 7
    kinds = [c.direction for c in wraith]
    assert kinds.count(Direction.nerf) == 5
    assert kinds.count(Direction.buff) == 1
    assert kinds.count(Direction.fix) == 1


def test_wraith_clubs_slow_is_nerf(patch_0916):
    (c,) = _find(patch_0916, "Wraith: Card Trick T3 Clubs slow")
    assert c.direction == Direction.nerf


def test_lash_falloff_range_is_nerf(patch_0916):
    (c,) = _find(patch_0916, "Lash: Gun falloff range")
    assert c.direction == Direction.nerf


def test_global_slow_is_neutral(patch_0916):
    (c,) = _find(patch_0916, "All move slow values reduced")
    assert c.entity_type == EntityType.system
    assert c.direction == Direction.neutral


def test_warden_bullet_damage(patch_0916):
    (c,) = _find(patch_0916, "Warden: Bullet damage per boon")
    assert c.direction == Direction.nerf
    assert c.old == "0.28"
    assert c.new == "0.25"


def test_celeste_dazzling_trick(patch_0916):
    (c,) = _find(patch_0916, "Celeste: Dazzling Trick cooldown")
    assert c.direction == Direction.nerf
    assert c.ability == "Dazzling Trick"


def test_shadow_weave_cooldown(patch_0916):
    (c,) = _find(patch_0916, "Shadow Weave: Cooldown")
    assert c.entity_type == EntityType.item
    assert c.direction == Direction.buff


def test_veil_walker_rework(patch_0916):
    (c,) = _find(patch_0916, "Veil Walker: No longer builds")
    assert c.direction == Direction.rework


def test_guardian_bounty(patch_0916):
    (c,) = _find(patch_0916, "Guardian bounty increased")
    assert c.entity_type == EntityType.system
    assert c.direction == Direction.buff


def test_plated_armor_fix(patch_0916):
    (c,) = _find(patch_0916, "Plated Armor: Fixed")
    assert c.direction == Direction.fix


def test_not_hotfix(patch_0916):
    assert not patch_0916.is_hotfix()


def test_hero_resolution_rate(entity_index):
    for date in DATES:
        patch = parse_patch(load_post(date), entity_index)
        hero_lines = [c for c in patch.changes if c.section == "Heroes"]
        if not hero_lines:
            continue
        unresolved = [c.entity_name for c in hero_lines if not c.resolved]
        rate = 1 - len(unresolved) / len(hero_lines)
        assert rate >= 0.95, f"{date}: {rate:.3f}, unresolved={sorted(set(unresolved))}"
