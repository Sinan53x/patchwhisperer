# Task: update the knowledge base after this patch

Patch: Paint the Town (2026-10-16)

## Synthesis

{
 "patch_size": "major",
 "size_why": "A full map and neutral overhaul (all camps replaced by nine Haunt creature types), two new district objectives, contested Soul Bags, a new Corrupted-item merchant tier, and six new heroes — the content moves where souls come from, not hero stats.",
 "headline": "The map economy is rebuilt from memorized farm routes into contested, discoverable soul sources — tempo arrives earlier and no two jungles read the same.",
 "meta_thesis": {
  "previous": "The lead engine was templated PvE income — guaranteed Tough Crate routes plus Sunken Plaza/Bell Tower hub fights — so AoE/sustain camp clearers and heavy-melee box farmers banked faster than lane bullies, with no comeback valve.",
  "new": "The off-lane economy still wins games, but the fixed routes are gone: souls now come from behavior-varied Haunt camps, contested Soul Bags, permanent-stat Buff Containers, and earlier district objectives, so map knowledge and fast-clear kits bank faster than template memorizers.",
  "relationship": "shift",
  "why": "Drivers: all neutral camps replaced by nine Haunt types with new behaviors, Bell Tower/Sunken Plaza objectives, contested Soul Bags, and Buff Containers now rolling Move Speed plus Bullet/Spirit Resist. It extends 'map economy wins' but changes how and how early income is earned."
 },
 "winners": [
  {
   "hero": "Seven",
   "why": "Storm Cloud/Static Charge is the best clear for grouped, chasing Haunts and his crate-route opener now farms even faster (B->A).",
   "indirect": true
  },
  {
   "hero": "Yamato",
   "why": "Punch AoE farms the new camps fastest and Flying Strike paths open separated Shrines/objectives the new layout creates.",
   "indirect": true
  },
  {
   "hero": "Lash",
   "why": "Green-lane roof/tree gives permanent lane high ground and districts/Steam Vents extend an already top-pick diver's routes; stays S.",
   "indirect": true
  },
  {
   "hero": "Silver",
   "why": "Front-line gun tank with Weighted Bola anti-air in a patch that forces earlier fights — both the flyer tax and the frontline rise point at her.",
   "indirect": true
  },
  {
   "hero": "Mo & Krill",
   "why": "Handed the default front-line slot with Baba still cut and Billy slipping; T3 bullet resist still commits under a Guardian despite the parry change.",
   "indirect": true
  }
 ],
 "losers": [
  {
   "hero": "Bebop",
   "why": "A single-target hook cannot punish crate/camp routing — the farm economy pays AoE, not pick combos.",
   "indirect": true
  },
  {
   "hero": "Grey Talon",
   "why": "Flyer tax is unchanged (air drag, Silver's Bola) and rising Lash is his worst lane — stays buried.",
   "indirect": true
  },
  {
   "hero": "Warden",
   "why": "Late gun scaler in a no-comeback economy that now closes even faster; no item in his core moved.",
   "indirect": true
  },
  {
   "hero": "Mirage",
   "why": "Split-push scaler punished by contested Soul Bags and rising M&K/Lash — beaten by the meta, not the notes.",
   "indirect": true
  },
  {
   "hero": "Celeste",
   "why": "Flying burst scaler in a tempo patch, now hunted by buffed Deadman Danny (61% against her) and grounded by Bola.",
   "indirect": true
  }
 ],
 "non_obvious_calls": [
  {
   "claim": "The parry change is framed as a general objective tweak but is really a targeted nerf to the T3-bullet-resist objective-dive chain that Apollo and Mo & Krill relied on.",
   "why": "Removing the cooldown reset on objective parries deletes the free parry chain only those resist-heavy divers used to sustain a Guardian dive.",
   "confidence": 0.6
  },
  {
   "claim": "Contested Soul Bags quietly nerf burst assassins who banked income on 'secure the kill, bank guaranteed.'",
   "why": "Kill income now requires winning a second last-hit race on the bag, so secure-burst patterns convert less reliably.",
   "confidence": 0.55
  },
  {
   "claim": "Buff Containers are no longer just caster range stops — rolling Move Speed and Bullet/Spirit Resist makes them tank-contested pickups.",
   "why": "Permanent defensive and mobility stats change who detours and why, raising the count of small skirmishes around pickups.",
   "confidence": 0.5
  },
  {
   "claim": "The Corrupted tier's value is inversely tied to how fast this patch ends games.",
   "why": "It only activates around ~30 min, but Bell Tower/Sunken Plaza and contested income push fights and closures earlier, so many lobbies never reach the payoff.",
   "confidence": 0.55
  }
 ],
 "uncertainties": [
  "Six new heroes are vote-gated, so their real meta impact is a rollout question, not a balance question — the first days are a lottery of who gets to play them.",
  "Haunt camp soul values and clear difficulty are unstated, so 'which camps pay' is a live discovery rather than a given.",
  "It is unclear whether the tempo shift actually closes games before The Broker's ~30-min window or just relocates the stall to the new hubs.",
  "The win/pick snapshot conflicts with the KB in places (e.g., Graves 56.5%/48.5%), so some directional reads rest on contested data."
 ],
 "what_to_watch": [
  "Haunt camp soul values — which creature types are farm-worthy and which punish, and which kits clear them fastest.",
  "First-contest timing at Bell Tower (bell broadcast) and Sunken Plaza (stamina strip) — the tells that hubs have moved earlier.",
  "Soul Bag pickup rate — do fights genuinely extend to secure bounty, or does the bag get snaked and shift nothing.",
  "Buff Container contest rate, especially Move Speed and Bullet Resist rolls, as the signal that pickups now matter to tanks.",
  "New hero pick/win rates as the vote schedule rolls them out — plus whether a hotfix touches camp or crate economy."
 ]
}

