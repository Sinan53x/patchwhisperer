# Task: systems analysis

Patch: Halloween 2026 + Gameplay Update (2026-10-30)

## Current meta thesis (knowledge base, written before this patch)

# Meta state
Last patch: Shh... This Won't Hurt a Bit. (2026-10-20)

## Thesis
Souls sit off-lane now: four corridors, nine Haunt types and contested hubs pay better than lane static, so income is a coverage problem a five-man team cannot solve — AoE camp clearers and heavy-melee crate openers bank first, single-target lane bullies and split pushers starve. Fights get scheduled at Bell Tower, Sunken Plaza and Buff Container spawns instead of picked in lane. Tempo still closes most lobbies before a late spike, but the wider map hands late scalers a longer leash than Paint the Town did.

## Economy and systems
- Comeback bounties stay trimmed; extra comeback souls reroute to the two lowest-econ players via tick gold. Leads stick.
- Guardian bounty +10%, Walker +5%, objective share 30->25% (09-16, holds).
- Kill income is contested: the Soul Bag must be last-hit after the kill, so secure-burst conversions stay unreliable.
- Objective parries no longer reset the parry cooldown — Guardian and Shrine dives are one-shot commitments.
- Respawn 38s at 20m; slows -20% globally, air drag 35% — grounded kiting strong, flyers taxed.
- The Broker spawns ~30 min then ~every 15 min, relocates per match and is not on the map; Corrupted rolls are symmetric, public and a runtime read.
- Cast-on-press: abilities fire on the input, not the next window — tightens combos and clutch parries for high-execution kits.

## Map
Lanes renamed; four districts plus off-lane corridors. Every neutral camp is one of nine Haunt creature types — they group, chase and hit harder, souls varying by type. Farm: Tough Crates (58 souls, guaranteed) need Heavy Melee; Barrel Mimics turn breakable-chaining into a fight rather than free tempo; Haunt camps; Sinner's Sacrifice variants; Buff Containers roll permanent Move Speed and Bullet/Spirit Resist alongside ability range, so tanks contest them. Pickups: Healing Snacks (10% max HP) and Steam Vents (invisibility roams). Hubs: Sunken Plaza (~5-8 min, stamina strip) and Bell Tower (8+, ~280 souls, one rope, three vaults, map-wide bell broadcast). Green lane holds a roof/tree above the bridge. Side asymmetry: Arch Mother's side owns Sunken Plaza plus the theater.

## Archetype standing
- AoE/sustain camp clearers: up — grouped, chasing Haunts make AoE the fastest income (Seven, Yamato, McGinnis, Infernus, Mina).
- Heavy-melee frontline/tanks: up — Tough Crates plus camp chip damage reward Heavy Melee and regen (Mo & Krill, Abrams, Rat King, Drifter).
- Sustain bruisers: up — harder camps reward regen stacks (Victor, Shiv, Kelvin).
- Roamers/pick assassins: up — corridors, Steam Vents and new hiding spots add angles (Holliday, Lash, Paradox, Drifter); Bebop's hook cannot convert on spread farm.
- Lane bullies: up — crate routes from ~2:30 convert lane pressure (Paige, Apollo), though Apollo's Guardian dive is now one-shot.
- Late scalers / split pushers: down — lane shoving converts to less income; the ~30-min Broker stock is the only real late spike (Mirage, Warden, Celeste, Graves).
- Flyers: down — air drag unchanged while vents hand divers an approach (Grey Talon, Celeste, Deadman Danny).
- Non-melee assassins: down — Calico's cat form still cannot heavy-melee the crate economy.
- Pre-placed trap/zone heroes: down — Graves' gun deletes Venator traps.

## Watchlist
- Per-Haunt-type souls and clear speed: if one type dominates, routes re-converge and the no-memorization intent fails.
- Average game length and share of games reaching the ~30-min Broker — the cleanest tempo-vs-stall test.
- Buff Container contest rate, especially Bullet Resist and Move Speed rolls.
- Steam Vent kill participation: if vent ganks spike, grouping discipline becomes the skill gap.
- Graves snapshot (56.5% WR / 40.9% PR) still conflicts with the KB (48.5% / 21%) — recheck.
- Rat King win rate against pick rate — an A-to-S jump this fast needs data.

