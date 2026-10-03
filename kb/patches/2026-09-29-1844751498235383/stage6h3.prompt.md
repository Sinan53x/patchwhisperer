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

## Current hero entries (this batch only)

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
  last_changed_patch: null
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
  released_on: null
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
  released_on: null
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
  released_on: null
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
  released_on: null
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
  released_on: null
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
  released_on: null
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
  released_on: null
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
