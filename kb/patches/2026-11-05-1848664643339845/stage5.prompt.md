# Task: verdicts for the reader's hero pool

Patch: Minor Update - 11-04-2026 (2026-11-05)

## Synthesis

{
 "patch_size": "minor",
 "size_why": "Thirty-six lines but zero systems, economy, map or objective changes — it is all hero kit tuning plus one item curve. The tier list moves a little; how souls are made and where fights happen does not move at all.",
 "headline": "A cleanup pass on the 10-30 outliers: Valve trims the strong (Baba, Celeste, Deadman Danny), feeds the weak (Rat King, Apollo, Mo & Krill) and quietly shrinks stacked anti-heal.",
 "meta_thesis": {
  "previous": "Leads must be converted into Guardians and Walkers fast because the 10-30 comeback levers and richer Haunts keep paying the trailing team, so one-cycle camp clearers who spend the lead early and late scalers with a farm floor are the winners.",
  "new": "Identical economy, identical map: the game is still won by farming Haunts and converting before comeback gold arrives. What changed is who survives the mid-fight — stacked anti-heal is weaker, so kit healers and self-sustain bruisers hold longer, and the outlier frontlines from 10-30 were trimmed.",
  "relationship": "continuation",
  "why": "The General/systems sections are empty and the only non-hero change is Healbane's stacking curve. Every mover here comes from individual kits and one item's diminishing returns, not from soul income or objective timers."
 },
 "winners": [
  {
   "hero": "Rat King",
   "why": "Buffs land exactly where 10-30 hurt: bullet damage 5.7->5.8, ammo 24->26, and Rule, Ratannia! T1 now cuts 25s off the 180s ult.",
   "indirect": false
  },
  {
   "hero": "Kelvin",
   "why": "The multi-source anti-heal that blanked Frozen Shelter caps at 72% (was 82.2%), so the best healer is harder to fully shut off.",
   "indirect": true
  },
  {
   "hero": "Apollo",
   "why": "Riposte Pommel Hit now disarms and T2 holds 0.6s->0.7s, turning his parry into a gun-carry shutdown — though it is still an immobilize, not a stun, so channels no longer break.",
   "indirect": false
  },
  {
   "hero": "Mo & Krill",
   "why": "Scorn heal 1.2x->1.3x, Burrow radius +0.5m and Combo HP per kill 40->50 give the tank more of the thing he does; the anti-heal cap compounds it.",
   "indirect": false
  },
  {
   "hero": "Ivy",
   "why": "The 10-30 stack system that crushed tether healing is partially reversed (4-stack 82.2%->72%), and her gun core is untouched.",
   "indirect": true
  }
 ],
 "losers": [
  {
   "hero": "Celeste",
   "why": "Every pick tool shrank at once: silence T3 +1.25s->+0.75s, Radiant Daggers 30m->25m, Shining Wonder slow -32%->-28% and cooldown 160s->170s.",
   "indirect": false
  },
  {
   "hero": "Deadman Danny",
   "why": "Close The Deal execute +75%->+55%, Strix Salvo spirit scaling -8% and Chimera Mk1 T2 heal 150->125 gut the dive-pick identity on a hero who must commit.",
   "indirect": false
  },
  {
   "hero": "Baba",
   "why": "Spirit Resistance scaling 0.7->0.5 plus melee damage -10% per boon cuts the resist wall her regen bruiser build stands behind.",
   "indirect": false
  },
  {
   "hero": "Drifter",
   "why": "His anti-heal bruiser variant stacked built-in heal cut on Healbane/Toxic Bullets — exactly the two-source case trimmed 57.8%->54.7% — and Apollo's rework sharpens a listed loss.",
   "indirect": true
  },
  {
   "hero": "Mina",
   "why": "Both worst matchups got harder: Mo & Krill's Scorn/Burrow buffs and Ivy's rebound from the anti-heal cap, while her single-target rotation gains nothing.",
   "indirect": true
  }
 ],
 "non_obvious_calls": [
  {
   "claim": "Healbane was not nerfed — single-source anti-heal is identical, so this is a tax on redundant buyers, not a nerf to the item.",
   "why": "Only the 2-stack (57.8%->54.7%) and 4-stack (82.2%->72%) curves moved; the first purchase decision is unchanged and triple-Healbane comps are the actual target.",
   "confidence": 0.8
  },
  {
   "claim": "Baba is still a top frontline despite the nerf stack.",
   "why": "Tiers come from measured data, not notes: 54.4% win rate after every resist and melee cut, same shape as her 10-30 nerfs that left her top of the table.",
   "confidence": 0.65
  },
  {
   "claim": "Rat King's real buff is a talent line, not the stat bumps.",
   "why": "Rule, Ratannia! T1 adding -25s cooldown is the cheapest answer to the 180s ult that 10-30 left as his problem — earlier than any Cooldown item.",
   "confidence": 0.6
  },
  {
   "claim": "Apollo's Riposte is a rework, not a straight buff.",
   "why": "Pommel Hit is an immobilize plus parry disable, so it can no longer interrupt channels; the added disarm pays into gun carries only, and the Pummel parry-strip wording stays unresolved.",
   "confidence": 0.55
  }
 ],
 "uncertainties": [
  "The Pummel 'ends a preexisting parry' line: whether it strips the target's parry state or Apollo's own is unclear, and it decides how strong his duel is.",
  "Baba's tier: 54.4% win rate argues S, but a ~29% resist-scaling cut is structural — she may drift a tier by week two rather than immediately.",
  "Graves' 57.5% win rate still conflicts with the KB's 48.5%/21% snapshot; nothing here touches her kit, so the number cannot be validated by this patch.",
  "Whether Celeste's nerfs actually cost her a tier outside the losing lanes she already dominated, since her burst numbers were untouched."
 ],
 "what_to_watch": [
  "Healbane purchases per team — if the average drops toward one, the anti-heal coverage plan is dead and kit healers rebound further.",
  "Kelvin, Ivy and Rem win rates: the cleanest read on whether the stacking cap is worth three points of heal throughput.",
  "Deadman Danny's pick rate and win rate — a fifth off the execute should show fast on a dive hero.",
  "Mo & Krill pick rate into frontline-heavy lobbies, as the answer to Baba and Viscous.",
  "Celeste's T3 talent pick rate: if players abandon the silence talent, her pick identity shifted, not just her numbers."
 ],
 "biggest_changes": [
  {
   "kind": "item",
   "subject": "Healbane",
   "title": "Second and third anti-heal copies are much weaker",
   "why": "4-stack heal cut 82.2%->72% with 20% faster decay; one source is unchanged.",
   "effect": "down"
  },
  {
   "kind": "hero",
   "subject": "Celeste",
   "title": "Silence, cast range and ult all shortened",
   "why": "Dazzling Trick silence +1.25s->+0.75s and Radiant Daggers 30m->25m cut her pick window 40%.",
   "effect": "down"
  },
  {
   "kind": "hero",
   "subject": "Rat King",
   "title": "Ult cooldown talent and gun stats buffed",
   "why": "Rule, Ratannia! T1 adds -25s cooldown and ammo goes 24->26.",
   "effect": "up"
  },
  {
   "kind": "hero",
   "subject": "Baba",
   "title": "Resist wall and melee damage cut again",
   "why": "Spirit Resistance scaling 0.7->0.5 and melee damage -10% per boon.",
   "effect": "down"
  },
  {
   "kind": "hero",
   "subject": "Deadman Danny",
   "title": "Execute and dive sustain both trimmed",
   "why": "Close The Deal bonus damage +75%->+55% and Chimera Mk1 T2 heal 150->125.",
   "effect": "down"
  },
  {
   "kind": "hero",
   "subject": "Apollo",
   "title": "Parry now disarms gun carries",
   "why": "Pommel Hit adds a disarm and Riposte T2 duration goes +0.6s->+0.7s — but it no longer interrupts channels.",
   "effect": "up"
  },
  {
   "kind": "hero",
   "subject": "Mo & Krill",
   "title": "More Scorn healing, bigger Burrow, healthier grab",
   "why": "Scorn heal 1.2x->1.3x, Burrow damage radius +0.5m, Combo HP per kill 40->50.",
   "effect": "up"
  }
 ]
}

