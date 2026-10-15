# Task: update the knowledge base after this patch

Patch: Minor Update - 10-14-2026 (2026-10-15)

## Synthesis

{
 "patch_size": "minor",
 "size_why": "One item trim (Radiant Regeneration) plus one major hero cut (Baba) and one buff package (Deadman Danny) — no economy, objective, movement, map or comeback lever moved, so the way games are won is untouched. The 'General 27' count is breadth of tuning, not structural depth.",
 "headline": "Baba's unkillable frontline got gutted and Deadman Danny got a real buff package, but the Tough Crate/Sunken Plaza/Bell Tower income engine still decides games exactly as before.",
 "meta_thesis": {
  "previous": "Games are won by templated PvE map income — guaranteed Tough Crate routes, Sunken Plaza (5-8m) and Bell Tower (8m+) hub fights — with no comeback valve, so AoE/sustain camp-clearers and heavy-melee box farmers bank faster than lane bullies.",
  "new": "Unchanged: the economy, objective bounties, respawn tax and no-comeback valve all carry over, so the farm-route-then-forced-hub-fight shape stands; the patch only reshuffles which sustain frontline holds the archetype slot, cutting Baba out of it and handing Deadman Danny a sharper (but still flyer-taxed) kit.",
  "relationship": "continuation",
  "why": "No systems, economy, map or item-slot change — the drivers are a third cumulative Radiant Regeneration trim and a Baba kit cut, which move heroes inside existing archetypes rather than moving the archetypes themselves."
 },
 "winners": [
  {
   "hero": "Deadman Danny",
   "why": "Direct package: base HP 680->730, gun 12->15 / charged 44->48, Chimera Mk1 scaling 1.15->1.4, Strix Salvo CD 30->25s and Close The Deal execute 50%->75%.",
   "indirect": false
  },
  {
   "hero": "Kelvin",
   "why": "His Extra Regen/Healing Booster sustain core is untouched while every named rival sustain buyer (Baba, Lady Geist, Shiv, Celeste) ate the Radiant Regeneration trim — a pure relative gain.",
   "indirect": true
  },
  {
   "hero": "Calico",
   "why": "Untouched, and her worst listed matchup (Baba, ~58% against her) just lost barrier, bullet resist and mobility.",
   "indirect": true
  },
  {
   "hero": "Apollo",
   "why": "S-tier and untouched; Baba beats him ~59% and just got materially weaker, easing his worst lane.",
   "indirect": true
  },
  {
   "hero": "Solomon",
   "why": "His hardest listed loss (Baba, 67%) took a major nerf — worst matchup loosens with no cost to him.",
   "indirect": true
  }
 ],
 "losers": [
  {
   "hero": "Baba",
   "why": "Brew barrier 1.2->0.7 scaling and base 100->90 with 25->27s CD, -7% Base Bullet Resist, spirit-resist scaling 0.12->0.1, plus Granny Long Legs and Threadsap trims — mobility, shield and tank identity all cut. B->C.",
   "indirect": false
  },
  {
   "hero": "Lady Geist",
   "why": "~98% buy on Radiant Regeneration; spirit scaling 0.04->0.035 bites hardest on her Spirit Soul-Exchange build.",
   "indirect": true
  },
  {
   "hero": "Celeste",
   "why": "Third trim to her sustain-burst core lands on a hero already falling, and Deadman Danny (beats her 61%) got a large buff package.",
   "indirect": true
  },
  {
   "hero": "Shiv",
   "why": "Radiant Regeneration chipped again in his near-universal Mystic/Extra Regen spirit-sustain core.",
   "indirect": true
  }
 ],
 "non_obvious_calls": [
  {
   "claim": "The patch's real winner set is 'anyone who fought Baba' — Apollo, Calico and Solomon all move up while untouched.",
   "why": "All three list Baba as their worst or near-worst matchup, and her cut hits barrier, bullet resist and mobility simultaneously.",
   "confidence": 0.5
  },
  {
   "claim": "Radiant Regeneration's third consecutive trim is a stealth buff to anti-heal and burst, not a sustain-item change.",
   "why": "No competing sustain item was added, so Healbane/Decay and pre-ramp burst get relatively better while the regen archetype erodes file-by-file.",
   "confidence": 0.6
  },
  {
   "claim": "Deadman Danny's buff package does not lift him out of C-tier despite the numbers.",
   "why": "He is still a flyer in an anti-air, high-air-drag environment where Silver's Bola is the answer — the direct buffs fight a context that was not changed.",
   "confidence": 0.55
  },
  {
   "claim": "Baba's cut is framed as hero tuning but targets the front-line dive slot only T3-bullet-resist picks can hold.",
   "why": "-7% Base Bullet Resist plus the barrier gutting attacks exactly the commit-to-dive role the KB says is reserved for Apollo/Mo & Krill.",
   "confidence": 0.45
  }
 ],
 "uncertainties": [
  "Whether Baba's -7% bullet resist plus barrier cut is survivable enough to keep her a frontline pick or drops her out of the archetype entirely.",
  "Kelvin's relative win is inferred with no KB entry — magnitude and relationship are low confidence.",
  "What 'Street Brawl' is (mode vs kit) and whether its change matters to the standard game is unclear from the supplied analysis.",
  "Whether Deadman Danny's buffs overcome the unchanged flyer tax — the buff and the context point opposite directions."
 ],
 "what_to_watch": [
  "Baba's WR and pick rate post-nerf — does the frontline slot go to Mo & Krill/Billy outright?",
  "Radiant Regeneration buy rate on Lady Geist, Shiv, Celeste and Baba — does the third trim finally drop it below core?",
  "Deadman Danny WR — does the buff package translate past the anti-air environment?",
  "Healbane/Decay buy rate as regen erodes — the tell that anti-heal is the new sustain answer.",
  "Any hotfix that adds a sustain item or touches the Tough Crate/Bell Tower economy, which would break the continuation thesis."
 ]
}

