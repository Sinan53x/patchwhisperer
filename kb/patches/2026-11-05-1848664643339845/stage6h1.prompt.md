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
 }
]

## Current hero entries (this batch only)

Seven:
  name: Seven
  role: spirit carry
  archetypes:
  - spirit carry
  - late scaler
  tier: S
  trend: rising
  why: "Jungle-payout carry: Haunt bounty and growth +10% lands squarely on the fastest\
    \ one-cycle clearer in the game, and the new comeback levers (30% non-hero cap,\
    \ tick souls to the two poorest) finally give a behind Seven a way back. The +10%\
    \ Haunt HP/damage barely costs a one-pass clear, and Static Charge T3 stun 0.9->1.1s\
    \ adds lockdown to the ability he uses to hold camps and fights \u2014 he still\
    \ dies to dives and Hook CC-locks before his AoE is up."
  core_items:
  - Mystic Vulnerability
  - Escalating Exposure
  - Healbane
  - Spirit Lifesteal
  - Arcane Surge
  - Monster Rounds
  - Cultist Sacrifice
  build_variants:
  - Spirit AoE carry
  - Farm/tempo hybrid
  enabled_by:
  - Abrams
  - Billy
  - Dynamo
  - Mo & Krill (frontline that makes space)
  - fastest clear of nine behavior-varied Haunt camps (Storm Cloud/Static Charge)
  - guaranteed high-value Tough-Crate routes
  - Healbane vs sustain comps
  countered_by:
  - Calico (dive)
  - Yamato (mobile burst)
  - Holliday (mobile burst)
  - Bebop (Hook CC-lock)
  - tempo/invade meta
  last_changed_patch: Halloween 2026 + Gameplay Update
  notes: "Halloween 2026 + Gameplay Update (10-30, direct): Static Charge T3 stun\
    \ 0.9->1.1s; Spirit Lifesteal +2/+2% and Healbane's multi-source anti-heal stacking\
    \ are both core, and Haunt bounty/growth +10% is pure profit for the fastest one-cycle\
    \ clearer \u2014 the new comeback levers also drop the 'farm a lead only' cap\
    \ on a behind Seven.\nShh... This Won't Hurt a Bit. (10-20, indirect): nine behavior-varied\
    \ Haunt types (grouped/chasing) make the fastest camp clear the biggest income\
    \ lever in the game; he has no crate or Barrel Mimic route and does not need one.\n\
    Paint the Town (10-16, indirect): fastest Haunt-camp clear plus telegraphed Plaza/Bell\
    \ Tower hub fights push him B->A; the no-comeback economy still caps a behind\
    \ Seven."
  builds:
  - name: Spirit AoE carry
    damage: spirit
    core_items:
    - Arcane Surge
    - Healbane
    - Mystic Vulnerability
    - Spirit Lifesteal
    - Escalating Exposure
    popularity: primary
    notes: Storm Cloud/Static Charge AoE with Escalating Exposure + Mystic Vulnerability
      stacking damage, Healbane + Spirit Lifesteal for sustain in extended fights.
  - name: Farm/tempo hybrid
    damage: hybrid
    core_items:
    - Monster Rounds
    - Extra Stamina
    - Cultist Sacrifice
    popularity: secondary
    notes: Early Monster Rounds and Cultist Sacrifice bankroll his fast jungle clear
      and soul lead; the 'best solo-queue farmer' identity, taken before the spirit
      core.
  matchups:
    beats:
    - Paradox
    - Lash
    - Vindicta
    - Billy
    - Drifter
    loses_to:
    - Calico
    - Abrams
    - Ivy
    - Bebop
    - Infernus
  matchup_notes: "Beats grouped/initiating S-tiers \u2014 Paradox and Lash (both 58%)\
    \ get punished by his AoE and out-ranged on engage, and Vindicta's 53% edge grows\
    \ as the patch grounds flyers. Loses to Calico (42%), who dives the immobile farmer\
    \ before his AoE is up, and to Abrams/Bebop, who either out-tank his burst or\
    \ Hook him out of Storm Cloud range."
  confidence: 0.52
  released_on: null
  provisional: false
