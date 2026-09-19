import asyncio
import logging
import os
from pathlib import Path

import discord
from discord import app_commands
from discord.ext import commands

from patchwhisperer.bot import jobs, poller, state
from patchwhisperer.kb.store import KBStore
from patchwhisperer.parse.entities import EntityIndex

log = logging.getLogger(__name__)

GUILD_ID = int(os.getenv("DISCORD_GUILD_ID", "0"))
CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID", "0"))
KB_ROOT = Path("kb")


def _resolve_heroes(
    index: EntityIndex, names: list[str]
) -> tuple[list[str], list[str]]:
    ok, bad = [], []
    for raw in names:
        raw = raw.strip()
        if not raw:
            continue
        hit = index.resolve(raw)
        if hit and hit[0].value == "hero":
            if hit[2] not in ok:
                ok.append(hit[2])
        else:
            bad.append(raw)
    return ok, bad


class PatchWhispererBot(commands.Bot):
    def __init__(self) -> None:
        intents = discord.Intents.default()
        intents.reactions = True
        super().__init__(command_prefix="!", intents=intents)
        self.index: EntityIndex | None = None
        self._poll_task: asyncio.Task | None = None

    async def setup_hook(self) -> None:
        state.init_db()
        self.index = await asyncio.to_thread(EntityIndex.load)
        self.tree.copy_global_to(guild=discord.Object(id=GUILD_ID))
        if GUILD_ID:
            await self.tree.sync(guild=discord.Object(id=GUILD_ID))
        self._poll_task = asyncio.create_task(poller.poll_loop(self._job, None))

    async def _job(self, gid: str) -> None:
        channel = self.get_channel(CHANNEL_ID) or await self.fetch_channel(CHANNEL_ID)
        loop = asyncio.get_running_loop()
        await asyncio.to_thread(jobs.analyze_and_post, gid, channel=channel, loop=loop)

    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        if payload.user_id == self.user.id:
            return
        emoji = str(payload.emoji)
        if emoji not in ("👍", "👎"):
            return
        kind = "reaction_up" if emoji == "👍" else "reaction_down"
        # find which patch this message belongs to
        with state._conn() as c:
            row = c.execute(
                "SELECT patch_id FROM posts WHERE message_id=?",
                (str(payload.message_id),),
            ).fetchone()
        if row:
            state.feedback_add(row["patch_id"], payload.user_id, kind)


