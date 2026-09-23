# Task: systems analysis

Patch: Minor Update - 09-16-2026 (2026-09-16)

## Current meta thesis (knowledge base, written before this patch)

# Meta state
Last patch: Minor Update - 09-16-2026 (2026-09-16)

## Thesis
The 09-16 patch finished what the 07-30 comeback rework started: it gutted comeback souls and early Unstable Rift generosity, so winning lane now actually wins the game. Tempo beats scaling. Early snowballers and mobile bruisers (Paige, Apollo, Silver, Yamato, Vindicta, Holliday, Lash, Haze) rise; late scalers and flyers (Celeste, Warden, Wraith) fall. The old "overloaded DLC" S-tiers (Mirage, Venator, Doorman, Pocket) keep their kits but sit at ~46% WR — the meta stopped rewarding them.

## Economy and systems
Comeback bounty trimmed and extra comeback souls partly rerouted to the two lowest-econ players via tick gold, killing the fed AFK farmer. Guardian bounty +10%, Walker +5%, objective share 30->25%. Rift resist is now 10% +1%/min (cap 40% at 30m) instead of a flat 35% — early rift fights are real fights. Respawn at 20m 35->38s. Stuns/parry pause reload instead of resetting; dashes and light melee no longer break gun cycle time (Silver/Abrams smoothing); slows -20% globally but now hit air drag at 35% (flyers down, slow-as-CC up).

## Archetype standing
Early tempo and mobile frontline lead; late scalers lose their safety net. Tanks stay fine (Abrams/Dynamo/Mo) — core tank items untouched. Supports hold value (Ivy 53.7%, Paige rising) but healing items were trimmed (Radiant Regeneration, Restorative Locket).

## Watchlist
- Silver: Weighted Bola acts as Phantom Strike, plus +health/+sprint and the gun-cycle change. Biggest winner.
- Apollo: absent from notes, best snowballer — "super buffed" by tempo.
- Celeste: 7 nerfs plus item/scaling/air-drag hits; her 54.6% WR is a lagging pre-patch number.
- Veil Walker buyers (Holliday, Warden): item lost Sprint Boots and movespeed-on-break.

## Recent history
07-30 added Ranked Mode. 07-09/07-28 item and hero tuning; 08-12 McGinnis/Apollo; 08-22 Celeste; 09-16 tempo patch. The 07-16 creator read framed the game as a stat-check with S-tier DLC kits; current data (those kits mid at high rank) and the tempo patch are the newer, authoritative state. Snapshot is 14 days and mostly pre-patch, so treat its WRs as baseline, not post-patch.

## Changes in the General / systems sections of this patch

General:
  - [rework] Unstable Rift comeback resist max values now scale over the course of the game. Previously the max values were 35%. Now it is 10% + 1% per minute (around ~20% for the first one), with an upper limit of 40% at 30 minutes.
  - [fix] Removed a fixed amount of extra bonus souls you would get for being behind even a very slightly amount in net worth for both hero kill bounties as well as Unstable Rift bounties (this had a larger impact on the early to mid game)
  - [neutral] Slightly reduced comeback bounties in general (this is in addition to the above change)
  - [neutral] A portion of the comeback souls earned by players above enemy teams average net worth is instead distributed via the tick gold system that is given to the lowest 2 players (70% of the extra comeback value goes to them)
  - [buff] Guardian bounty increased by 10%
  - [buff] Walker bounty increased by 5%
  - [nerf] Share for objectives bounty to nearby heroes reduced from 30% to 25% (the remaining gets split between all 6 players)
  - [nerf] Respawn Time at 20 minutes increased from 35s to 38s (does not affect the max values later on, just a little higher earlier)
  - [rework] Using parry now pauses reloading
  - [rework] Parrying while doing a regular dash will now cancel the dash (and momentum) and parry on the spot
  - [rework] Getting stunned now pauses your reload rather than restarting it
  - [neutral] Breakables in the underground tunnels initial spawn time increased from 3m to 5m
  - [neutral] Breakables in the underground tunnels respawn rate increased from 3m to 5m
  - [neutral] All move slow values reduced by ~20% globally
  - [neutral] All ground dash slows reduced by ~10% globally
  - [rework] Slows now also affect air drag by 35% of the slow value (convar citadel_enable_slows_affect_air_drag to toggle the slow drag behavior on and off)
  - [rework] Dashes and light melee's no longer pause your gun's cycle time (this is a general change that affects high-cycle time weapons the most like Silver or Abrams)

## Item and hero sections (for context only; do not analyze them here)

Items changed: Ballistic Enchantment, Cultist Sacrifice, Decay, Diviner's Kevlar, Focus Lens, Fortitude, Golden Goose Egg, Hollow Point, Leech, Lifestrike, Mercurial Magnum, Plated Armor, Radiant Regeneration, Restorative Locket, Shadow Weave, Slowing Hex, Spiritual Overflow, Tankbuster, Toxic Bullets, Trophy Collector, Veil Walker, Weakening Headshot
Heroes changed: Abrams, Celeste, Graves, Haze, Holliday, Ivy, Kelvin, Lady Geist, Lash, Paige, Paradox, Rem, Shiv, Silver, Venator, Viscous, Vyper, Warden, Wraith, Yamato

## What to do

Analyze only the systems-level changes. For each distinct system that moved (economy, comeback, objectives, respawn, movement, slows, parry/melee, reload, map/jungle, matchmaking), explain what changed and what it does to how the game is played. Then read the patch's tempo direction: does it reward early aggression and snowballing (toward tempo) or late scaling and comebacks (toward scaling)? Finally, map the effect onto hero archetypes.

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
