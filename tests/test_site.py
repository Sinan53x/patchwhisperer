import json
from pathlib import Path

import pytest

from patchwhisperer.analysis.schemas import HeroEntry
from patchwhisperer.parse.models import Change, Direction, EntityType, Patch
from patchwhisperer.site.build import build_site, load_analysis
from patchwhisperer.site.page import _driving_deltas, build_page_model

FIXTURES = Path(__file__).parent / "fixtures" / "site"
KB = FIXTURES / "kb"
PATCH_DIR = KB / "patches" / "2026-01-01-111"

HERO_NAMES = [
    "Infernus", "Seven", "Vindicta", "Lady Geist", "Abrams", "Wraith",
    "McGinnis", "Paradox", "Dynamo", "Kelvin", "Haze", "Holliday", "Bebop",
    "Calico", "Grey Talon", "Mo & Krill", "Shiv", "Ivy", "Warden", "Yamato",
    "Lash", "Viscous", "Pocket", "Mirage", "Vyper", "Sinclair", "Mina",
    "Drifter", "Venator", "Victor", "Paige", "The Doorman", "Billy", "Graves",
]


class FakeAPI:
    def heroes(self):
        return [
            {
                "id": i + 1,
                "name": n,
                "images": {
                    "icon_image_small": f"https://img.example/{i}.png"
                },
            }
            for i, n in enumerate(HERO_NAMES)
        ]

    def hero_abilities(self, hero_id):
        return {
            1: [{"name": "Afterburn",
                 "image": "https://img.example/afterburn.png",
                 "type": "ability"}],
            5: [{"name": "Seismic Impact",
                 "image": "https://img.example/seismic.png",
                 "type": "ability"}],
            6: [{"name": "Full Auto",
                 "image": "https://img.example/fullauto.png",
                 "type": "ability"}],
        }.get(hero_id, [])

    def items(self, type="upgrade"):
        return [
            {"name": "Cultist Sacrifice", "item_slot_type": "weapon",
             "shop_image": "https://img.example/cultist.png"},
            {"name": "Tesla Bullets", "item_slot_type": "spirit",
             "image": "https://img.example/tesla.png"},
        ]


def ok_fetch(url):
    return b"PNG" + url.encode()


def bad_fetch(url):
    raise OSError("offline")


def build(tmp_path, fetch=ok_fetch):
    out = tmp_path / "dist"
    n = build_site(
        kb=KB, out=out, api=FakeAPI(),
        cache_dir=tmp_path / "cache", fetch=fetch,
    )
    return out, n


@pytest.fixture
def built(tmp_path):
    return build(tmp_path)


def patch_html(out):
    return (out / "patches" / "2026-01-01-111" / "index.html").read_text()


def all_html(out):
    return "\n".join(p.read_text() for p in out.rglob("*.html"))


def test_build_skips_dirs_missing_either_file(built):
    out, n = built
    assert n == 1
    assert (out / "index.html").exists()
    assert (out / "patches" / "index.html").exists()
    assert (out / "patches" / "2026-01-01-111" / "index.html").exists()
    assert not (out / "patches" / "2026-01-02-222").exists()
    assert not (out / "patches" / "empty-dir").exists()


def test_writes_static_assets(built):
    out, _ = built
    assert (out / "style.css").exists()
    assert (out / "app.js").exists()
    assert any((out / "assets").iterdir())


def test_subpath_safe_relative_links(built):
    out, _ = built
    index = (out / "index.html").read_text()
    page = patch_html(out)
    assert 'href="style.css"' in index
    assert 'src="app.js"' in index
    assert 'href="../../style.css"' in page
    assert 'src="../../app.js"' in page
    for html in (index, page):
        assert 'href="/' not in html
        assert 'src="/' not in html


def test_null_verdict_falls_back_to_direction(built):
    out, _ = built
    html = patch_html(out)
    assert 'data-slug="wraith" data-verdict=""' in html
    wraith = html.split('id="sheet-hero-wraith"', 1)[1].split("</article>", 1)[0]
    assert 'badge v-bench">down<' in wraith


