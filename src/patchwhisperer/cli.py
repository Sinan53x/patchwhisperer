import asyncio
import json
import os
from collections import Counter
from datetime import UTC, date, datetime, timedelta
from pathlib import Path
from typing import Annotated

import typer
from pydantic import ValidationError

from patchwhisperer import config
from patchwhisperer.analysis import context as actx
from patchwhisperer.analysis.digest import prepare_patch
from patchwhisperer.analysis.llm import (
    SYSTEM_PROMPT,
    LLMClient,
    ReplayLLMClient,
    render_prompt,
    stage_marker,
)
from patchwhisperer.analysis.pipeline import (
    apply_kb_update,
    run_analysis,
    run_kb_update,
)
from patchwhisperer.analysis.render import render_discord, render_markdown
from patchwhisperer.analysis.schemas import DistilledSource, SeedKB
from patchwhisperer.kb.schema import HeroState, ItemState
from patchwhisperer.kb.store import KBStore, slugify
from patchwhisperer.parse.entities import EntityIndex
from patchwhisperer.parse.patch_parser import parse_patch
from patchwhisperer.sources.deadlock_api import DeadlockAPI
from patchwhisperer.sources.steam_news import (
    PostKind,
    fetch_patch_posts,
    fetch_post,
)
from patchwhisperer.sources.youtube import fetch_transcript

app = typer.Typer(help="PatchWhisperer: Deadlock patch-note analysis.")
kb_app = typer.Typer()
app.add_typer(kb_app, name="kb")

KB_ROOT = Path("kb")


@app.command()
def fetch(count: int = 20) -> None:
    """List recent patch posts."""
    for p in fetch_patch_posts(count=count):
        typer.echo(
            f"{p.gid}  {p.date:%Y-%m-%d}  {p.kind.value:<12}  "
            f"{p.title}  ({len(p.contents)} chars)"
        )


@app.command()
def parse(gid: str, as_json: bool = typer.Option(False, "--json")) -> None:
    """Parse a patch post by gid (or 'latest')."""
    post = fetch_post(gid) if gid != "latest" else fetch_patch_posts(count=1)[0]
    if post is None:
        typer.echo(f"post {gid} not found", err=True)
        raise typer.Exit(1)
    index = EntityIndex.load()
    patch = parse_patch(post, index)
    if as_json:
        typer.echo(patch.model_dump_json(indent=1))
        return
    for c in patch.changes:
        delta = f"{c.old} -> {c.new}" if c.old else ""
        flag = "" if c.resolved else "  [unresolved]"
        typer.echo(
            f"{c.section:<8} {c.entity_name:<20} {c.direction.value:<8} "
            f"{delta:<18} {c.raw[:60]}{flag}"
        )
    counts = Counter(c.section for c in patch.changes)
    unresolved = [c.raw for c in patch.changes if not c.resolved]
    typer.echo("---")
    typer.echo(
        f"total={len(patch.changes)} sections={dict(counts)} "
        f"unresolved={len(unresolved)} hotfix={patch.is_hotfix()} "
        f"kind={patch.kind.value}"
    )
    for u in unresolved:
        typer.echo(f"  unresolved: {u}")


@kb_app.command("init")
def kb_init() -> None:
    """Initialise the knowledge base from live assets."""
    store = KBStore(KB_ROOT)
    heroes = DeadlockAPI().heroes()
    store.save_heroes({h["name"]: HeroState(name=h["name"]) for h in heroes})
    if not store.items_path.exists():
        store.items_path.write_text("{}\n")
    if not store.meta_path.exists():
        store.meta_path.write_text("# PatchWhisperer meta\n\n(placeholder)\n")
    typer.echo(f"initialised {len(heroes)} heroes in {store.heroes_path}")


