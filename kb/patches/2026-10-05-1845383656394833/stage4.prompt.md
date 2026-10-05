# Task: synthesis (the verdict and the meta thesis)

Patch: Minor Update - 10-05-2026 (2026-10-05)
Change counts: General 25, total 25

## Update summary

{{digest_summary}}

## Previous meta thesis (knowledge base, pre-patch)

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

## Systems analysis

{
 "systems_changed": [
  {
   "system": "lane troopers / wave tempo",
   "change_summary": "Troopers were walking too slowly in lane; the bug fix restores intended trooper movement speed, so waves arrive, meet and crash on schedule again. This is a regression repair, not a tuning pass — it re-enables normal lane cadence rather than making troopers faster than baseline.",
   "driving_changes": [
    "[fix] Fixed bugs that were causing troopers to walk too slowly in lane"
   ],
   "magnitude": "minor",
   "effect_on_play": "Restores predictable wave timing for last-hits, freeze and push, and re-opens the standard dive/punish windows on an enemy who is stuck under a slow wave. Since the KB says the lead engine sits in the map economy (Tough Crates, Haunt camps, hub fights) rather than the lane, the practical impact is small — it mostly removes an unintended quality-of-life drag on lane phase rather than changing who wins."
  }
 ],
 "tempo_shift": {
  "direction": "neutral",
  "confidence": 0.6,
  "why": "Fixing trooper speed only restores baseline lane tempo; it adds no new early snowball or comeback lever, and the KB lead engine (map economy, no comeback valve) is untouched. Faintly toward tempo at best, because normal wave timing makes lane pressure and crashes land as designed again."
 },
 "archetype_effects": [
  {
   "archetype": "lane bully",
   "direction": "up",
   "magnitude": "minor",
   "why": "On-schedule trooper speed restores the wave-crash timing that makes bullying and dive-punish windows land reliably."
  },
  {
   "archetype": "split pusher",
   "direction": "up",
   "magnitude": "minor",
   "why": "Reliable trooper pathing makes pushed waves and side-lane pressure convert at the intended cadence rather than stalling."
  },
  {
   "archetype": "late scaler",
   "direction": "neutral",
   "magnitude": "minor",
   "why": "No economy, comeback or objective change accompanies the fix; the Broker stall window and trimmed comeback bounties are unchanged."
  }
 ],
 "intent_read": "Valve appears to be patching a regression from the City Never Sleeps map/trooper rework, not steering the meta. The intent is to make lane phase behave as originally designed; the game's lead engine (map economy, no comeback valve) is deliberately left untouched."
}

## Item analysis

{
 "items": [],
 "notable_item_stories": []
}

## Hero analysis (only heroes with direction != neutral)

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

## Creator sources published after this patch (optional corroboration; the notes, KB and snapshot remain primary — if a source contradicts them, say so and keep your own read)

{{creator_sources}}

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
