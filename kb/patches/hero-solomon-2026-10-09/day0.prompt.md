# Task: first evaluation of a newly released hero

Hero: Solomon
Date: 2026-10-09

## Kit (from game data; descriptions are the in-game tooltips)

type: mystic | gun: Projectile | tags: Strategist, Focused, Checkmate | complexity: 1
base stats: hp 780 | move 6.7 | sprint 3.25 | stamina 2 | light melee 50.0 | heavy melee 116 | regen 2.0
**Setup Bishop** — Create a bishop that remains in place indefinitely. Move ( ): Moves the bishop, applying a fading slow and dealing spirit damage to enemies it passes through. After a delay, activates diagonal squares that deal additional spirit damage when stepped on.Re-activate to recall all bishops, ending the ability.
  T1: MoveDistance 5m, FadingSlowPercent 15
  T2: MaxPieces 1, RecastWindow 8
  T3: TechArmorDamageReductionPerStack -2.5, MaxStacks 10, StackDuration 10, TileSteps 1
**Kingside Knight** — Promote an ally to be a knight, granting bonus stamina and barrier for a duration.If self-cast you develop yourself as king instead, granting double the barrier but no stamina. Move ( ): Moves the piece, making it invulnerable during the duration before landing.
  T1: AbilityCooldown -8
  T2: Stamina 1, CombatBarrier 80
  T3: MaxPieces 1, BonusTargetRadius 20m, RemoveDebuffs 1
**Rook Battery** — Release a pair of rooks that travel forward, dealing spirit damage and applying immobilize. If the rooks hit a wall, they reflect back in the opposite direction. Re-Activate: Split the rooks perpendicularly.
  T1: FireRateSlow 25, DebuffDuration 5
  T2: CurrentHealthPercent 5
  T3: AbilityCooldown -12, ImmobilizeDuration 0.5, MaxReflectCount 1
**Develop Queen** — 
  T1: AbilityCooldown -40
  T2: CheckmateThreshold 200, CheckmateThreshold 5, SlowPercent 15
  T3: TileSteps 1, QueenBonusMoves 2
popular items (early): Extra Regen (pick 38%, win 67%), Grit (pick 9%, win 75%), Guardian Ward (pick 6%, win 67%), Healbane (pick 6%, win 67%), High-Velocity Rounds (pick 40%, win 58%), Extra Spirit (pick 53%, win 60%), Extra Stamina (pick 19%, win 67%), Mystic Burst (pick 45%, win 71%)
popular items (mid): Arcane Surge (pick 11%, win 80%), Swift Striker (pick 11%, win 20%), Boundless Spirit (pick 6%, win 100%), Enduring Speed (pick 6%, win 100%), Extended Magazine (pick 6%, win 67%), Superior Cooldown (pick 40%, win 63%), Mystic Shot (pick 9%, win 100%), Express Shot (pick 9%, win 50%)
popular items (late): Vortex Web (pick 11%, win 100%), Swift Striker (pick 6%, win 33%), Boundless Spirit (pick 62%, win 52%), Superior Cooldown (pick 38%, win 50%), Divine Barrier (pick 17%, win 62%), Escalating Exposure (pick 6%, win 100%), Spirit Lifesteal (pick 9%, win 50%), Superior Duration (pick 9%, win 25%)

## Early ranked data (first days after release; inflated by novelty, one-tricks and unfamiliar opponents — treat as weak evidence)

(no ranked data yet)

## Release announcement

(none)

## Current meta thesis and map state

# Meta state
Last patch: Minor Update - 10-05-2026 (2026-10-05)

## Thesis
Games are still won in the map economy: templated PvE income — guaranteed Tough Crate routes from ~2:30, plus the Sunken Plaza (5-8 min) and Bell Tower (8+) hub fights — is the lead engine, so AoE/sustain camp-clearers and heavy-melee box farmers bank faster than pure lane bullies. The 10-05 patch repaired a trooper-speed regression, so wave crashes land on intended cadence again and lane tempo is marginally re-weighted upward versus camp farming — but no souls, bounty, objective, respawn, item or comeback lever moved, so the map-economy lead engine still decides games. The no-comeback valve is intact; The Broker's ~30-min Corrupted tier remains the only stall window for late scalers. Fight shape is unchanged: farm-route tempo, then forced telegraphed group fights at hubs.

