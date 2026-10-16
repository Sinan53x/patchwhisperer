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
 }
]

## Current hero entries (this batch only)

Mo & Krill:
  name: Mo & Krill
  role: spirit tank initiator
  archetypes:
  - tank/frontline
  - initiator
  tier: A
  trend: rising
  why: "Default sustained front line now that Billy has slipped \u2014 sustained uptime\
    \ and T3 bullet resist make him one of the few who can still commit under a tower\
    \ after the parry-cooldown change, and the camp/uptime meta suits him. Long-range\
    \ poke he cannot close on (Celeste, Vindicta) still kites him."
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
  notes: 'City Never Sleeps: camp/uptime meta plus Billy''s slide hand him the default
    sustained front-line slot.

    Spirit build confirmed by data (Mystic Burst 100%, Torment Pulse 91%); no Scourge
    in top 15 and ~40% PR is high, not a win-rate outlier.

    Last hero-relevant change: Minor Update - 07-28-2026.'
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
  why: Rising anti-tank fed by the tank/frontline wave (Abrams, Mo & Krill, Billy)
    his current-HP Serrated Knives shred and by harder camps rewarding his regen;
    the third Radiant Regeneration trim chips the spirit-sustain front line he holds,
    and burst/hook CC (Yamato, Drifter, Bebop) still kills him before regen ramps.
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
  notes: '10-14: Radiant Regeneration spirit scaling 0.04->0.035 chips his near-universal
    Mystic/Extra Regen spirit-sustain core; kit untouched.

    City Never Sleeps: rising anti-tank - the bigger front line feeds current-HP Serrated
    Knives and harder camps reward his regen.

    Spirit/regen rebuild confirmed (Mystic Regeneration/Extra Regen core); Mystic
    Vulnerability/Torment Pulse/Escalating Exposure run 40-55%.'
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
Warden:
  name: Warden
  role: gun carry
  archetypes:
  - gun carry
  - late scaler
  tier: C
  trend: falling
  why: 'Late-scaling gun carry the no-comeback, farm-route economy refuses to wait
    for: tempo now runs through crate routes and hub objectives rather than lane brawling,
    and Shadow Weave''s invis-engage gains little from the new Steam-Vent/district
    layout. His 09-16 cuts (bullet dmg/boon, flask range/speed, Willpower T3, nerfed
    T4 gun finishers) are still unanswered.'
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
  notes: 'City Never Sleeps: no direct line; the farm-route/no-comeback economy still
    refuses to wait for a late gun scaler, and Shadow Weave gains little from the
    new Steam-Vent/district layout.

    One dominant gun build; the ''cage'' is a Willpower choice, not an item path.

    09-16: bullet dmg/boon, flask range/speed, Willpower T3 cut; Mercurial Magnum
    + Spiritual Overflow nerfed, Veil Walker stripped.'
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
  why: 'The patch''s camp-clear champion: Flying Strike now creates paths against
    solid targets (turrets, Shrines, objectives) for extra mobility and objective
    access, and her punch AoE gathers the new grouped, chasing Haunt camps faster
    than almost anyone. Tempo burst plus point-click Spirit Snatch still deletes squishy
    carries; sustain tanks and anti-heal cap her at the top of A, toward S.'
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
  last_changed_patch: City Never Sleeps
  notes: "City Never Sleeps: Flying Strike now creates paths against solid targets\
    \ (turrets, Shrines, objectives) \u2014 new mobility/objective access \u2014 and\
    \ she is the patch's camp-clear champion vs the grouped Haunt camps.\nTankbuster\
    \ is 39% share at a 25m average buy (late luxury, not core); the Refresher build\
    \ stays niche/creator-driven.\n09-16: Crimson Slash T3 heal spirit scaling +0.4,\
    \ Flying Slash light-melee scaling 1.0->1.2."
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
  why: Highest-pick initiator (62% PR) whose dive-and-stomp engage still snowballs
    in the no-comeback economy, now with the green-lane roof/tree giving him permanent
    lane high ground and boxes mattering more to his farm. Mass pick pressure drags
    his 51.8% WR; Silver's Weighted Bola and the air-drag slows are still the counter.
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
  notes: 'City Never Sleeps: no direct line; the green-lane roof/tree gives permanent
    lane high ground and boxes matter more to his farm.

    Stomp/spirit is current; 30-day usage still shows gun Lash because the window
    is mostly pre-09-16.

    09-16: Ground Strike T3 scaling + per-meter damage up, gun falloff changed, Flog
    heal nerfed.'
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
  notes: "10-05: no direct change; the trooper-speed fix restores intended wave pathing\
    \ so his split-push side-lane pressure converts on schedule \u2014 tiny QoL, but\
    \ the tempo economy still buries his scaling.\n\nChangelog: 09-16 - no Mirage\
    \ line; tier stays B; hurt by the gutted comeback/tempo system changes, partially\
    \ offset by the Toxic Bullets scaling buff in his spirit-amp core.\n\nData over\
    \ creators: 30-day high-rank usage shows a spirit-amp hybrid core (Mystic Regen/Healbane/Mystic\
    \ Vulnerability), not the Echo Shard-Scourge-Inhibitor build the summer creators\
    \ cited - Echo Shard is ~0% now."
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
  released_on: null
  provisional: false
