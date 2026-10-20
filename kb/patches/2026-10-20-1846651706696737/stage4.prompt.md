# Task: synthesis (the verdict and the meta thesis)

Patch: Shh... This Won't Hurt a Bit. (2026-10-20)
Change counts: General 11, Map 13, Items 1, Heroes 8, total 33

## Update summary

A structural map-and-content update rather than a numbers patch: the neutral/jungle layer is rebuilt around new Haunt creatures, four off-lane Districts with their own objectives (Sunken Plaza, Bell Tower, Tough Crates, Steam Vents, Healing Snacks), and a rotating merchant, The Broker, who injects per-match Corrupted items into the economy. Six new heroes arrive on a voted, staggered release schedule, so the meta read is mostly about where souls now come from and which kits can exploit the new map geometry. No hero balance numbers were published, so archetype shifts are inferred from systems, not tuning.

## Previous meta thesis (knowledge base, pre-patch)

# Meta state
Last patch: Paint the Town (2026-10-16)

## Thesis
Games are still won in the map economy, but memorized routes are dead. Souls now come from behavior-varied Haunt camps, contested Soul Bags, permanent-stat Buff Containers and earlier district objectives, so map knowledge and fast-clear kits bank faster than template memorizers. Tempo closes games before late spikes: AoE camp clearers, heavy-melee crate farmers and sustained frontlines carry.

## Economy and systems
- Comeback bounties stay trimmed; extra comeback souls reroute to the two lowest-econ players via tick gold. Leads stick.
- Guardian bounty +10%, Walker +5%, objective share 30->25% (09-16, holds).
- Kill income is contested: the Soul Bag must be last-hit after the kill, so secure-burst conversions are less reliable.
- Objective parries no longer reset the parry cooldown — the free objective-parry chain is gone. T3-bullet-resist picks (Apollo, Mo & Krill) can still commit under a Guardian.
- Respawn 38s at 20m; slows -20% globally, air drag 35% — grounded kiting strong, flyers taxed.
- The Broker spawns ~30 min then ~every 15 min; Corrupted rolls are symmetric and a runtime read.

## Map
Lanes renamed; four districts. Every neutral camp is now one of nine Haunt creature types — they group, chase and hit harder, with souls varying by type. Farm: Tough Crates (58 souls, guaranteed, ~200-300-soul lane routes) need Heavy Melee; Haunt camps; Sinner's Sacrifice variants; Buff Containers now roll permanent stats — Move Speed plus Bullet/Spirit Resist alongside the old ability-range roll — so tanks contest them too. Pickups: Healing Snacks (10% max HP) and Steam Vents (invisibility roams). Hubs: Sunken Plaza (~5-8 min, stamina strip) and Bell Tower (8+, ~280 souls, one rope, three vaults, bell broadcast). Green lane holds a roof/tree above the bridge. Side asymmetry: Arch Mother's side owns Sunken Plaza plus the theater.

## Archetype standing
- AoE/sustain camp clearers: up — grouped, chasing Haunts make AoE the fastest route to income (Seven, Yamato, McGinnis, Infernus).
- Heavy-melee frontline/tanks: up — Tough Crates stay the guaranteed route; Mo & Krill holds the default slot as Billy slips.
- Sustain bruisers: up — harder camps reward regen stacks (Victor, Shiv); Radiant Regeneration's third trim still erodes the shared item.
- Roamers/pick assassins: up slightly — districts, Steam Vents and hiding spots add pick angles (Holliday, Paradox, Drifter).
- Lane bullies: up — crate/hub timings from ~2:30 convert lane pressure (Paige, Apollo).
- Late scalers / split pushers: down — contested Soul Bags and earlier hubs close games before the spike (Warden, Mirage, Celeste, Graves).
- Flyers: down — air drag unchanged, Silver's Bola the answer; Deadman Danny is the test of whether raw numbers beat the tax.
- Non-melee assassins: down — Calico's cat form still can't heavy-melee the crate economy.

## Watchlist
- Which Haunt types actually pay — soul values and clear difficulty are unstated, so farm-worthiness is a live discovery.
- Six vote-gated new heroes: track pick/win as the rollout schedule runs; day-one data is a lottery.
- Soul Bag pickup rate — does the bounty actually extend fights, or does it shift nothing?
- Buff Container contest rate, especially Move Speed and Bullet Resist rolls.
- Whether tempo closes lobbies before The Broker's ~30-min window, or just relocates the stall to the new hubs.
- Graves snapshot (56.5% WR / 40.9% PR) conflicts with the KB (48.5% / 21%) — recheck.

## Recent history
- Paint the Town (2026-10-16): nine Haunt camp types replace all neutrals, contested Soul Bags, objective-parry cooldown reset removed, permanent-stat Buff Containers, Corrupted tier (incl. Street Brawl), six vote-gated new heroes.
- Minor Update - 10-14-2026: Baba frontline cut; Deadman Danny buff package; Radiant Regeneration third trim.
- Minor Update - 10-05-2026: trooper-speed regression fixed; Rat King and Sinclair trimmed.
- City Never Sleeps: renamed lanes, four districts, Haunt camps replace neutrals, Tough Crate/Broker economy.
- Minor Update - 09-16-2026: tempo patch — comeback souls gutted, on-hit spirit carry killed, flyers taxed.

## Systems analysis

