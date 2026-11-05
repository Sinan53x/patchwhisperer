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


## Entries to check

[
 {
  "hero": "Mo & Krill",
  "in_notes": true,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.6,
  "direct_reasons": [
   "Scorn heal from heroes 1.2x\u21921.3x and Combo health per kill 40\u219250 both extend his grind-down frontline.",
   "Burrow damage radius +0.5m widens the lockdown hitbox; Sand Blast T2 trades a weaker dash cut (-26%\u2192-28% is a smaller relative reduction) for a stronger slow (-24%\u2192-28%), roughly a wash."
  ],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Small Scorn and Combo buffs plus softer anti-heal make him a slightly better frontline.",
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
    "label": "Sand Blast T2",
    "old": "-24% slow / -26% dash",
    "new": "-28% both",
    "text": null,
    "effect": "neutral",
    "ability": "Sand Blast"
   },
   {
    "label": "Combo HP/kill",
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
  "magnitude": "minor",
  "confidence": 0.55,
  "direct_reasons": [
   "Riposte Pommel Hit now also disarms the target, adding a new trade-winning tool to his lane-bully kit.",
   "Riposte Pummel now ends any preexisting parry on the target, stripping a defensive answer.",
   "Riposte T2 duration +0.6s\u2192+0.7s and Itani Lo Sahn T3 bonus damage +50%\u2192+60%."
  ],
  "tier_before": "S",
  "tier_after": "S",
  "one_liner": "Riposte now disarms and breaks parries \u2014 a sharper lane bully, still S.",
  "verdict": "keep",
  "rows": [
   {
    "label": "Disarm",
    "old": null,
    "new": null,
    "text": "Pommel Hit now disarms",
    "effect": "good",
    "ability": "Riposte"
   },
   {
    "label": "Parry break",
    "old": null,
    "new": null,
    "text": "Pummel ends preexisting parry",
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
  "change_kind": "rework",
  "change_size": "minor"
 },
 {
  "hero": "Celeste",
  "in_notes": true,
  "direction": "down",
  "magnitude": "major",
  "confidence": 0.7,
  "direct_reasons": [
   "Dazzling Trick T3 silence +1.25s\u2192+0.75s cuts her lockdown window.",
   "Radiant Daggers cast range 30m\u219225m and spirit amp +7%\u2192+6% per stack trim her poke and scaling.",
   "Shining Wonder slow -32%\u2192-28%, cooldown 160s\u2192170s, bounce 15.5m\u219215m, T1 -16%\u2192-14%, T2 +90\u2192+80 hit every axis of her ult."
  ],
  "tier_before": "C",
  "tier_after": "D",
  "one_liner": "Every ability got trimmed at once \u2014 silence, range, ult slow and cooldown all down.",
  "verdict": "bench",
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
    "old": "+7%",
    "new": "+6%",
    "text": null,
    "effect": "bad",
    "ability": "Radiant Daggers"
   },
   {
    "label": "Slow",
    "old": "-32%",
    "new": "-28%",
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
    "label": "T1 slow",
    "old": "-16%",
    "new": "-14%",
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
  "change_size": "major"
 },
 {
  "hero": "Rat King",
  "in_notes": true,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.6,
  "direct_reasons": [
   "Rule, Ratannia! T1 now adds -25s cooldown, partly restoring the banner uptime cut on 10-30.",
   "Bullet damage 5.7\u21925.8, ammo 24\u219226 and +3m\u2192+4m move speed are small stat gains.",
   "Scrap Grenade melee fuse extension 0.4s\u21920.25s is a minor loss to his grenade-clear combo."
  ],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Small stat bumps plus a -25s banner cooldown talent restore some ult uptime.",
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
    "text": "Adds -25s cooldown",
    "effect": "good",
    "ability": "Rule, Ratannia!"
   },
   {
    "label": "Fuse extension",
    "old": "0.4s",
    "new": "0.25s",
    "text": null,
    "effect": "bad",
    "ability": "Scrap Grenade"
   }
  ],
  "change_kind": "buff",
  "change_size": "minor"
 },
 {
  "hero": "Baba",
  "in_notes": true,
  "direction": "down",
  "magnitude": "moderate",
  "confidence": 0.65,
  "direct_reasons": [
   "Spirit Resistance scaling 0.7\u21920.5 and melee damage per boon -10% cut her bruiser durability and damage.",
   "Baba's Brew cooldown 27s\u219228s, burn spirit scaling 0.15\u21920.13 and cycle 1.5s\u21921.6s all worsen her core ability.",
   "Granny Long Legs melee resist 30%\u219225% and debuff resist 30%\u219225% thin her frontline shell."
  ],
  "tier_before": "D",
  "tier_after": "D",
  "one_liner": "Resist scaling, melee damage and Brew all trimmed \u2014 the bruiser shell is thinner.",
  "verdict": "watch",
  "rows": [
   {
    "label": "Spirit resist",
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
    "label": "Melee resist",
    "old": "30%",
    "new": "25%",
    "text": null,
    "effect": "bad",
    "ability": "Granny Long Legs"
   },
   {
    "label": "Debuff resist",
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
  "confidence": 0.65,
  "direct_reasons": [
   "Close The Deal bonus damage to under-half targets +75%\u2192+55% cuts his execute.",
   "Strix Salvo spirit scaling -8% lowers his mark damage.",
   "Chimera Mk1 T2 heal 150\u2192125 and heal spirit scaling 2.0\u21921.7 trim his dive sustain."
  ],
  "tier_before": "C",
  "tier_after": "C",
  "one_liner": "Execute and mark damage both cut \u2014 his dive converts fewer kills.",
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
    "label": "T2 heal scaling",
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
   "Bullet damage +8% lifts the gun-damage charge economy her sustain build runs on.",
   "Lurking Terrors fear buildup 2s\u21921.75s and vertical angle 50%\u219265% widen and speed the fear cone."
  ],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Gun damage up and a faster, wider fear cone \u2014 small but real gains.",
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
