# Task: synthesis (the verdict and the meta thesis)

Patch: Paint the Town (2026-10-16)
Change counts: General 10, Map 9, Items 1, Heroes 7, new_heroes 6, total 33

## Update summary

City Never Sleeps / Paint the Town is a major content update: a full map and neutral overhaul (new Haunts, districts, objectives, and pickups), six new heroes rolled out on a vote schedule, plus a temporary Corrupted-item merchant (The Broker). Almost no hero balance numbers — the meta moves through new soul sources, new pickups, and the Corrupted-item system rather than stat tuning. Read it as an economy/objective/kit-access update, not a balance patch.

## Previous meta thesis (knowledge base, pre-patch)

# Meta state
Last patch: Minor Update - 10-14-2026 (2026-10-15)

## Thesis
Games are still won in the map economy: templated PvE income — guaranteed Tough Crate routes from ~2:30, plus Sunken Plaza (5-8 min) and Bell Tower (8+) hub fights — is the lead engine, so AoE/sustain camp-clearers and heavy-melee box farmers bank faster than lane bullies. The 10-14 patch moved no souls, bounty, objective, respawn, item-slot, map or comeback lever; it only reshuffled which sustain front-line holds the tank slot — Baba cut out of it, Deadman Danny handed a buff package that still fights the unchanged anti-air environment. The no-comeback valve is intact; The Broker's ~30-min Corrupted tier remains the only stall window for late scalers. Fight shape is unchanged: farm-route tempo, then forced telegraphed group fights at hubs.

## Economy and systems
- Comeback bounties stay trimmed; extra comeback souls reroute to the two lowest-econ players via tick gold. Farm and lane leads stick.
- Guardian bounty +10%, Walker +5%, objective share 30->25% (carried from 09-16).
- Parrying a Guardian/objective spends the parry; only T3-bullet-resist picks (Apollo, Mo & Krill) still commit to dives.
- Respawn 38s at 20m — the long death tax keeps every pick's value high.
- Slows -20% globally, air drag 35%. Grounded kiting strong; flyers pulled down.
- Instant cast and Walker fireballs live: combat fast, objectives hit back.
- Trooper waves crash on intended cadence (10-05 fix holds); no new tempo lever since.
- The Broker spawns ~30 min, then ~every 15 min; Corrupted negatives are a runtime read.

## Map
Lanes renamed; four districts added. Neutral camps are Haunt creatures: they group, chase and hit harder, rewarding AoE clear and sustain. Farm sources: Tough Crates (58 souls, guaranteed, ~200-300-soul lane routes) need a Heavy Melee to open; Haunt camps; Sinner's Sacrifice variants; Buff Containers (ability range, spirit resist). Pickups: Healing Snacks (10% max HP), Steam Vents (invisibility roams). Hubs: Sunken Plaza (~5-8 min) and Bell Tower (8+, ~280 souls, one rope up/down, three vaults) concentrate telegraphed fights. New roofs/high ground and hiding spots — green lane holds a roof/tree above the bridge. Side asymmetry: Arch Mother's side owns Sunken Plaza plus the theater; split WRs by map side.

## Archetype standing
- AoE/sustain camp clearers: stable (top) — crate/Haunt income untouched.
- Heavy-melee frontline/tanks: stable, slot-migrated — Baba's barrier/resist/mobility cut vacates the slot; Mo & Krill (and Billy) hold it, and no other pick gained barrier or bullet resist.
- Sustain-frontline bruisers: down — Radiant Regeneration's third consecutive trim erodes the shared item the whole archetype frontlines behind.
- Roamers/pick assassins: stable — districts, hiding spots, Steam Vents unchanged.
- Stealth: stable — Vent routes expand; sense-reveal is the counter.
- Lane bullies / split pushers: up slightly — trooper-cadence fix persists.
- Late scalers: down, softening — no comeback valve vs the Broker stall window.
- Flyers: down — air drag unchanged, Silver's Bola still the answer; Deadman Danny is now the test of whether raw numbers beat that tax.
- On-hit spirit carries: down — 09-16 item hits (Mercurial Magnum, Spiritual Overflow, Plated Armor) persist.
- Non-melee assassins (Calico-style): down — cat form cannot heavy-melee the crate economy.