@app.command()
def ingest(url: str) -> None:
    """Fetch a YouTube transcript into kb/sources/raw/."""
    t = fetch_transcript(url)
    out = KB_ROOT / "sources" / "raw" / f"{t.author.lower()}-{t.video_id}.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(t.text)
    out.with_suffix(".meta.json").write_text(
        json.dumps(
            {
                "video_id": t.video_id,
                "title": t.title,
                "author": t.author,
                "upload_date": t.upload_date,
            },
            indent=1,
        )
    )
    typer.echo(f"{t.title} ({t.author}) -> {out} ({len(t.text)} chars)")


def _usage_line(usage: dict) -> str:
    cost = (
        usage.get("prompt_tokens", 0) / 1e6 * config.PRICE_INPUT_PER_M
        + usage.get("completion_tokens", 0) / 1e6 * config.PRICE_OUTPUT_PER_M
    )
    return (
        f"tokens: {usage.get('prompt_tokens', 0)} in / "
        f"{usage.get('completion_tokens', 0)} out (~${cost:.3f})"
    )


@app.command()
def analyze(
    gid: str,
    pool: str = typer.Option("", "--pool"),
    dry_run: bool = typer.Option(False, "--dry-run"),
    no_kb_update: bool = typer.Option(False, "--no-kb-update"),
    model: str = typer.Option("", "--model"),
    notes: Annotated[Path | None, typer.Option("--notes")] = None,
    sources: bool = typer.Option(False, "--sources/--no-sources"),
    out: Annotated[Path | None, typer.Option("--out")] = None,
) -> None:
    """Run the full analysis pipeline on a patch post."""
    post = fetch_post(gid) if gid != "latest" else fetch_patch_posts(count=1)[0]
    if post is None:
        typer.echo(f"post {gid} not found", err=True)
        raise typer.Exit(1)
    if post.kind == PostKind.hero_release:
        typer.echo(
            "hero release post; nothing to analyse "
            "(roster sync handles new heroes)"
        )
        raise typer.Exit(0)
    index = EntityIndex.load()
    kb = KBStore(KB_ROOT)
    llm = LLMClient(model=model or config.LLM_MODEL)
    patch = prepare_patch(
        post, index, kb, llm, notes=notes.read_text() if notes else None
    )
    api = DeadlockAPI()
    min_unix = int(post.date.timestamp()) - 14 * 86400
    stats = api.hero_stats(min_unix=min_unix, max_unix=int(post.date.timestamp()))
    name_by_id = {h["id"]: h["name"] for h in api.heroes()}
    total = sum(s["matches"] for s in stats) or 1
    snap = {
        name_by_id.get(s["hero_id"], str(s["hero_id"])): {
            "hero_id": s["hero_id"],
            "matches": s["matches"],
            "win_rate": s["wins"] / s["matches"] if s["matches"] else 0.0,
            "pick_rate": s["matches"] / (total / 12),
        }
        for s in stats
    }
    pool_list = [
        p.strip() for p in (pool or config.DEFAULT_POOL).split(",") if p.strip()
    ]
    bundle = run_analysis(
        patch,
        kb,
        snap,
        pool_list,
        llm,
        update_kb=not no_kb_update,
        creator_sources=actx.creator_sources_since(
            KB_ROOT / "sources", post.date.date()
        )
        if sources
        else "",
    )
    md = render_markdown(bundle)
    typer.echo(md)
    if out:
        out.write_text(md)
    typer.echo("---")
    for n, secs in sorted(bundle.usage.get("stage_seconds", {}).items()):
        typer.echo(f"stage {n}: {secs:.1f}s")
    typer.echo(_usage_line(bundle.usage))
    if bundle.kb_update and not dry_run:
        changed = apply_kb_update(kb, bundle.kb_update)
        typer.echo(f"kb updated: {[str(p) for p in changed]}")
    elif bundle.kb_update:
        typer.echo("(dry-run: kb update not applied)")


def _demo_dir() -> Path:
    for base in (Path("demo/2026-09-16"), Path(__file__).resolve().parents[2] / "demo" / "2026-09-16"):
        if (base / "post.json").exists():
            return base
    typer.echo("demo/2026-09-16 not found", err=True)
    raise typer.Exit(1)