## Hero analysis (movers only)

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

## Current meta.md

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

## Current item entries (changed items only; may be empty for items not yet in the KB)

Corrupted items:
  name: Corrupted items
  role: "Late-game merchant tier unlocked by The Broker (~30 min, then ~every 15 min);\
    \ not a buildable slot \u2014 you convert a finished high-tier item for extra\
    \ stats plus match-wide random negative attributes."
  bought_by: []
  slot: "Merchant shipment (The Broker) \u2014 no Vitality/Weapon/Spirit slot."
  tier: null
  notes: 'Rolls are symmetric: identical for all players in a match, so the tier adds
    between-match variance, not intra-match advantage to whoever reaches The Broker
    first. It rewards teams that can bank souls and stall to ~30 min, running counter
    to this patch''s early-close economy. Read it at runtime, not in a build plan;
    low-confidence (first KB entry).'


## What to do

Produce the post-patch knowledge base state. This KB is read by the analyst on the *next* patch, so write it as durable state, not as a patch summary.

1. **meta.md**: rewrite the whole document in this structure (markdown, <= 550 words):
   - `# Meta state` line with `Last patch: Paint the Town (2026-10-16)`
   - `## Thesis` — 2-4 sentences: how games are won right now (tempo vs scaling, fight shape, what archetypes carry).
   - `## Economy and systems` — bullets describing the current state of comeback, bounties, objectives, respawn, movement/slows, in present tense with current numbers where known.
   - `## Map` — current map state in present tense: lanes/districts, objectives with timings and values where known, farm sources (Haunt tiers, crates/boxes, Sinner's Sacrifice variants, Buff Containers), pickups (Healing Snacks, Steam Vents), side asymmetry, key routes. Keep it when nothing changed.
   - `## Archetype standing` — one bullet per archetype in play: up/down/stable and why.
   - `## Watchlist` — 3-6 bullets: heroes/items/systems that are uncertain and should be checked against data.
   - `## Recent history` — keep at most 5 bullets, newest first, one line per patch: "Paint the Town: <headline>". Carry forward existing bullets from the current meta.md, drop the oldest beyond 5.
2. **item_updates**: for each changed item, the fields that changed. Allowed fields: role, bought_by, slot, tier, notes. `bought_by` must list hero names that build it as core or common situational pick, updated for this patch.
3. **change_log**: one line per KB edit you made, for the human to skim.

Tier is one of S/A/B/C/D. Trend is rising/stable/falling.

## Output schema

{
  "meta_md": "full markdown text",
  "item_updates": {"Item Name": {"role": "...", "bought_by": ["..."], "notes": "..."}},
  "change_log": ["Item Name: bought_by +Wraith (now core after rework)", "..."]
}
