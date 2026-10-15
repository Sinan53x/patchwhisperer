# Task: synthesis (the verdict and the meta thesis)

Patch: Minor Update - 10-14-2026 (2026-10-15)
Change counts: General 27, total 27

## Update summary

(n/a)

## Previous meta thesis (knowledge base, pre-patch)

# Meta state
Last patch: Minor Update - 10-05-2026 (2026-10-05)

## Thesis
Games are still won in the map economy: templated PvE income — guaranteed Tough Crate routes from ~2:30, plus the Sunken Plaza (5-8 min) and Bell Tower (8+) hub fights — is the lead engine, so AoE/sustain camp-clearers and heavy-melee box farmers bank faster than pure lane bullies. The 10-05 patch repaired a trooper-speed regression, so wave crashes land on intended cadence again and lane tempo is marginally re-weighted upward versus camp farming — but no souls, bounty, objective, respawn, item or comeback lever moved, so the map-economy lead engine still decides games. The no-comeback valve is intact; The Broker's ~30-min Corrupted tier remains the only stall window for late scalers. Fight shape is unchanged: farm-route tempo, then forced telegraphed group fights at hubs.

## Economy and systems
- Comeback bounties stay trimmed; extra comeback souls reroute to the two lowest-econ players via tick gold. Farm and lane leads stick.
- Guardian bounty +10%, Walker +5%, objective share 30->25% (carried from 09-16).
- Parrying a Guardian/objective spends the parry (cooldown applies on objectives); only T3-bullet-resist picks (Apollo, Mo & Krill) still commit to dives.
- Respawn 38s at 20m — the long death tax keeps every pick's value high.
- Slows -20% globally, air drag 35%. Grounded kiting strong; flyers pulled down.
- Instant cast and Walker fireballs are live: combat fast, objectives hit back.
- Trooper speed regression fixed (10-05): waves crash on intended cadence. A restoration, not a new tempo lever.
- The Broker spawns ~30 min, then ~every 15 min; Corrupted negatives are a runtime read, not something to build toward.

## Map
Lanes renamed; four new districts added. Old neutrals are replaced by Haunt creatures: camps group, chase and hit harder, rewarding AoE clear and sustain. Farm sources: Tough Crates (58 souls, guaranteed, ~200-300-soul lane routes) require a Heavy Melee to open; Haunt camps; Sinner's Sacrifice variants; Buff Containers (ability range, spirit resist). Pickups: Healing Snacks (10% max HP), Steam Vents (invisibility roams). Hubs: Sunken Plaza (~5-8 min) and Bell Tower (8+, ~280 souls, a single rope up/down, three vaults) concentrate telegraphed group fights. New roofs/high ground and hiding spots — green lane holds a roof/tree above the bridge. Side asymmetry: Arch Mother's side owns Sunken Plaza plus the theater, so split WRs by map side.

## Archetype standing
- AoE/sustain camp clearers: stable (top) — crate/Haunt income untouched; only trooper cadence moved.
- Heavy-melee frontline/tanks: stable (up) — Tough Crate access plus sustain; Mo & Krill holds Billy's front-line slot.
- Roamers/pick assassins: stable — districts, hiding spots and Steam Vents unchanged.
- Stealth: stable — Vent routes expand; sense-reveal is the counter.
- Lane bullies / split pushers: up slightly — trooper-speed fix restores crash-timing punish and split-push conversion windows.
- Late scalers: down, softening — no comeback valve vs The Broker stall window.
- Flyers: down — air drag unchanged; Silver's Bola remains the answer.
- On-hit spirit carries: down — 09-16 item hits (Mercurial Magnum, Spiritual Overflow, Plated Armor) persist.
- Non-melee assassins (Calico-style): down — cat form cannot heavy-melee the crate economy.

## Watchlist
- Rat King WR post-nerf (ult cooldown 130->160, total banner DR 35->25%) — does 61% fall below ~55%?
- Sinclair pick rate — near-zero confirms the kit-steal slot is dead after the broad trim.
- Lane-phase dive/kill stats vs camp-farm souls — did restored trooper speed actually re-raise lane-bully WRs?
- Trooper cadence: watch for over-correction to faster-than-baseline waves.
- Tough Crates: a hotfix nerf still flips the farm-route thesis back toward lane tempo.
- Late-scaler WRs (Warden, Celeste, Infernus) after 30 min — validates Broker-as-safety-valve.