## Hero analysis entries for the pool heroes

[
 {
  "hero": "Wraith",
  "in_notes": false,
  "direction": "neutral",
  "magnitude": "minor",
  "confidence": 0.45,
  "direct_reasons": [],
  "indirect_reasons": [
   "Celeste (a listed loss) lost silence duration and slow, trimming one bad lane.",
   "Ivy's tether heals are now harder to stack anti-heal onto, and Ivy is also a listed loss \u2014 roughly cancels the above."
  ],
  "build_changes": [],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Untouched again: one bad lane got easier, another got harder, nothing in her gun core moved.",
  "verdict": "keep",
  "rows": [],
  "change_kind": "none",
  "change_size": "none"
 },
 {
  "hero": "Warden",
  "in_notes": false,
  "direction": "neutral",
  "magnitude": "none",
  "confidence": 0.5,
  "direct_reasons": [],
  "indirect_reasons": [
   "Healbane's stacked cut is weaker, so the sustain he has to cage through (Ivy 48%) is marginally harder to suppress, and Mo & Krill \u2014 who tanks his cage \u2014 took direct Scorn/Burrow/Combo buffs."
  ],
  "build_changes": [],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Nothing for Warden this patch; his late gun window is the same race against the clock.",
  "verdict": "keep",
  "rows": [],
  "change_kind": "none",
  "change_size": "none"
 }
]

