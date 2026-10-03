# Task: per-hero analysis (all heroes)

Patch: City Never Sleeps (2026-09-29)

## Systems analysis

{
 "systems_changed": [
  {
   "system": "map/layout",
   "change_summary": "Full visual rework with lanes renamed (Broadway/Greenwich/York) and four new districts (Theater, Chinatown, Haunted Lot, Plaza) branching off the main lanes; the layout now dictates where picks and fights happen.",
   "driving_changes": [
    "Map: full visual rework; lanes renamed Blue Lane → Broadway, Green Lane → Greenwich, Yellow Lane → York",
    "Districts: 4 new districts branching off the main lanes — Theater, Chinatown, Haunted Lot, Plaza"
   ],
   "magnitude": "major",
   "effect_on_play": "New high-ground, roofs and hiding geometry change lane control and roaming routes; per peercontent the green-lane roof/tree above the bridge lets a hero hold lane permanently, so lane matchups are now map-conditional, not just kit-based."
  },
  {
   "system": "neutrals/jungle",
   "change_summary": "All old neutrals are replaced by Haunt creatures that hit harder, cluster and chase; the efficient jungle pattern becomes stacking camps and clearing them with AoE.",
   "driving_changes": [
    "Neutrals: all old neutrals replaced by new Haunt creatures with new behaviors (Specimen, Gutter Ghouls, Barrel Mimics, Past Dues, Stage Hands, Crabbage Pots, Festival Spirit, Shrooms, Underhands)",
    "peercontent: camps deal more damage, group together and follow you, so sustain and AoE clear define the early game"
   ],
   "magnitude": "major",
   "effect_on_play": "Sustain and AoE camp-clear rise (Yamato, Mina), squishy heroes get punished for casual jungling, and grouped chasing camps can be deliberately stacked for faster clears — a mechanical skill gap that replaces the old static-camp farm."
  },
  {
   "system": "economy/farm (Tough Crates)",
   "change_summary": "Tough Crates need a Heavy Melee to open and pay guaranteed souls (~58 each), and several lanes have 200-300-soul box routes, making box runs more soul-efficient than camp farming.",
   "driving_changes": [
    "Tough Crates: breakables that require a Heavy Melee to open and pay out extra souls, rewarding heavy-melee access",
    "peercontent: 58 souls per crate, guaranteed drops, 200-300-soul quick routes; the 2:30 wave's boxes become heavy crates worth >100 souls"
   ],
   "magnitude": "major",
   "effect_on_play": "Early income concentrates into crate routes from ~2:30, so farming efficiency and heavy-melee access decide the first ten minutes; heroes locked out of heavy melee (Calico's cat form) lose a farm lane they can't contest."
  },
  {
   "system": "objectives/economy (Sunken Plaza & Bell Tower)",
   "change_summary": "Two new soul hotspots anchor the map: Sunken Plaza (~400-500 souls in seconds at 5 min, exits to the secret shop, drains stamina/mutes sound) and Bell Tower (~280 souls at 5 min, three vaults, capture rings a map-wide bell).",
   "driving_changes": [
    "Sunken Plaza: sub-area beneath the Plaza district; descending drains your stamina and mutes outside sound; high risk, high reward",
    "Bell Tower: Chinatown objective at the top of the tower holding a concentrated soul hotspot; collecting it rings a bell heard across the whole map"
   ],
   "magnitude": "major",
   "effect_on_play": "Fights converge on Plaza at 5-8 min and Bell Tower after 8; teams must rotate to contest telegraphed soul hubs, and Plaza's secret-shop exit plus stamina drain make it a committed fight rather than a free grab."
  },
  {
   "system": "buff containers",
   "change_summary": "Buff Containers are reworked to grant permanent Spirit Resist, Bullet Resist, Ability Range and Move Speed instead of their old effect.",
   "driving_changes": [
    "Buff Containers: revamped golden statues now also grant Spirit Resist, Bullet Resist, Ability Range, and Move Speed as permanent bonuses"
   ],
   "magnitude": "moderate",
   "effect_on_play": "Adds objective-gated stats independent of items, quietly scaling whoever controls early containers; Ability Range in particular rewards caster/poke kits that leverage the stat."
  },
  {
   "system": "sustain & stealth (Healing Snacks, Steam Vents)",
   "change_summary": "Healing Snacks (10% max HP) sit just behind lanes, and Steam Vents grant invisibility plus small regen for silent rotations.",
   "driving_changes": [
    "Healing Snacks: hidden pickups around the map for quick healing",
    "Steam Vents: standing on one grants invisibility and a small regen, enabling silent team rotations"
   ],
   "magnitude": "moderate",
   "effect_on_play": "Laning sustain and re-engage potential improve without items, and stealth rotations become map-driven; reveal/detection kits (Drifter, whose sense sees stealth) gain value from the stealth-friendly layout."
  },
  {
   "system": "items/broker",
   "change_summary": "A temporary merchant (The Broker) spawns with a first shipment ~30 min in, then roughly every 15 min, trading high-tier items for Corrupted versions.",
   "driving_changes": [
    "The Broker: temporary merchant spawning in random locations... first shipment ~30 min into a match, then roughly every 15 min; trades high-tier items for Corrupted versions"
   ],
   "magnitude": "moderate",
   "effect_on_play": "Creates a mid-late power spike and build variance around 30 min, rewarding players who bank souls and know the Corrupted pool; the random location adds contest risk."
  },
  {
   "system": "parry vs objectives",
   "change_summary": "Successfully parrying an objective no longer resets your Parry cooldown.",
   "driving_changes": [
    "Parry: successfully parrying objectives no longer resets your Parry cooldown"
   ],
   "magnitude": "moderate",
   "effect_on_play": "Tower dives become punishable — parry the Guardian, then heavy-melee the diver while the tower wakes up; only sustained/dive-capable picks (Apollo, Mo & Krill) can still dive, so sieging shifts from routine to committed."
  },
  {
   "system": "combat input",
   "change_summary": "Ability and item use is now instant on button press instead of waiting for the next input window.",
   "driving_changes": [
    "Abilities and items: use is now instant on button press instead of waiting for the next input window"
   ],
   "magnitude": "moderate",
   "effect_on_play": "Raises the reaction ceiling — faster parries, dashes and spell combos — so high-APM execution and tight reaction windows are rewarded over pre-planned inputs."
  },
  {
   "system": "walkers",
   "change_summary": "Walkers no longer keep firing fireballs after dying.",
   "driving_changes": [
    "Walkers: no longer keep firing fireballs after dying"
   ],
   "magnitude": "minor",
   "effect_on_play": "Removes post-mortem chip damage, making sieges and dives around a dying Walker slightly safer — a small nudge toward aggression on structures."
  },
  {
   "system": "sinner's sacrifice",
   "change_summary": "The Sinner's Sacrifice bonus now has variable timings.",
   "driving_changes": [
    "Sinner's Sacrifice: the bonus now has variable timings"
   ],
   "magnitude": "minor",
   "effect_on_play": "Less predictable farm objective, forcing players to re-time their sacrifice route; exact upside is unclear from the notes."
  },
  {
   "system": "street brawl",
   "change_summary": "Street Brawl grants a corrupted item after the Round 5 item draft.",
   "driving_changes": [
    "Street Brawl: grants a corrupted item after the Round 5 item draft"
   ],
   "magnitude": "minor",
   "effect_on_play": "Alternate mode gains earlier corrupted-item access; no bearing on the standard match meta."
  }
 ],
 "tempo_shift": {
  "direction": "toward_tempo",
  "confidence": 0.5,
  "why": "Early soul income is concentrated into crate routes (from ~2:30) and contested hubs (Plaza 5-8 min, Bell Tower 8+), with no new comeback valve, so map control and efficient routing decide games before most scalers spike. The counterweight — peercontent's read that guaranteed box drops push toward farming and slower brawling — keeps this a modest, economy-driven tempo shift rather than a return to pure lane brawling."
 },
 "archetype_effects": [
  {
   "archetype": "tank/frontline",
   "direction": "up",
   "magnitude": "moderate",
   "why": "Harder-hitting, clumping Haunt camps reward sustain front lines (Krill up, Billy down per peercontent)."
  },
  {
   "archetype": "mobile assassin",
   "direction": "up",
   "magnitude": "moderate",
   "why": "New districts, extra hiding spots and Steam Vent invisibility open roam/pick routes (Paradox, Drifter, Doorman)."
  },
  {
   "archetype": "split pusher",
   "direction": "up",
   "magnitude": "moderate",
   "why": "More vaults spread around the map (Bell Tower alone has three) make objectives harder to defend against side pressure."
  },
  {
   "archetype": "spirit carry",
   "direction": "up",
   "magnitude": "minor",
   "why": "Buff Containers now grant permanent Ability Range and Spirit Resist independent of items."
  },
  {
   "archetype": "late scaler",
   "direction": "down",
   "magnitude": "moderate",
   "why": "Crate routes, early hubs and the intact no-comeback economy still close games early, though efficient farming partially offsets the loss."
  },
  {
   "archetype": "lane bully",
   "direction": "up",
   "magnitude": "minor",
   "why": "Lane-adjacent crate routes and Healing Snacks (10% max HP) reward early lane pressure and sustain."
  },
  {
   "archetype": "gun carry",
   "direction": "neutral",
   "magnitude": "minor",
   "why": "Instant item/ability use and bullet-resist containers help, but the top farm route (Tough Crates) needs heavy melee, not gun DPS."
  },
  {
   "archetype": "burst caster",
   "direction": "up",
   "magnitude": "minor",
   "why": "Instant-cast abilities plus Ability Range containers favor fast combo execution around the new contested hubs."
  },
  {
   "archetype": "initiator",
   "direction": "up",
   "magnitude": "minor",
   "why": "Telegraphed hub fights (Plaza, Bell Tower) and stealth rotations create structured pick windows."
  },
  {
   "archetype": "support/healer",
   "direction": "neutral",
   "magnitude": "minor",
   "why": "Healing Snacks and Steam Vent sustain ease lane pressure, but the value shifts toward roaming utility, not pure healing."
  }
 ],
 "intent_read": "Valve is converting the game from a lane-brawl deciding factor into a map-objective economy skill test: behavior-rich Haunt camps, guaranteed soul-dense crate routes and the Plaza/Bell Tower hubs make routing, timing and contest the primary expression, with the Broker and corrupted items probing build variance for the road to 1.0. The parry-cooldown, Walker-fireball and instant-cast changes show a parallel push to tighten combat feel and punish greedy tower dives."
}

## Item analysis

{
 "items": [
  {
   "item": "Corrupted items",
   "direction": "rework",
   "magnitude": "moderate",
   "summary": "This is not a slot anyone builds toward — it is a new late-game tier that only exists after The Broker spawns (~30 min, then ~every 15). Because the negative attributes and small stat rolls are match-wide random (identical for all players), the same Corrupted item can be a clean pickup in one match and a trap in the next, so its value is a runtime read, not something you plan a build around; my read is low-confidence (no KB entry).",
   "affected_heroes": [],
   "build_shift": "Adds a bank-souls incentive that competes with dumping souls into a sixth slot before 30 min, since the corrupted trade is the only way to convert a finished high-tier item into the tier's extra stats."
  }
 ],
 "notable_item_stories": [
  "The Broker's 30-min spike runs counter to this patch's early-close/tempo read: it gives late scalers a concrete reason to survive and hold souls, partially offsetting the no-comeback economy and the late-scaler burial flagged in the systems pass.",
  "Because corrupted rolls are symmetric (match-wide identical), the tier adds variance between matches, not between players inside a match, so it should not skew win rates toward whoever reaches The Broker first — only toward teams that can stall to 30 min."
 ]
}

## Direct hero changes in this patch (grouped by hero; heroes not listed had no direct changes)

Check out everything that's new at:
  - [neutral] Check out everything that's new at: https://www.playdeadlock.com/cityneversleeps
Corrupted items:
  - [neutral] Corrupted items: high-tier items exchanged at The Broker; each match rolls random negative attributes from a predefined set with small stat variability, identical for every player in that match
Rat King:
  - [rework] Nurse Harrow, Deadman Danny, Baba, Solomon, Rat King, Violet: six new heroes announced; released two per week on Tuesdays and Fridays starting Oct 2, order decided by community vote
Yamato:
  - [rework] Yamato: Flying Strike now creates paths against targets that are solid to the player (turrets, Shrines, objectives)
Graves:
  - [rework] Graves: can now destroy Venator's traps with her gun

## Knowledge base: current state of every hero (pre-patch)

Infernus:
  name: Infernus
  role: gun/spirit carry
  archetypes:
  - gun carry
  - spirit carry
  - mobile assassin
  - late scaler
  tier: B
  trend: stable
  why: 'Infernus holds a huge 35.3% pick rate on a 47.7% WR: a comfort staple, not
    a killer. Dashfernus (spirit dash) is his stronger, untouched line, while the
    09-16 Spiritual Overflow nerf stripped the capstone from his burn-gun build, widening
    the gap between his two identities in a meta that rewards mobility over late scaling.'
  core_items:
  - Extra Spirit
  - Improved Spirit
  - Spirit Lifesteal
  - Mystic Vulnerability
  - Healbane
  - Rapid Rounds
  - Swift Striker
  - Toxic Bullets
  - Superior Duration
  - Escalating Exposure
  - Spiritual Overflow
  - Titanic Magazine
  build_variants:
  - Dashfernus (spirit dash)
  - Burn gun carry
  enabled_by:
  - Toxic Bullets scaling buff (09-16)
  - Healbane into healer-heavy comps (77% buy)
  - "Spirit scaling \u2014 Escalating Exposure 54.0% WR leads (Spiritual Overflow\
    \ nerfed 09-16)"
  - 09-16 dash no longer breaking gun cycle time
  countered_by:
  - Decay
  - Healbane
  - Dispel Magic
  - Dynamo
  - Bebop
  - Vyper
  - Paradox
  - Yamato
  - Lash
  - tempo/snowball meta
  notes: "09-16 (indirect): Spiritual Overflow nerfed (40->30 spirit, 30->25% fire\
    \ rate) \u2014 burn gun build drops it for Toxic Bullets/Swift Striker; Dashfernus\
    \ untouched.\nCorrection accepted: not a pure gun hero \u2014 data agrees (spirit\
    \ items lead on both share and WR), so both builds kept; spirit build edges out\
    \ gun. Low confidence on matchups (samples 150-350 games) and on any post-patch\
    \ shift, since the 47.7%/35.3% snapshot is pre-09-16."
  builds:
  - name: Dashfernus (spirit dash)
    damage: spirit
    core_items:
    - Extra Spirit
    - Improved Spirit
    - Healbane
    - Spirit Lifesteal
    - Mystic Vulnerability
    - Rapid Recharge
    - Superior Duration
    - Escalating Exposure
    popularity: primary
    notes: 'Full-spirit mobility build: Flame Dash to kite and re-engage, burn + Mystic
      Vulnerability/Escalating Exposure for damage; posts the higher win rates of
      his two builds and is untouched by 09-16.'
  - name: Burn gun carry
    damage: gun
    core_items:
    - Extra Spirit
    - Improved Spirit
    - Rapid Rounds
    - Swift Striker
    - Extended Magazine
    - Titanic Magazine
    - Toxic Bullets
    popularity: secondary
    notes: "Gun build leaning on burn via Toxic Bullets; Spiritual Overflow was nerfed\
      \ 09-16 (spirit 40->30, fire rate 30->25%, slower buildup) so it is dropped\
      \ for Swift Striker/Titanic Magazine \u2014 still his weaker-performing item\
      \ set."
  matchups:
    beats:
    - Shiv
    - Pocket
    - Drifter
    - Seven
    - Mina
    loses_to:
    - Dynamo
    - Vyper
    - Bebop
    - Ivy
    - Paradox
  matchup_notes: 'He beats melee bruisers he can kite (Shiv 54%, Drifter 52%) and
    squishies his burn out-ranges (Pocket 54%, Seven 51%). He loses to displacement-plus-burst
    that negates his low-HP kite game: Dynamo 41% and Bebop 43% (initiations/hooks)
    and Vyper 42%, a straight gun duel his HP cap can''t win.'
  confidence: 0.6
  provisional: false
Seven:
  name: Seven
  role: spirit carry
  archetypes:
  - spirit carry
  - late scaler
  tier: B
  trend: falling
  why: "Farm-first spirit AoE carry \u2014 the item data (Mystic Vulnerability 91%,\
    \ Escalating Exposure 89%) says spirit, not the gun build the KB lists. A 51.2%\
    \ WR on a 25.5% PR is healthy and he actually wins the tempo S-tiers Lash and\
    \ Billy, but the 09-16 patch gutted comeback souls and early Rift generosity,\
    \ so the scaling farmer who falls behind no longer recovers. Strong in low elo\
    \ where teams don't invade; unremarkable at the very top."
  core_items:
  - Mystic Vulnerability
  - Escalating Exposure
  - Healbane
  - Spirit Lifesteal
  - Arcane Surge
  - Monster Rounds
  - Cultist Sacrifice
  build_variants:
  - Spirit AoE carry
  - Farm/tempo hybrid
  enabled_by:
  - Abrams
  - Billy
  - Dynamo
  - Mo & Krill (frontline that makes space)
  - fast jungle clear
  - Healbane vs sustain comps
  countered_by:
  - Calico (dive)
  - Yamato (mobile burst)
  - Holliday (mobile burst)
  - Bebop (Hook CC-lock)
  - tempo/invade meta
  last_changed_patch: Minor Update - 08-12-2026
  notes: '09-16 (indirect): Cultist Sacrifice bounty 180->170% trims his farm-banker
    opener.

    Changelog: 09-16 tempo patch (comeback souls cut, early Rift resist now 10%+1%/min,
    +3s respawn at 20m) hurts farm-first scalers.'
  builds:
  - name: Spirit AoE carry
    damage: spirit
    core_items:
    - Arcane Surge
    - Healbane
    - Mystic Vulnerability
    - Spirit Lifesteal
    - Escalating Exposure
    popularity: primary
    notes: Storm Cloud/Static Charge AoE with Escalating Exposure + Mystic Vulnerability
      stacking damage, Healbane + Spirit Lifesteal for sustain in extended fights.
  - name: Farm/tempo hybrid
    damage: hybrid
    core_items:
    - Monster Rounds
    - Extra Stamina
    - Cultist Sacrifice
    popularity: secondary
    notes: Early Monster Rounds and Cultist Sacrifice bankroll his fast jungle clear
      and soul lead; the 'best solo-queue farmer' identity, taken before the spirit
      core.
  matchups:
    beats:
    - Paradox
    - Lash
    - Vindicta
    - Billy
    - Drifter
    loses_to:
    - Calico
    - Abrams
    - Ivy
    - Bebop
    - Infernus
  matchup_notes: "Beats grouped/initiating S-tiers \u2014 Paradox and Lash (both 58%)\
    \ get punished by his AoE and out-ranged on engage, and Vindicta's 53% edge grows\
    \ as the patch grounds flyers. Loses to Calico (42%), who dives the immobile farmer\
    \ before his AoE is up, and to Abrams/Bebop, who either out-tank his burst or\
    \ Hook him out of Storm Cloud range."
  confidence: 0.52
  provisional: false
