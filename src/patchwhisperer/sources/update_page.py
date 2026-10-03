import html
import json
import re
from urllib.parse import urljoin

import httpx

BASE_URL = "https://www.playdeadlock.com"
UPDATE_LINK_RE = re.compile(r"playdeadlock\.com/([A-Za-z0-9_-]+)")
_MAIN_JS_RE = re.compile(r'src="([^"]*?/react/main\.js[^"]*)"')
_JSON_PARSE_RE = re.compile(r"JSON\.parse\('(.*)'\)", re.DOTALL)
_TAG_RE = re.compile(r"<[^>]+>")


def update_page_slug(contents: str) -> str | None:
    """First playdeadlock.com/<slug> link in the post that isn't a forums link."""
    for m in UPDATE_LINK_RE.finditer(contents):
        if m.group(1) != "forums":
            return m.group(1)
    return None


def _chunk_id(main_js: str, slug: str) -> str:
    # main.js maps "./<slug>_english.json": [<dep>, <chunk file id>]
    m = re.search(
        r'"?\./?' + re.escape(slug) + r'_english\.json"?\s*:\s*\[\s*\d+\s*,\s*(\d+)\s*\]',
        main_js,
    )
    if not m:
        raise RuntimeError(f"no english chunk id for slug {slug!r} in main.js")
    return m.group(1)


def _chunk_json(chunk_js: str) -> dict:
    m = _JSON_PARSE_RE.search(chunk_js)
    if m:
        payload = m.group(1)
        try:
            return json.loads(payload)
        except json.JSONDecodeError:
            # JS single-quoted strings allow \', which JSON rejects
            return json.loads(payload.replace("\\'", "'"))
    start, end = chunk_js.find("{"), chunk_js.rfind("}")
    if start != -1 and end > start:
        return json.loads(chunk_js[start : end + 1])
    raise RuntimeError("no JSON payload found in english chunk")


def fetch_update_page_text(slug: str, client: httpx.Client | None = None) -> str:
    """Fetch a JS-rendered playdeadlock.com update page as `KEY: value` lines."""
    own = client is None
    client = client or httpx.Client(timeout=30)
    try:
        r = client.get(f"{BASE_URL}/{slug}")
        if r.status_code != 200:
            raise RuntimeError(f"update page /{slug} returned {r.status_code}")
        m = _MAIN_JS_RE.search(r.text)
        if not m:
            raise RuntimeError(f"update page /{slug} has no main.js script tag")
        main_js_url = urljoin(BASE_URL, m.group(1))
        r = client.get(main_js_url)
        if r.status_code != 200:
            raise RuntimeError(f"main.js fetch returned {r.status_code}")
        chunk_id = _chunk_id(r.text, slug)
        r = client.get(f"{BASE_URL}/public/javascript/react/{chunk_id}.js")
        if r.status_code != 200:
            raise RuntimeError(f"chunk {chunk_id}.js fetch returned {r.status_code}")
        strings = _chunk_json(r.content.decode("utf-8"))
        lines = []
        for key, value in strings.items():
            if key == "language":
                continue
            text = html.unescape(_TAG_RE.sub("", str(value)))
            text = re.sub(r"\s+", " ", text).strip()
            if text:
                lines.append(f"{key}: {text}")
        return "\n".join(lines)
    finally:
        if own:
            client.close()