{
 "systems_changed": [
  {
   "system": "Jungle / neutral camps (Haunts)",
   "change_summary": "Every neutral camp is now one of nine named Haunt creature types with its own group/chase/hit behavior, so the camp layer is content, not a timer table. Clear routes, sustain math and camp value must be re-learned per type rather than memorized per spawn.",
   "driving_changes": [
    "Haunts: all neutral camps replaced by new creature types (Specimen, Gutter Ghouls, Barrel Mimics, Past Dues, Stage Hands, Crabbage Pots, Festival Spirit, Shrooms, Underhands) with new behaviors — prior clear routes, timings and sustain math no longer transfer"
   ],
   "magnitude": "major",
   "effect_on_play": "Farm efficiency becomes a kit question (AoE to hit grouped chasers, regen to survive the damage, disengage if a camp turns) instead of a route question. Kits that must single-target or take chip damage per camp fall behind on income without dying loudly."
  },
  {
   "system": "Breakables / crates and boxes",
   "change_summary": "Some breakables are now Barrel Mimics — smashing jungle crates is no longer guaranteed income and can turn into a fight. The 'free souls on the walk between camps' assumption is gone.",
   "driving_changes": [
    "Barrel Mimics: some breakables are now mimics — smashing crates and boxes in the jungle is no longer free souls"
   ],
   "magnitude": "moderate",
   "effect_on_play": "Crate-clearing adds risk to what was a zero-risk income habit, and low-HP clearers get punished for chaining breakables while weak. The payoff skews to kits that can kill a mimic instantly or heal through it."
  },
  {
   "system": "Map / districts",
   "change_summary": "Four off-lane corridors (Theater, Chinatown, Haunted Lot, Plaza) now carry their own content, pulling soul income off the three lanes. The map has more simultaneous farm sites than a five-player team can cover.",
   "driving_changes": [
    "Districts: four off-lane corridors added (Theater, Chinatown, Haunted Lot, Plaza) with their own content — souls are no longer concentrated on the three lanes"
   ],
   "magnitude": "major",
   "effect_on_play": "Lane static-holding loses value; the team that rotates through corridor content banks more and creates more pick angles. It also means fewer bodies per lane, so ganks and collapses arrive from directions old lane reads don't predict."
  },
  {
   "system": "Sunken Plaza (sub-area)",
   "change_summary": "A high-risk sub-area below the Plaza square where stamina drains on descent and outside sound fades — entry is cheap, exit is not. It pays committed kits and taxes low-mobility or disengage-poor ones.",
   "driving_changes": [
    "Sunken Plaza: high-risk sub-area below the Plaza District square; stamina drains as you descend and outside sound fades — taxes low-mobility and disengage-poor kits, pays those who can commit"
   ],
   "magnitude": "moderate",
   "effect_on_play": "It becomes a commitment check: mobile, burst-y kits can farm it and leave, while immobile farmers effectively hand a kill to anyone who follows them down. Stamina drain doubles as a fight-denial tool for whoever arrives first."
  },
  {
   "system": "Bell Tower (vertical objective)",
   "change_summary": "A vertical Chinatown hotspot whose soul payout rings a map-wide bell, converting a farm route into a broadcast gank target. Income and information are now the same action.",
   "driving_changes": [
    "Bell Tower: Chinatown vertical objective; concentrated soul hotspot at the top, but collecting rings the bell map-wide — turns a farm route into a broadcast gank target"
   ],
   "magnitude": "moderate",
   "effect_on_play": "Farming the top is a public commitment, so it wants either a teammate holding the rope or a kit that can escape vertically. It also gives roamers a scheduled convergence point instead of a lucky one."
  },
  {
   "system": "Tough Crates",
   "change_summary": "Heavy-Melee-gated breakables pay extra souls, creating a farm lane lanes cannot contest. Heavy-melee access is now a direct income stat, not just a dueling tool.",
   "driving_changes": [
    "Tough Crates: breakables requiring a Heavy Melee that pay extra souls — rewards heavy-melee access and gives melee-capable kits a farm lane lanes cannot contest"
   ],
   "magnitude": "moderate",
   "effect_on_play": "Frontline and melee bruisers get a guaranteed income floor while ranged glass kits farm slower off the same map. It rewards putting a body in the jungle rather than in lane, which suits tank/frontline tempo."
  },
  {
   "system": "Buff Containers",
   "change_summary": "Golden statues now roll permanent Spirit Resist, Bullet Resist, Ability Range and Move Speed, so the pickup is a permanent-stat draft rather than a heal. Contest value rises for tanks (defensive rolls) and casters (range).",
   "driving_changes": [
    "Buff Containers: revamped golden statues now also roll permanent Spirit Resist, Bullet Resist, Ability Range and Move Speed — not just a damage/health pickup, so permanent-buff contests matter for tanks and casters alike"
   ],
   "magnitude": "major",
   "effect_on_play": "Contesting containers is now worth a rotation and a fight, and the roll itself creates asymmetry — a Bullet Resist roll changes a duel outcome for the rest of the match. It pushes early skirmishing toward the containers instead of the lanes."
  },
  {
   "system": "Healing Snacks",
   "change_summary": "Hidden map pickups give a heal in place, cutting forced base returns during lane phase. Lane uptime rises, and chip damage converts into map pressure less reliably.",
   "driving_changes": [
    "Healing Snacks: hidden pickups scattered around the map for healing in a pinch — reduces forced base returns during lane phase"
   ],
   "magnitude": "minor",
   "effect_on_play": "Poke that would have forced a recall now just moves the opponent to a snack, so sustained lane pressure matters more than one big trade. Suits bullies and sustain kits, hurts pure poke."
  },
  {
   "system": "Steam Vents",
   "change_summary": "Standing on a vent grants invisibility plus small regen — a reusable stealth tile rather than a hero ability. Gank setup and disengage become map skills available to every kit.",
   "driving_changes": [
    "Steam Vents: standing on one grants invisibility and small regen — new gank setup and disengage tool; makes vision and grouped rotations stronger"
   ],
   "magnitude": "moderate",
   "effect_on_play": "Every hero gets a soft escape and an ambush angle, so overextending near a vent is punished and grouped rotations beat solo picks. Vision denial becomes a real cost, favoring teams that travel together."
  },
  {
   "system": "The Broker",
   "change_summary": "A relocating merchant injects Corrupted items into the economy from ~30 minutes, then roughly every 15 minutes, at a per-match location. A mid/late-game contested point is created on a schedule the map does not advertise.",
   "driving_changes": [
    "The Broker: temporary merchant that relocates per match (dark uptown alley, abandoned Chinatown storefront); first stock around 30 minutes, further Corrupted items roughly every 15 minutes after — pulls players to a contested point in the mid/late game"
   ],
   "magnitude": "moderate",
   "effect_on_play": "It gives losing teams a scheduled reason to group and fight, and gives winning teams a place to force a decisive fight — either way the game converges on a known point instead of a PvE race. Corrupted rolls are symmetric, so it's a tempo swing, not a comeback lever."
  },
  {
   "system": "Sinner's Sacrifice timing",
   "change_summary": "The ritual camp no longer runs on a fixed timer, so pre-timing it from memory fails. Camp planning shifts from schedule knowledge to scouting.",
   "driving_changes": [
    "Sinner's Sacrifice: bonus now has variable timings — the ritual is no longer a fixed-timer camp, so pre-timing it is harder"
   ],
   "magnitude": "minor",
   "effect_on_play": "Small, but it removes another memorized timer, which is the patch's recurring theme: you have to look at the map instead of the clock."
  },
  {
   "system": "Input / ability & item cast",
   "change_summary": "Casting fires on button press instead of the next input window — every hero gains a frame of responsiveness on casts, cancels and parries.",
   "driving_changes": [
    "Ability/item cast: fires the instant the button is pressed instead of on the next input window — reaction speed, cancels and clutch parries get tighter for every hero"
   ],
   "magnitude": "moderate",
   "effect_on_play": "Higher-execution play is rewarded: combos land more reliably and clutch parries become a real skill expression. This raises the ceiling on burst and reaction-based kits without changing any number."
  },
  {
   "system": "Parry vs objectives",
   "change_summary": "Parrying an objective no longer resets the parry cooldown, deleting the free defensive reset before a dive. Committing under a Guardian now carries an un-refunded cooldown.",
   "driving_changes": [
    "Parry: successfully parrying objectives no longer resets Parry cooldown — objective-parry stops being a free defensive reset before a fight"
   ],
   "magnitude": "moderate",
   "effect_on_play": "Objective dives and defenses are one-shot decisions: tanks with bullet resist can still commit under a Guardian, but nobody gets a second parry for free. Slightly favors the attacker who forces the parry early."
  },
  {
   "system": "Walkers",
   "change_summary": "Walkers stop firing fireballs after death, so killing one removes the zone immediately rather than after the corpse clears.",
   "driving_changes": [
    "Walkers: no longer keep firing fireballs after dying — diving a Walker you just killed is now safe"
   ],
   "magnitude": "minor",
   "effect_on_play": "Siege sequences get cleaner — kill the Walker, then commit into the space behind it without eating posthumous chip. Small, but it rewards fast conversion after a pick instead of waiting out the corpse."
  },
  {
   "system": "Lanes / callouts",
   "change_summary": "Lanes renamed Broadway (blue), Greenwich (green), York (yellow) with a visual rework — old lane vocabulary and its muscle memory are dated.",
   "driving_changes": [
    "Lanes: renamed Broadway (blue), Greenwich (green), York (yellow) — callouts change with the visual rework; treat old lane knowledge as dated"
   ],
   "magnitude": "minor",
   "effect_on_play": "A short-term coordination tax on every team, and a real edge for stacks that relearn callouts fast. No economic effect beyond early-patch confusion."
  },
  {
   "system": "Hero releases & Street Brawl",
   "change_summary": "Six new heroes ship two per week on a voted order, with voting moved to the Pregame lobby (winning team's votes double) and play earning priority tokens; Street Brawl grants a corrupted item after the Round 5 draft.",
   "driving_changes": [
    "Hero releases: six new heroes, two per week on Tue/Fri 2:00pm PT, first release Oct 2, order decided by vote; voting moved to the Pregame lobby with the winning team's votes counting double, and play earns priority tokens",
    "Street Brawl: corrupted item granted after the Round 5 item draft"
   ],
   "magnitude": "minor",
   "effect_on_play": "A staggered rollout means the roster is unstable week to week, so archetype reads are provisional and day-one pick/win data is noise. Corrupted items enter Brawl at the same mid-point they enter the main mode, keeping that mode's power curve aligned."
  }
 ],
 "tempo_shift": {
  "direction": "toward_tempo",
  "confidence": 0.7,
  "why": "Souls spread across four off-lane corridors, Heavy-Melee Tough Crates and contested Buff Containers reward early rotations and map presence over lane farming, and Healing Snacks plus Steam Vents cut the cost of staying out. The Broker's ~30-minute stock is the counterweight that can stall a game, but the bell-broadcast and container fights resolve earlier."
 },
 "archetype_effects": [
  {
   "archetype": "tank/frontline",
   "direction": "up",
   "magnitude": "major",
   "why": "Heavy-Melee Tough Crates give a guaranteed uncontestable soul route, harder Haunt camps reward sustain stacks, and Buff Container's permanent Bullet/Spirit Resist rolls are tank stats."
  },
  {
   "archetype": "mobile assassin",
   "direction": "up",
   "magnitude": "major",
   "why": "Four off-lane corridors, Steam Vent invisibility and Bell Tower's broadcast gank target hand roamers scheduled pick angles they didn't have on three lanes."
  },
  {
   "archetype": "lane bully",
   "direction": "up",
   "magnitude": "moderate",
   "why": "Healing Snacks remove forced base returns during lane phase, so converted lane pressure sticks instead of resetting on a recall."
  },
  {
   "archetype": "initiator",
   "direction": "up",
   "magnitude": "moderate",
   "why": "Bell Tower rings map-wide and Buff Container contests are permanent-stat fights, giving initiators fixed points to force engagements on."
  },
  {
   "archetype": "support/healer",
   "direction": "up",
   "magnitude": "minor",
   "why": "Grouped rotations beat Steam Vent solos and Healing Snacks supplement in-fight sustain, both favoring a body that enables the group."
  },
  {
   "archetype": "poke/siege",
   "direction": "neutral",
   "magnitude": "minor",
   "why": "Walker fireballs stopping on death and instant casts help conversion, but Healing Snacks blunt the chip damage that poke relies on — roughly a wash."
  },
  {
   "archetype": "spirit carry",
   "direction": "neutral",
   "magnitude": "minor",
   "why": "Buff Container's Ability Range roll helps, but its permanent Spirit Resist roll gives opponents a stacking answer to spirit damage."
  },
  {
   "archetype": "gun carry",
   "direction": "neutral",
   "magnitude": "minor",
   "why": "Bullet Resist and Move Speed rolls on contested containers cut both ways, and The Broker's per-match Corrupted stock adds variance rather than a guaranteed spike."
  },
  {
   "archetype": "burst caster",
   "direction": "up",
   "magnitude": "minor",
   "why": "Casts now fire on button press rather than the next input window, tightening combo execution, and Ability Range is a permanent container roll."
  },
  {
   "archetype": "split pusher",
   "direction": "down",
   "magnitude": "moderate",
   "why": "Souls moving off the lanes into corridors means sidelane pressure converts to less income, and shared map objectives pull the pusher's team elsewhere."
  },
  {
   "archetype": "late scaler",
   "direction": "down",
   "magnitude": "moderate",
   "why": "Corridor souls, contested containers and bell-broadcast fights bank tempo before a late spike; The Broker at ~30 minutes is the only scheduled late-game bailout."
  }
 ],
 "intent_read": "Valve is deleting route memorization: souls move off the three lanes into corridors, sub-areas and behavior-varied Haunt camps, so income comes from reading the map and fitting a kit to the content rather than knowing timers. The Broker and Bell Tower exist to convert farming into announced, contested fights, so games resolve on map pressure instead of a PvE race — and the push is deliberately toward tempo, at the cost of late-scaling identities."
}