Vindicta:
  name: Vindicta
  role: poke/siege carry
  archetypes:
  - poke/siege
  - gun carry
  tier: A
  trend: stable
  why: "High-tempo poke/siege carry \u2014 the exact profile the 09-16 patch rewards:\
    \ super-scaling trimmed, respawns stretched to 38s at 20m, and real early Rift\
    \ fights mean lane pressure sticks. She is also the archetypal flyer, so the same\
    \ patch taxes her uptime (air-drag slows, Silver's Weighted Bola grounding). Holds\
    \ A rather than the S the tempo read implies: 37.8% PR keeps her everywhere but\
    \ 50.3% WR says she is not free wins."
  core_items:
  - High-Velocity Rounds
  - Opening Rounds
  - Extra Spirit
  - Extra Charge
  - Improved Spirit
  - Rapid Recharge
  - Long Range
  - Swift Striker
  - Counterspell
  - Sharpshooter
  - Burst Fire
  build_variants:
  - Gun poke
  - Spirit CDR / ult-poke
  enabled_by:
  - tempo economy (super-scaling trimmed)
  - increased 20m respawn timer
  - real early Rift fights (resist 10%+1%/min)
  - High-Velocity Rounds / Sharpshooter gun-core
  countered_by:
  - Silver (Weighted Bola grounds flyers)
  - global slows now hit air drag
  - Lash (mobile initiator)
  - dive/CC comps
  - Yamato (mobile burst assassin)
  last_changed_patch: Minor Update - 08-12-2026
  notes: "09-16 (indirect): global slows now bite air drag and Silver's Weighted Bola\
    \ grounds Flight \u2014 anti-flyer tax offsets her tempo gains, so she holds A\
    \ (two-sided mover).\nheresy's 09-17 ricochet/split-shot ult buff is unattributable;\
    \ the 09-16 notes give it to Venator \u2014 treat as uncertain.\nLast changed\
    \ Minor Update - 08-12-2026 (Stake T1 nerf)."
  builds:
  - name: Gun poke
    damage: gun
    core_items:
    - High-Velocity Rounds
    - Opening Rounds
    - Long Range
    - Swift Striker
    - Counterspell
    - Sharpshooter
    - Burst Fire
    popularity: primary
    notes: Range/fire-rate weapon core to out-trade from max range; online by ~4 min
      and scales into Sharpshooter/Burst Fire, with Counterspell as the mandatory
      anti-dive/anti-burst slot.
  - name: Spirit CDR / ult-poke
    damage: spirit
    core_items:
    - Extra Spirit
    - Extra Charge
    - Improved Spirit
    - Rapid Recharge
    popularity: secondary
    notes: Spirit/CDR path to spam Flight and Assassinate and amplify Crow Familiar;
      note Extra Charge (99%) and Rapid Recharge (90%) ride along in almost every
      game even on the gun build.
  matchups:
    beats:
    - Venator
    - Mirage
    - Victor
    - Bebop
    - Abrams
    loses_to:
    - Vyper
    - Lash
    - Celeste
    - Wraith
    - Ivy
    - Silver
  matchup_notes: "Out-ranges and out-snipes other gun carries who want to stand and\
    \ trade (Venator 61%, Mirage 55%) and punishes immobile fronts (Victor 55%, Bebop\
    \ 54%, Abrams 53%). Folds to mobile divers and burst that close the gap before\
    \ she can kite \u2014 Lash 46%, Vyper 45%, Celeste 46% \u2014 the classic low-HP\
    \ flyer weakness."
  confidence: 0.63
  provisional: false
Lady Geist:
  name: Lady Geist
  role: spirit bruiser
  archetypes:
  - tank/frontline
  - late scaler
  - spirit carry
  tier: A
  trend: rising
  why: 'Essence Bomb/Life Drain buffs land on a hero whose tank/regen core the tempo
    patch left untouched, and her spirit-caster rivals (Celeste, Pocket, Mina) are
    all falling, so she climbs the bruiser slot by attrition. The gain is capped:
    the comeback rework guts her classic 0-6-lane-then-AFK-farm pattern, and Radiant
    Regeneration (98% buy share) was trimmed, so she reads as a durable ult-bot rather
    than a true scaler.'
  core_items:
  - Extra Regen
  - Monster Rounds
  - Mystic Regeneration
  - Radiant Regeneration
  - Kinetic Dash
  - Berserker
  - Spirit Resilience
  build_variants:
  - Regen gun-bruiser
  - Spirit Soul-Exchange
  enabled_by:
  - regen gun-bruiser core (Extra Regen/Mystic Regeneration) untouched
  - Life Drain T3 spirit scaling buff
  - Essence Bomb T3 +4%
  - 'falling spirit-caster rivals: Celeste, Pocket, Mina'
  - Soul Exchange fight-winning ult
  - 'frontline partners: Abrams, Mo & Krill, Dynamo'
  countered_by:
  - 'anti-heal: Decay, Healbane'
  - Radiant Regeneration nerf (hits 98% of her games)
  - tempo meta + comeback rework vs farm-then-scale
  - Lash (S) dive/burst
  - Yamato (S) burst assassin
  - Silver (S) gun tank that out-damages and out-tanks her
  - silence/burst before Soul Exchange
  last_changed_patch: Minor Update - 09-16-2026
  notes: '09-16: Life Drain T3 spirit scaling 0.3->0.45 and Essence Bomb T3 26->30%
    buff her bomb/drain, but Radiant Regeneration 2->1.7 per-boon trims her 98%-buy
    regen core.

    Radiant Regeneration nerf plus the comeback rework gutting her 0-6-then-farm pattern
    are what cap this rise, so I weight it below the creators'' ''rising''.

    WR 46.6% / PR 14.4% is a 14-day pre-patch snapshot; creator reads are A but direction
    is split (vegas stable, heresy rising).'
  builds:
  - name: Regen gun-bruiser
    damage: hybrid
    core_items:
    - Extra Regen
    - Monster Rounds
    - Mystic Regeneration
    - Radiant Regeneration
    - Kinetic Dash
    - Berserker
    popularity: primary
    notes: "Buy regen first (Extra Regen 2.7m, Monster Rounds 3.1m) to survive a losing\
      \ lane, then Kinetic Dash + Berserker to frontline and gun-spam; Soul Exchange\
      \ is the finisher \u2014 the vegas '6000 HP fire-rate hero'."
  - name: Spirit Soul-Exchange
    damage: spirit
    core_items:
    - Mystic Regeneration
    - Radiant Regeneration
    - Mystic Burst
    - Bullet Resist Shredder
    - Spirit Resilience
    popularity: secondary
    notes: Caster-leaning variant leaning on the buffed bomb/drain and a Spirit Resilience/Healing
      Booster defensive layer; weaker lane, better burst and bigger ult finisher.
  matchups:
    beats: []
    loses_to:
    - Lash
    - Drifter
  matchup_notes: "The sample lists Lash (41%) and Drifter (45%) under both beats and\
    \ loses_to; both are sub-50%, so treat both as losses and beats as empty. Lash\
    \ (S-tier) throws/dives her before she scales, Drifter (A) wins the melee duel\
    \ on tempo, and she has no positive matchup sample \u2014 low confidence."
  confidence: 0.55
  provisional: false
Abrams:
  name: Abrams
  role: tank initiator
  archetypes:
  - tank/frontline
  - initiator
  tier: B
  trend: rising
  why: A tempo patch that rewards early frontline bruisers left his core melee/tank
    items untouched, and the dash/light-melee gun-cycle change lets him weave shots
    and punches in lane. Anti-heal stacking (Decay, Radiant Regeneration trims) still
    caps his Siphon sustain, so he settles as a healthy baseline rather than a dominant
    pick. 50.3% WR at a huge 35.3% PR says the lobby understands him exactly.
  core_items:
  - Close Quarters
  - Monster Rounds
  - Melee Lifesteal
  - Stalker
  - Melee Charge
  - Bullet Resist Shredder
  - Hunter's Aura
  - Extra Regen
  - Warp Stone
  - Duration Extender
  - Dispel Magic
  - Superior Duration
  - Phantom Strike
  - Spirit Resilience
  build_variants:
  - Melee brawler (gun)
  - CC/sustain tank (spirit)
  enabled_by:
  - gun-cycle change (dashes/light melee no longer break gun cycle)
  - Infernal Resilience T3 buff
  - Fortitude max-health regen 2->2.25% (09-16)
  - early-tempo/early-snowball meta
  - core tank items untouched
  - Rem (heal enabler)
  countered_by:
  - Decay / anti-heal stacking
  - kiting mobile gun carries (Vyper, Wraith)
  - spirit burst (Celeste)
  - Shiv (anti-tank bruiser)
  - Ivy (peel/slow)
  last_changed_patch: Minor Update - 09-16-2026
  notes: "Corrected vs prior entry: matchup data has him beating Venator 62% (197\
    \ games), so Venator is a target, not a counter; anti-heal belongs in countered_by\
    \ as an item/system threat (Decay), not a hero pair.\nBuilds are data-derived\
    \ (Close Quarters/Monster Rounds/Melee Charge >85% share) \u2014 one melee-gun\
    \ core plus a late spirit-CC tank layer; creator echo-shard claim is not in current\
    \ usage data.\nChangelog 09-16: Seismic Impact T3 Unstoppable 6s->5s; global dash/light-melee\
    \ no longer break gun cycle. Snapshot WR is mostly pre-patch, so trend magnitude\
    \ is low-confidence."
  builds:
  - name: Melee brawler (gun)
    damage: gun
    core_items:
    - Close Quarters
    - Monster Rounds
    - Melee Lifesteal
    - Stalker
    - Melee Charge
    - Bullet Resist Shredder
    - Hunter's Aura
    popularity: primary
    notes: 'The default at ~80-90% buy share: cheap Close Quarters/Monster Rounds
      spike the early melee trade, then Hunter''s Aura and Stalker (which gates his
      Shoulder Charge engage) carry it into mid.'
  - name: CC/sustain tank (spirit)
    damage: spirit
    core_items:
    - Extra Regen
    - Warp Stone
    - Duration Extender
    - Dispel Magic
    - Superior Duration
    - Phantom Strike
    - Spirit Resilience
    popularity: secondary
    notes: Late-game defensive layer (avg buy 17-26m) that extends Seismic Impact/Siphon
      Life with Superior Duration + Duration Extender and blinks him onto targets
      via Warp Stone/Phantom Strike; the answer to being kited and anti-healed.
  matchups:
    beats:
    - Venator
    - Yamato
    - Apollo
    - Mirage
    - Mina
    loses_to:
    - Ivy
    - Vyper
    - Celeste
    - Wraith
    - Paige
  matchup_notes: "He wins any trade he can force: Venator (62%), Yamato (58%) and\
    \ Apollo (56%) are squishier carries whose burst Infernal Resilience + Siphon\
    \ out-sustain once he closes \u2014 note this directly contradicts the prior entry's\
    \ claim that Venator counters him. He loses to disengage and spirit burst: Ivy\
    \ (41%) peels/slows his engage, while Vyper (45%), Wraith (45%) and Celeste (45%)\
    \ out-range or out-burst a static frontline."
  confidence: 0.7
  provisional: false
Wraith:
  name: Wraith
  role: gun carry
  archetypes:
  - gun carry
  - late scaler
  tier: B
  trend: falling
  why: 'Wraith''s spirit on-hit identity was heavily weakened by 09-16: Card Trick
    heal/scaling/resist/slow cuts plus the Mercurial Magnum nerf and Plated Armor''s
    on-hit fix (which now blanks Full Auto''s spirit damage) push her toward a pure-gun
    build. She keeps a high floor (~51% WR, near-50% PR) as a fire-rate M1/AoE-delete,
    but is outclassed in her slot by tempo carries (Silver, Venator, Haze) and punished
    by the dive the meta rewards.'
  core_items:
  - Monster Rounds
  - Quicksilver Reload
  - Rapid Rounds
  - Extra Spirit
  - Swift Striker
  - Surge of Power
  - Dispel Magic
  - Ricochet
  - Spirit Lifesteal
  build_variants:
  - Spirit on-hit
  - Sustain gun
  enabled_by:
  - Ricochet
  - Quicksilver Reload
  - Abrams
  - Mo & Krill
  countered_by:
  - Plated Armor
  - Yamato
  - Silver
  - Paige
  - Sinclair
  last_changed_patch: Minor Update - 09-16-2026
  notes: "09-16: Card Trick heal 75->60, heal scaling 0.75->0.5, resist shred -8->-7%\
    \ (T3 -5->-4%), T3 slow +20->+15%; Mercurial Magnum + Spiritual Overflow gutted\
    \ and Plated Armor now blanks Full Auto spirit damage \u2014 on-hit-spirit core\
    \ weakened, lean pure gun.\nCreator-cited Capacitor/Slowing Hex appear in none\
    \ of the top-15 item slots; usage says the real core was spirit on-hit (Quicksilver\
    \ Reload 100%, Mercurial Magnum 93%) \u2014 Magnum now weakened.\nBuild clustering\
    \ is medium-confidence: inferred from shares/buy_min, no ability text."
  builds:
  - name: Gun carry (pure gun)
    damage: gun
    core_items:
    - Monster Rounds
    - Quicksilver Reload
    - Rapid Rounds
    - Swift Striker
    - Surge of Power
    - Ricochet
    popularity: primary
    notes: 'Post-09-16 rebuild: the Mercurial Magnum / on-hit-spirit package is weakened
      (Magnum base 25->20% and scaling 0.49->0.38, Spiritual Overflow nerfed, Plated
      Armor now blanks Full Auto''s spirit damage), so stack fire rate and gun damage
      instead of spirit procs; Quicksilver Reload (100% share) is still the signature
      early buy and Ricochet still turns her into an AoE-delete.'
  - name: Sustain gun
    damage: gun
    core_items:
    - Rapid Rounds
    - Swift Striker
    - Dispel Magic
    - Spirit Lifesteal
    popularity: secondary
    notes: Fire-rate gun line with Dispel Magic (85%) and Spirit Lifesteal (53% item
      WR) to survive being focused; take it when you're the dive target, not when
      you're free-hitting.
  matchups:
    beats:
    - Grey Talon
    - McGinnis
    - Mirage
    - Graves
    - Apollo
    loses_to:
    - Paige
    - Sinclair
    - Celeste
    - Dynamo
    - Ivy
  matchup_notes: "Card Trick's homing spirit damage plus Full Auto's AoE delete squishy\
    \ poke/siege heroes who cannot dodge \u2014 Grey Talon (60%), McGinnis (56%),\
    \ Mirage (56%). She folds to CC-and-dive she can't out-range: Paige's lane pressure\
    \ (43%), Dynamo's initiation (46%), Sinclair's burst (46%)."
  confidence: 0.6
  provisional: false
McGinnis:
  name: McGinnis
  role: poke/siege controller
  archetypes:
  - poke/siege
  - tank/frontline
  tier: B
  trend: stable
  why: "McGinnis is a draft-dependent zone controller whose value is lane/siege tempo\
    \ rather than scaling, so the 09-16 tempo shift cuts both ways: early turret pressure\
    \ matters more, but the mobile-burst meta (Yamato, Holliday, Silver) jumps her\
    \ wall and deletes turrets. Data backs the 'above-average but not dominant' read\
    \ \u2014 51.7% WR at a healthy 17.7% PR \u2014 and her item spread shows a genuine\
    \ gun core, not the pure turret/support identity creators repeat. Held at B: near-uncounterable\
    \ into the right draft, near-useless into dive+ AoE."
  core_items:
  - Intensifying Magazine
  - Monster Rounds
  - Heroic Aura
  - Extra Charge
  - Mystic Vulnerability
  - Escalating Exposure
  - Rapid Recharge
  build_variants:
  - Gun turret
  - Spirit turret/ult
  - Zoning utility
  enabled_by:
  - frontline tanks (Abrams, Dynamo, Billy) who hold space for turret and Medicinal
    Specter setups
  - "tempo/objective meta \u2014 Guardian bounty +10% rewards her lane siege"
  - Mini Turret HP buffs (08-12) and Medicinal Specter resist
  countered_by:
  - mobile burst divers (Yamato, Holliday, Silver) that jump the wall and delete turrets
  - AoE spirit burst (Lady Geist, Celeste, Dynamo) that clears turret stacks
  - global -20% slow nerf, which weakens her wall/Suppressor zoning
  last_changed_patch: Minor Update - 08-12-2026
  notes: 'Item data (14d, mostly pre-09-16) shows a real gun core (Intensifying Magazine
    77%, Monster Rounds 62%) plus spirit-amp turret items; no single dominant build,
    so the old ''turret/AoE-support'' labels understate the gun.

    Matchup feed duplicated heroes in both Beats and Loses-to; resolved by direction
    (Lash/Drifter >50% = beats, Wraith <50% = loses).

    Changelog: 09-16 tempo patch (comeback gutted, slows -20%) hits her indirectly;
    no direct McGinnis change since 08-12.'
  builds:
  - name: Gun turret
    damage: gun
    core_items:
    - Monster Rounds
    - Intensifying Magazine
    - Heroic Aura
    popularity: primary
    notes: "Highest-share core (Intensifying Magazine 77%, Monster Rounds 62%) \u2014\
      \ ramp fire rate behind turret cover, Monster Rounds for lane farm, Heroic Aura\
      \ to buff team fights."
  - name: Spirit turret/ult
    damage: spirit
    core_items:
    - Extra Charge
    - Mystic Vulnerability
    - Escalating Exposure
    - Rapid Recharge
    popularity: secondary
    notes: Extra Charge+Rapid Recharge for turret uptime, Mystic Vulnerability+Escalating
      Exposure to amp turret and Heavy Barrage damage into mid-game fights.
  - name: Zoning utility
    damage: hybrid
    core_items:
    - Healbane
    - Enduring Speed
    - Extra Stamina
    - Enchanter's Emblem
    - Suppressor
    popularity: niche
    notes: Defensive/support fillers (39-47% each) that keep her alive and zoning;
      Suppressor applies her slow, Medicinal Specter covers extended fights.
  matchups:
    beats:
    - Lash
    - Drifter
    loses_to:
    - Wraith
  matchup_notes: "She beats melee divers who must walk into her zone \u2014 Lash 56%,\
    \ Drifter 52% \u2014 because Spectral Wall cuts their approach and turrets punish\
    \ the dive. She loses to Wraith (44%, i.e. Wraith wins 56%): a ranged gun carry\
    \ who out-ranges and bursts her before the wall matters. Small samples (150-230\
    \ games), so treat as directional."
  confidence: 0.55
  provisional: false
Paradox:
  name: Paradox
  role: pick/sniper initiator
  archetypes:
  - burst caster
  - initiator
  - poke/siege
  tier: B
  trend: falling
  why: 'Pick/sniper whose identity narrowed further by 09-16: the Kinetic Carbine
    min-damage quick-scope (25->10%, no longer T3-scaled) is gone, so only the max-range
    HVR/Sharpshooter path converts. A 47.5% WR on a 44% PR means the pick fantasy
    stays popular even as the stationary sniper folds to the tempo meta''s mobile
    divers (Yamato, Lash, Holliday).'
  core_items:
  - Restorative Shot
  - Headshot Booster
  - High-Velocity Rounds
  - Headhunter
  - Long Range
  - Sharpshooter
  - Express Shot
  - Slowing Hex
  - Mystic Burst
  - Tankbuster
  - Compress Cooldown
  build_variants:
  - Carbine sniper
  - Ability burst
  - Echo Shard bomb
  enabled_by:
  - Slowing Hex
  - Time Wall
  - Tankbuster
  - Dynamo
  - Mo & Krill
  countered_by:
  - Yamato
  - Lash
  - Holliday
  - cleanse/dispel
  - Veil Walker
  - range denial
  last_changed_patch: Minor Update - 09-16-2026
  notes: "Data disagrees with the old 'Echo Shard every game' read: Echo Shard and\
    \ Superior Cooldown miss the top-15 items; the real core is a gun/carbine sniper,\
    \ and Slowing Hex is 60%, not guaranteed.\nLow-confidence on the niche Echo Shard\
    \ line \u2014 usage suggests it is a personal build, not the meta path.\nChangelog\
    \ 09-16: Kinetic Carbine min-damage multiplier 25->10% and no longer scaled by\
    \ T3; Slowing Hex cooldown up."
  builds:
  - name: Carbine sniper
    damage: gun
    core_items:
    - Restorative Shot
    - Headshot Booster
    - High-Velocity Rounds
    - Headhunter
    - Long Range
    - Sharpshooter
    - Express Shot
    popularity: primary
    notes: Stack weapon range and headshot damage and farm picks off Kinetic Carbine
      at max range; Headhunter/Express Shot reward carbine crits.
  - name: Ability burst
    damage: spirit
    core_items:
    - Slowing Hex
    - Mystic Burst
    - Tankbuster
    - Compress Cooldown
    popularity: secondary
    notes: Pulse Grenade + carbine spirit burst, Compress Cooldown to cycle Time Wall/Swap,
      Tankbuster for %HP damage into tanks; Slowing Hex sets up picks and peels dives.
  - name: Echo Shard bomb
    damage: hybrid
    core_items:
    - Echo Shard
    popularity: niche
    notes: The old double-bomb/swap combo build; usage data no longer shows Echo Shard
      in the top 15, so treat this as a personal-choice line, not the mainstream path.
  matchups:
    beats:
    - Grey Talon
    - Venator
    - Infernus
    - Pocket
    - Apollo
    loses_to:
    - Seven
    - Yamato
    - Lash
    - Celeste
    - Holliday
  matchup_notes: "She out-ranges and pins immobile poke/gun carries \u2014 Grey Talon\
    \ (59%) and Venator (57%) cannot contest Kinetic Carbine/Time Wall range. She\
    \ folds to anything that closes distance or dumps burst on her small HP pool:\
    \ Yamato (43%), Lash (43%) and Holliday (43%) all dive her, and Celeste (43%)\
    \ out-trades her outright."
  confidence: 0.72
  provisional: false
