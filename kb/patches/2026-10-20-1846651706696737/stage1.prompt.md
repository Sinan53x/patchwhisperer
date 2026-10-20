# Task: systems analysis

Patch: Shh... This Won't Hurt a Bit. (2026-10-20)

## Current meta thesis (knowledge base, written before this patch)

# Meta state
Last patch: Paint the Town (2026-10-16)

## Thesis
Games are still won in the map economy, but memorized routes are dead. Souls now come from behavior-varied Haunt camps, contested Soul Bags, permanent-stat Buff Containers and earlier district objectives, so map knowledge and fast-clear kits bank faster than template memorizers. Tempo closes games before late spikes: AoE camp clearers, heavy-melee crate farmers and sustained frontlines carry.

## Economy and systems
- Comeback bounties stay trimmed; extra comeback souls reroute to the two lowest-econ players via tick gold. Leads stick.
- Guardian bounty +10%, Walker +5%, objective share 30->25% (09-16, holds).
- Kill income is contested: the Soul Bag must be last-hit after the kill, so secure-burst conversions are less reliable.
- Objective parries no longer reset the parry cooldown — the free objective-parry chain is gone. T3-bullet-resist picks (Apollo, Mo & Krill) can still commit under a Guardian.
- Respawn 38s at 20m; slows -20% globally, air drag 35% — grounded kiting strong, flyers taxed.
- The Broker spawns ~30 min then ~every 15 min; Corrupted rolls are symmetric and a runtime read.

## Map
Lanes renamed; four districts. Every neutral camp is now one of nine Haunt creature types — they group, chase and hit harder, with souls varying by type. Farm: Tough Crates (58 souls, guaranteed, ~200-300-soul lane routes) need Heavy Melee; Haunt camps; Sinner's Sacrifice variants; Buff Containers now roll permanent stats — Move Speed plus Bullet/Spirit Resist alongside the old ability-range roll — so tanks contest them too. Pickups: Healing Snacks (10% max HP) and Steam Vents (invisibility roams). Hubs: Sunken Plaza (~5-8 min, stamina strip) and Bell Tower (8+, ~280 souls, one rope, three vaults, bell broadcast). Green lane holds a roof/tree above the bridge. Side asymmetry: Arch Mother's side owns Sunken Plaza plus the theater.

## Archetype standing
- AoE/sustain camp clearers: up — grouped, chasing Haunts make AoE the fastest route to income (Seven, Yamato, McGinnis, Infernus).
- Heavy-melee frontline/tanks: up — Tough Crates stay the guaranteed route; Mo & Krill holds the default slot as Billy slips.
- Sustain bruisers: up — harder camps reward regen stacks (Victor, Shiv); Radiant Regeneration's third trim still erodes the shared item.
- Roamers/pick assassins: up slightly — districts, Steam Vents and hiding spots add pick angles (Holliday, Paradox, Drifter).
- Lane bullies: up — crate/hub timings from ~2:30 convert lane pressure (Paige, Apollo).
- Late scalers / split pushers: down — contested Soul Bags and earlier hubs close games before the spike (Warden, Mirage, Celeste, Graves).
- Flyers: down — air drag unchanged, Silver's Bola the answer; Deadman Danny is the test of whether raw numbers beat the tax.
- Non-melee assassins: down — Calico's cat form still can't heavy-melee the crate economy.

## Watchlist
- Which Haunt types actually pay — soul values and clear difficulty are unstated, so farm-worthiness is a live discovery.
- Six vote-gated new heroes: track pick/win as the rollout schedule runs; day-one data is a lottery.
- Soul Bag pickup rate — does the bounty actually extend fights, or does it shift nothing?
- Buff Container contest rate, especially Move Speed and Bullet Resist rolls.
- Whether tempo closes lobbies before The Broker's ~30-min window, or just relocates the stall to the new hubs.
- Graves snapshot (56.5% WR / 40.9% PR) conflicts with the KB (48.5% / 21%) — recheck.

## Recent history
- Paint the Town (2026-10-16): nine Haunt camp types replace all neutrals, contested Soul Bags, objective-parry cooldown reset removed, permanent-stat Buff Containers, Corrupted tier (incl. Street Brawl), six vote-gated new heroes.
- Minor Update - 10-14-2026: Baba frontline cut; Deadman Danny buff package; Radiant Regeneration third trim.
- Minor Update - 10-05-2026: trooper-speed regression fixed; Rat King and Sinclair trimmed.
- City Never Sleeps: renamed lanes, four districts, Haunt camps replace neutrals, Tough Crate/Broker economy.
- Minor Update - 09-16-2026: tempo patch — comeback souls gutted, on-hit spirit carry killed, flyers taxed.