## Recent history
- Shh... This Won't Hurt a Bit. (2026-10-20): off-lane corridors and hub fights priced in; Haunt behaviors, Barrel Mimics, Steam Vents, Healing Snacks, instant casts; Graves gun destroys Venator traps; Corrupted items at the Broker.
- Paint the Town (2026-10-16): nine Haunt camp types replace all neutrals, contested Soul Bags, objective-parry cooldown reset removed, permanent-stat Buff Containers, Corrupted tier, six vote-gated new heroes.
- Minor Update - 10-14-2026: Baba frontline cut; Deadman Danny buff package; Radiant Regeneration third trim.
- Minor Update - 10-05-2026: trooper-speed regression fixed; Rat King and Sinclair trimmed.
- City Never Sleeps: renamed lanes, four districts, Haunt camps replace neutrals, Tough Crate/Broker economy.


## Changes in the General / systems sections of this patch

General:
  - [neutral] {STEAM_CLAN_LOC_IMAGE}/45164767/6073862c8be5bfb374b9d02531bd64d50c1db8c5.png
  - [rework] As Halloween draws near, the residents of The Cursed Apple have put out some decorations to celebrate their favorite holiday. The Hideout gains a spooky new look, our heroes don masks, and NYC is now littered with pumpkins and curious Halloween Cauldrons that grant willing trick-or-treaters delicious candy.
  - [neutral] [img src="{STEAM_CLAN_LOC_IMAGE}/45164767/74c75f698993f653082fa1bfed91b2f9f5ce25d4.png"]As you walk down the streets of Manhattan during a match, you'll come across bubbling cauldrons boasting a tempting display of treats. With a Heavy Melee, break the cauldron to pick up a piece of Candy and stash it in your pocket for later. When you're feeling a bit snacky, you can consume the candy to grant yourself a boost of energy with the temporary Sugar Rush buff. - Who said candy is bad for you?
  - [rework] The Halloween festivities are available in-game now through November 2nd, 2026. Happy Haunting!
  - [neutral] -------------------------------
  - [neutral] General:
  - [neutral] Breakables growth values reduced by 10%
  - [fix] Fixed some boxes taking longer to respawn if another box's or powerup's pickup was left on the ground
  - [buff] Haunts base bounty and growth increased by 10%
  - [buff] Haunts HP and Damage output increased by 10%
  - [rework] Haunted Souls secure rate is now 25% slower
  - [rework] Haunted Souls secure rate is now up to 50% faster than baseline based on how far behind you are in Net Worth compared to the enemy team's average (max rate at a 20% Net Worth gap)
  - [neutral] Comeback gold from non-hero sources increased from a max of 26% to 30% (when behind by ~20% Net Worth)
  - [rework] The bonus NPC souls multiplier when behind now also increases tick souls for the 2 poorest players
  - [buff] Healing Snacks heal increased from 10% Max HP to 14%
  - [rework] Steam Vents now increase stamina regeneration by 150%
  - [neutral] Move slow to air drag ratio increased from 0.35 to 0.5
  - [nerf] Move speed in tunnels reduced from +70% to +50%
  - [fix] Fixed some bugs with Walker stomp logic
  - [rework] Latest 6 heroes are no longer categorized as "new" anymore. This means they have normal hero unlocking requirements for ranked and can now be banned.
  - [neutral] Items:
  - [neutral] Heroes:
  - [neutral] Street Brawl:

## Item and hero sections (for context only; do not analyze them here)

Items changed: Armor Piercer, Battle Vest, Bullet Lifesteal, Bullet Resilience, Crippling Headshot, Decay, Divine Barrier, Echo Shard, Express Shot, Focus Lens, Fury Trance, Glass Cannon, Golden Goose Egg, Healbane, Healing Booster, Healing Nova, High-Velocity Rounds, Hunter's Aura, Infuser, Juggernaut, Leech, Lightning Scroll, Metal Skin, Mystic Slow, Point Blank, Radiant Regeneration, Rebuttal, Return Fire, Shadow Weave, Silence Wave, Spellbreaker, Spirit Lifesteal, Spirit Sap, Spirit Shielding, Spiritual Overflow, Torment Pulse, Toxic Bullets, Vampiric Burst
Heroes changed: Abrams, Apollo, Baba, Billy, Calico, Celeste, Deadman Danny, Drifter, Graves, Grey Talon, Haunts - Past Dues, Haze, Infernus, Kelvin, Lady Geist, Lash, McGinnis, Mid-Boss, Mirage, Mo & Krill, Nurse Harrow, Paige, Paradox, Rat King, Seven, Shiv, Silver, Solomon, The Doorman, Venator, Victor, Violet, Viscous, Warden, Wraith, Yamato

## Update summary

(n/a)

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
