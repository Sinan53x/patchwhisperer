# Task: update hero knowledge-base entries after this patch

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

## Hero analysis (this batch only)

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

## Current hero entries (this batch only)

Lady Geist:
  name: Lady Geist
  role: spirit bruiser
  archetypes:
  - tank/frontline
  - late scaler
  - spirit carry
  tier: A
  trend: rising
  why: 'Regen spirit bruiser climbing the front-line slot: the patch''s harder-hitting
    Haunt camps reward her Extra Regen/Mystic Regeneration sustain stack, Buff-Container
    Spirit Resist adds free defense, and her spirit-caster rivals (Celeste, Pocket,
    Mina) keep fading. Capped by the intact no-comeback economy that guts her 0-6-then-farm
    pattern and by the 09-16 Radiant Regeneration trim.'
  core_items:
  - Extra Regen
  - Monster Rounds
  - Mystic Regeneration
  - Radiant Regeneration
  - Kinetic Dash
  - Berserker
  - Spirit Resilience
  build_variants:
  - Regen gun-bruiser
  - Spirit Soul-Exchange
  enabled_by:
  - regen gun-bruiser core (Extra Regen/Mystic Regeneration) untouched
  - harder Haunt camps (regen/sustain value)
  - Buff-Container Spirit Resist
  - Life Drain T3 spirit scaling buff
  - Essence Bomb T3 +4%
  - 'falling spirit-caster rivals: Celeste, Pocket, Mina'
  - Soul Exchange fight-winning ult
  - 'frontline partners: Abrams, Mo & Krill, Dynamo'
  countered_by:
  - 'anti-heal: Decay, Healbane'
  - Radiant Regeneration nerf (hits 98% of her games)
  - tempo meta + comeback rework vs farm-then-scale
  - Lash (S) dive/burst
  - Yamato (S) burst assassin
  - Silver (S) gun tank that out-damages and out-tanks her
  - silence/burst before Soul Exchange
  last_changed_patch: Minor Update - 09-16-2026
  notes: 'City Never Sleeps (09-29, indirect): harder Haunt camps reward her sustain
    stack and Buff-Container Spirit Resist adds free defense; the no-comeback economy
    still caps her farm-then-scale pattern.

    09-16: Life Drain T3 spirit scaling 0.3->0.45 and Essence Bomb T3 26->30% buff
    her bomb/drain, but Radiant Regeneration 2->1.7 per-boon trims her 98%-buy regen
    core.

    WR 46.6% / PR 14.4% is a 14-day pre-patch snapshot; direction is split (vegas
    stable, heresy rising).'
  builds:
  - name: Regen gun-bruiser
    damage: hybrid
    core_items:
    - Extra Regen
    - Monster Rounds
    - Mystic Regeneration
    - Radiant Regeneration
    - Kinetic Dash
    - Berserker
    popularity: primary
    notes: "Buy regen first (Extra Regen 2.7m, Monster Rounds 3.1m) to survive a losing\
      \ lane, then Kinetic Dash + Berserker to frontline and gun-spam; Soul Exchange\
      \ is the finisher \u2014 the vegas '6000 HP fire-rate hero'."
  - name: Spirit Soul-Exchange
    damage: spirit
    core_items:
    - Mystic Regeneration
    - Radiant Regeneration
    - Mystic Burst
    - Bullet Resist Shredder
    - Spirit Resilience
    popularity: secondary
    notes: Caster-leaning variant leaning on the buffed bomb/drain and a Spirit Resilience/Healing
      Booster defensive layer; weaker lane, better burst and bigger ult finisher.
  matchups:
    beats: []
    loses_to:
    - Lash
    - Drifter
  matchup_notes: "The sample lists Lash (41%) and Drifter (45%) under both beats and\
    \ loses_to; both are sub-50%, so treat both as losses and beats as empty. Lash\
    \ (S-tier) throws/dives her before she scales, Drifter (A) wins the melee duel\
    \ on tempo, and she has no positive matchup sample \u2014 low confidence."
  confidence: 0.55
  released_on: null
  provisional: false
