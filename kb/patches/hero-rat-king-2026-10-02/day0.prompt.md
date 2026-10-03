# Task: first evaluation of a newly released hero

Hero: Rat King
Date: 2026-10-03

## Kit (from game data; descriptions are the in-game tooltips)

type: brawler | gun: Spreadshot | tags: Scrappy, Regal, Tenacious | complexity: 3
base stats: hp 800 | move 6.8 | sprint 1.6 | stamina 3 | light melee 50.0 | heavy melee 116 | regen 2.0
**Rat Swarm** — Call forth a swarm of rats that leap onto enemies, dealing spirit damage over time and reducing their bullet resist with every bite. The more rats are attached, the faster they will bite the target.Enemies can have multiple rats attached, but can shake off a rat early by performing a ground or air dash.
  T1: AbilityCharges 1
  T2: RatSwarmCols 2, RatSwarmRows 1, RatSwarmWidth 100, DebuffDuration 4
  T3: ArmorReductionPerBite -1, DamagePerBite 8
**Scrap Grenade** — Throw a grenade of scrap that detonates multiple times, dealing bullet damage and applying slow.The grenade can be meleed to knock it away.
  T1: AbilityCooldown -8
  T2: DamagePerShrapnel 65
  T3: Detonations 1, BigExplosionDamage 300, BigExplosionDamage 1.0, BigExplosionRadius 14m, BigExplosionRadius 1, BigExplosionSlowPercent 0.12
**Royal Pestments** — Adorn scrappy armor, gaining barrier based on your max health. As long as the armor holds, bullets have a chance to be deflected back towards the attacker.The barrier does not benefit from resists.
  T1: AbilityDuration 4
  T2: ReturnFireChance 15, AbilityCooldown -8
  T3: MaxHealthPct 10, MaxDamagePerHit 250
**Rule, Ratannia!** — Charge up and summon the banner of Ratannia, granting all nearby allies increased move speed, immunity from slows, and reduced incoming damage while near the banner.
  T1: AbilityCooldown -20, BonusMoveSpeed 1m
  T2: FlagDuration 8, Radius 8m, AbilityDuration 8
  T3: Damage 150, AllyDamageReduction 15
popular items (early): Extended Magazine (pick 24%, win 64%), Close Quarters (pick 37%, win 59%), Extra Regen (pick 54%, win 44%), Fleetfoot (pick 7%, win 33%), Extra Health (pick 15%, win 29%), High-Velocity Rounds (pick 78%, win 47%), Long Range (pick 7%, win 67%), Mystic Expansion (pick 7%, win 67%)
popular items (mid): Berserker (pick 9%, win 0%), Swift Striker (pick 9%, win 100%), Lifestrike (pick 7%, win 33%), Bullet Resist Shredder (pick 13%, win 50%), Ballistic Enchantment (pick 17%, win 62%), Burst Fire (pick 7%, win 0%), Enduring Speed (pick 50%, win 61%), Fortitude (pick 30%, win 43%)
popular items (late): Witchmail (pick 24%, win 82%), Armor Piercer (pick 9%, win 25%), Crippling Headshot (pick 9%, win 25%), Berserker (pick 11%, win 60%), Ballistic Enchantment (pick 30%, win 43%), Enduring Speed (pick 7%, win 33%), Cheat Death (pick 7%, win 33%), Fortitude (pick 11%, win 40%)

## Early ranked data (first days after release; inflated by novelty, one-tricks and unfamiliar opponents — treat as weak evidence)

WR 59.4% | PR 8.5% | matches 29096 (first 7 days)

## Release announcement

{STEAM_CLAN_LOC_IMAGE}/45164767/40a0a47432b4e8c857d40152295f1551702c1012.png
Out of the sewers and into the streets, the rightful King of the Rats is here at last. Rodent-hating citizens of Manhattan won't be prepared to see his Scrap Grenade bouncing down Broadway, nor for his Swarm of Rats biting at their heels. By donning his Royal Pestments, the Rat King shakes off incoming damage, allowing him to bravely lead the charge into battle. His loyal subjects will feel awed and inspired when they see the great Banner of Rattania waving in the middle of combat, and those who oppose him will rue the day they ever thought they could overthrow the king. - "Oh the rats are taking over, baby!"
The Rat King is available to play now! Have a great weekend and keep those votes coming, as our next hero will be joining us on Tuesday at 2pm PDT. We'll see you then!

## Current meta thesis and map state

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
Sinclair: C (stable) — burst cast/steal
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

Deadman Danny, Solomon, Violet, Nurse Harrow, Baba

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