## Economy and systems
- Comeback bounties stay trimmed; extra comeback souls reroute to the two lowest-econ players via tick gold. Farm and lane leads stick.
- Guardian bounty +10%, Walker +5%, objective share 30->25% (carried from 09-16).
- Parrying a Guardian/objective spends the parry (cooldown applies on objectives); only T3-bullet-resist picks (Apollo, Mo & Krill) still commit to dives.
- Respawn 38s at 20m — the long death tax keeps every pick's value high.
- Slows -20% globally, air drag 35%. Grounded kiting strong; flyers pulled down.
- Instant cast and Walker fireballs are live: combat fast, objectives hit back.
- Trooper speed regression fixed (10-05): waves crash on intended cadence. A restoration, not a new tempo lever.
- The Broker spawns ~30 min, then ~every 15 min; Corrupted negatives are a runtime read, not something to build toward.

## Map
Lanes renamed; four new districts added. Old neutrals are replaced by Haunt creatures: camps group, chase and hit harder, rewarding AoE clear and sustain. Farm sources: Tough Crates (58 souls, guaranteed, ~200-300-soul lane routes) require a Heavy Melee to open; Haunt camps; Sinner's Sacrifice variants; Buff Containers (ability range, spirit resist). Pickups: Healing Snacks (10% max HP), Steam Vents (invisibility roams). Hubs: Sunken Plaza (~5-8 min) and Bell Tower (8+, ~280 souls, a single rope up/down, three vaults) concentrate telegraphed group fights. New roofs/high ground and hiding spots — green lane holds a roof/tree above the bridge. Side asymmetry: Arch Mother's side owns Sunken Plaza plus the theater, so split WRs by map side.

## Archetype standing
- AoE/sustain camp clearers: stable (top) — crate/Haunt income untouched; only trooper cadence moved.
- Heavy-melee frontline/tanks: stable (up) — Tough Crate access plus sustain; Mo & Krill holds Billy's front-line slot.
- Roamers/pick assassins: stable — districts, hiding spots and Steam Vents unchanged.
- Stealth: stable — Vent routes expand; sense-reveal is the counter.
- Lane bullies / split pushers: up slightly — trooper-speed fix restores crash-timing punish and split-push conversion windows.
- Late scalers: down, softening — no comeback valve vs The Broker stall window.
- Flyers: down — air drag unchanged; Silver's Bola remains the answer.
- On-hit spirit carries: down — 09-16 item hits (Mercurial Magnum, Spiritual Overflow, Plated Armor) persist.
- Non-melee assassins (Calico-style): down — cat form cannot heavy-melee the crate economy.

## Watchlist
- Rat King WR post-nerf (ult cooldown 130->160, total banner DR 35->25%) — does 61% fall below ~55%?
- Sinclair pick rate — near-zero confirms the kit-steal slot is dead after the broad trim.
- Lane-phase dive/kill stats vs camp-farm souls — did restored trooper speed actually re-raise lane-bully WRs?
- Trooper cadence: watch for over-correction to faster-than-baseline waves.
- Tough Crates: a hotfix nerf still flips the farm-route thesis back toward lane tempo.
- Late-scaler WRs (Warden, Celeste, Infernus) after 30 min — validates Broker-as-safety-valve.

## Recent history
- Minor Update - 10-05-2026: trooper-speed regression fixed (lane cadence restored); Rat King and Sinclair trimmed; map-economy engine untouched.
- City Never Sleeps: map rework — renamed lanes, four districts, Haunt camps replace neutrals, Tough Crate/Broker economy; lead engine moves off the lane.
- Minor Update - 09-16-2026: tempo patch — comeback souls gutted, on-hit spirit carry killed, flyers taxed.
- 08-22-2026: Celeste tuning.
- 08-12-2026: McGinnis/Apollo tuning.

## Current tier list (for cross-hero reasoning)

