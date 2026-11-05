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
 }
]

## Current hero entries (this batch only)

Yamato:
  name: Yamato
  role: mobile burst assassin
  archetypes:
  - mobile assassin
  - burst caster
  tier: D
  trend: falling
  why: Still the camp-clear and objective-path champion, but Flying Slash 26->23m
    (T3 +8m) and Shadow Transformation pushed to T2 at 160s cut the engage reach and
    the all-in speed a mobile burst assassin is bought for. She now has to buy the
    gap back with stamina routes instead of range.
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
  last_changed_patch: Halloween 2026 + Gameplay Update
  notes: 'Halloween 2026: Flying Slash 26->23m (T3 +15->+8m) with the mark visible
    on cast, Shadow Transformation 150->160s and moved to T2, Power Slash +6% spirit
    scaling. Hunter''s Aura LOS gate and Healbane kill-heal 275->170 trim her late
    spirit line; Torment Pulse +4% melee resist helps her commit.

    Shh... This Won''t Hurt a Bit. (10-20): Flying Strike creates paths against solid
    targets (turrets, Shrines, objectives) for extra mobility/objective access; parry
    no longer resets on objectives, so her Shrine/Walker dive is one-shot.

    Paint the Town: no direct change; punch AoE is still the fastest clear for the
    new grouped, behavior-varied Haunt camps and Flying Strike paths open the separated
    Shrine/objective layout.'
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
Viscous:
  name: Viscous
  role: tank/enabler
  archetypes:
  - tank/frontline
  - support/healer
  tier: D
  trend: falling
  why: Splatter T1 +36->+45 damage and +5% alt-fire growth give his lane poke real
    numbers, and Cube rescue gains from scheduled hub fights, but he is still a B
    enabler with no post-patch win rate proving the 09-16 cooldown/Cube trims are
    absorbed.
  core_items:
  - High-Velocity Rounds
  - Mystic Burst
  - Mystic Shot
  - Express Shot
  - Spirit Strike
  - Mystic Expansion
  - Spirit Snatch
  - Tankbuster
  - Superior Cooldown
  build_variants:
  - Spirit-hybrid Splatter/Punch
  - Cooldown Cube support
  enabled_by:
  - Cube rescue
  - Goo Ball T3 spirit scaling
  - Rem
  - Paige
  - tank-frontline comps (Billy, Apollo)
  countered_by:
  - Lash
  - Mo & Krill
  - Drifter
  - Silver (Weighted Bola)
  - tempo snowball meta
  - global slows (slow-as-CC)
  last_changed_patch: Minor Update - 09-16-2026
  notes: 'Halloween 2026: Splatter T1 +36->+45 damage and +5% alt-fire damage growth
    per boon, Goo Ball melee/Ethereal Shift exploit during cast delay fixed; Express
    Shot secondary-fire -5% sits in his core. Tier holds B.

    Shh... This Won''t Hurt a Bit. (10-20, indirect): Bell Tower''s spread vaults
    and four corridors suit Goo Ball traversal, and harder camps plus forced hub fights
    raise Cube rescue value.

    City Never Sleeps: no direct line; harder camps reward Cube sustain and spread-out
    vaults suit Goo Ball, but this is a low-confidence lift.'
  builds:
  - name: Spirit-hybrid Splatter/Punch
    damage: hybrid
    core_items:
    - High-Velocity Rounds
    - Mystic Burst
    - Mystic Shot
    - Express Shot
    - Spirit Strike
    - Mystic Expansion
    - Spirit Snatch
    - Tankbuster
    popularity: primary
    notes: Spirit-scaling Splatter and Puddle Punch poke carried by spirit-hybrid
      weapon items; his default lane-and-skirmish shell.
  - name: Cooldown Cube support
    damage: spirit
    core_items:
    - Sprint Boots
    - Veil Walker
    - Improved Spirit
    - Compress Cooldown
    - Superior Cooldown
    - Greater Expansion
    popularity: secondary
    notes: Cooldown-stacking enabler shell that maximizes Cube uptime and Goo Ball
      resets for coordinated rescue plays.
  matchups:
    beats:
    - Pocket
    - Haze
    - Calico
    - Abrams
    - Vindicta
    loses_to:
    - Mo & Krill
    - Lash
    - Drifter
    - Warden
    - Wraith
  matchup_notes: 'Beats Pocket/Haze/Calico because Cube nullifies their burst windows
    and his tanky frontline out-trades squishy carries; Abrams is a sustain-vs-sustain
    grind he edges. Loses to Mo & Krill (43%) and Lash (46%): Lash''s mobility and
    displacement punish a slow enabler, and Mo & Krill''s tank-sustain plus combo
    out-trades him; Drifter''s melee bruiser kit does the same.'
  confidence: 0.55
  released_on: null
  provisional: false
