# Task: update hero knowledge-base entries after this patch

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

## Hero analysis (this batch only)

[
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

## Current hero entries (this batch only)

Rem:
  name: Rem
  role: support/healer
  archetypes:
  - support/healer
  tier: D
  trend: rising
  why: Coin-flip support whose percent-max-HP heal and cleanse gain value as harder
    Haunt camps reward sustain and Bell Tower's three spread vaults stretch the map.
    Healing Snacks cheapen dedicated healing, and he still loses the heal-slot duel
    to Ivy.
  core_items:
  - Extra Charge
  - Healing Booster
  - Improved Spirit
  - Extra Spirit
  - Arcane Surge
  - Grit
  - Extra Regen
  - Guardian Ward
  - Superior Duration
  - Divine Barrier
  build_variants:
  - Spirit heal support
  - Vitality frontline shell
  - Lane gun package
  enabled_by:
  - percent-max-HP heal
  - cleanse
  - harder Haunt camps reward sustain
  - spread-out vaults (Bell Tower now three)
  - Abrams
  - Billy
  - Shiv
  - Viscous
  - Dynamo
  - Divine Barrier
  countered_by:
  - anti-heal
  - trimmed healing items
  - Ivy
  - Lash
  - Drifter
  - Yamato
  - Holliday
  - tempo meta
  last_changed_patch: Minor Update - 09-16-2026
  notes: "10-20 Shh...: no direct change; harder corridor camps raise the value of\
    \ his percent-max-HP heal on the farm route, but Healing Snacks do part of his\
    \ job for free and he still loses the heal-slot duel to Ivy \u2014 held B/rising.\n\
    \n09-29 City Never Sleeps: no direct change; harder camps reward his sustain and\
    \ spread-out vaults (Bell Tower now three) strengthen his map play, while Healing\
    \ Snacks slightly cheapen dedicated healing - trend up (peercontent).\n\n09-16\
    \ change is a breakable-spawn/bug fix plus target UI only (heresy 09-17); not\
    \ the 'big nerf' the community assumed, so strength impact is minor."
  builds:
  - name: Spirit heal support
    damage: spirit
    core_items:
    - Extra Charge
    - Healing Booster
    - Improved Spirit
    - Extra Spirit
    - Arcane Surge
    popularity: primary
    notes: Stacks spirit power and heal amps to scale the percent-max-HP heal and
      Naptime/Pillow Toss utility; the default Rem build (Extra Charge 93% at 5.4
      min).
  - name: Vitality frontline shell
    damage: hybrid
    core_items:
    - Grit
    - Extra Regen
    - Guardian Ward
    - Superior Duration
    - Divine Barrier
    popularity: secondary
    notes: Early survival shell so Rem can hold heal range on the frontline; Divine
      Barrier (45%, 55.8% WR) is the late payoff for fights.
  - name: Lane gun package
    damage: gun
    core_items:
    - High-Velocity Rounds
    - Opening Rounds
    popularity: niche
    notes: Very early (1.6/4.4 min) last-hit and poke tools for lane control, not
      a carry build.
  matchups:
    beats:
    - Paradox
    - Wraith
    - Paige
    - Vindicta
    - Haze
    loses_to:
    - Ivy
    - Warden
    - Lash
    - Drifter
    - Mo & Krill
  matchup_notes: Cleanse plus percent-max-HP heal erases pick/burst setups (Paradox)
    and out-lasts gun carries (Wraith, Haze) in extended fights. Loses to Ivy, who
    does the same heal job with a tankier body and a shorter-cooldown ult, and to
    dive/initiators Lash, Drifter and Mo & Krill that reach a low-HP support before
    the heal lands.
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
  tier: C
  trend: falling
  why: "Flying spirit burster whose entire shell \u2014 Radiant Regeneration plus\
    \ Healing Booster \u2014 was gutted in the same patch that buffed Decay, Toxic\
    \ Bullets and stacking Healbane; Shining Wonder 140->125 and the 0.35->0.5 air-drag\
    \ ratio leave her with no sustain and no safe angle."
  core_items:
  - Extra Regen
  - High-Velocity Rounds
  - Mystic Regeneration
  - Mystic Expansion
  - Restorative Locket
  - Torment Pulse
  - Greater Expansion
  - Witchmail
  - Spirit Shielding
  - Grit
  - Spirit Lifesteal
  build_variants:
  - Spirit sustain-burst carrier
  - Anti-CC / anti-debuff tech
  enabled_by:
  - High base power + overloaded kit (mobility, four abilities)
  - Torment Pulse + Greater Expansion AoE around her ult
  - Ult damage in Mid Boss / Rift fights
  - Torment Pulse 18->22% melee resist + Spirit Lifesteal 13->15% as the replacement
    sustain layer
  countered_by:
  - "Silver \u2014 Weighted Bola grounds flyers like her"
  - Slows now bleed air drag (system)
  - "Radiant Regeneration and Healing Booster gutted \u2014 her sustain shell is gone"
  - Anti-heal stacking (Decay -55%, Toxic Bullets 40%, Healbane) vs regen/lifesteal
    flyers
  - "Scaling/comeback nerfs \u2014 late-scaler into a tempo meta"
  - "Ivy \u2014 out-sustains her burst window"
  - "Lash / Calico \u2014 mobile initiators that close and survive"
  last_changed_patch: Halloween 2026 + Gameplay Update
  notes: '10-30 Halloween + Gameplay Update: B -> C. Shining Wonder 140->125 is the
    note; the real hit is Radiant Regeneration (0.35->0.25 spirit regen scaling, heal-on-cast
    65->40, in-combat only) plus Healing Booster losing Extra Regen and +3 flat regen,
    into buffed Decay/Toxic Bullets/stacking Healbane. Spirit Shielding 18->15%, HVR
    60->45% velocity and Metal Skin''s +20% gravity compound it; pivot to Spirit Lifesteal
    + Torment Pulse.

    10-20 Shh...: no direct change; the off-lane/corridor economy gives her no camp
    or crate income route, and Barrel Mimics tax a low-HP clearer, so the tempo patch
    keeps her B/falling.

    10-16 Paint the Town: no direct change; the contested, earlier soul economy punishes
    her late-scaling line and buffed Deadman Danny (61% vs her) adds a direct threat;
    tier B held.'
  builds:
  - name: Spirit sustain-burst carrier
    damage: spirit
    core_items:
    - Extra Regen
    - High-Velocity Rounds
    - Mystic Regeneration
    - Mystic Expansion
    - Restorative Locket
    - Torment Pulse
    - Greater Expansion
    - Spirit Lifesteal
    popularity: primary
    notes: "Radiant Regeneration and Healing Booster are out of the shell \u2014 Spirit\
      \ Lifesteal (6->8 spirit, 13->15%) plus Torment Pulse (18->22% melee resist)\
      \ is the new sustain layer. HVR's 60->45% velocity makes the early poke weaker,\
      \ so upgrade it faster or skip it."
  - name: Anti-CC / anti-debuff tech
    damage: hybrid
    core_items:
    - Witchmail
    - Spirit Shielding
    - Grit
    popularity: secondary
    notes: "Witchmail is her highest-WR item (60.6%, bought ~24m) \u2014 the answer\
      \ into heavy slow/CC comps, which matter more now that slows bleed air drag.\
      \ Spirit Shielding 18->15% makes this shell thinner than it was."
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
    - Deadman Danny
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
  tier: S
  trend: falling
  why: Still a 116-heavy-melee frontline who opens Tough Crates and wants the forced
    hub fights, but Scrap Grenade's damage cuts and the banner ult's knockup and cooldown
    nerfs dent his one-button camp clear and his teamfight reset, right as Haunt camps
    gained +10% HP.
  core_items:
  - Monster Rounds
  - High-Velocity Rounds
  - Opening Rounds
  - Extra Health
  - Cultist Sacrifice
  - Enduring Speed
  - Fortitude
  - Superior Cooldown
  - Compress Cooldown
  build_variants:
  - Gun bruiser
  - Vitality frontline
  - Swarm shred
  enabled_by:
  - "Tough Crate routes needing heavy melee \u2014 116 heavy melee, 800 HP, 2.0 regen\
    \ open guaranteed ~58-soul crates"
  - "Forced telegraphed hub fights at Sunken Plaza/Bell Tower \u2014 banner ult adds\
    \ move speed, slow immunity and DR"
  - "Gun-carry meta \u2014 Rat Swarm's bullet-resist shred and Royal Pestments deflect\
    \ punish Venator/Silver/Paradox"
  - Heavy-Melee Cauldrons and Healing Snacks 10->14% keep his frontline brawl ticking
  countered_by:
  - "Heal/save supports that out-sustain his damage window \u2014 Ivy, Kelvin, Paige,\
    \ Dynamo"
  - "Spirit burst that bypasses the anti-bullet barrier \u2014 Celeste"
  - Silence/CC (Silence Wave, Silencer) denying banner and barrier
  - Anti-heal (Healbane, Decay) against his regen stacking
  last_changed_patch: Halloween 2026 + Gameplay Update
  notes: '10-30 Halloween + Gameplay Update: S -> A. Scrap Grenade 70->60 (T2 +70->+60,
    T3 300->275), fuse +0.1s; Rule, Ratannia! knockup halved, 160->180s and now goes
    on cooldown if he is stunned before placing; base bullet -5% and growth -20%.
    Haunt camps +10% HP finish the one-button clear. Offsets: Heavy-Melee Cauldrons,
    Healing Snacks 10->14%.

    10-20 Shh...: no direct change; Tough Crates, grouped chasing Haunts, forced Bell
    Tower/Sunken Plaza hubs and Barrel Mimics all point at heavy-melee camp-clear
    frontlines, so the systems patch lifts him A -> S on fit, not numbers - confirm
    against win rate before locking.

    10-16 Paint the Town: notes entry only - added to the weekly release-vote schedule,
    no balance change; the contested-Haunt economy still matches his heavy-melee crate
    and AoE-clear kit, so tier held A.'
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
      \ the work. Scrap Grenade is no longer a one-button camp clear (fuse +0.1s):\
      \ pull camps with melee first, then grenade the clump."
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
      Superior/Compress Cooldown (57.9%/57.7% WR) are now mandatory rather than optional
      to cover the banner ult's 180s cooldown.
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
Baba:
  name: Baba
  role: bulky spirit bruiser-caster
  archetypes:
  - spirit carry
  - tank/frontline
  - lane bully
  - initiator
  tier: S
  trend: falling
  why: 'Grounded regen bruiser whose identity was removed twice over: Baba''s Brew
    is now random-order on a 1.5s cycle so she cannot guarantee the silence or barrier
    she needs, and both Radiant Regeneration (94% buy) and Healing Booster were gutted
    into a patch that buffed every anti-heal item.'
  core_items:
  - Extra Charge
  - Extra Regen
  - Mystic Regeneration
  - Spirit Strike
  - Spirit Resilience
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
  - Heavy-Melee Cauldrons and Healing Snacks 10->14%
  countered_by:
  - 'Anti-heal vs her regen wall: Healbane (now stacking), Decay -55%, Toxic Bullets
    40%'
  - Random brew order + 1.5s cycle removes on-demand silence/barrier
  - 'Sustain supports that neutralize her grind: Kelvin, Dynamo, Paige'
  - 'Channel interrupts/silence on her ult: Knockdown, Cursed Relic, Silencer'
  - 'Burst/mobile gun pressure she can''t out-poke: Holliday, Wraith; Plated Armor
    and Bullet Resilience vs her gun damage'
  last_changed_patch: Halloween 2026 + Gameplay Update
  notes: '10-30 Halloween + Gameplay Update: C -> D. Baba''s Brew order is random
    each cast on a 1->1.5s cycle (silence 3->2.75s), spirit-resist scaling 0.1->0.07,
    Threadsap 22->16s and cleanse now wipes stolen spirit, Granny heavy-melee slow
    4->2s; Radiant Regeneration (94% buy) and Healing Booster both gutted into an
    anti-heal patch. Offsets: Heavy-Melee Cauldrons, Healing Snacks 10->14%.

    10-20 Shh...: no direct change; the new corridors, grouped Haunt camps and forced
    Bell Tower/Plaza fights suit her melee-regen clear and arrest the post-10-14 fall,
    but the barrier/resist cuts still bind - trend falling -> stable at C.

    10-14: major kit cut - Brew barrier scaling 1.2->0.7 and base 100->90 with CD
    25->27s (later, T2), -7% Base Bullet Resist, spirit-resist scaling 0.12->0.1,
    Granny Long Legs CD 30->32 with lower light-melee launch and decaying repeat air-melee
    momentum, Threadsap CD 26->28 with its spirit shred now ending on death; plus
    Radiant Regeneration 0.04->0.035. Tier B -> C, trend falling.'
  builds:
  - name: Cooldown caster
    damage: spirit
    core_items:
    - Compress Cooldown
    - Spirit Snatch
    - Duration Extender
    - Superior Cooldown
    - Rapid Recharge
    - Spirit Resilience
    popularity: primary
    notes: "The regen shell is gone \u2014 Radiant Regeneration and Healing Booster\
      \ were both gutted \u2014 so the cooldown/duration line is the build now. Brew\
      \ order is random each cast on a 1->1.5s cycle: hold the cast until the needed\
      \ brew cycles in rather than opening fights blind."
  - name: Spirit bruiser
    damage: spirit
    core_items:
    - Extra Charge
    - Extra Regen
    - Mystic Regeneration
    - Spirit Strike
    - Torment Pulse
    - Spirit Resilience
    popularity: secondary
    notes: HP/regen filler to out-sustain Haunt chip and hub fights; Torment Pulse
      18->22% melee resist is the only sustain gain, and anti-heal stacking (Decay
      -55%, Healbane) now cuts straight through it.
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
  role: zone-control support
  archetypes:
  - support/healer
  - initiator
  - poke/siege
  tier: D
  trend: stable
  why: "Zone-control support whose Bishop is now the damage (0.85 on-square scaling,\
    \ T3 shred -5%/stack on impact) while Rook Battery 1.3->0.9 and base bullet 30->25\
    \ gut the gun lane \u2014 and his three worst matchups (Rat King, Baba, Celeste)\
    \ all ate major nerfs, so the floor rises even as his own numbers fall."
  core_items:
  - Extra Spirit
  - Mystic Expansion
  - Improved Spirit
  - Superior Cooldown
  - Greater Expansion
  - Compress Cooldown
  - Mystic Burst
  - High-Velocity Rounds
  - Opening Rounds
  build_variants:
  - Spirit cooldown control
  - Gun lane
  - Vitality/sustain
  enabled_by:
  - Hub-fight meta (Sunken Plaza ~5-8 min, Bell Tower 8+) rewarding telegraphed zone
    control
  - "Cooldown stacking \u2014 Superior Cooldown (84%), Greater Expansion (81%), Compress\
    \ Cooldown (73%)"
  - 'Heavy melee 116 opening Tough Crates: not a camp-clearer, so income rides on
    guaranteed 58-soul routes and team souls'
  - "Front-line-heavy lobbies \u2014 beats Abrams, Mo & Krill, Shiv"
  countered_by:
  - 'Burst mobility landing before the self-cast Knight''s invuln: Lash (S), Holliday,
    Calico, Yamato (all A/S, rising)'
  - Silence (Silencer, Silence Wave) denying the cooldown loop
  - Unstoppable ignoring rook immobilize; Knockdown on the cast
  - Rat King (A, stable) and Celeste spirit burst closing into his zone (35% losses)
  last_changed_patch: Halloween 2026 + Gameplay Update
  notes: '10-30 Halloween + Gameplay Update: base bullet 30->25 and -20% headshot
    gut the HVR/Opening Rounds lane crutch, Rook Battery 1.3->0.9 scaling is a real
    damage cut, Develop Queen 210->240s; Setup Bishop is now the damage (0.64->0.85
    on-square, T1 slow +25%, T3 shred -5%/stack on impact) and checkmate is base kit.
    Max Bishop over Rook Battery. Three losing matchups (Rat King, Baba, Celeste)
    ate major nerfs. C held.

    7-day check-in (2026-10-16): tier B -> C, WR 45%, PR 61% over 329000 matches.
    Usage overrides the day-0 ''Barrier support'' and full-gun builds: Divine Barrier/Healbane/Healing
    Booster/Superior Duration and Swift Striker do not appear in high-rank item data.
    Vindicta now reads 48% (even), not the day-0 loss; Baba still 36% despite the
    10-14 front-line cut (her barrier 1.2->0.7, -7% bullet resist, B->C).

    10-14: no direct change; one week old and the empty Develop Queen tooltip leaves
    his ult and its Checkmate (200/5) threshold the biggest unknown.'
  builds:
  - name: Spirit cooldown control
    damage: spirit
    core_items:
    - Extra Spirit
    - Mystic Expansion
    - Improved Spirit
    - Mystic Burst
    - Compress Cooldown
    - Superior Cooldown
    - Greater Expansion
    - Boundless Spirit
    popularity: primary
    notes: Stacks spirit power + cooldown reduction (Superior Cooldown 84% at 20:00,
      Greater Expansion 81%, Compress Cooldown 73%) to spam Bishop/Rook; the only
      shell where single items beat his 42.6% baseline (Mystic Burst 44.6%, Boundless
      Spirit 49.3%).
  - name: Gun lane
    damage: gun
    core_items:
    - High-Velocity Rounds
    - Opening Rounds
    popularity: secondary
    notes: "HVR (86% at 2:42) and Opening Rounds (83% at 5:06) are near-universal\
      \ early buys but sit at the ~43% baseline \u2014 the day-0 full-weapon path\
      \ (Swift Striker, Extended Magazine) never shows up in usage, so treat this\
      \ as a lane crutch, not a carry build."
  - name: Vitality/sustain
    damage: spirit
    core_items:
    - Grit
    - Extra Stamina
    - Guardian Ward
    - Stamina Mastery
    popularity: niche
    notes: Stamina/HP fillers (Extra Stamina 68%, Grit 53%) to survive dive-heavy
      lobbies; the day-0 'Barrier support' shell (Divine Barrier, Healbane, Healing
      Booster, Superior Duration) is absent from high-rank usage.
  matchups:
    beats:
    - Deadman Danny
    - Mo & Krill
    - Abrams
    - Vindicta
    - Shiv
    loses_to:
    - Celeste
    - Rat King
    - Baba
    - Holliday
    - Yamato
  matchup_notes: "Bishop tiles + rook immobilize zone anything that must physically\
    \ hold hub space, so he beats front-line bodies (Deadman Danny 61%; Shiv/Mo &\
    \ Krill/Abrams ~even) \u2014 note Vindicta now reads 48% (even), not the loss\
    \ the day-0 entry claimed. He dies to burst mobility that lands before his self-cast\
    \ Knight's invuln (Holliday 37%, Yamato 38%) and to Rat King/Celeste closing inside\
    \ his zone."
  confidence: 0.4
  released_on: '2026-10-09'
  provisional: false
