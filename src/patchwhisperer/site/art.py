"""Resolve hero/ability/item art and copy it into the site output.

Images are downloaded at build time (never hotlinked), cached on disk under
~/.cache/patchwhisperer/site-assets, and referenced by relative paths.
Download failures degrade to None so callers can fall back to initials.
"""

import hashlib
import shutil
from pathlib import Path
from urllib.parse import urlparse

import httpx

from patchwhisperer.kb.store import slugify

DEFAULT_CACHE_DIR = Path.home() / ".cache" / "patchwhisperer" / "site-assets"


def _fetch(url: str) -> bytes:
    r = httpx.get(url, timeout=30, follow_redirects=True)
    r.raise_for_status()
    return r.content


class SiteArt:
    """Name -> relative asset path lookups for one site build."""

    def __init__(
        self,
        api,
        assets_dir: Path,
        cache_dir: Path = DEFAULT_CACHE_DIR,
        fetch=_fetch,
    ) -> None:
        self._api = api
        self._assets_dir = assets_dir
        self._cache_dir = cache_dir
        self._fetch = fetch
        self._heroes = {h["name"]: h for h in api.heroes()}
        self._items = {i["name"]: i for i in api.items()}
        self._ability_cache: dict[int, list[dict]] = {}
        self._portraits: dict[str, str | None] = {}
        self._ability_icons: dict[tuple[str, str], str | None] = {}
        self._item_icons: dict[str, str | None] = {}

    def _place(self, url: str | None, stem: str) -> str | None:
        """Copy (downloading if needed) url into assets; return relative path."""
        if not url:
            return None
        ext = Path(urlparse(url).path).suffix.lower()
        if ext not in (".png", ".webp", ".jpg", ".jpeg", ".gif", ".svg"):
            ext = ".png"
        digest = hashlib.sha1(url.encode()).hexdigest()[:8]
        fname = f"{slugify(stem)}-{digest}{ext}"
        dest = self._assets_dir / fname
        if not dest.exists():
            cached = self._cache_dir / fname
            if not cached.exists():
                try:
                    data = self._fetch(url)
                except (httpx.HTTPError, OSError):
                    return None
                cached.parent.mkdir(parents=True, exist_ok=True)
                cached.write_bytes(data)
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(cached, dest)
        return f"assets/{fname}"

    def hero_portrait(self, name: str) -> str | None:
        if name not in self._portraits:
            hero = self._heroes.get(name)
            url = (hero or {}).get("images", {}).get("icon_image_small")
            self._portraits[name] = self._place(url, f"hero-{name}")
        return self._portraits[name]

    def _abilities(self, hero_name: str) -> list[dict]:
        hero = self._heroes.get(hero_name)
        if not hero:
            return []
        hid = hero["id"]
        if hid not in self._ability_cache:
            try:
                self._ability_cache[hid] = self._api.hero_abilities(hid)
            except (httpx.HTTPError, OSError):
                self._ability_cache[hid] = []
        return self._ability_cache[hid]

    def ability_icon(self, hero_name: str, ability: str | None) -> str | None:
        if not ability:
            return None
        key = (hero_name, ability)
        if key not in self._ability_icons:
            url = None
            lowered = ability.lower()
            for a in self._abilities(hero_name):
                if (a.get("name") or "").lower() == lowered:
                    url = a.get("image")
                    break
            self._ability_icons[key] = self._place(
                url, f"ability-{hero_name}-{ability}"
            )
        return self._ability_icons[key]

    def item_icon(self, name: str) -> str | None:
        if name not in self._item_icons:
            item = self._items.get(name) or {}
            self._item_icons[name] = self._place(
                item.get("shop_image") or item.get("image"), f"item-{name}"
            )
        return self._item_icons[name]

    def item_category(self, name: str) -> str:
        return (self._items.get(name) or {}).get("item_slot_type") or "other"

    def rank_badges(self) -> list[dict]:
        """[{tier, name, color, icon}] for the ranked tiers, low to high."""
        try:
            ranks = self._api.ranks()
        except (httpx.HTTPError, OSError, AttributeError):
            return []
        out = []
        for r in sorted(ranks, key=lambda r: r.get("tier", 0)):
            if not r.get("tier"):
                continue  # tier 0 is unranked
            images = r.get("images") or {}
            out.append(
                {
                    "tier": r["tier"],
                    "name": r.get("name", ""),
                    "color": r.get("color") or "#7c7c7c",
                    "icon": self._place(
                        images.get("small_webp") or images.get("large"),
                        f"rank-{r.get('name', r['tier'])}",
                    ),
                }
            )
        return out
