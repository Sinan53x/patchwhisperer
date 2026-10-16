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

## Current hero entries (this batch only)

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
  notes: '10-05: no direct change; the trooper-speed fix marginally helps his lane-bully
    all-in, but his real slide (front-line slot lost to rising Mo & Krill, anti-tank
    Shiv climbing) is unchanged.


    09-29 City Never Sleeps: no direct change; the crate/camp-uptime meta wants sustained
    presence and his front-line slot moved to rising Mo & Krill, with anti-tank Shiv
    climbing - S was popularity-supported, so slides to A (peercontent, unverified).


    Changelog: 09-16 - no direct line; item tailwinds (Lifestrike heal/slow, Fortitude
    regen) and the lane-wins meta supported him.'
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
  notes: '10-05: no direct change; the trooper-speed fix marginally helps her split-push
    wave pathing, but her no-comeback early game is still the problem.


    Changelog: 09-16 - comeback souls trimmed and Rift resist made per-minute, removing
    her comeback path; health/boon 33->35 + Jar of Dead buffs are small; Toxic Bullets
    scaling buff is a marginal on-hit gain.


    Creator vegas (07-16) rates D; I rate C because 48.5% WR is bad but not collapse
    and 21% PR keeps her visible. heresy (09-17) gives no read.'
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
  why: 'Tempo lane bully the map-economy patch favors: he routes crate paths and roams,
    and with T3 bullet resist is one of the few who can still commit under a Guardian
    after the parry-cooldown change; his spirit core is untouched and his worst lane
    (Baba, ~59%) just got materially weaker.'
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
  notes: '10-14: Baba (beats him ~59%) took a major nerf - a marginal easing of a
    bad lane; no direct change.

    10-05: no direct change; the trooper-speed regression fix restores on-schedule
    lane crashes for his bully pressure, and Rat King''s frontline trim thins the
    competing A-tier bruiser pool.'
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
  notes: '09-29 City Never Sleeps: no direct change; the frontline/tank archetype
    is up, but the move from lane tempo to farm-route tempo is roughly neutral for
    a lane-fight gun tank, and heavy-melee crate routes need a heavy melee she does
    not build toward (peercontent, low confidence).

    09-16: health/boon 28->31, sprint 1.5->2.5, and Weighted Bola now grounds/interrupts
    flyers - direct buffs; tier S held.

    Matchups: data lists Lash and Drifter at 45%; treated as losing records. Low-confidence:
    no post-patch WR exists.'
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
Celeste:
  name: Celeste
  role: spirit burst carry
  archetypes:
  - spirit carry
  - burst caster
  - mobile assassin
  - late scaler
  tier: B
  trend: falling
  why: Late-scaling flying spirit burst is the wrong profile for a lane-wins tempo
    meta (comeback souls gone, early-Rift fights real, the air-drag slow bleeds her
    mid-flight), and a third Radiant Regeneration trim plus a buffed Deadman Danny
    (beats her 61%) compound the loss; she still bursts squishy melee threats (Yamato,
    Pocket) but folds to sustain and mobile initiators.
  core_items:
  - Extra Regen
  - High-Velocity Rounds
  - Mystic Regeneration
  - Radiant Regeneration
  - Mystic Expansion
  - Healing Booster
  - Restorative Locket
  - Torment Pulse
  - Greater Expansion
  - Witchmail
  - Spirit Shielding
  - Grit
  build_variants:
  - Spirit sustain-burst carrier
  - Anti-CC / anti-debuff tech
  enabled_by:
  - High base power + overloaded kit (mobility, four abilities)
  - Torment Pulse + Greater Expansion AoE around her ult
  - Ult damage in Mid Boss / Rift fights
  - Mystic/Radiant Regeneration sustain stack (nerfed but still core)
  countered_by:
  - "Silver \u2014 Weighted Bola grounds flyers like her"
  - Slows now bleed air drag (system)
  - 'Healing item trims: Radiant Regeneration, Restorative Locket'
  - "Scaling/comeback nerfs \u2014 late-scaler into a tempo meta"
  - "Ivy \u2014 out-sustains her burst window"
  - "Lash / Calico \u2014 mobile initiators that close and survive"
  last_changed_patch: Minor Update - 09-16-2026
  notes: '10-14: Radiant Regeneration spirit scaling 0.04->0.035 is the third trim
    to her sustain-burst core; Deadman Danny (beats her 61%) got a buff package.

    09-16: tier held at B (down from A) - the seven-nerf stack plus the air-drag flyer
    tax; Witchmail remains her anti-slow answer.

    54.6% WR / 26.4% PR is a 14-day, mostly pre-patch snapshot - treat as a ceiling,
    not current strength.'
  builds:
  - name: Spirit sustain-burst carrier
    damage: spirit
    core_items:
    - Extra Regen
    - High-Velocity Rounds
    - Mystic Regeneration
    - Radiant Regeneration
    - Mystic Expansion
    - Healing Booster
    - Restorative Locket
    - Torment Pulse
    - Greater Expansion
    popularity: primary
    notes: "Regen-stacked spirit build: HVR early for bullet velocity/movespeed, then\
      \ Torment Pulse + Greater Expansion for AoE burst around her ult \u2014 weaker\
      \ now that Radiant Regeneration and Restorative Locket were trimmed."
  - name: Anti-CC / anti-debuff tech
    damage: hybrid
    core_items:
    - Witchmail
    - Spirit Shielding
    - Grit
    popularity: secondary
    notes: "Witchmail is her highest-WR item (60.6%, bought ~24m) \u2014 the answer\
      \ into heavy slow/CC comps, which matter more now that slows bleed air drag."
  matchups:
    beats:
    - Pocket
    - Yamato
    - Haze
    - Paradox
    - Bebop
    loses_to:
    - Ivy
    - Warden
    - Lash
    - Calico
    - Mina
  matchup_notes: "She wins the burst race vs squishy close-range threats \u2014 61%\
    \ vs Pocket and 59% vs Yamato (S-tier, but she lands her damage before he closes).\
    \ Sustained healers out-last her damage window (Ivy 47%), while mobile initiators/bruisers\
    \ who survive the first burst and close the gap (Lash, Calico) beat her 52-53%."
  confidence: 0.6
  released_on: null
  provisional: false