Kelvin:
  name: Kelvin
  role: support/healer
  archetypes:
  - support/healer
  - late scaler
  tier: B
  trend: rising
  why: Support/healer whose dome/sustain is more valuable against the patch's harder-hitting
    Haunt camps, with his cheap early sustain core turning Frozen Shelter's spirit
    scaling online early. Still capped by meta anti-heal (Healbane) and mobile dive
    (Lash, Drifter).
  core_items:
  - Extra Regen
  - Extra Charge
  - Extra Spirit
  - Healing Booster
  - Healbane
  - Improved Spirit
  - Rapid Recharge
  - Mystic Expansion
  build_variants:
  - Spirit heal/support
  - Spirit scaling/expansion
  enabled_by:
  - Frozen Shelter spirit scaling
  - harder-hitting Haunt camps (dome/sustain value)
  - Extra Charge / Improved Spirit spirit stacking
  - tempo patch early heal relevance
  - healing-item nerfs (Radiant Regeneration 2->1.7, Restorative Locket trims) hurt
    rival sustain more than his Extra Regen/Healing Booster core
  - strong frontline allies he can heal (Abrams, Dynamo, Mo & Krill, Billy)
  countered_by:
  - anti-heal stacking (Healbane, Toxic Decay)
  - Lash
  - Drifter
  - silence and burst that kill through the dome
  - late-scaling compression (tempo meta)
  last_changed_patch: Minor Update - 09-16-2026
  notes: "City Never Sleeps (09-29, indirect): harder Haunt camps raise the value\
    \ of his dome/sustain; Healing Snacks (10% max HP) reduce the relative value of\
    \ dedicated healing.\nKB core_items were wrong: usage shows a spirit-sustain line\
    \ (Extra Regen/Extra Charge/Healing Booster), not Radiant Regeneration/Healing\
    \ Nova/Fortitude \u2014 corrected.\nChangelog: 09-16 \u2014 Frozen Shelter innate\
    \ regen now scales with spirit power; High-Velocity Rounds (42%, 1.6 min) is lane\
    \ filler, not a build."
  builds:
  - name: Spirit heal/support
    damage: spirit
    core_items:
    - Extra Regen
    - Extra Charge
    - Extra Spirit
    - Healing Booster
    - Healbane
    - Improved Spirit
    popularity: primary
    notes: Stack spirit power to scale Frozen Shelter regen and heal throughput; buys
      Healbane for self/team anti-heal. The default path on most Kelvin games (each
      item 73-81% buy rate).
  - name: Spirit scaling/expansion
    damage: spirit
    core_items:
    - Rapid Recharge
    - Mystic Expansion
    - Mystic Vulnerability
    - Escalating Exposure
    - Greater Expansion
    - Boundless Spirit
    popularity: secondary
    notes: Late luxury line bought past 16 min; Greater Expansion (55.9%) and Boundless
      Spirit (57.5%) have the best WRs but only ~50% buy rates, so treat as win-more
      rather than core.
  matchups:
    beats:
    - Bebop
    - Wraith
    loses_to:
    - Lash
    - Drifter
  matchup_notes: "Bebop (58%) and Wraith (51%) are his best: their spirit burst is\
    \ fully answered by dome + heal, so he simply out-sustains their damage windows.\
    \ Lash (45%) and Drifter (46%) are his worst \u2014 mobile melee initiators that\
    \ reach and burst him before the dome lands, and his low mobility can't disengage.\
    \ Paradox (50%) is a coin flip; a pick initiator can swap him out of position."
  confidence: 0.55
  released_on: null
  provisional: false