@app.command()
def demo(
    full: bool = typer.Option(False, "--full", help="Print all thread chunks."),
    keep: bool = typer.Option(
        False, "--keep", help="Keep the temporary KB dir and print its path."
    ),
) -> None:
    """Replay the real 2026-09-16 pipeline run offline (no API key/network)."""
    import shutil
    import tempfile

    from patchwhisperer.analysis import context as ctx
    from patchwhisperer.sources.steam_news import SteamPost

    src = _demo_dir()
    tmp = Path(tempfile.mkdtemp(prefix="pw-demo-"))
    kb_dir = tmp / "kb"
    shutil.copytree(src / "kb", kb_dir)
    kb = KBStore(kb_dir)

    it = json.loads((src / "post.json").read_text())
    post = SteamPost(
        gid=str(it["gid"]),
        title=it["title"],
        date=datetime.fromtimestamp(it["date"], tz=UTC),
        url=it["url"],
        author=it["author"],
        contents=it["contents"],
    )
    assets = src / "assets"
    index = EntityIndex(
        json.loads((assets / "heroes.json").read_text()),
        json.loads((assets / "items.json").read_text()),
        {
            int(k): v
            for k, v in json.loads((assets / "abilities.json").read_text()).items()
        },
    )
    patch = parse_patch(post, index)
    pool = [p.strip() for p in (src / "pool.txt").read_text().splitlines() if p.strip()]

    canned: dict[str, list[str]] = {}
    for stem, prompt_name in {
        "stage1": "stage1_systems",
        "stage2": "stage2_items",
        "stage3": "stage3_heroes",
        "stage4": "stage4_synthesis",
        "stage5": "stage5_pool",
        "stage6": "stage6_kb_update",
    }.items():
        canned[stage_marker(prompt_name)] = [(src / f"{stem}.json").read_text()]
    canned[stage_marker("stage6_kb_heroes")] = [
        (src / f"stage6h{i}.json").read_text() for i in range(1, 5)
    ]
    llm = ReplayLLMClient(canned)

    typer.echo(f"# {patch.title}")
    typer.echo(ctx.change_counts(patch))
    typer.echo("")

    bundle = run_analysis(patch, kb, {}, pool, llm, update_kb=False)
    for n, secs in sorted(bundle.usage["stage_seconds"].items(), key=str):
        typer.echo(f"stage {n} done ({secs:.1f}s)")

    heroes = bundle.heroes
    movers = [h for h in heroes.heroes if h.direction != "neutral"]
    ups = [h.hero for h in movers if h.direction == "up"]
    downs = [h.hero for h in movers if h.direction == "down"]
    typer.echo("")
    typer.echo(f"stage 3 movers: {len(movers)}/{len(heroes.heroes)} heroes")
    typer.echo(f"  up: {', '.join(ups)}")
    typer.echo(f"  down: {', '.join(downs)}")

    rendered = render_discord(bundle)
    typer.echo("")
    typer.echo("## Discord TL;DR")
    typer.echo("")
    typer.echo(rendered.tldr)
    for extra in rendered.tldr_extra:
        typer.echo("")
        typer.echo(extra)
    typer.echo("")
    typer.echo("## Discord thread")
    typer.echo("")
    chunks = rendered.thread if full else rendered.thread[:2]
    for c in chunks:
        typer.echo(c)
        typer.echo("")
    if not full and len(rendered.thread) > 2:
        typer.echo(f"({len(rendered.thread) - 2} more chunks — rerun with --full)")

    before = kb.load_heroes()
    kb_update = run_kb_update(patch, kb, bundle, llm)
    leftover = [m for m, q in llm.canned.items() if q]
    if leftover:
        typer.echo(f"error: unused replay payloads for {leftover}", err=True)
        raise typer.Exit(1)
    apply_kb_update(kb, kb_update)
    after = kb.load_heroes()

    typer.echo("## KB changes")
    typer.echo("")
    other = 0
    for name, fields in kb_update.hero_updates.items():
        interesting = {"tier", "trend"} & set(fields)
        for f in interesting:
            typer.echo(
                f"  {name}: {f} {getattr(before[name], f)} -> {getattr(after[name], f)}"
            )
        other += len(set(fields) - {"tier", "trend"})
    typer.echo(f"  (+{other} other field updates across {len(kb_update.hero_updates)} heroes)")
    typer.echo("")
    for line in kb_update.change_log:
        typer.echo(f"  - {line}")

    typer.echo("")
    typer.echo("Replayed from the real 2026-09-24 run; no API calls made.")
    if keep:
        typer.echo(f"temp KB kept at: {kb_dir}")
    else:
        shutil.rmtree(tmp, ignore_errors=True)