Pocket:
  name: Pocket
  role: spirit carry
  archetypes:
  - spirit carry
  - burst caster
  - late scaler
  - mobile assassin
  tier: D
  trend: rising
  why: 'The economy flipped in his favour: 30% non-hero comeback gold, tick souls
    to the two poorest and up to 50% faster secure when behind fund the slow Affliction
    ramp the last meta killed. Still folds to anything that out-ranges him (Celeste)
    or sticks to a low-HP caster (Warden, Drifter, Viscous).'
  core_items:
  - Mystic Burst
  - Monster Rounds
  - Cold Front
  - Cultist Sacrifice
  - Dispel Magic
  - Majestic Leap
  - Mystic Expansion
  - Tankbuster
  - Superior Cooldown
  - Spirit Burn
  - Superior Duration
  - Greater Expansion
  build_variants:
  - Affliction spirit burst
  - Cloak skirmish
  enabled_by:
  - Affliction (win-condition DoT)
  - sidelane wave clear
  - Majestic Leap (engage/escape)
  - mobility cloak
  countered_by:
  - Counterspell (removes Affliction)
  - tempo comps (close the game before he scales)
  - roots/lockdown (Warden, Viscous slows)
  - burst that out-ranges him (Celeste)
  last_changed_patch: Minor Update - 07-28-2026
  notes: "Halloween 2026 (indirect): the comeback levers (non-hero comeback cap 26->30%,\
    \ tick souls to the two poorest, deficit-scaled secure speed) reverse the premise\
    \ of his B-falling read \u2014 the farm bail-out now arrives before his Affliction\
    \ spike. No core item moved.\nChangelog: 09-16 - no direct line; 30-day usage\
    \ shows no gun build (Monster Rounds 92%, Cultist Sacrifice 93%), so the spirit\
    \ stack stands.\nOld entry's core (Boundless Spirit, Echo Shard, Fortitude) shows\
    \ zero current usage \u2014 replaced with the spirit stack the data actually shows."
  builds:
  - name: Affliction spirit burst
    damage: spirit
    core_items:
    - Mystic Burst
    - Cold Front
    - Tankbuster
    - Superior Cooldown
    - Spirit Burn
    - Superior Duration
    - Greater Expansion
    popularity: primary
    notes: "The default ranked build \u2014 burst plus duration to maximize Affliction's\
      \ DoT and Barrage; buy order Mystic Burst/Cold Front early, Tankbuster\u2192\
      Spirit Burn\u2192Superior Duration late (99% Mystic Burst, 95% Tankbuster)."
  - name: Cloak skirmish
    damage: hybrid
    core_items:
    - Monster Rounds
    - Cultist Sacrifice
    - Majestic Leap
    - Mystic Expansion
    - Dispel Magic
    popularity: secondary
    notes: "Farm-speed plus mobility/survivability splash \u2014 Monster Rounds/Cultist\
      \ Sacrifice to clear camps, Majestic Leap and Dispel Magic to engage or bail\
      \ out; taken when the enemy comp punishes the all-in."
  matchups:
    beats:
    - Venator
    - Apollo
    - Mirage
    - Abrams
    - Wraith
    loses_to:
    - Celeste
    - Warden
    - Drifter
    - Haze
    - Viscous
  matchup_notes: 'Beats squishy carries he can cloak onto and burst before they scale
    (Venator 54%, Apollo 53%, Mirage 52%). Loses to anything that out-ranges or sticks
    to a low-HP caster: Celeste out-trades at range (39%), Warden''s root and gun
    pressure catch the dive (41%), and Drifter/Viscous stay glued to him (41%/44%).'
  confidence: 0.58
  released_on: null
  provisional: false
