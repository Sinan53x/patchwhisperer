#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = ["playwright"]
# ///
"""Retake the README screenshots in docs/images/ against the live site.

Usage:
    uv run --with playwright python scripts/readme_screenshots.py [BASE_URL] [--out DIR]
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import sync_playwright

DEFAULT_BASE = "https://patch-whisperer.plaid-earth.workers.dev"
DEFAULT_OUT = Path(__file__).resolve().parents[1] / "docs" / "images"

HIDE_TOPBAR = "document.querySelector('.topbar').style.display = 'none'"

# (output filename, site path, element selector or None for a viewport shot)
SHOTS = [
    ("site-top.png", "", None),
    ("site-tiers.png", "", "#heroes"),
    ("site-plan.png", "patches/2026-10-30-1847920302240420/", "#plan .pace"),
    ("site-season-ladder.png", "patches/2026-11-05-1848664643342973/", "#ladder"),
]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "base",
        nargs="?",
        default=DEFAULT_BASE,
        help=f"site base URL (default: {DEFAULT_BASE})",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=DEFAULT_OUT,
        help=f"output directory (default: {DEFAULT_OUT})",
    )
    args = parser.parse_args()

    base = args.base.rstrip("/")
    args.out.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            viewport={"width": 1200, "height": 800}, device_scale_factor=2
        )
        page = context.new_page()
        for name, path, selector in SHOTS:
            url = f"{base}/{path}"
            page.goto(url, wait_until="networkidle")
            target = args.out / name
            if selector is None:
                page.screenshot(path=str(target))
            else:
                locator = page.locator(selector)
                try:
                    locator.wait_for(timeout=15_000)
                except PlaywrightTimeoutError:
                    sys.exit(f"error: selector {selector!r} not found on {url}")
                page.evaluate(HIDE_TOPBAR)
                locator.screenshot(path=str(target))
            print(f"wrote {target}")
        browser.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