## Watchlist
- Baba WR and pick rate — does the front-line slot go to Mo & Krill/Billy outright, or does she survive as a T3-bullet-resist body?
- Radiant Regeneration buy rate on Lady Geist (~98%), Baba (~94%), Shiv, Celeste — does the third trim finally drop it below core?
- Deadman Danny WR — do the health/gun/mark buffs translate past the anti-air environment?
- Healbane/Decay buy rate — the tell that anti-heal, not regen, is the sustain answer.
- Any hotfix that adds a sustain item or touches Tough Crate/Bell Tower economy — that flips the thesis.
- Rat King WR post-09-16 nerf; Sinclair pick rate (kit-steal slot dead?).

## Recent history
- Minor Update - 10-14-2026: Baba frontline cut (barrier 1.2->0.7, -7% bullet resist, Granny Long Legs/Threadsap mobility trims, B->C); Deadman Danny buff package (HP 680->730, gun 12->15/44->48, Strix Salvo CD 30->25, execute 50->75%); Radiant Regeneration spirit scaling 0.04->0.035 (third trim).
- Minor Update - 10-05-2026: trooper-speed regression fixed (lane cadence restored); Rat King and Sinclair trimmed; map-economy engine untouched.
- City Never Sleeps: map rework — renamed lanes, four districts, Haunt camps replace neutrals, Tough Crate/Broker economy; lead engine moves off the lane.
- Minor Update - 09-16-2026: tempo patch — comeback souls gutted, on-hit spirit carry killed, flyers taxed.
- 08-22-2026: Celeste tuning.

## Systems analysis