Dynamo:
  name: Dynamo
  role: initiator/support
  archetypes:
  - initiator
  - support/healer
  tier: A
  trend: rising
  why: "Dynamo is a tempo initiator and the 09-16 patch made tempo the win condition\
    \ \u2014 a won lane plus one Singularity pick converts straight into kills and\
    \ objectives. His 52.1% WR at a 27% pick rate is backed by real usage, and his\
    \ item spine (Mystic Expansion, Extra Charge, Refresher) went untouched while\
    \ his only structural counters are matchups, not global nerfs. He isn't S because\
    \ a single interruptible channel is the whole payoff; durable frontline and Unstoppable\
    \ buyers blank it."
  core_items:
  - Extra Charge
  - Arcane Surge
  - Mystic Expansion
  - Compress Cooldown
  - Duration Extender
  - Warp Stone
  - Refresher
  - Superior Cooldown
  - Unstoppable
  - Debuff Reducer
  build_variants:
  - Spirit AoE initiator
  - Refresher double-ult
  enabled_by:
  - tempo conversion
  - AoE dispel (Quantum Entanglement)
  - Refresher
  - Singularity pickoff
  - Diviner's Kevlar +10% ultimate CDR (09-16)
  - core tank items untouched
  countered_by:
  - durable frontline (Billy, Mo & Krill, Abrams)
  - Unstoppable buyers
  - long-range CC/silence on the channel
  - anti-heal vs Rejuvenating Aurora
  - Paige lane pressure
  last_changed_patch: Minor Update - 07-28-2026
  notes: "09-16 (indirect): Diviner's Kevlar gained +10% ultimate CDR \u2014 now a\
    \ live buy for his Refresher/Singularity plan.\nNewest creator note (07-16) rates\
    \ him B, but the 09-16 tempo patch plus 52.1% WR / 27% PR supports A-rising; I\
    \ follow the data. Matchup samples are moderate (~180-320) and the WR snapshot\
    \ predates 09-16, so post-patch numbers could move.\nBuild read is spirit-spine\
    \ with a Refresher late spike; Headshot Booster (50%, 2.6 min) is just a starting\
    \ item, not a gun build."
  builds:
  - name: Spirit AoE initiator
    damage: spirit
    core_items:
    - Extra Charge
    - Arcane Surge
    - Mystic Expansion
    - Compress Cooldown
    - Duration Extender
    - Warp Stone
    popularity: primary
    notes: "Every-game spine: cheaper, larger and more frequent Singularity/Rejuvenating\
      \ Aurora, with Warp Stone to reposition into the ult or escape after it \u2014\
      \ all high-share (74-78%) and early buys."
  - name: Refresher double-ult
    damage: spirit
    core_items:
    - Refresher
    - Superior Cooldown
    - Unstoppable
    - Debuff Reducer
    popularity: secondary
    notes: "Late spike for a second Black Hole; self-Unstoppable/Debuff Reducer make\
      \ the channel uninterruptible \u2014 these are his highest-WR items (Refresher\
      \ 57.2%, Superior Cooldown 56.6%)."
  matchups:
    beats:
    - Infernus
    - Calico
    - Drifter
    - Lash
    - Bebop
    loses_to:
    - Billy
    - Mo & Krill
    - Warden
    - Abrams
    - Paige
  matchup_notes: "Quantum Entanglement's AoE dispel is why he beats Infernus (59%)\
    \ and DOT/dive heroes \u2014 one cast strips burn and setup, and Calico/Drifter/Lash/Bebop\
    \ fold to AoE CC when they commit on him. He loses to durable frontline (Billy\
    \ 42%, Mo & Krill 45%, Abrams 49%): they eat Singularity, can't be repositioned,\
    \ and outlast the cooldown, while Paige (51%) simply wins the lane in front of\
    \ him."
  confidence: 0.72
  provisional: false
Kelvin:
  name: Kelvin
  role: support/healer
  archetypes:
  - support/healer
  - late scaler
  tier: B
  trend: rising
  why: "Frozen Shelter's regen now scales with spirit power, so his cheap early sustain\
    \ items (Extra Regen, Healing Booster, Extra Charge) turn into real healing before\
    \ he maxes the dome \u2014 the tempo patch rewards that timing. But he is still\
    \ a late scaler at 47.8% WR / 17.7% PR, and the things that beat him (Healbane-stacking\
    \ anti-heal, mobile dive from Lash/Drifter) are all meta, which caps him at B."
  core_items:
  - Extra Regen
  - Extra Charge
  - Extra Spirit
  - Healing Booster
  - Healbane
  - Improved Spirit
  - Rapid Recharge
  - Mystic Expansion
  build_variants:
  - Spirit heal/support
  - Spirit scaling/expansion
  enabled_by:
  - Frozen Shelter spirit scaling
  - Extra Charge / Improved Spirit spirit stacking
  - tempo patch early heal relevance
  - healing-item nerfs (Radiant Regeneration 2->1.7, Restorative Locket trims) hurt
    rival sustain more than his Extra Regen/Healing Booster core
  - strong frontline allies he can heal (Abrams, Dynamo, Mo & Krill, Billy)
  countered_by:
  - anti-heal stacking (Healbane, Toxic Decay)
  - Lash
  - Drifter
  - silence and burst that kill through the dome
  - late-scaling compression (tempo meta)
  last_changed_patch: Minor Update - 09-16-2026
  notes: "KB core_items were wrong: usage shows a spirit-sustain line (Extra Regen/Extra\
    \ Charge/Healing Booster), not Radiant Regeneration/Healing Nova/Fortitude \u2014\
    \ corrected. Vegas (07-16) wanted a late->early power shift, but the 09-16 Frozen\
    \ Shelter spirit scaling is a late-value change heresy (09-17) called usable WITHOUT\
    \ maxing; I follow the newer read. High-Velocity Rounds (42%, 1.6 min) is lane\
    \ filler, not a build. Changelog: 09-16 \u2014 Frozen Shelter innate regen now\
    \ scales with spirit power."
  builds:
  - name: Spirit heal/support
    damage: spirit
    core_items:
    - Extra Regen
    - Extra Charge
    - Extra Spirit
    - Healing Booster
    - Healbane
    - Improved Spirit
    popularity: primary
    notes: Stack spirit power to scale Frozen Shelter regen and heal throughput; buys
      Healbane for self/team anti-heal. The default path on most Kelvin games (each
      item 73-81% buy rate).
  - name: Spirit scaling/expansion
    damage: spirit
    core_items:
    - Rapid Recharge
    - Mystic Expansion
    - Mystic Vulnerability
    - Escalating Exposure
    - Greater Expansion
    - Boundless Spirit
    popularity: secondary
    notes: Late luxury line bought past 16 min; Greater Expansion (55.9%) and Boundless
      Spirit (57.5%) have the best WRs but only ~50% buy rates, so treat as win-more
      rather than core.
  matchups:
    beats:
    - Bebop
    - Wraith
    loses_to:
    - Lash
    - Drifter
  matchup_notes: "Bebop (58%) and Wraith (51%) are his best: their spirit burst is\
    \ fully answered by dome + heal, so he simply out-sustains their damage windows.\
    \ Lash (45%) and Drifter (46%) are his worst \u2014 mobile melee initiators that\
    \ reach and burst him before the dome lands, and his low mobility can't disengage.\
    \ Paradox (50%) is a coin flip; a pick initiator can swap him out of position."
  confidence: 0.55
  provisional: false
Haze:
  name: Haze
  role: gun carry
  archetypes:
  - gun carry
  tier: B
  trend: rising
  why: 'Haze is a tempo gun carry: the Fixation buff (headshot stacks 2->3, higher
    T3 weapon scaling) lifts exactly the early-mid damage that wins lane, and 09-16
    gutted comeback souls so a won lane converts to a win. But her ceiling still sits
    on weak T4 gun items (Ricochet/Capacitor) and the meta''s mobile divers and lane
    bullies hunt her low-mobility frame, so a 49.8% WR caps her at B. Strong tempo
    pick, not a top one.'
  core_items:
  - Extra Spirit
  - Rapid Rounds
  - Active Reload
  - Swift Striker
  - Surge of Power
  - Tesla Bullets
  - Ricochet
  - Burst Fire
  - Capacitor
  build_variants:
  - Gun carry (Fixation)
  - Ricochet AoE / late pivot
  enabled_by:
  - Fixation buff (headshot stacks 2->3, higher T3 weapon scaling)
  - tempo meta (comeback souls gutted, lane win converts)
  - gun-cycle smoothing (dash/light melee no longer break gun cycle)
  - Ricochet farm
  countered_by:
  - Plated Armor (gun resist)
  - CC lockdown
  - mobile dive (Holliday, Calico, Yamato)
  - lane bullies (Paige, Apollo)
  - Celeste burst
  - weak T4 gun items (Ricochet/Capacitor)
  last_changed_patch: Minor Update - 09-16-2026
  notes: "09-16 (indirect): Plated Armor's on-hit fix now blanks Tesla Bullets spirit\
    \ damage, weakening her Ricochet/Tesla late pivot.\nRole reframed per reader:\
    \ farm-carry is meta-dependent, not her identity \u2014 historically a Smoke Bomb\
    \ roamer/ganker on isolated targets, and T4 weakness gates the late-scaler label.\n\
    Changelog: Minor Update - 09-16-2026 \u2014 Fixation headshot stacks 2->3, higher\
    \ T3 weapon scaling."
  builds:
  - name: Gun carry (Fixation)
    damage: gun
    core_items:
    - Extra Spirit
    - Rapid Rounds
    - Active Reload
    - Swift Striker
    - Surge of Power
    - Burst Fire
    popularity: primary
    notes: "Default build: cheap early attack speed/reload items (buy_min 3.6-8.3)\
      \ land Fixation headshots faster, then Surge of Power/Burst Fire convert a lane\
      \ lead into single-target kills \u2014 pick it from a winning or even lane."
  - name: Ricochet AoE / late pivot
    damage: gun
    core_items:
    - Tesla Bullets
    - Ricochet
    - Capacitor
    popularity: secondary
    notes: Late waveclear/clustered-fight pivot (buy_min 17-22, ~55% Ricochet share);
      it farms well but lives on the weak T4 gun items that stop her scaling, so it
      is a fallback when the game stretches, not a win condition.
  matchups:
    beats:
    - Lady Geist
    - Grey Talon
    - Silver
    - Paradox
    - Pocket
    loses_to:
    - Celeste
    - Ivy
    - Victor
    - Vyper
    - Paige
  matchup_notes: "She out-tempos immobile, kit-dependent heroes \u2014 Lady Geist\
    \ (57%) and Grey Talon (56%) cannot punish her lane before their tools scale,\
    \ and Silver (56%) is a slow gun tank she pokes out on Fixation. Her losses are\
    \ the meta's strong mobile/lane heroes: Celeste (42%) out-bursts her before stacks\
    \ build, Vyper (45%) and Ivy (43%) dive or out-sustain her low-mobility frame,\
    \ and Paige (46%) wins the lane outright."
  confidence: 0.68
  provisional: false
Holliday:
  name: Holliday
  role: mobile assassin
  archetypes:
  - mobile assassin
  - initiator
  tier: A
  trend: rising
  why: 'The tempo patch is shaped for her: with comeback souls gutted, lane winners
    snowball and the 20m respawn bump (35->38s) makes her Spirit Lasso picks worth
    more, while Crackshot T2 shred and a longer Lasso raise her pick value. Caveat:
    the Veil Walker rework stripped her disengage, so entries now commit harder, and
    her 48.6% WR is a pre-patch, pilot-conditional baseline.'
  core_items:
  - Extra Charge
  - Extra Spirit
  - Rapid Recharge
  - Improved Spirit
  - Mystic Burst
  - Superior Duration
  - Superior Cooldown
  - Sprint Boots
  - Extra Stamina
  - Recharging Rush
  - Veil Walker
  - Stamina Mastery
  - Tankbuster
  build_variants:
  - Charge-spirit pick
  - Stamina hybrid skirmisher
  enabled_by:
  - tempo meta (comeback gutted; lane wins snowball)
  - 20m respawn 35->38s (picks worth more)
  - Spirit Lasso buff + longer lasso
  - Crackshot T2 resist-shred
  - bounce-pad double-charge via Extra Charge/Rapid Recharge
  countered_by:
  - Veil Walker nerf (lost Sprint Boots + movespeed-on-break)
  - Bebop hook
  - Mo & Krill / Lash lockdown ultimates
  - Drifter melee bruiser pressure
  - Warden slowing gun pressure
  - slows now apply to air drag / slows-as-CC up
  last_changed_patch: Minor Update - 09-16-2026
  notes: "Changelog 09-16: Crackshot T2 resist-shred, longer Spirit Lasso, health/boon\
    \ 41->43; Veil Walker lost Sprint Boots and movespeed-on-break.\nDisagreement:\
    \ heresy (09-17) frames a 'gun hybrid' \u2014 ranked data shows a spirit charge/duration\
    \ build with no gun items beyond Recharging Rush, so treat 'gun hybrid' as a skirmish\
    \ label, not a build.\nLow confidence: 48.6% WR is a 14-day pre-patch baseline;\
    \ 21% PR with sub-50 WR reads as over-picked at low elo, so the tier is pilot-conditional."
  builds:
  - name: Charge-spirit pick
    damage: spirit
    core_items:
    - Extra Charge
    - Extra Spirit
    - Rapid Recharge
    - Improved Spirit
    - Mystic Burst
    - Superior Duration
    - Superior Cooldown
    popularity: primary
    notes: Buy the T1 charges (Extra Charge ~3.7m, Rapid Recharge) to double-dip bounce-pad/lasso
      casts, then spirit and duration to convert picks; the duration/cooldown finishers
      carry her highest win rates.
  - name: Stamina hybrid skirmisher
    damage: hybrid
    core_items:
    - Sprint Boots
    - Extra Stamina
    - Recharging Rush
    - Veil Walker
    - Stamina Mastery
    - Tankbuster
    popularity: secondary
    notes: "Stamina stack plus Recharging Rush to survive the skirmish and reposition;\
      \ Veil Walker is bought (57%) for the break despite losing its movespeed-on-break,\
      \ and this is the source of the 'gun hybrid' label \u2014 there is no real gun\
      \ build in the data."
  matchups:
    beats:
    - Haze
    - Paradox
    - Mina
    - Calico
    - Wraith
    loses_to:
    - Drifter
    - Bebop
    - Warden
    - Lash
    - Mo & Krill
  matchup_notes: 'She farms squishy, immobile poke/gun carries (Haze 57%, Wraith,
    Paradox) by closing with bounce-pad and lassoing them out of position. She loses
    to point-blank lockdown and anti-mobility: Drifter''s melee bruiser pressure (42%),
    Bebop''s hook, and Mo & Krill/Lash ults punish a low-HP assassin who has to commit
    on entry.'
  confidence: 0.6
  provisional: false
Bebop:
  name: Bebop
  role: hook initiator
  archetypes:
  - initiator
  - burst caster
  tier: B
  trend: falling
  why: 'Break-even hook initiator (~50% WR at a 54% PR) whose single-target lock-down
    still generates picks but converts less after the patch: his 77%-buy Veil Walker
    lost Sprint Boots and movespeed-on-break, and his slows were trimmed (Slowing
    Hex cd 27->29s, global slows -20%). He neither snowballs nor scales into a tempo
    meta full of tanks and sustain.'
  core_items:
  - Headshot Booster
  - Spirit Strike
  - Slowing Hex
  - Veil Walker
  - Headhunter
  - Spirit Snatch
  - Stalker
  - Fleetfoot
  - Siphon Bullets
  build_variants:
  - Hook combo
  - Gun
  - Beam/spirit burst
  enabled_by:
  - hook pick potential
  - Slowing Hex
  - Spirit Snatch
  - Veil Walker
  - tempo/early-snowball meta
  countered_by:
  - Billy
  - Kelvin
  - Dynamo
  - burst-proof tanks (Abrams, Mo & Krill)
  - cleanse/dispel items
  notes: "Builds: creators say 'gun is the build, don't build spirit,' but spirit-tagged\
    \ items (Spirit Strike 95%, Spirit Snatch 88%, Slowing Hex 81%) out-share the\
    \ gun items \u2014 the real default is hybrid; data wins. Siphon Bullets (27%\
    \ buy, 60.4% WR) is a small-sample late luxury, not a must-buy. 09-16 changelog:\
    \ slows -20% and Veil Walker loses Sprint Boots + movespeed-on-break; snapshot\
    \ WRs are pre-patch baseline."
  builds:
  - name: Hook combo
    damage: hybrid
    core_items:
    - Headshot Booster
    - Spirit Strike
    - Slowing Hex
    - Veil Walker
    - Headhunter
    - Spirit Snatch
    popularity: primary
    notes: 'The default Bebop: hook into Slowing Hex, then Sticky Bomb/uppercut burst
      while Veil Walker covers the dive; buys a gun T1 (Headshot Booster) in lane
      but the pick tools are spirit-tagged.'
  - name: Gun
    damage: gun
    core_items:
    - Headshot Booster
    - Stalker
    - Headhunter
    - Fleetfoot
    - Siphon Bullets
    popularity: secondary
    notes: Right-click DPS behind hook lockdown; creators call it the strongest build,
      but only Headshot Booster/Headhunter reach the share of the combo core, so the
      data ranks it second.
  - name: Beam/spirit burst
    damage: spirit
    core_items:
    - Spirit Strike
    - Slowing Hex
    - Spirit Snatch
    - Siphon Bullets
    popularity: niche
    notes: Hyper Beam-focused spirit burst; creators flag it as easily counterable,
      and it only scales late off Siphon Bullets (28.5 min), so few commit to it.
  matchups:
    beats:
    - Holliday
    - Infernus
    - Venator
    - Sinclair
    - Shiv
    loses_to:
    - Kelvin
    - Billy
    - Celeste
    - Dynamo
    - Vyper
  matchup_notes: 'Bebop''s hook punishes squishy carries that must stand their ground
    to deal damage (Infernus 57%, Venator 56%) and out-picks mobile assassins like
    Holliday (57%). He folds to anything that ignores a single-target combo: burst-proof
    tanks (Billy 43%), sustain that erases the burst (Kelvin 42%), and a better initiator
    dictating fights (Dynamo 44%).'
  confidence: 0.6
  provisional: false