Infernus: B (stable) — gun/spirit carry
Seven: B (rising) — spirit carry
Vindicta: A (rising) — poke/siege carry
Lady Geist: A (rising) — spirit bruiser
Abrams: B (rising) — tank initiator
Wraith: B (falling) — gun carry
McGinnis: B (rising) — poke/siege controller
Paradox: B (rising) — pick/sniper initiator
Dynamo: A (rising) — initiator/support
Kelvin: B (rising) — support/healer
Haze: B (rising) — gun carry
Holliday: A (rising) — mobile assassin
Bebop: B (falling) — hook initiator
Calico: A (stable) — mobile assassin
Grey Talon: C (falling) — poke/siege carry
Mo & Krill: A (rising) — spirit tank initiator
Shiv: A (rising) — anti-tank spirit bruiser
Ivy: A (falling) — support/healer
Warden: C (falling) — gun carry
Yamato: A (rising) — mobile burst assassin
Lash: S (rising) — mobile initiator
Viscous: B (falling) — tank/enabler
Pocket: B (falling) — spirit carry
Mirage: B (falling) — split-push hybrid carry
Vyper: B (falling) — gun carry
Sinclair: C (falling) — burst cast/steal
Mina: C (stable) — mobile spirit assassin
Drifter: A (rising) — melee bruiser
Venator: A (rising) — gun carry
Victor: A (rising) — tank/frontline
Paige: S (rising) — lane-winning support
The Doorman: B (stable) — utility initiator
Billy: A (falling) — tank/frontline
Graves: C (falling) — gun carry/summoner split pusher
Apollo: S (rising) — lane bully initiator
Rem: B (rising) — support/healer
Silver: S (rising) — gun tank carry
Celeste: B (falling) — spirit burst carry
Rat King: A (stable) — frontline brawler
Baba: B (stable) — bulky spirit bruiser-caster

## Reader corrections (authoritative)

# Reader corrections

Human-authored facts and judgments that override model output. Injected verbatim into
the KB enrichment and the per-hero analysis stage. Keep entries short; date them.

## 2026-09-19

- Infernus: not a pure gun hero. Roughly 50/50 between a gun build (burn synergy) and
  "Dashfernus", a full-spirit dash/mobility build. Both are mainstream, not niche.
- Vindicta: S tier is doubtful. Flyers got hurt this patch: Silver's Weighted Bola now
  grounds/interrupts flyers, and slows now affect air drag. Cross-hero effects like this
  (a buffed anti-air tool on a strong hero) must count against flyers.
- Calico: likely benefits from the tempo meta; re-evaluate upward.
- Haze: rated too high. The Fixation buff is good but T4 gun items are still weak, so
  gun carries that depend on them do not scale as the tier suggests. Compare against
  Venator, who is probably the better pick in that slot.
- General: reason about builds (which items, gun vs spirit, and how popular each build
  actually is) and about how heroes affect each other given who is strong right now,
  not just about a hero's own numbers.

## 2026-09-23

- Haze: not inherently a side-lane farming gun carry. That is how she is played in the
  current patch, but historically she often plays as a roamer/ganker (Smoke Bomb picks,
  Fixation on isolated targets). Her playstyle swings with balance and meta, so frame the
  farm-carry role as meta-dependent, not as her identity.
- Counter items: note the main counter items per archetype where relevant (e.g. Plated
  Armor vs gun carries, Phantom Strike vs flyers/mobile heroes), but remember counters
  have counters (e.g. Armor Piercing Rounds vs Plated Armor). Mention the key ones; do
  not try to list every counter item for every hero.


## What creators have said about this hero (may be empty)

(none)

## Other announced heroes not yet released

Deadman Danny, Violet, Nurse Harrow

## Item names in the game (canonical spelling; do not invent items)