{
 "systems_changed": [
  {
   "system": "Jungle / neutral camps (Haunts rework)",
   "change_summary": "Every neutral camp is replaced by nine new Haunt creature types with new behaviors (Specimen, Gutter Ghouls, Barrel Mimics, Past Dues, Stage Hands, Crabbage Pots, Festival Spirit, Shrooms, Underhands).",
   "driving_changes": [
    "Haunts: all neutral camps replaced by new creature types with new behaviors"
   ],
   "magnitude": "major",
   "effect_on_play": "Fixed jungle routes are dead — players must re-learn which camps pay and which punish, so map knowledge and AoE/sustain kits bank faster than memorized templates. Camp-fight shape (grouping, chasing, damage) is now a per-creature read rather than one known camp."
  },
  {
   "system": "Objectives (Bell Tower / Sunken Plaza)",
   "change_summary": "Two new district objectives: Bell Tower atop Chinatown (high soul concentration but rings a map-wide bell) and Sunken Plaza beneath the Plaza (strips stamina on descent and mutes outside sound).",
   "driving_changes": [
    "Bell Tower: new objective atop the Chinatown district; highly concentrated soul hotspot, but collecting it rings a bell heard across the map",
    "Sunken Plaza: new objective beneath the Plaza district main square; descending strips your stamina and mutes outside sound"
   ],
   "magnitude": "major",
   "effect_on_play": "Both pull telegraphed group fights to fixed hubs earlier, matching the existing Sunken Plaza/Bell Tower fight-gravity. Bell Tower taxes greed by broadcasting the farm; Sunken Plaza rewards a commit but the stamina-strip and muted audio make the exit a real risk."
  },
  {
   "system": "Bounty economy (Soul Bags)",
   "change_summary": "Kills now drop a contested Soul Bag you must secure before an ally takes it; last-hit rules apply to the bounty itself.",
   "driving_changes": [
    "Soul Bags: kills now drop a Soul Bag you must secure before an ally takes it — contested-last-hit rules now apply to the bounty itself"
   ],
   "magnitude": "moderate",
   "effect_on_play": "Kill income is no longer banked on the kill alone — the killer (or a faster teammate) must secure the bag, so fights extend and bounty income becomes slightly less reliable. Marginal nerf to clean 'secure the kill, bank guaranteed' burst patterns."
  },
  {
   "system": "Economy — Buff Containers",
   "change_summary": "Buff Containers now also roll Spirit Resist, Bullet Resist, Ability Range and Move Speed as permanent bonuses, not just the old range/resist pair.",
   "driving_changes": [
    "Buff Containers: revamped golden statues now also roll Spirit Resist, Bullet Resist, Ability Range, and Move Speed as permanent bonuses"
   ],
   "magnitude": "moderate",
   "effect_on_play": "Detouring for containers now pays off across more of a build, so off-lane routing and map-control roams gain value for every archetype; move speed and resists are worth contesting, raising the number of small skirmishes around pickups."
  },
  {
   "system": "Melee / breakables (Tough Crates)",
   "change_summary": "Tough Crates stay Heavy-Melee-gated and yield extra souls, confirming melee itemization as a farm prerequisite.",
   "driving_changes": [
    "Tough Crates: breakables that require a Heavy Melee to open; yield extra souls"
   ],
   "magnitude": "moderate",
   "effect_on_play": "Reinforces the heavy-melee frontline as the crate-economy king; gun-only and non-melee kits must buy into melee or concede that income, keeping the box-farm lead engine intact after the camp rework."
  },
  {
   "system": "Traversal / movement (Steam Vents, districts, pickups)",
   "change_summary": "Steam Vents grant invisibility plus regen while stood on, four off-lane districts add farm/fight routes, Healing Snacks are hidden heal pickups, and Sunken Plaza strips stamina on descent.",
   "driving_changes": [
    "Steam Vents: new terrain pickups granting invisibility and a small amount of regen while standing on them",
    "Districts: four off-lane areas added — Theater, Chinatown, Haunted Lot, Plaza",
    "Healing Snacks: new hidden pickups around the map that heal on grab",
    "Sunken Plaza: descending strips your stamina"
   ],
   "magnitude": "moderate",
   "effect_on_play": "Movement now carries a stealth/escape layer and stat detours, so repositioning and vision play matter more than raw lane presence; invisibility vents reward mobile assassins and vision counters, and healing snacks reward sustain-light kits."
  },
  {
   "system": "Parry",
   "change_summary": "Successfully parrying objectives no longer resets Parry cooldown.",
   "driving_changes": [
    "Parry: successfully parrying objectives no longer resets your Parry cooldown"
   ],
   "magnitude": "minor",
   "effect_on_play": "Kills the free parry chain at objective fights, so objective diving is harder to sustain and the T3-bullet-resist bodies that leaned on chained parries (Apollo, Mo & Krill) lose a small edge."
  },
  {
   "system": "Ability / Item activation",
   "change_summary": "Abilities and items now fire the instant the button is pressed instead of waiting for the next input window, lowering reaction latency globally.",
   "driving_changes": [
    "Ability/Item use: now fires the instant the button is pressed instead of waiting for the next input window"
   ],
   "magnitude": "moderate",
   "effect_on_play": "Combo and defensive-item timing tightens for every hero; burst and initiation windows land more cleanly and reactive saves (parry, defensive items) are more reliable, mildly favouring fast-cast kits over slow telegraphs."
  },
  {
   "system": "Corrupted items / The Broker",
   "change_summary": "Broker trades high-tier items for Corrupted versions with shared per-match random negatives, first shipment ~30 min then roughly every 15 min; Street Brawl now grants a Corrupted item after the Round 5 draft.",
   "driving_changes": [
    "Corrupted items: high-tier items can be exchanged for Corrupted versions with random negative attributes assigned per match; the positive/negative roll is identical for all players in a given game",
    "Street Brawl: now grants a Corrupted item after the item draft in Round 5"
   ],
   "magnitude": "major",
   "effect_on_play": "Adds a mid-late risk/reward conversion layer that is identical for everyone, keeping the ~30-min mark as the key scaling/stall window and rewarding leads that convert before the shared negatives bite."
  },
  {
   "system": "Sinner's Sacrifice",
   "change_summary": "Bonus now has variable timings instead of a fixed window.",
   "driving_changes": [
    "Sinner's Sacrifice: bonus now has variable timings instead of a fixed window"
   ],
   "magnitude": "minor",
   "effect_on_play": "Removes memorized-timer contesting of the sacrifice, so players must react to it and the objective becomes higher-variance and less reliably pre-farmed."
  },
  {
   "system": "Walkers",
   "change_summary": "Walkers no longer keep firing fireballs after dying.",
   "driving_changes": [
    "Walkers: no longer keep firing fireballs after dying"
   ],
   "magnitude": "minor",
   "effect_on_play": "Removes post-death chip damage, so lingering near a killed Walker to push the wave or take a fight is safer — a small quality-of-life buff to sieging and to holding a just-cleared lane."
  }
 ],
 "tempo_shift": {
  "direction": "toward_tempo",
  "confidence": 0.6,
  "why": "New early-mid soul hotspots (Bell Tower, Sunken Plaza) and contested Soul Bags push fights over income sooner while no comeback lever is added and the Broker's ~30-min window stays the only scaling stall. The shared Corrupted layer and Buff Container stat detours add map-wide risk/reward but do not add a comeback valve."
 },
 "archetype_effects": [
  {
   "archetype": "tank/frontline",
   "direction": "up",
   "magnitude": "moderate",
   "why": "Tough Crates keep heavy-melee income king and Buff Containers now roll Bullet/Spirit Resist as permanent bonuses; the objective-parry nerf is only a minor tax."
  },
  {
   "archetype": "mobile assassin",
   "direction": "up",
   "magnitude": "moderate",
   "why": "Steam Vents grant invisibility, districts add routes, and instant ability/item activation tightens pick and escape timing."
  },
  {
   "archetype": "burst caster",
   "direction": "up",
   "magnitude": "minor",
   "why": "Instant ability/item use cleans up combo windows, and Buff Containers now roll Ability Range as a permanent bonus."
  },
  {
   "archetype": "initiator",
   "direction": "up",
   "magnitude": "minor",
   "why": "Lower activation latency makes engage windows land more reliably across the new telegraphed hubs."
  },
  {
   "archetype": "gun carry",
   "direction": "neutral",
   "magnitude": "minor",
   "why": "Instant activation helps, but the crate economy stays melee-gated and Buff Containers roll defensive stats rather than gun stats."
  },
  {
   "archetype": "lanes bully",
   "direction": "neutral",
   "magnitude": "minor",
   "why": "Lane cadence is untouched and the income engine still lives off-lane in camps and district hubs."
  },
  {
   "archetype": "late scaler",
   "direction": "down",
   "magnitude": "minor",
   "why": "No comeback lever was added and new early-mid hotspots concentrate tempo fights, while the Broker window is unchanged."
  },
  {
   "archetype": "support/healer",
   "direction": "down",
   "magnitude": "minor",
   "why": "Healing Snacks and Steam Vent regen let sustain-light kits self-sustain, trimming reliance on dedicated healing."
  },
  {
   "archetype": "split pusher",
   "direction": "neutral",
   "magnitude": "minor",
   "why": "Districts open more routes but contested Soul Bags make bounty income less reliable, roughly cancelling out."
  },
  {
   "archetype": "poke/siege",
   "direction": "up",
   "magnitude": "minor",
   "why": "Walkers no longer fire after dying, making it safer to hold a just-cleared lane and press the wave."
  }
 ],
 "intent_read": "Valve is relaunching the City Never Sleeps map as the game's main content and re-spreading soul income across many contested, discoverable sources rather than one memorized route. The reworked Haunts, new district objectives, contested Soul Bags and permanent-stat Buff Containers push players into more telegraphed, fought-over economy moments, with the shared Corrupted-item layer standardizing late risk/reward across the lobby."
}