Mirage:
  name: Mirage
  role: split-push hybrid carry
  archetypes:
  - gun carry
  - split pusher
  - late scaler
  tier: D
  trend: falling
  why: 'Split-push hybrid the patch buried: souls moved off the lanes into corridors
    and shared objectives, so sidelane pressure converts to less income, and Steam-Vent
    invisibility hands roamers a free approach on his map-play. Farm corridors instead;
    Djinn''s Mark picks isolated camp clearers.'
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
  notes: "Shh... This Won't Hurt a Bit. (10-20, indirect): souls moved off the lanes\
    \ into corridors and shared objectives, so split-push converts to less income;\
    \ Steam Vents give roamers a free approach on his map-play.\nPaint the Town: no\
    \ direct change; contested Soul Bags and earlier hub objectives worsen a slow\
    \ split-pusher, and rising M&K/Lash dive him off his map-play \u2014 beaten by\
    \ the meta, not the notes.\n10-05: trooper-speed fix restores intended wave pathing\
    \ so his split-push converts on schedule (tiny QoL)."
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
Vyper:
  name: Vyper
  role: gun carry
  archetypes:
  - gun carry
  tier: D
  trend: falling
  why: Pure-gun carry whose spirit-amp splice is already gutted; Buff Containers'
    permanent Bullet Resist rolls tax her entire damage type for the match and Barrel
    Mimics punish the crate chains she has no disengage to escape. Still farms CC-light
    comps, still lifted out by hard-CC initiation (Dynamo, Mo & Krill).
  core_items:
  - Close Quarters
  - Rapid Rounds
  - Split Shot
  - Burst Fire
  - Quicksilver Reload
  build_variants:
  - Gun build
  - Spirit-amp
  - Survive-the-CC
  enabled_by:
  - no-CC lobbies
  - gun-cycle/reload smoothing (09-16)
  - Paige
  countered_by:
  - CC/knockup comps
  - Lash
  - Billy
  - Yamato
  - Apollo
  - Dynamo
  - Mo & Krill
  - The Doorman
  - Plated Armor buyers (hard-counter the spirit-on-hit splice)
  last_changed_patch: Minor Update - 09-16-2026
  notes: '10-20 Shh...: no direct change; Bullet Resist container rolls tax her gun
    all game and Barrel Mimics punish crate chains she cannot disengage from.

    09-16: Slither T3 barrier 5->4s / Petrifying Bola cd 105->115s are cosmetic; the
    real hit is indirect (Mercurial Magnum gut + Plated Armor on-hit fix), tier A->B,
    build pivots to pure gun.

    54.6% WR / 26.9% PR is a pre-09-16 baseline (14-day snapshot, mostly pre-patch).'
  builds:
  - name: Gun build
    damage: gun
    core_items:
    - Close Quarters
    - Rapid Rounds
    - Split Shot
    - Burst Fire
    popularity: primary
    notes: 'Now the main carry path: with Mercurial Magnum gutted (base 25->20%, scaling
      0.49->0.38) and Plated Armor blocking her spirit on-hit, the old near-universal
      (79-93%) spirit splice is weakened. Swift Striker (58%) and Tesla Bullets (52%)
      stay flex adds for close-range/AoE, though Tesla''s damage is now blocked by
      Plated Armor too.'
  - name: Survive-the-CC
    damage: hybrid
    core_items:
    - Grit
    - Spirit Shielding
    - Stamina Mastery
    - Unstoppable
    - Debuff Reducer
    popularity: niche
    notes: Defensive overlay (47-71% share) into knockup/CC comps - Unstoppable +
      Debuff Reducer keep the gun online vs Dynamo and Mo & Krill; more load-bearing
      now that her spirit-amp damage is gone.
  matchups:
    beats:
    - Mina
    - Calico
    - Infernus
    - Haze
    - Ivy
    loses_to:
    - Dynamo
    - Warden
    - Billy
    - Mo & Krill
    - Wraith
  matchup_notes: 'Data beats CC-light squishies - Mina (60%), Calico (58%), Infernus
    (58%) can''t trade into her gun and have no hard interrupt to stop the dive. The
    genuine losing lanes are initiation/CC: Dynamo (46%) and Mo & Krill lift/combo
    her out of the fight and Warden''s (48%) cage/trap punishes the dive. Note the
    creator-flagged counters (Billy 50%, Silver/Venator) do NOT show in data - so
    treat ''she loses to CC'' as a comp-level problem, not a specific-hero counter.'
  confidence: 0.6
  released_on: null
  provisional: false