## Item analysis entries that mention a pool hero

[]

## Knowledge base entries for the pool heroes

Wraith:
  name: Wraith
  role: gun carry
  archetypes:
  - gun carry
  - late scaler
  tier: B
  trend: falling
  why: 'Fire-rate gun carry with a high floor and no growth path: the 09-16 spirit
    on-hit gutting pushed her fully onto fire-rate M1, and this patch only trims her
    Card Trick heal 60->45 and Project Mind (46->50s, initial cast 0.75->1s) without
    touching the gun core. Cheap anti-gun defence got better in the same patch (Bullet
    Resilience 30->35%, Return Fire''s 10% bullet resist now on the tooltip), so she
    outclasses no one in her slot.'
  core_items:
  - Monster Rounds
  - Quicksilver Reload
  - Rapid Rounds
  - Extra Spirit
  - Swift Striker
  - Surge of Power
  - Dispel Magic
  - Ricochet
  - Spirit Lifesteal
  build_variants:
  - Spirit on-hit
  - Sustain gun
  enabled_by:
  - Ricochet
  - Quicksilver Reload
  - Abrams
  - Mo & Krill
  countered_by:
  - Plated Armor
  - Yamato
  - Silver
  - Paige
  - Sinclair
  last_changed_patch: Halloween 2026 + Gameplay Update
  notes: "Halloween 2026 + Gameplay Update (10-30, direct): Card Trick heal 60->45\
    \ and Project Mind 46->50s with a slower 0.75->1s initial cast trim the only sustain\
    \ and the repositioning her survival plan runs on; her fire-rate gun core (Monster\
    \ Rounds/Quicksilver Reload/Rapid Rounds/Swift Striker/Ricochet) is untouched.\n\
    09-16: Card Trick heal 75->60, heal scaling 0.75->0.5, resist shred -8->-7% (T3\
    \ -5->-4%), T3 slow +20->+15%; Mercurial Magnum + Spiritual Overflow gutted and\
    \ Plated Armor now blanks Full Auto spirit damage \u2014 on-hit-spirit core weakened,\
    \ lean pure gun.\nCreator-cited Capacitor/Slowing Hex appear in none of the top-15\
    \ item slots; usage says the real core was spirit on-hit (Quicksilver Reload 100%,\
    \ Mercurial Magnum 93%) \u2014 Magnum now weakened."
  builds:
  - name: Gun carry (pure gun)
    damage: gun
    core_items:
    - Monster Rounds
    - Quicksilver Reload
    - Rapid Rounds
    - Swift Striker
    - Surge of Power
    - Ricochet
    popularity: primary
    notes: 'Post-09-16 rebuild: the Mercurial Magnum / on-hit-spirit package is weakened
      (Magnum base 25->20% and scaling 0.49->0.38, Spiritual Overflow nerfed, Plated
      Armor now blanks Full Auto''s spirit damage), so stack fire rate and gun damage
      instead of spirit procs; Quicksilver Reload (100% share) is still the signature
      early buy and Ricochet still turns her into an AoE-delete.'
  - name: Sustain gun
    damage: gun
    core_items:
    - Rapid Rounds
    - Swift Striker
    - Dispel Magic
    - Spirit Lifesteal
    popularity: secondary
    notes: Fire-rate gun line with Dispel Magic (85%) and Spirit Lifesteal (53% item
      WR) to survive being focused; take it when you're the dive target, not when
      you're free-hitting.
  matchups:
    beats:
    - Grey Talon
    - McGinnis
    - Mirage
    - Graves
    - Apollo
    loses_to:
    - Paige
    - Sinclair
    - Celeste
    - Dynamo
    - Ivy
  matchup_notes: "Card Trick's homing spirit damage plus Full Auto's AoE delete squishy\
    \ poke/siege heroes who cannot dodge \u2014 Grey Talon (60%), McGinnis (56%),\
    \ Mirage (56%). She folds to CC-and-dive she can't out-range: Paige's lane pressure\
    \ (43%), Dynamo's initiation (46%), Sinclair's burst (46%)."
  confidence: 0.6
  released_on: null
  provisional: false