## Recent history
- Minor Update - 10-05-2026: trooper-speed regression fixed (lane cadence restored); Rat King and Sinclair trimmed; map-economy engine untouched.
- City Never Sleeps: map rework — renamed lanes, four districts, Haunt camps replace neutrals, Tough Crate/Broker economy; lead engine moves off the lane.
- Minor Update - 09-16-2026: tempo patch — comeback souls gutted, on-hit spirit carry killed, flyers taxed.
- 08-22-2026: Celeste tuning.
- 08-12-2026: McGinnis/Apollo tuning.

## Systems analysis

{
 "systems_changed": [],
 "tempo_shift": {
  "direction": "neutral",
  "confidence": 0.9,
  "why": "no systems changes — the General/systems section is empty, so the map-economy lead engine, comeback valve, respawn timers, slows and objective bounties all carry over unchanged from 10-05."
 },
 "archetype_effects": [],
 "intent_read": "This is a narrow housekeeping patch: one item (Radiant Regeneration) and three hero kits (Baba, Deadman Danny, Street Brawl) were touched, with nothing at the economy, objective, movement or map layer. Valve is not trying to move the meta here — the templated Tough Crate/Sunken Plaza/Bell Tower income engine and the no-comeback valve stand as the KB thesis describes, so any meta movement must come from the item and hero changes alone."
}

## Item analysis

{
 "items": [
  {
   "item": "Radiant Regeneration",
   "direction": "nerf",
   "magnitude": "minor",
   "summary": "Third cumulative trim to the regen-sustain shell (heal-on-cast 08-22, per-boon 09-16, spirit scaling 0.04->0.035 now). At 94-98% buy on its holders it won't drop out of builds, but spirit-scaling means each point of spirit power buys less healing, so spirit-stacking users feel it more than gun-hybrid ones.",
   "affected_heroes": [
    {
     "hero": "Baba",
     "relationship": "core",
     "effect": "down",
     "why": "Radiant Regeneration is ~94% buy in her regen-stacking shell; the scaling cut shaves the exact heal her out-sustain-the-economy plan runs on."
    },
    {
     "hero": "Lady Geist",
     "relationship": "core",
     "effect": "down",
     "why": "~98% buy across both builds, and the trim bites hardest on her Spirit Soul-Exchange variant because it stacks the most spirit power."
    },
    {
     "hero": "Shiv",
     "relationship": "core",
     "effect": "down",
     "why": "Near-universal in his Mystic/Extra Regen spirit-sustain core — one more chip off the regen wall he frontlines behind."
    },
    {
     "hero": "Celeste",
     "relationship": "core",
     "effect": "down",
     "why": "Still core to her sustain-burst shell, but she's already B-tier and falling, so a third regen trim compounds her survivability loss rather than being absorbed."
    },
    {
     "hero": "Kelvin",
     "relationship": "situational",
     "effect": "down",
     "why": "Listed as a buyer and named as the sustain support Baba loses to, but he has no KB entry — low confidence on relationship and magnitude."
    }
   ],
   "build_shift": "No component or slot change: Radiant Regeneration stays the T3 Spirit regen slot and its healing rivals (Restorative Locket, Healing Booster) were trimmed in the same window, so nothing displaces it — the slot just shrinks in value."
  }
 ],
 "notable_item_stories": [
  "Radiant Regeneration is on its third consecutive trim with no competing sustain item added, so the regen archetype keeps eroding file-by-file — a quiet buff to anti-heal (Healbane, Decay) and to burst that lands before sustain ramps."
 ]
}

## Hero analysis (only heroes with direction != neutral)

