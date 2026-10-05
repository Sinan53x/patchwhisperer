# Task: systems analysis

Patch: Minor Update - 10-05-2026 (2026-10-05)

## Current meta thesis (knowledge base, written before this patch)

# Meta state
Last patch: City Never Sleeps (2026-09-29)

## Thesis
Games are won in the map economy now, not the lane. Templated PvE income — guaranteed Tough Crate routes from ~2:30 and the Sunken Plaza (5-8 min) and Bell Tower (8+) hub fights — is the lead engine, so AoE/sustain camp-clearers and heavy-melee box farmers bank faster than pure lane bullies. The no-comeback valve is intact, so leads still close games, but The Broker's ~30-min Corrupted tier gives late scalers a concrete reason to stall and partly re-opens scaling. Fight shape = farm-route tempo, then forced, telegraphed group fights at hubs.

## Economy and systems
- Comeback bounties stay trimmed; extra comeback souls still reroute to the two lowest-econ players via tick gold — farm and lane leads stick.
- Guardian bounty +10%, Walker +5%, objective share 30->25% (carried from 09-16).
- Parrying a Guardian/objective now spends the parry (cooldown applies on objectives), so tower-diving is punishable for most of the roster; only T3-bullet-resist picks (Apollo, Mo & Krill) still commit.
- Respawn still 38s at 20m — the longer death tax raises every pick's value.
- Slows -20% globally, air drag 35% (unchanged): grounded kiting strong, flyers pulled down.
- Instant cast and Walker fireballs are live: combat is faster and objectives hit back harder.
- The Broker spawns ~30 min, then ~every 15 min. Corrupted items roll match-wide identical random negatives — a runtime read, not something you build toward.

## Map
Lanes renamed; four new districts added. All old neutrals are replaced by new Haunt creatures: camps group and chase, and hit harder, rewarding AoE clear and sustain. Farm sources: Tough Crates (58 souls, guaranteed, ~200-300-soul lane routes) require a Heavy Melee to open; Haunt camps; Sinner's Sacrifice variants; Buff Containers (ability range, spirit resist). Pickups: Healing Snacks (10% max HP), Steam Vents (invisibility roams). Hubs: Sunken Plaza (~5-8 min) and Bell Tower (8+, ~280 souls, a single rope up/down, three vaults) concentrate telegraphed group fights. New roofs/high ground and hiding spots — green lane holds a roof/tree above the bridge. Side asymmetry: Arch Mother's side owns Sunken Plaza plus the theater, so watch win rate by map side.

## Archetype standing
- AoE/sustain camp clearers: up — stacked, chasing Haunt camps and heavier camp damage reward Storm Cloud/punch-style clears.
- Heavy-melee frontline/tanks: up — Tough Crate access plus sustain; Mo & Krill takes Billy's front-line slot.
- Roamers/pick assassins: up — more districts, hiding spots and Steam Vents; Paradox ahead of Bebop in the slot.
- Stealth: up — Vent layout expands routes, and sense-reveal is the counter.
- Late scalers: down, softening — no comeback valve vs The Broker stall window.
- Flyers: down — air-drag slows unchanged; Silver's Bola remains the answer.
- On-hit spirit carries: down — 09-16 item hits (Mercurial Magnum, Spiritual Overflow, Plated Armor) persist.
- Non-melee assassins (Calico-style): down — cat form cannot heavy-melee the crate economy.

## Watchlist
- Tough Crates: peercontent expects a hotfix nerf — that would flip the farm-route thesis back toward lane tempo.
- Yamato/Seven/Mina presence and WR as the camp-clear AoE test.
- Calico and Bebop pick rates — near-zero confirms the crate-lockout and roamer-slot reads.
- Late-scaler WRs (Warden, Celeste, Infernus) after 30 min — validates Broker-as-safety-valve.
- Arch Mother vs other side win rates — quantify the side asymmetry.
- Infernus WR: peercontent reports an undocumented global napalm team-amp removal — unverified, not in notes.

## Recent history
- City Never Sleeps: map rework — renamed lanes, four districts, Haunt camps replace neutrals, Tough Crate/Broker economy; the lead engine moves off the lane.
- Minor Update - 09-16-2026: tempo patch — comeback souls gutted, on-hit spirit carry killed, flyers taxed.
- 08-22-2026: Celeste tuning.
- 08-12-2026: McGinnis/Apollo tuning.
- 07-30-2026: Ranked Mode added.

## Changes in the General / systems sections of this patch

General:
  - [fix] Fixed bugs that were causing troopers to walk too slowly in lane

## Item and hero sections (for context only; do not analyze them here)

Items changed: (none)
Heroes changed: Rat King, Sinclair

## Update summary

{{digest_summary}}

## Creator sources published after this patch (optional corroboration; the notes, KB and snapshot remain primary — if a source contradicts them, say so and keep your own read)

{{creator_sources}}

## What to do

Analyze only the systems-level changes. For each distinct system that moved (economy, comeback, objectives, respawn, movement, slows, parry/melee, reload, map/jungle/objectives, matchmaking), explain what changed and what it does to how the game is played. Then read the patch's tempo direction: does it reward early aggression and snowballing (toward tempo) or late scaling and comebacks (toward scaling)? Finally, map the effect onto hero archetypes.

For a major content update the input is prose, not number tweaks; still produce one `systems_changed` entry per system that moved and read tempo from how soul income and fight locations changed.

Archetype vocabulary (use these labels): gun carry, spirit carry, burst caster, tank/frontline, lane bully, late scaler, mobile assassin, support/healer, split pusher, initiator, poke/siege.

If there are no systems changes, return empty lists and a neutral tempo shift with why = "no systems changes".

## Output schema

{
  "systems_changed": [
    {"system": "string", "change_summary": "1-2 sentences", "driving_changes": ["raw change text", "..."], "magnitude": "minor|moderate|major", "effect_on_play": "1-2 sentences"}
  ],
  "tempo_shift": {"direction": "toward_tempo|toward_scaling|neutral", "confidence": 0.0, "why": "1-2 sentences"},
  "archetype_effects": [
    {"archetype": "string from vocabulary", "direction": "up|down|neutral", "magnitude": "minor|moderate|major", "why": "1 sentence naming the driver"}
  ],
  "intent_read": "1-3 sentences on what problem Valve appears to be solving"
}