Mina:
  name: Mina
  role: mobile spirit assassin
  archetypes:
  - mobile assassin
  - burst caster
  tier: D
  trend: stable
  why: "Mobile burst assassin with one of the patch's best farm shapes \u2014 grouped\
    \ Haunt camps and new districts suit her AoE clear and dive routes \u2014 but\
    \ her single-target rotation still cannot kill the tank front line (Billy, Mo\
    \ & Krill, Victor), and that archetype just got better. Yamato still owns the\
    \ mobile-burst niche."
  core_items:
  - Extra Spirit
  - Mystic Burst
  - Quicksilver Reload
  - Mystic Expansion
  - Improved Spirit
  - Extra Stamina
  - Dispel Magic
  - Stamina Mastery
  - Tankbuster
  - Boundless Spirit
  - Spirit Shredder Bullets
  - Spirit Burn
  build_variants:
  - Spirit burst
  - Gun-weave shred
  enabled_by:
  - tempo/snowball meta (early mobile kills)
  - mobility + burst damage kit
  - spirit burst item curve (Mystic Burst, Boundless Spirit)
  - ult silence
  countered_by:
  - CC/lockdown (Mo & Krill, Billy, Victor)
  - sustain/healing (Ivy)
  - tank/bruiser frontline that survives her burst
  - Yamato (owns the mobile-assassin niche)
  last_changed_patch: Minor Update - 07-28-2026
  notes: '10-20 Shh...: no direct change; grouped Haunt camps and new districts suit
    her AoE clear and dive routes, but the tank frontline she cannot kill got better.

    09-29 City Never Sleeps: no direct change; camp/uptime patch rewards grouped-camp
    AoE clear and new-district mobility, but her damage gap is unchanged.

    Last direct touch: 07-28-2026.'
  builds:
  - name: Spirit burst
    damage: spirit
    core_items:
    - Extra Spirit
    - Mystic Burst
    - Quicksilver Reload
    - Mystic Expansion
    - Improved Spirit
    - Extra Stamina
    - Dispel Magic
    - Stamina Mastery
    - Tankbuster
    - Boundless Spirit
    popularity: primary
    notes: "Spirit-power burst with a near-universal stamina/dispel backbone (all\
      \ ~96-100% share) \u2014 dive a squishy carry and delete them before they react,\
      \ using Quicksilver Reload to cycle abilities through reloads and Dispel Magic\
      \ to clear the CC that otherwise ends her."
  - name: Gun-weave shred
    damage: hybrid
    core_items:
    - Quicksilver Reload
    - Spirit Shredder Bullets
    - Spirit Burn
    popularity: secondary
    notes: Adds spirit-shred and %HP burn so gun autos keep damage up between cooldowns;
      the minority path (~66% share) players take when the enemy stacks tank, though
      it still loses the tank matchup.
  matchups:
    beats:
    - Mirage
    - Pocket
    - Haze
    - Venator
    - Vindicta
    loses_to:
    - Ivy
    - Vyper
    - Billy
    - Mo & Krill
    - Victor
  matchup_notes: "She beats the squishy carries she can dive and burst \u2014 Mirage,\
    \ Pocket, Haze (52-53%) \u2014 where her mobility converts a kill before they\
    \ can react. She loses hard to tanks and bruisers with CC/sustain (Billy 43%,\
    \ Mo & Krill 43%, Victor 44%) and to Ivy (40%), who out-heals her burst. Single-target\
    \ burst into heroes that survive the first rotation is the whole story."
  confidence: 0.7
  released_on: null
  provisional: false
