# Task: synthesis (the verdict and the meta thesis)

Patch: City Never Sleeps (2026-09-29)
Change counts: General 12, Map 10, Items 1, Heroes 3, total 26

## Update summary

City Never Sleeps is a major content update: a full visual rework of the map with renamed lanes, all neutrals replaced by new Haunt creatures with new behaviors, and a wave of new map objectives and pickups (Sunken Plaza, Bell Tower, Tough Crates, revamped Buff Containers, Healing Snacks, Steam Vents). A temporary merchant, The Broker, sells match-wide Corrupted versions of high-tier items, and six new heroes are announced for staggered release. System-level changes (parry vs objectives, instant ability/item use, Walker death fireballs, Sinner's Sacrifice timing) and a handful of hero interaction fixes round out the update.

## Previous meta thesis (knowledge base, pre-patch)

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

## Hero analysis (only heroes with direction != neutral)

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

## What to do

Write the verdict a strong player wants in the first 30 seconds.

1. **Patch size.** Classify: `major` (systems rework or many structural changes; content updates: map rework, new objectives, new heroes; the way games are played changes), `significant` (meaningful systems or economy moves plus broad tuning; the tier list will move), `minor` (tuning; a few heroes move a tier, no systems shift), `hotfix` (a handful of fixes/tweaks). Justify in one or two sentences naming the drivers. Change counts alone do not decide size; a 5-line economy change can be major.
2. **Headline.** One sentence, the thing to remember.
3. **Meta thesis.** State the previous thesis in one sentence, the new thesis in one or two, and whether this is a continuation, a shift, or a reversal. The thesis is about *how the game is won* (tempo vs scaling, which archetypes carry, what the fights look like), not a list of heroes.
4. **Winners and losers.** 3-5 each, ranked, with the driver. Include indirect movers where justified; mark them as such.
5. **Non-obvious calls.** 2-4 claims a casual reader of the notes would miss: unlisted heroes that moved, a "general" change that is really a targeted nerf, a build that died, a sleeper item. Each with a confidence.
6. **Uncertainties and what to watch.** What you are unsure about and what data would settle it in the first week.

## Output schema

{
  "patch_size": "major|significant|minor|hotfix",
  "size_why": "1-2 sentences",
  "headline": "1 sentence",
  "meta_thesis": {
    "previous": "1 sentence",
    "new": "1-2 sentences",
    "relationship": "continuation|shift|reversal",
    "why": "1-2 sentences naming the drivers"
  },
  "winners": [{"hero": "name", "why": "1 sentence", "indirect": false}],
  "losers": [{"hero": "name", "why": "1 sentence", "indirect": false}],
  "non_obvious_calls": [{"claim": "1 sentence", "why": "1 sentence", "confidence": 0.0}],
  "uncertainties": ["1 sentence each"],
  "what_to_watch": ["1 sentence each"]
}
