# Task: update the knowledge base after this patch

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

## Hero analysis (movers only)

[
 {
  "hero": "Seven",
  "in_notes": false,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.55,
  "direct_reasons": [],
  "indirect_reasons": [
   "Healbane sits in his spirit AoE core as the sustain-comp answer; with the 2-stack case 57.8%->54.7% and the ceiling 82.2%->72%, that counter-build is less of a hard counter.",
   "Ivy (a listed Seven loss, 42%-ish) is one of the clearest Healbane-stacking winners, so the tether he could previously shut down comes back."
  ],
  "build_changes": [
   "Keep Healbane as your single anti-heal slot, but if a teammate already runs it, spend that Vitality slot elsewhere \u2014 the second source is now worth far less.",
   "No change to the Monster Rounds/Cultist Sacrifice farm spine; the jungle economy is untouched."
  ],
  "tier_before": "S",
  "tier_after": "S",
  "one_liner": "Still the fastest farmer in the game; Healbane is just a worse second buy when a teammate already has it.",
  "verdict": "keep",
  "rows": [],
  "change_kind": "none",
  "change_size": "none"
 },
 {
  "hero": "Vindicta",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.45,
  "direct_reasons": [],
  "indirect_reasons": [
   "Celeste took a kit-wide nerf (Shining Wonder slow -32%->-28%, cooldown 160->170s, Radiant Daggers cast range 30->25m) and is one of Vindicta's worst lanes at 46%."
  ],
  "build_changes": [],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Nothing in her notes; one bad lane (Celeste) got gutted, but the flyer tax is unchanged.",
  "verdict": "keep",
  "rows": [],
  "change_kind": "none",
  "change_size": "none"
 },
 {
  "hero": "Lady Geist",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [],
  "indirect_reasons": [
   "She buys no Healbane, so the anti-heal stack trim is pure upside: Radiant Regeneration and Mystic Regeneration are harder to fully suppress.",
   "Drifter's anti-heal bruiser variant (Veil Walker/Healbane/Tankbuster) is the composition the stack nerf hits hardest \u2014 and Drifter is a listed Geist loss.",
   "Celeste, one of the falling spirit-caster rivals her Soul-Exchange line was measured against, lost cast range and slow."
  ],
  "build_changes": [
   "Regen core (Extra Regen/Mystic Regeneration/Radiant Regeneration) is now slightly more reliable out of the dive \u2014 no swap needed."
  ],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Stacked anti-heal can't choke her regen as hard anymore, so the sustain bruiser gets a small refund.",
  "verdict": "keep",
  "rows": [],
  "change_kind": "none",
  "change_size": "none"
 },
 {
  "hero": "Paradox",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.4,
  "direct_reasons": [],
  "indirect_reasons": [
   "Celeste, a listed loss at 43%, lost Radiant Daggers cast range 30m->25m, T3 silence -1.25s->-0.75s and Shining Wonder slow -32%->-28% \u2014 the out-trade lane gets noticeably softer."
  ],
  "build_changes": [],
  "tier_before": "D",
  "tier_after": "D",
  "one_liner": "No lines for her; one losing lane got weaker, which doesn't fix a 46% hero.",
  "verdict": "keep",
  "rows": [],
  "change_kind": "none",
  "change_size": "none"
 },
 {
  "hero": "Dynamo",
  "in_notes": false,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.55,
  "direct_reasons": [],
  "indirect_reasons": [
   "Mo & Krill \u2014 his worst listed loss \u2014 got Scorn heal 1.2x->1.3x, Burrow damage radius +0.5m and Combo health per kill 40->50, so the durable frontline that eats Singularity is better at exactly that.",
   "Sand Blast T2 now slows -28% (from -24%) and cuts dash distance -28% (from -26%), making his engage easier to peel.",
   "No item driver: he buys no Healbane and nothing in his Extra Charge/Arcane Surge/Refresher spine moved."
  ],
  "build_changes": [
   "Keep Unstoppable/Refresher on the channel \u2014 expect more Mo & Krill frontlines that survive the whole ult.",
   "Value Mystic Expansion/duration for wider Singularity pulls rather than trying to out-burst the frontline."
  ],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Still wins the scheduled hub fights, but Mo & Krill's buffs make the wall that eats Singularity taller.",
  "verdict": "keep",
  "rows": [],
  "change_kind": "none",
  "change_size": "none"
 },
 {
  "hero": "Kelvin",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.6,
  "direct_reasons": [],
  "indirect_reasons": [
   "Healbane one source is untouched but the ceiling dropped 82.2%->72% and stacks decay 20% faster \u2014 the multi-source anti-heal plan that was his worst system change can no longer fully shut off Frozen Shelter or Healing Booster.",
   "Drifter, a listed Kelvin loss, leaned on the anti-heal bruiser composition this nerf targets."
  ],
  "build_changes": [
   "Healbane stays a fine buy for your own team anti-heal; don't expect a second or third source on the enemy team to blank your dome anymore.",
   "Extra Regen/Healing Booster spirit core is unchanged \u2014 keep funding heal throughput."
  ],
  "tier_before": "S",
  "tier_after": "S",
  "one_liner": "Stacked anti-heal can't fully blank the dome now, so the best healer in the game gets quietly better.",
  "verdict": "keep",
  "rows": [],
  "change_kind": "none",
  "change_size": "none"
 },
 {
  "hero": "Holliday",
  "in_notes": false,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [],
  "indirect_reasons": [
   "Mo & Krill, her listed hard loss, got Sand Blast T2 to -28% slow and -28% dash distance (from -24%/-26%), a bigger Burrow radius (+0.5m) and Combo health per kill 40->50 \u2014 point-blank lockdown that punishes her commit got stronger across the kit.",
   "Her own anti-heal/Healbane exposure is nil, so the item change does nothing for her."
  ],
  "build_changes": [
   "Buy Unstoppable/Debuff Reducer earlier into Mo & Krill \u2014 the -28% slow and larger Burrow radius make the entry harder to escape.",
   "Lean on bounce-pad pre-placement rather than reactive lasso commits into the tank frontline."
  ],
  "tier_before": "D",
  "tier_after": "D",
  "one_liner": "Nothing in her notes, but Mo & Krill's stronger slow and bigger Burrow make her worst matchup worse.",
  "verdict": "keep",
  "rows": [],
  "change_kind": "none",
  "change_size": "none"
 },
 {
  "hero": "Bebop",
  "in_notes": false,
  "direction": "neutral",
  "magnitude": "none",
  "confidence": 0.5,
  "direct_reasons": [],
  "indirect_reasons": [
   "Celeste, a listed counter (he wins 44% into her), lost Dazzling Trick silence (T3 +1.25s->+0.75s), Radiant Daggers range (30m->25m) and Shining Wonder cooldown (160s->170s) \u2014 a small relief in a lane he was losing.",
   "Healbane's stacked ceiling falls 82.2%->72%, so the sustain that already erases his burst (Kelvin, 42%) is now harder for a second buyer to cut \u2014 a small extra tax on the hook combo."
  ],
  "build_changes": [],
  "tier_before": "C",
  "tier_after": "C",
  "one_liner": "No lines for Bebop; a single-target hook still has nothing to punish in this economy.",
  "verdict": "watch",
  "rows": [],
  "change_kind": "none",
  "change_size": "none"
 },
 {
  "hero": "Calico",
  "in_notes": false,
  "direction": "neutral",
  "magnitude": "none",
  "confidence": 0.45,
  "direct_reasons": [],
  "indirect_reasons": [
   "Apollo, a 55% winner into her, added a Riposte Pommel Hit disarm, a parry-ending Pummel and T2 duration 0.6s->0.7s; a disarm barely touches her melee-spirit burst, so the squeeze is small."
  ],
  "build_changes": [],
  "tier_before": "C",
  "tier_after": "C",
  "one_liner": "Untouched kit, untouched jungle income \u2014 still a sharper diver with no safety net.",
  "verdict": "keep",
  "rows": [],
  "change_kind": "none",
  "change_size": "none"
 },
 {
  "hero": "Grey Talon",
  "in_notes": false,
  "direction": "neutral",
  "magnitude": "none",
  "confidence": 0.5,
  "direct_reasons": [],
  "indirect_reasons": [],
  "build_changes": [],
  "tier_before": "D",
  "tier_after": "D",
  "one_liner": "Nothing in this patch fixes a sub-50% flyer with no camp or crate route.",
  "verdict": "watch",
  "rows": [],
  "change_kind": "none",
  "change_size": "none"
 },
 {
  "hero": "Mo & Krill",
  "in_notes": true,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.65,
  "direct_reasons": [
   "Scorn heal from heroes 1.2x->1.3x raises the sustain that is his survive-the-fight engine.",
   "Burrow damage radius +0.5m makes the AoE his camp clear and dive both wider.",
   "Combo health per kill 40->50, so finishing the grab pays more than it did.",
   "Sand Blast T2 re-tunes the slow/dash cut to a flat -28% (from -24% slow / -26% dash): tagged a nerf in the notes, but the numbers read as a wash."
  ],
  "indirect_reasons": [
   "Healbane's stacking ceiling drops 82.2%->72% with 20% faster decay, so the multi-source anti-heal aimed at his Scorn sustain is materially weaker.",
   "Celeste, his 46% matchup, ate kit-wide nerfs (Dazzling Trick silence T3 +1.25s->+0.75s, Shining Wonder 160s->170s), removing kiting pressure from a lane he loses."
  ],
  "build_changes": [
   "Scorn 1.2x->1.3x rewards holding Scorn for hero contact instead of burning it on a camp; with the anti-heal ceiling capped, one Healbane on the team is enough \u2014 second and third copies are no longer worth a slot.",
   "Combo HP per kill 40->50 pushes the kill-complete play over poke: Burrow in, grab, finish \u2014 not a Burrow-and-walk-away."
  ],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "More Scorn healing, a bigger Burrow, +10 HP per grab \u2014 the tank holds targets and now survives doing it.",
  "verdict": "keep",
  "rows": [
   {
    "label": "Scorn heal",
    "old": "1.2x",
    "new": "1.3x",
    "text": null,
    "effect": "good",
    "ability": "Scorn"
   },
   {
    "label": "Burrow radius",
    "old": null,
    "new": null,
    "text": "Damage radius +0.5m",
    "effect": "good",
    "ability": "Burrow"
   },
   {
    "label": "T2 slow",
    "old": "-24% slow / -26% dash",
    "new": "-28% for both",
    "text": null,
    "effect": "good",
    "ability": "Sand Blast"
   },
   {
    "label": "Combo HP",
    "old": "40",
    "new": "50",
    "text": null,
    "effect": "good",
    "ability": "Combo"
   }
  ],
  "change_kind": "buff",
  "change_size": "minor"
 },
 {
  "hero": "Shiv",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.55,
  "direct_reasons": [],
  "indirect_reasons": [
   "Healbane's stack ceiling falls 82.2%->72% with 20% faster decay, so the Radiant Regeneration + Spirit Lifesteal shell he fights out of is far less punishable by a team's second and third anti-heal source.",
   "His own Healbane is a single source and is untouched \u2014 his heal-cut into bruisers does not change."
  ],
  "build_changes": [
   "Do not re-add out-of-combat regen: Radiant Regeneration is still in-combat-only, but stacked enemy anti-heal is now weaker, so Spirit Lifesteal + Torment Pulse carry the buff instead of another regen slot."
  ],
  "tier_before": "D",
  "tier_after": "D",
  "one_liner": "Weaker stacked anti-heal buys his regen stack back some buffer; he still starts fights smaller than pre-10-30.",
  "verdict": "watch",
  "rows": [],
  "change_kind": "none",
  "change_size": "none"
 },
 {
  "hero": "Ivy",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.6,
  "direct_reasons": [],
  "indirect_reasons": [
   "The 10-30 multi-source Healbane stack that specifically crushed tether healing is capped: 4-stack 82.2%->72%, 2-stack 57.8%->54.7%, decay 20% more aggressive.",
   "Mo & Krill, her 48% matchup, gained Scorn 1.2x->1.3x, +0.5m Burrow radius and +10 Combo HP per kill \u2014 displacement she cannot heal through got better."
  ],
  "build_changes": [
   "Run exactly one Healbane on the team, not three: the first source is unchanged and the marginal second/third slot is now worth more as any other Vitality item.",
   "Healing Booster/tether support gets a small relative rebound; the gun core (Titanic Magazine/Tesla Bullets) is still the build to fund."
  ],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "The anti-heal stack ceiling came down, so her tethers hold longer \u2014 gun core is still the build.",
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
 },
 {
  "hero": "Yamato",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.45,
  "direct_reasons": [],
  "indirect_reasons": [
   "Celeste, her 41% worst matchup, lost Dazzling Trick silence duration (T3 +1.25s->+0.75s), Radiant Daggers range (30m->25m) and Shining Wonder cooldown (160s->170s).",
   "Mo & Krill, her 42% matchup, got Scorn heal 1.2x->1.3x plus Burrow radius and Combo HP buffs \u2014 the sustain she cannot burst got better too, offsetting the Celeste gain."
  ],
  "build_changes": [],
  "tier_before": "D",
  "tier_after": "D",
  "one_liner": "Celeste's nerfs open one lane, but the sustain tank she cannot burst just got tankier.",
  "verdict": "watch",
  "rows": [],
  "change_kind": "none",
  "change_size": "none"
 },
 {
  "hero": "Lash",
  "in_notes": false,
  "direction": "neutral",
  "magnitude": "none",
  "confidence": 0.55,
  "direct_reasons": [],
  "indirect_reasons": [],
  "build_changes": [],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Untouched, still the top-pick initiator \u2014 nothing here blunts the grapple-dive loop.",
  "verdict": "keep",
  "rows": [],
  "change_kind": "none",
  "change_size": "none"
 },
 {
  "hero": "Viscous",
  "in_notes": false,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.45,
  "direct_reasons": [],
  "indirect_reasons": [
   "Mo & Krill, his 43% frontline loss, gained Scorn heal 1.2x->1.3x, Burrow damage radius +0.5m and Combo HP per kill 40->50 \u2014 the tank-sustain that already out-trades him got better.",
   "Healbane's stacked ceiling falls 82.2%->72%, which helps sustain comps generally but gives his own poke-and-Cube shell nothing specific."
  ],
  "build_changes": [],
  "tier_before": "D",
  "tier_after": "D",
  "one_liner": "No lines for Viscous, and the M&K buff makes the frontline he loses to harder to grind.",
  "verdict": "watch",
  "rows": [],
  "change_kind": "none",
  "change_size": "none"
 },
 {
  "hero": "Pocket",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [],
  "indirect_reasons": [
   "Celeste, his 39% worst matchup, lost Dazzling Trick silence (T3 +1.25s->+0.75s), Radiant Daggers range (30m->25m) and Shining Wonder cooldown (160s->170s) \u2014 the burst that out-ranged him is smaller.",
   "Healbane's stacked cut (82.2%->72%) makes team heal-cut weaker, which marginally hurts a DoT-burst carry trying to close through sustain; small and second-order."
  ],
  "build_changes": [],
  "tier_before": "D",
  "tier_after": "D",
  "one_liner": "Celeste nerfs soften his worst lane; the Affliction ramp still needs the game to last.",
  "verdict": "keep",
  "rows": [],
  "change_kind": "none",
  "change_size": "none"
 },
 {
  "hero": "Mirage",
  "in_notes": false,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [],
  "indirect_reasons": [
   "Mo & Krill, his 40% matchup, gained Scorn heal 1.2x->1.3x, Burrow radius +0.5m and Combo HP per kill 40->50 \u2014 the silence/combo that already locked him down got stronger.",
   "His own Healbane is a single source and is unchanged (57.8%->54.7% only hits the second source), so his anti-heal core buys the same thing it did."
  ],
  "build_changes": [
   "Keep one Healbane, not two: the second copy on your team now pays about three points less heal-cut.",
   "Split-push still converts worse than corridor farming after 10-20 \u2014 route through camps and take Djinn's Mark picks on isolated clearers."
  ],
  "tier_before": "D",
  "tier_after": "D",
  "one_liner": "The split-pusher gets nothing back, and the tank that silence-locks him got stronger.",
  "verdict": "bench",
  "rows": [],
  "change_kind": "none",
  "change_size": "none"
 },
 {
  "hero": "Vyper",
  "in_notes": false,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.4,
  "direct_reasons": [],
  "indirect_reasons": [
   "No direct lines; Mo & Krill, one of her listed losing matchups, gained Scorn heal 1.2x->1.3x and +0.5m Burrow radius, making the lift/combo dive on her cleaner.",
   "Healbane's multi-source nerf does not reach her: no Healbane in her gun core and no kit sustain to protect."
  ],
  "build_changes": [],
  "tier_before": "D",
  "tier_after": "D",
  "one_liner": "Nothing in the notes for her; her CC-counter Mo & Krill only got tankier, so the ~46% sits still.",
  "verdict": "keep",
  "rows": [],
  "change_kind": "none",
  "change_size": "none"
 },
 {
  "hero": "Sinclair",
  "in_notes": false,
  "direction": "neutral",
  "magnitude": "none",
  "confidence": 0.5,
  "direct_reasons": [],
  "indirect_reasons": [],
  "build_changes": [],
  "tier_before": "D",
  "tier_after": "D",
  "one_liner": "Untouched again: no item in his duration/cooldown shell moved and his divers did not change.",
  "verdict": "keep",
  "rows": [],
  "change_kind": "none",
  "change_size": "none"
 },
 {
  "hero": "Mina",
  "in_notes": false,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.4,
  "direct_reasons": [],
  "indirect_reasons": [
   "Her two worst listed matchups both eased for the enemy: Mo & Krill got Scorn 1.2x->1.3x plus +0.5m Burrow radius, and Ivy gains from the Healbane stacking cut.",
   "Weaker stacked anti-heal does nothing for her single-target rotation, which already loses to sustain."
  ],
  "build_changes": [],
  "tier_before": "D",
  "tier_after": "D",
  "one_liner": "Same 44.7% niche: the tanks she can't kill (Mo & Krill) and the healer she can't out-burst (Ivy) both got slightly better.",
  "verdict": "keep",
  "rows": [],
  "change_kind": "none",
  "change_size": "none"
 },
 {
  "hero": "Drifter",
  "in_notes": false,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [],
  "indirect_reasons": [
   "Healbane's 2-source cut 57.8%->54.7% specifically devalues his anti-heal bruiser variant, which stacked his built-in heal cut on top of Healbane/Toxic Bullets.",
   "Apollo's Riposte rework (added disarm, T2 +0.6s->+0.7s) sharpens a listed loss, and Mo & Krill's Scorn 1.2x->1.3x hardens another."
  ],
  "build_changes": [
   "Default to the spirit melee core (Melee Lifesteal/Stalker/Spirit Strike); the anti-heal bruiser package is now the weaker buy into healing comps."
  ],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Still a blind-pickable bruiser, but his anti-heal variant lost its edge and two of his losing lanes got buffed.",
  "verdict": "keep",
  "rows": [],
  "change_kind": "none",
  "change_size": "none"
 },
 {
  "hero": "Venator",
  "in_notes": false,
  "direction": "neutral",
  "magnitude": "none",
  "confidence": 0.55,
  "direct_reasons": [],
  "indirect_reasons": [],
  "build_changes": [],
  "tier_before": "D",
  "tier_after": "D",
  "one_liner": "No lines, and neither his trap-clearer Graves nor his tank counters moved; he is the same 46.7% gun-bruiser.",
  "verdict": "keep",
  "rows": [],
  "change_kind": "none",
  "change_size": "none"
 },
 {
  "hero": "Victor",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.45,
  "direct_reasons": [],
  "indirect_reasons": [
   "Anti-heal stacking is a listed counter to his grind-down shell, and the 4-stack Healbane ceiling fell 82.2%->72%, so Spirit Lifesteal/Healing Booster sustain is harder to fully suppress.",
   "Offset: Mo & Krill, a 47% matchup for him, gained Scorn heal 1.2x->1.3x and Combo 40->50 health per kill."
  ],
  "build_changes": [],
  "tier_before": "S",
  "tier_after": "S",
  "one_liner": "Quietly helped: the anti-heal that counters his sustain shell got weaker, and his own numbers are untouched.",
  "verdict": "keep",
  "rows": [],
  "change_kind": "none",
  "change_size": "none"
 },
 {
  "hero": "Paige",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.45,
  "direct_reasons": [],
  "indirect_reasons": [
   "Multi-source Healbane is listed as the anti-heal counter to her heal/lane-pressure shell, and its 2-source value fell 57.8%->54.7% (4-stack 82.2%->72%).",
   "Ivy, her toughest support matchup, gains from the same anti-heal cut, so the heal-duel stays roughly even."
  ],
  "build_changes": [],
  "tier_before": "S",
  "tier_after": "S",
  "one_liner": "55.6% lane bully untouched, and the stacked anti-heal teams used to answer her heals is weaker now.",
  "verdict": "keep",
  "rows": [],
  "change_kind": "none",
  "change_size": "none"
 },
 {
  "hero": "Graves",
  "in_notes": false,
  "direction": "neutral",
  "magnitude": "none",
  "confidence": 0.55,
  "direct_reasons": [],
  "indirect_reasons": [],
  "build_changes": [],
  "tier_before": "S",
  "tier_after": "S",
  "one_liner": "Nothing touches her shell \u2014 no Healbane in it, no counter buffed \u2014 so the 57.5% top win rate stands.",
  "verdict": "keep",
  "rows": [],
  "change_kind": "none",
  "change_size": "none"
 },
 {
  "hero": "Apollo",
  "in_notes": true,
  "direction": "up",
  "magnitude": "moderate",
  "confidence": 0.5,
  "direct_reasons": [
   "Riposte Pommel Hit now also disarms, turning his parry punish into a hard shutdown of a gun carry's M1 window on top of the existing immobilize.",
   "Riposte T2 duration +0.6s->+0.7s and Itani Lo Sahn T3 +50%->+60% bonus damage both lengthen or strengthen the pick he already converts.",
   "Pummel hit now ends a preexisting parry on the target \u2014 the least clear line (it strips the enemy's parry state rather than Apollo's), so treat one edge of this kit as unresolved."
  ],
  "indirect_reasons": [
   "Restorative Locket is his sustain slot and heal-stacking via Healbane is now weaker (2-source 57.8%->54.7%), so enemy anti-heal coverage of his Locket shell shrinks."
  ],
  "build_changes": [
   "Value Riposte as a duel/pick tool vs gun carries now that it disarms \u2014 hold the parry for their sustained-fire commit rather than fishing for channel interrupts (it is still an immobilize, not a stun)."
  ],
  "tier_before": "C",
  "tier_after": "B",
  "one_liner": "Riposte now disarms, holds 0.1s longer, and Itani Lo Sahn T3 hits harder \u2014 his pick punish finally has teeth.",
  "verdict": "keep",
  "rows": [
   {
    "label": "Disarm",
    "old": null,
    "new": null,
    "text": "Pommel Hit now also disarms",
    "effect": "good",
    "ability": "Riposte"
   },
   {
    "label": "Parry strip",
    "old": null,
    "new": null,
    "text": "Pummel hit ends target's preexisting parry",
    "effect": "good",
    "ability": "Riposte"
   },
   {
    "label": "T2 duration",
    "old": "+0.6s",
    "new": "+0.7s",
    "text": null,
    "effect": "good",
    "ability": "Riposte"
   },
   {
    "label": "T3 damage",
    "old": "+50%",
    "new": "+60%",
    "text": null,
    "effect": "good",
    "ability": "Itani Lo Sahn"
   }
  ],
  "change_kind": "buff",
  "change_size": "moderate"
 },
 {
  "hero": "Rem",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.45,
  "direct_reasons": [],
  "indirect_reasons": [
   "His percent-max-HP kit heal is exactly what the Healbane stacking cut protects \u2014 2-source 57.8%->54.7% and decay 20% more aggressive means fewer full-strength heal cuts land.",
   "Ivy, the support who owns his slot in the heal duel, gains from the same change, so the item-side lift doesn't win him the pick."
  ],
  "build_changes": [],
  "tier_before": "D",
  "tier_after": "D",
  "one_liner": "Anti-heal stacking got weaker, which is worth more to a percent-HP healer than anything else in this patch.",
  "verdict": "keep",
  "rows": [],
  "change_kind": "none",
  "change_size": "none"
 },
 {
  "hero": "Celeste",
  "in_notes": true,
  "direction": "down",
  "magnitude": "moderate",
  "confidence": 0.7,
  "direct_reasons": [
   "Dazzling Trick T3 silence +1.25s->+0.75s cuts her pick window by 40% on the ability that sets up her burst.",
   "Radiant Daggers cast range 30m->25m forces her closer, and the spirit amp per stack 7%->6% trims the payoff of the same ability.",
   "Shining Wonder nerfed on every axis: slow -32%->-28%, cooldown 160s->170s, bounce 15.5m->15m, T1 slow -16%->-14%, T2 damage +90->+80."
  ],
  "indirect_reasons": [
   "Healbane's stacked ceiling 82.2%->72% slightly relieves her Spirit Lifesteal/Torment Pulse sustain, but she never bought the item herself so the gain is one-sided and small."
  ],
  "build_changes": [
   "Shining Wonder at 170s is a fight-defining cast, not a rotation tool \u2014 stop valuing ult uptime and buy damage/uptime elsewhere.",
   "Silence T3 1.25->0.75s weakens the pick setup; lean on Spirit Lifesteal + Torment Pulse as the sustain layer rather than the gutted regen shell."
  ],
  "tier_before": "C",
  "tier_after": "D",
  "one_liner": "Every tool she picks with got shorter: silence, cast range, ult slow and ult cooldown all down.",
  "verdict": "watch",
  "rows": [
   {
    "label": "Silence T3",
    "old": "+1.25s",
    "new": "+0.75s",
    "text": null,
    "effect": "bad",
    "ability": "Dazzling Trick"
   },
   {
    "label": "Cast range",
    "old": "30m",
    "new": "25m",
    "text": null,
    "effect": "bad",
    "ability": "Radiant Daggers"
   },
   {
    "label": "Spirit amp",
    "old": "+7% per stack",
    "new": "+6% per stack",
    "text": null,
    "effect": "bad",
    "ability": "Radiant Daggers"
   },
   {
    "label": "Slow",
    "old": "-32% (T1 -16%)",
    "new": "-28% (T1 -14%)",
    "text": null,
    "effect": "bad",
    "ability": "Shining Wonder"
   },
   {
    "label": "Cooldown",
    "old": "160s",
    "new": "170s",
    "text": null,
    "effect": "bad",
    "ability": "Shining Wonder"
   },
   {
    "label": "Bounce range",
    "old": "15.5m",
    "new": "15m",
    "text": null,
    "effect": "bad",
    "ability": "Shining Wonder"
   },
   {
    "label": "T2 damage",
    "old": "+90",
    "new": "+80",
    "text": null,
    "effect": "bad",
    "ability": "Shining Wonder"
   }
  ],
  "change_kind": "nerf",
  "change_size": "moderate"
 },
 {
  "hero": "Rat King",
  "in_notes": true,
  "direction": "up",
  "magnitude": "moderate",
  "confidence": 0.7,
  "direct_reasons": [
   "Rule, Ratannia! T1 now also cuts 25s of cooldown, directly buying back part of the 180s ult timer that was his post-10-30 problem.",
   "Bullet damage 5.7->5.8 and ammo 24->26 feed the Monster Rounds/HVR gun-bruiser core that is his primary build.",
   "Rule, Ratannia! move speed +3m->+4m improves the banner window he uses to force hub fights."
  ],
  "indirect_reasons": [
   "Healbane's stacked heal-cut ceiling 82.2%->72% makes his regen/Fortitude frontline harder to fully suppress \u2014 the anti-heal answer to him is weaker.",
   "Baba's spirit-resist scaling 0.7->0.5 and melee damage -10% remove pressure from a fellow S-tier frontline contesting the same crates and hubs."
  ],
  "build_changes": [
   "Take Rule, Ratannia! T1 earlier \u2014 the -25s cooldown is now the cheapest fix for the 180s ult, ahead of Superior/Compress Cooldown.",
   "Scrap Grenade fuse-extension 0.4s->0.25s makes the melee-the-fuse trick less reliable; pull camps with melee first, then grenade the clump."
  ],
  "tier_before": "S",
  "tier_after": "S",
  "one_liner": "Buffs land on the exact spots 10-30 hit: ammo, bullet damage, banner speed and a 25s ult cooldown cut.",
  "verdict": "keep",
  "rows": [
   {
    "label": "Bullet damage",
    "old": "5.7",
    "new": "5.8",
    "text": null,
    "effect": "good",
    "ability": null
   },
   {
    "label": "Ammo",
    "old": "24",
    "new": "26",
    "text": null,
    "effect": "good",
    "ability": null
   },
   {
    "label": "Fuse extension",
    "old": "0.4s",
    "new": "0.25s",
    "text": null,
    "effect": "bad",
    "ability": "Scrap Grenade"
   },
   {
    "label": "Move speed",
    "old": "+3m",
    "new": "+4m",
    "text": null,
    "effect": "good",
    "ability": "Rule, Ratannia!"
   },
   {
    "label": "T1",
    "old": null,
    "new": null,
    "text": "Also -25s cooldown",
    "effect": "good",
    "ability": "Rule, Ratannia!"
   }
  ],
  "change_kind": "buff",
  "change_size": "moderate"
 },
 {
  "hero": "Baba",
  "in_notes": true,
  "direction": "down",
  "magnitude": "moderate",
  "confidence": 0.65,
  "direct_reasons": [
   "Spirit Resistance scaling 0.7->0.5 is a ~29% cut to the resist wall her regen bruiser build stands behind.",
   "Melee damage per boon -10% and Granny Long Legs melee/debuff resist 30%->25% trim both her heavy-melee crate clear and her brawl durability.",
   "Baba's Brew cooldown 27s->28s, cycle 1.5s->1.6s and burn spirit scaling 0.15->0.13 slow the random-order brew she already cannot control."
  ],
  "indirect_reasons": [
   "Healbane's stacked ceiling 82.2%->72% is a small relief for a regen-wall hero, but single-source anti-heal is untouched so the counter still works.",
   "Rat King's bullet damage, ammo and ult-cooldown buffs strengthen the frontline she competes with for crates and hub space."
  ],
  "build_changes": [
   "Spirit Resistance scaling 0.7->0.5 makes resist-stacking slots worse \u2014 put the spend into cooldown/duration (Compress Cooldown, Superior Cooldown) instead.",
   "Melee damage -10% per boon weakens the Granny Long Legs crate route; still open Tough Crates, but stop treating melee as a damage source."
  ],
  "tier_before": "S",
  "tier_after": "A",
  "one_liner": "Resist scaling and melee both cut again, but 54.4% win rate says she is still a top frontline.",
  "verdict": "keep",
  "rows": [
   {
    "label": "Spirit resist scaling",
    "old": "0.7",
    "new": "0.5",
    "text": null,
    "effect": "bad",
    "ability": null
   },
   {
    "label": "Melee damage",
    "old": null,
    "new": null,
    "text": "-10% per boon",
    "effect": "bad",
    "ability": null
   },
   {
    "label": "Cooldown",
    "old": "27s",
    "new": "28s",
    "text": null,
    "effect": "bad",
    "ability": "Baba's Brew"
   },
   {
    "label": "Burn scaling",
    "old": "0.15",
    "new": "0.13",
    "text": null,
    "effect": "bad",
    "ability": "Baba's Brew"
   },
   {
    "label": "Cycle time",
    "old": "1.5s",
    "new": "1.6s",
    "text": null,
    "effect": "bad",
    "ability": "Baba's Brew"
   },
   {
    "label": "Melee/debuff resist",
    "old": "30%",
    "new": "25%",
    "text": null,
    "effect": "bad",
    "ability": "Granny Long Legs"
   }
  ],
  "change_kind": "nerf",
  "change_size": "moderate"
 },
 {
  "hero": "Solomon",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.45,
  "direct_reasons": [],
  "indirect_reasons": [
   "Two of his three worst lanes were nerfed in the same patch \u2014 Baba (spirit resist scaling 0.7->0.5, melee -10%) and Celeste (silence, cast range, ult) \u2014 while Rat King, his other loss, was buffed.",
   "Healbane's stacked ceiling 82.2%->72% does nothing for him: his usage data shows no Healbane, so the anti-heal change is neutral here."
  ],
  "build_changes": [],
  "tier_before": "D",
  "tier_after": "D",
  "one_liner": "His two worst matchups got nerfed, but a 46.5% floor and a buffed Rat King keep him at D.",
  "verdict": "watch",
  "rows": [],
  "change_kind": "none",
  "change_size": "none"
 },
 {
  "hero": "Deadman Danny",
  "in_notes": true,
  "direction": "down",
  "magnitude": "moderate",
  "confidence": 0.7,
  "direct_reasons": [
   "Close The Deal bonus damage to under-half targets +75%->+55% cuts the execute that defines his dive-pick identity by a fifth.",
   "Strix Salvo spirit scaling -8% hits the ability his primary spirit-mark build scales everything into.",
   "Chimera Mk1 T2 heal-on-hit 150->125 and heal spirit scaling 2.0->1.7 remove sustain from a 730-HP flyer who has to commit to every dive."
  ],
  "indirect_reasons": [
   "Healbane's stacked ceiling 82.2%->72% does not help him \u2014 his problem is incoming burst, not suppressed healing.",
   "Rat King's buffs are irrelevant to him; his real counters (Kelvin, Paige, Celeste, Vyper) are unchanged or, for Celeste, nerfed on the ult rather than the burst that kills him."
  ],
  "build_changes": [
   "Chimera Mk1 T2 heal 150->125 with 2.0->1.7 scaling makes heal-on-hit a weaker talent \u2014 Reactive Barrier and Grit carry the dive instead.",
   "With the execute at +55%, stop diving targets above half HP expecting the mark to finish them; commit only on already-chipped targets."
  ],
  "tier_before": "A",
  "tier_after": "B",
  "one_liner": "Execute cut to +55%, Salvo scaling down 8% and the jetpack heal trimmed \u2014 the dive pays less.",
  "verdict": "watch",
  "rows": [
   {
    "label": "Execute damage",
    "old": "+75%",
    "new": "+55%",
    "text": null,
    "effect": "bad",
    "ability": "Close The Deal"
   },
   {
    "label": "Spirit scaling",
    "old": null,
    "new": null,
    "text": "-8%",
    "effect": "bad",
    "ability": "Strix Salvo"
   },
   {
    "label": "T2 heal",
    "old": "150",
    "new": "125",
    "text": null,
    "effect": "bad",
    "ability": "Chimera Mk1"
   },
   {
    "label": "Heal scaling",
    "old": "2.0",
    "new": "1.7",
    "text": null,
    "effect": "bad",
    "ability": "Chimera Mk1"
   }
  ],
  "change_kind": "nerf",
  "change_size": "moderate"
 },
 {
  "hero": "Violet",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.45,
  "direct_reasons": [],
  "indirect_reasons": [
   "Healbane's stacked heal-cut ceiling 82.2%->72% protects the regen stack she actually buys (Radiant Regeneration 96%, Mystic Regeneration 93%, Healing Booster 78%) from multi-source anti-heal.",
   "Baba's spirit-resist scaling 0.7->0.5 and melee -10% soften one of her 41% losing lanes; Rat King's buffs worsen the other."
  ],
  "build_changes": [],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Anti-heal stacking got weaker, which is the one thing her regen-heavy build needed; still 50.8%.",
  "verdict": "keep",
  "rows": [],
  "change_kind": "none",
  "change_size": "none"
 },
 {
  "hero": "Nurse Harrow",
  "in_notes": true,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.6,
  "direct_reasons": [
   "Bullet damage +8% is a straight gain for a hero whose primary build is Titanic Magazine mag-dump uptime.",
   "Lurking Terrors fear buildup 2s->1.75s makes her lockdown land a quarter-second sooner, tightening the channel window she wins fights in.",
   "Lurking Terrors vertical angle 50%->65% widens the cone so off-angle targets above and below her now get feared."
  ],
  "indirect_reasons": [
   "Healbane's stacked ceiling 82.2%->72% is a small relief for a dedicated healer whose entire sustain is healing-based, though single-source anti-heal still answers her.",
   "Rat King's buffs put more of the frontline she beats (59% into Billy-class brawlers) into lobbies, which suits her cone."
  ],
  "build_changes": [
   "Bullet damage +8% reinforces Titanic Magazine as the weapon core \u2014 no reason to revisit HVR/Active Reload.",
   "Fear buildup 2s->1.75s makes Lurking Terrors a reliable opener rather than a follow-up; lead with it."
  ],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Faster fear, wider cone and +8% bullet damage \u2014 small buffs that steady a falling A-tier.",
  "verdict": "keep",
  "rows": [
   {
    "label": "Bullet damage",
    "old": null,
    "new": null,
    "text": "+8%",
    "effect": "good",
    "ability": null
   },
   {
    "label": "Fear buildup",
    "old": "2s",
    "new": "1.75s",
    "text": null,
    "effect": "good",
    "ability": "Lurking Terrors"
   },
   {
    "label": "Vertical angle",
    "old": "50%",
    "new": "65%",
    "text": null,
    "effect": "good",
    "ability": "Lurking Terrors"
   }
  ],
  "change_kind": "buff",
  "change_size": "minor"
 }
]

