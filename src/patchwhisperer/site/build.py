"""Build the static site from kb/patches directories."""

import hashlib
import json
import shutil
from pathlib import Path

from jinja2 import Environment, PackageLoader
from pydantic import ValidationError

from patchwhisperer.analysis.schemas import AnalysisBundle, HeroEntry
from patchwhisperer.analysis.tiers import load_tiers
from patchwhisperer.parse.models import Patch
from patchwhisperer.site.art import DEFAULT_CACHE_DIR, SiteArt
from patchwhisperer.site.page import ArchiveEntry, build_page_model

STATIC_DIR = "static"


def _asset_version(name: str) -> str:
    """Short content hash of a bundled static asset, for cache busting."""
    data = (Path(__file__).parent / STATIC_DIR / name).read_bytes()
    return hashlib.sha256(data).hexdigest()[:8]


def _env() -> Environment:
    return Environment(
        loader=PackageLoader("patchwhisperer.site", "templates"),
        autoescape=True,
    )


def load_analysis(path: Path) -> AnalysisBundle:
    """Parse analysis.json; drop hero entries that fail validation.

    Older runs predate newer HeroEntry fields and may contain junk entries
    (e.g. an empty hero name). The boundary stays strict everywhere else.
    """
    data = json.loads(path.read_text())
    data.pop("pool", None)
    heroes = data.get("heroes")
    if isinstance(heroes, dict):
        kept = []
        for raw in heroes.get("heroes", []):
            try:
                HeroEntry.model_validate(raw)
            except ValidationError:
                continue
            kept.append(raw)
        heroes["heroes"] = kept
    return AnalysisBundle.model_validate(data)


def _patch_dirs(kb: Path) -> list[tuple[Path, AnalysisBundle, Patch]]:
    patches_dir = kb / "patches"
    found = []
    if not patches_dir.is_dir():
        return found
    for d in sorted(patches_dir.iterdir()):
        if not d.is_dir():
            continue
        analysis_path = d / "analysis.json"
        patch_path = d / "patch.json"
        if not (analysis_path.exists() and patch_path.exists()):
            continue
        found.append(
            (
                d,
                load_analysis(analysis_path),
                Patch.model_validate_json(patch_path.read_text()),
            )
        )
    return found


def _wipe(out: Path) -> None:
    """Remove stale output, only inside the out dir."""
    if not out.exists():
        return
    for child in out.iterdir():
        if child.is_dir() and not child.is_symlink():
            shutil.rmtree(child)
        else:
            child.unlink()


def build_site(
    kb: Path,
    out: Path,
    api=None,
    cache_dir: Path = DEFAULT_CACHE_DIR,
    fetch=None,
) -> int:
    """Build all patch pages + archive into `out`. Returns page count."""
    from patchwhisperer.sources.deadlock_api import DeadlockAPI

    entries = _patch_dirs(kb)
    out.mkdir(parents=True, exist_ok=True)
    _wipe(out)

    env = _env()
    patch_tpl = env.get_template("patch.html")
    archive_tpl = env.get_template("archive.html")
    asset_v = {"css_v": _asset_version("style.css"), "js_v": _asset_version("app.js")}

    for name in (STATIC_DIR,):
        src = Path(__file__).parent / name
        shutil.copytree(src, out, dirs_exist_ok=True)

    if not entries:
        return 0

    assets_dir = out / "assets"
    assets_dir.mkdir(exist_ok=True)
    art_kwargs = {"fetch": fetch} if fetch else {}
    art = SiteArt(
        api or DeadlockAPI(),
        assets_dir,
        cache_dir=cache_dir,
        **art_kwargs,
    )

    dated = sorted(
        entries, key=lambda e: (e[2].date, e[0].name), reverse=True
    )
    archive_entries: list[ArchiveEntry] = []
    for patch_dir, analysis, patch in dated:
        page = build_page_model(analysis, patch, art, load_tiers(patch_dir))
        dest = out / "patches" / patch_dir.name
        dest.mkdir(parents=True, exist_ok=True)
        html = patch_tpl.render(page=page, rel="../../", **asset_v)
        (dest / "index.html").write_text(html)
        archive_entries.append(
            ArchiveEntry(
                patch_id=patch_dir.name,
                title=page.title,
                date_display=page.date_display,
                headline=page.headline,
                patch_size=page.patch_size,
            )
        )

    latest_dir, latest_analysis, latest_patch = dated[0]
    latest_page = build_page_model(
        latest_analysis, latest_patch, art, load_tiers(latest_dir)
    )
    (out / "index.html").write_text(
        patch_tpl.render(page=latest_page, rel="", **asset_v)
    )

    (out / "patches" / "index.html").write_text(
        archive_tpl.render(entries=archive_entries, rel="../", **asset_v)
    )
    return len(entries)