_slug = slugify


def _source_md(meta: dict, published: str, vid: str, result: DistilledSource) -> str:
    lines = [
        f"# {meta.get('title', vid)} — {meta.get('author', '?')} ({published})",
        "",
        "## Meta thesis",
        result.meta_thesis,
        "",
        "## Hero claims",
    ]
    for h in result.hero_claims:
        lines.append(f"- **{h.hero}** tier={h.tier} dir={h.direction}: {h.why}")
    lines.append("\n## Map claims")
    lines += [
        f"- **{c.topic}**: {c.claim}"
        + (f" ({c.numbers})" if c.numbers else "")
        for c in result.map_claims
    ]
    lines.append("\n## Reasoning patterns")
    lines += [f"- {r}" for r in result.reasoning_patterns]
    return "\n".join(lines)


@app.command()
def distill(raw: str) -> None:
    """Distill a raw transcript (path or file stem under kb/sources/raw)."""
    path = Path(raw)
    if not path.exists():
        path = KB_ROOT / "sources" / "raw" / f"{raw}.txt"
    if not path.exists():
        typer.echo(f"no such transcript: {raw}", err=True)
        raise typer.Exit(1)
    meta_path = path.with_suffix(".meta.json")
    meta = json.loads(meta_path.read_text()) if meta_path.exists() else {}
    transcript = path.read_text()
    index = EntityIndex.load()
    published = meta.get("upload_date") or "unknown"
    patch_context = "unknown"
    if meta.get("upload_date"):
        try:
            ud = datetime.strptime(meta["upload_date"], "%Y%m%d").replace(tzinfo=UTC)
            for p in fetch_patch_posts(count=50):
                if p.date <= ud:
                    patch_context = f"{p.title} ({p.date:%Y-%m-%d})"
                    break
        except ValueError:
            pass
    visual_path = path.with_suffix(".visual.md")
    visual_notes = visual_path.read_text() if visual_path.exists() else "(none)"
    prompt = render_prompt(
        "distill_source",
        author=meta.get("author", path.stem.split("-")[0]),
        title=meta.get("title", path.stem),
        video_id=meta.get("video_id", path.stem),
        published=published,
        patch_context=patch_context,
        transcript=transcript,
        visual_notes=visual_notes,
        hero_names=", ".join(h["name"] for h in index.heroes),
    )
    llm = LLMClient()
    result: DistilledSource = llm.complete_json(SYSTEM_PROMPT, prompt, DistilledSource)
    slug = _slug(meta.get("author", "source"))
    vid = meta.get("video_id", path.stem)
    base = KB_ROOT / "sources" / f"{slug}-{published}-{vid}"
    base.with_suffix(".json").write_text(result.model_dump_json(indent=1))
    base.with_suffix(".md").write_text(_source_md(meta, published, vid, result))
    typer.echo(f"-> {base.with_suffix('.json')} ({_usage_line(llm.usage)})")


