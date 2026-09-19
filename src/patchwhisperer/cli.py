from collections import Counter
from pathlib import Path

import typer

from patchwhisperer.kb.schema import HeroState
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
    typer.echo(f"{t.title} ({t.author}) -> {out} ({len(t.text)} chars)")


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


def main() -> None:
    app()
