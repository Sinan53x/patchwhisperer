# Task: verdicts for the reader's hero pool

Patch: Minor Update - 09-16-2026 (2026-09-16)

## Synthesis

{
 "patch_size": "major",
 "size_why": "It deletes a core economy mechanic (flat behind-net-worth bounty souls, 70% rerouted to tick gold for the two poorest) and adds a new one (slows now hit air drag at 35%), plus a gun-cycle/reload rework and a coordinated four-item deletion of a carry build. That is a systems rework, not tuning, despite the 'Minor Update' label and the modest hero numbers.",
 "headline": "The comeback lever is gone: winning lane now wins the game outright, and tempo snowballers own the meta.",
 "meta_thesis": {
  "previous": "Tempo already beat scaling after the 07-30 comeback rework, with early snowballers rising and late scalers and flyers falling while the old overloaded S-tier kits sat mid.",
  "new": "This patch finishes the job: the flat catch-up bounty is removed, so a fed team's lead is sticky instead of printable by one lucky kill, and a new anti-air slow vector clips flyers and airborne poke. Snowballing is now the only reliable win condition, and long-fight steroid/proc builds lose their window.",
  "relationship": "continuation",
  "why": "Every systems lever points the same way as the prior thesis (comeback souls removed, objective bounties up, respawns +3s, tunnel farm delayed, air-drag slows added); the item layer completes the anti-scaler story by gutting Mercurial/Spiritual Overflow and Golden Goose Egg."
 },
 "winners": [
  {
   "hero": "Silver",
   "why": "Weighted Bola now grounds and interrupts flyers (Phantom-Strike rules) plus +3 hp/boon, sprint 1.5->2.5, and the no-pause gun-cycle change directly boosts her high-cycle gun.",
   "indirect": false
  },
  {
   "hero": "Paige",
   "why": "Heavy Melee spirit scaling 0.3->0.45, Captivating Read CDs improved, and her lane-bully/support archetype is the exact snowball the tempo economy rewards.",
   "indirect": false
  },
  {
   "hero": "Billy",
   "why": "Lifestrike heal and slow buffed (48% now drags flyers), Decay/Fortitude buffed — an already-dominant frontline gets sustain plus new anti-air lockdown.",
   "indirect": true
  },
  {
   "hero": "Yamato",
   "why": "More buffs (Crimson Slash heal scaling, Flying Slash 1.0->1.2) stacked on an S-tier mobile assassin in a pick-heavy patch.",
   "indirect": false
  },
  {
   "hero": "Apollo",
   "why": "Absent from the notes but the lane-bully snowball archetype is exactly what the comeback removal and higher objective bounties reward; only his Restorative Locket takes a trim.",
   "indirect": true
  }
 ],
 "losers": [
  {
   "hero": "Warden",
   "why": "A four-way pile-on: Mercurial Magnum 0.49->0.38, Spiritual Overflow triple-nerf, Veil Walker stripped of Sprint Boots, and Plated Armor now blocks his on-hit spirit damage — the proc build is dead.",
   "indirect": false
  },
  {
   "hero": "Celeste",
   "why": "Nerfed seven ways (stamina, Light Eater, Dazzling Trick, Shining Wonder radius/bounces, Dagger T2) while the new 35% air-drag slow punishes her flying kit and the anti-scaling tilt removes her safety net.",
   "indirect": false
  },
  {
   "hero": "Wraith",
   "why": "Card Trick heal and resist-shred cut, Slowing Hex CD up, and Plated Armor now eats Full Auto's on-hit spirit damage — her CC and carry builds both lose a tool.",
   "indirect": false
  },
  {
   "hero": "Viscous",
   "why": "The Cube cast range 26m->20m guts his signature rescue, and Puddle Punch 21s->24s plus damage trims hit his identity; only the Goo Ball buff helps.",
   "indirect": false
  },
  {
   "hero": "Grey Talon",
   "why": "A C-tier poke carry the tempo meta already punishes; the new air-drag slows land on airborne poke and he has no compensation beyond a Hollow Point nudge.",
   "indirect": true
  }
 ],
 "non_obvious_calls": [
  {
   "claim": "The 'general' dash/no-pause gun-cycle and reload-pause changes are functionally a Silver and Abrams buff, not a neutral quality-of-life pass.",
   "why": "Valve's own note says it matters most for high-cycle-time weapons, and Silver separately gets stat buffs; net gun-DPS rises unevenly toward those two.",
   "confidence": 0.7
  },
  {
   "claim": "Golden Goose Egg's 'stored souls count toward net worth' clause is a targeted deletion of the lose-lane-and-bank-while-ignoring-comeback pattern, not a generic econ trim.",
   "why": "It interacts directly with the removed behind-net-worth bounty, so hiding net worth no longer dodges the system the patch just tightened.",
   "confidence": 0.75
  },
  {
   "claim": "The air-drag slow is really an anti-flyer nerf aimed at Celeste, Vindicta, and airborne poke, dressed up as a movement-feel change.",
   "why": "Slows were cut ~20% globally yet gain a 35% air-drag vector, a penalty that only applies to airborne heroes — Celeste is separately hit seven ways.",
   "confidence": 0.7
  },
  {
   "claim": "The invisibility items have quietly swapped roles: Shadow Weave is now the cheap gun-reposition tool and Veil Walker a pick-hero-only buy.",
   "why": "Shadow Weave gains the Sprint Boots component plus sprint/cooldown buffs while Veil Walker loses the component and movespeed-on-break, diverging on the same T3 Vitality path.",
   "confidence": 0.65
  }
 ],
 "uncertainties": [
  "The win/pick snapshot is 14 days and mostly pre-patch, so every WR cited is a baseline, not a post-patch number.",
  "Whether Silver's grounded-interrupt Bola is over-tuned or just right — no post-patch data yet.",
  "Low-confidence hero reads (Seven, Mina, Grey Talon, Graves) rest on archetype direction rather than kit changes.",
  "Whether Plated Armor's on-hit fix actually pulls tank-side buyers toward it or stays a niche counter-pick."
 ],
 "what_to_watch": [
  "Silver's pick/ban rate and WR — the clearest winner; a spike confirms the Bola-plus-stat read.",
  "Warden's pick rate collapse and whether a pure silence-cage utility build survives.",
  "Apollo's post-patch WR to validate the unlisted-lane-bully thesis.",
  "Celeste's WR to confirm the air-drag plus seven-nerf stack.",
  "Golden Goose Egg and Veil Walker pick rates to confirm the item-layer deletions landed."
 ]
}