## Item analysis

{
 "items": [
  {
   "item": "Healbane",
   "direction": "nerf",
   "magnitude": "minor",
   "summary": "Only the stacking curve moved: one source of anti-heal is exactly as strong, so nobody's single purchase decision changes. But the second-through-fourth sources pay less (4-stack ceiling 82.2%->72%), which quietly reverses part of the 10-30 'anti-heal is a team coverage plan' move and restores relative value to kit-based sustain.",
   "affected_heroes": [
    {
     "hero": "Seven",
     "relationship": "core",
     "effect": "down",
     "why": "Healbane is his answer to sustain comps; the payoff for adding it on top of a teammate's heal-cut is now materially smaller, so his counter-build is less of a hard counter."
    },
    {
     "hero": "Infernus",
     "relationship": "core",
     "effect": "neutral",
     "why": "His Toxic Bullets 40% heal-cut plus Healbane is exactly the two-source case trimmed 57.8%->54.7%, but the same change leaves his Spirit Lifesteal/Napalm sustain less punished by enemy stacked anti-heal — roughly a wash."
    },
    {
     "hero": "Drifter",
     "relationship": "situational",
     "effect": "down",
     "why": "The anti-heal bruiser variant's whole selling point was built-in heal cut stacking with Healbane/Toxic Bullets; that composition is the nerfed case, so his edge into healer comps shrinks."
    },
    {
     "hero": "Kelvin",
     "relationship": "core",
     "effect": "up",
     "why": "He still buys Healbane for self/team anti-heal, but the dome and Healing Booster throughput he sells is now harder for a team to fully shut down with multiple anti-heal sources."
    },
    {
     "hero": "Ivy",
     "relationship": "situational",
     "effect": "up",
     "why": "The 10-30 stack system was the worst change for her tether heals; capping the stack ceiling partially un-does that, though her gun core remains the correct build."
    },
    {
     "hero": "Shiv",
     "relationship": "core",
     "effect": "up",
     "why": "He buys Healbane himself, but more importantly his post-10-30 problem was starting fights small — a weaker anti-heal ceiling on his regen stack buys back some of the buffer Radiant Regeneration lost."
    },
    {
     "hero": "Mo & Krill",
     "relationship": "core",
     "effect": "up",
     "why": "Scorn sustain is his survive-the-fight engine; less effective stacked anti-heal on him is the one item-side gain for a tank whose spirit damage was gutted on 10-30."
    },
    {
     "hero": "Apollo",
     "relationship": "situational",
     "effect": "up",
     "why": "Restorative Locket carries his sustain after Healing Booster was gutted, and that heal is now harder to fully suppress with stacked anti-heal."
    }
   ],
   "build_shift": "No component or slot change — it stays a Vitality T2 — but its marginal value collapses for a team's second and third buyer, so on a comp that already has one Healbane the slot now competes with any other Vitality item instead of reading as free coverage.",
   "rows": [
    {
     "label": "2-stack heal cut",
     "old": "57.8%",
     "new": "54.7%",
     "text": null,
     "effect": "bad",
     "ability": null
    },
    {
     "label": "4-stack heal cut",
     "old": "82.2%",
     "new": "72%",
     "text": null,
     "effect": "bad",
     "ability": null
    },
    {
     "label": "Stack decay",
     "old": null,
     "new": null,
     "text": "Stacks diminish 20% more aggressively",
     "effect": "bad",
     "ability": null
    }
   ]
  }
 ],
 "notable_item_stories": [
  "Anti-heal is back to being a slot you buy rather than a coverage plan you draft: single-source Healbane is untouched, so expect fewer triple-Healbane comps and a small rebound for kit healers (Kelvin, Ivy) and self-sustain bruisers (Shiv, Mo & Krill).",
  "The losers are the heroes who used Healbane as a second layer over their own heal-cut (Infernus with Toxic Bullets, Drifter's built-in cut, Seven into sustain comps) — that specific stack is now worth about 3 points less at two sources and far less at four."
 ]
}

