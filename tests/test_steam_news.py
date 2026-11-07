from datetime import UTC, datetime

import httpx
import respx
from conftest import load_post

from patchwhisperer.sources.steam_news import (
    NEWS_URL,
    PostKind,
    SteamPost,
    classify_post,
    fetch_patch_posts,
    is_patch_post,
)


def _post(title: str, contents: str = "[p]hi[/p]", tags: list[str] | None = None):
    return SteamPost(
        gid="g1",
        title=title,
        date=datetime(2026, 11, 5, tzinfo=UTC),
        url="https://example.com",
        author="valve",
        contents=contents,
        tags=tags or [],
    )


@respx.mock
def test_fetch_patch_posts():
    payload = {
        "appnews": {
            "newsitems": [
                {
                    "gid": "123",
                    "title": "Minor Update",
                    "url": "https://example.com",
                    "author": "valve",
                    "contents": "[p]- x[/p]",
                    "date": 1758000000,
                },
                {
                    "gid": "456",
                    "title": "Community Spotlight",
                    "url": "https://example.com/2",
                    "author": "valve",
                    "contents": "[p]hi[/p]",
                    "date": 1758000000,
                },
            ]
        }
    }
    respx.get(NEWS_URL).mock(return_value=httpx.Response(200, json=payload))
    posts = fetch_patch_posts(count=2)
    assert len(posts) == 1
    p = posts[0]
    assert p.gid == "123"
    assert p.title == "Minor Update"
    assert p.contents == "[p]- x[/p]"


def test_is_patch_post_without_tag():
    post = load_post("03-06-2026")
    assert "patchnotes" not in post.tags
    assert is_patch_post(post)


def test_classify_ranked_season():
    assert classify_post(_post("Ranked - Beta Season 2")) == PostKind.ranked_season
    assert classify_post(_post("season rollover news")) == PostKind.ranked_season


def test_classify_balance_wins_over_season_title():
    assert classify_post(_post("Ranked Season Update")) == PostKind.balance
    assert classify_post(_post("Season hotfix")) == PostKind.balance
    assert classify_post(_post("Ranked 11-05-2026 notes")) == PostKind.balance
    assert (
        classify_post(_post("Community news", tags=["patchnotes"]))
        == PostKind.balance
    )


def test_classify_unrelated_title_stays_other():
    assert classify_post(_post("Community Spotlight")) == PostKind.other
