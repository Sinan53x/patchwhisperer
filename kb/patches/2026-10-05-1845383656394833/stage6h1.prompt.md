# Task: update hero knowledge-base entries after this patch

Patch: Minor Update - 10-05-2026 (2026-10-05)

## Synthesis

{
 "patch_size": "minor",
 "size_why": "The defining move is a regression repair (trooper speed restored) plus targeted trims to two outliers (Rat King, Sinclair); there are no systems, economy, objective, or item changes, so the way games are won is untouched. Twenty-five line items sounds broad, but they cluster as tuning/fixes, not structural shifts.",
 "headline": "A regression-repair patch: lane wave tempo is fixed and two outliers are trimmed, but the map-economy lead engine is deliberately left alone.",
 "meta_thesis": {
  "previous": "Games are won in the map economy — guaranteed Tough Crate routes, Haunt camp farming and telegraphed hub fights — not the lane, with no comeback valve and late scalers only relieved by The Broker's ~30-min stall window.",
  "new": "The shape is unchanged: the map-economy lead engine still decides games, and this patch only restores intended lane wave cadence and trims two outliers. Restored trooper speed marginally re-weights the lane versus camp farming, but no economy, objective, item or comeback lever moved.",
  "relationship": "continuation",
  "why": "Drivers are the trooper-speed regression fix (restores baseline lane cadence, not a new tempo lever) and the Rat King/Sinclair kit trims; nothing touches souls, bounties, objectives or The Broker."
 },
 "winners": [
  {
   "hero": "Apollo",
   "why": "On-schedule wave crashes restore his lane-bully punish windows, and Rat King's frontline trim thins the competing A-tier bruiser pool.",
   "indirect": true
  },
  {
   "hero": "Paige",
   "why": "Lane-cadence fix maximizes the wave pressure her tempo-support identity trades on; still S.",
   "indirect": true
  },
  {
   "hero": "Billy",
   "why": "Restored wave timing helps his lane-bully all-in, though his real slide (slot lost to Mo & Krill) is unchanged.",
   "indirect": true
  },
  {
   "hero": "Mirage",
   "why": "Reliable trooper pathing lets split-push side-lane pressure convert on schedule instead of stalling.",
   "indirect": true
  }
 ],
 "losers": [
  {
   "hero": "Rat King",
   "why": "Banner ult gutted — cooldown 130->160, DR 20->15%, radius 24->20m, charge 12->10s, plus T1/T2/T3 talent strips (total DR 35->25%) — hitting the 61% WR outlier.",
   "indirect": false
  },
  {
   "hero": "Sinclair",
   "why": "Broad trim across lane, utility and ult — HP regen 2->1, gun falloff and bullet damage down, Rabbit Hex radius down, ult copy duration 12->9s / cooldown 40%->60%, Vexing Bolt halved on objectives.",
   "indirect": false
  },
  {
   "hero": "Sinclair duration build",
   "why": "With Hex radius and copy duration both cut, the duration-spirit build now leans entirely on stealing a strong enemy kit to function.",
   "indirect": false
  }
 ],
 "non_obvious_calls": [
  {
   "claim": "The trooper 'bug fix' is effectively a partial, unintended walk-back of the City Never Sleeps lane de-emphasis — it re-weights lane tempo upward against camp farming.",
   "why": "Restoring wave-crash timing re-opens dive/punish windows, benefiting lane bullies and split pushers the KB had ranked below AoE camp clearers.",
   "confidence": 0.45
  },
  {
   "claim": "Rat King stays A-tier despite the ult gutting; don't move him down a tier.",
   "why": "Base-kit buffs (Scrap Grenade 65->70, Rat Swarm 28->24s, bounce targeting fixed) offset the banner nerf, so this is a correction toward 50%, not a burial.",
   "confidence": 0.55
  },
  {
   "claim": "The quiet kill in this patch is Sinclair's Vexing Bolt doing half damage to objectives — a kit-steal pick's only structure pressure removed.",
   "why": "He was already C-tier per the KB; stripping objective damage leaves the pick with almost no win-condition beyond stealing a meta kit.",
   "confidence": 0.5
  },
  {
   "claim": "The single largest number swing here is Rat King's total banner DR going 35->25%, a team-fight-identity nerf, not a solo-stat trim.",
   "why": "Base 20->15% plus T3 15->10% compounds to a 10-point swing, hitting the AoE damage-reduction aura his comp play revolved around.",
   "confidence": 0.6
  }
 ],
 "uncertainties": [
  "The summary reports 25 general changes but only the trooper fix and two hero kits surfaced — other tuning may have landed unlisted.",
  "Whether the trooper speed fix over-corrects to faster-than-baseline waves rather than restoring the intended cadence.",
  "Whether Rat King's nerf is large enough to move a 61% WR toward 50% or just trims the ceiling.",
  "Whether Sinclair was already weak enough that this is a correction or a full burial, since no snapshot WR was given."
 ],
 "what_to_watch": [
  "Rat King win rate post-patch — does it fall below ~55%, validating the nerf?",
  "Sinclair pick rate — near-zero confirms the kit-steal slot is dead.",
  "Lane-phase dive/kill stats vs camp-farm souls — did restoring wave speed actually re-raise lane-bully WRs?",
  "Any follow-up hotfix to Tough Crates, still the KB's flagged farm-route risk."
 ]
}