## Changes in the General / systems sections of this patch

Haunts:
  - [rework] Haunts: all neutral camps replaced by new creature types (Specimen, Gutter Ghouls, Barrel Mimics, Past Dues, Stage Hands, Crabbage Pots, Festival Spirit, Shrooms, Underhands) with new behaviors — prior clear routes, timings and sustain math no longer transfer
Barrel Mimics:
  - [rework] Barrel Mimics: some breakables are now mimics — smashing crates and boxes in the jungle is no longer free souls
Districts:
  - [rework] Districts: four off-lane corridors added (Theater, Chinatown, Haunted Lot, Plaza) with their own content — souls are no longer concentrated on the three lanes
Sunken Plaza:
  - [neutral] Sunken Plaza: high-risk sub-area below the Plaza District square; stamina drains as you descend and outside sound fades — taxes low-mobility and disengage-poor kits, pays those who can commit
Bell Tower:
  - [neutral] Bell Tower: Chinatown vertical objective; concentrated soul hotspot at the top, but collecting rings the bell map-wide — turns a farm route into a broadcast gank target
Tough Crates:
  - [neutral] Tough Crates: breakables requiring a Heavy Melee that pay extra souls — rewards heavy-melee access and gives melee-capable kits a farm lane lanes cannot contest
Buff Containers:
  - [rework] Buff Containers: revamped golden statues now also roll permanent Spirit Resist, Bullet Resist, Ability Range and Move Speed — not just a damage/health pickup, so permanent-buff contests matter for tanks and casters alike
Healing Snacks:
  - [neutral] Healing Snacks: hidden pickups scattered around the map for healing in a pinch — reduces forced base returns during lane phase
Steam Vents:
  - [neutral] Steam Vents: standing on one grants invisibility and small regen — new gank setup and disengage tool; makes vision and grouped rotations stronger
The Broker:
  - [neutral] The Broker: temporary merchant that relocates per match (dark uptown alley, abandoned Chinatown storefront); first stock around 30 minutes, further Corrupted items roughly every 15 minutes after — pulls players to a contested point in the mid/late game
Sinner's Sacrifice:
  - [fix] Sinner's Sacrifice: bonus now has variable timings — the ritual is no longer a fixed-timer camp, so pre-timing it is harder
Lanes:
  - [neutral] Lanes: renamed Broadway (blue), Greenwich (green), York (yellow) — callouts change with the visual rework; treat old lane knowledge as dated
Uptown:
  - [neutral] Uptown: positioned as the quickest route to where the action is — rotations and collapses will route through it
Ability/item cast:
  - [neutral] Ability/item cast: fires the instant the button is pressed instead of on the next input window — reaction speed, cancels and clutch parries get tighter for every hero
Parry:
  - [rework] Parry: successfully parrying objectives no longer resets Parry cooldown — objective-parry stops being a free defensive reset before a fight
Walkers:
  - [rework] Walkers: no longer keep firing fireballs after dying — diving a Walker you just killed is now safe
Street Brawl:
  - [neutral] Street Brawl: corrupted item granted after the Round 5 item draft
Hero releases:
  - [neutral] Hero releases: six new heroes, two per week on Tue/Fri 2:00pm PT, first release Oct 2, order decided by vote; voting moved to the Pregame lobby with the winning team's votes counting double, and play earns priority tokens

## Item and hero sections (for context only; do not analyze them here)

Items changed: Corrupted Items
Heroes changed: Baba, Big Turnout, Corrupted Items, Deadman Danny, Dedication, Graves, Highly Effective, Nurse Harrow, Oracle, Rat King, Solomon, Unlucky, Victor, Violet, Yamato

## Update summary

A structural map-and-content update rather than a numbers patch: the neutral/jungle layer is rebuilt around new Haunt creatures, four off-lane Districts with their own objectives (Sunken Plaza, Bell Tower, Tough Crates, Steam Vents, Healing Snacks), and a rotating merchant, The Broker, who injects per-match Corrupted items into the economy. Six new heroes arrive on a voted, staggered release schedule, so the meta read is mostly about where souls now come from and which kits can exploit the new map geometry. No hero balance numbers were published, so archetype shifts are inferred from systems, not tuning.

## Creator sources published after this patch (optional corroboration; the notes, KB and snapshot remain primary — if a source contradicts them, say so and keep your own read)

(none)

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