## Item analysis

{
 "items": [
  {
   "item": "Corrupted items",
   "direction": "rework",
   "magnitude": "major",
   "summary": "A new non-buildable merchant tier converts a finished high-tier item into a stat-boosted version carrying match-wide random negatives, so it's a between-match variance lever rather than an edge to whoever reaches The Broker first (rolls are symmetric). Because it only activates at ~30 min and pays teams that bank and stall, it runs against this patch's earlier, more contested soul economy — the tier raises the ceiling for games that still go long, and largely idles in the tempo games the patch is pushing.",
   "affected_heroes": [],
   "build_shift": "It converts an existing completed slot rather than adding one, so a bad negative roll can brick a core item — expect late-game players to hold a spare high-tier slot or delay a purchase until after the first ~30-min shipment rather than buy greedily into an unknown roll."
  }
 ],
 "notable_item_stories": [
  "Corrupted items are the only new late-game power layer in a patch that pulled income earlier (Bell Tower, Sunken Plaza, contested Soul Bags), so its real value is inversely tied to how fast lobbies now close.",
  "Street Brawl's Round 5 Corrupted grant imports the tier into draft-mode mid-game, where symmetric rolls matter more than raw stats — watch whether it reshapes late Brawl picks.",
  "No hero has Corrupted items as a core or situational build slot (it isn't a buildable item), so there is no direct core-item hero link to trace this patch."
 ]
}