Calico:
  name: Calico
  role: mobile assassin
  archetypes:
  - mobile assassin
  tier: A
  trend: rising
  why: Calico's value is winning the early lane and snowballing with off-map gold,
    so the 09-16 tempo patch that gutted comeback souls plays directly to her; the
    reader correction to re-rate her upward matches both that and the newest creator
    read (bottom of A). Her melee-spirit kit bursts squishy carries (Seven 58%, Pocket
    56%) before they can kite. She is still capped by tanks she cannot burst and gun
    carries who out-range her, which is why she lands at the bottom of A rather than
    higher.
  core_items:
  - Melee Lifesteal
  - Stalker
  - Spirit Strike
  - Cold Front
  - Spirit Snatch
  - Spirit Shredder Bullets
  - Mystic Vulnerability
  - Improved Spirit
  - Boundless Spirit
  - Arctic Blast
  build_variants:
  - Melee spirit assassin
  - Spirit-shred scaling
  enabled_by:
  - tempo/early-snowball meta
  - comeback-soul nerf (winning lane wins game)
  - off-map soul generation as a 3/4
  - Sprint Boots
  - mobile assassin archetype
  countered_by:
  - CC/lockdown (Dynamo, Mo & Krill)
  - tank frontline she cannot burst (Abrams, Victor)
  - long-range kiting gun carries (Vyper, Warden)
  - burst vs low HP (Yamato)
  last_changed_patch: Minor Update - 07-28-2026
  notes: "Data overrides old core_items: the Rapid Recharge/Echo Shard/Superior Stamina\
    \ set is gone \u2014 current builds are melee-spirit (Melee Lifesteal/Stalker/Spirit\
    \ Strike/Cold Front/Spirit Snatch at 98-99%). Reader correction followed: re-rated\
    \ upward to A on tempo; snapshot WR 50.2% is a 14-day pre-patch baseline, not\
    \ post-09-16. Secondary shred variant is the low-confidence part.\nLast patch:\
    \ Minor Update - 09-16-2026 (tempo/economy; Calico not directly touched)."
  builds:
  - name: Melee spirit assassin
    damage: spirit
    core_items:
    - Melee Lifesteal
    - Stalker
    - Spirit Strike
    - Cold Front
    - Spirit Snatch
    popularity: primary
    notes: "Default build \u2014 spirit damage delivered through her melee combo;\
      \ Melee Lifesteal (1.2m) + Spirit Strike let her win the trade, Cold Front and\
      \ Spirit Snatch (both 98%) turn ganks into kills."
  - name: Spirit-shred scaling
    damage: hybrid
    core_items:
    - Spirit Shredder Bullets
    - Mystic Vulnerability
    - Improved Spirit
    - Boundless Spirit
    - Arctic Blast
    popularity: secondary
    notes: Adds on-hit spirit shred plus late spirit scalers to amp the burst; Boundless
      Spirit games post 58.4% WR but land ~28m, too slow when the tempo meta is already
      deciding lanes.
  matchups:
    beats:
    - Seven
    - Pocket
    - Shiv
    - Infernus
    - Grey Talon
    loses_to:
    - Warden
    - Vyper
    - Dynamo
    - Victor
    - Abrams
  matchup_notes: "She beats squishy spirit/gun carries she can dive and burst before\
    \ they kite \u2014 Seven (58%), Pocket (56%), Grey Talon (54%), even against a\
    \ flyer the anti-air patch doesn't save. She loses to gun carries who out-range\
    \ her (Warden 42%, Vyper 42%) and to CC/tank frontline she cannot burst through\
    \ the health pool (Dynamo 43%, Victor 45%, Abrams 46%) \u2014 the same 'no kill\
    \ through HP' problem creators flagged in April."
  confidence: 0.62
  provisional: false
Grey Talon:
  name: Grey Talon
  role: poke/siege carry
  archetypes:
  - poke/siege
  - gun carry
  tier: C
  trend: falling
  why: "45.7% WR across 1,354 games at a 20% pick rate, and his best matchup is only\
    \ 49% \u2014 he isn't actually winning anything, he just isn't getting buried\
    \ either. The 09-16 patch hits both his identities at once: as a flyer he eats\
    \ the new air-drag slow and Silver's anti-air bola, and as a poke/siege carry\
    \ he needs the time the tempo meta refuses to give him. The newest creator read\
    \ (July, low-A/falling) predates the patch; the data now says C."
  core_items:
  - High-Velocity Rounds
  - Opening Rounds
  - Mystic Burst
  - Extra Charge
  - Long Range
  - Sharpshooter
  - Improved Spirit
  - Boundless Spirit
  - Tankbuster
  - Rapid Recharge
  build_variants:
  - "Hybrid owl (gun lane \u2192 spirit execute)"
  - Spirit charge/burst
  - Gun carry
  enabled_by:
  - Sharpshooter (weapon scaling)
  - Extra Charge + Rapid Recharge (Rain of Arrows/charge uptime)
  - long-range poke teammates (Vindicta, McGinnis)
  countered_by:
  - Lash
  - Wraith
  - Paradox
  - Haze
  - Silver (Weighted Bola anti-air)
  - air-drag slows (09-16)
  notes: "Item data overrides the stale core_items: Mystic Shot and Hollow Point don't\
    \ appear in 30-day usage; the real opener is High-Velocity Rounds + Opening Rounds\
    \ into spirit charge items.\nFlyer penalty applied per reader correction \u2014\
    \ 09-16 air-drag slow and Silver's Weighted Bola both count against him.\nLast\
    \ patch: Minor Update - 09-16-2026. No post-patch creator coverage; confidence\
    \ mid."
  builds:
  - name: "Hybrid owl (gun lane \u2192 spirit execute)"
    damage: hybrid
    core_items:
    - High-Velocity Rounds
    - Opening Rounds
    - Mystic Burst
    - Long Range
    - Extra Charge
    - Sharpshooter
    - Improved Spirit
    - Boundless Spirit
    popularity: primary
    notes: "Opens with cheap weapon items to win lane, then stacks spirit/charge to\
      \ scale Rain of Arrows and the Guided Owl execute \u2014 the standard line,\
      \ and what vegas described."
  - name: Spirit charge/burst
    damage: spirit
    core_items:
    - Mystic Burst
    - Extra Charge
    - Improved Spirit
    - Extra Spirit
    - Compress Cooldown
    - Rapid Recharge
    - Tankbuster
    - Boundless Spirit
    popularity: secondary
    notes: "Charge-reset spam (Extra Charge, Rapid Recharge, Compress Cooldown) maximizes\
      \ Rain of Arrows/snare uptime and burst \u2014 best into grouped or tanky teams,\
      \ worst when dove."
  - name: Gun carry
    damage: gun
    core_items:
    - High-Velocity Rounds
    - Opening Rounds
    - Long Range
    - Sharpshooter
    - Swift Striker
    popularity: niche
    notes: Pure weapon scaling with no charge investment; only correct if the lane
      is free and the enemy can't close distance, which is rare at high rank.
  matchups:
    beats:
    - Warden
    - Vindicta
    - Drifter
    - Calico
    loses_to:
    - Lash
    - Wraith
    - Paradox
    - Haze
  matchup_notes: "His 'wins' are even at best \u2014 49% into Warden and Vindicta\
    \ (the latter a fellow flyer also hurt by anti-air) \u2014 while he kites melee\
    \ bruisers like Drifter/Calico with pure range. He hard-loses to mobile initiators\
    \ and closers: Lash (36%) dashes past his poke and bursts him before the Owl lands,\
    \ and Wraith/Paradox/Haze shut the same gap. Bebop sits at 46% both ways \u2014\
    \ treated as even."
  confidence: 0.55
  provisional: false
Mo & Krill:
  name: Mo & Krill
  role: spirit tank initiator
  archetypes:
  - tank/frontline
  - initiator
  tier: B
  trend: rising
  why: 'A genuinely balanced spirit bruiser who fit the 09-16 tempo patch: winning
    lane and minute-one brawls is exactly what he wants, and his core tank/spirit
    items were left untouched. His ceiling is capped by the meta''s strong poke and
    flyer kits, which out-range him, and by S-tier frontline Billy, who out-brawls
    him.'
  core_items:
  - Mystic Burst
  - Quicksilver Reload
  - Extra Spirit
  - Torment Pulse
  - Cold Front
  - Trophy Collector
  - Sprint Boots
  - Healbane
  - Superior Duration
  - Superior Cooldown
  - Tankbuster
  build_variants:
  - Spirit bruiser
  - Extended-lockdown tank
  enabled_by:
  - early tempo/brawl meta (09-16)
  - core tank items untouched
  - Quicksilver Reload/Mystic Burst early spike
  - Burrow cooldown starts immediately (07-28)
  countered_by:
  - poke/siege kiting (Vindicta, Celeste)
  - anti-heal (his Scorn sustain)
  - anti-tank bruisers (Billy, Shiv)
  - long-range gun carries (Vyper)
  last_changed_patch: Minor Update - 07-28-2026
  notes: "Data over creators: they named Scourge/Decay/Fortitude, but high-rank usage\
    \ shows a spirit build (Mystic Burst 100%, Torment Pulse 91%) with no Scourge\
    \ in the top 15. \"Underplayed\" is stale \u2014 ~40% PR is high, he is picked,\
    \ just not a win-rate outlier. Changelog: last hero-relevant change Minor Update\
    \ - 07-28-2026; 09-16 was systems-only."
  builds:
  - name: Spirit bruiser
    damage: spirit
    core_items:
    - Mystic Burst
    - Quicksilver Reload
    - Extra Spirit
    - Torment Pulse
    - Cold Front
    - Trophy Collector
    - Sprint Boots
    - Healbane
    popularity: primary
    notes: 'Spirit-damage front line: Scorn/Burrow plus Torment Pulse and Cold Front
      brawl and zone, Trophy Collector/Sprint Boots buy early tempo, Healbane for
      self-sustain.'
  - name: Extended-lockdown tank
    damage: spirit
    core_items:
    - Superior Duration
    - Superior Cooldown
    - Tankbuster
    - Duration Extender
    - Compress Cooldown
    popularity: secondary
    notes: 'Late-game utility add-on: Duration/Cooldown keep Burrow and Combo up in
      fights, Tankbuster shreds enemy fronts; luxuries that only pay once the game
      is won on tempo.'
  matchups:
    beats:
    - Mirage
    - Yamato
    - Viscous
    - Mina
    - Haze
    loses_to:
    - Celeste
    - Vindicta
    - Billy
    - Paige
    - Vyper
  matchup_notes: "Combo (grab/suppress) plus Torment Pulse punishes short-range divers\
    \ who have to commit into him: Mirage (60%), Yamato (58%), Mina/Haze. He loses\
    \ to ranged kiting he can never close on \u2014 Celeste (46%) and Vindicta (47%)\
    \ \u2014 and to S-tier frontline Billy (47%), who simply out-brawls him, and lane-winning\
    \ Paige (47%)."
  confidence: 0.7
  provisional: false
Shiv:
  name: Shiv
  role: anti-tank spirit bruiser
  archetypes:
  - tank/frontline
  - mobile assassin
  tier: A
  trend: rising
  why: 'Shiv is the mobile frontline the tempo patch rewards: elite movement plus
    current-HP Serrated Knives make him a live answer to the big-HP tanks (Billy,
    Abrams, Mo & Krill) tempo keeps in fights, and he wins three common carries (Haze,
    Paradox, Wraith). His identity is now a regen-heavy spirit bruiser, and that core
    took a hit when Radiant Regeneration and Restorative Locket were trimmed, which
    is why a 48% WR undersells a rising pick. Burst and hook CC (Yamato, Bebop, Drifter)
    still kill him before his sustain ramps.'
  core_items:
  - Mystic Regeneration
  - Extra Regen
  - Extra Charge
  - Radiant Regeneration
  - Healbane
  - Mystic Vulnerability
  - Torment Pulse
  - Compress Cooldown
  - Escalating Exposure
  build_variants:
  - Spirit sustain bruiser
  - Cooldown spirit shred
  enabled_by:
  - current-HP Serrated Knives
  - alt-fire buff
  - tempo/snowball meta
  - Billy
  - Abrams
  - Mo & Krill
  countered_by:
  - Bebop (hook CC)
  - Yamato (burst)
  - Dynamo (CC)
  - Healbane / anti-heal
  last_changed_patch: Minor Update - 09-16-2026
  notes: "Prior core_items (Decay/Fortitude/Witchmail/Tankbuster) don't appear in\
    \ 30-day usage \u2014 rebuilt off the spirit/regen data. Data disagrees with vegas's\
    \ \"zero damage items\" claim: Mystic Vulnerability/Torment Pulse/Escalating Exposure\
    \ run 40-55%. 09-16: knives current-HP rework + alt-fire buff; his 97% core Radiant\
    \ Regeneration and Restorative Locket were trimmed."
  builds:
  - name: Spirit sustain bruiser
    damage: spirit
    core_items:
    - Mystic Regeneration
    - Extra Regen
    - Radiant Regeneration
    - Healbane
    - Extra Charge
    popularity: primary
    notes: Stack regen and cooldown so extended fights are unwinnable; Healbane doubles
      as anti-heal against other sustain fronts.
  - name: Cooldown spirit shred
    damage: spirit
    core_items:
    - Mystic Vulnerability
    - Torment Pulse
    - Compress Cooldown
    - Escalating Exposure
    - Superior Cooldown
    popularity: secondary
    notes: Late-game damage extension off the same regen core; Escalating Exposure
      (40% share) carries his best win rate at 59%.
  matchups:
    beats:
    - Billy
    - Mina
    - Haze
    loses_to:
    - Yamato
    - Drifter
    - Bebop
  matchup_notes: "Current-HP Serrated Knives make him a direct counter to S-tier tanks\
    \ \u2014 Billy (57%) and the big-HP frontlines tempo keeps alive are free food\
    \ for him, and he out-sustains carries like Haze (54%). He loses to burst and\
    \ CC that land before his regen ramps: Yamato's burst (42%), Drifter's melee duel\
    \ (44%), and Bebop's hook (46%)."
  confidence: 0.6
  provisional: false
Ivy:
  name: Ivy
  role: support/healer
  archetypes:
  - support/healer
  tier: A
  trend: falling
  why: Still the default support at 53.7% WR / 36.6% PR, and Stone Form's i-frame
    + long stun remains the best peel in the game; the 09-16 trims (radius 6->5.75m,
    T1 heal 7->6%) are cosmetic. But the tempo patch rewards winning lane and trims
    heal items (Radiant Regeneration, Restorative Locket), and Ivy's weak lane plus
    4-stamina reliance make her the most exposed A-tier support. Her item data is
    gun-first (Extended/Titanic/Tesla at 68-74% share), contradicting the stale heal-support
    item tagging.
  core_items:
  - Monster Rounds
  - Extended Magazine
  - Titanic Magazine
  - Tesla Bullets
  - Active Reload
  - Capacitor
  - Extra Regen
  - Healbane
  - Healing Booster
  build_variants:
  - Gun Ivy (stat-check carry-support)
  - Heal / anti-heal support
  - Spirit AoE / control utility
  enabled_by:
  - frontline tanks (Abrams, Billy, Victor)
  - gun item core (Titanic Magazine, Tesla Bullets)
  - team sustain / tether
  - Air Drop map control
  - dive partners (Drifter, Venator) she can heal-tether
  countered_by:
  - anti-heal (Healbane)
  - mobile burst (Vyper, Yamato, Lash, Holliday)
  - displacement (Dynamo, Mo & Krill)
  - silence
  - grounding / air-drag slow (hits Air Drop)
  last_changed_patch: Minor Update - 09-16-2026
  notes: "Corrected: Healing Tempo / Healing Nova don't appear in 30-day high-rank\
    \ usage \u2014 real build is gun-first (Extended/Titanic/Tesla 68-74%); creator\
    \ heal-support framing is stale.\nLow confidence on how the new air-drag slow\
    \ interacts with Air Drop while airborne.\n09-16: Stone Form radius 6->5.75m,\
    \ T1 heal 7->6% \u2014 creator-approved trim to an overloaded kit."
  builds:
  - name: Gun Ivy (stat-check carry-support)
    damage: gun
    core_items:
    - Monster Rounds
    - Extended Magazine
    - Titanic Magazine
    - Tesla Bullets
    - Active Reload
    - Capacitor
    popularity: primary
    notes: 'Default slot: early mag/regen into Titanic + Tesla for sustained gun DPS,
      Capacitor late for the stun/utility spike.'
  - name: Heal / anti-heal support
    damage: hybrid
    core_items:
    - Extra Regen
    - Healbane
    - Healing Booster
    popularity: secondary
    notes: "Sustain package layered on the gun core \u2014 Healing Booster to amplify\
      \ her tether heals, Healbane to cut enemy healing; run when the enemy team has\
      \ real sustain or burst you can't out-trade."
  - name: Spirit AoE / control utility
    damage: spirit
    core_items:
    - Mystic Expansion
    - Bullet Resist Shredder
    - Superior Duration
    - Greater Expansion
    popularity: niche
    notes: Late pickups that widen Stone Form/Entangling Thorns and stretch the tether/ult;
      buy only when fights are clumped and you already have the gun core.
  matchups:
    beats:
    - Mina
    - Haze
    - Abrams
    - Rem
    - Victor
    loses_to:
    - Vyper
    - Yamato
    - Dynamo
    - Mo & Krill
    - Viscous
  matchup_notes: "She beats committed, immobile damage and frontline \u2014 Haze (59%)\
    \ and Abrams (59%) cannot punish the Stone Form i-frame/stun, and Kudzu Connection\
    \ out-sustains their chip while she out-ranges tanks. She loses to mobile burst\
    \ and displacement: Vyper (44%) and Yamato (47%) kill through her low-HP heal\
    \ before tether matters, while Dynamo and Mo & Krill (48%) displace her out of\
    \ tether range and stun past the Form window."
  confidence: 0.62
  provisional: false
Warden:
  name: Warden
  role: gun carry
  archetypes:
  - gun carry
  - late scaler
  tier: C
  trend: falling
  why: 'The patch''s clearest casualty: bullet damage/boon, Alchemical Flask range/speed
    and Willpower T3 were all cut and both T4 gun finishers (Mercurial Magnum, Spiritual
    Overflow) were nerfed, so his late-scaler ceiling is gone in a meta that ends
    games early. The silence cage keeps him pickable, but he lands at C rather than
    balanced.'
  core_items:
  - High-Velocity Rounds
  - Opening Rounds
  - Extended Magazine
  - Swift Striker
  - Titanic Magazine
  - Quicksilver Reload
  - Fleetfoot
  - Shadow Weave
  - Spirit Lifesteal
  build_variants:
  - Gun carry
  - Cage bruiser
  enabled_by:
  - silence cage (Willpower)
  - fast farm
  - Venator / Mirage (out-stats fellow gun carries)
  - Pocket (cage shuts ability carry)
  countered_by:
  - tempo comps (Paige, Apollo, Yamato, Lash, Silver)
  - Ivy (sustain through his damage)
  - Mo & Krill / Victor (tank the cage, win the frontline)
  - Veil Walker nerf (lost Sprint Boots + movespeed-on-break)
  - weak T4 gun items (Mercurial Magnum / Spiritual Overflow class)
  last_changed_patch: Minor Update - 09-16-2026
  notes: "Item data shows one dominant gun build; the 'cage build' is a Willpower\
    \ skill choice, not a separate item path \u2014 creators' 'cage' tag overstates\
    \ it.\nMatchup WRs are the 14-day, mostly pre-09-16 snapshot \u2014 use as baseline\
    \ only.\n09-16: bullet dmg/boon, flask range/speed, Willpower T3 cut; Mercurial\
    \ Magnum + Spiritual Overflow nerfed, Veil Walker lost Sprint Boots/movespeed-on-break."
  builds:
  - name: Gun carry
    damage: gun
    core_items:
    - High-Velocity Rounds
    - Opening Rounds
    - Extended Magazine
    - Swift Striker
    - Titanic Magazine
    - Quicksilver Reload
    - Fleetfoot
    popularity: primary
    notes: Stack weapon tiers to farm fast and stat-check, then play for the mid-game
      spike before tempo closes; the old T4 capstone (Mercurial Magnum/Spiritual Overflow)
      was nerfed this patch, so the late slot must be re-routed to another line.
  - name: Cage bruiser
    damage: hybrid
    core_items:
    - Shadow Weave
    - Spirit Lifesteal
    - Enduring Speed
    - Sprint Boots
    popularity: secondary
    notes: "Shadow Weave \u2014 now carrying Sprint Boots, faster sprint and a 37s\
      \ cooldown \u2014 replaces the stripped Veil Walker as the invis-engage shell\
      \ for walking up to land the silence cage."
  matchups:
    beats:
    - Venator
    - Mirage
    - Apollo
    - Pocket
    - Graves
    loses_to:
    - Paige
    - Ivy
    - Seven
    - Victor
    - Mo & Krill
  matchup_notes: 'The 61% into Venator/Mirage is the class mirror: Warden out-stats
    and out-scales other gun carries, and cage shuts ability-reliant ones (Pocket
    59%). He loses to lane bullies (Paige 47%), sustain (Ivy 48%), and durable fronts
    (Mo & Krill/Victor 50%) that tank the cage and out-tempo him before he scales.'
  confidence: 0.6
  provisional: false