Vindicta:
  name: Vindicta
  role: poke/siege carry
  archetypes:
  - poke/siege
  - gun carry
  tier: B
  trend: falling
  why: 'Max-range poke carry whose range guarantee is gone: High-Velocity Rounds velocity
    60->45% means fewer max-range hits land, and air drag 0.35->0.5 slows every airborne
    exit, so she still wants the roofs and telegraphed hub fights but now pays the
    flyer tax twice. Her gun core is intact, so this is a weaker version of the same
    hero rather than a dead one.'
  core_items:
  - High-Velocity Rounds
  - Opening Rounds
  - Extra Spirit
  - Extra Charge
  - Improved Spirit
  - Rapid Recharge
  - Long Range
  - Swift Striker
  - Counterspell
  - Sharpshooter
  - Burst Fire
  build_variants:
  - Gun poke
  - Spirit CDR / ult-poke
  enabled_by:
  - tempo economy (super-scaling trimmed)
  - increased 20m respawn timer
  - real early Rift fights (resist 10%+1%/min)
  - new roofs/high ground (lane hold + hub poke)
  - High-Velocity Rounds / Sharpshooter gun-core
  countered_by:
  - Silver (Weighted Bola grounds flyers)
  - High-Velocity Rounds velocity 60->45% (no max-range guarantee)
  - global slows and air drag 0.35->0.5 on airborne exits
  - Lash (mobile initiator)
  - dive/CC comps
  - Yamato (mobile burst assassin)
  last_changed_patch: Minor Update - 08-12-2026
  notes: "Halloween 2026 + Gameplay Update (10-30, indirect): High-Velocity Rounds\
    \ velocity 60->45% removes the max-range guarantee her gun core buys first and\
    \ air drag 0.35->0.5 taxes every airborne exit; the roofs and hub-fight value\
    \ are unchanged, the range is not.\nCity Never Sleeps (09-29, indirect): new roofs/high\
    \ ground and telegraphed Plaza/Bell Tower hub fights favor her max-range poke;\
    \ flyer tax unchanged.\n09-16 (indirect): global slows now bite air drag and Silver's\
    \ Weighted Bola grounds Flight \u2014 anti-flyer tax offsets her tempo gains,\
    \ so she held A."
  builds:
  - name: Gun poke
    damage: gun
    core_items:
    - High-Velocity Rounds
    - Opening Rounds
    - Long Range
    - Swift Striker
    - Counterspell
    - Sharpshooter
    - Burst Fire
    popularity: primary
    notes: Range/fire-rate weapon core to out-trade from max range; online by ~4 min
      and scales into Sharpshooter/Burst Fire, with Counterspell as the mandatory
      anti-dive/anti-burst slot.
  - name: Spirit CDR / ult-poke
    damage: spirit
    core_items:
    - Extra Spirit
    - Extra Charge
    - Improved Spirit
    - Rapid Recharge
    popularity: secondary
    notes: Spirit/CDR path to spam Flight and Assassinate and amplify Crow Familiar;
      note Extra Charge (99%) and Rapid Recharge (90%) ride along in almost every
      game even on the gun build.
  matchups:
    beats:
    - Venator
    - Mirage
    - Victor
    - Bebop
    - Abrams
    loses_to:
    - Vyper
    - Lash
    - Celeste
    - Wraith
    - Ivy
    - Silver
  matchup_notes: "Out-ranges and out-snipes other gun carries who want to stand and\
    \ trade (Venator 61%, Mirage 55%) and punishes immobile fronts (Victor 55%, Bebop\
    \ 54%, Abrams 53%). Folds to mobile divers and burst that close the gap before\
    \ she can kite \u2014 Lash 46%, Vyper 45%, Celeste 46% \u2014 the classic low-HP\
    \ flyer weakness."
  confidence: 0.63
  released_on: null
  provisional: false