## Hero analysis (movers only)

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

## Current meta.md

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

## Current item entries (changed items only; may be empty for items not yet in the KB)

Radiant Regeneration:
  name: Radiant Regeneration
  role: healing spirit item
  bought_by:
  - Baba
  - Celeste
  - Kelvin
  - Lady Geist
  - Shiv
  slot: Spirit
  tier: 3
  notes: "08-22 heal on cast 70->65 plus 09-16 per-boon scaling 2->1.7 \u2014 a cumulative\
    \ nerf to healing supports; they can no longer absorb an early deficit."


## What to do

Produce the post-patch knowledge base state. This KB is read by the analyst on the *next* patch, so write it as durable state, not as a patch summary.

1. **meta.md**: rewrite the whole document in this structure (markdown, <= 550 words):
   - `# Meta state` line with `Last patch: Minor Update - 10-14-2026 (2026-10-15)`
   - `## Thesis` — 2-4 sentences: how games are won right now (tempo vs scaling, fight shape, what archetypes carry).
   - `## Economy and systems` — bullets describing the current state of comeback, bounties, objectives, respawn, movement/slows, in present tense with current numbers where known.
   - `## Map` — current map state in present tense: lanes/districts, objectives with timings and values where known, farm sources (Haunt tiers, crates/boxes, Sinner's Sacrifice variants, Buff Containers), pickups (Healing Snacks, Steam Vents), side asymmetry, key routes. Keep it when nothing changed.
   - `## Archetype standing` — one bullet per archetype in play: up/down/stable and why.
   - `## Watchlist` — 3-6 bullets: heroes/items/systems that are uncertain and should be checked against data.
   - `## Recent history` — keep at most 5 bullets, newest first, one line per patch: "Minor Update - 10-14-2026: <headline>". Carry forward existing bullets from the current meta.md, drop the oldest beyond 5.
2. **item_updates**: for each changed item, the fields that changed. Allowed fields: role, bought_by, slot, tier, notes. `bought_by` must list hero names that build it as core or common situational pick, updated for this patch.
3. **change_log**: one line per KB edit you made, for the human to skim.

Tier is one of S/A/B/C/D. Trend is rising/stable/falling.

## Output schema

{
  "meta_md": "full markdown text",
  "item_updates": {"Item Name": {"role": "...", "bought_by": ["..."], "notes": "..."}},
  "change_log": ["Item Name: bought_by +Wraith (now core after rework)", "..."]
}
