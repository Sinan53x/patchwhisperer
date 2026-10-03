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
  "hero": "Bebop",
  "in_notes": false,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.45,
  "direct_reasons": [],
  "indirect_reasons": [
   "peercontent: the roamer slot is more viable but Paradox has moved ahead of him, and his single-target hook converts less into a farm-and-sustain economy."
  ],
  "build_changes": [],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Same roamer slot as Paradox, now the lower-priority option."
 },
 {
  "hero": "Calico",
  "in_notes": false,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [],
  "indirect_reasons": [
   "Tough Crates \u2014 the patch's dominant farm route \u2014 need a Heavy Melee, which forces her out of cat form and locks her out of that economy; peercontent has her unpicked in DNS.",
   "Offset: the tempo meta still suits her dives."
  ],
  "build_changes": [
   "Cannot run the box-route economy efficiently; lean harder on kills/off-map gold and delay farm-heavy openings."
  ],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Cat form locks her out of the new heavy-crate farm \u2014 the patch's one real black mark on her."
 },
 {
  "hero": "Mo & Krill",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [],
  "indirect_reasons": [
   "peercontent: the camp/uptime meta favors sustained front lines and he takes Billy's front-line slot; tank archetype up.",
   "With two points in T3 bullet resist he is one of the few that can still dive towers after the parry-cooldown change."
  ],
  "build_changes": [],
  "tier_before": "B",
  "tier_after": "A",
  "one_liner": "Billy's fall hands him the front-line slot \u2014 the default sustained tank now."
 },
 {
  "hero": "Shiv",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.45,
  "direct_reasons": [],
  "indirect_reasons": [
   "Tank/frontline up means more big-HP targets for current-HP Serrated Knives; harder camps reward his regen sustain."
  ],
  "build_changes": [],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Anti-tank that eats the rising frontline wave \u2014 quietly the best tank-killer."
 },
 {
  "hero": "Ivy",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.35,
  "direct_reasons": [],
  "indirect_reasons": [
   "peercontent floats her up on camp-damage sustain (low-confidence); Healing Snacks and trimmed healing items cut both ways for a healer."
  ],
  "build_changes": [],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Sustain option for the harder camps, but the healing-item trims muddy her heal identity."
 },
 {
  "hero": "Warden",
  "in_notes": false,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.4,
  "direct_reasons": [],
  "indirect_reasons": [
   "Late-scaler gun carry in the early-close economy with no comeback valve; his Shadow Weave invis-engage gains little from Steam Vents relative to roamers."
  ],
  "build_changes": [],
  "tier_before": "C",
  "tier_after": "C",
  "one_liner": "Still a slow gun scaler the tempo economy refuses to wait for."
 },
 {
  "hero": "Yamato",
  "in_notes": true,
  "direction": "up",
  "magnitude": "moderate",
  "confidence": 0.55,
  "direct_reasons": [
   "Flying Strike now creates paths against solid targets (turrets, Shrines, objectives), adding mobility and objective access."
  ],
  "indirect_reasons": [
   "peercontent: she gathers and punches down the new grouped, chasing Haunt camps faster than almost anyone; the tempo meta rewards her burst."
  ],
  "build_changes": [],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Camp-clear champion of the patch with a new Flying Strike path \u2014 take A toward S."
 },
 {
  "hero": "Lash",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [],
  "indirect_reasons": [
   "peercontent: green-lane high ground (roof/tree above the bridge) lets him hold lane permanently, and boxes matter more; his dive/stomp snowballs in the no-comeback economy."
  ],
  "build_changes": [],
  "tier_before": "S",
  "tier_after": "S",
  "one_liner": "Still the highest-pick initiator, now with a lane-roof to farm off."
 },
 {
  "hero": "Viscous",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.3,
  "direct_reasons": [],
  "indirect_reasons": [
   "Harder camps reward his Cube sustain, and more spread-out vaults reward his Goo Ball map presence."
  ],
  "build_changes": [],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Cube sustain helps vs the harder camps; not a headline mover."
 },
 {
  "hero": "Mina",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.4,
  "direct_reasons": [],
  "indirect_reasons": [
   "peercontent: rises off grouped-camp AoE clear (same dynamic as Yamato), and her mobility suits the new districts."
  ],
  "build_changes": [],
  "tier_before": "C",
  "tier_after": "C",
  "one_liner": "Camps group and chase \u2014 she clears them; her damage problem stays."
 }
]

## Current hero entries (this batch only)

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
  last_changed_patch: null
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
  released_on: null
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
  released_on: null
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
  released_on: null
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
  released_on: null
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
  released_on: null
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
  released_on: null
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
  released_on: null
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
  released_on: null
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
  released_on: null
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