Lady Geist:
  name: Lady Geist
  role: spirit bruiser
  archetypes:
  - tank/frontline
  - late scaler
  - spirit carry
  tier: A
  trend: falling
  why: 'Regen frontline whose engine lost its out-of-combat half: Radiant Regeneration
    now heals only in combat at 65->40 base with boon 1.7->1.4 and spirit 0.35->0.25,
    and she buys it in 98% of games, while Decay''s -55% incoming-heal penalty deepens
    on her own sustain. The Essence Bomb 1.22->1.35 spirit buff is real but only pays
    the Soul-Exchange variant, and the new tick-soul comeback softens her slow start
    without replacing the regen she lost.'
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
  last_changed_patch: Halloween 2026 + Gameplay Update
  notes: 'Halloween 2026 + Gameplay Update (10-30, direct): Essence Bomb 1.22->1.35
    spirit scaling only pays the Soul-Exchange line; Radiant Regeneration becomes
    in-combat-only at 65->40/1.7->1.4/0.35->0.25 on a 98%-buy slot, and Decay''s incoming-heal
    penalty deepens -50->-55% on a core slot she fights out of.

    Shh... This Won''t Hurt a Bit. (10-20, indirect): harder camps plus Barrel Mimic
    fights make farm a sustain check her regen stack passes, and container Bullet/Spirit
    Resist rolls add free frontline stats; the same dive heroes still eat her.

    10-14: Radiant Regeneration spirit scaling 0.04->0.035 (third cumulative trim)
    narrows her ~98%-buy regen core; the Spirit Soul-Exchange variant, which stacks
    the most spirit power, loses most.'
  builds:
  - name: Regen gun-bruiser
    damage: hybrid
    core_items:
    - Extra Regen
    - Monster Rounds
    - Mystic Regeneration
    - Radiant Regeneration
    - Juggernaut
    - Kinetic Dash
    - Berserker
    popularity: primary
    notes: 'Regen-first opener still survives a losing lane, but the out-of-combat
      half is gone: Radiant Regeneration only fires in combat now, so Juggernaut (+8->+15
      regen) replaces the Healing Booster line as the cheap regen top-up; Soul Exchange
      remains the finisher.'
  - name: Spirit Soul-Exchange
    damage: spirit
    core_items:
    - Mystic Regeneration
    - Radiant Regeneration
    - Mystic Burst
    - Bullet Resist Shredder
    - Spirit Resilience
    - Spirit Lifesteal
    popularity: secondary
    notes: Caster-leaning variant; Essence Bomb 1.22->1.35 buys the kill window, but
      the trimmed spirit scaling on Radiant Regeneration (0.35->0.25) hits the variant
      that stacks the most spirit hardest, so sustain shifts into Spirit Lifesteal.
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
Paradox:
  name: Paradox
  role: pick/sniper initiator
  archetypes:
  - burst caster
  - initiator
  - poke/siege
  tier: D
  trend: stable
  why: 'Carbine pick/sniper who traded pick quality for frequency: Paradoxical Swap
    at 95s buys her an extra pick per fight cycle, but Express Shot -5% secondary
    fire and HVR 60->45% velocity weaken the crit-carbine burst that pick converts.
    The ability-burst line gains relative value over the crit line; anything that
    closes distance still kills her.'
  core_items:
  - Restorative Shot
  - Headshot Booster
  - High-Velocity Rounds
  - Headhunter
  - Long Range
  - Sharpshooter
  - Express Shot
  - Slowing Hex
  - Mystic Burst
  - Tankbuster
  - Compress Cooldown
  build_variants:
  - Carbine sniper
  - Ability burst
  - Echo Shard bomb
  enabled_by:
  - Slowing Hex
  - Time Wall
  - Tankbuster
  - Dynamo
  - Mo & Krill
  - instant casts (carbine->swap combo fires on input, not the next window)
  - Paradoxical Swap cooldown 110->95s
  - new districts/hiding spots (roamer pick setups; ahead of Bebop)
  countered_by:
  - Yamato
  - Lash
  - Holliday
  - cleanse/dispel
  - Veil Walker
  - range denial
  last_changed_patch: Halloween 2026 + Gameplay Update
  notes: "Halloween 2026 + Gameplay Update (10-30, direct): Paradoxical Swap 110->95s\
    \ adds a pick per fight cycle; Express Shot -5% secondary-fire damage and HVR\
    \ velocity 60->45% cut the carbine crit burst \u2014 ability burst (Slowing Hex/Compress\
    \ Cooldown/Tankbuster) now outranks the HVR/Express Shot crit line.\nShh... This\
    \ Won't Hurt a Bit. (10-20, indirect): instant casts tighten her carbine->swap\
    \ combo, and Barrel Mimics leave squishy crate clearers stationary for picks;\
    \ mobile divers still close on her.\nPaint the Town (10-16, indirect): new districts,\
    \ more hiding spots and Steam-Vent invisibility sharpen her roamer pick setups\
    \ and keep her ahead of Bebop in that slot; the sniper line still folds to mobile\
    \ divers."
  builds:
  - name: Carbine sniper
    damage: gun
    core_items:
    - Restorative Shot
    - Headshot Booster
    - High-Velocity Rounds
    - Headhunter
    - Long Range
    - Sharpshooter
    - Express Shot
    popularity: primary
    notes: Stack weapon range and headshot damage and farm picks off Kinetic Carbine
      at max range; Headhunter/Express Shot reward carbine crits.
  - name: Ability burst
    damage: spirit
    core_items:
    - Slowing Hex
    - Mystic Burst
    - Tankbuster
    - Compress Cooldown
    popularity: secondary
    notes: Pulse Grenade + carbine spirit burst, Compress Cooldown to cycle Time Wall/Swap,
      Tankbuster for %HP damage into tanks; Slowing Hex sets up picks and peels dives.
  - name: Echo Shard bomb
    damage: hybrid
    core_items:
    - Echo Shard
    popularity: niche
    notes: The old double-bomb/swap combo build; usage data no longer shows Echo Shard
      in the top 15, so treat this as a personal-choice line, not the mainstream path.
  matchups:
    beats:
    - Grey Talon
    - Venator
    - Infernus
    - Pocket
    - Apollo
    loses_to:
    - Seven
    - Yamato
    - Lash
    - Celeste
    - Holliday
  matchup_notes: "She out-ranges and pins immobile poke/gun carries \u2014 Grey Talon\
    \ (59%) and Venator (57%) cannot contest Kinetic Carbine/Time Wall range. She\
    \ folds to anything that closes distance or dumps burst on her small HP pool:\
    \ Yamato (43%), Lash (43%) and Holliday (43%) all dive her, and Celeste (43%)\
    \ out-trades her outright."
  confidence: 0.72
  released_on: null
  provisional: false