Calico:
  name: Calico
  role: mobile assassin
  archetypes:
  - mobile assassin
  tier: A
  trend: stable
  why: "Lane-winning mobile assassin whose tempo snowball still fits the no-comeback\
    \ economy, but the patch's best soul route \u2014 guaranteed Tough Crates \u2014\
    \ needs a Heavy Melee that forces her out of cat form, locking her out of that\
    \ farm. She still bursts squishy carries (Seven, Pocket) before they kite and\
    \ remains capped by tanks she cannot burst."
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
  notes: 'City Never Sleeps: cat form cannot perform the Heavy Melee that Tough Crates
    need, locking her out of the patch''s best soul route; lean on kills/off-map gold.

    Melee-spirit is the default (Melee Lifesteal/Stalker/Spirit Strike/Cold Front/Spirit
    Snatch at 98-99%); the Rapid Recharge/Echo Shard set is gone.

    Last direct patch: Minor Update - 07-28-2026. Snapshot WR 50.2% is a 14-day pre-patch
    baseline.'
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
Shiv:
  name: Shiv
  role: anti-tank spirit bruiser
  archetypes:
  - tank/frontline
  - mobile assassin
  tier: A
  trend: rising
  why: 'Rising anti-tank: the tank/frontline wave (Abrams, Mo & Krill, Billy) feeds
    his current-HP Serrated Knives, and harder camps reward his regen sustain. Burst
    and hook CC (Yamato, Drifter, Bebop) still kill him before regen ramps, and his
    core Radiant Regeneration was trimmed.'
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
  notes: "City Never Sleeps: rising anti-tank \u2014 the bigger front line feeds current-HP\
    \ Serrated Knives and harder camps reward his regen.\nSpirit/regen rebuild confirmed\
    \ (Mystic Regeneration/Extra Regen core); Mystic Vulnerability/Torment Pulse/Escalating\
    \ Exposure run 40-55%.\n09-16: knives current-HP rework + alt-fire buff; Radiant\
    \ Regeneration and Restorative Locket trimmed."
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
  notes: '10-05: no direct change; the trooper-speed regression fix restores on-schedule
    lane crashes for his bully pressure (net near-neutral for an already top frontline),
    and Rat King''s frontline trim thins the competing A-tier bruiser pool.'
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
  why: 'Late-scaling flying spirit burst is the wrong profile for a lane-wins tempo
    meta: comeback souls are gone, early-Rift fights are real, and the new air-drag
    slow bleeds her mid-flight. Seven direct 09-16 nerfs stack on Radiant Regeneration
    and Restorative Locket trims, which is why she sits at B rather than A; the 54.6%
    WR / 26.4% PR is a pre-patch baseline, and she still bursts squishy melee threats
    (Yamato, Pocket) but folds to sustain and mobile initiators.'
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
  notes: "09-16: tier held at B (down from A) \u2014 the seven-nerf stack below plus\
    \ the air-drag flyer tax; Witchmail remains her anti-slow answer.\n54.6% WR /\
    \ 26.4% PR is a 14-day, mostly pre-patch snapshot \u2014 treat as a ceiling, not\
    \ current strength.\n09-16: seven direct nerfs plus indirect item, scaling, and\
    \ air-drag hits."
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
Baba:
  name: Baba
  role: bulky spirit bruiser-caster
  archetypes:
  - spirit carry
  - tank/frontline
  - lane bully
  - initiator
  tier: B
  trend: stable
  why: "Baba is one of the patch's most-picked heroes (51.0% WR, 64.1% PR over 4.7k\
    \ games), and the usage data \u2014 not her old theorycrafted shell \u2014 defines\
    \ her: a regen-stacking spirit bruiser (Extra Charge, Mystic Regeneration, Radiant\
    \ Regeneration) who out-sustains the Haunt/crate economy and forces hub fights\
    \ her AoE hex and silence win. She holds B rather than rising because sustain\
    \ supports (Kelvin, Dynamo, Paige) match her grind and mobile gun pressure (Holliday,\
    \ Wraith) out-pokes her before the ult channel completes. The map-economy patch\
    \ still suits her heavy-melee plus AoE farm profile."
  core_items:
  - Extra Charge
  - Extra Regen
  - Mystic Regeneration
  - Spirit Strike
  - Radiant Regeneration
  - Healing Booster
  - Torment Pulse
  - Compress Cooldown
  - Spirit Snatch
  - Duration Extender
  - Superior Cooldown
  build_variants:
  - Spirit regen bruiser
  - Cooldown caster
  enabled_by:
  - "Tough Crates need heavy melee and Haunts group-and-sustain-check \u2014 Baba\
    \ clears both with Granny Long Legs melee plus a regen stack"
  - Forced, telegraphed hub fights at Sunken Plaza and Bell Tower reward her AoE hex
    and silence on grouped enemies
  - Global slows -20% / air drag 35% favor grounded bruisers over flyers
  - No-comeback economy rewards her early camp income converting into an unkillable
    mid-game frontline
  countered_by:
  - 'Anti-heal vs her regen wall: Healbane, Decay, Toxic Bullets'
  - 'Sustain supports that neutralize her grind: Kelvin, Dynamo, Paige'
  - 'Channel interrupts/silence on her ult: Knockdown, Cursed Relic, Silencer'
  - 'Burst/mobile gun pressure she can''t out-poke: Holliday, Wraith; Plated Armor
    and Bullet Resilience vs her gun damage'
  last_changed_patch: Mind the Birds!
  notes: "7-day check-in (2026-10-13): tier B -> B, WR 51%, PR 64% over 305220 matches.\n\
    1) Usage overrides the prior entry: Boundless Spirit/Arcane Surge and the on-hit/melee\
    \ shells (High-Velocity Rounds, Lifestrike, Colossus) barely register in high-rank\
    \ buys \u2014 the real core is regen + cooldown-spirit items. 2) Matchups replaced\
    \ by 7-day data (beats Solomon/Apollo/Calico; loses to Kelvin/Dynamo/Paige), which\
    \ differs sharply from the day-0 guesses. 3) Changelog: no Baba kit change since\
    \ Mind the Birds!; 10-05 was a trooper-speed fix only, leaving her map-economy\
    \ engine intact."
  builds:
  - name: Spirit regen bruiser
    damage: spirit
    core_items:
    - Extra Charge
    - Extra Regen
    - Mystic Regeneration
    - Spirit Strike
    - Radiant Regeneration
    - Healing Booster
    - Torment Pulse
    popularity: primary
    notes: 'The every-game shell: stack regen and HP to out-sustain Haunt chip and
      hub fights, with Torment Pulse turning her into an AoE aura; Extra Charge (98%),
      Mystic Regeneration (95%) and Radiant Regeneration (94%) are near-universal.'
  - name: Cooldown caster
    damage: spirit
    core_items:
    - Compress Cooldown
    - Spirit Snatch
    - Duration Extender
    - Superior Cooldown
    - Rapid Recharge
    popularity: secondary
    notes: Late slot conversion (~20-24 min) to spam Threadsap/Brew/ult and extend
      hex/silence; Duration Extender (59.3%) and Superior Cooldown (58.8%) are her
      best-winrate items, while Rapid Recharge (48.2%) is a trap.
  matchups:
    beats:
    - Solomon
    - Apollo
    - Calico
    - Grey Talon
    - Mina
    loses_to:
    - Kelvin
    - Dynamo
    - Paige
    - Holliday
    - Wraith
  matchup_notes: "She beats telegraphed control/spirit heroes she can silence and\
    \ out-sustain \u2014 Solomon (67%) and Apollo (59%), plus Calico (58%), who cannot\
    \ heavy-melee the crate economy so Baba out-farms the tempo assassin. She loses\
    \ to sustain that matches her regen \u2014 Kelvin (39%) and Dynamo (41%) \u2014\
    \ and to S-tier lane support Paige (43%) and mobile gun pressure Holliday (44%)/Wraith\
    \ (45%) she cannot out-poke before the channel lands."
  confidence: 0.55
  released_on: '2026-10-06'
  provisional: false