## Item analysis

{
 "items": [
  {
   "item": "Corrupted Items",
   "direction": "rework",
   "magnitude": "moderate",
   "summary": "A new late-game gold sink rather than a build slot: you trade an item you already own for a stronger-with-a-downside version, so it changes nothing about early build paths and only taxes the 25-40 minute gold decision. Because every Corrupted item in a lobby rolls the same negative attributes (small magnitude variance), the downside is public information — both teams know exactly which stat is degraded, so the edge goes to whoever's build cares least about that roll, not to whoever bought it first. Whether it is net strong or net weak is unclear (no KB entry, no numbers), so treat this as a low-confidence rework read.",
   "affected_heroes": [],
   "build_shift": "The exchange doesn't move components or add a slot; it competes with sixth-slot completion and counter-item purchases, and it rewards banking souls for the ~30-minute Broker stock — an anti-tempo habit in a patch that otherwise pays you to spend and rotate."
  }
 ],
 "notable_item_stories": [
  "Corrupted Items are a win-more lever: an ahead team converts surplus souls into stacked corrupted upgrades every ~15 minutes, so despite the Broker being a scheduled group-and-fight point for losing teams, the economy gap widens if the ahead team wins that fight.",
  "Since the negative roll is identical for everyone and visible, corrupted items turn into an exploit map — you know which stat your opponents lost and can build or fight into that hole, which favors teams that actually check the roll over teams that just take the upgrade.",
  "The Broker relocates per match and isn't advertised on the map, so the first corrupt is a scouting check; in uncoordinated lobbies the tempo lost hunting the merchant likely exceeds the item's value, which quietly favors stacks."
 ]
}