## Hero analysis entries for the pool heroes

[
 {
  "hero": "Wraith",
  "in_notes": true,
  "direction": "down",
  "magnitude": "moderate",
  "confidence": 0.7,
  "direct_reasons": [
   "Card Trick heart heal 75->60 and its spirit scaling 0.75->0.5 cut her sustain.",
   "Card Trick Diamond resist-shred -8%->-7% (and T3 -5%->-4%) weakens her debuff.",
   "Full Auto spirit damage per bullet 0.03->0.045 is a small compensation."
  ],
  "indirect_reasons": [
   "Plated Armor now blocks Full Auto's on-hit spirit damage \u2014 a direct counter.",
   "Slowing Hex cooldown 27->29s trims her CC-build uptime.",
   "Late-scaler archetype down with comeback souls removed."
  ],
  "build_changes": [
   "De-prioritize Card Trick maxing; lean Full Auto gun build over CC build."
  ],
  "tier_before": "B",
  "tier_after": "C",
  "one_liner": "Card Trick gutted plus Plated Armor counter; Wraith slides out of B."
 },
 {
  "hero": "Warden",
  "in_notes": true,
  "direction": "down",
  "magnitude": "major",
  "confidence": 0.8,
  "direct_reasons": [
   "Bullet damage per boon 0.28->0.25 and fire-rate spirit scaling 0.25->0.21 cut his carry damage.",
   "Alchemical Flask range and speed reduced 30%, gutting his catch/farm.",
   "Willpower T3 spirit scaling +2.7->+2.1 and debuff resist 40%->30% nerf his kit."
  ],
  "indirect_reasons": [
   "Mercurial Magnum scaling 0.49->0.38 and Spiritual Overflow triple-nerf remove his proc build.",
   "Veil Walker stripped (lost Sprint Boots) removes his escape enabler.",
   "Plated Armor now blocks Mercurial on-hit spirit damage, a hard counter.",
   "Late-scaler archetype down with comeback souls removed."
  ],
  "build_changes": [
   "Proc/on-hit Warden (Mercurial + Spiritual Overflow) is dead; pivot to pure silence-cage utility or drop."
  ],
  "tier_before": "B",
  "tier_after": "C",
  "one_liner": "Warden's carry build deleted on all sides \u2014 a four-item pile-on; cage only."
 }
]

## Item analysis entries that mention a pool hero