def test_missing_image_falls_back_to_initials(tmp_path):
    out, _ = build(tmp_path, fetch=bad_fetch)
    html = patch_html(out)
    assert 'class="initials"' in html
    assert 'src="../../assets/' not in html


def test_one_liner_is_escaped(built):
    out, _ = built
    html = patch_html(out)
    assert "&lt;script&gt;alert" in html
    assert "<script>alert" not in html
    assert 'alert("x")' not in html


def test_pool_data_never_published(built):
    out, _ = built
    assert "POOL_SECRET_SHHH" not in all_html(out)


def test_empty_rows_fall_back_to_patch_changes(built):
    out, _ = built
    html = patch_html(out)
    abrams = html.split('id="sheet-hero-abrams"', 1)[1].split("</article>", 1)[0]
    assert "Seismic Impact cooldown increased from 20s to 24s" in abrams
    assert "e-bad" in abrams


def test_stale_output_is_removed(tmp_path):
    out = tmp_path / "dist"
    out.mkdir()
    (out / "stale.txt").write_text("old")
    stale_dir = out / "old-dir"
    stale_dir.mkdir()
    (stale_dir / "x").write_text("y")
    build_site(
        kb=KB, out=out, api=FakeAPI(),
        cache_dir=tmp_path / "cache", fetch=ok_fetch,
    )
    assert not (out / "stale.txt").exists()
    assert not stale_dir.exists()


def test_rebuild_is_idempotent(tmp_path):
    out1, _ = build(tmp_path)
    snapshot1 = {
        str(p.relative_to(out1)): p.read_bytes()
        for p in sorted(out1.rglob("*"))
        if p.is_file()
    }
    out2 = tmp_path / "dist2"
    build_site(
        kb=KB, out=out2, api=FakeAPI(),
        cache_dir=tmp_path / "cache2", fetch=ok_fetch,
    )
    snapshot2 = {
        str(p.relative_to(out2)): p.read_bytes()
        for p in sorted(out2.rglob("*"))
        if p.is_file()
    }
    assert snapshot1.keys() == snapshot2.keys()


class FakeArt:
    def hero_portrait(self, name):
        return "assets/p.png"

    def ability_icon(self, hero, ability):
        return "assets/a.png" if ability else None

    def item_icon(self, name):
        return "assets/i.png"

    def item_category(self, name):
        return "weapon"


def _fixture_page(mutate=None):
    analysis = load_analysis(PATCH_DIR / "analysis.json")
    patch = Patch.model_validate_json((PATCH_DIR / "patch.json").read_text())
    if mutate:
        mutate(analysis, patch)
    return build_page_model(analysis, patch, FakeArt())


def test_unresolved_note_entity_is_a_system_not_a_hero():
    def add_mid_boss(analysis, patch):
        patch.changes.append(
            Change(
                section="General",
                entity_type=EntityType.unknown,
                entity_name="Mid-Boss",
                raw="Mid-Boss: Health increased by 20%",
                direction=Direction.neutral,
                resolved=False,
            )
        )
        analysis.heroes.heroes.append(
            HeroEntry(hero="Mid-Boss", direction="up", magnitude="major", one_liner="Tougher")
        )

    page = _fixture_page(add_mid_boss)
    assert "Mid-Boss" not in {h.name for h in page.heroes}
    assert "mid-boss" not in {h["slug"] for h in page.picker}
    mid_boss = next(s for s in page.systems if s.name == "Mid-Boss")
    assert mid_boss.change_summary == "Tougher"


def test_board_groups_come_from_the_notes_not_the_model_flag():
    def lie(analysis, patch):
        for h in analysis.heroes.heroes:
            h.in_notes = not h.in_notes

    page = _fixture_page(lie)
    direct = {
        c.entity_name
        for c in Patch.model_validate_json((PATCH_DIR / "patch.json").read_text()).changes
        if c.entity_type == EntityType.hero
    }
    for h in page.heroes:
        assert h.in_notes == (h.name in direct)
        if h.in_notes:
            assert h.board_group in {"buff", "nerf", "rework"}