Deadman Danny:
  name: Deadman Danny
  role: Flying spirit marksman / dive-pick
  archetypes:
  - spirit carry
  - mobile assassin
  - burst caster
  tier: A
  trend: stable
  why: 'Spirit mark-burster whose dive got taxed twice: slows now cut jetpack impulse,
    so the escape got worse; the Close The Deal damage fix is the only gain on a 730-HP
    flyer with the air-drag tax intact.'
  core_items:
  - High-Velocity Rounds
  - Extra Spirit
  - Mystic Burst
  - Improved Spirit
  - Mystic Expansion
  - Reactive Barrier
  - Tankbuster
  - Greater Expansion
  - Opening Rounds
  - Express Shot
  build_variants:
  - Spirit mark burst
  - Hybrid charged-shot
  enabled_by:
  - Grouped hub fights (Sunken Plaza ~5-8 min, Bell Tower 8+) that reward mark-then-AoE-dive
    on stacked targets
  - "Spirit AoE (Mystic Burst, Mystic Expansion, Greater Expansion) into grouped,\
    \ chasing Haunt camps \u2014 the meta's fastest income route"
  - 'Anchor initiators who hold targets for Strix Salvo marks and Close The Deal:
    Dynamo, Mo & Krill, Abrams (all A/rising)'
  - "Shadow Weave is now the only invis-engage tool \u2014 pick angles must be bought,\
    \ not found"
  countered_by:
  - "Silver's Weighted Bola \u2014 S-tier anti-air that grounds him in addition to\
    \ out-trading his gun"
  - Slows now cut jetpack impulse directly, and harder under movement-ability silence
  - Silence/knockdown (Silencing Hex, Knockdown) plus Bebop hook catching a committed
    dive
  - Plated Armor vs HV Rounds/Opening Rounds poke; Debuff Reducer vs his marks and
    fading slow
  - "His own whiffed-dive self-stun against the 38s respawn timer at 20 min \u2014\
    \ a single bad dive is a lost fight"
  - 'Late payoff vs tempo: Boundless Spirit''s ~47-min average buy arrives after the
    game usually ends'
  last_changed_patch: Halloween 2026 + Gameplay Update
  notes: "10-30 Halloween + Gameplay Update: Chimera Mk1 nerfed across the board \u2014\
    \ jetpack unusable while cursed, slows now cut jetpack impulse harder (worse under\
    \ movement-ability silence), grounding pulls land more reliably. HVR 60->45% velocity\
    \ hits his lone weapon staple; the Close The Deal damage fix is the only gain.\
    \ C held, trend rising -> stable.\n7-day check-in (2026-10-20): tier C -> C, WR\
    \ 45%, PR 69% over 446352 matches. Corrected: the usage data kills the 'shred/mark\
    \ gun' identity - Bullet Resist Shredder does not appear at all, and the real\
    \ build is spirit (Extra/Improved Spirit, Mystic Burst at 79-90%) with HV Rounds\
    \ as the lone weapon staple. The old beats list was inverted - Celeste (33%) and\
    \ Graves (32%) are among his worst lanes, not wins. PR 69.1% is a new-hero novelty\
    \ spike (previously 0.2% on a two-day sample), so read WR 38.5% and ignore pick\
    \ rate. Held C/rising: the build finally consolidated and WR gained ~3.6 points,\
    \ but nothing clears 49% head-to-head and the flyer tax is intact; upgrade only\
    \ on ~45%+ WR, drop to D if the spirit capstone stays a post-30-min luxury.\n\
    10-20 Shh...: no direct change; grouped chasing Haunt camps and corridor farm\
    \ suit his spirit AoE marks and Steam Vents add approach angles, but the flyer\
    \ tax and Barrel Mimic risk on a 730-HP commit keep him C/rising."
  builds:
  - name: Spirit mark burst
    damage: spirit
    core_items:
    - High-Velocity Rounds
    - Extra Spirit
    - Mystic Burst
    - Improved Spirit
    - Mystic Expansion
    - Reactive Barrier
    - Tankbuster
    - Greater Expansion
    - Boundless Spirit
    popularity: primary
    notes: Spirit stacking amplifies Strix Salvo marks (1.1 spirit scaling) and the
      75% Close The Deal execute while Mystic Burst/Expansion give the overheat-dive
      AoE; Compress and Superior Cooldown are the late luxuries and Boundless Spirit
      lands ~47 min, after most games are decided.
  - name: Hybrid charged-shot
    damage: hybrid
    core_items:
    - High-Velocity Rounds
    - Opening Rounds
    - Grit
    - Extra Health
    - Express Shot
    popularity: secondary
    notes: "The surviving gun skeleton \u2014 HV Rounds into Opening Rounds keeps\
      \ lane poke and the mark-consume hit relevant while spirit items carry the burst;\
      \ Grit, Extra Health and Reactive Barrier are near-universal defensive glue\
      \ across both builds, not a separate archetype."
  matchups:
    beats:
    - Violet
    - Grey Talon
    - Calico
    - Paradox
    loses_to:
    - Kelvin
    - Vyper
    - Graves
    - Celeste
    - Paige
  matchup_notes: "Nothing on the roster is actually favourable \u2014 Violet at 49%\
    \ is his ceiling, so 'beats' means least-bad. The genuine losses are sustain-plus-slow:\
    \ Kelvin (29%) heals through the mark-to-execute window and his slow stacks with\
    \ the 35% air drag, while Paige (33%) out-lanes him and converts the ~2:30 crate/hub\
    \ timing before his kit is online. Celeste and Vyper (33/32%) simply out-burst\
    \ a 730-HP flyer who has to commit to a dive; Silver (unsampled) is the theoretical\
    \ floor via Weighted Bola."
  confidence: 0.55
  released_on: '2026-10-13'
  provisional: false