[
 {
  "hero": "Lady Geist",
  "in_notes": true,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.4,
  "direct_reasons": [],
  "indirect_reasons": [
   "Radiant Regeneration spirit scaling 0.04->0.035 trims the ~98%-buy regen core in both her gun-bruiser and Spirit Soul-Exchange builds; the spirit build loses the most."
  ],
  "build_changes": [
   "No swap needed, just a narrower sustain window - Healbane/Decay now beat her regen slightly more easily."
  ],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Kit untouched, but a third regen-item trim narrows the sustain her build runs on."
 },
 {
  "hero": "Kelvin",
  "in_notes": true,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.3,
  "direct_reasons": [],
  "indirect_reasons": [
   "The Radiant Regeneration trim hits rival sustain (Baba, Lady Geist, Shiv, Celeste) while his Extra Regen/Healing Booster core is untouched - a small relative gain."
  ],
  "build_changes": [],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Rivals' healing got trimmed, not his - a quiet, small relative win."
 },
 {
  "hero": "Calico",
  "in_notes": true,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.25,
  "direct_reasons": [],
  "indirect_reasons": [
   "Baba, who beats her roughly 58%, took a major nerf - her worst listed matchup loosens slightly."
  ],
  "build_changes": [],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Untouched; her worst matchup (Baba) got weaker."
 },
 {
  "hero": "Shiv",
  "in_notes": true,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.4,
  "direct_reasons": [],
  "indirect_reasons": [
   "Radiant Regeneration scaling 0.04->0.035 chips the regen wall in his near-universal Mystic/Extra Regen spirit-sustain core."
  ],
  "build_changes": [],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Anti-tank kit untouched; a small regen trim chips his sustain front line."
 },
 {
  "hero": "Apollo",
  "in_notes": true,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.25,
  "direct_reasons": [],
  "indirect_reasons": [
   "Baba, who beats him roughly 59%, took a major nerf - a marginal easing of a bad lane."
  ],
  "build_changes": [],
  "tier_before": "S",
  "tier_after": "S",
  "one_liner": "Untouched; only notable shift is Baba, his bad lane, getting nerfed."
 },
 {
  "hero": "Celeste",
  "in_notes": true,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.4,
  "direct_reasons": [],
  "indirect_reasons": [
   "Radiant Regeneration scaling 0.04->0.035 trims her sustain-burst core; Deadman Danny, who beats her 61%, got a large buff package."
  ],
  "build_changes": [],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Already falling; another regen trim plus a buffed matchup dent her survivability."
 },
 {
  "hero": "Baba",
  "in_notes": true,
  "direction": "down",
  "magnitude": "major",
  "confidence": 0.6,
  "direct_reasons": [
   "Baba's Brew barrier scaling 1.2->0.7 and base 100->90 gut the frontline shield her regen-bruiser build runs, and CD 25->27s moves it to T2 (later online).",
   "-7% Base Bullet Resistance plus Spirit Resistance scaling 0.12->0.1 cut both her lane bullet-tank and her anti-spirit bruiser identity.",
   "Granny Long Legs (CD 30->32, lower light-melee launch, decaying repeat air-melee momentum, no slope speed on heavy melee) trims her mobility and escape; Threadsap CD 26->28 and its spirit shred now ends when she dies."
  ],
  "indirect_reasons": [
   "Radiant Regeneration spirit scaling 0.04->0.035 shaves her ~94%-buy core heal - a third trim to the sustain her tank plan leans on."
  ],
  "build_changes": [
   "Regen stack is shakier now - buy Healing Booster/Spirit Resilience earlier and value Duration Extender/Superior Cooldown for silence plays over pure sustain; Brew lands later as a T2."
  ],
  "tier_before": "B",
  "tier_after": "C",
  "one_liner": "Mobility, barrier and bullet resist all cut - no longer the unkillable frontline she was."
 },
 {
  "hero": "Solomon",
  "in_notes": true,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.25,
  "direct_reasons": [],
  "indirect_reasons": [
   "Baba - his hardest listed loss at 67% - took a major nerf, loosening his worst matchup."
  ],
  "build_changes": [],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "No direct change, but Baba's nerf loosens his worst matchup."
 },
 {
  "hero": "Deadman Danny",
  "in_notes": true,
  "direction": "up",
  "magnitude": "moderate",
  "confidence": 0.5,
  "direct_reasons": [
   "Base health 680->730 and regen 2.5->3.25 shore up his squishy flyer frame.",
   "Gun 12->15 uncharged / 44->48 charged plus Chimera Mk1 weapon scaling 1.15->1.4 raise his marksman DPS.",
   "Strix Salvo CD 30->25s, spirit scaling 0.9->1.1, T2 +30/+45, T3 +0.35 buff his mark burst; Close The Deal AP +50->+90 and execute +50%->+75%; Rocket Jump self-damage 6.5%->5%."
  ],
  "indirect_reasons": [],
  "build_changes": [
   "Lean into the buffed Strix Salvo plus Close The Deal mark-execute line with Bullet Resist Shredder and HV Rounds/Express Shot; stay ranged - the anti-air flyer tax is unchanged."
  ],
  "tier_before": "C",
  "tier_after": "C",
  "one_liner": "Big health, gun and mark buffs - but still a flyer in an anti-air patch."
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
