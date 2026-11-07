import json

from patchwhisperer.site.notify import new_page_dirs, notify


def _kb(tmp_path):
    patch = tmp_path / "patches" / "2026-11-05-1"
    patch.mkdir(parents=True)
    (patch / "analysis.json").write_text(
        json.dumps({"patch_title": "x", "synthesis": {"headline": "Baba trimmed."}})
    )
    (patch / "patch.json").write_text(json.dumps({"title": "Minor Update"}))
    season = tmp_path / "patches" / "2026-11-05-2"
    season.mkdir()
    (season / "season.json").write_text(
        json.dumps({"season_name": "Beta Season 2", "headline": "Shields cut."})
    )
    return tmp_path


class _Resp:
    def raise_for_status(self):
        pass


def test_only_new_page_files_count():
    added = [
        "kb/patches/a/analysis.json",
        "kb/patches/a/stage1.json",
        "kb/patches/b/tiers.json",
        "kb/patches/c/season.json",
        "kb/heroes.yaml",
    ]
    assert new_page_dirs(added) == ["a", "c"]


def test_posts_one_link_per_new_page(tmp_path):
    kb = _kb(tmp_path)
    posts = []
    sent = notify(
        "https://hook",
        kb,
        ["kb/patches/2026-11-05-1/analysis.json", "kb/patches/2026-11-05-2/season.json"],
        post=lambda url, json, timeout: posts.append(json["content"]) or _Resp(),
    )
    assert sent == ["2026-11-05-1", "2026-11-05-2"]
    assert posts[0].startswith("**New patch: Minor Update**\nBaba trimmed.\n")
    assert posts[0].endswith("/patches/2026-11-05-1/")
    assert posts[1].startswith("**New ranked season: Beta Season 2**")


def test_nothing_new_posts_nothing(tmp_path):
    assert notify("https://hook", _kb(tmp_path), ["kb/patches/x/tiers.json"], post=None) == []