def test_system_deltas_read_the_numbers_out_of_note_lines():
    deltas = _driving_deltas(
        [
            "Haunts base bounty and growth increased by 10%",
            "Comeback gold from non-hero sources increased from a max of 26% to 30% (when behind)",
            "Breakables growth reduced by 10%",
            "Steam Vents now grant stamina",
        ]
    )
    assert [(d.label, d.value, d.direction) for d in deltas] == [
        ("Haunts base bounty and growth", "+10%", "up"),
        ("Comeback gold from non-hero sources", "26% → 30%", "up"),
        ("Breakables growth", "-10%", "down"),
    ]


def test_item_detail_is_not_rendered_inside_the_grid(built):
    out, _ = built
    html = patch_html(out)
    grid = html.split('id="items"', 1)[1].split("</section>", 1)[0]
    assert "<details" not in grid
    assert 'data-sheet="item-' in grid
    assert 'id="sheet-item-' in html


def test_page_model_hero_sort():
    page = _fixture_page()
    assert page.headline == "Comeback gold moves to the jungle."
    assert page.heroes[0].name == "Infernus"  # major magnitude first
    infernus = page.heroes[0]
    assert infernus.tier_chip == "A → S"
    assert {c for g in infernus.groups for c in (g.ability,)} == {
        "Afterburn", None
    }
    wraith = next(h for h in page.heroes if h.name == "Wraith")
    assert wraith.badge_word == "down"
    vindicta = next(h for h in page.heroes if h.name == "Vindicta")
    assert vindicta.badge_word == "watch"


def test_lenient_load_drops_invalid_hero_entry():
    analysis = load_analysis(PATCH_DIR / "analysis.json")
    assert analysis.heroes is not None
    assert len(analysis.heroes.heroes) == 34
    assert all(h.hero for h in analysis.heroes.heroes)


def test_archive_lists_patch(built):
    out, _ = built
    html = (out / "patches" / "index.html").read_text()
    assert 'href="2026-01-01-111/"' in html
    assert "Fixture Update" in html


def test_items_render_with_direction_badges(built):
    out, _ = built
    html = patch_html(out)
    assert "d-rework" in html
    assert "d-nerf" in html
    assert "d-buff" in html
    for cat in ("weapon", "spirit", "other"):
        assert f'class="cat">{cat}<' in html


def test_empty_kb_builds_nothing(tmp_path):
    out = tmp_path / "dist"
    n = build_site(
        kb=tmp_path / "nope", out=out, api=FakeAPI(),
        cache_dir=tmp_path / "cache", fetch=ok_fetch,
    )
    assert n == 0
    assert not (out / "index.html").exists()


def test_downloads_are_cached(tmp_path):
    calls = []

    def counting_fetch(url):
        calls.append(url)
        return b"PNG" + url.encode()

    out = tmp_path / "dist"
    cache = tmp_path / "cache"
    build_site(
        kb=KB, out=out, api=FakeAPI(),
        cache_dir=cache, fetch=counting_fetch,
    )
    first = len(calls)
    assert first > 0
    build_site(
        kb=KB, out=tmp_path / "dist2", api=FakeAPI(),
        cache_dir=cache, fetch=counting_fetch,
    )
    assert len(calls) == first


def test_picker_payload_is_json_safe(built):
    out, _ = built
    html = patch_html(out)
    marker = "window.PW_POOL = "
    payload = html.split(marker, 1)[1].split(";", 1)[0]
    heroes = json.loads(payload)
    assert {h["slug"] for h in heroes} >= {"infernus", "abrams", "wraith"}
    assert "<" not in payload


def test_board_follows_the_notes_kind_not_the_net_direction():
    def buffed_but_hurt_by_items(analysis, patch):
        h = next(h for h in analysis.heroes.heroes if h.hero == "Abrams")
        h.direction = "down"
        h.change_kind = "buff"
        h.change_size = "moderate"

    page = _fixture_page(buffed_but_hurt_by_items)
    abrams = next(h for h in page.heroes if h.name == "Abrams")
    assert abrams.board_group == "buff"
    assert abrams.kind_word == "Buffed"
    assert abrams.chevrons == 2