Violet:
  name: Violet
  role: spirit zone-control caster
  archetypes:
  - spirit carry
  - burst caster
  - initiator
  - late scaler
  tier: B
  trend: falling
  why: "Zone caster whose ult was cut on every axis at once (180s cooldown, 5s duration,\
    \ 0.04->0.01 scaling, ends on death, ink destructible again) and whose Still Life\
    \ regen only ticks while drawing \u2014 Spirit Lifesteal 13->15% is the only sustain\
    \ she has left, into a patch that buffs every anti-heal item."
  core_items:
  - Extra Spirit
  - Mystic Regeneration
  - Extra Charge
  - Improved Spirit
  - Rapid Recharge
  - Superior Cooldown
  - Boundless Spirit
  - Tankbuster
  - Spirit Lifesteal
  build_variants:
  - Spirit caster (lead)
  - Anti-bruiser sustain
  - Mystic Shot poke
  enabled_by:
  - "Grouped, chasing Haunt camps \u2014 AoE spirit clear is the fastest income in\
    \ the off-lane corridor meta"
  - "Tough Crates (58 souls, guaranteed) \u2014 opened on her standard 116 heavy melee\
    \ without committing to a gun build"
  - Scheduled hub fights at Bell Tower (~280 souls, one rope, three vaults) and Sunken
    Plaza plus Buff Container rolls, where a vision-blocking silence zone decides
    the contest
  - "Superior Cooldown + Boundless Spirit \u2014 the kit is cooldown-gated and those\
    \ are the only two purchases above her baseline (52.9% / 54.4%)"
  - "Tankbuster \u2014 the meta's frontline density (Rat King, Mo & Krill, Victor,\
    \ Shiv, Silver) makes %-HP spirit damage her best mid-game slot"
  countered_by:
  - "Dive assassins (Lash, Holliday, Calico, Yamato) \u2014 no dash, 710 HP, no escape\
    \ once the engage lands"
  - "Vindicta \u2014 39% WR, outranges the zone and flyers are the one ranged archetype\
    \ she does not beat"
  - "Frontline HP stacks (Rat King, Mo & Krill, Baba \u2014 all 41%) that walk through\
    \ the DoT"
  - "Healbane / anti-heal \u2014 Radiant Regeneration (96%), Mystic Regeneration (93%)\
    \ and Healing Booster (78%) are near-universal, so one anti-heal item taxes most\
    \ of her spend"
  - "Silence Wave / Knockdown / Disarming Hex \u2014 interrupt or cancel the Still\
    \ Life gaze"
  last_changed_patch: Halloween 2026 + Gameplay Update
  notes: "10-30 Halloween + Gameplay Update: B -> C. Abstract Landscape 165->180s,\
    \ 0.04->0.01 duration scaling, ends on death, 0.5->0.75s re-apply and T3 ink destructible\
    \ again; Still Life stun 1.0->0.9s, LOS required at channel end, T1 regen only\
    \ while drawing (0.25->0.15). Spirit Lifesteal 6->8 spirit / 13->15% is the replacement\
    \ sustain; anti-heal stacking taxes the rest.\n7-day check-in (2026-10-23): tier\
    \ B -> C, WR 50%, PR 64% over 539876 matches. Data corrects the day-0 read: B/rising\
    \ was a tooltip judgment, so C is a correction, not a decline \u2014 46.1% WR\
    \ at 70.9% PR, and she loses to frontline brawlers rather than punishing melee.\
    \ Watch whether her WR climbs with reps; the tooltip read also claimed Seven and\
    \ the gun line as wins, but Seven is 49% over 170 and Living Ink/HVR no longer\
    \ appear in her item data at all. 10-20 Shh...: no Violet changes; her position\
    \ moves on systems (Haunt grouping, Tough Crates, hub fights) and on the dive/frontline\
    \ meta around her."
  builds:
  - name: Spirit caster (lead)
    damage: spirit
    core_items:
    - Extra Spirit
    - Mystic Regeneration
    - Extra Charge
    - Improved Spirit
    - Rapid Recharge
    - Superior Cooldown
    - Boundless Spirit
    - Spirit Lifesteal
    popularity: primary
    notes: Cooldown/regen ramp into T3-T4 spirit; Radiant Regeneration is out and
      Spirit Lifesteal (6->8 spirit, 13->15%) is the replacement sustain. Only Superior
      Cooldown (52.9%) and Boundless Spirit (54.4%) beat her 46% baseline, and both
      land after 24 min.
  - name: Anti-bruiser sustain
    damage: spirit
    core_items:
    - Extra Regen
    - Grit
    - Spirit Shielding
    - Tankbuster
    - Spirit Lifesteal
    popularity: secondary
    notes: Vitality shell plus Tankbuster (57% share, 49.7% WR, 24.4 min) to chew
      the Rat King/Mo & Krill/Victor/Shiv frontlines; Healing Booster lost Extra Regen
      and its flat regen, and the regen half dies to Healbane stacking.
  - name: Mystic Shot poke
    damage: hybrid
    core_items:
    - Mystic Shot
    - Mystic Burst
    popularity: niche
    notes: Mystic Shot (47% share, 46.9%) is the only weapon-side item left in her
      data; the Living Ink / High-Velocity Rounds gun line from the day-0 read has
      fallen out of usage entirely.
  matchups:
    beats:
    - Grey Talon
    - Deadman Danny
    - Mina
    - Paradox
    loses_to:
    - Vindicta
    - Baba
    - Mo & Krill
    - Wraith
    - Rat King
  matchup_notes: "She beats the grounded marksman/flyer tier (Grey Talon 54%, Deadman\
    \ Danny 51%) \u2014 35% air drag and vent-fed approaches force them into her zone\
    \ \u2014 while Vindicta at 39% is the exception because she pokes from outside\
    \ it. She loses to HP-stacking frontlines (Rat King 41%, Mo & Krill 41%) that\
    \ outlast the DoT, and to Wraith's single-target burst; 710 HP with no dash means\
    \ the zone lands after she's dead. The dive class (Lash, Holliday, Calico, Yamato)\
    \ is the same structural problem even where the sample is too thin to list."
  confidence: 0.6
  released_on: '2026-10-16'
  provisional: false
