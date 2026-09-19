import asyncio
import json
import os
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path
from typing import Annotated

import typer
from pydantic import ValidationError

from patchwhisperer import config
from patchwhisperer.analysis import context as actx
from patchwhisperer.analysis.llm import SYSTEM_PROMPT, LLMClient, render_prompt
from patchwhisperer.analysis.pipeline import apply_kb_update, run_analysis
from patchwhisperer.analysis.render import render_markdown
from patchwhisperer.analysis.schemas import DistilledSource, SeedKB
from patchwhisperer.kb.schema import HeroState, ItemState
from patchwhisperer.kb.store import KBStore
from patchwhisperer.parse.entities import EntityIndex
from patchwhisperer.parse.patch_parser import parse_patch
from patchwhisperer.sources.deadlock_api import DeadlockAPI
from patchwhisperer.sources.steam_news import fetch_patch_posts, fetch_post
from patchwhisperer.sources.youtube import fetch_transcript

app = typer.Typer(help="PatchWhisperer: Deadlock patch-note analysis.")
kb_app = typer.Typer()
app.add_typer(kb_app, name="kb")

KB_ROOT = Path("kb")


@app.command()
def fetch(count: int = 20) -> None:
    """List recent patch posts."""
    for p in fetch_patch_posts(count=count):
        typer.echo(f"{p.gid}  {p.date:%Y-%m-%d}  {p.title}  ({len(p.contents)} chars)")


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
        f"unresolved={len(unresolved)} hotfix={patch.is_hotfix()}"
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
    out: Annotated[Path | None, typer.Option("--out")] = None,
) -> None:
    """Run the full analysis pipeline on a patch post."""
    post = fetch_post(gid) if gid != "latest" else fetch_patch_posts(count=1)[0]
    if post is None:
        typer.echo(f"post {gid} not found", err=True)
        raise typer.Exit(1)
    patch = parse_patch(post, EntityIndex.load())
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
    kb = KBStore(KB_ROOT)
    llm = LLMClient(model=model or config.LLM_MODEL)
    bundle = run_analysis(patch, kb, snap, pool_list, llm, update_kb=not no_kb_update)
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


def _slug(text: str) -> str:
    return "".join(c.lower() if c.isalnum() else "-" for c in text).strip("-")


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
    prompt = render_prompt(
        "distill_source",
        author=meta.get("author", path.stem.split("-")[0]),
        title=meta.get("title", path.stem),
        video_id=meta.get("video_id", path.stem),
        published=published,
        patch_context=patch_context,
        transcript=transcript,
        hero_names=", ".join(h["name"] for h in index.heroes),
    )
    llm = LLMClient()
    result: DistilledSource = llm.complete_json(SYSTEM_PROMPT, prompt, DistilledSource)
    slug = _slug(meta.get("author", "source"))
    vid = meta.get("video_id", path.stem)
    base = KB_ROOT / "sources" / f"{slug}-{published}-{vid}"
    base.with_suffix(".json").write_text(result.model_dump_json(indent=1))
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
    lines.append("\n## Reasoning patterns")
    lines += [f"- {r}" for r in result.reasoning_patterns]
    base.with_suffix(".md").write_text("\n".join(lines))
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
def bot() -> None:
    """Start the Discord bot and the patch poller."""
    from patchwhisperer.bot.discord_bot import run

    run()


@app.command(name="run-job")
def run_job(
    gid: str,
    force: bool = typer.Option(False, "--force"),
) -> None:
    """Run analyze_and_post once without the gateway (posts to Discord)."""
    import discord

    from patchwhisperer.bot import jobs, state

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
            result["r"] = await asyncio.to_thread(
                jobs.analyze_and_post,
                gid,
                force=force,
                channel=channel,
                loop=loop,
            )
        finally:
            await client.close()

    token = os.environ.get("DISCORD_TOKEN")
    if not token:
        typer.echo("DISCORD_TOKEN not set", err=True)
        raise typer.Exit(1)
    client.run(token)
    typer.echo(result.get("r"))


def main() -> None:
    import logging

    logging.basicConfig(level=logging.INFO)
    app()