@app.command()
def seed(patches: int = typer.Option(6, "--patches")) -> None:
    """Build the initial KB from distilled sources + recent patches + stats."""
    kb = KBStore(KB_ROOT)
    index = EntityIndex.load()
    src_files = sorted((KB_ROOT / "sources").glob("*.json"), reverse=True)
    sources = []
    for f in src_files:
        parts = f.stem.rsplit("-", 2)
        header = (
            f"### source: {parts[0]} (published {parts[1] if len(parts) > 2 else '?'})"
        )
        sources.append(header + "\n" + f.read_text())
    posts = fetch_patch_posts(count=patches)
    patches_json = []
    for p in posts:
        patch = parse_patch(p, index)
        patches_json.append(
            {
                "title": p.title,
                "date": f"{p.date:%Y-%m-%d}",
                "changes_by_entity": {
                    k: [c.raw for c in v] for k, v in patch.by_entity().items()
                },
            }
        )
    snap = DeadlockAPI().snapshot()
    latest = posts[0] if posts else None
    prompt = render_prompt(
        "seed_kb",
        as_of_date=f"{datetime.now(tz=UTC):%Y-%m-%d}",
        latest_patch_title=latest.title if latest else "unknown",
        latest_patch_date=f"{latest.date:%Y-%m-%d}" if latest else "unknown",
        sources_json="\n\n".join(sources) or "(none)",
        patches_json=json.dumps(patches_json, indent=1),
        snapshot=actx.snapshot_table(snap),
        hero_names=", ".join(h["name"] for h in index.heroes),
        item_names=", ".join(sorted(i["name"] for i in index.items)),
    )
    llm = LLMClient()
    result: SeedKB = llm.complete_json(SYSTEM_PROMPT, prompt, SeedKB, max_tokens=40000)

    existing = kb.load_heroes()
    heroes: dict[str, HeroState] = {}
    missing = []
    for name in existing:
        fields = result.heroes.get(name)
        if fields is None:
            missing.append(name)
            heroes[name] = existing[name]
            continue
        fields["name"] = name
        try:
            heroes[name] = HeroState(**fields)
        except (ValidationError, TypeError) as e:
            typer.echo(f"warn: {name}: {e}; keeping placeholder")
            heroes[name] = existing[name]
    if missing:
        typer.echo(f"warn: LLM omitted heroes, kept placeholders: {missing}")
    kb.save_heroes(heroes)
    if result.meta_md:
        kb.save_meta(result.meta_md)
    items = {}
    for name, fields in result.items.items():
        fields["name"] = name
        try:
            items[name] = ItemState(**fields)
        except (ValidationError, TypeError) as e:
            typer.echo(f"warn: item {name}: {e}")
    kb.save_items(items)
    tiers = Counter(h.tier for h in heroes.values())
    typer.echo(f"seeded {len(heroes)} heroes, {len(items)} items")
    if not heroes or not items:
        typer.echo("error: seed produced empty KB sections", err=True)
        raise typer.Exit(1)
    typer.echo(f"tiers: {dict(tiers)}")
    typer.echo(_usage_line(llm.usage))


@app.command()
def snapshot() -> None:
    """Print top 10 heroes by win rate (last 14 days)."""
    snap = DeadlockAPI().snapshot()
    top = sorted(snap.items(), key=lambda kv: kv[1]["win_rate"], reverse=True)[:10]
    for name, s in top:
        typer.echo(
            f"{name:<20} WR {s['win_rate'] * 100:5.2f}%  "
            f"PR {s['pick_rate'] * 100:5.2f}%  matches {s['matches']}"
        )