## Current meta.md

# Meta state
Last patch: Halloween 2026 + Gameplay Update (2026-10-30)

## Thesis
Games are won by converting a lead into Guardians/Walkers before the comeback economy catches up. Off-lane Haunt farm is still the income engine, but it now pays the trailing team too: Haunt bounty and growth are up, non-hero comeback gold is capped at 30%, tick souls feed the two poorest, and a team that is behind secures contested Haunt souls up to 50% faster. So the winners are one-cycle camp clearers who can also spend the lead fast, plus late scalers who now have a farm floor; teams that sit on an advantage bleed it into a jungle that keeps paying the loser.

## Economy and systems
- Comeback: non-hero comeback gold capped at 30% (was 26%), tick souls routed to the two lowest-econ players, deficit-scaled secure rate up to 50% faster on contested Haunt souls. Sitting on a lead is now a losing line.
- Kill income stays contested: the Soul Bag must be last-hit after the kill.
- Bounties: Guardian +10%, Walker +5%, objective share 30->25% (09-16, holds).
- Objective parries no longer reset the parry cooldown — Guardian/Shrine dives are one-shot.
- Respawn 38s at 20m. Global slows -20%; air drag ratio 0.5 (was 0.35) — airborne exits are slower, ground kiting stronger, flyers taxed harder.
- Steam Vents keep their invisibility and now also add +150% stamina regen.
- Cast-on-press holds; Healing Snacks 10% max HP unchanged.