[
 {
  "item": "Spiritual Overflow",
  "direction": "nerf",
  "magnitude": "major",
  "summary": "35% slower buildup plus spirit power 40->30 and fire rate 30->25% is a triple gut on top of July's cuts \u2014 this is the proc-carry steroid that powered the Warden Mercurial build, and it no longer pays off inside a fight's window.",
  "affected_heroes": [
   {
    "hero": "Warden",
    "relationship": "core",
    "effect": "down",
    "why": "Loses his primary damage steroid on top of Mercurial Magnum and Plated Armor hits \u2014 a three-item pile-on."
   }
  ],
  "build_shift": "With slower buildup, the item wants longer fights the tempo meta no longer provides; effectively removed from the spirit-carry proc build."
 },
 {
  "item": "Veil Walker",
  "direction": "nerf",
  "magnitude": "major",
  "summary": "Losing the Sprint Boots component kills +2 sprint/regen, movespeed now drops when invis ends, and spirit power 10->6 \u2014 the escape-and-reposition package is gutted. It goes from auto-buy to a pick-hero-only tool.",
  "affected_heroes": [
   {
    "hero": "Holliday",
    "relationship": "core",
    "effect": "down",
    "why": "Loses a core enabler just as the tempo meta otherwise favors her pick play."
   },
   {
    "hero": "Warden",
    "relationship": "core",
    "effect": "down",
    "why": "Compounds his Mercurial/Overflow losses \u2014 now stripped on item and hero side."
   }
  ],
  "build_shift": "No longer on the Sprint Boots path, so it competes for a Vitality slot without the mobility subsidy; Shadow Weave now inherits that component."
 },
 {
  "item": "Plated Armor",
  "direction": "buff",
  "magnitude": "moderate",
  "summary": "The fix is a real balance shift, not cosmetic: it now blocks on-hit spirit damage from Mercurial Magnum, Vindicta's Flight, Wraith's Full Auto and Tesla Bullets/Capacitor \u2014 turning a defensive slot into a hard counter to mixed-damage on-hit carries.",
  "affected_heroes": [
   {
    "hero": "Warden",
    "relationship": "situational",
    "effect": "down",
    "why": "Mercurial Magnum on-hit spirit damage is now actually blocked \u2014 third hit to his build this patch."
   },
   {
    "hero": "Wraith",
    "relationship": "situational",
    "effect": "down",
    "why": "Full Auto spirit damage now gets eaten, worsening her already-falling trajectory."
   },
   {
    "hero": "Vindicta",
    "relationship": "situational",
    "effect": "down",
    "why": "Flight on-hit is now counterable by a defensive pick, trimming the tempo winner's tools."
   }
  ],
  "build_shift": "Becomes the defensive answer to on-hit/mixed-damage builds, competing with generic resist slots for tank-side buyers."
 },
 {
  "item": "Slowing Hex",
  "direction": "nerf",
  "magnitude": "minor",
  "summary": "27->29s cooldown trims the pick-engage frequency on near-every-game pick heroes, but the global slow change cuts the other way: its slow now drags flyers out of the air, adding a new anti-air use that partially offsets the CD tax.",
  "affected_heroes": [
   {
    "hero": "Paradox",
    "relationship": "core",
    "effect": "down",
    "why": "Loses some uptime on her cheap pick-enabler on top of her Carbine trim."
   },
   {
    "hero": "Wraith",
    "relationship": "core",
    "effect": "down",
    "why": "CC-build staple gets shorter engage windows during an already-falling patch."
   },
   {
    "hero": "Paige",
    "relationship": "core",
    "effect": "neutral",
    "why": "Loses a little CD but gains the new anti-air slow on the flyers she was buffed to punish."
   }
  ],
  "build_shift": ""
 },
 {
  "item": "Mercurial Magnum",
  "direction": "nerf",
  "magnitude": "major",
  "summary": "Base bullet scaling 0.49->0.38 and base damage 25->20% is a heavy cut \u2014 combined with the Spiritual Overflow nerf and Plated Armor fix, the Mercurial on-hit carry build it anchored is dead in one patch.",
  "affected_heroes": [
   {
    "hero": "Warden",
    "relationship": "core",
    "effect": "down",
    "why": "His signature carry item is gutted, and his two supporting items were hit in the same patch."
   }
  ],
  "build_shift": "No longer a damage engine; the on-hit proc build has no reliable core."
 }
]

## Knowledge base entries for the pool heroes

Wraith:
  name: Wraith
  role: gun carry
  archetypes:
  - gun carry
  - late scaler
  tier: B
  trend: falling
  why: "Nerfed as a scaler (Card Trick heal/resist/slow cut) and punished by Plated\
    \ Armor's on-hit fix, which now blocks Full Auto's spirit damage \u2014 a double\
    \ hit in a tempo meta she doesn't like."
  core_items:
  - Capacitor
  - Slowing Hex
  - Lucky Shot
  build_variants:
  - gun build
  - CC build
  enabled_by:
  - Full Auto scaling buff
  countered_by:
  - Plated Armor
  - tempo nerfs to super-scaling
  last_changed_patch: Minor Update - 09-16-2026
  notes: Well-designed benchmark carry, but the tempo patch strips the safety net
    that let her scale.
Warden:
  name: Warden
  role: gun carry
  archetypes:
  - gun carry
  - late scaler
  tier: B
  trend: falling
  why: Gutted across the board (bullet damage/boon, fire-rate spirit scaling, flask
    range/speed -30%, Willpower T3) and the tempo patch strips his scaling safety
    net; the silence cage keeps him viable, but 55% WR should settle.
  core_items:
  - Veil Walker
  - Mercurial Magnum
  - Spiritual Overflow
  - Fortitude
  build_variants:
  - gun build
  - cage build
  enabled_by:
  - silence cage
  - fast farm
  countered_by:
  - Mercurial/spirit-overflow item nerfs
  - tempo comps
  last_changed_patch: Minor Update - 09-16-2026
  notes: 'Creator: nerfed, not gutted; expect it to settle near balanced rather than
    55% WR.'


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
