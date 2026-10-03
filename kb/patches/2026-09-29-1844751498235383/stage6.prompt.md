# Task: update the knowledge base after this patch

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

## Hero analysis (movers only)

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
 },
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
 },
 {
  "hero": "Drifter",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [],
  "indirect_reasons": [
   "peercontent: more centers/hiding spots and his stealth-revealing sense favor him in the Steam-Vent layout; heavy-melee crate access and the tank/roamer archetypes are up."
  ],
  "build_changes": [],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Stealth-friendly map plus a stealth-revealing sense \u2014 the roamer who benefits most."
 },
 {
  "hero": "Victor",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.45,
  "direct_reasons": [],
  "indirect_reasons": [
   "Tank/frontline archetype up: harder camps reward his regen/sustain stack, and the snapshot's 56.4% WR is the second-highest on the board."
  ],
  "build_changes": [],
  "tier_before": "B",
  "tier_after": "A",
  "one_liner": "Sustain frontline the camp-damage meta feeds \u2014 climbing on the numbers."
 },
 {
  "hero": "Paige",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.4,
  "direct_reasons": [],
  "indirect_reasons": [
   "Lane-adjacent crate routes and Healing Snacks reward the lane pressure that is her whole identity; the contested hubs suit her carry-snowball."
  ],
  "build_changes": [],
  "tier_before": "S",
  "tier_after": "S",
  "one_liner": "Wins lane then banks crates and heals \u2014 exactly what the patch pays for."
 },
 {
  "hero": "The Doorman",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.45,
  "direct_reasons": [],
  "indirect_reasons": [
   "peercontent: Bell Tower's single rope up/down plus its ~280 souls makes his Doorway kidnap strong, and the height gap forces pre-placed doors \u2014 a build-around.",
   "Offset: the tempo read still punishes his delayed setup."
  ],
  "build_changes": [
   "Pre-place a Doorway before roping up to Bell Tower to enable the kidnap."
  ],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Bell Tower's single rope makes his kidnap a real objective play."
 },
 {
  "hero": "Billy",
  "in_notes": false,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [],
  "indirect_reasons": [
   "peercontent: he fell off because the camp/farm meta wants more uptime, and his front-line slot went to rising Krill; anti-tank Shiv is still climbing."
  ],
  "build_changes": [],
  "tier_before": "S",
  "tier_after": "A",
  "one_liner": "Fell off \u2014 the meta wants uptime and sustain, so Krill took the front-line slot."
 },
 {
  "hero": "Apollo",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [],
  "indirect_reasons": [
   "peercontent: roaming pseudo-front-line that farms crates/roams better and, with T3 bullet resist, is one of few still able to dive towers after the parry-cooldown change."
  ],
  "build_changes": [],
  "tier_before": "S",
  "tier_after": "S",
  "one_liner": "Tempo lane bully that can still tower-dive \u2014 the patch's clean archetype winner."
 },
 {
  "hero": "Rem",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.45,
  "direct_reasons": [],
  "indirect_reasons": [
   "peercontent: harder camps reward his sustain and more spread-out vaults (Bell Tower now has three) make his map play stronger; Healing Snacks slightly cheapen dedicated healing."
  ],
  "build_changes": [],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Rises on a map change, not a buff \u2014 harder camps and harder-to-defend vaults."
 },
 {
  "hero": "Silver",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.35,
  "direct_reasons": [],
  "indirect_reasons": [
   "Tank/frontline up suits her gun-tank sustain shell; her anti-air (Weighted Bola) already prices flyers out."
  ],
  "build_changes": [],
  "tier_before": "S",
  "tier_after": "S",
  "one_liner": "Gun tank the sustain/camp meta feeds; still the flyer answer."
 }
]

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

## Current meta.md

# Meta state
Last patch: Minor Update - 09-16-2026 (2026-09-16)

## Thesis
Games are won in the lane. With comeback souls gutted and early Unstable Rift fights now real, a lane lead converts straight into tempo — brawling bruisers and mobile snowballers (Paige, Apollo, Silver, Yamato, Holliday, Lash, Haze) set the pace. Late scalers and flyers (Celeste, Warden, Wraith, Vindicta) lost the nets that bought them time. The old "overloaded DLC" S-tiers (Mirage, Venator, Doorman, Pocket) keep their kits at ~46% WR; the meta no longer rewards them.

