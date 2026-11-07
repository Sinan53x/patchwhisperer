"""Hero tiers measured from public match data, never from model opinion."""

import time
from pathlib import Path

from pydantic import BaseModel

from patchwhisperer.kb.store import KBStore
from patchwhisperer.parse.models import Patch

SHRINK_MATCHES = 300
S_MIN_PICK_RATE = 0.05
MIN_POST_PATCH_MATCHES = 3000
PRE_PATCH_DAYS = 14
SETTLE_SECONDS = 3600
TIER_CUTS = (("S", 2.5), ("A", 1.0), ("B", -1.0), ("C", -2.5))
BANDS = (
    ("ranked", "All ranks", "ranked", None, None),
    ("high", "High rank", "ranked", 101, 116),
)


class HeroTier(BaseModel):
    tier: str
    prev_tier: str | None = None
    win_rate: float
    matches: int
    pick_rate: float
    delta: float | None = None


class TierBand(BaseModel):
    key: str
    label: str
    post_patch: bool
    matches: int
    heroes: dict[str, HeroTier]


class TierSnapshot(BaseModel):
    generated_at: int
    patch_unix: int
    bands: list[TierBand]


def tier_for(win_rate: float, matches: int, pick_rate: float, mean: float) -> str:
    score = (win_rate * matches + SHRINK_MATCHES * mean) / (matches + SHRINK_MATCHES)
    offset = (score - mean) * 100
    tier = next((name for name, cut in TIER_CUTS if offset >= cut), "D")
    if tier == "S" and pick_rate < S_MIN_PICK_RATE:
        return "A"
    return tier


def _measure(rows: list[dict]) -> dict[int, tuple[str, float, int, float]]:
    slots = sum(r["matches"] for r in rows)
    if not slots:
        return {}
    mean = sum(r["wins"] for r in rows) / slots
    total_matches = slots / 12
    out = {}
    for r in rows:
        if not r["matches"]:
            continue
        win_rate = r["wins"] / r["matches"]
        pick_rate = r["matches"] / total_matches
        out[r["hero_id"]] = (
            tier_for(win_rate, r["matches"], pick_rate, mean),
            win_rate,
            r["matches"],
            pick_rate,
        )
    return out


def build_band(
    key: str, label: str, post: list[dict], pre: list[dict], names: dict[int, str]
) -> TierBand:
    match_count = _games(post)
    post_patch = match_count >= MIN_POST_PATCH_MATCHES
    before = _measure(pre)
    current = _measure(post) if post_patch else before
    heroes = {}
    for hero_id, (tier, win_rate, matches, pick_rate) in current.items():
        if hero_id not in names:
            continue
        prior = before.get(hero_id) if post_patch else None
        heroes[names[hero_id]] = HeroTier(
            tier=tier,
            prev_tier=prior[0] if prior else None,
            win_rate=win_rate,
            matches=matches,
            pick_rate=pick_rate,
            delta=win_rate - prior[1] if prior else None,
        )
    return TierBand(
        key=key,
        label=label,
        post_patch=post_patch,
        matches=match_count if post_patch else _games(pre),
        heroes=heroes,
    )


def _games(rows: list[dict]) -> int:
    return sum(r["matches"] for r in rows) // 12


def build_snapshot(
    api, patch_unix: int, prev_patch_unix: int | None = None
) -> TierSnapshot:
    """Compare against games since the previous patch, so its effects aren't
    counted as this one's. Falls back to two weeks if those games are too few."""
    names = {h["id"]: h["name"] for h in api.heroes()}
    since = patch_unix + SETTLE_SECONDS
    two_weeks = patch_unix - PRE_PATCH_DAYS * 86400
    pre_since = max(two_weeks, (prev_patch_unix or 0) + SETTLE_SECONDS)
    bands = []
    for key, label, mode, low, high in BANDS:
        common = {"match_mode": mode, "min_average_badge": low, "max_average_badge": high}
        post = api.hero_stats(min_unix=since, **common)
        pre = api.hero_stats(min_unix=pre_since, max_unix=patch_unix, **common)
        if pre_since > two_weeks and _games(pre) < MIN_POST_PATCH_MATCHES:
            pre = api.hero_stats(min_unix=two_weeks, max_unix=patch_unix, **common)
        bands.append(build_band(key, label, post, pre, names))
    return TierSnapshot(
        generated_at=int(time.time()), patch_unix=patch_unix, bands=bands
    )


def tiers_path(patch_dir: Path) -> Path:
    return patch_dir / "tiers.json"


def load_tiers(patch_dir: Path) -> TierSnapshot | None:
    path = tiers_path(patch_dir)
    if not path.exists():
        return None
    return TierSnapshot.model_validate_json(path.read_text())


def refresh_latest(kb: KBStore, api) -> Path:
    candidates = []
    for patch_json in (kb.root / "patches").glob("*/patch.json"):
        if (patch_json.parent / "analysis.json").exists():
            patch = Patch.model_validate_json(patch_json.read_text())
            candidates.append((patch.date, patch_json.parent, patch))
    if not candidates:
        raise ValueError("no analyzed patch to refresh")
    candidates.sort(key=lambda c: (c[0], c[1].name))
    _, patch_dir, patch = candidates[-1]
    prev_unix = int(candidates[-2][0].timestamp()) if len(candidates) > 1 else None
    snapshot = build_snapshot(api, int(patch.date.timestamp()), prev_unix)
    path = tiers_path(patch_dir)
    path.write_text(snapshot.model_dump_json(indent=1))
    return path


def sync_kb_tiers(kb: KBStore, snapshot: dict) -> None:
    """Start each analysis from measured tiers, so a past guess can't compound."""
    if not snapshot or not kb.heroes_path.exists():
        return
    slots = sum(s["matches"] for s in snapshot.values())
    if not slots:
        return
    mean = sum(s["win_rate"] * s["matches"] for s in snapshot.values()) / slots
    heroes = kb.load_heroes()
    for name, s in snapshot.items():
        if name in heroes and s["matches"]:
            heroes[name].tier = tier_for(
                s["win_rate"], s["matches"], s["pick_rate"], mean
            )
    kb.save_heroes(heroes)