## Hero analysis (only heroes with direction != neutral)

[
 {
  "hero": "Infernus",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.45,
  "direct_reasons": [],
  "indirect_reasons": [
   "Grouped, chasing Haunt camps reward his burn AoE clear (Haunts rework)",
   "Buff Containers now roll Ability Range and Move Speed, both live on his spirit build",
   "Late-scaler down: no comeback lever added and the tempo shift ends games before his burn spikes"
  ],
  "build_changes": [
   "Dashfernus stays the primary line; the AoE farm tailwind adds value to the spirit build, not the burn gun build"
  ],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Burn AoE farms the new Haunt camps, but the map still ends before his late spike."
 },
 {
  "hero": "Seven",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.55,
  "direct_reasons": [],
  "indirect_reasons": [
   "Storm Cloud/Static Charge is among the best clears for grouped, chasing Haunt camps (Haunts rework)",
   "Guaranteed high-value Tough Crate routes bankroll his farm-then-scale opener",
   "New telegraphed hub fights (Sunken Plaza, Bell Tower) reward his AoE; Buff Containers add Ability Range",
   "Loses to rising dive (Calico/Yamato/Holliday) and the no-comeback economy still caps a behind Seven"
  ],
  "build_changes": [
   "Keep the Monster Rounds/Cultist Sacrifice farm opener; AoE camp clear is now the fastest route to his spirit core"
  ],
  "tier_before": "B",
  "tier_after": "A",
  "one_liner": "Best camp-clearer in the patch banks the new routes \u2014 strongest farmer, still no comeback."
 },
 {
  "hero": "Abrams",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.55,
  "direct_reasons": [],
  "indirect_reasons": [
   "Melee core gives cheap heavy-melee access to Tough Crates (58 souls each)",
   "Parry no longer resetting on objectives makes dives onto him riskier",
   "Tank/frontline and initiator archetypes both up; rising anti-tank Shiv is his real counter"
  ],
  "build_changes": [
   "Keep Close Quarters/Monster Rounds opener; treat Tough Crates as a second guaranteed soul route alongside lane"
  ],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Crate-melee income plus the parry change make him the farm-and-frontline winner."
 },
 {
  "hero": "McGinnis",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [],
  "indirect_reasons": [
   "Turrets clear grouped Haunt camps, adding a real farm route",
   "Telegraphed Plaza/Bell Tower hubs suit wall/turret zoning; Buff Containers add Ability Range",
   "Parry change punishes dives into her zone; poke/siege archetype up"
  ],
  "build_changes": [
   "Gun-turret core stays; turret AoE is now worth farming camps between hub fights"
  ],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Turrets farm the new camps and zone the new hubs \u2014 a quiet map-rework winner."
 },
 {
  "hero": "Paradox",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.55,
  "direct_reasons": [],
  "indirect_reasons": [
   "New districts, hiding spots and Steam-Vent invisibility upgrade her roamer pick setups",
   "Burst caster (Ability Range containers) and initiator archetypes up",
   "Still folds to rising mobile divers Yamato/Lash/Holliday"
  ],
  "build_changes": [],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Steam Vents and extra districts sharpen her picks; divers still punish the sniper."
 },
 {
  "hero": "Dynamo",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.55,
  "direct_reasons": [],
  "indirect_reasons": [
   "Telegraphed Plaza/Bell Tower hub fights give Singularity clean setup; initiator up",
   "Quantum Entanglement AoE dispel beats rising Lash/Drifter/Calico commits",
   "Loses to rising durable frontline Mo & Krill and Abrams"
  ],
  "build_changes": [
   "Spirit AoE initiator spine unchanged; hub fights make Warp Stone engage timings more valuable"
  ],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "New forced hub fights hand him Singularity windows; tank rise is the offset."
 },
 {
  "hero": "Holliday",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.55,
  "direct_reasons": [],
  "indirect_reasons": [
   "New districts, hiding spots and Steam-Vent invisibility expand her roam routes (mobile assassin up)",
   "Bell Tower hub fights reward Spirit Lasso picks",
   "Still loses to point-blank lockdown (Drifter, Bebop, Mo & Krill/Lash ults)"
  ],
  "build_changes": [
   "Charge-spirit pick build unchanged; Extra Charge/Rapid Recharge double-dips matter more with more roam angles"
  ],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "More districts and Steam Vents give the best pick assassin more routes and more lassos."
 },
 {
  "hero": "Bebop",
  "in_notes": false,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [],
  "indirect_reasons": [
   "A single-target hook cannot punish PvE crate/camp routing, and the roamer slot has tilted to Paradox",
   "Contested Soul Bags slightly extend fights he can win, but the farm/sustain economy converts less",
   "Loses to sustain and burst-proof tanks (Kelvin, Billy, Vyper)"
  ],
  "build_changes": [
   "Stays hook-combo hybrid; Siphon Bullets remains a niche late luxury, not a carry pivot"
  ],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Hook picks still land, but the economy now pays farming, not single-target combos."
 },
 {
  "hero": "Calico",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [],
  "indirect_reasons": [
   "Tempo/lane-snowball economy and new district/Steam-Vent routes suit her roam (mobile assassin up)",
   "Cat form still cannot heavy-melee Tough Crates, locking her out of the patch's best soul route",
   "Loses to rising tank frontline she cannot burst (Abrams, Victor, Dynamo)"
  ],
  "build_changes": [
   "Lean kills/off-map souls over crate income; Melee Lifesteal/Stalker spirit-assassin core unchanged"
  ],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Tempo and extra routes reward her dives; the crate lockout caps the farm half."
 },
 {
  "hero": "Grey Talon",
  "in_notes": false,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.45,
  "direct_reasons": [],
  "indirect_reasons": [
   "Flyer tax unchanged: air-drag slows and Silver's Weighted Bola ground him",
   "Lash (S, rising) is his worst lane at 36% and the highest-pick initiator",
   "New roofs/hubs favor poke, but the tempo economy denies him time"
  ],
  "build_changes": [],
  "tier_before": "C",
  "tier_after": "C",
  "one_liner": "Poke-flyer squeezed by the anti-air tax and a rising Lash \u2014 stays buried."
 },
 {
  "hero": "Mo & Krill",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.55,
  "direct_reasons": [],
  "indirect_reasons": [
   "Parry no longer resets on objectives removes his free objective-parry chain",
   "Default sustained front line with Billy slipping; T3 bullet resist still lets him commit under a Guardian",
   "Camp/uptime meta and telegraphed hubs suit Scorn/Burrow brawling",
   "Loses to rising Paige lane pressure and long-range kiting (Celeste, Vindicta)"
  ],
  "build_changes": [
   "Spirit bruiser core unchanged; Torment Pulse/Cold Front AoE is now a camp-clear tool between hub fights"
  ],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Handed the default front-line slot by the map economy; ranged kiting still beats him."
 },
 {
  "hero": "Shiv",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.45,
  "direct_reasons": [],
  "indirect_reasons": [
   "The tank/frontline wave (Abrams, Mo & Krill, Billy) feeds his current-HP Serrated Knives",
   "Harder Haunt camps reward his regen stack",
   "Snapshot WR is only 43.4% \u2014 treat the archetype read as directional, not confirmed"
  ],
  "build_changes": [
   "Spirit regen bruiser core unchanged; Serrated Knives get more value as frontline picks rise"
  ],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Rising frontlines are free food for his knives \u2014 if the low snapshot WR turns around."
 },
 {
  "hero": "Warden",
  "in_notes": false,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [],
  "indirect_reasons": [
   "Late-scaler down: the farm-route, no-comeback economy refuses to wait for his spike",
   "Shadow Weave gains little from the new district/Steam-Vent layout",
   "Gun-carry archetype neutral; no item in his core moved"
  ],
  "build_changes": [
   "One gun build stays; no new capstone replaces the nerfed T4 gun finishers"
  ],
  "tier_before": "C",
  "tier_after": "C",
  "one_liner": "Late gun scaler in an economy that ends games before he finishes building."
 },
 {
  "hero": "Yamato",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.55,
  "direct_reasons": [],
  "indirect_reasons": [
   "The patch's camp-clear champion: punch AoE gathers grouped, chasing Haunt camps",
   "Flying Strike creates paths against solid targets (turrets, Shrines, objectives) \u2014 extra objective access and mobility",
   "Mobile assassin and burst caster archetypes up; Buff Containers add Ability Range",
   "Still loses to rising sustain tanks Mo & Krill and Abrams"
  ],
  "build_changes": [
   "On-hit spirit proc backbone unchanged; use Flying Strike paths to reach Shrines/objectives the layout now separates"
  ],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Fastest camp-clear plus new objective paths \u2014 top-of-A assassin, capped by tanks."
 },
 {
  "hero": "Lash",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.6,
  "direct_reasons": [],
  "indirect_reasons": [
   "Green-lane roof/tree gives permanent lane high ground and boxes matter more to his farm",
   "Mobile assassin and initiator archetypes up; Steam Vents and districts extend his dive routes",
   "Silver's Weighted Bola and air-drag slows remain the counter"
  ],
  "build_changes": [
   "Stomp spirit build stays primary; the 09-16 Ground Strike scaling buffs still lead"
  ],
  "tier_before": "S",
  "tier_after": "S",
  "one_liner": "Highest-pick initiator gets lane high ground and more dive routes \u2014 still S."
 },
 {
  "hero": "Mirage",
  "in_notes": false,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [],
  "indirect_reasons": [
   "Late-scaler down and split-pusher archetype neutral under the contested-Soul-Bag economy",
   "Loses to rising Mo & Krill silence, Abrams and Lash dive",
   "Kit intact \u2014 he is beaten by the meta, not the notes"
  ],
  "build_changes": [],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Split-push scaler the tempo economy buries; kit fine, meta hostile."
 },
 {
  "hero": "Drifter",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.55,
  "direct_reasons": [],
  "indirect_reasons": [
   "New districts, Steam Vents and heavy-melee Tough-Crate routes fit his stealth-reveal melee roam",
   "Mobile assassin and tank/frontline archetypes up",
   "Loses to rising Apollo, Dynamo and Mo & Krill lane pressure"
  ],
  "build_changes": [
   "Spirit melee bruiser core unchanged; Tough-Crate melee routes add a farm angle to his roam"
  ],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Blind-pickable melee bruiser the new map's routes and crates were built for."
 },
 {
  "hero": "Victor",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.55,
  "direct_reasons": [],
  "indirect_reasons": [
   "Harder Haunt camps and longer PvE routes reward his Spirit Lifesteal/Healing Booster regen stack",
   "Tank/frontline up; his Aura of Suffering outlasts rising divers Mina/Calico/Lash",
   "Loses to anti-heal stacking and trimmed healing items"
  ],
  "build_changes": [
   "Spirit sustain bruiser core unchanged; regen stack is at its most valuable in a harder-camp economy"
  ],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "The camp meta feeds his regen stack; anti-heal is still his off-switch."
 },
 {
  "hero": "Paige",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.55,
  "direct_reasons": [],
  "indirect_reasons": [
   "Lane-adjacent crate routes and Healing Snacks reward her lane pressure",
   "Contested Plaza/Bell Tower hubs suit her carry-snowball; anti-flyer shifts help her team",
   "Loses to burst assassins (Yamato, Lash, Holliday), who are rising"
  ],
  "build_changes": [
   "Tempo support core unchanged; crate-route timings from ~2:30 add to her lane-pressure snowball"
  ],
  "tier_before": "S",
  "tier_after": "S",
  "one_liner": "Lane pressure converts straight into the patch's early crate and hub economy \u2014 still S."
 },
 {
  "hero": "The Doorman",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [],
  "indirect_reasons": [
   "Bell Tower's single rope and ~280-soul payout make his Doorway kidnap a real objective play",
   "Initiator archetype up; AoE/charge spirit items suit his Bell build",
   "Still punished by dive tempo (Yamato, Lash, Apollo, Holliday)"
  ],
  "build_changes": [
   "Bell carry (AoE spirit) stays the real build; pre-place a Doorway before roping up to Bell Tower"
  ],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Bell Tower finally gives his Doorway a kidnap objective play, but tempo still beats setup."
 },
 {
  "hero": "Billy",
  "in_notes": false,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [],
  "indirect_reasons": [
   "Crate/camp-uptime meta wants sustained presence; his front-line slot has moved to rising Mo & Krill",
   "Anti-tank Shiv (his worst lane, 43%) is climbing",
   "Tank archetype up, but his lane-bully all-in profile fits the patch less than the sustained fronts"
  ],
  "build_changes": [],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Lane-bully frontliner losing his slot to Mo & Krill in a sustain-and-farm economy."
 },
 {
  "hero": "Graves",
  "in_notes": true,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.4,
  "direct_reasons": [
   "Her gun now destroys Venator's traps \u2014 a real utility tool into an A-tier, 42% PR hero"
  ],
  "indirect_reasons": [
   "Late-scaler down: the no-comeback economy deletes her ~25-min scaling path",
   "Split-pusher archetype neutral; she still has the worst carry early game",
   "Snapshot reads 56.5% WR / 40.9% PR against the KB's 48.5% / 21% \u2014 conflict noted, tier held"
  ],
  "build_changes": [],
  "tier_before": "C",
  "tier_after": "C",
  "one_liner": "Trap-clearing is a genuine new tool, but the economy still denies her scaling window."
 },
 {
  "hero": "Apollo",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.55,
  "direct_reasons": [],
  "indirect_reasons": [
   "Parry no longer resets on objectives costs him the free objective-parry chain",
   "Routes crate paths and roams; T3 bullet resist still lets him commit under a Guardian despite the parry change",
   "Lane bully/initiator/tank archetypes up; his spirit item pool is untouched",
   "Baba's nerf eases his worst lane (~59% against him)"
  ],
  "build_changes": [
   "Spirit bruiser core unchanged; spirit items are untouched, so early T1s into Improved Spirit still lead"
  ],
  "tier_before": "S",
  "tier_after": "S",
  "one_liner": "Lane-bully initiator the crate-and-hub economy was built for \u2014 still S."
 },
 {
  "hero": "Silver",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.6,
  "direct_reasons": [],
  "indirect_reasons": [
   "Tank/frontline archetype up; gun cycle smoothing keeps her dash/melee M1 online",
   "Weighted Bola grounds the flyers the meta now leans on (Vindicta, Grey Talon, Celeste, Deadman Danny)",
   "Loses to rising Lash and Drifter, mobile bruisers that stick to her"
  ],
  "build_changes": [
   "Gun tank shell unchanged; Weighted Bola is now a live anti-air pick into flyer lanes"
  ],
  "tier_before": "S",
  "tier_after": "S",
  "one_liner": "Front-line gun tank with built-in anti-air, in a patch that rewards early fights \u2014 S."
 },
 {
  "hero": "Celeste",
  "in_notes": false,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [],
  "indirect_reasons": [
   "Late-scaler down plus the flyer tax (air-drag slows, Silver's Bola)",
   "Deadman Danny got a buff package and beats her 61% \u2014 a direct cross-hero threat",
   "Still loses to rising Ivy/Lash/Calico sustain-and-dive"
  ],
  "build_changes": [
   "Witchmail (her best-WR item) is the anti-slow answer now that slows matter more"
  ],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Flying burst scaler: wrong profile for a tempo patch, and Danny now hunts her."
 },
 {
  "hero": "Rat King",
  "in_notes": true,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [
   "Notes entry only: added to the weekly release-vote schedule \u2014 no balance change this patch"
  ],
  "indirect_reasons": [
   "Map-economy lead engine: heavy-melee Tough Crates, Scrap Grenade AoE clear of grouped Haunts, forced hub fights",
   "Tank/frontline and lane-bully fit the farm-then-group-fight meta",
   "Loses to sustain supports (Ivy, Kelvin, Paige, Dynamo) that out-heal one damage window"
  ],
  "build_changes": [
   "Gun-bruiser core unchanged; banner ult CD trim stays covered by Superior/Compress Cooldown"
  ],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Heavy-melee crate king with the board's best kit fit \u2014 holds A, not S."
 }
]

## Creator sources published after this patch (optional corroboration; the notes, KB and snapshot remain primary — if a source contradicts them, say so and keep your own read)

(none)

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
