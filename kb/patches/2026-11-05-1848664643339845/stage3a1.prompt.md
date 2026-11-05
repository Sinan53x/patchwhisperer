# Task: fact-check hero entries against the patch notes

Patch: Minor Update - 11-04-2026 (2026-11-05)

A separate analyst wrote the entries below. Find mistakes by comparing each entry with its hero's note lines. The notes are the only source of truth for what changed.

## Note lines

Apollo:
  - [rework] Riposte: Apollo: Riposte - Pommel Hit now also disarms the enemy
  - [rework] Riposte: Apollo: Riposte - Pummel hit now ends any preexisting parry on the target
  - [buff] Riposte: Apollo: Riposte - T2 increased from +0.6s duration to +0.7s
  - [buff] Itani Lo Sahn: Apollo: Itani Lo Sahn - T3 bonus damage increased from +50% to +60%
Baba:
  - [nerf] Baba: Spirit Resistance scaling reduced from 0.7 to 0.5
  - [nerf] Melee: Baba: Melee damage per boon reduced by 10%
  - [nerf] Baba's Brew: Baba: Baba's Brew - Cooldown increased from 27s to 28s
  - [nerf] Baba's Brew: Baba: Baba's Brew - Burn DPS spirit scaling reduced from 0.15 to 0.13
  - [nerf] Baba's Brew: Baba: Baba's Brew - Cycle time increased from 1.5s to 1.6s
  - [nerf] Granny Long Legs: Baba: Granny Long Legs - Melee Resist reduced from 30% to 25%
  - [nerf] Granny Long Legs: Baba: Granny Long Legs - Debuff Resist reduced from 30% to 25%
Celeste:
  - [nerf] Dazzling Trick: Celeste: Dazzling Trick - T3 silence duration reduced from +1.25s to +0.75s
  - [nerf] Radiant Daggers: Celeste: Radiant Daggers - Cast range reduced from 30m to 25m (moved to T2)
  - [neutral] Radiant Daggers: Celeste: Radiant Daggers - Spirit Amp per Stack reduced from +7% to +6% (moved to T3)
  - [nerf] Shining Wonder: Celeste: Shining Wonder - Slow reduced from -32% Movement to -28%
  - [nerf] Shining Wonder: Celeste: Shining Wonder - Cooldown increased from 160s to 170s
  - [nerf] Shining Wonder: Celeste: Shining Wonder - Bounce range reduced from 15.5m to 15m
  - [nerf] Shining Wonder: Celeste: Shining Wonder - T1 move speed slow reduced from -16% to -14%
  - [nerf] Shining Wonder: Celeste: Shining Wonder - T2 bonus damage reduced from +90 to +80
Deadman Danny:
  - [nerf] Close The Deal: Deadman Danny: Close The Deal - Bonus damage to under half health targets reduced from +75% to +55%
  - [nerf] Strix Salvo: Deadman Danny: Strix Salvo - Spirit scaling reduced by 8%
  - [nerf] Chimera Mk1: Deadman Danny: Chimera Mk1 - T2 reduced from 150 Heal On Hit to 125
  - [nerf] Chimera Mk1: Deadman Danny: Chimera Mk1 - T2 heal spirit scaling reduced from 2.0 to 1.7
Mo & Krill:
  - [buff] Scorn: Mo & Krill: Scorn - Heal from heroes increased from 1.2x to 1.3x
  - [buff] Burrow: Mo & Krill: Burrow - Damage radius increased by +0.5m
  - [nerf] Sand Blast: Mo & Krill: Sand Blast - T2 slow from -24% Slow and -26% Dash distance to -28% for both
  - [buff] Combo: Mo & Krill: Combo - Health per kill increased from 40 to 50
Nurse Harrow:
  - [buff] Nurse Harrow: Bullet damage increased by 8%
  - [neutral] Lurking Terrors: Nurse Harrow: Lurking Terrors - Vertical angle increased from 50% to 65%
  - [buff] Lurking Terrors: Nurse Harrow: Lurking Terrors - Fear buildup time reduced from 2s to 1.75s