@app.command()
def enrich(
    hero: str = typer.Option("", "--hero"),
    days: int = typer.Option(30, "--days"),
    all_heroes: bool = typer.Option(False, "--all"),
) -> None:
    """Enrich KB hero entries with item-usage and matchup data."""
    from patchwhisperer.analysis.context import creator_claims, tier_list
    from patchwhisperer.analysis.enrich import enrich_hero, merge_enrichment

    kb = KBStore(KB_ROOT)
    index = EntityIndex.load()
    api = DeadlockAPI()
    llm = LLMClient()
    heroes = kb.load_heroes()
    meta_md = kb.load_meta() if kb.meta_path.exists() else ""
    corrections = kb.load_corrections()
    tiers = tier_list(kb)
    snap = api.snapshot(days=14)
    claims = creator_claims(KB_ROOT / "sources")
    counters = api.hero_counters(days=days)
    latest = fetch_patch_posts(count=1)
    latest_title = latest[0].title if latest else "unknown"

    targets = (
        list(heroes)
        if all_heroes
        else ([index.resolve(hero)[2]] if hero and index.resolve(hero) else [])
    )
    if not targets:
        typer.echo("specify --hero NAME or --all", err=True)
        raise typer.Exit(1)

    for name in targets:
        h = heroes[name]
        before = h.tier
        result = enrich_hero(
            name,
            kb=kb,
            index=index,
            api=api,
            llm=llm,
            claims=claims,
            counters=counters,
            snap=snap,
            meta_md=meta_md,
            corrections=corrections,
            tiers=tiers,
            latest_title=latest_title,
            days=days,
        )
        merge_enrichment(h, result)
        heroes[name] = h
        kb.save_heroes(heroes)
        loses_short = ", ".join(h.matchups.loses_to[:3])
        typer.echo(
            f"{name}: {before} -> {h.tier} ({h.trend}) | builds: "
            f"{', '.join(f'{b.name}/{b.popularity}' for b in h.builds)} | "
            f"loses to: {loses_short}"
        )

    # deterministic rebuild of items.bought_by from hero builds
    for h in heroes.values():
        for b in h.builds:
            kb.add_bought_by(h.name, b.core_items)
    typer.echo(_usage_line(llm.usage))


@app.command()
def bot() -> None:
    """Start the Discord bot and the patch poller."""
    from patchwhisperer.bot.discord_bot import run

    run()


def _with_channel(fn):
    """Run async fn(channel, loop) inside a minimal Discord client."""
    import discord

    from patchwhisperer.bot import state

    state.init_db()
    channel_id = int(os.environ.get("DISCORD_CHANNEL_ID", "0"))
    if not channel_id:
        typer.echo("DISCORD_CHANNEL_ID not set", err=True)
        raise typer.Exit(1)

    intents = discord.Intents.default()
    client = discord.Client(intents=intents)
    result = {}

    @client.event
    async def on_ready():
        channel = client.get_channel(channel_id) or await client.fetch_channel(
            channel_id
        )
        loop = asyncio.get_running_loop()
        try:
            result["r"] = await fn(channel, loop)
        finally:
            await client.close()

    token = os.environ.get("DISCORD_TOKEN")
    if not token:
        typer.echo("DISCORD_TOKEN not set", err=True)
        raise typer.Exit(1)
    client.run(token)
    return result.get("r")


@app.command(name="run-job")
def run_job(
    gid: str,
    force: bool = typer.Option(False, "--force"),
    sources: bool = typer.Option(False, "--sources/--no-sources"),
) -> None:
    """Run analyze_and_post once without the gateway (posts to Discord)."""
    from patchwhisperer.bot import jobs

    fn = (
        (lambda post: actx.creator_sources_since(KB_ROOT / "sources", post.date.date()))
        if sources
        else None
    )
    r = _with_channel(
        lambda channel, loop: asyncio.to_thread(
            jobs.analyze_and_post,
            gid,
            force=force,
            channel=channel,
            loop=loop,
            creator_sources_fn=fn,
        )
    )
    typer.echo(r)


roster_app = typer.Typer()
app.add_typer(roster_app, name="roster")


def _tmp_kb() -> KBStore:
    import shutil
    import tempfile

    root = Path(tempfile.mkdtemp(prefix="pw-kb-"))
    for f in ("heroes.yaml", "items.yaml", "meta.md", "corrections.md"):
        src = KB_ROOT / f
        if src.exists():
            shutil.copy(src, root / f)
    return KBStore(root)