## Economy and systems
- Comeback bounties are trimmed and extra comeback souls rerouted to the two lowest-econ players via tick gold, so the fed AFK farmer is dead and lane leads stick.
- Guardian bounty +10%, Walker +5%, objective share 30->25%.
- Unstable Rift resist 10% +1%/min (cap 40% at 30m), not flat 35% — early rift contests are real fights.
- Respawn at 20m 35->38s; a longer death tax raises the value of every pick.
- Stuns/parry pause reload instead of resetting; dashes and light melee no longer break gun cycle time (smooths Silver/Abrams weaving).
- Slows -20% globally but now drag air drag at 35% — grounded kiting improves, airborne heroes get pulled down.

## Map
(pre-City-Never-Sleeps map; not yet described)

## Archetype standing
- Tempo bruisers/frontline: up — brawl patch, gun-cycle smoothing, lane-wins economy.
- Early snowball carries: up — no comeback valve punishes an early lead.
- Late scalers: down — no safety net; games close before they spike.
- Flyers: down — air-drag slows plus Silver's anti-air Bola.
- On-hit spirit carries: weakened — Mercurial Magnum, Spiritual Overflow and Plated Armor hit at once.
- Tanks: stable — core items untouched; Dynamo gains ult CDR from Diviner's Kevlar.
- Sustain supports: down — Radiant Regeneration and Restorative Locket both trimmed.

## Watchlist
- Silver: Bola now grounds/interrupts flyers, plus HP/sprint and the gun-cycle change. Biggest winner.
- On-hit spirit trio (Warden, Wraith, Vyper): check WR dips and migration to pure gun.
- Veil Walker vs Shadow Weave: the invis items swapped Sprint Boots; watch Bebop/Holliday/Viscous.
- Celeste: seven nerfs plus item/flyer hits; her 54.6% WR is a lagging pre-patch number.
- Flyer WRs (Vindicta, Grey Talon, Lash) as evidence air-drag slows bite.

## Recent history
- Minor Update - 09-16-2026: tempo patch — comeback souls gutted, on-hit spirit carry killed, flyers taxed.
- 08-22-2026: Celeste tuning.
- 08-12-2026: McGinnis/Apollo tuning.
- 07-30-2026: Ranked Mode added.
- 07-28-2026: item and hero tuning.

## Current item entries (changed items only; may be empty for items not yet in the KB)

Corrupted items: (not in KB yet)

## What to do

Produce the post-patch knowledge base state. This KB is read by the analyst on the *next* patch, so write it as durable state, not as a patch summary.

1. **meta.md**: rewrite the whole document in this structure (markdown, <= 550 words):
   - `# Meta state` line with `Last patch: City Never Sleeps (2026-09-29)`
   - `## Thesis` — 2-4 sentences: how games are won right now (tempo vs scaling, fight shape, what archetypes carry).
   - `## Economy and systems` — bullets describing the current state of comeback, bounties, objectives, respawn, movement/slows, in present tense with current numbers where known.
   - `## Map` — current map state in present tense: lanes/districts, objectives with timings and values where known, farm sources (Haunt tiers, crates/boxes, Sinner's Sacrifice variants, Buff Containers), pickups (Healing Snacks, Steam Vents), side asymmetry, key routes. Keep it when nothing changed.
   - `## Archetype standing` — one bullet per archetype in play: up/down/stable and why.
   - `## Watchlist` — 3-6 bullets: heroes/items/systems that are uncertain and should be checked against data.
   - `## Recent history` — keep at most 5 bullets, newest first, one line per patch: "City Never Sleeps: <headline>". Carry forward existing bullets from the current meta.md, drop the oldest beyond 5.
2. **item_updates**: for each changed item, the fields that changed. Allowed fields: role, bought_by, slot, tier, notes. `bought_by` must list hero names that build it as core or common situational pick, updated for this patch.
3. **change_log**: one line per KB edit you made, for the human to skim.

Tier is one of S/A/B/C/D. Trend is rising/stable/falling.

## Output schema

{
  "meta_md": "full markdown text",
  "item_updates": {"Item Name": {"role": "...", "bought_by": ["..."], "notes": "..."}},
  "change_log": ["Item Name: bought_by +Wraith (now core after rework)", "..."]
}