Rat King:
  - [buff] Rat King: Bullet damage increased from 5.7 to 5.8
  - [buff] Rat King: Ammo increased from 24 to 26
  - [neutral] Scrap Grenade: Rat King: Scrap Grenade - Meleeing the grenade fuse time extension reduced from 0.4s to 0.25s
  - [buff] Rule, Ratannia!: Rat King: Rule, Ratannia! - Move Speed increased from +3m to +4m
  - [rework] Rule, Ratannia!: Rat King: Rule, Ratannia! - T1 now also reduces cooldown by -25s

## Reader corrections (authoritative)

# Reader corrections

Human-authored facts and judgments that override model output. Injected verbatim into
the KB enrichment and the per-hero analysis stage. Keep entries short; date them.

## 2026-09-19

- Infernus: not a pure gun hero. Roughly 50/50 between a gun build (burn synergy) and
  "Dashfernus", a full-spirit dash/mobility build. Both are mainstream, not niche.
- Vindicta: S tier is doubtful. Flyers got hurt this patch: Silver's Weighted Bola now
  grounds/interrupts flyers, and slows now affect air drag. Cross-hero effects like this
  (a buffed anti-air tool on a strong hero) must count against flyers.
- Calico: likely benefits from the tempo meta; re-evaluate upward.
- Haze: rated too high. The Fixation buff is good but T4 gun items are still weak, so
  gun carries that depend on them do not scale as the tier suggests. Compare against
  Venator, who is probably the better pick in that slot.
- General: reason about builds (which items, gun vs spirit, and how popular each build
  actually is) and about how heroes affect each other given who is strong right now,
  not just about a hero's own numbers.

## 2026-09-23

- Haze: not inherently a side-lane farming gun carry. That is how she is played in the
  current patch, but historically she often plays as a roamer/ganker (Smoke Bomb picks,
  Fixation on isolated targets). Her playstyle swings with balance and meta, so frame the
  farm-carry role as meta-dependent, not as her identity.
- Counter items: note the main counter items per archetype where relevant (e.g. Plated
  Armor vs gun carries, Phantom Strike vs flyers/mobile heroes), but remember counters
  have counters (e.g. Armor Piercing Rounds vs Plated Armor). Mention the key ones; do
  not try to list every counter item for every hero.

## 2026-11-03

- The Broker is gone from the game. It was a limited-time feature of City Never Sleeps.
  Never mention it, its 30-minute spawn or its shop as a current mechanic. Corrupted
  items came from the Broker and no longer exist, so never suggest them.
- Apollo (10-30): Riposte's Pommel Hit went from a stun to an immobilize and parry
  disable. That is a rework and a real loss, since it can no longer interrupt channels.
- General: crowd control changing type is never a plain buff, even when its duration rises.

## 2026-11-04

- Steam Vents still grant invisibility. Halloween only added +150% stamina regen on top.
  Never say they lost invisibility.
- General: an added effect is not a replacement. Say something was removed only when the
  notes say so.
- Lines under a "Street Brawl" header apply only to that mode. Never present them as
  main-game changes.
- Tiers come from measured match data, not from the notes. A heavily nerfed hero can still
  be the strongest hero: Baba took big nerfs on 10-30 and still has the top win rate.


## Entries to check

[
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
    "effect": "neutral",
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

## What counts as a mistake

- `change_kind` or `change_size` does not match the hero's own lines. They ignore items and systems. `buff` means clearly stronger, `nerf` clearly weaker, `rework` means an ability works differently, `adjusted` means trade-offs or only fixes.
- A mechanical loss is underplayed. A stun becoming an immobilize can no longer interrupt channels, so it is `bad` and leads the `one_liner`.
- A row's `effect` is backwards for that hero's player: a longer cooldown is `bad`, a shorter one is `good`.
- A row misstates its line, or a gameplay relevant line has no row.
- The `one_liner` contradicts the notes, for example says a cooldown got shorter when it went up, or states a fact with no source.

Report only real mistakes. Most entries are fine, and an empty list is a good answer. Never add a number absent from the notes. When you fix `rows`, return that hero's complete row list.

## Output schema

{
  "fixes": [
    {
      "hero": "exact hero name",
      "issue": "one sentence naming the mistake",
      "change_kind": "buff|nerf|rework|adjusted, or omit",
      "change_size": "minor|moderate|major, or omit",
      "verdict": "keep|watch|bench, or omit",
      "one_liner": "replacement, or omit",
      "rows": [{"label": "1-3 words", "old": "before", "new": "after", "effect": "good|bad|neutral", "ability": "optional"}]
    }
  ]
}