Yamato:
  name: Yamato
  role: mobile burst assassin
  archetypes:
  - mobile assassin
  - burst caster
  tier: A
  trend: rising
  why: Two straight buffs (Crimson Slash T3 heal spirit scaling +0.4, Flying Slash
    light-melee scaling 1.0->1.2) land on a tempo meta that rewards her point-click
    Spirit Snatch burst and Refresher-Unstoppable windows, and creators expect a real
    pick-rate climb. But 49.7% WR at 29.2% PR is a popularity-not-dominance profile,
    and the rising tank wave (Abrams, Mo & Krill, Billy) plus cheap anti-heal caps
    her ceiling. I take A over the tier list's S until a post-patch WR confirms the
    buffs converted.
  core_items:
  - Spirit Strike
  - Spirit Snatch
  - Mystic Shot
  - Restorative Shot
  - Healbane
  - Tankbuster
  - Mystic Reverb
  - Torment Pulse
  - Hunter's Aura
  build_variants:
  - on-hit spirit proc
  - late spirit burst
  - Refresher unstoppable
  enabled_by:
  - tempo meta
  - 09-16 buffs
  - Refresher
  - Spirit Snatch
  - Tankbuster + Mystic Reverb burst
  countered_by:
  - Counterspell
  - Dispel Magic
  - Abrams
  - Mo & Krill
  - Celeste
  - anti-heal (Healbane buyers)
  last_changed_patch: Minor Update - 09-16-2026
  notes: "Disagreement resolved (data > creators): Tankbuster is 39% share at a 25m\
    \ avg buy \u2014 a late luxury, not a core slot \u2014 and Refresher/Reverb fall\
    \ below the usage cutoff, so the Refresher build is creator-driven and niche.\n\
    Tier: list says S, but the last two creators who assigned one said A; 49.7% WR\
    \ at 29.2% PR is popularity, not dominance, and that WR is a pre-09-16 baseline.\n\
    09-16 changelog: Crimson Slash T3 heal spirit scaling +0.4, Flying Slash light-melee\
    \ scaling 1.0->1.2 (last_changed_patch: Minor Update - 09-16-2026)."
  builds:
  - name: on-hit spirit proc
    damage: hybrid
    core_items:
    - Spirit Strike
    - Restorative Shot
    - Mystic Shot
    - Healbane
    - Spirit Snatch
    popularity: primary
    notes: 'The 82-93%-share backbone: spirit procs (Spirit Strike, Spirit Snatch)
      layered with weapon on-hits (Mystic Shot, Restorative Shot) that fire off her
      melee/ability weaving, with Healbane to cut bruiser sustain.'
  - name: late spirit burst
    damage: spirit
    core_items:
    - Spirit Snatch
    - Tankbuster
    - Mystic Reverb
    - Torment Pulse
    - Hunter's Aura
    popularity: secondary
    notes: "Post-20m spike: Tankbuster+Reverb turns her point-click into a 1,000+\
      \ delete; Torment Pulse/Hunter's Aura add shred and AoE. Luxury tier \u2014\
      \ Tankbuster's 39% share lands at a 25m average buy."
  - name: Refresher unstoppable
    damage: spirit
    core_items:
    - Refresher
    - Mystic Reverb
    - Tankbuster
    popularity: niche
    notes: 'Creator-favoured win-more package: Refresher into Unstoppable gives a
      long unstoppable window for urn/Rift fights, but it sits under the usage cutoff,
      so treat it as situational, not standard.'
  matchups:
    beats:
    - Shiv
    - Paradox
    - Mina
    - Pocket
    - Wraith
    loses_to:
    - Celeste
    - Mo & Krill
    - Warden
    - Abrams
    - Haze
  matchup_notes: "She point-clicks squishy mobile and late-scaler carries before they\
    \ can answer (Shiv 58%, Paradox 57%, Mina 55%, Wraith 53% \u2014 Wraith is a falling\
    \ late scaler with no instant answer). She loses to sustain tanks that outlast\
    \ her burst (Mo & Krill 42%, Abrams 42%) and to Celeste/Warden (41-42%) who outrange\
    \ or CC her approach, while Counterspell and Dispel Magic delete the engage outright."
  confidence: 0.62
  provisional: false
Lash:
  name: Lash
  role: mobile initiator
  archetypes:
  - mobile assassin
  - initiator
  tier: S
  trend: rising
  why: "Highest pick rate in the game (62%) plus a tempo patch that gutted comeback\
    \ souls means his dive-and-stomp engage snowballs harder than almost anyone's,\
    \ and the 09-16 Ground Strike scaling buffs pushed him off gun items onto the\
    \ stomp build. The 51.8% WR undersells him \u2014 mass pick pressure drags it\
    \ and creators still rank him S \u2014 but Silver's Weighted Bola and the new\
    \ air-drag slows are the one thing that can check his aerial engage."
  core_items:
  - Mystic Burst
  - Extra Charge
  - Quicksilver Reload
  - Bullet Resist Shredder
  - Tankbuster
  - Headshot Booster
  - Recharging Rush
  - Headhunter
  - Sharpshooter
  build_variants:
  - Stomp spirit
  - Gun Lash
  - Bruiser flex
  enabled_by:
  - Ground Strike T3 scaling + per-meter damage buffs
  - Tempo meta (comeback souls gutted, early leads stick)
  - Mobility + CC kit (Grapple, Death Slam, Flog)
  - Extra Charge (near-mandatory spirit T1)
  countered_by:
  - Silver (Weighted Bola grounds/interrupts airborne engage)
  - Air-drag slows (new global slow-vs-air change)
  - 'Zone/anti-dive control: Dynamo, McGinnis, Seven'
  - Flog heal nerf + healing-item trims (Radiant Regeneration, Restorative Locket)
  last_changed_patch: Minor Update - 09-16-2026
  notes: "Data vs creator: 30-day usage still shows gun Lash (Headhunter 93%, Recharging\
    \ Rush 78%) because the window is mostly pre-09-16; the 09-17 creator says the\
    \ gun build is dead \u2014 treat stomp/spirit as current.\nLow-confidence: Vyper/McGinnis/Paige\
    \ samples are small (152-300 games) and pre-patch.\n09-16: Ground Strike T3 scaling\
    \ + per-meter damage up, gun falloff changed, Flog heal nerfed."
  builds:
  - name: Stomp spirit
    damage: spirit
    core_items:
    - Mystic Burst
    - Extra Charge
    - Quicksilver Reload
    - Bullet Resist Shredder
    - Tankbuster
    popularity: primary
    notes: "Ground-Strike spam; the 09-16 T3 scaling/per-meter buffs made this the\
      \ best Lash \u2014 dump the stomp on a grouped team, reset with Grapple."
  - name: Gun Lash
    damage: gun
    core_items:
    - Headshot Booster
    - Recharging Rush
    - Headhunter
    - Sharpshooter
    popularity: secondary
    notes: The old standard (Recharging Rush -> Headhunter); nerfed for him on 09-16
      and called 'killed' by the newest creator, yet still near half of 30-day games.
  - name: Bruiser flex
    damage: hybrid
    core_items:
    - Extra Stamina
    - Stamina Mastery
    - Siphon Bullets
    - Dispel Magic
    popularity: niche
    notes: Stamina plus late Siphon Bullets turn him into a sustained dive bruiser;
      a shared defensive layer over either damage path, not a standalone build.
  matchups:
    beats:
    - Grey Talon
    - Lady Geist
    - Paradox
    - Venator
    - Mirage
    loses_to:
    - Seven
    - Dynamo
    - McGinnis
    - Vyper
    - Paige
  matchup_notes: "Talon (64%) is his best lane \u2014 an immobile poke carry Lash\
    \ grapples onto and closes before he can kite, and Talon also eats the new air-drag/slow\
    \ change; Lady Geist (59%) is a slow bruiser with no answer to the dive. He loses\
    \ lane-to-late vs Seven (42%) and McGinnis (44%) \u2014 sustained AoE, turret/wall\
    \ zoning and stuns punish his engage \u2014 while Dynamo (44%) simply out-initiates\
    \ him in the 5v5."
  confidence: 0.6
  provisional: false
Viscous:
  name: Viscous
  role: tank/enabler
  archetypes:
  - tank/frontline
  - support/healer
  tier: B
  trend: falling
  why: Cube rescue still wins games, but the 09-16 trims to Cube cast range (26->20m),
    Puddle Punch cooldown (21->24s) and Splatter/alt-fire remove the tools that carried
    him, the tempo meta punishes a scaling enabler, and his cooldown-Cube shell lost
    Veil Walker's Sprint Boots and movespeed-on-break. Creators' S read is July/pre-nerf,
    so he settles at B until a post-patch WR shows otherwise.
  core_items:
  - High-Velocity Rounds
  - Mystic Burst
  - Mystic Shot
  - Express Shot
  - Spirit Strike
  - Mystic Expansion
  - Spirit Snatch
  - Tankbuster
  - Superior Cooldown
  build_variants:
  - Spirit-hybrid Splatter/Punch
  - Cooldown Cube support
  enabled_by:
  - Cube rescue
  - Goo Ball T3 spirit scaling
  - Rem
  - Paige
  - tank-frontline comps (Billy, Apollo)
  countered_by:
  - Lash
  - Mo & Krill
  - Drifter
  - Silver (Weighted Bola)
  - tempo snowball meta
  - global slows (slow-as-CC)
  last_changed_patch: Minor Update - 09-16-2026
  notes: "Disagreement: creators call Decay/Echo Shard core, but usage data has neither\
    \ in his top 15 \u2014 Mystic Burst (94%) and High-Velocity Rounds (81%) lead,\
    \ so the real shell is spirit-hybrid plus cooldown items, not Echo Shard resets.\n\
    Tier set to B: creators' S read is July (pre-nerf) and 51.5%/23.4% is a pre-09-16\
    \ snapshot, so the nerfs land him at B, not S.\n09-16: Cube cast range 26->20m,\
    \ Puddle Punch cooldown 21->24s, Splatter/alt-fire nerfs, Goo Ball T3 scaling\
    \ buff; cooldown-Cube shell also lost Veil Walker's Sprint Boots/movespeed-on-break."
  builds:
  - name: Spirit-hybrid Splatter/Punch
    damage: hybrid
    core_items:
    - High-Velocity Rounds
    - Mystic Burst
    - Mystic Shot
    - Express Shot
    - Spirit Strike
    - Mystic Expansion
    - Spirit Snatch
    - Tankbuster
    popularity: primary
    notes: Spirit-scaling Splatter and Puddle Punch poke carried by spirit-hybrid
      weapon items; his default lane-and-skirmish shell.
  - name: Cooldown Cube support
    damage: spirit
    core_items:
    - Sprint Boots
    - Veil Walker
    - Improved Spirit
    - Compress Cooldown
    - Superior Cooldown
    - Greater Expansion
    popularity: secondary
    notes: Cooldown-stacking enabler shell that maximizes Cube uptime and Goo Ball
      resets for coordinated rescue plays.
  matchups:
    beats:
    - Pocket
    - Haze
    - Calico
    - Abrams
    - Vindicta
    loses_to:
    - Mo & Krill
    - Lash
    - Drifter
    - Warden
    - Wraith
  matchup_notes: 'Beats Pocket/Haze/Calico because Cube nullifies their burst windows
    and his tanky frontline out-trades squishy carries; Abrams is a sustain-vs-sustain
    grind he edges. Loses to Mo & Krill (43%) and Lash (46%): Lash''s mobility and
    displacement punish a slow enabler, and Mo & Krill''s tank-sustain plus combo
    out-trades him; Drifter''s melee bruiser kit does the same.'
  confidence: 0.55
  provisional: false
Pocket:
  name: Pocket
  role: spirit carry
  archetypes:
  - spirit carry
  - burst caster
  - late scaler
  - mobile assassin
  tier: B
  trend: falling
  why: 'Late-scaling Affliction burst carry with no comeback safety net: the gutted
    comeback souls and the Cultist Sacrifice bounty trim (180->170%) removed the bail-out
    his slow farm-and-scale line needed, so he stays popular at 46.2% WR but rarely
    spikes before tempo ends the game. Beats squishy carries he can cloak onto; folds
    to anything that out-ranges or sticks to him.'
  core_items:
  - Mystic Burst
  - Monster Rounds
  - Cold Front
  - Cultist Sacrifice
  - Dispel Magic
  - Majestic Leap
  - Mystic Expansion
  - Tankbuster
  - Superior Cooldown
  - Spirit Burn
  - Superior Duration
  - Greater Expansion
  build_variants:
  - Affliction spirit burst
  - Cloak skirmish
  enabled_by:
  - Affliction (win-condition DoT)
  - sidelane wave clear
  - Majestic Leap (engage/escape)
  - mobility cloak
  countered_by:
  - Counterspell (removes Affliction)
  - tempo comps (close the game before he scales)
  - roots/lockdown (Warden, Viscous slows)
  - burst that out-ranges him (Celeste)
  last_changed_patch: Minor Update - 07-28-2026
  notes: 'Changelog: 09-16 - no direct line; tier stays B (falling) on the gutted
    comeback economy + Cultist Sacrifice trim. Low confidence on whether Flying Cloak
    counts as a flyer for the new air-drag slow rule.

    Creators'' ''7k on gun items'' claim is contradicted by 30-day usage: the only
    weapons with real share are farm items (Monster Rounds 92%, Cultist Sacrifice
    93%); there is no gun build. Data wins.

    Old entry''s core (Boundless Spirit, Echo Shard, Fortitude) shows zero current
    usage - replaced with the spirit stack the data actually shows.'
  builds:
  - name: Affliction spirit burst
    damage: spirit
    core_items:
    - Mystic Burst
    - Cold Front
    - Tankbuster
    - Superior Cooldown
    - Spirit Burn
    - Superior Duration
    - Greater Expansion
    popularity: primary
    notes: "The default ranked build \u2014 burst plus duration to maximize Affliction's\
      \ DoT and Barrage; buy order Mystic Burst/Cold Front early, Tankbuster\u2192\
      Spirit Burn\u2192Superior Duration late (99% Mystic Burst, 95% Tankbuster)."
  - name: Cloak skirmish
    damage: hybrid
    core_items:
    - Monster Rounds
    - Cultist Sacrifice
    - Majestic Leap
    - Mystic Expansion
    - Dispel Magic
    popularity: secondary
    notes: "Farm-speed plus mobility/survivability splash \u2014 Monster Rounds/Cultist\
      \ Sacrifice to clear camps, Majestic Leap and Dispel Magic to engage or bail\
      \ out; taken when the enemy comp punishes the all-in."
  matchups:
    beats:
    - Venator
    - Apollo
    - Mirage
    - Abrams
    - Wraith
    loses_to:
    - Celeste
    - Warden
    - Drifter
    - Haze
    - Viscous
  matchup_notes: 'Beats squishy carries he can cloak onto and burst before they scale
    (Venator 54%, Apollo 53%, Mirage 52%). Loses to anything that out-ranges or sticks
    to a low-HP caster: Celeste out-trades at range (39%), Warden''s root and gun
    pressure catch the dive (41%), and Drifter/Viscous stay glued to him (41%/44%).'
  confidence: 0.58
  provisional: false
Mirage:
  name: Mirage
  role: split-push hybrid carry
  archetypes:
  - gun carry
  - split pusher
  - late scaler
  tier: B
  trend: falling
  why: 'Slow teleport/split-push scaler that the 09-16 economy punishes hardest: comeback
    souls are gone and early Rift is now a real fight, so his map-play rarely comes
    online (46.3% WR, 39-45% into mobile bruisers). Kit intact - he is beaten by the
    meta, not the notes. Toxic Bullets'' scaling buff (0.005->0.006) gives his spirit-amp
    core a small offset.'
  core_items:
  - Mystic Regeneration
  - Healbane
  - Compress Cooldown
  - Dispel Magic
  - Mystic Vulnerability
  - Toxic Bullets
  - Escalating Exposure
  - Monster Rounds
  - Kinetic Dash
  - Titanic Magazine
  - Ricochet
  build_variants:
  - Spirit-amp hybrid
  - Attack-speed gun
  - Echo Shard tornado
  enabled_by:
  - spirit-amp item core (Mystic Vulnerability, Escalating Exposure)
  - Dust Devil knock-up / untargetable
  - split-push map pressure
  countered_by:
  - CC/pick comps (Mo & Krill silence, Lash)
  - mobile bruisers and assassins (Yamato, Silver, Holliday)
  - ranged gun carries (Warden)
  - tempo/snowball meta
  last_changed_patch: Minor Update - 07-28-2026
  notes: 'Changelog: 09-16 - no Mirage line; tier stays B; hurt by the gutted comeback/tempo
    system changes, partially offset by the Toxic Bullets scaling buff in his spirit-amp
    core.

    Data over creators: 30-day high-rank usage shows a spirit-amp hybrid core (Mystic
    Regen/Healbane/Mystic Vulnerability), not the Echo Shard-Scourge-Inhibitor build
    the summer creators cited - Echo Shard is ~0% now.

    Low confidence on whether the new air-drag slow interacts with Dust Devil''s lift.'
  builds:
  - name: Spirit-amp hybrid
    damage: hybrid
    core_items:
    - Mystic Regeneration
    - Healbane
    - Compress Cooldown
    - Dispel Magic
    - Mystic Vulnerability
    - Toxic Bullets
    - Escalating Exposure
    popularity: primary
    notes: 'The near-universal high-rank core (80-96% share): Mystic Regen + Healbane
      sustain into Compress Cooldown/Mystic Vulnerability spirit-amp on Fire Scarabs
      and Djinn''s Mark, with Toxic Bullets for gun; Escalating Exposure is the late
      capstone and correlates with his best item WR (50.8%).'
  - name: Attack-speed gun
    damage: gun
    core_items:
    - Monster Rounds
    - Kinetic Dash
    - Titanic Magazine
    - Ricochet
    popularity: secondary
    notes: "Gun/spread package at ~40-80% share (Ricochet 80%) for players leaning\
      \ on his gun and animation-cancel \u2014 late-scaling and therefore the half\
      \ of the kit the tempo meta punishes hardest."
  - name: Echo Shard tornado
    damage: spirit
    core_items:
    - Echo Shard
    - Scourge
    popularity: niche
    notes: The summer-2026 S-tier double-tornado build; 30-day high-rank usage shows
      it near-zero, so treat it as historical rather than a live option.
  matchups:
    beats:
    - Calico
    - Infernus
    - Paradox
    - Bebop
    - Haze
    loses_to:
    - Warden
    - Mo & Krill
    - Lash
    - Wraith
    - Abrams
  matchup_notes: "He farms immobile carries and squishy divers \u2014 53% into Infernus\
    \ and Calico \u2014 because Djinn's Mark plus Fire Scarab spirit-amp bursts low-HP\
    \ targets while Dust Devil's knock-up and untargetability blunt a dive. He folds\
    \ to CC-frontline and ranged gun pressure: 39% vs Warden (poke he cannot close),\
    \ 40% vs Mo & Krill (silence/combo locks a slow caster), 44% vs Lash (S-tier dive\
    \ displaces him off split-push)."
  confidence: 0.6
  provisional: false
