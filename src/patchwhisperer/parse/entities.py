import json
import time
from pathlib import Path

import httpx
from rapidfuzz import fuzz, process

from patchwhisperer.parse.models import EntityType

ASSETS_BASE = "https://api.deadlock-api.com/v1/assets"
CACHE_PATH = Path.home() / ".cache" / "patchwhisperer" / "assets.json"
CACHE_TTL = 24 * 3600

ALIASES = {
    "doorman": "The Doorman",
    "geist": "Lady Geist",
    "mo and krill": "Mo & Krill",
    "mo & krill": "Mo & Krill",
    "gray talon": "Grey Talon",
    "mcginnis": "McGinnis",
    "vindcita": "Vindicta",
}


class EntityIndex:
    def __init__(
        self,
        heroes: list[dict],
        items: list[dict],
        abilities: dict[int, list[str]],
    ) -> None:
        self.heroes = heroes
        self.items = items
        # hero_id -> ability display names
        self.abilities = abilities
        self._names: dict[str, tuple[EntityType, int, str]] = {}
        for h in heroes:
            self._names[h["name"].lower()] = (EntityType.hero, h["id"], h["name"])
        for it in items:
            self._names.setdefault(
                it["name"].lower(), (EntityType.item, it["id"], it["name"])
            )

    # -- construction -------------------------------------------------

    @classmethod
    def fetch(cls, client: httpx.Client | None = None) -> "EntityIndex":
        own = client is None
        client = client or httpx.Client(timeout=60)
        try:
            heroes = client.get(
                f"{ASSETS_BASE}/heroes", params={"only_active": "true"}
            ).json()
            if not isinstance(heroes, list) or not heroes:
                heroes = client.get(f"{ASSETS_BASE}/heroes").json()
            items = client.get(
                f"{ASSETS_BASE}/items", params={"type": "upgrade"}
            ).json()
            if any("shopable" in it for it in items):
                shopable = [it for it in items if it.get("shopable")]
                if shopable:
                    items = shopable
            abilities: dict[int, list[str]] = {}
            for h in heroes:
                try:
                    abs_ = client.get(
                        f"{ASSETS_BASE}/items/by-hero-id/{h['id']}"
                    ).json()
                    abilities[h["id"]] = [
                        a["name"]
                        for a in abs_
                        if a.get("type") == "ability" and a.get("name")
                    ]
                except httpx.HTTPError:
                    abilities[h["id"]] = []
            idx = cls(heroes, items, abilities)
            idx.save_cache()
            return idx
        finally:
            if own:
                client.close()

    @classmethod
    def load(cls, client: httpx.Client | None = None) -> "EntityIndex":
        if CACHE_PATH.exists() and time.time() - CACHE_PATH.stat().st_mtime < CACHE_TTL:
            data = json.loads(CACHE_PATH.read_text())
            return cls(
                data["heroes"],
                data["items"],
                {int(k): v for k, v in data["abilities"].items()},
            )
        return cls.fetch(client)

    def save_cache(self, path: Path = CACHE_PATH) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(
                {
                    "heroes": self.heroes,
                    "items": self.items,
                    "abilities": self.abilities,
                }
            )
        )

    # -- lookup ---------------------------------------------------------

    def resolve(self, name: str) -> tuple[EntityType, int, str] | None:
        key = name.strip().lower()
        key = ALIASES.get(key, key).lower()
        if key in self._names:
            return self._names[key]
        match = process.extractOne(
            key, list(self._names), scorer=fuzz.WRatio, score_cutoff=90
        )
        if match:
            return self._names[match[0]]
        return None

    def ability_for(self, hero_id: int, text: str) -> str | None:
        text_l = text.lower()
        best = None
        for name in self.abilities.get(hero_id, []):
            if name.lower() in text_l and (best is None or len(name) > len(best)):
                best = name
        return best