Dynamo:
  name: Dynamo
  role: initiator/support
  archetypes:
  - initiator
  - support/healer
  tier: A
  trend: rising
  why: "Tempo initiator whose Singularity wins the now pre-announced hub fights \u2014\
    \ fights are scheduled at Bell Tower and Sunken Plaza, so setup is planned rather\
    \ than opportunistic. His ceiling is unchanged: the durable frontlines that eat\
    \ Singularity (Billy, Mo & Krill, Abrams) are also rising."
  core_items:
  - Extra Charge
  - Arcane Surge
  - Mystic Expansion
  - Compress Cooldown
  - Duration Extender
  - Warp Stone
  - Refresher
  - Superior Cooldown
  - Unstoppable
  - Debuff Reducer
  build_variants:
  - Spirit AoE initiator
  - Refresher double-ult
  enabled_by:
  - tempo conversion
  - telegraphed Plaza/Bell Tower hub fights (Singularity setup)
  - AoE dispel (Quantum Entanglement)
  - Refresher
  - Singularity pickoff
  - Diviner's Kevlar +10% ultimate CDR (09-16)
  - core tank items untouched
  countered_by:
  - durable frontline (Billy, Mo & Krill, Abrams)
  - Unstoppable buyers
  - long-range CC/silence on the channel
  - anti-heal vs Rejuvenating Aurora
  - Paige lane pressure
  last_changed_patch: Minor Update - 07-28-2026
  notes: "Shh... This Won't Hurt a Bit. (10-20, indirect): hub contests are pre-announced\
    \ (the Bell Tower rings map-wide), so his setup windows are planned rather than\
    \ opportunistic \u2014 good for coordination, bad for surprise, raising the value\
    \ of Unstoppable/Refresher on the channel.\nPaint the Town (10-16, indirect):\
    \ telegraphed Plaza/Bell Tower hub fights hand Singularity clean windows and Quantum\
    \ Entanglement's AoE dispel beats rising Lash/Drifter/Calico commits; durable-frontline\
    \ counters (M&K, Abrams) are the offset.\nCity Never Sleeps (09-29, indirect):\
    \ telegraphed Plaza/Bell Tower hub fights give Singularity clean setup windows;\
    \ initiator items untouched."
  builds:
  - name: Spirit AoE initiator
    damage: spirit
    core_items:
    - Extra Charge
    - Arcane Surge
    - Mystic Expansion
    - Compress Cooldown
    - Duration Extender
    - Warp Stone
    popularity: primary
    notes: "Every-game spine: cheaper, larger and more frequent Singularity/Rejuvenating\
      \ Aurora, with Warp Stone to reposition into the ult or escape after it \u2014\
      \ all high-share (74-78%) and early buys."
  - name: Refresher double-ult
    damage: spirit
    core_items:
    - Refresher
    - Superior Cooldown
    - Unstoppable
    - Debuff Reducer
    popularity: secondary
    notes: "Late spike for a second Black Hole; self-Unstoppable/Debuff Reducer make\
      \ the channel uninterruptible \u2014 these are his highest-WR items (Refresher\
      \ 57.2%, Superior Cooldown 56.6%)."
  matchups:
    beats:
    - Infernus
    - Calico
    - Drifter
    - Lash
    - Bebop
    loses_to:
    - Billy
    - Mo & Krill
    - Warden
    - Abrams
    - Paige
  matchup_notes: "Quantum Entanglement's AoE dispel is why he beats Infernus (59%)\
    \ and DOT/dive heroes \u2014 one cast strips burn and setup, and Calico/Drifter/Lash/Bebop\
    \ fold to AoE CC when they commit on him. He loses to durable frontline (Billy\
    \ 42%, Mo & Krill 45%, Abrams 49%): they eat Singularity, can't be repositioned,\
    \ and outlast the cooldown, while Paige (51%) simply wins the lane in front of\
    \ him."
  confidence: 0.72
  released_on: null
  provisional: false
