"""Ping a Discord webhook with a link when a new page goes live."""

import json
from pathlib import Path

import httpx

SITE = "https://patch-whisperer.plaid-earth.workers.dev"
PAGE_FILES = ("analysis.json", "season.json")


def new_page_dirs(added: list[str]) -> list[str]:
    """Patch dir names whose page file was added, from `git diff --name-only`."""
    dirs = []
    for path in added:
        parts = Path(path).parts
        is_page = len(parts) == 4 and parts[:2] == ("kb", "patches")
        if is_page and parts[3] in PAGE_FILES and parts[2] not in dirs:
            dirs.append(parts[2])
    return dirs


def page_message(patch_dir: Path) -> str:
    url = f"{SITE}/patches/{patch_dir.name}/"
    season = patch_dir / "season.json"
    if season.exists():
        data = json.loads(season.read_text())
        title = f"New ranked season: {data.get('season_name') or data.get('title')}"
        headline = data.get("headline", "")
    else:
        analysis = json.loads((patch_dir / "analysis.json").read_text())
        patch = json.loads((patch_dir / "patch.json").read_text())
        title = f"New patch: {patch.get('title') or analysis.get('patch_title')}"
        headline = (analysis.get("synthesis") or {}).get("headline", "")
    lines = [f"**{title}**"]
    if headline:
        lines.append(headline)
    lines.append(url)
    return "\n".join(lines)


def notify(webhook: str, kb: Path, added: list[str], post=httpx.post) -> list[str]:
    """Post one message per new page; returns the dir names announced."""
    sent = []
    for name in new_page_dirs(added):
        patch_dir = kb / "patches" / name
        if not patch_dir.is_dir():
            continue
        r = post(webhook, json={"content": page_message(patch_dir)}, timeout=15)
        r.raise_for_status()
        sent.append(name)
    return sent
