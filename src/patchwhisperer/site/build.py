"""Build the static site from kb/patches directories."""

import hashlib
import json
import shutil
from datetime import UTC, date, datetime
from pathlib import Path

from jinja2 import Environment, PackageLoader
from pydantic import ValidationError

from patchwhisperer.analysis.schemas import (
    AnalysisBundle,
    HeroEntry,
    SeasonBundle,
)
from patchwhisperer.analysis.tiers import load_tiers
from patchwhisperer.parse.models import Patch
from patchwhisperer.site.art import DEFAULT_CACHE_DIR, SiteArt
from patchwhisperer.site.page import (
    ArchiveEntry,
    _parse_date,
    build_page_model,
    build_season_model,
    fmt_date,
)

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


def _season_dirs(kb: Path) -> list[tuple[Path, SeasonBundle]]:
    patches_dir = kb / "patches"
    found = []
    if not patches_dir.is_dir():
        return found
    for d in sorted(patches_dir.iterdir()):
        if not d.is_dir() or (d / "analysis.json").exists():
            continue
        season_path = d / "season.json"
        if season_path.exists():
            found.append(
                (d, SeasonBundle.model_validate_json(season_path.read_text()))
            )
    return found


def _season_start(bundle: SeasonBundle) -> date | None:
    return _parse_date(bundle.starts) or _parse_date(bundle.date)


def _reset_on(patch: Patch, season_starts: list[date], today: date) -> str | None:
    """Display date of the first rank reset inside the patch's data window."""
    hit = min(
        (d for d in season_starts if patch.date.date() <= d <= today),
        default=None,
    )
    return f"{hit:%b} {hit.day}" if hit else None


def _season_banner(
    seasons: list[tuple[Path, SeasonBundle]], today: date
) -> dict | None:
    """One-line banner for the index when a season started in the last 30 days."""
    newest = max(
        ((d, b) for d, b in seasons if _season_start(b)),
        key=lambda s: _season_start(s[1]),
        default=None,
    )
    if newest is None:
        return None
    started = _season_start(newest[1])
    if not (0 <= (today - started).days <= 30):
        return None
    return {
        "href": f"patches/{newest[0].name}/",
        "text": (
            f"Ranked {newest[1].season_name or newest[1].title} started "
            f"{started:%b} {started.day} · see what changed"
        ),
    }


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
    today: date | None = None,
) -> int:
    """Build all patch + season pages and the archive into `out`."""
    from patchwhisperer.sources.deadlock_api import DeadlockAPI

    entries = _patch_dirs(kb)
    seasons = _season_dirs(kb)
    out.mkdir(parents=True, exist_ok=True)
    _wipe(out)

    env = _env()
    patch_tpl = env.get_template("patch.html")
    season_tpl = env.get_template("season.html")
    archive_tpl = env.get_template("archive.html")
    asset_v = {"css_v": _asset_version("style.css"), "js_v": _asset_version("app.js")}

    for name in (STATIC_DIR,):
        src = Path(__file__).parent / name
        shutil.copytree(src, out, dirs_exist_ok=True)

    if not entries and not seasons:
        return 0

    today = today or datetime.now(tz=UTC).date()
    pages = 0
    archive_entries: list[tuple[tuple, ArchiveEntry]] = []
    season_starts = sorted(
        d for d in (_season_start(b) for _, b in seasons) if d
    )

    assets_dir = out / "assets"
    assets_dir.mkdir(exist_ok=True)
    art_kwargs = {"fetch": fetch} if fetch else {}
    art = SiteArt(
        api or DeadlockAPI(),
        assets_dir,
        cache_dir=cache_dir,
        **art_kwargs,
    )

    if entries:
        dated = sorted(
            entries, key=lambda e: (e[2].date, e[0].name), reverse=True
        )
        for patch_dir, analysis, patch in dated:
            reset_on = _reset_on(patch, season_starts, today)
            page = build_page_model(
                analysis, patch, art, load_tiers(patch_dir), reset_on=reset_on
            )
            dest = out / "patches" / patch_dir.name
            dest.mkdir(parents=True, exist_ok=True)
            html = patch_tpl.render(page=page, rel="../../", **asset_v)
            (dest / "index.html").write_text(html)
            archive_entries.append(
                ((patch.date.isoformat(), patch_dir.name), ArchiveEntry(
                    patch_id=patch_dir.name,
                    title=page.title,
                    date_display=page.date_display,
                    headline=page.headline,
                    label=page.patch_size,
                ))
            )
            pages += 1

        latest_dir, latest_analysis, latest_patch = dated[0]
        latest_page = build_page_model(
            latest_analysis,
            latest_patch,
            art,
            load_tiers(latest_dir),
            reset_on=_reset_on(latest_patch, season_starts, today),
        )
        (out / "index.html").write_text(
            patch_tpl.render(
                page=latest_page,
                rel="",
                banner=_season_banner(seasons, today),
                **asset_v,
            )
        )

    ranks = art.rank_badges() if seasons else []
    for season_dir, bundle in seasons:
        page = build_season_model(bundle, season_dir.name, today, ranks)
        dest = out / "patches" / season_dir.name
        dest.mkdir(parents=True, exist_ok=True)
        (dest / "index.html").write_text(
            season_tpl.render(page=page, rel="../../", **asset_v)
        )
        archive_entries.append(
            ((bundle.date or bundle.starts, season_dir.name), ArchiveEntry(
                patch_id=season_dir.name,
                title=bundle.title or bundle.season_name,
                date_display=fmt_date(bundle.date or bundle.starts),
                headline=bundle.headline,
                label="Ranked season",
            ))
        )
        pages += 1

    (out / "patches" / "index.html").write_text(
        archive_tpl.render(
            entries=[
                e for _, e in sorted(
                    archive_entries, key=lambda t: t[0], reverse=True
                )
            ],
            rel="../",
            **asset_v,
        )
    )
    return pages