Vyper:
  name: Vyper
  role: gun carry
  archetypes:
  - gun carry
  tier: B
  trend: falling
  why: 'Pre-patch elite numbers (54.6% WR / 26.9% PR) undercut by the 09-16 items:
    Mercurial Magnum''s base/scaling gut (25->20%, 0.49->0.38) plus Plated Armor''s
    on-hit fix weaken her 93%-share spirit-amp splice, pushing her toward a lower-ceiling
    pure-gun carry (the Slither/Bola nerfs are cosmetic). Still farms CC-light comps,
    still lifted out by hard-CC initiation (Dynamo, Mo & Krill).'
  core_items:
  - Close Quarters
  - Rapid Rounds
  - Split Shot
  - Burst Fire
  - Quicksilver Reload
  build_variants:
  - Gun build
  - Spirit-amp
  - Survive-the-CC
  enabled_by:
  - no-CC lobbies
  - gun-cycle/reload smoothing (09-16)
  - Paige
  countered_by:
  - CC/knockup comps
  - Lash
  - Billy
  - Yamato
  - Apollo
  - Dynamo
  - Mo & Krill
  - The Doorman
  - Plated Armor buyers (hard-counter the spirit-on-hit splice)
  last_changed_patch: Minor Update - 09-16-2026
  notes: 'Changelog: 09-16 - direct Slither T3 barrier 5->4s / Petrifying Bola cd
    105->115s are cosmetic; the real hit is indirect (Mercurial Magnum gut + Plated
    Armor on-hit fix), tier A->B, build pivots to pure gun.

    54.6% WR / 26.9% PR is a pre-09-16 baseline (14-day snapshot, mostly pre-patch).

    Low confidence: whether the Mercurial spirit line was a true second build or a
    mandatory splice - less relevant now that it is weakened.'
  builds:
  - name: Gun build
    damage: gun
    core_items:
    - Close Quarters
    - Rapid Rounds
    - Split Shot
    - Burst Fire
    popularity: primary
    notes: 'Now the main carry path: with Mercurial Magnum gutted (base 25->20%, scaling
      0.49->0.38) and Plated Armor blocking her spirit on-hit, the old near-universal
      (79-93%) spirit splice is weakened. Swift Striker (58%) and Tesla Bullets (52%)
      stay flex adds for close-range/AoE, though Tesla''s damage is now blocked by
      Plated Armor too.'
  - name: Survive-the-CC
    damage: hybrid
    core_items:
    - Grit
    - Spirit Shielding
    - Stamina Mastery
    - Unstoppable
    - Debuff Reducer
    popularity: niche
    notes: Defensive overlay (47-71% share) into knockup/CC comps - Unstoppable +
      Debuff Reducer keep the gun online vs Dynamo and Mo & Krill; more load-bearing
      now that her spirit-amp damage is gone.
  matchups:
    beats:
    - Mina
    - Calico
    - Infernus
    - Haze
    - Ivy
    loses_to:
    - Dynamo
    - Warden
    - Billy
    - Mo & Krill
    - Wraith
  matchup_notes: 'Data beats CC-light squishies - Mina (60%), Calico (58%), Infernus
    (58%) can''t trade into her gun and have no hard interrupt to stop the dive. The
    genuine losing lanes are initiation/CC: Dynamo (46%) and Mo & Krill lift/combo
    her out of the fight and Warden''s (48%) cage/trap punishes the dive. Note the
    creator-flagged counters (Billy 50%, Silver/Venator) do NOT show in data - so
    treat ''she loses to CC'' as a comp-level problem, not a specific-hero counter.'
  confidence: 0.6
  provisional: false
Sinclair:
  name: Sinclair
  role: burst cast/steal
  archetypes:
  - burst caster
  - mobile assassin
  tier: C
  trend: stable
  why: Kit-steal coin-flip with no draft to force a favourable matchup (48.3% WR).
    The tempo patch strengthens the gap-closing divers that already beat him (Lash,
    Yamato, Holliday, Drifter) while his two winning lanes (Wraith, Paradox) are falling
    archetypes getting rarer, and no item change touches his duration/cooldown spirit
    build - net flat-to-slightly-down.
  core_items:
  - Greater Expansion
  - Superior Duration
  - Mystic Expansion
  - Duration Extender
  - Rapid Recharge
  - Extra Charge
  - High-Velocity Rounds
  - Opening Rounds
  - Monster Rounds
  build_variants:
  - Spirit Duration
  - Lane Gun-Hybrid
  enabled_by:
  - kit stealing
  - parry/bolt utility
  - urn value
  - strong enemy S-tier kits to steal (Yamato, Lash, Apollo)
  countered_by:
  - no draft (cannot force a favourable matchup)
  - mobile divers and bruisers (Lash, Yamato, Holliday, Calico, Drifter)
  - Bebop hook
  - low base survivability
  notes: 'Changelog: 09-16 - no Sinclair line; divers that beat him gained from the
    tempo push, his winning matchups (Wraith, Paradox) shrink, and no spirit/duration
    item moved. Net flat.

    Data disagrees with creators: no Echo Shard in the top-15 buys (30d, high rank);
    the build is duration/cooldown spirit, so the 07-16 ''Echo Shard bunny'' claim
    is dated.

    Low confidence: without drafting his tier is effectively an RNG function, and
    the 48.3% WR is a 14-day near-pre-patch snapshot.'
  builds:
  - name: Spirit Duration
    damage: spirit
    core_items:
    - Mystic Expansion
    - Rapid Recharge
    - Extra Charge
    - Duration Extender
    - Superior Duration
    - Greater Expansion
    popularity: primary
    notes: Stacks ability/Hex duration and cooldown (Superior Duration + Greater Expansion
      ~80% share) to keep Rabbit Hex and stolen-kit CC on target; the actual zero-variance
      path, not Echo Shard.
  - name: Lane Gun-Hybrid
    damage: gun
    core_items:
    - High-Velocity Rounds
    - Monster Rounds
    - Opening Rounds
    popularity: secondary
    notes: Near-universal early weapon package (buy_min 1.5-4.3) for lane pressure
      and gun-cycle smoothing before pivoting to spirit; ~79% open with HVR/Opening
      Rounds.
  matchups:
    beats:
    - Wraith
    - Paradox
    loses_to:
    - Drifter
    - Bebop
    - Calico
    - Lash
  matchup_notes: "His only real wins are Wraith (54%) and Paradox (51%) \u2014 falling\
    \ squishy carries he can burst before they scale. He loses to Drifter (43%), Bebop\
    \ (44%) and rising divers Lash/Calico (47%): gap-closers, hooks and dive punish\
    \ his low HP and his inability to pick a favourable setup without draft."
  confidence: 0.42
  provisional: false
Mina:
  name: Mina
  role: mobile spirit assassin
  archetypes:
  - mobile assassin
  - burst caster
  tier: C
  trend: falling
  why: 'Overloaded mobile burst assassin who no longer converts (47.3% WR on 39.9%
    PR): the tempo/tank frontline (Billy, Mo & Krill) eats her single-target rotation,
    Yamato has taken over her mobile-burst niche, and the Tankbuster trim (current-health
    bonus 8->7.5%) weakens her last anti-tank answer. Damage is missing - a rework
    problem, not a numbers problem.'
  core_items:
  - Extra Spirit
  - Mystic Burst
  - Quicksilver Reload
  - Mystic Expansion
  - Improved Spirit
  - Extra Stamina
  - Dispel Magic
  - Stamina Mastery
  - Tankbuster
  - Boundless Spirit
  - Spirit Shredder Bullets
  - Spirit Burn
  build_variants:
  - Spirit burst
  - Gun-weave shred
  enabled_by:
  - tempo/snowball meta (early mobile kills)
  - mobility + burst damage kit
  - spirit burst item curve (Mystic Burst, Boundless Spirit)
  - ult silence
  countered_by:
  - CC/lockdown (Mo & Krill, Billy, Victor)
  - sustain/healing (Ivy)
  - tank/bruiser frontline that survives her burst
  - Yamato (owns the mobile-assassin niche)
  last_changed_patch: Minor Update - 07-28-2026
  notes: 'Changelog: 09-16 - no direct line; Tankbuster 8->7.5% shaves her anti-tank
    finisher and the tempo/tank meta punishes her burst. Held at C.

    Data shows essentially one spirit build (Extra Spirit/Mystic Burst/Quicksilver
    Reload all ~100%) - ''build diversity'' is a myth; only late anti-tank items diverge.
    Vegas (07-16): C falling, ''needs a rework not a buff.''

    Unchanged by Minor Update 09-16-2026; last direct touch 07-28-2026.'
  builds:
  - name: Spirit burst
    damage: spirit
    core_items:
    - Extra Spirit
    - Mystic Burst
    - Quicksilver Reload
    - Mystic Expansion
    - Improved Spirit
    - Extra Stamina
    - Dispel Magic
    - Stamina Mastery
    - Tankbuster
    - Boundless Spirit
    popularity: primary
    notes: "Spirit-power burst with a near-universal stamina/dispel backbone (all\
      \ ~96-100% share) \u2014 dive a squishy carry and delete them before they react,\
      \ using Quicksilver Reload to cycle abilities through reloads and Dispel Magic\
      \ to clear the CC that otherwise ends her."
  - name: Gun-weave shred
    damage: hybrid
    core_items:
    - Quicksilver Reload
    - Spirit Shredder Bullets
    - Spirit Burn
    popularity: secondary
    notes: Adds spirit-shred and %HP burn so gun autos keep damage up between cooldowns;
      the minority path (~66% share) players take when the enemy stacks tank, though
      it still loses the tank matchup.
  matchups:
    beats:
    - Mirage
    - Pocket
    - Haze
    - Venator
    - Vindicta
    loses_to:
    - Ivy
    - Vyper
    - Billy
    - Mo & Krill
    - Victor
  matchup_notes: "She beats the squishy carries she can dive and burst \u2014 Mirage,\
    \ Pocket, Haze (52-53%) \u2014 where her mobility converts a kill before they\
    \ can react. She loses hard to tanks and bruisers with CC/sustain (Billy 43%,\
    \ Mo & Krill 43%, Victor 44%) and to Ivy (40%), who out-heals her burst. Single-target\
    \ burst into heroes that survive the first rotation is the whole story."
  confidence: 0.7
  provisional: false
Drifter:
  name: Drifter
  role: melee bruiser
  archetypes:
  - mobile assassin
  - tank/frontline
  tier: A
  trend: stable
  why: 'Blind-pickable melee bruiser on a spirit-melee core (Melee Lifesteal, Stalker,
    Spirit Strike) with built-in anti-heal, and his 57.8% pick rate is the field''s
    highest. The 51.4% WR is a floor, not a ceiling: the tempo patch suits early bruisers
    and his build spikes before 7m, but rising Dynamo/Mo & Krill/Apollo pressure his
    losing matchups while he still lacks hard CC and closing mobility.'
  core_items:
  - Melee Lifesteal
  - Stalker
  - Spirit Strike
  - Mystic Burst
  - Spirit Snatch
  - Veil Walker
  - Healbane
  - Trophy Collector
  - Tankbuster
  build_variants:
  - Spirit melee bruiser
  - Anti-heal bruiser
  enabled_by:
  - blind-pickable
  - built-in anti-heal
  - tempo/early-snowball meta
  - Stalker (weapon T2)
  countered_by:
  - Dynamo
  - Mo & Krill
  - Apollo
  - Vyper
  - anti-heal stacking
  - CC/silence
  notes: "Dropped KB core_items Decay/Toxic Bullets/Fortitude \u2014 none show in\
    \ current 30-day usage; the 'Toxic Bullets bot' framing is a 2026-04 artifact\
    \ (data over creator). Celeste falling softens one losing matchup, but Dynamo/Mo\
    \ & Krill/Apollo rising worsen others \u2014 net stable. 09-16 Minor Update: no\
    \ direct Drifter change; gutted comeback souls and ramped rift resist suit his\
    \ early-bruiser floor."
  builds:
  - name: Spirit melee bruiser
    damage: spirit
    core_items:
    - Melee Lifesteal
    - Stalker
    - Spirit Strike
    - Mystic Burst
    - Spirit Snatch
    popularity: primary
    notes: Spirit-proc melee core; earliest spikes (Melee Lifesteal 1.5m, Stalker
      5.3m) win lane duels and dive squishies.
  - name: Anti-heal bruiser
    damage: hybrid
    core_items:
    - Veil Walker
    - Healbane
    - Trophy Collector
    - Tankbuster
    - Superior Duration
    popularity: secondary
    notes: "Mid-game survivability, anti-heal and extended ult duration \u2014 the\
      \ pick into healing comps and tanky fronts."
  matchups:
    beats:
    - Pocket
    - Holliday
    - Sinclair
    - Venator
    - Shiv
    loses_to:
    - Dynamo
    - Vyper
    - Celeste
    - Mo & Krill
    - Apollo
  matchup_notes: "Beats squishy burst/carry targets he can close and delete \u2014\
    \ Pocket, Venator, Holliday, Sinclair (57-59%). Loses the front-line/CC war to\
    \ Dynamo and Mo & Krill (44-48%), who out-sustain his dive and lock him down,\
    \ and to rising lane bullies Apollo and Vyper who never let him start."
  confidence: 0.72
  provisional: false
Venator:
  name: Venator
  role: gun carry
  archetypes:
  - gun carry
  - tank/frontline
  tier: A
  trend: rising
  why: Hugely popular default gun carry (28.7% PR) at 45.7% WR - not a free win. The
    09-16 Ira Domini buff (now chains Ricochet/Split Shot into 3 bolts) raises his
    late ceiling and slots him ahead of Haze, but hard-CC frontlines (Abrams, Lash)
    and a tempo meta that ends before his tank items cap him under S. The Weakening
    Headshot -13->-12% trim slightly widens his cheap-shred gap to buffed Hollow Point.
  core_items:
  - Restorative Shot
  - Close Quarters
  - Monster Rounds
  - Weakening Headshot
  - Battle Vest
  - Bullet Lifesteal
  - Fleetfoot
  - Berserker
  - Extra Charge
  - Rapid Recharge
  build_variants:
  - Gun bruiser
  - Grenade pivot
  enabled_by:
  - 09-16 Ira Domini + Ricochet/Split Shot buff
  - huge HP/base stats
  - vitality items untouched this patch
  - built-in anti-heal (grenade) into a sustain/tank meta
  countered_by:
  - mobile initiators (Lash, Yamato)
  - gap-closing tanks (Abrams)
  - CC and kiting comps
  - poke that out-ranges him (Vindicta)
  last_changed_patch: Minor Update - 09-16-2026
  notes: 'Changelog: 09-16 - Ira Domini now works with Ricochet/Split Shot (3 bolts);
    Weakening Headshot -13->-12% nudges his lane shred relative to buffed Hollow Point.
    Snapshot is 14 days and mostly pre-patch - treat WRs as baseline.

    Data over creators: Fortitude and Hollow Point dropped from core (not in usage);
    Battle Vest (90% share) is the real first buy. Creator ''S-tier, no weak point''
    read is contradicted by his 45.7% WR.

    Two-build reality: gun bruiser is primary (70-90% shares), a ~40% grenade pivot
    is the secondary late option.'
  builds:
  - name: Gun bruiser
    damage: gun
    core_items:
    - Restorative Shot
    - Close Quarters
    - Monster Rounds
    - Intensifying Magazine
    - Weakening Headshot
    - Battle Vest
    - Bullet Lifesteal
    - Fleetfoot
    - Berserker
    popularity: primary
    notes: Frontline M1 build that stacks health, lifesteal and fire-rate so he can
      stand in melee range; Monster Rounds + Weakening Headshot win lane, Battle Vest/Bullet
      Lifesteal/Berserker turn him into an unkillable bruiser.
  - name: Grenade pivot
    damage: hybrid
    core_items:
    - Extra Charge
    - Spirit Resilience
    - Rapid Recharge
    popularity: secondary
    notes: Late re-buy (~20-23 min) into grenade charges and cooldown; the creators'
      anti-tank finisher that drops a Consecrating Grenade on Mid Boss/urn and shreds
      Metal Skin.
  matchups:
    beats:
    - Infernus
    - Haze
    - Wraith
    - Mo & Krill
    loses_to:
    - Abrams
    - Warden
    - Vindicta
    - Drifter
    - Lash
  matchup_notes: "Beats fellow gun carries by out-tanking and out-sustaining them\
    \ \u2014 Haze 48% and Wraith 47% match the reader note that he is the better pick\
    \ in that slot. Loses to gap-closing frontline CC (Abrams 38%, Lash 43%) that\
    \ locks him out of his own range. Vindicta's 39% is likely a lagging pre-patch\
    \ number \u2014 she is falling and flyers were hurt this patch."
  confidence: 0.6
  provisional: false
Victor:
  name: Victor
  role: tank/frontline
  archetypes:
  - tank/frontline
  tier: B
  trend: stable
  why: "A 26.1% pick rate with an exactly break-even 49.7% WR makes him the fair B-tier\
    \ baseline other frontlines are measured against \u2014 popular, never oppressive.\
    \ He grinds melee divers down with Aura of Suffering plus a Spirit Lifesteal/Healing\
    \ Booster sustain stack, but his low HP-per-boon leaves him the one tank that\
    \ burst and anti-heal can delete. The 09-16 tempo patch neither rewarded nor punished\
    \ him, so he holds at B."
  core_items:
  - High-Velocity Rounds
  - Extra Regen
  - Extra Spirit
  - Opening Rounds
  - Torment Pulse
  - Healing Booster
  - Enduring Speed
  - Spirit Lifesteal
  - Mystic Vulnerability
  - Infuser
  - Escalating Exposure
  build_variants:
  - Spirit sustain bruiser
  - Weapon-tempo start
  enabled_by:
  - core tank items left untouched by 09-16
  - Spirit Lifesteal + Healing Booster sustain stack
  - melee-diver meta he outlasts (Mina, Calico, Lash)
  countered_by:
  - burst vs low HP-per-boon (Yamato, Holliday)
  - anti-heal and trimmed healing items
  - ranged poke / flyers (Vindicta)
  - tank stat-checks (Abrams, Mo & Krill)
  - CC
  last_changed_patch: Minor Update - 07-09-2026
  notes: "Data disagrees with the 07-16 creator read: Refresher and Echo Shard appear\
    \ in none of his top-15 high-rank buys over 30 days \u2014 his real build is spirit\
    \ sustain, not a Refresher initiator.\nWin and matchup numbers are a 14-day pre-09-16\
    \ snapshot; the tier could drift if anti-heal or burst assassins tighten.\nUntouched\
    \ by Minor Update 09-16 (last changed 07-09)."
  builds:
  - name: Spirit sustain bruiser
    damage: spirit
    core_items:
    - Extra Regen
    - Extra Spirit
    - Torment Pulse
    - Healing Booster
    - Enduring Speed
    - Spirit Lifesteal
    - Mystic Vulnerability
    - Infuser
    - Escalating Exposure
    popularity: primary
    notes: 'Default build: stack regen through lane, then spirit DoT (Torment Pulse,
      Mystic Vulnerability, Escalating Exposure) to grind fights down while outlasting
      them.'
  - name: Weapon-tempo start
    damage: hybrid
    core_items:
    - High-Velocity Rounds
    - Opening Rounds
    popularity: secondary
    notes: Very early weapon items (~2.4 and 5.1 min) to win the lane last-hit/deny
      war before pivoting into the spirit build; 40% share and the best WR of any
      cluster item.
  matchups:
    beats:
    - Mina
    - Calico
    - Bebop
    - Haze
    - Lash
    loses_to:
    - Ivy
    - Vindicta
    - Mo & Krill
    - Abrams
    - Drifter
  matchup_notes: "He beats divers who must enter his Aura of Suffering (Mina 56%,\
    \ Calico 55%, Lash 53%) \u2014 his DoT sustain outlasts their burst. He loses\
    \ to a kiting healer (Ivy 43%) and a ranged flyer (Vindicta 45%) he cannot reach\
    \ or finish, and drops the tank mirror (Abrams 47%, Mo & Krill 47%) where low\
    \ HP-per-boon leaves him out-stat."
  confidence: 0.6
  provisional: false