Warden:
  name: Warden
  role: gun carry
  archetypes:
  - gun carry
  - late scaler
  tier: B
  trend: stable
  why: 'The kit got real: Alchemical Flask travels 40% faster, Willpower +20% speed
    and Last Stand T2 is 50 DPS at -40s cooldown, so his debuff-and-cage window lands
    on reaction. But Shadow Weave now demands 6s of pre-stealth and HVR lost a quarter
    of its velocity, so he still has no answer to the clock that kills a late gun
    scaler.'
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
  last_changed_patch: Halloween 2026 + Gameplay Update
  notes: "Halloween 2026: flask 40% faster travel (weapon damage -30% from -25%),\
    \ Willpower +15->+20% speed, Last Stand T2 +40.5->50 DPS with -40s cooldown; Shadow\
    \ Weave reworked into a 6s pre-stealth ambush item and HVR velocity 60->45% \u2014\
    \ kit up, items down, tier holds C.\nShh... This Won't Hurt a Bit. (10-20, indirect):\
    \ Steam Vents give every hero the invis-engage he pays Shadow Weave for, flattening\
    \ his one unique tool while tempo still ends games before his late gun spike.\n\
    Paint the Town: no direct line; contested Soul Bags and earlier Bell Tower/Sunken\
    \ Plaza objectives close games even faster, deepening the wait a late gun scaler\
    \ cannot afford \u2014 no core item moved."
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
    notes: Stack weapon tiers to farm fast and stat-check into the mid-game spike;
      HVR keeps the slot as a cheap stat-stick but at 45% velocity it no longer guarantees
      max-range hits, so value it for stats, not poke.
  - name: Cage bruiser
    damage: hybrid
    core_items:
    - Shadow Weave
    - Spirit Lifesteal
    - Enduring Speed
    - Sprint Boots
    popularity: secondary
    notes: "Shadow Weave is now a setup item: +50% ambush weapon damage only reaches\
      \ full power after 6s of stealth and the fire rate is gone, so pre-commit the\
      \ stealth before walking to the cage instead of reacting with it \u2014 and\
      \ pair with Battle Vest/Bullet Lifesteal, which never turn off."
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


## The reader's pool

Wraith, Warden

## What to do

For each hero in the pool give a verdict a player can act on tonight:

- `keep`: still a good pick; direct + indirect effects are neutral or positive, or negative but minor relative to the hero's standing.
- `watch`: real change in either direction whose size is uncertain; play but adapt (usually a build or timing change).
- `bench`: the hero lost what made them good (core build gutted, archetype hard-countered by systems change, major kit nerf on a hero that was not over-performing).

Explain the direct effects and the indirect effects separately so the reader can see the indirect ones (they are what they would miss). Give concrete build adjustments (item to drop, item to add, talent order) only if the analysis supports them; otherwise leave the list empty. Keep every field short; the whole card must read in 20 seconds.

## Output schema

{
  "verdicts": [
    {
      "hero": "name",
      "verdict": "keep|watch|bench",
      "one_liner": "<= 20 words",
      "direct": "1-2 sentences on the hero's own changes; 'No direct changes.' if none",
      "indirect": "1-2 sentences on item/system effects; 'No meaningful indirect effects.' if none",
      "build_adjustments": ["short imperative sentences"],
      "confidence": 0.0
    }
  ]
}