Kelvin:
  name: Kelvin
  role: support/healer
  archetypes:
  - support/healer
  - late scaler
  tier: S
  trend: rising
  why: Support/healer whose dome is now an objective-fight tool at Bell Tower/Sunken
    Plaza and whose Extra Regen/Healing Booster core the Radiant Regeneration trims
    never touched. Cheap Healing Snacks cap how much dedicated healing he can sell,
    and anti-heal plus mobile dive still end him.
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
  notes: 'Shh... This Won''t Hurt a Bit. (10-20, indirect): harder camps and Barrel
    Mimic fights raise dome/sustain value while cheap Healing Snacks cap the between-fight
    healing he used to sell; his dome is worth most at the announced hub contests,
    not in lane.

    10-14: Radiant Regeneration spirit scaling 0.04->0.035 trims rival sustain (Baba,
    Lady Geist, Shiv, Celeste) while his Extra Regen/Healing Booster core is untouched
    - small relative gain.

    City Never Sleeps (09-29, indirect): harder Haunt camps raise the value of his
    dome/sustain; Healing Snacks (10% max HP) reduce the relative value of dedicated
    healing.'
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
Holliday:
  name: Holliday
  role: mobile assassin
  archetypes:
  - mobile assassin
  - initiator
  tier: D
  trend: rising
  why: 'Mobile lasso assassin built for the widened map: Steam Vent invisibility plus
    Barrel Mimic pauses create more stationary targets, and the map-wide Bell Tower
    call is a scheduled, pre-plannable pick window. Point-blank lockdown that punishes
    her commit-heavy entry is still the answer.'
  core_items:
  - Extra Charge
  - Extra Spirit
  - Rapid Recharge
  - Improved Spirit
  - Mystic Burst
  - Superior Duration
  - Superior Cooldown
  - Sprint Boots
  - Extra Stamina
  - Recharging Rush
  - Veil Walker
  - Stamina Mastery
  - Tankbuster
  build_variants:
  - Charge-spirit pick
  - Stamina hybrid skirmisher
  enabled_by:
  - tempo meta (comeback gutted; lane wins snowball)
  - 20m respawn 35->38s (picks worth more)
  - new districts/hiding spots/Steam Vent invisibility (roam routes)
  - Bell Tower hub fights (lasso picks)
  - Spirit Lasso buff + longer lasso
  - Crackshot T2 resist-shred
  - bounce-pad double-charge via Extra Charge/Rapid Recharge
  countered_by:
  - Veil Walker nerf (lost Sprint Boots + movespeed-on-break)
  - Bebop hook
  - Mo & Krill / Lash lockdown ultimates
  - Drifter melee bruiser pressure
  - Warden slowing gun pressure
  - slows now apply to air drag / slows-as-CC up
  last_changed_patch: Minor Update - 09-16-2026
  notes: "Shh... This Won't Hurt a Bit. (10-20, indirect): behavior-varied camps and\
    \ Barrel Mimics leave farmers stationary at predictable spots \u2014 more lasso\
    \ targets \u2014 and the Bell Tower payout is a scheduled map-wide announcement\
    \ she can pre-place bounce pads around.\nPaint the Town (10-16, indirect): new\
    \ districts and Steam-Vent invisibility expand her roam routes and Bell Tower\
    \ hub fights reward Spirit Lasso picks; point-blank lockdown still punishes her\
    \ commit.\nCity Never Sleeps (09-29, indirect): new districts/hiding spots/Steam\
    \ Vents expand her roam routes and Bell Tower hub fights reward lasso picks."
  builds:
  - name: Charge-spirit pick
    damage: spirit
    core_items:
    - Extra Charge
    - Extra Spirit
    - Rapid Recharge
    - Improved Spirit
    - Mystic Burst
    - Superior Duration
    - Superior Cooldown
    popularity: primary
    notes: Buy the T1 charges (Extra Charge ~3.7m, Rapid Recharge) to double-dip bounce-pad/lasso
      casts, then spirit and duration to convert picks; the duration/cooldown finishers
      carry her highest win rates.
  - name: Stamina hybrid skirmisher
    damage: hybrid
    core_items:
    - Sprint Boots
    - Extra Stamina
    - Recharging Rush
    - Veil Walker
    - Stamina Mastery
    - Tankbuster
    popularity: secondary
    notes: "Stamina stack plus Recharging Rush to survive the skirmish and reposition;\
      \ Veil Walker is bought (57%) for the break despite losing its movespeed-on-break,\
      \ and this is the source of the 'gun hybrid' label \u2014 there is no real gun\
      \ build in the data."
  matchups:
    beats:
    - Haze
    - Paradox
    - Mina
    - Calico
    - Wraith
    loses_to:
    - Drifter
    - Bebop
    - Warden
    - Lash
    - Mo & Krill
  matchup_notes: 'She farms squishy, immobile poke/gun carries (Haze 57%, Wraith,
    Paradox) by closing with bounce-pad and lassoing them out of position. She loses
    to point-blank lockdown and anti-mobility: Drifter''s melee bruiser pressure (42%),
    Bebop''s hook, and Mo & Krill/Lash ults punish a low-HP assassin who has to commit
    on entry.'
  confidence: 0.6
  released_on: null
  provisional: false