Paige:
  name: Paige
  role: lane-winning support
  archetypes:
  - support/healer
  - lane bully
  tier: S
  trend: rising
  why: 'Support best built for the lane-wins-matter economy: she wins lane then snowballs
    a carry (Billy, Abrams) before trimmed comeback souls can rescue the enemy. 09-16
    heavy-melee spirit scaling (0.3->0.45) and Captivating Read buffs (T1 -11->-14s,
    T3 +1m->+2m) sharpen a kit already lane-dominant, and the flyer threats she feared
    were cut. 52.7% WR / 29.2% PR; near-even into Rem/Ivy caps her dominance.'
  core_items:
  - High-Velocity Rounds
  - Opening Rounds
  - Extra Charge
  - Slowing Hex
  - Mystic Expansion
  - Knockdown
  - Superior Cooldown
  - Greater Expansion
  build_variants:
  - Tempo support
  - CC lockdown
  enabled_by:
  - 09-16 buffs (heavy melee spirit scaling; Captivating Read talents)
  - tempo / lane-wins meta
  - anti-flyer shifts (air-drag slows, Silver's Weighted Bola)
  - Billy/Abrams frontline partners
  countered_by:
  - burst assassins (Yamato, Lash, Holliday)
  - Rem
  - Ivy
  - anti-heal (healing-item trims)
  last_changed_patch: Minor Update - 09-16-2026
  notes: 'Changelog: 09-16 - heavy-melee spirit scaling 0.3->0.45, Captivating Read
    T1 -11->-14s / T3 +1m->+2m; Slowing Hex cd 27->29s is a minor tax, partly offset
    by its new air-drag reach.

    Data check: old core items Healing Tempo and Fortitude do not appear in the 30-day
    usage list - replaced by the real early-gun-into-spirit core. Knockdown is a below-average
    buy (50.8% WR vs 52.7% hero) despite 50% usage.

    Matchup samples are small and the snapshot is pre-09-16, so the S leans on the
    thesis plus the newest creator read (heresy 09-17) - confidence modest.'
  builds:
  - name: Tempo support
    damage: hybrid
    core_items:
    - High-Velocity Rounds
    - Opening Rounds
    - Extra Charge
    - Slowing Hex
    - Mystic Expansion
    - Superior Cooldown
    - Greater Expansion
    popularity: primary
    notes: Cheap weapon T1/T2 win the lane (HVR 1.2m, Opening Rounds 4.6m), then spirit
      charges/cooldown/range spam Captivating Read and Plot Armor to snowball a carry.
  - name: CC lockdown
    damage: spirit
    core_items:
    - Slowing Hex
    - Knockdown
    popularity: secondary
    notes: Adds anti-mobility lockdown for pick comps; creator-flagged 'CC-slop,'
      and Knockdown's 50.8% WR (below her 52.7%) marks it as the weaker path.
  matchups:
    beats:
    - Wraith
    - Paradox
    - Haze
    - Mina
    - Warden
    loses_to:
    - Rem
    - Ivy
    - Dynamo
    - Billy
    - Vindicta
  matchup_notes: "The real edges are vs falling gun carries/initiators \u2014 Wraith\
    \ 57%, Paradox 57%, Haze 55% \u2014 where her lane pressure and Plot Armor heals\
    \ blunt the picks and scaling windows those archetypes need. She is only even\
    \ (49%) into Rem and Ivy, fitting the creator read that she is a weaker Rem: both\
    \ out-heal and out-escape her. Dynamo at 49% contradicts the old 'counters Dynamo\
    \ ult' line \u2014 treat that as stale."
  confidence: 0.6
  provisional: false
The Doorman:
  name: The Doorman
  role: utility initiator
  archetypes:
  - initiator
  - burst caster
  tier: B
  trend: falling
  why: 'Popular but not winning (46.5% WR, 12.7% PR): a delayed, setup-dependent initiator
    that early snowball beats. The 09-16 patch hit him indirectly twice - the tempo
    meta rewards dive over setup, and Veil Walker''s rework stripped the Sprint Boots
    plus movespeed-on-break his kidnap/escape shell relied on. Doorway still isolates
    a carry (his answer to Silver), but reach comes too late.'
  core_items:
  - Mystic Burst
  - Extra Charge
  - Mystic Expansion
  - Rapid Recharge
  - Tankbuster
  - Boundless Spirit
  - Vortex Web
  - Slowing Hex
  - Veil Walker
  build_variants:
  - Bell carry (AoE spirit)
  - Kidnap / utility (Doorway pick)
  enabled_by:
  - Doorway isolate (answers Silver by removing the carry from a fight)
  - AoE/charge spirit items (Mystic Expansion, Greater Expansion, Extra Charge)
  - high pick rate keeps a large coordinated-player base
  countered_by:
  - dive tempo (Yamato, Lash, Apollo, Holliday)
  - Doorway range cut 70->65m (08-12)
  - 'tempo meta: early snowball beats his delayed payoff'
  - Vortex Web/Slowing Hex being low-WR bait items
  last_changed_patch: Minor Update - 08-12-2026
  notes: 'Changelog: 09-16 - no direct line; loses his Veil Walker disengage (Sprint
    Boots + movespeed-on-break removed) and his archetype is punished by the tempo
    push.

    Usage backs the creator ''kidnap is a trap'' read: Vortex Web (56%, 45.1% WR)
    and Slowing Hex (70%, 45.3%) are his two worst staples vs the Bell core''s Tankbuster
    51.2% / Boundless Spirit 57.4%.

    No gun build exists despite HVR 78% / Opening Rounds 66% - those are cheap lane
    filler. Low confidence on matchups (no qualifying pairs).'
  builds:
  - name: Bell carry (AoE spirit)
    damage: spirit
    core_items:
    - Mystic Burst
    - Extra Charge
    - Mystic Expansion
    - Rapid Recharge
    - Tankbuster
    - Boundless Spirit
    popularity: primary
    notes: Extra charges + AoE expansion + cooldown turn Call Bell into the 50-70k
      damage build creators call the real one; highest-WR staples (Tankbuster 51.2%,
      Boundless Spirit 57.4%).
  - name: Kidnap / utility (Doorway pick)
    damage: spirit
    core_items:
    - Vortex Web
    - Slowing Hex
    - Veil Walker
    - Improved Spirit
    - Greater Expansion
    popularity: secondary
    notes: Doorway-isolate pick build; hit by the 09-16 Veil Walker rework (lost Sprint
      Boots + movespeed-on-break, weakening the escape). Its staples were already
      his worst-WR buys (Vortex Web 45.1%, Slowing Hex 45.3%), matching the creator
      'kidnap build is the noob trap' claim; Shadow Weave is the nominal invis replacement
      but he gains far less from it than a gun carry.
  matchups:
    beats:
    - Silver
    loses_to:
    - Yamato
    - Lash
    - Apollo
  matchup_notes: 'No enemy pair cleared the sample threshold, so this is inference
    - low confidence. Doorway still isolates a carry, so he keeps a real answer to
    Silver, the meta''s top gun tank. He loses to dive tempo (Yamato, Lash, Apollo):
    they reach a squishy caster before Luggage Cart/Doorway set up - the same ''tempo
    beats setup'' pattern the 09-16 patch rewards.'
  confidence: 0.55
  provisional: false
Billy:
  name: Billy
  role: tank/frontline
  archetypes:
  - tank/frontline
  - lane bully
  tier: S
  trend: stable
  why: Lobby-default frontline (52.1% WR, 31.8% PR) that the tempo patch suits - winning
    lane now wins the game, and his lane-bully all-in wants early kills. Item tailwinds
    help the brawl (Lifestrike melee-heal up to 120+1.75 and its slow now drags flyers;
    Fortitude regen 2->2.25%), but anti-tank Shiv is his worst matchup and rising,
    so S is popularity-supported, not runaway.
  core_items:
  - Spirit Snatch
  - Stalker
  - Close Quarters
  - Monster Rounds
  - Grit
  - Spirit Shielding
  - Spirit Strike
  - Bullet Resist Shredder
  - Slowing Hex
  build_variants:
  - Melee-range hybrid bruiser
  - Spirit shred/slow bruiser
  enabled_by:
  - 09-16 tempo patch (lane leads snowball)
  - Spirit Snatch
  - untouched core tank/Vitality items
  - lane-bully meta
  - Lifestrike melee-heal + flyer-dragging slow buff (low confidence - item sits outside
    his top-15 30-day buys)
  - Fortitude regen buff
  countered_by:
  - anti-tank bruisers (Shiv)
  - anti-heal
  - kiting / sustained ranged gun (Warden, Seven)
  - sustain-peel (Ivy)
  last_changed_patch: Minor Update - 08-12-2026
  notes: 'Changelog: 09-16 - no direct line; item tailwinds (Lifestrike heal/slow,
    Fortitude regen) and the lane-wins meta support him. Anti-tank Shiv (his worst
    lane) is climbing.

    Data beats creators: Lifestrike, Echo Shard, Witchmail and Scourge/Scrooge never
    appear in his top-15 buys - real core is Spirit Snatch (95%), Stalker (90%), Close
    Quarters (88%), Monster Rounds (86%), Grit (83%). Item analysis calls him Lifestrike''s
    prime buyer, which the 30-day usage contradicts - treat that as low confidence.

    Held at S on 31.8% PR + a solid-not-dominant 52.1% WR; downgrade risk is real.'
  builds:
  - name: Melee-range hybrid bruiser
    damage: hybrid
    core_items:
    - Close Quarters
    - Monster Rounds
    - Grit
    - Stalker
    - Spirit Snatch
    popularity: primary
    notes: Closes distance early and brawls with point-blank gun + melee, then Spirit
      Snatch (95% buy) converts lane kills into the HP buffer that lets him front-line.
  - name: Spirit shred/slow bruiser
    damage: spirit
    core_items:
    - Spirit Shielding
    - Spirit Strike
    - Bullet Resist Shredder
    - Slowing Hex
    - Spirit Snatch
    popularity: secondary
    notes: Spirit-damage variant that shreds and slows to stay glued to squishy carries;
      pick it when the enemy frontline, not their backline, is the problem.
  matchups:
    beats:
    - Dynamo
    - Bebop
    - Mina
    - Paradox
    - Pocket
    loses_to:
    - Shiv
    - Ivy
    - Warden
    - Seven
    - Vindicta
  matchup_notes: "He farms squishy, low-mobility heroes who can't escape a melee bruiser\
    \ that out-stats them \u2014 Dynamo, Bebop, Paradox, Pocket and Mina all sit at\
    \ 55-58%. He bleeds to anti-tank and sustain: Shiv's execute kit is his worst\
    \ lane (43%) and Shiv is rising, while Ivy and Warden out-sustain/out-range his\
    \ all-in (45% each) and Seven/Vindicta poke the big slow body from range (48%)."
  confidence: 0.58
  provisional: false
Graves:
  name: Graves
  role: gun carry/summoner split pusher
  archetypes:
  - gun carry
  - split pusher
  - late scaler
  tier: C
  trend: falling
  why: 'Worst early game of any carry (low HP, two stamina, no mobility) and the 09-16
    economy deletes her path: with comeback souls gutted, her ~25-min scaling line
    has no bail-out, so the small health/boon (33->35) and Jar of Dead buffs don''t
    offset it (48.5% WR, 21% PR reads as low-elo popularity, not strength). Toxic
    Bullets'' scaling buff (0.005->0.006) is a marginal pickup for her on-hit line.'
  core_items:
  - Restorative Shot
  - Mystic Shot
  - Extra Spirit
  - Arcane Surge
  - Improved Spirit
  - Heroic Aura
  - Toxic Bullets
  - Superior Duration
  - Echo Shard
  build_variants:
  - Summoner/cooldown spirit
  - On-hit gun
  enabled_by:
  - Jar of Dead buffs
  - health/boon buffs (33->35)
  - stall supports (Kelvin, Ivy)
  - late-game scaling
  countered_by:
  - mobile assassins (Holliday, Lash, Yamato, Mina, Calico, Drifter)
  - dive
  - out-scaling gun carries (Haze, Silver, Wraith, Warden)
  - slows
  - tempo/comeback-nerf meta
  last_changed_patch: Minor Update - 09-16-2026
  notes: 'Changelog: 09-16 - comeback souls trimmed and Rift resist made per-minute,
    removing her comeback path; health/boon 33->35 + Jar of Dead buffs are small;
    Toxic Bullets scaling buff is a marginal on-hit gain.

    Creator vegas (07-16) rates D; I rate C because 48.5% WR is bad but not collapse
    and 21% PR keeps her visible. heresy (09-17) gives no read.

    Losses skew to mobile dive (Warden 42%, Wraith 44%) and assassins who reach her
    before she scales.'
  builds:
  - name: Summoner/cooldown spirit
    damage: spirit
    core_items:
    - Extra Spirit
    - Arcane Surge
    - Improved Spirit
    - Echo Shard
    - Superior Duration
    popularity: primary
    notes: Cooldown/duration stack (Echo Shard + Superior Duration + Arcane Surge)
      to spam Jar of Dead summons and Grasping Hands; the most-bought cluster and
      why she is not a pure gun hero.
  - name: On-hit gun
    damage: gun
    core_items:
    - Restorative Shot
    - Mystic Shot
    - Heroic Aura
    - Toxic Bullets
    popularity: secondary
    notes: Lane-sustain into sustained on-hit; Heroic Aura's fire-rate aura plus Toxic
      Bullets vs tanks, but she lacks the scaling to out-carry a real gun carry.
  matchups:
    beats:
    - Paradox
    - Bebop
    loses_to:
    - Warden
    - Wraith
    - Calico
  matchup_notes: "Beats Paradox (53%) and Bebop (52%): both stand still to channel\
    \ or duel, so Grasping Hands and summon pressure land easily. Loses to Warden\
    \ (42%) and Wraith (44%) \u2014 gun carries that out-range and out-scale her,\
    \ Warden's Binding Word pinning her immobile frame. Calico/Lash/Drifter are near-even\
    \ but all mobile dive, so they reach her before she scales."
  confidence: 0.6
  provisional: false
Apollo:
  name: Apollo
  role: lane bully initiator
  archetypes:
  - lane bully
  - initiator
  - tank/frontline
  tier: S
  trend: rising
  why: "The tempo patch's clearest archetype winner despite no direct notes: gutted\
    \ comeback souls and the scaling early-Rift resist turn his win-lane/invade/escape\
    \ tempo into real wins, and his spirit core lost nothing \u2014 only his secondary\
    \ Restorative Locket sustain line was trimmed. The 49.3% WR / 21.3% PR is a 14-day\
    \ pre-patch baseline, so hold the S read loosely; Riposte (08-12) keeps his duel/escape\
    \ tool free."
  core_items:
  - Extra Regen
  - Mystic Burst
  - Extra Spirit
  - Mystic Expansion
  - Spirit Strike
  - Improved Spirit
  - Healing Booster
  - Spirit Snatch
  - Boundless Spirit
  - Tankbuster
  - Restorative Locket
  - Healbane
  - Dispel Magic
  build_variants:
  - Spirit bruiser
  - Spirit support/utility
  - Cooldown scaling
  enabled_by:
  - economy/tempo patch (09-16)
  - comeback-soul gutting
  - early-Rift resist nerf
  - Riposte buffs (08-12)
  - spirit item pool untouched
  countered_by:
  - Lash
  - Abrams
  - Mo & Krill
  - Warden
  - anti-heal vs his Locket/heal sustain
  last_changed_patch: Minor Update - 08-12-2026
  notes: "09-16: no direct changes \u2014 structural economy/Rift shifts favor his\
    \ tempo; the Restorative Locket nerf dents only his support line.\nOld core_items\
    \ (Fortitude) had zero usage; data says pure spirit, so reworked to Extra Spirit/Mystic\
    \ Burst/Improved Spirit cores.\n'Super buffed this patch' (heresy 09-17) is creator\
    \ inference, not measured \u2014 his 49.3% WR is a pre-patch baseline, so hold\
    \ the size of the buff loosely."
  builds:
  - name: Spirit bruiser
    damage: spirit
    core_items:
    - Extra Regen
    - Mystic Burst
    - Extra Spirit
    - Mystic Expansion
    - Spirit Strike
    - Improved Spirit
    - Healing Booster
    - Spirit Snatch
    - Boundless Spirit
    - Tankbuster
    popularity: primary
    notes: Lane-phase spirit poke into flat spirit burst; buy early T1s -> Improved
      Spirit -> T3/T4 spirit once ahead. Boundless Spirit and Tankbuster are late-game
      luxuries (buy_min 22+), not lane items.
  - name: Spirit support/utility
    damage: spirit
    core_items:
    - Restorative Locket
    - Healbane
    - Dispel Magic
    popularity: secondary
    notes: Team-fight sustain and debuff-clear package that matches the older 'unkillable
      with Locket + Dispel' read; buy when fights are extended or the enemy has debuffs/heal
      to answer.
  - name: Cooldown scaling
    damage: spirit
    core_items:
    - Compress Cooldown
    - Superior Cooldown
    popularity: niche
    notes: Late CDR pivot; these have the best item WRs on the board (Superior Cooldown
      55.6%) but low share, so it is a win-more when games run long.
  matchups:
    beats:
    - Mina
    - Vindicta
    - Drifter
    - Haze
    - Calico
    loses_to:
    - Warden
    - Abrams
    - Lash
    - Wraith
    - Mo & Krill
  matchup_notes: "He beats burst squishies he can dive before they scale: Mina (55%),\
    \ Vindicta/Haze (~52%), whose range his lane pressure and Riposte punish. He loses\
    \ to frontline that out-sustains his burst (Abrams 44%, Mo & Krill 46%) and to\
    \ Lash (44%), whose mobility out-positions his melee range \u2014 the vegas line\
    \ that Riposte 'cancels Lash' reads as dated, the data has him losing that pairing."
  confidence: 0.6
  provisional: false
Rem:
  name: Rem
  role: support/healer
  archetypes:
  - support/healer
  tier: B
  trend: stable
  why: 'Rem is a coin-flip support (50.1% WR) whose value tracks the frontline meta:
    with deathball comps out and healing items trimmed (Radiant Regeneration, Restorative
    Locket), his percent-max-HP heal and cleanse are strong but no longer a win condition
    on their own. He farms wins off squishy burst carries he can out-sustain (Paradox,
    Wraith, Haze) and loses to the meta''s divers (Lash, Drifter) and to Ivy, who
    fills the same heal slot with a better body.'
  core_items:
  - Extra Charge
  - Healing Booster
  - Improved Spirit
  - Extra Spirit
  - Arcane Surge
  - Grit
  - Extra Regen
  - Guardian Ward
  - Superior Duration
  - Divine Barrier
  build_variants:
  - Spirit heal support
  - Vitality frontline shell
  - Lane gun package
  enabled_by:
  - percent-max-HP heal
  - cleanse
  - Abrams
  - Billy
  - Shiv
  - Viscous
  - Dynamo
  - Divine Barrier
  countered_by:
  - anti-heal
  - trimmed healing items
  - Ivy
  - Lash
  - Drifter
  - Yamato
  - Holliday
  - tempo meta
  last_changed_patch: Minor Update - 09-16-2026
  notes: '09-16 change is a breakable-spawn/bug fix plus target UI only (heresy 09-17);
    not the ''big nerf'' the community assumed, so strength impact is minor.

    Old core_items Decay/Healing Nova are absent from current high-rank usage; the
    July ''always buys Decay'' read is stale and replaced by the spirit heal shell.

    Trend call is low-confidence: the 1500-match snapshot is 14 days and mostly pre-patch,
    so 50.1% is a baseline, not a post-patch number.'
  builds:
  - name: Spirit heal support
    damage: spirit
    core_items:
    - Extra Charge
    - Healing Booster
    - Improved Spirit
    - Extra Spirit
    - Arcane Surge
    popularity: primary
    notes: Stacks spirit power and heal amps to scale the percent-max-HP heal and
      Naptime/Pillow Toss utility; the default Rem build (Extra Charge 93% at 5.4
      min).
  - name: Vitality frontline shell
    damage: hybrid
    core_items:
    - Grit
    - Extra Regen
    - Guardian Ward
    - Superior Duration
    - Divine Barrier
    popularity: secondary
    notes: Early survival shell so Rem can hold heal range on the frontline; Divine
      Barrier (45%, 55.8% WR) is the late payoff for fights.
  - name: Lane gun package
    damage: gun
    core_items:
    - High-Velocity Rounds
    - Opening Rounds
    popularity: niche
    notes: Very early (1.6/4.4 min) last-hit and poke tools for lane control, not
      a carry build.
  matchups:
    beats:
    - Paradox
    - Wraith
    - Paige
    - Vindicta
    - Haze
    loses_to:
    - Ivy
    - Warden
    - Lash
    - Drifter
    - Mo & Krill
  matchup_notes: Cleanse plus percent-max-HP heal erases pick/burst setups (Paradox)
    and out-lasts gun carries (Wraith, Haze) in extended fights. Loses to Ivy, who
    does the same heal job with a tankier body and a shorter-cooldown ult, and to
    dive/initiators Lash, Drifter and Mo & Krill that reach a low-HP support before
    the heal lands.
  confidence: 0.6
  provisional: false
