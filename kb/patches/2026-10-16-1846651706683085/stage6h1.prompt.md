# Task: update hero knowledge-base entries after this patch

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

## Hero analysis (this batch only)

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
  why: "Burn gun/spirit carry whose AoE still clears the new grouped, chasing Haunt\
    \ camps, so the patch's farm-route economy is roughly neutral for him and Dashfernus\
    \ (spirit dash) stays his stronger, untouched line. Watch item: an unverified\
    \ report that his global napalm team-damage amp was removed \u2014 it is not in\
    \ these notes."
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
  notes: "City Never Sleeps (09-29): burn AoE clears the new grouped Haunt camps;\
    \ an unverified peercontent report that his global napalm team-damage amp was\
    \ removed is not in the notes \u2014 confirm via win rate.\n09-16 (indirect):\
    \ Spiritual Overflow nerfed (40->30 spirit, 30->25% fire rate) \u2014 burn gun\
    \ build drops it for Toxic Bullets/Swift Striker; Dashfernus untouched.\nCorrection\
    \ accepted: not a pure gun hero \u2014 spirit items lead on both share and WR,\
    \ so both builds kept; spirit build edges out gun."
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
  trend: rising
  why: "Farm-first spirit AoE carry whose Storm Cloud/Static Charge is among the best\
    \ clears for the patch's grouped, chasing Haunt camps, so guaranteed high-value\
    \ crate routes bankroll his farm-then-scale line faster than most. The no-comeback\
    \ economy is still intact, so a behind Seven cannot recover \u2014 the map-economy\
    \ shift favors his archetype without restoring brawling."
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
  - fast jungle clear vs grouped Haunt camps (Storm Cloud/Static Charge)
  - guaranteed high-value Tough-Crate routes
  - Healbane vs sustain comps
  countered_by:
  - Calico (dive)
  - Yamato (mobile burst)
  - Holliday (mobile burst)
  - Bebop (Hook CC-lock)
  - tempo/invade meta
  last_changed_patch: Minor Update - 08-12-2026
  notes: 'City Never Sleeps (09-29, indirect): grouped Haunt camps + guaranteed Tough-Crate
    routes reward his AoE farm-first line; the no-comeback valve still caps a behind
    Seven.

    09-16 (indirect): Cultist Sacrifice bounty 180->170% trims his farm-banker opener.

    09-16 tempo patch (comeback souls cut, early Rift resist now 10%+1%/min, +3s respawn
    at 20m) hurts farm-first scalers.'
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
Abrams:
  name: Abrams
  role: tank initiator
  archetypes:
  - tank/frontline
  - initiator
  tier: B
  trend: rising
  why: Melee tank initiator whose melee core gives cheap heavy-melee access to the
    patch's best farm route (Tough Crates, 58 souls each), while the parry-cooldown-on-objectives
    change makes diving him under a Guardian riskier. Anti-heal stacking (Decay) still
    caps his Siphon sustain.
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
  - melee core -> cheap heavy-melee access to Tough Crates (58 souls)
  - parry-cooldown change makes dives on him riskier
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
  notes: "City Never Sleeps (09-29, indirect): his melee core farms Tough Crates cheaply\
    \ and the parry-on-objective change punishes dives on him; frontline archetype\
    \ up.\nCorrected vs prior entry: matchup data has him beating Venator 62% (197\
    \ games), so Venator is a target, not a counter; anti-heal (Decay) is an item/system\
    \ threat, not a hero pair.\nBuilds are data-derived (Close Quarters/Monster Rounds/Melee\
    \ Charge >85% share) \u2014 one melee-gun core plus a late spirit-CC tank layer;\
    \ creator echo-shard claim is not in usage data."
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
  trend: rising
  why: "Zone controller whose turret/wall setup fits the patch's telegraphed hub fights\
    \ (Sunken Plaza, Bell Tower), whose turrets also clear the grouped Haunt camps,\
    \ and who benefits from the parry change punishing dives onto her wall. Still\
    \ draft-dependent \u2014 near-useless into mobile dive + AoE."
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
  - telegraphed Plaza/Bell Tower hub fights (turret/wall zoning)
  - turrets clear grouped Haunt camps
  - parry-cooldown change punishes dives into her zone
  - "tempo/objective meta \u2014 Guardian bounty +10% rewards her lane siege"
  - Mini Turret HP buffs (08-12) and Medicinal Specter resist
  countered_by:
  - mobile burst divers (Yamato, Holliday, Silver) that jump the wall and delete turrets
  - AoE spirit burst (Lady Geist, Celeste, Dynamo) that clears turret stacks
  - global -20% slow nerf, which weakens her wall/Suppressor zoning
  last_changed_patch: Minor Update - 08-12-2026
  notes: 'City Never Sleeps (09-29, indirect): telegraphed hub fights and the dive-punishing
    parry change favor her turret/wall zoning, and turrets clear the grouped Haunt
    camps.

    Item data (14d, mostly pre-09-16) shows a real gun core (Intensifying Magazine
    77%, Monster Rounds 62%) plus spirit-amp turret items; no single dominant build.

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
  trend: rising
  why: 'Pick/sniper whose roamer identity is the winner here: new districts, more
    hiding spots and Steam-Vent invisibility upgrade her pick setups and put her ahead
    of Bebop in the roamer slot. Her stationary Carbine sniper line still folds to
    the meta''s mobile divers (Yamato, Lash, Holliday).'
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
  - new districts/hiding spots/Steam Vent invisibility (roamer pick setups; ahead
    of Bebop)
  countered_by:
  - Yamato
  - Lash
  - Holliday
  - cleanse/dispel
  - Veil Walker
  - range denial
  last_changed_patch: Minor Update - 09-16-2026
  notes: 'City Never Sleeps (09-29, indirect): new districts/hiding spots/Steam Vents
    upgrade her roamer pick setups and move her ahead of Bebop in that slot; the sniper
    line still folds to mobile divers.

    Data disagrees with the old ''Echo Shard every game'' read: the real core is a
    gun/carbine sniper, and Slowing Hex is 60%, not guaranteed.

    Changelog 09-16: Kinetic Carbine min-damage multiplier 25->10% and no longer scaled
    by T3; Slowing Hex cooldown up.'
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
  why: 'Tempo initiator whose Singularity gets clean setup windows from the patch''s
    telegraphed hub fights (Sunken Plaza, Bell Tower), with his initiator item spine
    untouched. Offset: his durable-frontline counters (Mo & Krill, Abrams) are the
    rising tank picks.'
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
  - telegraphed Plaza/Bell Tower hub fights (Singularity setup)
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
  notes: "City Never Sleeps (09-29, indirect): telegraphed Plaza/Bell Tower hub fights\
    \ give Singularity clean setup windows; initiator items untouched.\n09-16 (indirect):\
    \ Diviner's Kevlar gained +10% ultimate CDR \u2014 now a live buy for his Refresher/Singularity\
    \ plan.\nBuild read is a spirit-spine with a Refresher late spike; Headshot Booster\
    \ (50%, 2.6 min) is just a starting item, not a gun build."
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
Holliday:
  name: Holliday
  role: mobile assassin
  archetypes:
  - mobile assassin
  - initiator
  tier: A
  trend: rising
  why: 'Mobile pick assassin built for the new map: new districts, more hiding spots
    and Steam-Vent invisibility expand her roam routes, and the Bell Tower hub fights
    reward Spirit Lasso picks. She still loses to point-blank lockdown (Drifter, Bebop,
    Mo & Krill/Lash ults) that punishes her commit-heavy entry.'
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
  - new districts/hiding spots/Steam Vent invisibility (roam routes)
  - Bell Tower hub fights (lasso picks)
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
  notes: "City Never Sleeps (09-29, indirect): new districts/hiding spots/Steam Vents\
    \ expand her roam routes and Bell Tower hub fights reward lasso picks.\nChangelog\
    \ 09-16: Crackshot T2 resist-shred, longer Spirit Lasso, health/boon 41->43; Veil\
    \ Walker lost Sprint Boots and movespeed-on-break.\nDisagreement: heresy (09-17)\
    \ frames a 'gun hybrid' \u2014 ranked data shows a spirit charge/duration build\
    \ with no gun items beyond Recharging Rush, so treat 'gun hybrid' as a skirmish\
    \ label, not a build."
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
Bebop:
  name: Bebop
  role: hook initiator
  archetypes:
  - initiator
  - burst caster
  tier: B
  trend: falling
  why: 'Break-even single-target hook initiator (~50% WR at ~54% PR) who still generates
    picks but converts less in a farm-and-sustain economy: the roamer slot has tilted
    to Paradox, and a hook cannot punish PvE crate routing or camp clears. His 77%-buy
    Veil Walker remains stripped (no Sprint Boots, no movespeed-on-break) and his
    slows are still trimmed.'
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
  notes: "City Never Sleeps: no direct line; the farm/sustain economy plus Paradox's\
    \ rise down-rank him in the roamer slot.\nSiphon Bullets (27% buy, 60.4% WR) is\
    \ a small-sample late luxury, not a must-buy; builds stay hybrid \u2014 spirit-tagged\
    \ pick tools (Spirit Strike/Snatch, Slowing Hex) out-share the gun items.\n09-16:\
    \ slows -20%, Veil Walker loses Sprint Boots + movespeed-on-break; snapshot WRs\
    \ are pre-patch baseline."
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
  trend: stable
  why: Lane-winning mobile assassin whose tempo snowball still fits the no-comeback
    economy, and her worst matchup (Baba, ~58% against her) just lost barrier, bullet
    resist and mobility; she is still locked out of the Tough Crate farm by cat form
    and remains capped by tanks she cannot burst.
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
  notes: '10-14: Baba (beats her ~58%, her worst listed matchup) took a major nerf
    - eases with no cost to her; no direct change.

    City Never Sleeps: cat form cannot perform the Heavy Melee that Tough Crates need,
    locking her out of the patch''s best soul route; lean on kills/off-map gold.

    Melee-spirit is the default (Melee Lifesteal/Stalker/Spirit Strike/Cold Front/Spirit
    Snatch at 98-99%); the Rapid Recharge/Echo Shard set is gone.'
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
  last_changed_patch: null
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
  released_on: null
  provisional: false


