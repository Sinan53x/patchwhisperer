import asyncio
import inspect
import logging
import os

import httpx

from patchwhisperer.bot import state
from patchwhisperer.sources.steam_news import fetch_patch_posts

log = logging.getLogger(__name__)

POLL_INTERVAL_S = int(os.getenv("POLL_INTERVAL_S", "300"))
HEALTHCHECK_URL = os.getenv("HEALTHCHECK_URL", "")


async def poll_once(job, db=None, *, first_run_mark_only: bool = False) -> None:
    """One poll iteration; job(gid) is called for each unseen post."""
    posts = await asyncio.to_thread(fetch_patch_posts, 10)
    if state.seen_count(db) == 0 or first_run_mark_only:
        # first-run guard: don't analyze the backlog, only mark it seen
        for p in posts:
            state.seen_mark(p.gid, p.title, f"{p.date:%Y-%m-%d}", "skipped", db)
        log.info("first poll: marked %d existing posts as skipped", len(posts))
        return
    for p in reversed(posts):  # oldest first
        seen = state.seen_get(p.gid, db)
        if seen is None or seen["kind"] == "pending":
            if inspect.iscoroutinefunction(job):
                await job(p.gid)
            else:
                await asyncio.to_thread(job, p.gid)


async def healthcheck() -> None:
    if not HEALTHCHECK_URL:
        return
    try:
        async with httpx.AsyncClient(timeout=10) as c:
            await c.get(HEALTHCHECK_URL)
    except httpx.HTTPError as e:
        log.warning("healthcheck ping failed: %s", e)


async def poll_loop(job, db=None, shutdown: asyncio.Event | None = None) -> None:
    while shutdown is None or not shutdown.is_set():
        try:
            await poll_once(job, db)
            await healthcheck()
        except Exception:
            log.exception("poll iteration failed")
        try:
            if shutdown is not None:
                await asyncio.wait_for(shutdown.wait(), POLL_INTERVAL_S)
                break
            else:
                await asyncio.sleep(POLL_INTERVAL_S)
        except TimeoutError:
            pass