Mo & Krill:
  name: Mo & Krill
  role: spirit tank initiator
  archetypes:
  - tank/frontline
  - initiator
  tier: B
  trend: falling
  why: "Still the default sustained front line \u2014 Scorn/Burrow, Torment Pulse's\
    \ +4% melee resist and an unchanged Combo keep him a lockdown tank \u2014 but\
    \ Spirit per boon 1.1->0.6 and -10% spirit damage on every ability mean he now\
    \ holds targets without threatening them."
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
  last_changed_patch: Halloween 2026 + Gameplay Update
  notes: "Halloween 2026: spirit per boon 1.1->0.6 and -10% spirit damage on every\
    \ ability; Combo untouched, bullet per boon +4% \u2014 move one slot to gun (Bullet\
    \ Lifesteal/Battle Vest). Torment Pulse +4% melee resist up; Decay's deeper self-heal\
    \ penalty and Healbane heal-on-kill 275->170 down.\nShh... This Won't Hurt a Bit.\
    \ (10-20, indirect): harder Haunt camps and contested Buff Containers reward his\
    \ sustained frontline; objective parries no longer reset, trimming the free Guardian-dive\
    \ chain.\nPaint the Town: no direct change; the Haunt-camp/hub economy keeps him\
    \ the default sustained front line, but objective parries no longer reset \u2014\
    \ the free dive chain is trimmed."
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
  tier: D
  trend: falling
  why: 'The knife exchange got better (Serrated Knives rage 3.5%->4% current HP, +T3
    spirit scaling) but his pre-fight health is gone: Radiant Regeneration now heals
    only in combat at 65->40 and Healbane''s kill-heal was cut, so he starts fights
    smaller and executes in a shorter window.'
  core_items:
  - Mystic Regeneration
  - Extra Regen
  - Radiant Regeneration
  - Spirit Lifesteal
  - Healbane
  - Extra Charge
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
  last_changed_patch: Halloween 2026 + Gameplay Update
  notes: "Halloween 2026: Serrated Knives rage 3.5%->4% + T3 spirit scaling up, Killing\
    \ Blow recast 16->12s, alt-fire per boon -5%; Radiant Regeneration went in-combat-only\
    \ at 65->40 and Healbane kill-heal 275->170, so his pre-fight buffer is gone \u2014\
    \ Torment Pulse +4% melee resist is the offset.\nShh... This Won't Hurt a Bit.\
    \ (10-20, indirect): harder camps reward his regen stack and the rising frontline\
    \ feeds current-HP Serrated Knives, but vents hand divers a free approach before\
    \ he ramps.\nPaint the Town: no direct change; harder Haunt camps reward his regen\
    \ stack and the rising frontline feeds Serrated Knives, but a 43.4% snapshot WR\
    \ keeps this soft."
  builds:
  - name: Spirit sustain bruiser
    damage: spirit
    core_items:
    - Mystic Regeneration
    - Extra Regen
    - Radiant Regeneration
    - Spirit Lifesteal
    - Healbane
    - Extra Charge
    popularity: primary
    notes: "Radiant Regeneration is now an in-combat heal only (65->40, boon 1.7->1.4,\
      \ spirit 0.35->0.25), so it no longer pays for rotation/farm \u2014 stack in-fight\
      \ Spirit Lifesteal and cheap Juggernaut regen (8->15) beside it rather than\
      \ leaning on Radiant as an out-of-combat engine."
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
      (40% share) carries his best win rate at 59%, and Torment Pulse's +4% melee
      resist is the one piece of the front-line package that improved this patch.
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
Ivy:
  name: Ivy
  role: support/healer
  archetypes:
  - support/healer
  tier: A
  trend: falling
  why: "Still the best peel in the game (Stone Form i-frame/stun) and a 53.7% WR support,\
    \ but every piece of her heal path got worse in one patch \u2014 Healbane now\
    \ stacks across sources to cut tethers, Healing Booster lost its Extra Regen link\
    \ and Healing Nova went spirit-scaled \u2014 so her gun core is the only build\
    \ worth funding."
  core_items:
  - Monster Rounds
  - Extended Magazine
  - Titanic Magazine
  - Tesla Bullets
  - Active Reload
  - Capacitor
  - Extra Regen
  - Healbane
  - Healing Booster
  build_variants:
  - Gun Ivy (stat-check carry-support)
  - Heal / anti-heal support
  - Spirit AoE / control utility
  enabled_by:
  - frontline tanks (Abrams, Billy, Victor)
  - gun item core (Titanic Magazine, Tesla Bullets)
  - team sustain / tether
  - Air Drop map control
  - dive partners (Drifter, Venator) she can heal-tether
  countered_by:
  - anti-heal (Healbane)
  - mobile burst (Vyper, Yamato, Lash, Holliday)
  - displacement (Dynamo, Mo & Krill)
  - silence
  - grounding / air-drag slow (hits Air Drop)
  last_changed_patch: Minor Update - 09-16-2026
  notes: "Halloween 2026 (indirect, item-driven): Healbane now stacks across sources\
    \ \u2014 the worst system change for tether healing \u2014 Healing Booster lost\
    \ its Extra Regen upgrade and +3 flat regen, and Healing Nova moved to spirit\
    \ scaling off her gun-first build. Skip the heal package.\nShh... This Won't Hurt\
    \ a Bit. (10-20, indirect): Healing Snacks plus spread corridors cut the value\
    \ of a grouped healer; districts pull her team apart, so tether a frontline bruiser\
    \ sweeping corridors instead of a lane partner.\nCity Never Sleeps: no direct\
    \ line; peercontent floats a small lift off camp-damage sustain, but the Healing\
    \ Snack addition and trimmed heal items cut both ways for her (low confidence)."
  builds:
  - name: Gun Ivy (stat-check carry-support)
    damage: gun
    core_items:
    - Monster Rounds
    - Extended Magazine
    - Titanic Magazine
    - Tesla Bullets
    - Active Reload
    - Capacitor
    popularity: primary
    notes: 'Default slot: early mag/regen into Titanic + Tesla for sustained gun DPS,
      Capacitor late for the stun/utility spike.'
  - name: Heal / anti-heal support
    damage: hybrid
    core_items:
    - Extra Regen
    - Healbane
    - Healing Booster
    popularity: secondary
    notes: "Sustain package layered on the gun core \u2014 Healing Booster to amplify\
      \ her tether heals, Healbane to cut enemy healing; run when the enemy team has\
      \ real sustain or burst you can't out-trade."
  - name: Spirit AoE / control utility
    damage: spirit
    core_items:
    - Mystic Expansion
    - Bullet Resist Shredder
    - Superior Duration
    - Greater Expansion
    popularity: niche
    notes: Late pickups that widen Stone Form/Entangling Thorns and stretch the tether/ult;
      buy only when fights are clumped and you already have the gun core.
  matchups:
    beats:
    - Mina
    - Haze
    - Abrams
    - Rem
    - Victor
    loses_to:
    - Vyper
    - Yamato
    - Dynamo
    - Mo & Krill
    - Viscous
  matchup_notes: "She beats committed, immobile damage and frontline \u2014 Haze (59%)\
    \ and Abrams (59%) cannot punish the Stone Form i-frame/stun, and Kudzu Connection\
    \ out-sustains their chip while she out-ranges tanks. She loses to mobile burst\
    \ and displacement: Vyper (44%) and Yamato (47%) kill through her low-HP heal\
    \ before tether matters, while Dynamo and Mo & Krill (48%) displace her out of\
    \ tether range and stun past the Form window."
  confidence: 0.62
  released_on: null
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