Nurse Harrow:
  name: Nurse Harrow
  role: marksman-support hybrid
  archetypes:
  - gun carry
  - support/healer
  tier: A
  trend: falling
  why: Marksman-healer whose Lurking Terrors is now a 5s lockdown with 2s fear buildup
    and 50% damage reduction instead of immunity, in a patch where Decay, Toxic Bullets
    and stacking Healbane all cut her healing; the 0.2->0.24 spirit scaling on Healing
    Needles is the pivot, not a replacement.
  core_items:
  - Extra Regen
  - Extended Magazine
  - Titanic Magazine
  - Extra Stamina
  - Kinetic Dash
  - Extra Spirit
  - Arcane Surge
  - Superior Cooldown
  - Superior Duration
  build_variants:
  - Mag-dump sustain
  - Cooldown/Duration spirit
  - Ricochet gun carry
  enabled_by:
  - "Sustain-bruiser / melee-frontline meta (Shiv, Billy, Rat King, Victor, Mo & Krill\
    \ all up) \u2014 the fights she wins are long, grouped and close-range, where\
    \ cone DoT and AoE heal both pay"
  - "Hub scheduling at Bell Tower, Sunken Plaza and Buff Container spawns \u2014 the\
    \ map now forces grouped fights on her terms"
  - "Cast-on-press (10-20) \u2014 Leech into Vapors into Needles resolves on input,\
    \ so her combo no longer drops a window"
  - "Buff Container permanent rolls \u2014 Leech Therapy eats buff duration and T3\
    \ Needles extends her team's, so contested containers hand her value"
  - "Ricochet (38% share, 59.1% WR) \u2014 bounces feed her gun-damage charge economy\
    \ in precisely the stacked fights the map creates"
  countered_by:
  - "Long-range spirit burst and zone control (Baba 43%, Celeste 45%, Wraith 46%)\
    \ \u2014 none of it enters the fear cone, and no dash or regen means the fight\
    \ ends before Healing Needles pay"
  - "Healbane / Decay / Toxic Bullets \u2014 anti-heal is the archetype answer to\
    \ a healer, and all her sustain is healing-based"
  - "Silencer / Cursed Relic / Knockdown \u2014 Lurking Terrors is a channel and her\
    \ survivability is ability-based; Knockdown stops the channel outright"
  - "Plated Armor \u2014 the needle charge economy runs on gun damage, and Armor Piercing\
    \ Rounds is the answer but eats a slot she needs for uptime"
  - "Off-angle dives and hooks \u2014 the fear cone only covers the facing arc, and\
    \ Dynamo's 45% shows what an AoE engage does to her"
  - "Lane bullies at the top (Paige, Apollo at S) \u2014 0 base regen and 730 HP mean\
    \ she loses the attrition lane she is supposed to win"
  last_changed_patch: Halloween 2026 + Gameplay Update
  notes: "10-30 Halloween + Gameplay Update: Lurking Terrors fear buildup 1.3->2s,\
    \ T3 immunity -> 50% damage reduction, no fear from >50\xB0 above/below the target's\
    \ view; base gun damage -10%, Healing Needles 25->22 (T2 +20->+16) but spirit\
    \ scaling 0.2->0.24; Leech Therapy ground leeches 180s -> 120s + 3s/min and cleared\
    \ on round reset. Anti-heal buffs land on a dedicated healer. B held, trend stable\
    \ -> falling.\n7-day check-in (2026-10-27): tier B -> B, WR 51%, PR 63% over 607252\
    \ matches. Data overrides the day-0 read: Swift Striker, High-Velocity Rounds\
    \ and Active Reload show no meaningful share (Titanic Magazine is the weapon core\
    \ at 98% / 6.7m), and the 7-day spread contains none of the dash assassins the\
    \ fear-cone thesis predicted. Extra Regen is not the trap the previous note called\
    \ it \u2014 97% at 2.1m with a baseline win rate makes it a mandatory lane tax\
    \ for 0 base regen, indifferent rather than informative. Changelog: released 2026-10-20\
    \ in Shh... This Won't Hurt a Bit., first full-week check (7.3k matches, no creator\
    \ content); nearly every item WR sits at 50.5-51%, so build-level signals are\
    \ weak and confidence is capped."
  builds:
  - name: Mag-dump sustain
    damage: gun
    core_items:
    - Extra Regen
    - Extended Magazine
    - Titanic Magazine
    - Extra Stamina
    - Kinetic Dash
    popularity: primary
    notes: 'The build lands before 10 minutes and buys uptime, not damage: Titanic
      Magazine (98%) is her fire-rate package and Kinetic Dash plus Extra Stamina
      buy the dash her kit lacks. Healing Booster is out now that it lost Extra Regen
      and +3 flat regen, so Extra Regen carries the lane alone.'
  - name: Cooldown/Duration spirit
    damage: spirit
    core_items:
    - Extra Spirit
    - Arcane Surge
    - Improved Spirit
    - Duration Extender
    - Superior Cooldown
    - Superior Duration
    popularity: secondary
    notes: "Every item she buys after ~18 minutes in these games is spirit, and Superior\
      \ Cooldown (52.7%) and Superior Duration (52.0%) are her two best non-luxury\
      \ win rates \u2014 ability uptime, not raw spirit, is the payload. Lean on Healing\
      \ Needles' 0.2->0.24 spirit scaling rather than flat heal-per-shot, which was\
      \ trimmed twice."
  - name: Ricochet gun carry
    damage: gun
    core_items:
    - Titanic Magazine
    - Extended Magazine
    - Healing Booster
    - Kinetic Dash
    - Ricochet
    popularity: niche
    notes: Ricochet's 59.1% is the sample's biggest outlier and the natural T4 for
      a charge economy fed by gun damage, but a 27-minute buy time means part of that
      win rate is 'already winning'.
  matchups:
    beats:
    - Billy
    - Mina
    - Solomon
    - Shiv
    - Pocket
    loses_to:
    - Baba
    - Dynamo
    - Celeste
    - Wraith
    - Ivy
  matchup_notes: "Lurking Terrors does its job on melee frontlines \u2014 Billy 59%,\
    \ Shiv 55%, Pocket 55% \u2014 but the day-0 claim that it taxes dash assassins\
    \ is unproven: Holliday, Calico, Yamato and Drifter do not appear as wins anywhere\
    \ in the window. Losses cluster at range and on AoE engage: Baba 43%, Celeste\
    \ 45%, Wraith 46% all trade from outside the cone, and Dynamo's 45% is a grouped\
    \ initiation beating her single-target heal."
  confidence: 0.6
  released_on: '2026-10-20'
  provisional: false