@roster_app.command("sync")
def roster_sync(
    dry_run: bool = typer.Option(False, "--dry-run"),
) -> None:
    """Evaluate new heroes and run due 7-day check-ins (no Discord)."""
    from patchwhisperer.analysis.render import render_hero_card
    from patchwhisperer.analysis.roster import (
        checkin_hero,
        checkins_due,
        evaluate_new_hero,
        new_heroes,
        sync_roster,
    )

    kb = _tmp_kb() if dry_run else KBStore(KB_ROOT)
    index = EntityIndex.load()
    api = DeadlockAPI()
    llm = LLMClient()
    today = datetime.now(tz=UTC).date()
    if not dry_run:
        result = sync_roster(
            kb=kb,
            index=index,
            api=api,
            llm=llm,
            sources_dir=KB_ROOT / "sources",
            repo_root=Path("."),
        )
        heroes_after = kb.load_heroes()
        parts = []
        for n in result.added:
            h = heroes_after.get(n)
            if h is not None and h.released_on:
                due = date.fromisoformat(h.released_on) + timedelta(days=7)
                parts.append(f"{n} (released {h.released_on}, check-in due {due})")
            else:
                parts.append(n)
        typer.echo(
            f"added: {', '.join(parts) or '(none)'}, "
            f"check-ins: {result.checked_in or '(none)'}"
        )
        return
    heroes = kb.load_heroes()
    for hero in sorted(new_heroes(api.heroes(), heroes), key=lambda h: h["id"]):
        state, card = evaluate_new_hero(
            hero["name"],
            hero,
            kb=kb,
            index=index,
            api=api,
            llm=llm,
            release_post=None,
            sources_dir=KB_ROOT / "sources",
            today=today,
        )
        import yaml

        typer.echo(render_hero_card(hero["name"], card, state))
        due = date.fromisoformat(state.released_on) + timedelta(days=7)
        typer.echo(
            f"released_on: {state.released_on} (check-in due {due})"
        )
        typer.echo("---")
        typer.echo(yaml.safe_dump(state.model_dump(), sort_keys=False))
    for name in checkins_due(heroes, today):
        _, _, card = checkin_hero(
            name, kb=kb, index=index, api=api, llm=llm, today=today
        )
        typer.echo(card)


@roster_app.command("checkin")
def roster_checkin(
    hero: str,
    dry_run: bool = typer.Option(False, "--dry-run"),
) -> None:
    """Run the 7-day data check-in for one hero."""
    from patchwhisperer.analysis.roster import checkin_hero
    from patchwhisperer.kb.git import git_commit_kb

    kb = _tmp_kb() if dry_run else KBStore(KB_ROOT)
    index = EntityIndex.load()
    hit = index.resolve(hero)
    if not hit:
        typer.echo(f"unknown hero: {hero}", err=True)
        raise typer.Exit(1)
    name = hit[2]
    api = DeadlockAPI()
    llm = LLMClient()
    _, _, card = checkin_hero(
        name,
        kb=kb,
        index=index,
        api=api,
        llm=llm,
        today=datetime.now(tz=UTC).date(),
    )
    typer.echo(card)
    if dry_run:
        typer.echo("(dry-run: nothing saved or committed)")
        return
    git_commit_kb(
        Path("."), [kb.heroes_path, kb.items_path], f"kb: {name} 7-day check-in"
    )


@roster_app.command("post-sync")
def roster_post_sync() -> None:
    """Run roster sync and post cards to Discord."""
    from patchwhisperer.bot import jobs

    r = _with_channel(
        lambda channel, loop: asyncio.to_thread(
            jobs.run_roster_sync, channel=channel, loop=loop
        )
    )
    typer.echo(r)


def main() -> None:
    import logging

    logging.basicConfig(level=logging.INFO)
    app()
