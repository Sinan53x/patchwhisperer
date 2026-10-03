import json
import time
from pathlib import Path

import httpx
from pydantic import BaseModel

BASE = "https://api.deadlock-api.com"
CACHE_DIR = Path.home() / ".cache" / "patchwhisperer"


class ItemUsage(BaseModel):
    item: str
    share: float
    win_rate: float
    avg_buy_min: float
    slot: str | None = None
    tier: int | None = None


class Counters(BaseModel):
    beats: list[tuple[str, float, int]] = []
    loses_to: list[tuple[str, float, int]] = []


class DeadlockAPI:
    def __init__(self, client: httpx.Client | None = None) -> None:
        self._own = client is None
        self.client = client or httpx.Client(timeout=60)

    def close(self) -> None:
        if self._own:
            self.client.close()

    def _get(self, path: str, **params) -> list | dict:
        r = self.client.get(f"{BASE}{path}", params=params or None)
        r.raise_for_status()
        return r.json()

    def heroes(self) -> list[dict]:
        return self._get("/v1/assets/heroes", only_active="true")

    def all_heroes(self) -> list[dict]:
        return self._get("/v1/assets/heroes")

    def hero_abilities(self, hero_id: int) -> list[dict]:
        return self._get(f"/v1/assets/items/by-hero-id/{hero_id}")

    def items(self, type: str = "upgrade") -> list[dict]:
        return self._get("/v1/assets/items", type=type)

    def hero_stats(
        self,
        min_unix: int,
        max_unix: int | None = None,
        min_average_badge: int | None = None,
    ) -> list[dict]:
        params: dict = {"min_unix_timestamp": min_unix}
        if max_unix is not None:
            params["max_unix_timestamp"] = max_unix
        if min_average_badge is not None:
            params["min_average_badge"] = min_average_badge
        return self._get("/v1/analytics/hero-stats", **params)

    def snapshot(self, days: int = 14, min_average_badge: int = 100) -> dict[str, dict]:
        stats = self.hero_stats(
            min_unix=int(time.time()) - days * 86400,
            min_average_badge=min_average_badge,
        )
        name_by_id = {h["id"]: h["name"] for h in self.heroes()}
        total_matches = sum(s["matches"] for s in stats)
        total_players = total_matches / 12 if total_matches else 1
        snap: dict[str, dict] = {}
        for s in stats:
            name = name_by_id.get(s["hero_id"], str(s["hero_id"]))
            matches = s["matches"]
            snap[name] = {
                "hero_id": s["hero_id"],
                "matches": matches,
                "win_rate": s["wins"] / matches if matches else 0.0,
                "pick_rate": matches / total_players if total_players else 0.0,
            }
        return snap

    def hero_build_stats(self, hero_id: int) -> list[dict]:
        # NOTE: returns per-build aggregates (hero_build_id, wins, losses,
        # matches, players), not per-item rows. Best-effort: sorted by matches.
        data = self._get(f"/v1/analytics/hero-build-stats/{hero_id}")
        if isinstance(data, list):
            return sorted(data, key=lambda b: b.get("matches", 0), reverse=True)
        return [data]

    # -- analytics with daily disk cache ---------------------------------

    def _get_cached(self, cache_key: str, path: str, **params):
        cache_file = CACHE_DIR / f"{cache_key}-{time.strftime('%Y%m%d')}.json"
        if cache_file.exists():
            return json.loads(cache_file.read_text())
        data = self._get(path, **params)
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        cache_file.write_text(json.dumps(data))
        return data

    def hero_item_usage(
        self,
        hero_id: int,
        index,
        *,
        days: int = 30,
        min_badge: int = 100,
        top: int = 15,
    ) -> list[ItemUsage]:
        rows = self._get_cached(
            f"item-stats-{hero_id}-{days}d",
            "/v1/analytics/item-stats",
            hero_id=hero_id,
            min_unix_timestamp=int(time.time()) - days * 86400,
            min_average_badge=min_badge,
        )
        hero_rows = self.hero_stats(
            min_unix=int(time.time()) - days * 86400, min_average_badge=min_badge
        )
        hero_matches = next(
            (s["matches"] for s in hero_rows if s["hero_id"] == hero_id), 0
        )
        item_by_id = {it["id"]: it for it in index.items}
        out = []
        for r in rows:
            it = item_by_id.get(r["item_id"])
            if it is None or not hero_matches:
                continue
            out.append(
                ItemUsage(
                    item=it["name"],
                    share=r["matches"] / hero_matches,
                    win_rate=r["wins"] / r["matches"] if r["matches"] else 0.0,
                    avg_buy_min=(r.get("avg_buy_time_s") or 0) / 60,
                    slot=it.get("item_slot_type"),
                    tier=it.get("item_tier"),
                )
            )
        out.sort(key=lambda u: -u.share)
        return out[:top]

    def hero_counters(
        self, *, days: int = 30, min_badge: int = 100, min_matches: int = 150
    ) -> dict[int, Counters]:
        rows = self._get_cached(
            f"counter-stats-{days}d",
            "/v1/analytics/hero-counter-stats",
            min_unix_timestamp=int(time.time()) - days * 86400,
            min_average_badge=min_badge,
        )
        name_by_id = {h["id"]: h["name"] for h in self.heroes()}
        by_hero: dict[int, list[tuple[str, float, int]]] = {}
        for r in rows:
            n = r.get("matches_played") or r.get("matches") or 0
            if n < min_matches:
                continue
            wr = r["wins"] / n if n else 0.0
            enemy = name_by_id.get(r["enemy_hero_id"])
            if enemy:
                by_hero.setdefault(r["hero_id"], []).append((enemy, wr, n))
        out = {}
        for hid, pairs in by_hero.items():
            pairs.sort(key=lambda p: -p[1])
            out[hid] = Counters(beats=pairs[:5], loses_to=pairs[-5:][::-1])
        return out