## Map
Lanes renamed; four districts plus off-lane corridors. All neutrals are one of nine Haunt types that group and chase — bounty and growth +10%, HP and damage +10%. Tough Crates (58 souls, Heavy Melee only), Barrel Mimics, Sinner's Sacrifice variants, and Buff Containers rolling permanent Move Speed, Bullet/Spirit Resist and ability range; a Halloween candy-cauldron layer rewards Heavy Melee. Hubs: Sunken Plaza (~5-8 min, stamina strip) and Bell Tower (8+, ~280 souls, one rope, three vaults, map-wide bell). Green lane holds a roof/tree above the bridge. Arch Mother's side owns Sunken Plaza plus the theater.

## Archetype standing
- AoE one-cycle camp clearers: up — richer Haunts barely cost them HP (Seven, Infernus, McGinnis, Mina, Yamato).
- In-fight lifesteal bruisers: up — lifesteal cluster buffed while out-of-combat regen was cut (Victor, Infernus, Drifter).
- Heavy-melee frontline/tanks: stable — Torment Pulse +4% melee resist, but Hunter's Aura is LOS-gated and Decay/Healbane tax self-heal (Abrams, Mo & Krill, Billy, Shiv).
- Out-of-combat regen sustain: down — Radiant Regeneration is combat-only, Healing Booster delinked and trimmed (Baba, Shiv, Lady Geist, Celeste).
- Dedicated healers: down — Healbane now stacks across sources (Kelvin, Ivy, Rem).
- Max-range poke/gun carries: down — HVR velocity 60->45%, Express Shot -5%, worse air drag (Vindicta, Grey Talon, Paige).
- Roamers/pick assassins: mixed — slower tunnels and Shadow Weave needs 6s setup, but stamina vents feed re-engages (Lash, Holliday, Paradox, Calico).
- Lane bullies: slightly down — the comeback floor blunts snowball conversion (Paige, Apollo).
- Late scalers: up — non-hero comeback gold and tick souls fund the slow curve (Pocket, Mirage, Warden).
- Flyers: down — air drag 0.5 plus reliable grounding (Grey Talon, Celeste, Vindicta, Deadman Danny).