## What to do

Produce the post-patch knowledge base state for the heroes in this batch. This KB is read by the analyst on the *next* patch, so write it as durable state, not as a patch summary.

1. **hero_updates**: for each mover, the fields that changed. Allowed fields: role, archetypes, tier, trend, why, core_items, builds (full replacement list of {name, damage, core_items, popularity, notes}), matchups ({beats, loses_to}), enabled_by, countered_by, notes. When an item change kills or creates a build, update `builds`, not just `notes`. When another hero's change alters a matchup, update `matchups`. Set `last_changed_patch` to "Minor Update - 11-04-2026" for heroes that had direct changes. `why` is 1-2 sentences of present-tense state ("strong because X; weak to Y"), not a changelog. `notes` may hold a short changelog line (keep the last 3 lines, newest first). Do not touch heroes not in this batch.

   For each hero, output only the fields whose value actually changes. Omit any field that stays the same — omitted fields are kept as-is in the KB. Include `builds` only if at least one build is created, killed, or its core items change; when you include it, it is a full replacement list. Include `matchups` only if a matchup changes.
2. **change_log**: one line per KB edit you made, for the human to skim.

Tier is one of S/A/B/C/D. Trend is rising/stable/falling.

## Output schema

{
  "hero_updates": {"Hero Name": {"tier": "A", "trend": "falling", "why": "...", "core_items": ["..."], "last_changed_patch": "...", "notes": "..."}},
  "change_log": ["Hero Name: tier S -> A (Card Trick heal nerfs + Veil Walker loss)", "..."]
}