## Hero analysis (only heroes with direction != neutral)

[
 {
  "hero": "Infernus",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.55,
  "direct_reasons": [],
  "indirect_reasons": [
   "Grouped, chasing Haunt camps are the biggest income route now and his burn AoE clears them without extra items.",
   "Buff Containers roll permanent Spirit Resist, a match-long answer to burn/spirit damage that he cannot strip.",
   "Containers also roll Ability Range and Move Speed, which feeds the Dashfernus spirit line more than the gun line."
  ],
  "build_changes": [
   "Skip Tough Crates entirely \u2014 he has no heavy-melee route; farm grouped camps instead.",
   "In lobbies that stack Bullet/Spirit Resist container rolls, lean on the gun/burn build over pure spirit."
  ],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Camps and containers both like him; his two builds don't change."
 },
 {
  "hero": "Seven",
  "in_notes": false,
  "direction": "up",
  "magnitude": "moderate",
  "confidence": 0.6,
  "direct_reasons": [],
  "indirect_reasons": [
   "Storm Cloud/Static Charge is still the fastest clear of the new behavior-varied Haunt camps \u2014 and camp income is now the main soul route.",
   "Bell Tower and Sunken Plaza force the grouped hub fights his AoE farms best.",
   "The tempo push still ends games before a behind Seven recovers, so this rewards the lead, not the comeback."
  ],
  "build_changes": [
   "Keep the Monster Rounds/Cultist Sacrifice farm opener; corridor camps replace lane static-holding.",
   "Only rope up to Bell Tower with a teammate holding the rope \u2014 the bell is a map-wide gank call."
  ],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Fastest camp clearer in the game, and camps are now where souls live."
 },
 {
  "hero": "Lady Geist",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [],
  "indirect_reasons": [
   "Buff Containers now roll permanent Bullet/Spirit Resist \u2014 frontline stats her regen shell wants for free.",
   "Harder Haunt camps reward her Extra Regen/Mystic Regeneration stack; Tough Crates stay closed to her without a heavy-melee commitment.",
   "Lash and other divers gain from Steam Vents and corridors, and she is still their food."
  ],
  "build_changes": [
   "Regen first stays correct \u2014 camp chip damage is higher than last patch.",
   "Contest Buff Containers; a Bullet Resist roll is worth more to her than any damage roll."
  ],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Tankier from container rolls, still dies to the same dive heroes."
 },
 {
  "hero": "Abrams",
  "in_notes": false,
  "direction": "up",
  "magnitude": "moderate",
  "confidence": 0.6,
  "direct_reasons": [],
  "indirect_reasons": [
   "His melee core gives a cheap Heavy Melee, the only key to Tough Crates (58 souls each) \u2014 an income lane ranged kits cannot contest.",
   "Harder Haunt camps reward his Siphon/melee-lifesteal sustain on the farm route.",
   "Parry no longer resets on objectives: dives on him are one-shot, but his own Guardian-dive loses the free second parry."
  ],
  "build_changes": [
   "Insert a Tough-Crate sweep between camp respawns; his heavy melee makes it free souls.",
   "Keep the Close Quarters/Monster Rounds opener \u2014 it is the same spike as before."
  ],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Heavy melee is now a farm stat, and he owns that route."
 },
 {
  "hero": "McGinnis",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [],
  "indirect_reasons": [
   "Turrets clear the new grouped, chasing Haunt camps without leaving cover.",
   "The objective-parry change punishes dives into her wall/turret zone under a Guardian.",
   "Fights spread across four corridors dilute her static-zone value relative to a three-lane map."
  ],
  "build_changes": [
   "Prioritize turret placement on Sunken Plaza and Bell Tower approaches over lane siege."
  ],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Her turrets farm the new camps; just stop sieging empty lanes."
 },
 {
  "hero": "Paradox",
  "in_notes": false,
  "direction": "up",
  "magnitude": "moderate",
  "confidence": 0.55,
  "direct_reasons": [],
  "indirect_reasons": [
   "Four off-lane districts and Steam-Vent invisibility add fresh Kinetic Carbine pick angles off the lanes.",
   "Barrel Mimics make crate-chaining risky for the low-HP clearers she picks on."
  ],
  "build_changes": [
   "Set picks from Steam Vents and corridors instead of lane brushes; carbine sniper core unchanged."
  ],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "The map finally has hiding spots for her carbine picks."
 },
 {
  "hero": "Dynamo",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.55,
  "direct_reasons": [],
  "indirect_reasons": [
   "Telegraphed Bell Tower and Sunken Plaza fights hand Singularity clean setup windows on grouped teams.",
   "His worst matchups (Billy, Mo & Krill, Abrams) are also up \u2014 the frontline archetype rose with him."
  ],
  "build_changes": [
   "Payoff stays Refresher/Unstoppable double-ult; spend it on hub contests, not lane."
  ],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Grouped fights at objectives are exactly where his ult wins games."
 },
 {
  "hero": "Kelvin",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [],
  "indirect_reasons": [
   "Harder, behavior-varied Haunt camps raise the value of dome sustain on the farm route.",
   "Bell Tower and Sunken Plaza make Frozen Shelter a zone tool at forced objective fights.",
   "Healing Snacks cut the number of forced returns he used to heal teammates through."
  ],
  "build_changes": [
   "Save the dome for the Bell Tower/Plaza contest; snacks cover the between-camp healing."
  ],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "His dome is now worth more at objectives than in lane."
 },
 {
  "hero": "Holliday",
  "in_notes": false,
  "direction": "up",
  "magnitude": "moderate",
  "confidence": 0.6,
  "direct_reasons": [],
  "indirect_reasons": [
   "Four off-lane corridors plus Steam Vent invisibility expand her roam routes beyond the old lanes.",
   "Bell Tower's top payout rings map-wide, which is a scheduled gank spot for a lasso pick."
  ],
  "build_changes": [
   "Pre-place bounce-pad exits near the Bell Tower rope before roping; lasso the farmer, not the escort."
  ],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "More routes and a broadcast target \u2014 her kind of map."
 },
 {
  "hero": "Bebop",
  "in_notes": false,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [],
  "indirect_reasons": [
   "A single-target hook converts nothing on a spread-out corridor farm route \u2014 there is no lane body to punish.",
   "Paradox keeps the roamer slot and the new districts and Steam Vents give her pick angles a hook cannot match.",
   "Steam Vents give every target a free disengage his combo cannot chase."
  ],
  "build_changes": [
   "Hook off corridor chokepoints and camp entrances instead of lane."
  ],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Hooks still land, but nothing in the new economy punishes a farm route."
 },
 {
  "hero": "Calico",
  "in_notes": false,
  "direction": "up",
  "magnitude": "moderate",
  "confidence": 0.55,
  "direct_reasons": [],
  "indirect_reasons": [
   "Districts and Steam Vent invisibility sharpen the tempo roam the no-comeback economy already rewards.",
   "Cat form still cannot Heavy Melee, so Tough Crates stay closed \u2014 her income must come from kills and corridors.",
   "The frontline archetype rose, giving her more bodies she cannot burst (Abrams, Rat King)."
  ],
  "build_changes": [
   "Lean kills and off-map souls; ignore Corrupted items, they are a late gold sink she should not bank for."
  ],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Better roam angles, same locked-out crate route."
 },
 {
  "hero": "Grey Talon",
  "in_notes": false,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [],
  "indirect_reasons": [
   "Steam Vents give roamers free invisibility against a sub-50%-WR immobile flyer.",
   "Healing Snacks blunt the chip damage his poke converts into lane leads.",
   "Air-drag slow and Silver's Weighted Bola are unchanged, and neither camp routes nor crates suit him."
  ],
  "build_changes": [],
  "tier_before": "C",
  "tier_after": "C",
  "one_liner": "Poke carries keep losing value; the map keeps giving divers more ways in."
 },
 {
  "hero": "Mo & Krill",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.55,
  "direct_reasons": [],
  "indirect_reasons": [
   "Sustained frontline is what harder Haunt camps and contested Buff Containers reward.",
   "Objective parries no longer reset, so his Guardian-dive chain is now one-shot.",
   "Ranged poke he cannot close on still beats him, and that is unchanged."
  ],
  "build_changes": [
   "Frontline the Buff Container contests; a Bullet Resist roll compounds with his T3."
  ],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Default front line for a patch that pays for standing in camps."
 },
 {
  "hero": "Shiv",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.45,
  "direct_reasons": [],
  "indirect_reasons": [
   "Harder camps reward his regen stack, and the rising frontline feeds current-HP Serrated Knives.",
   "Steam Vents hand divers a free approach on a hero who needs regen ramp time before he is unkillable."
  ],
  "build_changes": [],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Anti-tank is still the right job; the camp damage just helps him ramp."
 },
 {
  "hero": "Ivy",
  "in_notes": false,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.45,
  "direct_reasons": [],
  "indirect_reasons": [
   "Healing Snacks plus spread corridors reduce the value of a dedicated healer who wants the team grouped.",
   "Districts pull her team apart, so a single tether covers less of the map than on three lanes.",
   "Her frontline partners (Abrams, Billy) are up, which is the one thing going her way."
  ],
  "build_changes": [
   "Tether to a frontline bruiser sweeping corridors rather than a lane partner."
  ],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Still the best peel in the game, but the map now punishes grouping less."
 },
 {
  "hero": "Warden",
  "in_notes": false,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.45,
  "direct_reasons": [],
  "indirect_reasons": [
   "Steam Vents give every hero the invis-engage he pays Shadow Weave for, flattening his one unique tool.",
   "Tempo still ends games before his late gun spike, and no item or system route slows that."
  ],
  "build_changes": [
   "Shadow Weave stays the engage shell, but it no longer buys exclusivity."
  ],
  "tier_before": "C",
  "tier_after": "C",
  "one_liner": "Everyone gets a free invis now; his late spike still arrives too late."
 },
 {
  "hero": "Yamato",
  "in_notes": true,
  "direction": "up",
  "magnitude": "moderate",
  "confidence": 0.55,
  "direct_reasons": [
   "Flying Strike now creates paths against solid targets (turrets, Shrines, objectives) \u2014 objective-adjacent ults stop whiffing and she gets a second mobility vector."
  ],
  "indirect_reasons": [
   "Her punch AoE remains the fastest clear of the grouped, behavior-varied Haunt camps.",
   "Parry no longer resets on objectives, so her Shrine/Walker dive is one-shot \u2014 plan the exit before committing."
  ],
  "build_changes": [
   "Use Flying Strike off a Walker or Guardian to path out, not only to engage."
  ],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Free pathing off objectives plus the best camp clear: closest thing to S."
 },
 {
  "hero": "Lash",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.55,
  "direct_reasons": [],
  "indirect_reasons": [
   "Districts and Steam Vents extend his dive routes beyond the three lanes.",
   "Bell Tower and Sunken Plaza concentrate teams into exactly his Ground Strike setup.",
   "The objective-parry change removes the free defensive reset from the fights he starts."
  ],
  "build_changes": [
   "Rotate corridors between stomps \u2014 roam income replaces lane pressure."
  ],
  "tier_before": "S",
  "tier_after": "S",
  "one_liner": "More places to dive from, same stomp."
 },
 {
  "hero": "Viscous",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.4,
  "direct_reasons": [],
  "indirect_reasons": [
   "Bell Tower's spread vaults and four corridors suit Goo Ball traversal and escapes.",
   "Harder camps reward Cube sustain, and forced hub fights raise Cube rescue value."
  ],
  "build_changes": [
   "Hold Cube for the Buff Container or Bell Tower contest, not lane trades."
  ],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Cube rescue is worth more when fights are scheduled at objectives."
 },
 {
  "hero": "Mirage",
  "in_notes": false,
  "direction": "down",
  "magnitude": "moderate",
  "confidence": 0.5,
  "direct_reasons": [],
  "indirect_reasons": [
   "Split-push loses its payoff \u2014 souls moved off the lanes into corridors and shared objectives, so sidelane pressure converts to less income.",
   "Steam Vent invisibility hands roamers a free approach on his map-play."
  ],
  "build_changes": [
   "Farm corridors instead of shoving a lane; Djinn's Mark picks isolated camp clearers."
  ],
  "tier_before": "B",
  "tier_after": "C",
  "one_liner": "The patch deleted lane-pushing as an income strategy."
 },
 {
  "hero": "Vyper",
  "in_notes": false,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.4,
  "direct_reasons": [],
  "indirect_reasons": [
   "Buff Containers roll permanent Bullet Resist, a match-long tax on a pure-gun carry.",
   "Barrel Mimics punish close-range crate-chaining while low on a hero with no disengage."
  ],
  "build_changes": [
   "Nothing to swap; the pure-gun pivot is worse into resist rolls, not better."
  ],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Every container roll of Bullet Resist is a small loss for her."
 },
 {
  "hero": "Mina",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [],
  "indirect_reasons": [
   "Grouped Haunt camps suit her AoE clear, and the new districts give her dive routes.",
   "The tank/frontline archetype rose, and tanks are her worst matchups."
  ],
  "build_changes": [
   "Dive corridor farmers between camps; skip crates, she has no heavy-melee route."
  ],
  "tier_before": "C",
  "tier_after": "C",
  "one_liner": "The camps love her; the tanks she cannot kill got better."
 },
 {
  "hero": "Drifter",
  "in_notes": false,
  "direction": "up",
  "magnitude": "moderate",
  "confidence": 0.6,
  "direct_reasons": [],
  "indirect_reasons": [
   "Steam Vents and the new hiding spots fit his stealth-reveal roam exactly.",
   "Heavy-Melee Tough Crates give his melee core the same uncontestable soul lane the tanks got.",
   "The frontline archetype rose, though so did his counters Dynamo and Mo & Krill."
  ],
  "build_changes": [
   "Sweep Tough Crates between roams; Stalker stays the first buy."
  ],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Melee bruiser with a private income lane and free hiding spots."
 },
 {
  "hero": "Venator",
  "in_notes": true,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.55,
  "direct_reasons": [
   "Graves' gun now destroys his traps, turning a C-tier pick into a direct counter into his zoning."
  ],
  "indirect_reasons": [
   "Buff Containers' permanent Bullet Resist roll taxes a gun-bruiser carry for the whole match.",
   "Spread corridors and Steam Vents add flank angles on a slow tanky gunner."
  ],
  "build_changes": [
   "Against a Graves, hold traps for fight setup instead of pre-placing them as lane vision."
  ],
  "tier_before": "A",
  "tier_after": "B",
  "one_liner": "Trap zoning now has a hero who deletes traps, and he is popular."
 },
 {
  "hero": "Victor",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.55,
  "direct_reasons": [],
  "indirect_reasons": [
   "Harder, behavior-varied Haunt camps and longer PvE routes feed his Spirit Lifesteal/Healing Booster stack.",
   "Buff Containers' Bullet/Spirit Resist rolls are frontline stats he gets for contesting."
  ],
  "build_changes": [
   "Contest containers; keep the High-Velocity Rounds/Opening Rounds weapon start."
  ],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Camp damage went up; his sustain stack went up with it."
 },
 {
  "hero": "Paige",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.55,
  "direct_reasons": [],
  "indirect_reasons": [
   "Healing Snacks let her lane pressure stick instead of resetting on an opponent's recall.",
   "Lane-adjacent crate routes from ~2:30 keep the tempo lead she builds in lane."
  ],
  "build_changes": [
   "Convert the lane win into corridor crate routes rather than a sidelane shove."
  ],
  "tier_before": "S",
  "tier_after": "S",
  "one_liner": "Wins lane, and the new map pays lane winners immediately."
 },
 {
  "hero": "The Doorman",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [],
  "indirect_reasons": [
   "Bell Tower's single rope and ~280-soul payout give Doorway a real kidnap play on the top platform.",
   "The dive archetype is up (Yamato, Lash, Holliday) and still reaches him before Cart/Doorway set up."
  ],
  "build_changes": [
   "Pre-place the door at the Bell Tower base before roping up."
  ],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Bell Tower is a kidnap setup with his name on it."
 },
 {
  "hero": "Billy",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.4,
  "direct_reasons": [],
  "indirect_reasons": [
   "Harder Haunt camps and sustained presence reward the frontline archetype he lives in.",
   "The front-line slot still reads Mo & Krill, and ranged corridor clear beats his all-in."
  ],
  "build_changes": [],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Frontline patch, but he is still the second-best front line."
 },
 {
  "hero": "Graves",
  "in_notes": true,
  "direction": "up",
  "magnitude": "moderate",
  "confidence": 0.6,
  "direct_reasons": [
   "Her gun now destroys Venator's traps, making her a genuine counter-pick into a 40%-pick-rate A-tier hero."
  ],
  "indirect_reasons": [
   "Split-push and late-scaling both got worse: souls moved into corridors and shared objectives, away from the sidelanes she pressed.",
   "Barrel Mimics punish a low-HP, two-stamina carry chaining breakables."
  ],
  "build_changes": [
   "Draft her into Venator specifically; skip risky crate chains while low.",
   "Corrupted items at ~30 minutes are her only realistic late power spike \u2014 bank for the Broker."
  ],
  "tier_before": "C",
  "tier_after": "B",
  "one_liner": "Finally a reason to pick her: she deletes Venator's traps."
 },
 {
  "hero": "Apollo",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [],
  "indirect_reasons": [
   "His lane-bully pressure now converts into lane-adjacent crate routes and Healing Snacks.",
   "The objective-parry change trims his T3-bullet-resist Guardian dive chain to one shot.",
   "Frontline archetype up and his spirit core untouched."
  ],
  "build_changes": [
   "Dive Guardians as a one-shot decision; there is no free second parry."
  ],
  "tier_before": "S",
  "tier_after": "S",
  "one_liner": "Still a lane bully, but his free Guardian dive is gone."
 },
 {
  "hero": "Rem",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.4,
  "direct_reasons": [],
  "indirect_reasons": [
   "Harder camps raise the value of a percent-max-HP heal on the farm route.",
   "Healing Snacks cheapen the dedicated healing he sells, and the tank partners who benefit are up."
  ],
  "build_changes": [
   "Shadow a frontline bruiser through corridors rather than sitting in a lane."
  ],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Sustain matters more, but snacks do part of his job for free."
 },
 {
  "hero": "Celeste",
  "in_notes": false,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.45,
  "direct_reasons": [],
  "indirect_reasons": [
   "Flyer tax is intact (air-drag slow, Weighted Bola) while fights concentrate at the vertical Bell Tower.",
   "Late-scaling burst is exactly the profile a tempo patch punishes; Barrel Mimics punish squishy clearers too."
  ],
  "build_changes": [
   "Witchmail stays the anti-slow answer; do not rope up alone."
  ],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Flying late scaler in a grounded, early-fight patch."
 },
 {
  "hero": "Rat King",
  "in_notes": true,
  "direction": "up",
  "magnitude": "moderate",
  "confidence": 0.55,
  "direct_reasons": [],
  "indirect_reasons": [
   "His 116 heavy-melee open still cracks Tough Crates for guaranteed ~58 souls each \u2014 an uncontestable income route.",
   "Scrap Grenade AoE clears the grouped, chasing Haunt camps and the corridors between them.",
   "Sunken Plaza and Bell Tower force the grouped fights his banner ult was built for."
  ],
  "build_changes": [
   "Open the same heavy-melee/HP line and sweep crates before the first camp."
  ],
  "tier_before": "A",
  "tier_after": "S",
  "one_liner": "The map was rebuilt around heavy melee, camp AoE and forced fights \u2014 his kit."
 },
 {
  "hero": "Baba",
  "in_notes": true,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.45,
  "direct_reasons": [],
  "indirect_reasons": [
   "Her melee-regen stack still clears Tough Crates and grouped Haunt camps, the two new income routes.",
   "Grounded bruisers gain from the air-drag slow, and forced hub fights suit her AoE hex and silence.",
   "The 10-14 barrier/resist cuts are unchanged \u2014 this patch adds fit, not power."
  ],
  "build_changes": [
   "Buy Healing Booster/Spirit Resilience earlier and stop counting on out-tanking focus."
  ],
  "tier_before": "C",
  "tier_after": "C",
  "one_liner": "The new map suits her kit; the barrier nerf still does not."
 },
 {
  "hero": "Solomon",
  "in_notes": true,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.4,
  "direct_reasons": [],
  "indirect_reasons": [
   "Telegraphed Bell Tower and Sunken Plaza fights reward his Bishop/Rook zone control.",
   "The dive archetype is up (Yamato, Lash, Holliday) and still lands before his zones are placed."
  ],
  "build_changes": [
   "Set zones on the Bell Tower rope and container spawns, not lanes."
  ],
  "tier_before": "C",
  "tier_after": "C",
  "one_liner": "Scheduled fights help him; the heroes that skip his zones are still strong."
 },
 {
  "hero": "Deadman Danny",
  "in_notes": true,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.4,
  "direct_reasons": [],
  "indirect_reasons": [
   "Spirit AoE marks suit the grouped, chasing Haunt camps that now carry the income.",
   "Bell Tower and Plaza reward mark-then-dive on stacked teams.",
   "The flyer tax is intact and Barrel Mimics punish a 730-HP commit."
  ],
  "build_changes": [
   "Farm grouped camps, not crates; keep High-Velocity Rounds as the only weapon staple."
  ],
  "tier_before": "C",
  "tier_after": "C",
  "one_liner": "His mark burst likes stacked camps; the air tax still eats him."
 },
 {
  "hero": "Violet",
  "in_notes": true,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.35,
  "direct_reasons": [],
  "indirect_reasons": [
   "A 116 heavy-melee open lets her farm Tough Crates and grouped camps like a frontline.",
   "Buff Container and Bell Tower contests are where her silence zone decides the fight.",
   "Steam Vents give dive assassins a free approach on a 710-HP caster with no escape."
  ],
  "build_changes": [
   "Spirit plus cooldown only \u2014 the High-Velocity Rounds gun line sits at ~28% WR."
  ],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Her kit was quietly built for the new map, if she survives the dive."
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