## Watchlist
- Average game length: if flat, comeback gold is going into fights, not items.
- Steal rate on contested Haunt souls: does the jungle become a fight zone?
- Radiant Regeneration buy rate and Juggernaut/lifesteal uptake — proxy for whether regen died or re-slotted into in-fight sustain.
- Double anti-heal comps (Healbane + Toxic Bullets/Crippling Headshot) into Kelvin/Ivy/Rem.
- Graves snapshot 56.5% WR / 40.9% PR still conflicts with the KB's 48.5% / 21% — recheck.
- Rat King win rate against pick rate.

## Recent history
- Halloween 2026 + Gameplay Update (2026-10-30): comeback levers (30% non-hero cap, tick souls to the two poorest, faster secure when behind), Haunt bounty/growth and HP/damage +10%, Steam Vents add +150% stamina regen, ~30 item moves — regen out, in-fight lifesteal and stacked anti-heal in.
- Shh... This Won't Hurt a Bit (2026-10-20): off-lane corridors and hub fights priced in; Haunt behaviors, Barrel Mimics, Steam Vents, Healing Snacks, instant casts; Graves gun destroys Venator traps.
- Paint the Town (2026-10-16): nine Haunt camp types replace all neutrals, contested Soul Bags, objective-parry cooldown reset removed, permanent-stat Buff Containers, six vote-gated new heroes.
- Minor Update - 10-14-2026: Baba frontline cut; Deadman Danny buff package; Radiant Regeneration third trim.
- Minor Update - 10-05-2026: trooper-speed regression fixed; Rat King and Sinclair trimmed.