Solomon:
  name: Solomon
  role: control support / zone-control strategist
  archetypes:
  - support/healer
  - initiator
  - poke/siege
  tier: B
  trend: rising
  why: 'Solomon is a cooldown-driven zone controller: persistent bishop zones (slow
    + spirit ticks + diagonal mines, T3 stacks a -2.5/stack armor shred) and a two-rook
    immobilize convert telegraphed hub fights better than raw DPS. Kingside Knight
    (ally stamina + barrier, double barrier self-cast, T3 cleanse) plus an invulnerable
    reposition on the piece makes him a genuine enabler under the 38s respawn tax.
    He is not a top camp-clearer, so his income rides on heavy-melee crate routes
    and team souls rather than solo jungle farming.'
  core_items:
  - Extra Spirit
  - Superior Cooldown
  - Mystic Burst
  - Boundless Spirit
  build_variants:
  - Cooldown control
  - Barrier support
  - Gun
  enabled_by:
  - Hub-fight meta (Sunken Plaza ~5-8 min, Bell Tower 8+) rewarding telegraphed zone
    control
  - Superior Cooldown / Arcane Surge cooldown stacking
  - Heavy melee 116 opening Tough Crates for guaranteed 58-soul routes
  - Barrier + cleanse support value under the 38s respawn tax
  countered_by:
  - Silence (Silencer, Silence Wave) denying the cooldown loop
  - Unstoppable (ignores rook immobilize)
  - Debuff Reducer (shrinks slow/immobilize)
  - Knockdown
  - Burst mobility landing before the self-cast invuln
  last_changed_patch: Released 2026-10-09
  notes: "Day-0 kit read (2026-10-09), provisional \u2014 data check-in due 2026-10-16.\n\
    Develop Queen tooltip is empty \u2014 ult power is the single biggest unknown;\
    \ T2 hints a 'Checkmate' threshold (200/5) scaled by slow. Gun builds are losing,\
    \ spirit/cooldown builds winning, but on small novelty samples. If 7-day data\
    \ shows the Knight/Divine Barrier build clustering >55% WR, promote to A; if zone\
    \ impact proves marginal in the fast-cast meta, drop toward C."
  builds:
  - name: Cooldown control
    damage: spirit
    core_items:
    - Extra Spirit
    - Superior Cooldown
    - Mystic Burst
    - Arcane Surge
    - Boundless Spirit
    popularity: primary
    notes: Spams bishop/rook on short cooldowns; the winning cluster (Mystic Burst
      71% early, Arcane Surge 80% mid).
  - name: Barrier support
    damage: spirit
    core_items:
    - Divine Barrier
    - Guardian Ward
    - Healbane
    - Healing Booster
    - Superior Duration
    popularity: secondary
    notes: Leans into Kingside Knight barrier + cleanse for teamfights; Divine Barrier
      sits at 62% late WR.
  - name: Gun
    damage: gun
    core_items:
    - High-Velocity Rounds
    - Swift Striker
    - Extended Magazine
    popularity: niche
    notes: "Swift Striker is a trap here (20% mid, 33% late WR) \u2014 no kit reason\
      \ to buy attack speed yet."
  matchups:
    beats:
    - Drifter
    - Abrams
    - Grey Talon
    - Seven
    loses_to:
    - Lash
    - Holliday
    - Calico
    - Vindicta
  matchup_notes: 'Bishop tiles plus rook immobilize punish anything that must physically
    occupy hub space, so melee divers and low-mobility poke (Grey Talon, Seven) get
    zoned. He in turn dies to burst mobility that lands before he can self-cast Knight''s
    invuln (Lash, Holliday, Calico) and to Vindicta''s range. He is a strong pick-enabler:
    immobilize + shred set up Lash, Holliday and Paradox dives.'
  confidence: 0.35
  released_on: '2026-10-09'
  provisional: true