def make_bot() -> PatchWhispererBot:
    bot = PatchWhispererBot()
    tree = bot.tree

    pool_group = app_commands.Group(name="pool", description="Manage your hero pool")

    @pool_group.command(name="show")
    async def pool_show(interaction: discord.Interaction):
        heroes = state.pool_get(interaction.user.id)
        await interaction.response.send_message(
            "Your pool: " + (", ".join(heroes) if heroes else "(empty)")
        )

    @pool_group.command(name="set")
    async def pool_set(interaction: discord.Interaction, heroes: str):
        ok, bad = _resolve_heroes(bot.index, heroes.split(","))
        state.pool_set(interaction.user.id, ok)
        msg = f"Pool set: {', '.join(ok)}"
        if bad:
            msg += f" (unrecognized: {', '.join(bad)})"
        await interaction.response.send_message(msg)

    @pool_group.command(name="add")
    async def pool_add(interaction: discord.Interaction, hero: str):
        ok, bad = _resolve_heroes(bot.index, [hero])
        if bad:
            await interaction.response.send_message(f"Unknown hero: {hero}")
            return
        current = state.pool_get(interaction.user.id)
        if ok[0] not in current:
            current.append(ok[0])
        state.pool_set(interaction.user.id, current)
        await interaction.response.send_message(f"Pool: {', '.join(current)}")

    @pool_group.command(name="remove")
    async def pool_remove(interaction: discord.Interaction, hero: str):
        ok, _ = _resolve_heroes(bot.index, [hero])
        current = state.pool_get(interaction.user.id)
        current = [h for h in current if not ok or h != ok[0]]
        state.pool_set(interaction.user.id, current)
        await interaction.response.send_message(f"Pool: {', '.join(current)}")

    tree.add_command(pool_group)

    @tree.command(name="analyze", description="Analyze a patch (gid or 'latest')")
    async def analyze(
        interaction: discord.Interaction, patch: str = "latest", force: bool = False
    ):
        await interaction.response.defer(ephemeral=True)
        seen = state.seen_get(patch)
        if seen and seen["kind"] in ("analyzed", "hotfix") and not force:
            await interaction.followup.send(
                f"{seen['title']} already processed; use force=True to re-run."
            )
            return
        try:
            result = await asyncio.to_thread(
                jobs.analyze_and_post,
                patch,
                force=force,
                channel=interaction.channel,
                loop=asyncio.get_running_loop(),
            )
            if result is None:
                await interaction.followup.send("Already processed (use force=True).")
            else:
                await interaction.followup.send(
                    f"Posted {result.kind}: {result.patch_id}"
                )
        except Exception as e:  # noqa: BLE001 - report any job failure to the user
            await interaction.followup.send(f"Failed: {str(e)[:300]}")

    @tree.command(name="patches", description="Recent patch posts")
    async def patches(interaction: discord.Interaction):
        from patchwhisperer.sources.steam_news import fetch_patch_posts

        posts = await asyncio.to_thread(fetch_patch_posts, 10)
        lines = []
        for p in posts:
            seen = state.seen_get(p.gid)
            mark = f" ({seen['kind']})" if seen else " (new)"
            lines.append(f"{p.date:%Y-%m-%d} {p.title}{mark}")
        await interaction.response.send_message("\n".join(lines) or "none")

    kb_group = app_commands.Group(name="kb", description="Knowledge base")

    @kb_group.command(name="hero", description="Show a hero's KB entry")
    @app_commands.describe(name="hero name")
    async def kb_hero(interaction: discord.Interaction, name: str):
        heroes = KBStore(KB_ROOT).load_heroes()
        hit = bot.index.resolve(name)
        canonical = hit[2] if hit and hit[0].value == "hero" else name
        h = heroes.get(canonical)
        if not h:
            await interaction.response.send_message(f"No KB entry for {name}")
            return
        lines = [
            f"**{h.name}** — tier {h.tier}, trend {h.trend}",
            f"role: {h.role or '?'} | archetypes: {', '.join(h.archetypes) or '?'}",
            f"why: {h.why or '(none)'}",
            f"core items: {', '.join(h.core_items) or '(none)'}",
            f"builds: {', '.join(h.build_variants) or '(none)'}",
            f"enabled by: {', '.join(h.enabled_by) or '(none)'}",
            f"countered by: {', '.join(h.countered_by) or '(none)'}",
            f"last changed: {h.last_changed_patch or 'never'}",
        ]
        if h.notes:
            lines.append(f"notes: {h.notes}")
        await interaction.response.send_message("\n".join(lines))

    @kb_hero.autocomplete("name")
    async def kb_hero_ac(interaction: discord.Interaction, current: str):
        names = [h["name"] for h in bot.index.heroes]
        return [
            app_commands.Choice(name=n, value=n)
            for n in names
            if current.lower() in n.lower()
        ][:25]

    tree.add_command(kb_group)

    @tree.command(name="feedback", description="Leave feedback on the latest analysis")
    async def feedback(interaction: discord.Interaction, text: str):
        latest = state.post_latest()
        if not latest:
            await interaction.response.send_message("No analysis posted yet.")
            return
        state.feedback_add(latest["patch_id"], interaction.user.id, "text", text)
        await interaction.response.send_message(
            f"Feedback stored against {latest['patch_id']}. Thanks!"
        )

    return bot


def run() -> None:
    logging.basicConfig(level=logging.INFO)
    token = os.getenv("DISCORD_TOKEN")
    if not token:
        raise SystemExit("DISCORD_TOKEN not set (see .env.example)")
    make_bot().run(token)