## Current item entries (changed items only; may be empty for items not yet in the KB)

Healbane:
  name: Healbane
  role: anti-heal vitality item
  bought_by:
  - Apollo
  - Drifter
  - Infernus
  - Ivy
  - Kelvin
  - McGinnis
  - Mirage
  - Mo & Krill
  - Seven
  - Shiv
  - Solomon
  - Yamato
  slot: Vitality
  tier: 2
  notes: "10-30 rework, the patch's key system move: multi-source anti-heal now stacks\
    \ with diminishing returns, so two sources beat one strong healer \u2014 anti-heal\
    \ is a team coverage plan, not a slot. Heal-on-kill 275->170 (+3/boon) taxes frontline\
    \ buyers' own sustain. Best-in-class for buyers who want the enemy's healing gone\
    \ (Seven); worst for heroes who live on their own heals (Mo & Krill, Shiv, Kelvin,\
    \ Ivy)."


## What to do

Produce the post-patch knowledge base state. This KB is read by the analyst on the *next* patch, so write it as durable state, not as a patch summary.

1. **meta.md**: rewrite the whole document in this structure (markdown, <= 550 words):
   - `# Meta state` line with `Last patch: Minor Update - 11-04-2026 (2026-11-05)`
   - `## Thesis` — 2-4 sentences: how games are won right now (tempo vs scaling, fight shape, what archetypes carry).
   - `## Economy and systems` — bullets describing the current state of comeback, bounties, objectives, respawn, movement/slows, in present tense with current numbers where known.
   - `## Map` — current map state in present tense: lanes/districts, objectives with timings and values where known, farm sources (Haunt tiers, crates/boxes, Sinner's Sacrifice variants, Buff Containers), pickups (Healing Snacks, Steam Vents), side asymmetry, key routes. Keep it when nothing changed.
   - `## Archetype standing` — one bullet per archetype in play: up/down/stable and why.
   - `## Watchlist` — 3-6 bullets: heroes/items/systems that are uncertain and should be checked against data.
   - `## Recent history` — keep at most 5 bullets, newest first, one line per patch: "Minor Update - 11-04-2026: <headline>". Carry forward existing bullets from the current meta.md, drop the oldest beyond 5.
2. **item_updates**: for each changed item, the fields that changed. Allowed fields: role, bought_by, slot, tier, notes. `bought_by` must list hero names that build it as core or common situational pick, updated for this patch.
3. **change_log**: one line per KB edit you made, for the human to skim.

Tier is one of S/A/B/C/D. Trend is rising/stable/falling.

## Output schema

{
  "meta_md": "full markdown text",
  "item_updates": {"Item Name": {"role": "...", "bought_by": ["..."], "notes": "..."}},
  "change_log": ["Item Name: bought_by +Wraith (now core after rework)", "..."]
}