## What to do

Produce the post-patch knowledge base state for the heroes in this batch. This KB is read by the analyst on the *next* patch, so write it as durable state, not as a patch summary.

1. **hero_updates**: for each mover, the fields that changed. Allowed fields: role, archetypes, tier, trend, why, core_items, builds (full replacement list of {name, damage, core_items, popularity, notes}), matchups ({beats, loses_to}), enabled_by, countered_by, notes. When an item change kills or creates a build, update `builds`, not just `notes`. When another hero's change alters a matchup, update `matchups`. Set `last_changed_patch` to "Paint the Town" for heroes that had direct changes. `why` is 1-2 sentences of present-tense state ("strong because X; weak to Y"), not a changelog. `notes` may hold a short changelog line (keep the last 3 lines, newest first). Do not touch heroes not in this batch.

   For each hero, output only the fields whose value actually changes. Omit any field that stays the same — omitted fields are kept as-is in the KB. Include `builds` only if at least one build is created, killed, or its core items change; when you include it, it is a full replacement list. Include `matchups` only if a matchup changes.
2. **change_log**: one line per KB edit you made, for the human to skim.

Tier is one of S/A/B/C/D. Trend is rising/stable/falling.

## Output schema

{
  "hero_updates": {"Hero Name": {"tier": "A", "trend": "falling", "why": "...", "core_items": ["..."], "last_changed_patch": "...", "notes": "..."}},
  "change_log": ["Hero Name: tier S -> A (Card Trick heal nerfs + Veil Walker loss)", "..."]
}