## Item analysis

{
 "items": [],
 "notable_item_stories": []
}

## Hero analysis (this batch only)

[
 {
  "hero": "Rat King",
  "in_notes": true,
  "direction": "down",
  "magnitude": "moderate",
  "confidence": 0.55,
  "direct_reasons": [
   "Rule, Ratannia! gutted: cooldown 130->160, damage reduction 20->15%, radius 24->20m, charge duration 12->10s.",
   "Ult talents stripped: T1 loses -20s cooldown, T2 loses +8s charge, T3 DR 15->10% (total DR 35->25%).",
   "Bonus move speed no longer scales with Spirit, devaluing any spirit stacking for the banner.",
   "Base kit buffed: Scrap Grenade 65->70 (T2 too), Rat Swarm cooldown 28->24s, grenade bounce targeting fixed."
  ],
  "indirect_reasons": [
   "Trooper speed fix restores on-schedule wave crashes for his lane-bully archetype (minor)."
  ],
  "build_changes": [
   "Gun bruiser core unchanged and slightly favored (grenade +5, swarm -4s CD); drop any spirit-stack-for-ult-movespeed plan."
  ],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Banner ult is far weaker and base kit tweaked up; still strong, and the 61% WR was the target."
 },
 {
  "hero": "Sinclair",
  "in_notes": true,
  "direction": "down",
  "magnitude": "moderate",
  "confidence": 0.55,
  "direct_reasons": [
   "Base HP regen 2->1 and gun falloff 25-61->20-60 (also on Spectral Assistant) cut lane sustain and range.",
   "Bullet base damage 17.76->16.5 weakens both the gun-hybrid lane and assistant poke.",
   "Rabbit Hex radius 6.5->6m and T3 +3->+2m shrink the duration build's utility.",
   "Audience Participation copy duration 12->9s and copied cooldown 40%->60% blunt his kit-steal win-condition.",
   "Vexing Bolt now does half damage to objectives, cutting structure pressure."
  ],
  "indirect_reasons": [],
  "build_changes": [
   "Spirit Duration build now leans harder on stealing a strong enemy kit; value the gun-hybrid lane opener less."
  ],
  "tier_before": "C",
  "tier_after": "C",
  "one_liner": "Broad trim to an already-weak kit-steal pick; lane, utility and ult all worse."
 },
 {
  "hero": "Paige",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.45,
  "direct_reasons": [],
  "indirect_reasons": [
   "Trooper speed fix restores lane cadence, and her tempo-support identity trades on lane pressure (KB lane bully)."
  ],
  "build_changes": [],
  "tier_before": "S",
  "tier_after": "S",
  "one_liner": "No direct change; lane-cadence fix marginally helps her already-top lane pressure."
 },
 {
  "hero": "Billy",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.4,
  "direct_reasons": [],
  "indirect_reasons": [
   "Trooper fix restores wave timing that his lane-bully all-in depends on."
  ],
  "build_changes": [],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Marginal lane-cadence help; his real slide (slot lost to Mo & Krill) is unchanged."
 },
 {
  "hero": "Apollo",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.4,
  "direct_reasons": [],
  "indirect_reasons": [
   "Trooper fix restores lane crash timing for his lane-bully pressure."
  ],
  "build_changes": [],
  "tier_before": "S",
  "tier_after": "S",
  "one_liner": "No change; lane-cadence fix trims a hair off his lane edge, still top-frontline."
 },
 {
  "hero": "Mirage",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.4,
  "direct_reasons": [],
  "indirect_reasons": [
   "Trooper fix restores intended wave pathing, so pushed side-lane pressure converts on schedule for a split pusher."
  ],
  "build_changes": [],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Tiny split-push QoL from the trooper fix; the tempo economy still buries his scaling."
 },
 {
  "hero": "Graves",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.35,
  "direct_reasons": [],
  "indirect_reasons": [
   "Trooper fix restores wave pathing for her split-push line."
  ],
  "build_changes": [],
  "tier_before": "C",
  "tier_after": "C",
  "one_liner": "Marginal split-push help; her no-comeback early game is still the problem."
 }
]