Deadman Danny:
  name: Deadman Danny
  role: Flying marksman / dive-pick
  archetypes:
  - gun carry
  - mobile assassin
  - initiator
  tier: C
  trend: stable
  why: "A marksman with a full dive/pick kit \u2014 Chimera overheat explosion, Close\
    \ The Deal grab-slam, plus a genuine shred/mark gun package \u2014 so on paper\
    \ he is a lane-to-hub skirmisher, not a backline turret. But he is a flyer in\
    \ an explicitly anti-flyer patch (air drag 35%, slows hit him airborne by his\
    \ own tooltip, Silver's Bola grounds), so his signature mobility is a tax, not\
    \ an edge. The 34.9% WR over 0.2% PR is novelty-deflated, but the kit and item\
    \ scatter do not contradict the bad signal."
  core_items:
  - High-Velocity Rounds
  - Express Shot
  - Bullet Resist Shredder
  - Superior Cooldown
  build_variants:
  - Shred/mark gun
  - Ability burst
  - Dive bruiser
  enabled_by:
  - Grouped hub fights (Sunken Plaza, Bell Tower) that reward the overheat-dive AoE
    and launch
  - AoE clear of grouped Haunt camps
  - An anchor/initiator teammate to hold targets so Strix Salvo marks and Close The
    Deal land
  countered_by:
  - Anti-air (Silver's Weighted Bola)
  - Silence / Knockdown / Silencing Hex / Bebop hook
  - "Slows \u2014 doubled by the global air-drag tax plus his own airborne-slow tooltip"
  - Plated Armor vs his gun; Debuff Reducer vs his mark and fading slow
  - His own no-hero-hit self-stun combined with the long death tax
  last_changed_patch: Released 2026-10-13
  notes: "Day-0 kit read (2026-10-13), provisional \u2014 data check-in due 2026-10-20.\n\
    Provisional C on a ~2-day sample; 34.9% WR / 0.2% PR is novelty-deflated but directionally\
    \ bad, and the build pool is unformed (many 0-20% win picks). Would revise up\
    \ if WR clears ~45% as PR grows and a mark/charged-shot build consolidates; down\
    \ if the flyer tax holds and no build lands."
  builds:
  - name: Shred/mark gun
    damage: hybrid
    core_items:
    - High-Velocity Rounds
    - Express Shot
    - Bullet Resist Shredder
    - Superior Cooldown
    popularity: primary
    notes: Jettison Fuel's bullet-resist shred stacked with Bullet Resist Shredder
      amplifies the marksman damage; HV Rounds (86% pick) and Express Shot carry the
      charged-shot mark-consume.
  - name: Ability burst
    damage: spirit
    core_items:
    - Boundless Spirit
    - Superior Cooldown
    - Arctic Blast
    popularity: secondary
    notes: Scales Strix Salvo marks plus Close The Deal and overheat-dive spirit explosions;
      36% late Boundless Spirit pick shows players testing it.
  - name: Dive bruiser
    damage: hybrid
    core_items:
    - Fortitude
    - Extra Health
    - Indomitable
    popularity: niche
    notes: "Survivability to blunt the whiff-self-stun and always-explode-on-death\
      \ pattern; no clear payoff yet \u2014 Fortitude shows 9% win late."
  matchups:
    beats:
    - Seven
    - Celeste
    - Graves
    loses_to:
    - Silver
    - Lash
    - Apollo
  matchup_notes: 'He threatens squishy, grouped or immobile carries he can mark with
    Salvo then burst with a dive or Close The Deal. He loses to anti-air and disruption:
    Silver''s Weighted Bola grounds flyers on top of out-trading him, Lash can fling
    him out of dives, and Apollo out-lanes him. Silences/knockdowns and a whiffed
    dive (self-stun) are his own worst enemy given the 38s respawn tax.'
  confidence: 0.4
  released_on: '2026-10-13'
  provisional: true


## What to do

Produce the post-patch knowledge base state for the heroes in this batch. This KB is read by the analyst on the *next* patch, so write it as durable state, not as a patch summary.

1. **hero_updates**: for each mover, the fields that changed. Allowed fields: role, archetypes, tier, trend, why, core_items, builds (full replacement list of {name, damage, core_items, popularity, notes}), matchups ({beats, loses_to}), enabled_by, countered_by, notes. When an item change kills or creates a build, update `builds`, not just `notes`. When another hero's change alters a matchup, update `matchups`. Set `last_changed_patch` to "Minor Update - 10-14-2026" for heroes that had direct changes. `why` is 1-2 sentences of present-tense state ("strong because X; weak to Y"), not a changelog. `notes` may hold a short changelog line (keep the last 3 lines, newest first). Do not touch heroes not in this batch.

   For each hero, output only the fields whose value actually changes. Omit any field that stays the same — omitted fields are kept as-is in the KB. Include `builds` only if at least one build is created, killed, or its core items change; when you include it, it is a full replacement list. Include `matchups` only if a matchup changes.
2. **change_log**: one line per KB edit you made, for the human to skim.

Tier is one of S/A/B/C/D. Trend is rising/stable/falling.

## Output schema

{
  "hero_updates": {"Hero Name": {"tier": "A", "trend": "falling", "why": "...", "core_items": ["..."], "last_changed_patch": "...", "notes": "..."}},
  "change_log": ["Hero Name: tier S -> A (Card Trick heal nerfs + Veil Walker loss)", "..."]
}