Rat King:
  name: Rat King
  role: frontline brawler
  archetypes:
  - tank/frontline
  - lane bully
  tier: A
  trend: stable
  why: "Post-nerf he settles at 55.4% WR, right on the watchlist ~55% line \u2014\
    \ the 10-05 banner trim (CD 130->160, total DR 35->25%) pulled the 61% outlier\
    \ down without burying the kit. The gun-bruiser core is untouched and near-universally\
    \ built (Monster Rounds/HVR by ~3 min, Extra Health 91%), and his map-economy\
    \ fit (heavy-melee crates, AoE Haunt clear, forced hub fights) still matches the\
    \ farm-then-group-fight meta. He holds A, not S: strong but soft to sustain/support\
    \ comps and spirit burst that bypass his anti-bullet barrier."
  core_items:
  - Monster Rounds
  - High-Velocity Rounds
  - Opening Rounds
  - Extra Health
  - Cultist Sacrifice
  - Enduring Speed
  - Fortitude
  - Superior Cooldown
  build_variants:
  - Gun bruiser
  - Vitality frontline
  - Swarm shred
  enabled_by:
  - 'Map-economy lead engine: grouped, chasing Haunt camps reward Scrap Grenade AoE
    clear and regen sustain'
  - "Tough Crate routes needing heavy melee \u2014 116 heavy melee, 800 HP, 2.0 regen\
    \ open guaranteed ~58-soul crates"
  - "Forced telegraphed hub fights at Sunken Plaza/Bell Tower \u2014 banner ult adds\
    \ move speed, slow immunity and DR"
  - "Gun-carry meta \u2014 Rat Swarm's bullet-resist shred and Royal Pestments deflect\
    \ punish Venator/Silver/Paradox"
  countered_by:
  - "Heal/save supports that out-sustain his damage window \u2014 Ivy, Kelvin, Paige,\
    \ Dynamo"
  - "Spirit burst that bypasses the anti-bullet barrier \u2014 Celeste"
  - Silence/CC (Silence Wave, Silencer) denying banner and barrier
  - Anti-heal (Healbane, Decay) against his regen stacking
  last_changed_patch: Minor Update - 10-05-2026
  notes: "7-day check-in (2026-10-09): tier A -> A, WR 59%, PR 86% over 430072 matches.\n\
    10-05: banner ult trimmed (CD 130->160, DR 20->15% base + T3 15->10% = 35->25%\
    \ total, radius 24->20m, charge 12->10s, no Spirit-scaled move speed); base kit\
    \ buffed (Scrap Grenade 65->70, Rat Swarm CD 28->24s).\nData: WR 55.4% sits on\
    \ the watchlist ~55% line and PR 83.8% is novelty-inflated (~1-week-old hero)\
    \ \u2014 tier holds A, not S.\nDisagreement: prior 'Swarm shred' listed Bullet\
    \ Resist Shredder/Extra Spirit, but no shred item appears in usage; the spirit\
    \ angle is under-built (Mystic Expansion only)."
  builds:
  - name: Gun bruiser
    damage: gun
    core_items:
    - Monster Rounds
    - High-Velocity Rounds
    - Opening Rounds
    - Cultist Sacrifice
    - Fleetfoot
    - Berserker
    - Ballistic Enchantment
    popularity: primary
    notes: "Near-universal core \u2014 Monster Rounds + HVR at ~3 min into Opening\
      \ Rounds; Rat Swarm strips bullet resist so the Spreadshot/grenade window does\
      \ the work."
  - name: Vitality frontline
    damage: hybrid
    core_items:
    - Extra Health
    - Sprint Boots
    - Enduring Speed
    - Fortitude
    - Compress Cooldown
    - Superior Cooldown
    popularity: secondary
    notes: Extra Health (91%) and Fortitude (90%) anchor the lead-the-charge build;
      Superior/Compress Cooldown (57.9%/57.7% WR) are the post-nerf answer to the
      banner ult's 130->160s cooldown.
  - name: Swarm shred
    damage: spirit
    core_items:
    - Mystic Expansion
    popularity: niche
    notes: "Leans on Rat Swarm T3 shred plus Mystic Expansion AoE, but no dedicated\
      \ shred item shows in usage \u2014 under-built and data-thin."
  matchups:
    beats:
    - Venator
    - Paradox
    - Silver
    - Rem
    - Grey Talon
    loses_to:
    - Ivy
    - Kelvin
    - Celeste
    - Dynamo
    - Paige
  matchup_notes: "Royal Pestments' bullet deflect plus Rat Swarm's bullet-resist shred\
    \ make him a gun-carry killer \u2014 Venator 64%, Silver 62%, Paradox 62%. His\
    \ losses cluster on sustain/support comps that out-heal a single damage window\
    \ (Ivy 44%, Kelvin 48%, Paige 51%, Dynamo 51%) and on spirit burst that ignores\
    \ his anti-bullet barrier (Celeste 48%); Rem, another support, is the exception\
    \ he beats at 61%."
  confidence: 0.55
  released_on: '2026-10-02'
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