## Current hero entries (this batch only)

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
  last_changed_patch: null
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
Paige:
  name: Paige
  role: lane-winning support
  archetypes:
  - support/healer
  - lane bully
  tier: S
  trend: rising
  why: Lane-winning support whose pressure now converts straight into the patch's
    early crate routes and Healing Snacks; she wins lane, then snowballs a carry before
    trimmed comeback souls can rescue the enemy. 52.7% WR / 29.2% PR, near-even into
    Rem/Ivy caps her dominance.
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
  - guaranteed crate routes from ~2:30 + Healing Snacks
  countered_by:
  - burst assassins (Yamato, Lash, Holliday)
  - Rem
  - Ivy
  - anti-heal (healing-item trims)
  last_changed_patch: Minor Update - 09-16-2026
  notes: '09-29 City Never Sleeps: no direct change; lane-adjacent crate routes and
    Healing Snacks reward her lane pressure, and the contested hubs suit her carry-snowball
    (peercontent).

    Changelog: 09-16 - heavy-melee spirit scaling 0.3->0.45, Captivating Read T1 -11->-14s
    / T3 +1m->+2m; Slowing Hex cd 27->29s is a minor tax.

    Data check: old core items Healing Tempo and Fortitude do not appear in the 30-day
    usage list - replaced by the real early-gun-into-spirit core. Knockdown is a below-average
    buy (50.8% WR vs 52.7%).'
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
Billy:
  name: Billy
  role: tank/frontline
  archetypes:
  - tank/frontline
  - lane bully
  tier: A
  trend: falling
  why: 'Lobby-default frontline whose lane-bully all-in the map-economy patch suits
    less: the crate/camp meta wants sustained uptime, and his front-line slot has
    visibly moved to rising Mo & Krill. Anti-tank Shiv remains his worst lane and
    is climbing, so he slides off S.'
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
  notes: '09-29 City Never Sleeps: no direct change; the crate/camp-uptime meta wants
    sustained presence and his front-line slot moved to rising Mo & Krill, with anti-tank
    Shiv climbing - S was popularity-supported, so slides to A (peercontent, unverified).

    Changelog: 09-16 - no direct line; item tailwinds (Lifestrike heal/slow, Fortitude
    regen) and the lane-wins meta supported him.

    Data beats creators: Lifestrike, Echo Shard, Witchmail and Scourge/Scrooge never
    appear in his top-15 buys - real core is Spirit Snatch (95%), Stalker (90%), Close
    Quarters (88%), Monster Rounds (86%), Grit (83%).'
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
Apollo:
  name: Apollo
  role: lane bully initiator
  archetypes:
  - lane bully
  - initiator
  - tank/frontline
  tier: S
  trend: rising
  why: 'Tempo lane bully the map-economy patch still favors: he routes crate paths
    and roams, and with T3 bullet resist is one of the few who can still commit under
    a Guardian after the parry-cooldown change. Spirit core untouched - only his Locket
    sustain line was trimmed. 49.3% WR is a pre-patch baseline.'
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
  - tower-dive still open with T3 bullet resist vs the parry-cooldown change
  countered_by:
  - Lash
  - Abrams
  - Mo & Krill
  - Warden
  - anti-heal vs his Locket/heal sustain
  last_changed_patch: Minor Update - 08-12-2026
  notes: '09-29 City Never Sleeps: no direct change; the parry-cooldown change removes
    tower-diving for most of the roster, making his T3 bullet resist a real outlier
    advantage, and crate/roam routing suits him (peercontent).

    09-16: no direct changes - structural economy/Rift shifts favor his tempo; the
    Restorative Locket nerf dents only his support line.

    Old core_items (Fortitude) had zero usage; data says pure spirit, so reworked
    to Extra Spirit/Mystic Burst/Improved Spirit cores.'
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
Rat King:
  name: Rat King
  role: frontline brawler
  archetypes:
  - tank/frontline
  - lane bully
  tier: A
  trend: rising
  why: 'Rat King slots directly into the City Never Sleeps economy: 116 heavy melee
    plus 800 HP and 2.0 regen open Tough Crate routes, and Scrap Grenade''s multi-detonation
    clears the grouped, chasing Haunt camps. His banner ult converts the patch''s
    forced hub fights into favorable ones (move speed, slow immunity, damage reduction),
    while Rat Swarm strips bullet resist for his Spreadshot. The 59.4% first-week
    WR is novelty-inflated, but the kit-to-map fit justifies a provisional A.'
  core_items:
  - High-Velocity Rounds
  - Close Quarters
  - Extra Regen
  - Enduring Speed
  - Witchmail
  build_variants:
  - Gun bruiser
  - Vitality frontline
  - Swarm shred
  enabled_by:
  - "Grouped, chasing Haunt camps that reward AoE clear \u2014 Scrap Grenade multi-detonation"
  - "Tough Crate routes needing heavy melee \u2014 116 heavy melee, 800 HP, 2.0 regen"
  - "Forced hub fights at Sunken Plaza/Bell Tower \u2014 banner ult (move speed, slow\
    \ immunity, DR)"
  - "Gun-carry meta \u2014 Rat Swarm bullet-resist shred sets up Spreadshot"
  countered_by:
  - Spirit burst (barrier is anti-bullet and gains no resists)
  - Mobility/dashes that shake off rats and kill the shred
  - Silence and CC (Silence Wave, Silencer) denying banner and barrier
  - Anti-heal (Healbane, Decay) against his regen stacking
  last_changed_patch: Listen up, Crumbums! Your King is here.
  notes: "Day-0 kit read (2026-10-03), provisional \u2014 data check-in due 2026-10-09.\n\
    First-week 59.4% WR / 8.5% PR is novelty-inflated; the crate/camp/hub fit is the\
    \ reason to start at A, not the raw WR. Raise if he holds >52% with a settled\
    \ gun build; drop if swarm/vitality builds and spirit-burst counters dominate.\
    \ A Tough Crate hotfix (on the meta watchlist) would cut his farm-route value."
  builds:
  - name: Gun bruiser
    damage: gun
    core_items:
    - High-Velocity Rounds
    - Close Quarters
    - Extended Magazine
    - Ballistic Enchantment
    - Enduring Speed
    popularity: primary
    notes: Rat Swarm strips bullet resist, then Spreadshot and grenades do the work;
      HVR is the 78% default yet wins least (47%).
  - name: Vitality frontline
    damage: hybrid
    core_items:
    - Extra Regen
    - Fortitude
    - Extra Health
    - Enduring Speed
    - Witchmail
    popularity: secondary
    notes: Bulks up to lead the banner charge; Witchmail late is the standout signal
      (24% pick, 82% WR, small sample).
  - name: Swarm shred
    damage: spirit
    core_items:
    - Mystic Expansion
    - Bullet Resist Shredder
    - Extra Spirit
    popularity: niche
    notes: Leans on Rat Swarm T3 (-1 resist, +8 per bite); under-represented in the
      early item data.
  matchups:
    beats:
    - Haze
    - Wraith
    - Venator
    loses_to:
    - Celeste
    - Mina
    - Holliday
  matchup_notes: Royal Pestments (bullet deflect) plus Rat Swarm's bullet-resist shred
    make gun carries and grouped hub comps his best matchups, and the banner's slow
    immunity blunts slow-based kits. His real answers are spirit burst that ignores
    the anti-bullet barrier and dashes that shake off rats, so he is soft to mobile
    assassins and casters rather than to other gun heroes. Plated Armor is a weaker
    answer against him than against most gun carries because his swarm shreds the
    bullet resist it grants.
  confidence: 0.4


