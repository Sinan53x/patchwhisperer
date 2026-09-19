import asyncio
import logging
from dataclasses import dataclass
from pathlib import Path

from patchwhisperer.analysis.llm import LLMClient
from patchwhisperer.analysis.pipeline import apply_kb_update, patch_id_of, run_analysis
from patchwhisperer.analysis.render import render_discord
from patchwhisperer.bot import state
from patchwhisperer.kb.git import git_commit_kb, kb_commit_message
from patchwhisperer.kb.store import KBStore
from patchwhisperer.parse.entities import EntityIndex
from patchwhisperer.parse.patch_parser import parse_patch
from patchwhisperer.sources.deadlock_api import DeadlockAPI
from patchwhisperer.sources.steam_news import fetch_patch_posts, fetch_post

log = logging.getLogger(__name__)

KB_ROOT = Path("kb")
REPO_ROOT = Path(".")
MAX_ATTEMPTS = 3


@dataclass
class PostResult:
    patch_id: str
    kind: str  # analyzed | hotfix
    message_id: str | None = None
    thread_id: str | None = None


def _snapshot_for(date_ts: float, api: DeadlockAPI) -> dict:
    stats = api.hero_stats(min_unix=int(date_ts) - 14 * 86400, max_unix=int(date_ts))
    name_by_id = {h["id"]: h["name"] for h in api.heroes()}
    total = sum(s["matches"] for s in stats) or 1
    return {
        name_by_id.get(s["hero_id"], str(s["hero_id"])): {
            "hero_id": s["hero_id"],
            "matches": s["matches"],
            "win_rate": s["wins"] / s["matches"] if s["matches"] else 0.0,
            "pick_rate": s["matches"] / (total / 12),
        }
        for s in stats
    }


def _await(coro, loop):
    """Bridge discord.py coroutines from a worker thread."""
    if asyncio.iscoroutine(coro):
        if loop is None:
            raise RuntimeError("discord channel call needs a running loop")
        return asyncio.run_coroutine_threadsafe(coro, loop).result()
    return coro


def _post_to_channel(bundle, channel, patch_title: str, hotfix: bool, loop=None):
    rendered = render_discord(bundle)
    message = _await(channel.send(rendered.tldr), loop)
    _await(message.add_reaction("👍"), loop)
    _await(message.add_reaction("👎"), loop)
    thread_id = None
    if not hotfix:
        thread = _await(message.create_thread(name=patch_title), loop)
        for chunk in rendered.thread:
            _await(thread.send(chunk), loop)
        thread_id = getattr(thread, "id", None)
    return getattr(message, "id", None), thread_id


def analyze_and_post(
    gid: str,
    *,
    force: bool = False,
    pool: list[str] | None = None,
    channel=None,
    loop=None,
    llm=None,
    kb: KBStore | None = None,
    index: EntityIndex | None = None,
    api: DeadlockAPI | None = None,
    db=None,
    repo_root: Path = REPO_ROOT,
    commit_fn=git_commit_kb,
) -> PostResult | None:
    """Fetch, analyze, and post a patch to Discord. Returns None if skipped."""
    post = fetch_post(gid) if gid != "latest" else fetch_patch_posts(count=1)[0]
    if post is None:
        raise RuntimeError(f"post {gid} not found")

    existing = state.seen_get(post.gid, db)
    if existing and existing["kind"] in ("analyzed", "hotfix") and not force:
        return None

    llm = llm or LLMClient()
    index = index or EntityIndex.load()
    patch = parse_patch(post, index)
    patch_id = patch_id_of(patch)
    hotfix = patch.is_hotfix()

    try:
        api = api or DeadlockAPI()
        snapshot = _snapshot_for(post.date.timestamp(), api)
        if pool is None:
            pool = state.pool_all(db)
        kb = kb or KBStore(KB_ROOT)

        bundle = run_analysis(patch, kb, snapshot, pool, llm, update_kb=not hotfix)

        if bundle.kb_update and not hotfix:
            changed = apply_kb_update(kb, bundle.kb_update)
            if changed:
                commit_fn(
                    repo_root,
                    changed,
                    kb_commit_message(patch.title, bundle.kb_update.change_log),
                )

        if channel is not None:
            message_id, thread_id = _post_to_channel(
                bundle, channel, patch.title, hotfix, loop
            )
        else:
            message_id = thread_id = None

        state.post_record(
            patch_id,
            getattr(channel, "id", ""),
            message_id or "",
            thread_id,
            db,
        )
        state.seen_mark(
            post.gid,
            post.title,
            f"{post.date:%Y-%m-%d}",
            "hotfix" if hotfix else "analyzed",
            db,
        )
        return PostResult(
            patch_id=patch_id,
            kind="hotfix" if hotfix else "analyzed",
            message_id=str(message_id) if message_id else None,
            thread_id=str(thread_id) if thread_id else None,
        )
    except Exception as e:
        attempts = state.seen_bump_attempt(
            post.gid, post.title, f"{post.date:%Y-%m-%d}", db
        )
        log.exception("analyze_and_post failed for %s (attempt %d)", gid, attempts)
        if attempts >= MAX_ATTEMPTS:
            state.seen_mark(
                post.gid, post.title, f"{post.date:%Y-%m-%d}", "skipped", db
            )
            if channel is not None:
                _await(
                    channel.send(
                        f"Patch {post.title}: giving up after {attempts} failed attempts."
                    ),
                    loop,
                )
        elif channel is not None:
            _await(
                channel.send(
                    f"Patch {post.title}: analysis failed ({str(e)[:200]}). Will retry."
                ),
                loop,
            )
        raise
