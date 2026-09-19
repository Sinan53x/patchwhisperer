import re
from datetime import UTC, datetime

import httpx
from pydantic import BaseModel, Field

NEWS_URL = "https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/"
APP_ID = 1422450

_DATE_TITLE_RE = re.compile(r"\b\d{2}-\d{2}-\d{4}\b")
_UPDATE_TITLE_RE = re.compile(r"update|hotfix", re.IGNORECASE)


class SteamPost(BaseModel):
    gid: str
    title: str
    date: datetime
    url: str
    author: str
    contents: str
    tags: list[str] = Field(default_factory=list)


def is_patch_post(post: SteamPost) -> bool:
    return (
        "patchnotes" in post.tags
        or bool(_DATE_TITLE_RE.search(post.title))
        or bool(_UPDATE_TITLE_RE.search(post.title))
    )


def _to_post(it: dict) -> SteamPost:
    return SteamPost(
        gid=str(it["gid"]),
        title=it["title"],
        date=datetime.fromtimestamp(it["date"], tz=UTC),
        url=it["url"],
        author=it.get("author", ""),
        contents=it["contents"],
        tags=it.get("tags") or [],
    )


def fetch_posts(count: int = 20, client: httpx.Client | None = None) -> list[SteamPost]:
    """All community announcements, unfiltered."""
    own = client is None
    client = client or httpx.Client(timeout=30)
    try:
        r = client.get(
            NEWS_URL,
            params={
                "appid": APP_ID,
                "feeds": "steam_community_announcements",
                "maxlength": 0,
                "format": "json",
                "count": count,
            },
        )
        r.raise_for_status()
        items = r.json()["appnews"]["newsitems"]
        return [_to_post(it) for it in items]
    finally:
        if own:
            client.close()


def fetch_patch_posts(
    count: int = 20, client: httpx.Client | None = None
) -> list[SteamPost]:
    """Announcements filtered down to patch/hotfix posts."""
    return [p for p in fetch_posts(count=count, client=client) if is_patch_post(p)]


def fetch_post(gid: str, client: httpx.Client | None = None) -> SteamPost | None:
    # the API has no by-gid endpoint; fetch a large window and filter
    for post in fetch_posts(count=200, client=client):
        if post.gid == str(gid):
            return post
    return None
