import logging
from dataclasses import dataclass
from pathlib import Path

from patchwhisperer.analysis.digest import prepare_patch
from patchwhisperer.analysis.llm import LLMClient
from patchwhisperer.analysis.matchups import sync_kb_matchups
from patchwhisperer.analysis.pipeline import (
    apply_kb_update,
    patch_id_of,
    run_analysis,
    run_kb_update,
)
from patchwhisperer.analysis.roster import RosterResult, sync_roster
from patchwhisperer.analysis.season import extract_season
from patchwhisperer.bot import state
from patchwhisperer.kb.git import git_commit_kb, git_sync, kb_commit_message
from patchwhisperer.kb.store import KBStore
from patchwhisperer.parse.entities import EntityIndex
from patchwhisperer.parse.patch_parser import parse_patch
from patchwhisperer.sources.deadlock_api import DeadlockAPI
from patchwhisperer.sources.steam_news import (
    PostKind,
    SteamPost,
    fetch_patch_posts,
    fetch_post,
)

log = logging.getLogger(__name__)

KB_ROOT = Path("kb")
REPO_ROOT = Path(".")
MAX_ATTEMPTS = 3


@dataclass
class PostResult:
    patch_id: str
    kind: str  # analyzed | hotfix | hero_release | ranked_season
    kb_updated: bool = False


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


def analyze_and_post(
    gid: str,
    *,
    force: bool = False,
    pool: list[str] | None = None,
    llm=None,
    kb: KBStore | None = None,
    index: EntityIndex | None = None,
    api: DeadlockAPI | None = None,
    db=None,
    repo_root: Path = REPO_ROOT,
    commit_fn=git_commit_kb,
    sync_fn=git_sync,
    on_hero_release=None,
    creator_sources_fn=None,
) -> PostResult | None:
    """Fetch, analyze, and commit a patch's artifacts to kb. Returns None if skipped.

    The automatic (bot/poller) path never injects creator sources; callers may
    opt in via `creator_sources_fn(post) -> str`."""
    post = fetch_post(gid) if gid != "latest" else fetch_patch_posts(count=1)[0]
    if post is None:
        raise RuntimeError(f"post {gid} not found")

    existing = state.seen_get(post.gid, db)
    if (
        existing
        and existing["kind"]
        in ("analyzed", "hotfix", "hero_release", "ranked_season")
        and not force
    ):
        return None

    llm = llm or LLMClient()

    try:
        sync_fn(repo_root)
        kb = kb or KBStore(KB_ROOT)
        if post.kind == PostKind.ranked_season:
            return _process_season(
                post,
                force=force,
                llm=llm,
                kb=kb,
                db=db,
                repo_root=repo_root,
                commit_fn=commit_fn,
            )
        index = index or EntityIndex.load()
        patch = parse_patch(post, index)
        patch_id = patch_id_of(patch)
        hotfix = patch.is_hotfix()
        creator_sources = creator_sources_fn(post) if creator_sources_fn else ""
        if not force and (kb.patch_dir(patch_id) / "analysis.json").exists():
            # a second machine already processed this post; kb is git-synced
            state.seen_mark(
                post.gid, post.title, f"{post.date:%Y-%m-%d}", "analyzed", db
            )
            return None
        if patch.kind == PostKind.hero_release:
            state.seen_mark(
                post.gid, post.title, f"{post.date:%Y-%m-%d}", "hero_release", db
            )
            if on_hero_release is not None:
                on_hero_release(post)
            return PostResult(patch_id=patch_id, kind="hero_release")
        patch = prepare_patch(post, index, kb, llm)
        patch_id = patch_id_of(patch)
        hotfix = patch.is_hotfix()
        api = api or DeadlockAPI()
        snapshot = _snapshot_for(post.date.timestamp(), api)
        sync_kb_matchups(kb, api)
        if pool is None:
            pool = state.pool_all(db)

        bundle = run_analysis(
            patch,
            kb,
            snapshot,
            pool,
            llm,
            update_kb=False,
            creator_sources=creator_sources,
        )

        state.seen_mark(
            post.gid,
            post.title,
            f"{post.date:%Y-%m-%d}",
            "hotfix" if hotfix else "analyzed",
            db,
        )
        kb_updated = False
        patch_dir = kb.patch_dir(patch_id)
        # publish the analysis artifacts now so a stage-6 failure cannot keep
        # them off the website; the KB update commit below still lands later
        try:
            commit_fn(repo_root, [patch_dir], f"kb: {patch.title} (analysis)")
        except Exception:
            log.exception("early patch commit failed for %s", patch_id)
        if not hotfix:
            try:
                kb_update = run_kb_update(patch, kb, bundle, llm)
                changed = apply_kb_update(kb, kb_update)
                kb_updated = True
                paths = changed + [patch_dir]
                message = kb_commit_message(patch.title, kb_update.change_log)
            except Exception:
                log.exception("kb update failed for %s", patch_id)
                paths = [patch_dir]
                message = f"kb: {patch.title} (analysis artifacts only)"
        else:
            paths = [patch_dir]
            message = f"kb: {patch.title} (analysis artifacts only)"
        try:
            commit_fn(repo_root, paths, message)
        except Exception:
            log.exception("kb commit failed for %s", patch_id)
        return PostResult(
            patch_id=patch_id,
            kind="hotfix" if hotfix else "analyzed",
            kb_updated=kb_updated,
        )
    except Exception:
        attempts = state.seen_bump_attempt(
            post.gid, post.title, f"{post.date:%Y-%m-%d}", db
        )
        log.exception("analyze_and_post failed for %s (attempt %d)", gid, attempts)
        if attempts >= MAX_ATTEMPTS:
            state.seen_mark(
                post.gid, post.title, f"{post.date:%Y-%m-%d}", "skipped", db
            )
        raise