## What to do

Produce the post-patch knowledge base state for the heroes in this batch. This KB is read by the analyst on the *next* patch, so write it as durable state, not as a patch summary.

1. **hero_updates**: for each mover, the fields that changed. Allowed fields: role, archetypes, tier, trend, why, core_items, builds (full replacement list of {name, damage, core_items, popularity, notes}), matchups ({beats, loses_to}), enabled_by, countered_by, notes. When an item change kills or creates a build, update `builds`, not just `notes`. When another hero's change alters a matchup, update `matchups`. Set `last_changed_patch` to "Minor Update - 10-05-2026" for heroes that had direct changes. `why` is 1-2 sentences of present-tense state ("strong because X; weak to Y"), not a changelog. `notes` may hold a short changelog line (keep the last 3 lines, newest first). Do not touch heroes not in this batch.

   For each hero, output only the fields whose value actually changes. Omit any field that stays the same — omitted fields are kept as-is in the KB. Include `builds` only if at least one build is created, killed, or its core items change; when you include it, it is a full replacement list. Include `matchups` only if a matchup changes.
2. **change_log**: one line per KB edit you made, for the human to skim.

Tier is one of S/A/B/C/D. Trend is rising/stable/falling.

## Output schema

{
  "hero_updates": {"Hero Name": {"tier": "A", "trend": "falling", "why": "...", "core_items": ["..."], "last_changed_patch": "...", "notes": "..."}},
  "change_log": ["Hero Name: tier S -> A (Card Trick heal nerfs + Veil Walker loss)", "..."]
}