Drifter:
  name: Drifter
  role: melee bruiser
  archetypes:
  - mobile assassin
  - tank/frontline
  tier: B
  trend: rising
  why: "Blind-pickable spirit-melee bruiser whose roaming income got richer \u2014\
    \ Haunt bounty/growth +10% rewards his heavy-melee crate and Steam Vent routes,\
    \ and stacking anti-heal (Toxic Bullets 40%, Healbane) composes with his built-in\
    \ heal cut into a real answer against sustain comps. Still no hard CC or closing\
    \ mobility, so lane bullies cap him at A."
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
  last_changed_patch: Halloween 2026 + Gameplay Update
  notes: 'Halloween 2026: base gun damage +3%, Bloodscent T3 +11%->+12% amp, Eternal
    Night T3 +2.5->2.75s; Haunt bounty/growth +10% raises his crate/vent roam income
    and multi-source anti-heal now composes with his built-in heal cut.

    10-20 Shh...: no direct change; Steam Vents, new hiding spots and heavy-melee
    Tough Crates extend his stealth-roam and give his melee core uncontestable crate
    income.

    09-29 City Never Sleeps: no direct change; new districts/Steam Vents and heavy-melee
    Tough-Crate routes fit his roam.'
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
  tier: S
  trend: rising
  why: 'Sustain frontline the patch actively fed: Spirit Lifesteal +2 spirit/+2% lifesteal,
    Infuser 6->8 spirit with a 75% active lifesteal window and Torment Pulse +4% melee
    resist all compound his grind-down shell, which is also the reliable answer to
    Haunts that now hit 10% harder. Healing Booster''s rework delays the shell''s
    early curve.'
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
  last_changed_patch: Halloween 2026 + Gameplay Update
  notes: "Halloween 2026: Aura of Suffering T3 +15%->+16%; Spirit Lifesteal, Infuser\
    \ (6->8 spirit, 75% active lifesteal) and Torment Pulse +4% melee resist feed\
    \ the grind-down core, while Healing Booster lost its Extra Regen link and +3\
    \ regen \u2014 buy it standalone, later.\n10-20 Shh...: no direct change; harder\
    \ Haunt camps, longer PvE routes and Buff Container Bullet/Spirit Resist rolls\
    \ feed his sustain stack \u2014 A held.\n09-29 City Never Sleeps: no direct change;\
    \ hard Haunt camps fed his sustain stack, flipping him from fair B-baseline to\
    \ A on the 56.4% snapshot WR."
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
  trend: falling
  why: "Still the best lane-winning support, but her lane itself got thinner \u2014\
    \ base bullet damage 35->32 is roughly a 9% lane cut \u2014 and the new economy\
    \ (tick souls to the two poorest, 30% non-hero comeback cap, deficit-scaled secure\
    \ rate) now rescues exactly the carry she used to snowball past. She wins lane;\
    \ the conversion is slower than on 10-20."
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
  - stacking anti-heal (multi-source Healbane, Toxic Bullets 40%, Crippling Headshot
    40%)
  last_changed_patch: Halloween 2026 + Gameplay Update
  notes: "10-30 Halloween + Gameplay Update: base bullet 35->32 (~9% lane cut; growth\
    \ 0.52->0.61 pays back later); HVR velocity 60->45 weakens her 1.2-min buy \u2014\
    \ Opening Rounds before HVR is now the safer opener, and comeback gold blunts\
    \ the lead she converts.\n10-20 Shh...: no direct change; Healing Snacks let her\
    \ lane pressure stick instead of resetting on a recall, and lane-adjacent crate\
    \ routes from ~2:30 pay the lane winner immediately \u2014 S held.\nCity Never\
    \ Sleeps: no direct change; lane-adjacent crate routes and Healing Snacks reward\
    \ her lane pressure, and the contested hubs suit her carry-snowball."
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
Apollo:
  name: Apollo
  role: lane bully initiator
  archetypes:
  - lane bully
  - initiator
  - tank/frontline
  tier: C
  trend: stable
  why: "S-tier lane bully whose Riposte now lands reliably (dash fixes, CC refunds\
    \ on Flawless Advance/Itani Lo Sahn) for a 1.5s disable instead of a 0.8s stun\
    \ \u2014 longer lockdown for picks, but no longer an interrupt for channeled ults,\
    \ and Healing Booster's gutting thins the sustain shell his spirit bruiser build\
    \ leans on."
  core_items:
  - Extra Regen
  - Mystic Burst
  - Extra Spirit
  - Mystic Expansion
  - Spirit Strike
  - Improved Spirit
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
  - Riposte reliability + 1.5s disable (dash fixes, CC refunds)
  - spirit item pool untouched
  - tower-dive still open with T3 bullet resist vs the parry-cooldown change
  countered_by:
  - Lash
  - Abrams
  - Mo & Krill
  - Warden
  - anti-heal vs his Locket/heal sustain
  last_changed_patch: Halloween 2026 + Gameplay Update
  notes: "10-30 Halloween + Gameplay Update: Riposte Pommel Hit is now an immobilize\
    \ + parry disable, not a stun \u2014 0.8->1.5s (T2 +0.4->+0.6s) with dash reliability\
    \ fixes and CC refunds on Flawless Advance/Itani Lo Sahn. He loses the channel\
    \ interrupt (Seven/Bebop/Harrow ults) and Healing Booster's gutting thins his\
    \ sustain; S held, trend rising -> stable.\n10-20 Shh...: no direct change; lane\
    \ pressure converts into lane-adjacent crate routes and Healing Snacks, but the\
    \ objective-parry change makes the Guardian dive a one-shot decision \u2014 S\
    \ held.\n10-16 Paint the Town: no direct change; the objective-parry cooldown-reset\
    \ removal trims the T3-bullet-resist Guardian-dive chain, but the crate-and-Haunt\
    \ economy keeps him S."
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
    - Restorative Locket
    - Spirit Snatch
    - Boundless Spirit
    - Tankbuster
    popularity: primary
    notes: Lane-phase spirit poke into flat spirit burst; Healing Booster is out of
      the shell now that it lost Extra Regen and its +3 flat regen, so Restorative
      Locket carries the sustain instead. Boundless Spirit and Tankbuster are late-game
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