Drifter:
  name: Drifter
  role: melee bruiser
  archetypes:
  - mobile assassin
  - tank/frontline
  tier: A
  trend: rising
  why: Blind-pickable spirit-melee bruiser still on the field's highest pick rate;
    the City Never Sleeps layout adds hiding spots, Steam Vents and heavy-melee Tough-Crate
    routes that suit a stealth-revealing melee roam. He still lacks hard CC and closing
    mobility, so a 51.4% WR floor and rising Dynamo/Mo & Krill/Apollo lane pressure
    cap him at A.
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
  - new districts + Steam Vents (stealth-reveal sense)
  - Heavy-Melee Tough Crate routes (melee core)
  countered_by:
  - Dynamo
  - Mo & Krill
  - Apollo
  - Vyper
  - anti-heal stacking
  - CC/silence
  last_changed_patch: null
  notes: '09-29 City Never Sleeps: no direct change - new districts/Steam Vents and
    heavy-melee Tough-Crate routes fit his stealth-reveal roam (peercontent, unverified).

    Dropped KB core_items Decay/Toxic Bullets/Fortitude - none show in current 30-day
    usage; the ''Toxic Bullets bot'' framing is a 2026-04 artifact (data over creator).
    Celeste falling softens one losing matchup, but Dynamo/Mo & Krill/Apollo rising
    worsen others - net stable. 09-16 Minor Update: no direct Drifter change; gutted
    comeback souls and ramped rift resist suit his early-bruiser floor.'
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
  tier: A
  trend: rising
  why: 'Sustain frontline the camp meta feeds: harder Haunt camps and longer PvE routes
    reward his Spirit Lifesteal/Healing Booster regen stack, and the snapshot''s 56.4%
    WR is the board''s second-highest. Still the one tank burst and anti-heal can
    delete, and he drops the mirror to Abrams/Mo & Krill.'
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
  - harder Haunt camps reward regen/sustain
  - Spirit Lifesteal + Healing Booster sustain stack
  - melee-diver meta he outlasts (Mina, Calico, Lash)
  countered_by:
  - burst vs low HP-per-boon (Yamato, Holliday)
  - anti-heal and trimmed healing items
  - ranged poke / flyers (Vindicta)
  - tank stat-checks (Abrams, Mo & Krill)
  - CC
  last_changed_patch: Minor Update - 07-09-2026
  notes: '09-29 City Never Sleeps: no direct change; hard Haunt camps and longer PvE
    routes feed his sustain stack - flipped from fair B-tier baseline to A on a 56.4%
    snapshot WR (peercontent read).

    Data disagrees with the 07-16 creator read: Refresher and Echo Shard appear in
    none of his top-15 high-rank buys over 30 days - his real build is spirit sustain,
    not a Refresher initiator.

    Untouched by Minor Update 09-16 (last changed 07-09).'
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
  notes: "10-05: no direct change; the trooper-speed fix restores lane-wave cadence,\
    \ marginally boosting the lane pressure her tempo-support identity trades on \u2014\
    \ still S.\n\n09-29 City Never Sleeps: no direct change; lane-adjacent crate routes\
    \ and Healing Snacks reward her lane pressure, and the contested hubs suit her\
    \ carry-snowball (peercontent).\n\nChangelog: 09-16 - heavy-melee spirit scaling\
    \ 0.3->0.45, Captivating Read T1 -11->-14s / T3 +1m->+2m; Slowing Hex cd 27->29s\
    \ is a minor tax."
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
  trend: stable
  why: Popular but not-winning setup initiator (46.5% WR) whose delayed payoff the
    tempo read still punishes - but Bell Tower's single rope and ~280-soul payout
    hand his Doorway a real kidnap play on the new top objective. Reach still comes
    late and early snowball beats him.
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
  - Bell Tower single rope + ~280 souls (Doorway kidnap)
  - AoE/charge spirit items (Mystic Expansion, Greater Expansion, Extra Charge)
  - high pick rate keeps a large coordinated-player base
  countered_by:
  - dive tempo (Yamato, Lash, Apollo, Holliday)
  - Doorway range cut 70->65m (08-12)
  - 'tempo meta: early snowball beats his delayed payoff'
  - Vortex Web/Slowing Hex being low-WR bait items
  last_changed_patch: Minor Update - 08-12-2026
  notes: '09-29 City Never Sleeps: no direct change; Bell Tower''s single rope + ~280
    souls makes his Doorway kidnap a real objective play (pre-place door before roping
    up), offset by the tempo read punishing delayed setup - trend up from falling
    to stable (peercontent).

    Changelog: 09-16 - no direct line; loses his Veil Walker disengage (Sprint Boots
    + movespeed-on-break removed).

    Usage backs the creator ''kidnap is a trap'' read: Vortex Web and Slowing Hex
    are his two worst staples vs the Bell core''s Tankbuster 51.2% / Boundless Spirit
    57.4%.'
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
