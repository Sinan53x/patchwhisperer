# Task: update hero knowledge-base entries after this patch

Patch: City Never Sleeps (2026-09-29)

## Synthesis

{
 "patch_size": "major",
 "size_why": "This is a full map rework with renamed lanes and four new districts, all neutrals replaced by new Haunt creatures, two new soul-hub objectives (Sunken Plaza, Bell Tower) plus a new crate economy, a temporary merchant tier (The Broker/Corrupted items), and combat-feel shifts (parry cooldown on objectives, instant cast, Walker fireballs). The way games are farmed and where they are fought both change, which is the definition of major.",
 "headline": "Where you farm and where you fight — guaranteed soul crates and telegraphed hub objectives — now decides matches more than lane mechanics do.",
 "meta_thesis": {
  "previous": "Games were won in the lane: with comeback souls gutted and an early Unstable Rift, a lane lead from tempo bruisers (Paige, Apollo, Silver, Yamato, Lash) snowballed straight into a close before late scalers could spike.",
  "new": "Games are now won in the map economy: routing to guaranteed high-value crate routes from ~2:30 and contesting Sunken Plaza (5-8 min) and Bell Tower (8+) replaces pure lane brawling as the lead engine, and AoE/sustain camp-clearers plus heavy-melee box farmers bank faster than anyone. The no-comeback valve is still intact, but efficient PvE farming and the ~30-min Broker spike partially re-open the door for scaling — the shift is from lane tempo to farm-route tempo, not a return to brawling.",
  "relationship": "shift",
  "why": "Tough Crates (58 souls, guaranteed, 200-300-soul lane routes) and the Plaza/Bell Tower hubs concentrate income into PvE routing (systems + peercontent), while the intact no-comeback economy keeps games close-able for camp-clearers like Yamato and Seven — the win condition moved off the lane, not off tempo."
 },
 "winners": [
  {
   "hero": "Yamato",
   "why": "Direct note: Flying Strike now creates paths against objectives, and her punch AoE gathers and clears the new grouped, chasing Haunt camps faster than almost anyone — the two things this patch pays for.",
   "indirect": false
  },
  {
   "hero": "Seven",
   "why": "Storm Cloud/Static Charge is arguably the best clear against stacked camps, so the patch's dominant PvE lead converts straight into his farm-then-scale line (55.0% WR on the snapshot).",
   "indirect": true
  },
  {
   "hero": "Mo & Krill",
   "why": "Billy fell off the front-line slot and Krill's sustained uptime plus T3 bullet resist make him the default tank — one of the few who can still tower-dive past the parry-cooldown change.",
   "indirect": true
  },
  {
   "hero": "Lash",
   "why": "The green-lane roof/tree lets him hold lane permanently (peercontent) and boxes matter more; still the top-pick initiator in a map built around forced hub fights.",
   "indirect": true
  },
  {
   "hero": "Drifter",
   "why": "New districts and hiding spots plus Steam-Vent invisibility expand roam routes, and his sense revealing stealth heroes is the direct counter to that layout.",
   "indirect": true
  }
 ],
 "losers": [
  {
   "hero": "Calico",
   "why": "Tough Crates — the patch's best farm route — require a Heavy Melee, which forces her out of cat form, locking her out of the dominant economy (unpicked in DNS per peercontent).",
   "indirect": true
  },
  {
   "hero": "Billy",
   "why": "The camp/uptime meta wants sustained presence and his front-line slot visibly moved to a rising Mo & Krill.",
   "indirect": true
  },
  {
   "hero": "Bebop",
   "why": "Same roamer slot as Paradox, but the more hiding-spot-friendly map now favors Paradox; his single-target hook converts less in a farm-and-sustain economy.",
   "indirect": true
  },
  {
   "hero": "Warden",
   "why": "A late-scaling gun carry in a map-economy patch with no comeback valve; the Stealth/Vent layout helps real roamers, not his Shadow Weave engage.",
   "indirect": true
  },
  {
   "hero": "Infernus",
   "why": "Peercontent reports his global napalm team-damage amp is gone — not present in these notes, so treat as unverified but he is sliding from first-pick/ban to ~sixth pick.",
   "indirect": true
  }
 ],
 "non_obvious_calls": [
  {
   "claim": "The 'Tough Crates need a Heavy Melee' line is effectively a targeted Calico nerf dressed as a general mechanic.",
   "why": "Her cat form cannot perform the heavy melee, so the single best soul route in the patch is closed to her while it opens for Abrams, Krill and other melee cores.",
   "confidence": 0.6
  },
  {
   "claim": "The Broker's ~30-min Corrupted shipment is an unintended late-scaler safety valve that partly offsets the no-comeback economy.",
   "why": "It gives scaling teams a concrete reason to bank souls and stall to 30 min, opposing the early-close thesis the rest of the patch reinforces.",
   "confidence": 0.45
  },
  {
   "claim": "The parry-cooldown change quietly deletes tower-diving for most of the roster, making Apollo and Krill outliers rather than the rule.",
   "why": "Parrying a Guardian now spends your parry, so the dive punish is real; only picks with T3 bullet resist can still commit under tower (peercontent).",
   "confidence": 0.55
  },
  {
   "claim": "Infernus's drop is driven by a change that is not in these notes at all.",
   "why": "If the reported global napalm amp removal is real, his fall is a stealth nerf a reader of the patch text would completely miss; flag as unverified.",
   "confidence": 0.3
  }
 ],
 "uncertainties": [
  "The tempo direction is genuinely split: the systems pass reads toward tempo (0.5 confidence) while peercontent argues guaranteed crate drops push toward farming and slower games — the patch may do both at different match stages.",
  "Six heroes announced for staggered release are not in these notes; their arrival can reset this entire thesis within weeks.",
  "The source-reported auto-mantle (climb-and-shoot) is not in the notes but is called extremely broken — if real, it is a bigger combat change than anything listed.",
  "Side asymmetry from Arch Mother (Sunken Plaza plus the theater) could skew win rates by map side rather than by hero, muddying week-one data."
 ],
 "what_to_watch": [
  "Whether crate routes get hotfixed-nerfed — peercontent expects it, and that would instantly flip the farm-route thesis back toward lane brawling.",
  "Yamato, Seven and Mina presence/win-rate as the camp-clear test of the AoE thesis.",
  "Calico and Bebop pick rates — if they stay near zero, the crate-lockout and roamer-slot reads are confirmed.",
  "Whether late-scaler win rates (Warden, Celeste, Infernus) stabilize after 30 min, which would validate the Broker-as-safety-valve read.",
  "Arch Mother vs the other side win rates to quantify the map asymmetry that already changed DNS draft rules.",
  "Any Infernus win-rate move to confirm or kill the unverified napalm-amp removal."
 ]
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

## Hero analysis (this batch only)

[
 {
  "hero": "Infernus",
  "in_notes": false,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.35,
  "direct_reasons": [],
  "indirect_reasons": [
   "peercontent reports his global napalm team-damage amp was removed, but it is not in these notes \u2014 treat as unverified and low-confidence.",
   "Burn AoE still clears the new grouped, chasing Haunt camps, so farm routes partly offset any loss."
  ],
  "build_changes": [],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "No notes change, but the community has him sliding \u2014 verify the napalm team-buff rumor before trusting it."
 },
 {
  "hero": "Seven",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.45,
  "direct_reasons": [],
  "indirect_reasons": [
   "Storm Cloud/Static Charge AoE clears the new stacked, chasing Haunt camps faster than almost anyone, and ability-range Buff Containers scale that AoE.",
   "No comeback valve still caps his farm-then-scale line, but the snapshot shows 55.0% WR."
  ],
  "build_changes": [
   "Farm-core (Monster Rounds/Cultist Sacrifice) is more valuable: clear stacked camps then run crate routes."
  ],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Best AoE jungle clearer in a patch built around stacked camps \u2014 his farm lead converts faster."
 },
 {
  "hero": "Vindicta",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.35,
  "direct_reasons": [],
  "indirect_reasons": [
   "New roofs/high ground let her hold lanes and poke into the Plaza (5-8 min) and Bell Tower fights; the flyer tax (Weighted Bola, air-drag slows) is already priced into her A."
  ],
  "build_changes": [],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Holds lanes from the new roofs and pokes every hub fight, but still pays the flyer tax."
 },
 {
  "hero": "Lady Geist",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [],
  "indirect_reasons": [
   "Tank/frontline archetype up: harder-hitting camps reward her regen/sustain stack, and Buff-Container Spirit Resist adds free defense.",
   "Her spirit-caster rivals Celeste and Pocket are still falling, clearing her slot."
  ],
  "build_changes": [],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Regen bruiser that out-sustains the harder camps \u2014 quietly climbing the front-line slot."
 },
 {
  "hero": "Abrams",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [],
  "indirect_reasons": [
   "Tank/frontline up, and his melee core gives cheap heavy-melee access to Tough Crates (58 souls each), the patch's best farm route.",
   "Parry-vs-objective change makes diving him under tower riskier for the enemy."
  ],
  "build_changes": [],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Melee frontline that can farm the new heavy crates as fast as anyone \u2014 quietly stronger."
 },
 {
  "hero": "McGinnis",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.4,
  "direct_reasons": [],
  "indirect_reasons": [
   "Turrets/wall zone the contested hub fights and defend against the now-punishable dives (parry-cooldown change); more spread vaults reward her siege.",
   "Turrets also help clear stacked camps."
  ],
  "build_changes": [],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Zone controller whose turret/wall setup fits the telegraphed hub fights and punishes dives."
 },
 {
  "hero": "Paradox",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.45,
  "direct_reasons": [],
  "indirect_reasons": [
   "New districts, hiding spots and Steam-Vent invisibility upgrade her roamer/pick setups; peercontent puts her ahead of Bebop in that slot."
  ],
  "build_changes": [],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "The annoying-roamer slot is more viable with more hiding spots \u2014 she's ahead of Bebop now."
 },
 {
  "hero": "Dynamo",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [],
  "indirect_reasons": [
   "Telegraphed hub fights (Plaza, Bell Tower) give Singularity clean setup windows, and his initiator items went untouched.",
   "Offset: his durable-frontline counters (Krill) are rising."
  ],
  "build_changes": [],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Singularity loves the new forced hub fights \u2014 still the default tempo initiator."
 },
 {
  "hero": "Kelvin",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.4,
  "direct_reasons": [],
  "indirect_reasons": [
   "Harder-hitting camps make his dome/sustain more valuable, and the snapshot's 54.2% WR supports it.",
   "Healing Snacks (10% max HP) and trimmed healing items slightly cheapen dedicated healing."
  ],
  "build_changes": [],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Sustain pick for the higher camp damage \u2014 peercontent calls him stable, the WR says strong."
 },
 {
  "hero": "Holliday",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [],
  "indirect_reasons": [
   "New districts, hiding spots and Steam-Vent invisibility expand her roam/pick routes; Bell Tower hub fights reward her lasso picks."
  ],
  "build_changes": [],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Mobile pick assassin built for the new hiding-spot, hub-fight map."
 }
]

## Current hero entries (this batch only)

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
  last_changed_patch: null
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
  released_on: null
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
  released_on: null
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
  released_on: null
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
  released_on: null
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
  released_on: null
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
  released_on: null
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
  released_on: null
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
  released_on: null
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
  released_on: null
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
  released_on: null
  provisional: false


## What to do

Produce the post-patch knowledge base state for the heroes in this batch. This KB is read by the analyst on the *next* patch, so write it as durable state, not as a patch summary.

1. **hero_updates**: for each mover, the fields that changed. Allowed fields: role, archetypes, tier, trend, why, core_items, builds (full replacement list of {name, damage, core_items, popularity, notes}), matchups ({beats, loses_to}), enabled_by, countered_by, notes. When an item change kills or creates a build, update `builds`, not just `notes`. When another hero's change alters a matchup, update `matchups`. Set `last_changed_patch` to "City Never Sleeps" for heroes that had direct changes. `why` is 1-2 sentences of present-tense state ("strong because X; weak to Y"), not a changelog. `notes` may hold a short changelog line (keep the last 3 lines, newest first). Do not touch heroes not in this batch.

   For each hero, output only the fields whose value actually changes. Omit any field that stays the same — omitted fields are kept as-is in the KB. Include `builds` only if at least one build is created, killed, or its core items change; when you include it, it is a full replacement list. Include `matchups` only if a matchup changes.
2. **change_log**: one line per KB edit you made, for the human to skim.

Tier is one of S/A/B/C/D. Trend is rising/stable/falling.

## Output schema

{
  "hero_updates": {"Hero Name": {"tier": "A", "trend": "falling", "why": "...", "core_items": ["..."], "last_changed_patch": "...", "notes": "..."}},
  "change_log": ["Hero Name: tier S -> A (Card Trick heal nerfs + Veil Walker loss)", "..."]
}
