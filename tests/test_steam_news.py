import httpx
import respx
from conftest import load_post

from patchwhisperer.sources.steam_news import (
    NEWS_URL,
    fetch_patch_posts,
    is_patch_post,
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