Active Reload, Alchemical Fire, Arcane Surge, Arctic Blast, Armor Piercer, Ballistic Enchantment, Battle Vest, Berserker, Blood Tribute, Boundless Spirit, Bullet Lifesteal, Bullet Resilience, Bullet Resist Shredder, Burst Fire, Capacitor, Celestial Blessing, Cheat Death, Cloak of Opportunity, Close Quarters, Cold Front, Colossus, Compress Cooldown, Counterspell, Crippling Headshot, Crushing Fists, Cultist Sacrifice, Cursed Relic, Debuff Reducer, Decay, Disarming Hex, Dispel Magic, Divine Barrier, Diviner's Kevlar, Duration Extender, Echo Shard, Electric Slippers, Enchanter's Emblem, Enduring Speed, Escalating Exposure, Escalating Resilience, Eternal Gift, Ethereal Shift, Express Shot, Extended Magazine, Extra Charge, Extra Health, Extra Regen, Extra Spirit, Extra Stamina, Fleetfoot, Focus Lens, Fortitude, Frenzy, Frostbite Charm, Fury Trance, Glass Cannon, Golden Goose Egg, Greater Expansion, Grit, Guardian Ward, Haunting Shot, Headhunter, Headshot Booster, Healbane, Healing Booster, Healing Nova, Healing Rite, Healing Tempo, Heroic Aura, High-Velocity Rounds, Hollow Point, Hunter's Aura, Improved Spirit, Indomitable, Infinite Rounds, Infuser, Inhibitor, Intensifying Magazine, Juggernaut, Kinetic Dash, Knockdown, Leech, Lifestrike, Lightning Scroll, Long Range, Lucky Shot, Magic Carpet, Majestic Leap, Melee Charge, Melee Lifesteal, Mercurial Magnum, Metal Skin, Monster Rounds, Mystic Burst, Mystic Conduit, Mystic Expansion, Mystic Regeneration, Mystic Reverb, Mystic Shot, Mystic Slow, Mystic Vulnerability, Mystical Piano, Nullification Burst, Omnicharge Signet, Opening Rounds, Phantom Strike, Plated Armor, Point Blank, Prism Blast, Quicksilver Reload, Radiant Regeneration, Rapid Recharge, Rapid Rounds, Reactive Barrier, Rebuttal, Recharging Rush, Refresher, Rescue Beam, Restorative Locket, Restorative Shot, Return Fire, Ricochet, Runed Gauntlets, Rusted Barrel, Scourge, Seraphim Wings, Shadow Strike, Shadow Weave, Sharpshooter, Shrink Ray, Silence Wave, Silencer, Siphon Bullets, Slowing Bullets, Slowing Hex, Spellbreaker, Spellslinger, Spirit Burn, Spirit Lifesteal, Spirit Rend, Spirit Resilience, Spirit Sap, Spirit Shielding, Spirit Shredder, Spirit Snatch, Spirit Strike, Spiritual Overflow, Split Shot, Sprint Boots, Stalker, Stamina Mastery, Superior Cooldown, Superior Duration, Suppressor, Surge of Power, Swift Striker, Tankbuster, Tesla Bullets, Titanic Magazine, Torment Pulse, Toxic Bullets, Transcendent Cooldown, Trophy Collector, Unstable Concoction, Unstoppable, Vampiric Burst, Veil Walker, Vortex Web, Warp Stone, Weakening Headshot, Weapon Shielding, Weighted Shots, Witchmail

## What to do

Produce the first knowledge-base entry and a short reader card for this hero. You have the kit, not months of data, so reason from mechanics: what the abilities do together, the power pattern (lane bully, scaler, teamfight, pick, split push), what the hero needs to function (farm, setup, peel) and what shuts it down (specific heroes, items such as anti-heal, silence, knockdown, Plated Armor, Phantom Strike). Then place it in the *current* meta and map (see thesis and map state): which objectives, farm sources and fight shapes it exploits or struggles with, and which strong heroes it threatens or is threatened by. Use the popular-items data to describe the builds people are actually running, and judge whether they make sense.

Keep the KB entry in the same shape as other heroes. Tier is provisional: pick the tier the kit and early signals justify and set `confidence` <= 0.5. In `notes` say what would change your mind within a week.

The card is what a player reads in 20 seconds: headline, 3-5 kit bullets, one or two sentences on meta fit, who it beats and who beats it, build read, provisional tier with confidence, and 2-3 things to watch before the 7-day data check-in.

## Output schema

{
  "enrichment": {
    "role": "short label",
    "archetypes": ["from: gun carry, spirit carry, burst caster, tank/frontline, lane bully, late scaler, mobile assassin, support/healer, split pusher, initiator, poke/siege"],
    "tier": "S|A|B|C|D",
    "trend": "rising|stable|falling",
    "why": "2-3 sentences, present tense",
    "builds": [{"name": "string", "damage": "gun|spirit|hybrid", "core_items": ["..."], "popularity": "primary|secondary|niche", "notes": "1 sentence"}],
    "core_items": ["..."],
    "matchups": {"beats": ["hero"], "loses_to": ["hero"]},
    "matchup_notes": "1-3 sentences",
    "enabled_by": ["..."],
    "countered_by": ["..."],
    "notes": "up to 3 lines",
    "confidence": 0.0
  },
  "card": {
    "headline": "<= 20 words",
    "kit_read": ["3-5 bullets"],
    "meta_fit": "1-2 sentences",
    "threatens": ["Hero — why", "..."],
    "threatened_by": ["Hero or item — why", "..."],
    "build_read": "1-2 sentences",
    "provisional_tier": "S|A|B|C|D",
    "confidence": 0.0,
    "what_to_watch": ["2-3 items"]
  }
}
