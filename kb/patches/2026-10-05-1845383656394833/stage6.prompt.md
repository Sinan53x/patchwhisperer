# Task: update the knowledge base after this patch

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

## Hero analysis (movers only)

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

## Item analysis

{
 "items": [],
 "notable_item_stories": []
}

## Current meta.md

# Meta state
Last patch: City Never Sleeps (2026-09-29)

## Thesis
Games are won in the map economy now, not the lane. Templated PvE income — guaranteed Tough Crate routes from ~2:30 and the Sunken Plaza (5-8 min) and Bell Tower (8+) hub fights — is the lead engine, so AoE/sustain camp-clearers and heavy-melee box farmers bank faster than pure lane bullies. The no-comeback valve is intact, so leads still close games, but The Broker's ~30-min Corrupted tier gives late scalers a concrete reason to stall and partly re-opens scaling. Fight shape = farm-route tempo, then forced, telegraphed group fights at hubs.

## Economy and systems
- Comeback bounties stay trimmed; extra comeback souls still reroute to the two lowest-econ players via tick gold — farm and lane leads stick.
- Guardian bounty +10%, Walker +5%, objective share 30->25% (carried from 09-16).
- Parrying a Guardian/objective now spends the parry (cooldown applies on objectives), so tower-diving is punishable for most of the roster; only T3-bullet-resist picks (Apollo, Mo & Krill) still commit.
- Respawn still 38s at 20m — the longer death tax raises every pick's value.
- Slows -20% globally, air drag 35% (unchanged): grounded kiting strong, flyers pulled down.
- Instant cast and Walker fireballs are live: combat is faster and objectives hit back harder.
- The Broker spawns ~30 min, then ~every 15 min. Corrupted items roll match-wide identical random negatives — a runtime read, not something you build toward.

## Map
Lanes renamed; four new districts added. All old neutrals are replaced by new Haunt creatures: camps group and chase, and hit harder, rewarding AoE clear and sustain. Farm sources: Tough Crates (58 souls, guaranteed, ~200-300-soul lane routes) require a Heavy Melee to open; Haunt camps; Sinner's Sacrifice variants; Buff Containers (ability range, spirit resist). Pickups: Healing Snacks (10% max HP), Steam Vents (invisibility roams). Hubs: Sunken Plaza (~5-8 min) and Bell Tower (8+, ~280 souls, a single rope up/down, three vaults) concentrate telegraphed group fights. New roofs/high ground and hiding spots — green lane holds a roof/tree above the bridge. Side asymmetry: Arch Mother's side owns Sunken Plaza plus the theater, so watch win rate by map side.

## Archetype standing
- AoE/sustain camp clearers: up — stacked, chasing Haunt camps and heavier camp damage reward Storm Cloud/punch-style clears.
- Heavy-melee frontline/tanks: up — Tough Crate access plus sustain; Mo & Krill takes Billy's front-line slot.
- Roamers/pick assassins: up — more districts, hiding spots and Steam Vents; Paradox ahead of Bebop in the slot.
- Stealth: up — Vent layout expands routes, and sense-reveal is the counter.
- Late scalers: down, softening — no comeback valve vs The Broker stall window.
- Flyers: down — air-drag slows unchanged; Silver's Bola remains the answer.
- On-hit spirit carries: down — 09-16 item hits (Mercurial Magnum, Spiritual Overflow, Plated Armor) persist.
- Non-melee assassins (Calico-style): down — cat form cannot heavy-melee the crate economy.

## Watchlist
- Tough Crates: peercontent expects a hotfix nerf — that would flip the farm-route thesis back toward lane tempo.
- Yamato/Seven/Mina presence and WR as the camp-clear AoE test.
- Calico and Bebop pick rates — near-zero confirms the crate-lockout and roamer-slot reads.
- Late-scaler WRs (Warden, Celeste, Infernus) after 30 min — validates Broker-as-safety-valve.
- Arch Mother vs other side win rates — quantify the side asymmetry.
- Infernus WR: peercontent reports an undocumented global napalm team-amp removal — unverified, not in notes.

## Recent history
- City Never Sleeps: map rework — renamed lanes, four districts, Haunt camps replace neutrals, Tough Crate/Broker economy; the lead engine moves off the lane.
- Minor Update - 09-16-2026: tempo patch — comeback souls gutted, on-hit spirit carry killed, flyers taxed.
- 08-22-2026: Celeste tuning.
- 08-12-2026: McGinnis/Apollo tuning.
- 07-30-2026: Ranked Mode added.

## Current item entries (changed items only; may be empty for items not yet in the KB)

(none)

## What to do

Produce the post-patch knowledge base state. This KB is read by the analyst on the *next* patch, so write it as durable state, not as a patch summary.

1. **meta.md**: rewrite the whole document in this structure (markdown, <= 550 words):
   - `# Meta state` line with `Last patch: Minor Update - 10-05-2026 (2026-10-05)`
   - `## Thesis` — 2-4 sentences: how games are won right now (tempo vs scaling, fight shape, what archetypes carry).
   - `## Economy and systems` — bullets describing the current state of comeback, bounties, objectives, respawn, movement/slows, in present tense with current numbers where known.
   - `## Map` — current map state in present tense: lanes/districts, objectives with timings and values where known, farm sources (Haunt tiers, crates/boxes, Sinner's Sacrifice variants, Buff Containers), pickups (Healing Snacks, Steam Vents), side asymmetry, key routes. Keep it when nothing changed.
   - `## Archetype standing` — one bullet per archetype in play: up/down/stable and why.
   - `## Watchlist` — 3-6 bullets: heroes/items/systems that are uncertain and should be checked against data.
   - `## Recent history` — keep at most 5 bullets, newest first, one line per patch: "Minor Update - 10-05-2026: <headline>". Carry forward existing bullets from the current meta.md, drop the oldest beyond 5.
2. **item_updates**: for each changed item, the fields that changed. Allowed fields: role, bought_by, slot, tier, notes. `bought_by` must list hero names that build it as core or common situational pick, updated for this patch.
3. **change_log**: one line per KB edit you made, for the human to skim.

Tier is one of S/A/B/C/D. Trend is rising/stable/falling.

## Output schema

{
  "meta_md": "full markdown text",
  "item_updates": {"Item Name": {"role": "...", "bought_by": ["..."], "notes": "..."}},
  "change_log": ["Item Name: bought_by +Wraith (now core after rework)", "..."]
}