Silver:
  name: Silver
  role: gun tank carry
  archetypes:
  - gun carry
  - tank/frontline
  tier: S
  trend: rising
  why: "An S-tier gun tank built for this patch: gun cycle now survives dashes/light\
    \ melee, health/boon rose 28->31 with sprint 1.5->2.5, and Weighted Bola grounds\
    \ and interrupts flyers \u2014 a front-line DPS tank who wants fights started\
    \ early, exactly what the lane-wins economy rewards. Her ceiling is stacked CC\
    \ (Mo & Krill, Bebop) and she still drops her two qualified matchups (Lash, Drifter);\
    \ the 46.7% WR is a pre-patch lagging number."
  core_items:
  - Restorative Shot
  - Melee Lifesteal
  - Stalker
  - Grit
  - Hunter's Aura
  - Spirit Shielding
  - Cold Front
  - Slowing Hex
  - Mystic Burst
  - Tankbuster
  - Unstoppable
  build_variants:
  - Gun tank
  - Utility/anti-CC bruiser
  enabled_by:
  - tempo/early-snowball meta
  - Weighted Bola grounded interrupt (anti-air)
  - gun-cycle smoothing (dash/light melee don't break cycle)
  - health/boon and sprint buffs
  - front-line initiators who start fights for her (Dynamo, Apollo, Lash)
  countered_by:
  - CC/debuff spam (Mo & Krill, Bebop, Paradox, The Doorman)
  - kiting and slows
  - anti-heal vs her Melee Lifesteal/Restorative Shot sustain
  - anti-tank bruisers (Shiv) and enemy Tankbuster buyers
  - matches up badly vs Lash and Drifter
  last_changed_patch: Minor Update - 09-16-2026
  notes: "09-16: health/boon 28->31, sprint 1.5->2.5, and Weighted Bola now grounds/interrupts\
    \ flyers \u2014 direct buffs; tier S held.\nMatchups: data lists Lash and Drifter\
    \ under both beats and loses_to at 45%; treated as losing records (45% < 50%).\n\
    Low-confidence: no post-patch WR exists (14-day snapshot is mostly pre-patch),\
    \ so the S/rising call leans on creator consensus and the meta thesis; anti-flyer\
    \ value of Weighted Bola is inferred."
  builds:
  - name: Gun tank
    damage: gun
    core_items:
    - Restorative Shot
    - Melee Lifesteal
    - Stalker
    - Grit
    - Hunter's Aura
    - Spirit Shielding
    popularity: primary
    notes: "The default shell \u2014 lane-sustain bruiser (97% Stalker, 96% Melee\
      \ Lifesteal, 90% Restorative Shot) that scales into a front-line DPS tank; run\
      \ it unless the enemy comp forces anti-CC."
  - name: Utility/anti-CC bruiser
    damage: hybrid
    core_items:
    - Cold Front
    - Slowing Hex
    - Mystic Burst
    - Tankbuster
    - Unstoppable
    popularity: secondary
    notes: "Splashes spirit chip and CC between gun cycles and stacks anti-CC when\
      \ you must survive the frontline \u2014 Unstoppable (42% share, 49.5% WR) and\
      \ Debuff Reducer are the highest-WR items on her."
  matchups:
    beats: []
    loses_to:
    - Lash
    - Drifter
  matchup_notes: "The only two qualified pairs are both 45% \u2014 Lash and Drifter,\
    \ mobile melee bruisers who can stick to her and out-trade; Silver has no positive\
    \ matchup with enough games. That is a ceiling note, not a floor: she wins through\
    \ tempo and pick pressure (15.1% PR) rather than countering specific heroes. Weighted\
    \ Bola's ground/interrupt should now help her against flyers (Vindicta, Grey Talon),\
    \ but that is inference, not data."
  confidence: 0.62
  provisional: false
Celeste:
  name: Celeste
  role: spirit burst carry
  archetypes:
  - spirit carry
  - burst caster
  - mobile assassin
  - late scaler
  tier: B
  trend: falling
  why: 'Late-scaling flying spirit burst is the wrong profile for a lane-wins tempo
    meta: comeback souls are gone, early-Rift fights are real, and the new air-drag
    slow bleeds her mid-flight. Seven direct 09-16 nerfs stack on Radiant Regeneration
    and Restorative Locket trims, which is why she sits at B rather than A; the 54.6%
    WR / 26.4% PR is a pre-patch baseline, and she still bursts squishy melee threats
    (Yamato, Pocket) but folds to sustain and mobile initiators.'
  core_items:
  - Extra Regen
  - High-Velocity Rounds
  - Mystic Regeneration
  - Radiant Regeneration
  - Mystic Expansion
  - Healing Booster
  - Restorative Locket
  - Torment Pulse
  - Greater Expansion
  - Witchmail
  - Spirit Shielding
  - Grit
  build_variants:
  - Spirit sustain-burst carrier
  - Anti-CC / anti-debuff tech
  enabled_by:
  - High base power + overloaded kit (mobility, four abilities)
  - Torment Pulse + Greater Expansion AoE around her ult
  - Ult damage in Mid Boss / Rift fights
  - Mystic/Radiant Regeneration sustain stack (nerfed but still core)
  countered_by:
  - "Silver \u2014 Weighted Bola grounds flyers like her"
  - Slows now bleed air drag (system)
  - 'Healing item trims: Radiant Regeneration, Restorative Locket'
  - "Scaling/comeback nerfs \u2014 late-scaler into a tempo meta"
  - "Ivy \u2014 out-sustains her burst window"
  - "Lash / Calico \u2014 mobile initiators that close and survive"
  last_changed_patch: Minor Update - 09-16-2026
  notes: "09-16: tier held at B (down from A) \u2014 the seven-nerf stack below plus\
    \ the air-drag flyer tax; Witchmail remains her anti-slow answer.\n54.6% WR /\
    \ 26.4% PR is a 14-day, mostly pre-patch snapshot \u2014 treat as a ceiling, not\
    \ current strength.\n09-16: seven direct nerfs plus indirect item, scaling, and\
    \ air-drag hits."
  builds:
  - name: Spirit sustain-burst carrier
    damage: spirit
    core_items:
    - Extra Regen
    - High-Velocity Rounds
    - Mystic Regeneration
    - Radiant Regeneration
    - Mystic Expansion
    - Healing Booster
    - Restorative Locket
    - Torment Pulse
    - Greater Expansion
    popularity: primary
    notes: "Regen-stacked spirit build: HVR early for bullet velocity/movespeed, then\
      \ Torment Pulse + Greater Expansion for AoE burst around her ult \u2014 weaker\
      \ now that Radiant Regeneration and Restorative Locket were trimmed."
  - name: Anti-CC / anti-debuff tech
    damage: hybrid
    core_items:
    - Witchmail
    - Spirit Shielding
    - Grit
    popularity: secondary
    notes: "Witchmail is her highest-WR item (60.6%, bought ~24m) \u2014 the answer\
      \ into heavy slow/CC comps, which matter more now that slows bleed air drag."
  matchups:
    beats:
    - Pocket
    - Yamato
    - Haze
    - Paradox
    - Bebop
    loses_to:
    - Ivy
    - Warden
    - Lash
    - Calico
    - Mina
  matchup_notes: "She wins the burst race vs squishy close-range threats \u2014 61%\
    \ vs Pocket and 59% vs Yamato (S-tier, but she lands her damage before he closes).\
    \ Sustained healers out-last her damage window (Ivy 47%), while mobile initiators/bruisers\
    \ who survive the first burst and close the gap (Lash, Calico) beat her 52-53%."
  confidence: 0.6
  provisional: false


## Win/pick-rate snapshot (last 14 days before this patch, ranked matches, high-rank filter)

hero | WR% | PR% | matches
Graves | 56.8 | 40.7 | 256798
Victor | 56.4 | 32.9 | 207561
Paige | 55.7 | 38.9 | 245072
Seven | 55.0 | 34.6 | 218176
Kelvin | 54.2 | 19.5 | 122749
Mo & Krill | 53.2 | 32.8 | 207058
Haze | 53.1 | 54.2 | 341559
Ivy | 52.7 | 28.7 | 181272
Dynamo | 52.5 | 31.4 | 198107
Lady Geist | 52.3 | 31.4 | 197703
Abrams | 52.1 | 32.9 | 207599
Calico | 51.7 | 27.1 | 171021
Lash | 51.1 | 46.9 | 295547
Drifter | 50.9 | 45.9 | 289535
Apollo | 50.8 | 26.9 | 169888
Vindicta | 50.5 | 31.2 | 196536
Yamato | 50.0 | 28.7 | 180954
Celeste | 49.6 | 29.2 | 184392
McGinnis | 49.2 | 16.3 | 102683
Infernus | 49.1 | 45.5 | 286629
Vyper | 49.1 | 19.0 | 119529
Warden | 49.1 | 20.6 | 129733
Wraith | 49.0 | 33.3 | 209755
Billy | 49.0 | 34.3 | 216500
Grey Talon | 47.9 | 16.8 | 106206
Holliday | 47.6 | 22.8 | 143890
Rem | 47.5 | 39.4 | 248505
Silver | 47.0 | 31.8 | 200635
Bebop | 46.7 | 47.9 | 302137
Viscous | 46.2 | 20.1 | 126663
Pocket | 46.1 | 25.1 | 158153
Shiv | 46.1 | 41.3 | 260511
Paradox | 46.0 | 33.3 | 209948
The Doorman | 45.9 | 19.1 | 120730
Venator | 45.9 | 45.7 | 288453
Mina | 45.8 | 39.3 | 247985
Mirage | 44.1 | 16.0 | 100775
Sinclair | 44.0 | 18.3 | 115317

## What to do

Produce an entry for **every hero in the knowledge base**, including heroes with no direct changes. For each hero combine:

- direct changes (kit, stats, talents) and their magnitude relative to how the hero is actually played (a nerf to an ability nobody maxes is minor);
- indirect effects from the item analysis (core items buffed/nerfed, build paths changed) and from the systems analysis (archetype up/down, tempo shift);
- the prior state: tier, trend, win rate. A hero at 54%+ win rate absorbing a moderate nerf is likely still strong; a hero at 47% taking the same nerf drops out.
- **cross-hero effects**: changes to *other* heroes matter. If a hero who counters this one (see `matchups.loses_to`, `countered_by`) got stronger or gained a tool that specifically punishes this hero (anti-air, anti-heal, silence, grounding), that is an indirect nerf; if a counter got weaker, an indirect buff. Name the other hero and the mechanic.
- **builds, not just kits**: judge a change against the hero's actual `builds` (gun vs spirit, primary vs niche). A nerf to an item only the niche build buys is minor; a nerf to the primary build's core item is not.
- **map and objectives**: for content/map updates, judge how the kit interacts with the new soul sources and fight locations (camp clear speed and AoE vs grouped Haunts, heavy melee for Tough Crates, mobility between districts, verticality for Bell Tower, stamina for Sunken Plaza, sustain vs harder camps, invisibility/vision for Steam Vents, split-push vs more spread-out objectives).

New heroes listed under direct changes but absent from the knowledge base: include them with `tier_before` "?", `in_notes` true, low `confidence`, and say the read is provisional.

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


## Creator sources published after this patch (optional corroboration; the notes, KB and snapshot remain primary — if a source contradicts them, say so and keep your own read)

### peercontent (2026-10-01)
Camps now hit harder and cluster so they chase you, so sustain and AoE camp clear (Yamato punch, Mina) define the early game — but the patch's real seismic change is Tough Crates: 58 souls each, guaranteed drops, and 200-300-soul quick routes in several lanes, which makes box runs more soul-efficient than camp farming and pushes the game toward farming and slower tempo. Where fights happen is now map-driven: Sunken Plaza at the 5-8 minute window, Bell Tower centers after 8, and lanes next to crate routes. Side asymmetry (Arch Mother gets Sunken Plaza plus the theater with healing bats and heavy crates) is large enough that pros altered draft rules around it, and tower dives are now punishable because parrying a Guardian spends your parry cooldown.
- map/neutrals: Haunt camps deal more damage so you must dodge attacks; players are already gaming it by pulling a T3 camp behind cover so it cannot shoot, clearing it with minimal damage.
- map/neutrals: Because camps group together and follow you, you can stack them for AoE clear, which is what pushes camp-clear items and heroes up.
- map/objectives: More vaults are on the map and spread out, making them harder to defend; Bell Tower alone has three. (Bell Tower: 3 vaults)
- map/objectives: Sunken Plaza (purple pit) connects to the secret shop, so unlike Bell Tower it has more than one way out.
- map/economy: Sunken Plaza pays ~4-500 souls collectible in about 10 seconds at 5 minutes, versus Rem's tunnels that gave about the same over a minute-plus — a massive efficiency jump. (~400-500 souls in ~10s vs ~500 souls over ~1min)
- map/economy: Bell Tower is worth around 280 souls at 5 minutes, so purple pit dominates the 5-8 minute window; after that the centers take priority. (~280 souls at 5 min)
- map/pickups: Healing Snacks (healing bats) heal 10% of maximum HP rather than missing HP, so even after taking laning damage two nearby bats reset you fast; they sit right behind each lane and pair well with a roamer's box route. (10% max HP)
- map/farm: Tough Crates are the patch's biggest change: each gives 58 souls on first spawn, guaranteed drops make the route efficient, several lanes have a quick route worth 200-300 souls, and the pre-2:30 neutral boxes turn into heavy crates worth over 100 souls. (58 souls per crate; 200-300 soul routes; >100 souls from the 2:30 wave's boxes)
- map/farm: Boxes now out-prioritize camps as a farm route because there are so many and the drops are guaranteed — and the creator expects crates to get nerfed.
- map/objectives: Arch Mother is the favored side because it gets Sunken Plaza plus the theater (healing bats and heavy crates); the asymmetry is large enough that the DNS draft rule was changed so that choosing side vs pick order goes to the other team.
- map/objectives: Guardians now spend your parry cooldown, so a tower dive can be punished — parry the Guardian, then heavy-melee the diver while the tower wakes up, forcing them to fight under it.
- map/movement: Auto-mantle — specifically backward auto-mantle — lets you kite and shoot while climbing, which the creator calls extremely broken and tells everyone to enable.
- patch call: major — Tough Crates (guaranteed 58-soul heavy boxes with 200-300-soul lane routes) make farming the dominant early game and push box routes above camp clears, while harder-hitting, clumping camps reward sustain and AoE.; winners: Yamato, Mina, Rem, The Doorman, Lash, Drifter, Apollo, Paradox, Mo & Krill, Celeste, Kelvin, Ivy; losers: Infernus, Billy, Calico, Bebop; non_obvious_calls: Rem rises because of a map change (three vaults at Bell Tower, vaults harder to defend), not a Rem buff., Infernus's drop is caused by removal of its global napalm amp that the creator could not find in the patch notes., Calico is held back by Tough Crates specifically, since punching them requires leaving cat form., Tower diving is effectively removed for most heroes by the parry-cooldown change, making Apollo and Krill outliers rather than the rule., Arch Mother's side advantage is big enough that DNS changed its side/pick-order draft rule around it., Sunken Plaza's value is its 5-8 minute timing (~400-500 souls in seconds) and secret-shop exit, so purple pit is the contested objective early while Bell Tower matures at 8+ minutes.
- Yamato: tier None rising — Camps group and follow you, and Yamato can gather them and punch them down fast, so the same camp-damage change that hurts others made Yamato jump up.
- Mina: tier None rising — Listed alongside Yamato as a riser off the grouped-camp clear dynamic.
- Rem: tier None rising — Perma-banned in DNS as it is; more vaults spread around the map (Bell Tower now has three) make defending against it harder, and camp damage makes its sustain more valuable.
- The Doorman: tier None rising — Bell Tower's single rope up/down plus its 280 souls makes kidnapping strong, and the height gap means you must pre-place a door before roping up — a build-around, not a casual pick. Bells ringing on any hit gives counterplay.
- Kelvin: tier None stable — Sustain pick for the higher camp damage; tried once in DNS, did not look great, but the creator still thinks it is good.
- Ivy: tier None rising — Floated as a sustain option for the same camp-damage pressure; low-confidence, one-line call.
- Lash: tier None rising — Lane matchups: in green lane the roof/tree above the bridge lets you hold the lane permanently — hit minions, take all souls, threaten — and boxes matter more now.
- Claire: tier None rising — Caption name is unreliable (not on the known hero list); grouped with Lash as buffed by lane matchups, specifically green-lane high-ground control. Treat as an unidentified hero.
- Infernus: tier None falling — Its global napalm amp is gone — teammates no longer get the bonus damage on tagged targets — which the creator says is not in the patch notes he saw; it fell from first ban/first pick to sixth pick.
- Drifter: tier None rising — More centers and hiding spots on the map, and Drifter's sense reveals players inside stealth, so it benefits from the stealth-friendly layout; typically paired with Apollo as a roaming pseudo front line.
- Apollo: tier None rising — Roaming pseudo front line that farms better; with two points in its T3 for bullet resist it is one of the few picks that can still dive towers after the Guardian-parry change.
- Paradox: tier None rising — The annoying-roamer slot is more viable with more hiding spots, and Paradox has moved ahead of Bebop in priority.
- Bebop: tier None falling — Same roamer archetype as Paradox but now the lower-priority option in that slot.
- Mo & Krill: tier None rising — The camp/uptime meta favors sustained front lines; with Billy down, Krill is the remaining real front line and already showed up in DNS.
- Billy: tier None falling — Fell off because the meta is oriented around camps and needs more uptime; its front-line slot went to Krill.
- Celeste: tier None stable — Unaffected and still extremely strong — very fast and a great scaler.
- Calico: tier None falling — Tough Crates hurt it because you must leave cat form to heavy-punch them; unpicked so far in DNS, which the creator attributes to that.

For heroes with nothing relevant (no direct changes, no affected core items, archetype neutral) set direction "neutral", magnitude "none", and keep reasons empty. Do not pad.

`tier_after` is your call on the post-patch tier (S/A/B/C/D); keep `tier_before` from the KB (use "?" if unknown). Only move a tier when the reasons justify it. `confidence` reflects how sure you are about the direction, 0-1.

## Output schema

{
  "heroes": [
    {
      "hero": "hero name exactly as in the knowledge base",
      "in_notes": true,
      "direction": "up|down|neutral",
      "magnitude": "none|minor|moderate|major",
      "confidence": 0.0,
      "direct_reasons": ["1 short sentence per driving change, name the stat"],
      "indirect_reasons": ["1 short sentence per item/system driver, name the item or system"],
      "build_changes": ["concrete build advice: swap X for Y, delay Z, new core W; empty if none"],
      "tier_before": "S|A|B|C|D|?",
      "tier_after": "S|A|B|C|D",
      "one_liner": "<= 20 words a player would actually say about this hero after the patch"
    }
  ]
}
