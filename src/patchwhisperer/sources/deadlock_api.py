import time

import httpx

BASE = "https://api.deadlock-api.com"


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