def _process_season(
    post: SteamPost,
    *,
    force: bool,
    llm,
    kb: KBStore,
    db,
    repo_root: Path,
    commit_fn,
) -> PostResult | None:
    """Extract a ranked-season post into kb. No KB update."""
    patch_id = f"{post.date:%Y-%m-%d}-{post.gid}"
    pdir = kb.patch_dir(patch_id)
    if not force and (pdir / "season.json").exists():
        # a second machine already processed this post; kb is git-synced
        state.seen_mark(
            post.gid, post.title, f"{post.date:%Y-%m-%d}", "ranked_season", db
        )
        return None
    extract_season(post, kb, llm)
    state.seen_mark(
        post.gid, post.title, f"{post.date:%Y-%m-%d}", "ranked_season", db
    )
    try:
        commit_fn(repo_root, [pdir], f"kb: {post.title} (ranked season)")
    except Exception:
        log.exception("season commit failed for %s", patch_id)
    return PostResult(patch_id=patch_id, kind="ranked_season")


def season_ingest(
    gid: str,
    *,
    force: bool = False,
    llm=None,
    kb: KBStore | None = None,
    db=None,
    repo_root: Path = REPO_ROOT,
    commit_fn=git_commit_kb,
    sync_fn=git_sync,
) -> PostResult | None:
    """Backfill entry point: extract a ranked-season post by gid."""
    post = fetch_post(gid)
    if post is None:
        raise RuntimeError(f"post {gid} not found")
    if post.kind != PostKind.ranked_season:
        raise RuntimeError(
            f"post {gid} is a {post.kind.value} post, not a ranked season"
        )
    existing = state.seen_get(post.gid, db)
    if existing and existing["kind"] == "ranked_season" and not force:
        return None
    llm = llm or LLMClient()
    sync_fn(repo_root)
    kb = kb or KBStore(KB_ROOT)
    return _process_season(
        post,
        force=force,
        llm=llm,
        kb=kb,
        db=db,
        repo_root=repo_root,
        commit_fn=commit_fn,
    )


def run_roster_sync(
    *,
    llm=None,
    kb: KBStore | None = None,
    index: EntityIndex | None = None,
    api: DeadlockAPI | None = None,
    repo_root: Path = REPO_ROOT,
    commit_fn=git_commit_kb,
    sync_fn=git_sync,
    release_post=None,
) -> RosterResult:
    """Sync new heroes into the KB (day-0 read) and run due 7-day check-ins."""
    llm = llm or LLMClient()
    index = index or EntityIndex.load()
    api = api or DeadlockAPI()
    kb = kb or KBStore(KB_ROOT)

    return sync_roster(
        kb=kb,
        index=index,
        api=api,
        llm=llm,
        sources_dir=KB_ROOT / "sources",
        release_post=release_post,
        commit_fn=commit_fn,
        sync_fn=sync_fn,
        repo_root=repo_root,
    )
