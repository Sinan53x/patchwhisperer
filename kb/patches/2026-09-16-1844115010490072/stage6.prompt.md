# Task: update the knowledge base after this patch

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

## Hero analysis (movers only)

[
 {
  "hero": "Seven",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [],
  "indirect_reasons": [
   "Hollow Point resist-shred 9->10% buffs his core T2 gun slot.",
   "Gun-carry archetype up from the dash/no-pause gun-cycle change.",
   "Tunnel breakables delayed 3m->5m slow his early solo farm."
  ],
  "build_changes": [],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Early-gun shred buff lands, but delayed tunnel farm and tempo divers still cap him."
 },
 {
  "hero": "Vindicta",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.6,
  "direct_reasons": [],
  "indirect_reasons": [
   "Hollow Point resist-shred buff hits her core first-gun slot.",
   "Tempo economy (comeback souls cut) suits her early-lead playstyle.",
   "Poke/siege archetype down via air-drag slows, a soft offset."
  ],
  "build_changes": [],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Tempo patch keeps Vindicta in A; the shred buff makes her lane pick stronger."
 },
 {
  "hero": "Lady Geist",
  "in_notes": true,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.7,
  "direct_reasons": [
   "Life Drain T3 spirit scaling +0.3->+0.45 boosts her ult heal/drain.",
   "Essence Bomb T3 damage +26%->30% raises her burst.",
   "Decay DPS down/duration up suits her sustained-brawl anti-heal slot."
  ],
  "indirect_reasons": [
   "Spirit-carry archetype down from removed comeback/Rift levers."
  ],
  "build_changes": [],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Direct buffs on an already-rising pick; she stays a top spirit bruiser."
 },
 {
  "hero": "Abrams",
  "in_notes": true,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.6,
  "direct_reasons": [
   "Infernal Resilience T3 heal +8%->+9% is a small sustain bump.",
   "Seismic Impact T3 Unstoppable 6s->5s is a real ult-window nerf."
  ],
  "indirect_reasons": [
   "Dash/melee no longer pausing gun cycle lets him weave shots between punches.",
   "Fortitude and Decay both buffed, his core brawler items."
  ],
  "build_changes": [],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Tiny numbers up, gun-cycle smoothing helps, but anti-heal meta keeps him B."
 },
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
  "hero": "Paradox",
  "in_notes": true,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.65,
  "direct_reasons": [
   "Kinetic Carbine min damage multiplier 25%->10% cuts her quick-scope poke.",
   "Carbine min multiplier no longer increased by T3, removing a poke-scaling path."
  ],
  "indirect_reasons": [
   "Slowing Hex cooldown 27->29s trims her pick-engage frequency.",
   "Global slow -20% reduces lockdown, offset by new anti-air on Slowing Hex."
  ],
  "build_changes": [
   "Lean on Echo Shard bomb over Carbine poke."
  ],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Carbine poke trimmed; still a strong bomb-pick initiator, just less oppressive."
 },
 {
  "hero": "Dynamo",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.6,
  "direct_reasons": [],
  "indirect_reasons": [
   "Diviner's Kevlar now grants +10% ultimate CDR, a core item for his ult build.",
   "Tempo meta converts won lanes into picks, his win condition."
  ],
  "build_changes": [
   "Diviner's Kevlar is now a stronger buy for faster ult cycles."
  ],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Ult-initiator gets a Kevlar CDR bump on top of a meta that loves his picks."
 },
 {
  "hero": "Haze",
  "in_notes": true,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.65,
  "direct_reasons": [
   "Fixation headshot stacks +2->+3 raises her stacking damage.",
   "Fixation T3 weapon scaling 0.0003->0.00035 adds late gun scaling."
  ],
  "indirect_reasons": [
   "Gun-carry archetype up from the gun-cycle/reload changes.",
   "Plated Armor's on-hit fix is a soft counter to her on-hit builds."
  ],
  "build_changes": [
   "Gun Haze with Fixation maxing is clearly the build over Echo Shard sleep."
  ],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Fixation buffs make gun Haze the play in a tempo meta she likes."
 },
 {
  "hero": "Holliday",
  "in_notes": true,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.6,
  "direct_reasons": [
   "Health per boon 41->43 adds lane durability.",
   "Crackshot T2 now applies -6% bullet resist for 5s, real pick damage.",
   "Bounce Pad lasso extension +1s->+1.25s improves her catch."
  ],
  "indirect_reasons": [
   "Veil Walker nerf removes a core enabler (Sprint Boots component lost).",
   "Tempo economy rewards her post-20 pick play."
  ],
  "build_changes": [
   "Consider a gun-hybrid Crackshot build; Veil Walker is now a worse slot."
  ],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Direct buffs and tempo favor her, but the Veil Walker strip bites."
 },
 {
  "hero": "Calico",
  "in_notes": false,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [],
  "indirect_reasons": [
   "Tunnel breakables spawn/respawn 3m->5m delays her early underground farm.",
   "Mobile-assassin archetype up but her power is early-farm dependent."
  ],
  "build_changes": [],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Breakable timing pushes back her early farm; a quiet nerf to a ~50% skirmisher."
 },
 {
  "hero": "Grey Talon",
  "in_notes": false,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.4,
  "direct_reasons": [],
  "indirect_reasons": [
   "Hollow Point shred buff helps his core slot.",
   "Poke/siege archetype down via new air-drag slows on flyers/airborne poke.",
   "47.7% WR pre-patch with no compensation."
  ],
  "build_changes": [],
  "tier_before": "C",
  "tier_after": "C",
  "one_liner": "Item buff can't fix a C-tier poke carry the tempo meta punishes."
 },
 {
  "hero": "Mo & Krill",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.55,
  "direct_reasons": [],
  "indirect_reasons": [
   "Fortitude regen buff and Decay duration buff hit his core frontline items.",
   "Tank/frontline and early-brawl archetype favored by the tempo shift."
  ],
  "build_changes": [],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Quietly winning tank gets small item help in a meta that rewards minute-one brawls."
 },
 {
  "hero": "Shiv",
  "in_notes": true,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.65,
  "direct_reasons": [
   "Alt fire base damage +4% and per-boon +0.2->+0.24 boost his sustained shred.",
   "Serrated Knives at full rage now deals 3.5% current HP on impact instead of ricocheting."
  ],
  "indirect_reasons": [
   "Tankbuster current-HP 8%->7.5% is a small trim to his anti-tank slot.",
   "Fortitude regen buff helps his bruiser builds."
  ],
  "build_changes": [],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Current-HP knives plus alt-fire buffs keep Shiv shredding the HP pools the patch inflates."
 },
 {
  "hero": "Ivy",
  "in_notes": true,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.6,
  "direct_reasons": [
   "Stone Form radius 6m->5.75m and T1 heal 7%->6% trim her survivability tool."
  ],
  "indirect_reasons": [
   "Support archetype neutral; no item economy lever against her."
  ],
  "build_changes": [],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Small Stone Form nerf won't move the support queen off the top slot."
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
 },
 {
  "hero": "Yamato",
  "in_notes": true,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.7,
  "direct_reasons": [
   "Crimson Slash T3 now adds +0.4 heal spirit scaling.",
   "Flying Slash light-melee scaling 1.0->1.2 raises her burst."
  ],
  "indirect_reasons": [
   "Tankbuster 8%->7.5% is a small trim on her anti-tank slot.",
   "Mobile-assassin and tempo archetypes up."
  ],
  "build_changes": [],
  "tier_before": "S",
  "tier_after": "S",
  "one_liner": "More buffs atop an S-tier pick; expect her pick rate to climb further."
 },
 {
  "hero": "Viscous",
  "in_notes": true,
  "direction": "down",
  "magnitude": "moderate",
  "confidence": 0.7,
  "direct_reasons": [
   "The Cube cast range 26m->20m badly weakens his signature rescue.",
   "Puddle Punch cooldown 21s->24s cuts his dueling frequency.",
   "Alt fire damage growth -10% and Splatter T1 +2m->+1.5m trim his damage.",
   "Splatter detonation cooldown 0.15->0.12 and Goo Ball T3 +0.2 spirit scaling are partial offsets."
  ],
  "indirect_reasons": [
   "Tank/enabler archetype roughly neutral in the tempo shift."
  ],
  "build_changes": [],
  "tier_before": "B",
  "tier_after": "C",
  "one_liner": "Cube range and Puddle Punch nerfs hit his identity; only the ball buff helps."
 },
 {
  "hero": "Pocket",
  "in_notes": false,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [],
  "indirect_reasons": [
   "Spirit-carry and burst-caster archetypes down/neutral in the tempo shift.",
   "Fortitude regen buff is his only item-side help; 45.8% WR pre-patch."
  ],
  "build_changes": [],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Cloak assassin still wants long fights the tempo meta doesn't allow."
 },
 {
  "hero": "Vyper",
  "in_notes": true,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.6,
  "direct_reasons": [
   "Slither T3 barrier duration 5s->4s trims her defensive window.",
   "Petrifying Bola cooldown 105s->115s raises her ult timer."
  ],
  "indirect_reasons": [
   "Hollow Point shred buff helps her core gun slot.",
   "Gun-carry archetype up; still coin-flip on enemy CC."
  ],
  "build_changes": [],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Two small nerfs, one item buff; still the top-WR coin-flip carry."
 },
 {
  "hero": "Mina",
  "in_notes": false,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.45,
  "direct_reasons": [],
  "indirect_reasons": [
   "Mobile-assassin archetype up, but she has no kit change to convert it.",
   "45.2% WR on 41.6% pick rate pre-patch, falling."
  ],
  "build_changes": [],
  "tier_before": "C",
  "tier_after": "C",
  "one_liner": "No changes given to a falling assassin; still needs a rework."
 },
 {
  "hero": "Drifter",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.55,
  "direct_reasons": [],
  "indirect_reasons": [
   "Toxic Bullets scaling buff and Decay duration buff hit his core anti-heal items.",
   "Fortitude regen buff helps his melee-bruiser brawls.",
   "Melee/bruiser archetype favored by the tempo shift."
  ],
  "build_changes": [],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Blind-pickable bruiser gets item tailwinds in a brawl-friendly patch."
 },
 {
  "hero": "Venator",
  "in_notes": true,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.6,
  "direct_reasons": [
   "Ira Domini now works with Ricochet (all shots bounce) and Split Shot (3 bolts) \u2014 real late damage.",
   "Weakening Headshot shred -13%->-12% trims his core item slightly."
  ],
  "indirect_reasons": [
   "Hollow Point shred buff helps his first-gun slot.",
   "Tempo meta and his 44.7% WR still work against his 'no weak point' read."
  ],
  "build_changes": [
   "Ricochet/Split Shot ult builds are now live; keep Weakening Headshot despite the trim."
  ],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Ult gains ricochet and split shot, but the data still says he doesn't convert."
 },
 {
  "hero": "Paige",
  "in_notes": true,
  "direction": "up",
  "magnitude": "major",
  "confidence": 0.75,
  "direct_reasons": [
   "Heavy Melee spirit scaling 0.3->0.45 is a large damage buff.",
   "Captivating Read T1 cooldown -11s->-14s and T3 +1m->+2m improve her engage.",
   "Rallying Charge collision fix removes clunk."
  ],
  "indirect_reasons": [
   "Restorative Locket heal/boon 0.5->0.45 and range 35->32m trims her sustain item.",
   "Slowing Hex cd 27->29s is a small tax, offset by new anti-air slow on flyers.",
   "Lane-bully/support archetypes up; tempo meta rewards her lane win."
  ],
  "build_changes": [
   "Keep Slowing Hex \u2014 its anti-air slow now punishes flyers she was buffed to beat."
  ],
  "tier_before": "S",
  "tier_after": "S",
  "one_liner": "Buff-stacked lane-winning support; still the patch's clearest S-tier winner."
 },
 {
  "hero": "Billy",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.6,
  "direct_reasons": [],
  "indirect_reasons": [
   "Lifestrike melee heal 100+1.5->120+1.75 and 30%->35% is effectively a Billy buff.",
   "Lifestrike's 48% slow now drags flyers out of the air, new anti-air CC.",
   "Decay duration buff and Fortitude regen buff hit his frontline items."
  ],
  "build_changes": [
   "Lifestrike now doubles as anti-air lockdown; value it over pure healing slots."
  ],
  "tier_before": "S",
  "tier_after": "S",
  "one_liner": "Lifestrike buff + new anti-air slow feed an already-dominant frontline."
 },
 {
  "hero": "Graves",
  "in_notes": true,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [
   "Health per boon 33->35 adds early durability."
  ],
  "indirect_reasons": [
   "Toxic Bullets scaling buff and Fortitude regen buff help her item path.",
   "Gun-carry archetype up, but her 56.7% snapshot WR is a lagging pre-patch read."
  ],
  "build_changes": [],
  "tier_before": "C",
  "tier_after": "C",
  "one_liner": "Small health/boon plus item buffs, but her awful base stats still cap her."
 },
 {
  "hero": "Apollo",
  "in_notes": false,
  "direction": "up",
  "magnitude": "moderate",
  "confidence": 0.65,
  "direct_reasons": [],
  "indirect_reasons": [
   "Restorative Locket heal/boon 0.5->0.45 and range 35->32m nerfs his sustain item.",
   "Tempo economy (comeback souls cut, objectives up) is exactly his lane-bully snowball playstyle.",
   "Initiator/lane-bully archetypes up in the tempo shift."
  ],
  "build_changes": [],
  "tier_before": "S",
  "tier_after": "S",
  "one_liner": "Absent from notes but the archetype winner; only his Locket slot takes a trim."
 },
 {
  "hero": "Silver",
  "in_notes": true,
  "direction": "up",
  "magnitude": "major",
  "confidence": 0.8,
  "direct_reasons": [
   "Health per boon 28->31 and sprint speed 1.5->2.5 are big stat buffs.",
   "Weighted Bola now increases gravity and interrupts flying abilities (Phantom-Strike rules) \u2014 a new pick tool.",
   "Dashes/light melee no longer pause gun cycle, directly boosting her high-cycle gun.",
   "Boot Kick and Entangling Bola now only target heroes/objectives, removing wasted hits."
  ],
  "indirect_reasons": [
   "Hollow Point shred buff and Fortitude regen buff hit her core slots.",
   "Diviner's Kevlar +10% ult CDR helps her existing buy.",
   "Gun-carry and tank archetypes both up."
  ],
  "build_changes": [
   "Weighted Bola is now a core grounded-interrupt pick; build around gun-tank with Diviner's Kevlar."
  ],
  "tier_before": "S",
  "tier_after": "S",
  "one_liner": "The patch's biggest winner headlined by a Phantom-Strike-style grounded Bola."
 },
 {
  "hero": "Celeste",
  "in_notes": true,
  "direction": "down",
  "magnitude": "major",
  "confidence": 0.8,
  "direct_reasons": [
   "Stamina cooldown 5->5.3, Light Eater spirit lifesteal 20%->18%, Dazzling Trick cd 34s->38s.",
   "Shining Wonder radius 16.5m->15.5m, T3 bounces +8->+6, Radiant Daggers T2 +80->+70, Light Eater T3 +25->+22."
  ],
  "indirect_reasons": [
   "Slows now affect air drag by 35%, punishing her flying kit.",
   "Spirit-carry archetype down with comeback/Rift levers removed.",
   "Paige's rise and the anti-scaling tilt squeeze her slot."
  ],
  "build_changes": [],
  "tier_before": "A",
  "tier_after": "B",
  "one_liner": "Nerfed seven ways plus air-drag slows on a flyer; drops out of A."
 }
]

## Item analysis

{
 "items": [
  {
   "item": "Weakening Headshot",
   "direction": "nerf",
   "magnitude": "minor",
   "summary": "A -13%->-12% shred trim is cosmetic on its own, but it lands on Venator whose whole identity is 'no weak point' — removing a point of resist-shred slightly narrows his already-struggling tempo conversion (45.7% WR).",
   "affected_heroes": [
    {
     "hero": "Venator",
     "relationship": "core",
     "effect": "down",
     "why": "His core resist-shred item got a point weaker, piling onto a WR that already hasn't matched his reputation."
    }
   ],
   "build_shift": ""
  },
  {
   "item": "Hollow Point",
   "direction": "buff",
   "magnitude": "minor",
   "summary": "9->10% resist-shred is a small number but it's on the cheap T2 early-gun item, exactly where the tempo patch wants damage online. Reinforces the win-lane-harder path rather than the super-scaling one.",
   "affected_heroes": [
    {
     "hero": "Vindicta",
     "relationship": "core",
     "effect": "up",
     "why": "Tempo early-gun carry whose T2 shred got stronger in the meta that already favors her."
    },
    {
     "hero": "Seven",
     "relationship": "core",
     "effect": "up",
     "why": "Loves the early shred but still draft-dependent and pace-sensitive."
    },
    {
     "hero": "Vyper",
     "relationship": "core",
     "effect": "up",
     "why": "Top-WR gun carry gets a small boost to her lane-dominant opening."
    },
    {
     "hero": "Silver",
     "relationship": "core",
     "effect": "up",
     "why": "The patch's biggest winner also buys the buffed early-gun shred."
    },
    {
     "hero": "Venator",
     "relationship": "core",
     "effect": "neutral",
     "why": "Compensates the small Weakening Headshot nerf but doesn't fix his conversion problem."
    },
    {
     "hero": "Grey Talon",
     "relationship": "core",
     "effect": "neutral",
     "why": "C-tier poke carry that still can't convert the early lead the item wants to create."
    }
   ],
   "build_shift": "Solidifies cheap T2 weapon shred as the default first-gun slot in the tempo meta."
  },
  {
   "item": "Toxic Bullets",
   "direction": "buff",
   "magnitude": "minor",
   "summary": "Spirit scaling 0.005->0.006% is a nudge, but anti-heal DoT gains value as the patch funnels fights into inflated-HP bruisers and tanks; it's one of the few clean answers to big health pools.",
   "affected_heroes": [
    {
     "hero": "Infernus",
     "relationship": "core",
     "effect": "up",
     "why": "Burn carry whose scaling gets a hair better; still out-paced by the tempo meta."
    },
    {
     "hero": "Drifter",
     "relationship": "core",
     "effect": "up",
     "why": "Blind-pickable bruiser with built-in anti-heal stacks another anti-heal DoT."
    },
    {
     "hero": "Graves",
     "relationship": "core",
     "effect": "neutral",
     "why": "Gets the buff but her core problem is base stats, not this item."
    }
   ],
   "build_shift": ""
  },
  {
   "item": "Shadow Weave",
   "direction": "buff",
   "magnitude": "moderate",
   "summary": "Now builds from Sprint Boots, sprint 1.5->2 and cooldown 45->37s — cheaper, faster, more uptime invis. Despite creators still calling it poor, the path change lowers the entry cost for gun carries who want a repositioning tool in a pick-heavy meta.",
   "affected_heroes": [],
   "build_shift": "Gains the Sprint Boots component while Veil Walker loses it — the two invis items now diverge on the same tier-3 Vitality path, and this is the cheaper of the two."
  },
  {
   "item": "Cultist Sacrifice",
   "direction": "nerf",
   "magnitude": "minor",
   "summary": "180->170% bounty is a small number but it stacks with the whole patch's anti-greed direction: econ items are worse when comeback souls are gone and tempo wins games, so a soul-printing buy is now a tempo tax.",
   "affected_heroes": [],
   "build_shift": ""
  },
  {
   "item": "Ballistic Enchantment",
   "direction": "buff",
   "magnitude": "minor",
   "summary": "14->20s duration is a real uptime gain on a niche spirit utility item, but with no clear user base in the KB this stays a fringe pickup. Low confidence on who it helps.",
   "affected_heroes": [],
   "build_shift": ""
  },
  {
   "item": "Spiritual Overflow",
   "direction": "nerf",
   "magnitude": "major",
   "summary": "35% slower buildup plus spirit power 40->30 and fire rate 30->25% is a triple gut on top of July's cuts — this is the proc-carry steroid that powered the Warden Mercurial build, and it no longer pays off inside a fight's window.",
   "affected_heroes": [
    {
     "hero": "Warden",
     "relationship": "core",
     "effect": "down",
     "why": "Loses his primary damage steroid on top of Mercurial Magnum and Plated Armor hits — a three-item pile-on."
    }
   ],
   "build_shift": "With slower buildup, the item wants longer fights the tempo meta no longer provides; effectively removed from the spirit-carry proc build."
  },
  {
   "item": "Restorative Locket",
   "direction": "nerf",
   "magnitude": "minor",
   "summary": "Heal per boon 0.5->0.45 and stack range 35->32m trims both throughput and uptime; on a tempo support it's a soft power cut stacked on 08-22's resist nerf.",
   "affected_heroes": [
    {
     "hero": "Apollo",
     "relationship": "core",
     "effect": "down",
     "why": "The patch's archetype winner takes a small item-side offset to his lane-bully sustain."
    }
   ],
   "build_shift": ""
  },
  {
   "item": "Trophy Collector",
   "direction": "nerf",
   "magnitude": "minor",
   "summary": "Souls/min 18->16 is another piece of the item-side economy tightening — pure-farm econ buys lose value in the same patch that delayed tunnel breakables and cut comeback souls.",
   "affected_heroes": [],
   "build_shift": ""
  },
  {
   "item": "Veil Walker",
   "direction": "nerf",
   "magnitude": "major",
   "summary": "Losing the Sprint Boots component kills +2 sprint/regen, movespeed now drops when invis ends, and spirit power 10->6 — the escape-and-reposition package is gutted. It goes from auto-buy to a pick-hero-only tool.",
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
     "why": "Compounds his Mercurial/Overflow losses — now stripped on item and hero side."
    }
   ],
   "build_shift": "No longer on the Sprint Boots path, so it competes for a Vitality slot without the mobility subsidy; Shadow Weave now inherits that component."
  },
  {
   "item": "Fortitude",
   "direction": "buff",
   "magnitude": "minor",
   "summary": "2->2.25% max-health regen is a rounding-level buff, but it's on the default survivability slot for nearly every bruiser and tank, and the patch's slower respawn/longer-fight direction makes sustained regen more valuable than burst.",
   "affected_heroes": [
    {
     "hero": "Abrams",
     "relationship": "core",
     "effect": "up",
     "why": "Bruiser already helped by the gun-cycle change; slight extra regen keeps him brawling."
    },
    {
     "hero": "Mo & Krill",
     "relationship": "core",
     "effect": "up",
     "why": "Tank that lives in minute-one brawls the patch rewards."
    },
    {
     "hero": "Lycan-style bruisers (Seven, Infernus, Shiv, Silver)",
     "relationship": "core",
     "effect": "up",
     "why": "Near-universal slot — anyone on Fortitude gets a tiny durability tax cut in longer fights."
    }
   ],
   "build_shift": ""
  },
  {
   "item": "Lifestrike",
   "direction": "buff",
   "magnitude": "moderate",
   "summary": "Melee heal 100+1.5->120+1.75 and 30->35% is a real sustain gain, but the bigger story is synergy: with slows now affecting air drag, its 48% slow becomes a genuine anti-air lockdown, so it reads as a CC item as much as a heal.",
   "affected_heroes": [
    {
     "hero": "Billy",
     "relationship": "core",
     "effect": "up",
     "why": "Effectively a Billy item — the heal buff plus new anti-air slow feeds his already-dominant S-tier frontline."
    }
   ],
   "build_shift": "Upgrades from a melee-sustain slot to a CC/anti-air option in the same patch slows gained air-drag effect."
  },
  {
   "item": "Leech",
   "direction": "buff",
   "magnitude": "minor",
   "summary": "25->28% bullet+spirit lifesteal raises ceiling but the KB still calls it weak, and in a tempo meta that ends fights fast there's little window to lifesteal back — the buff doesn't address why nobody buys it.",
   "affected_heroes": [],
   "build_shift": ""
  },
  {
   "item": "Plated Armor",
   "direction": "buff",
   "magnitude": "moderate",
   "summary": "The fix is a real balance shift, not cosmetic: it now blocks on-hit spirit damage from Mercurial Magnum, Vindicta's Flight, Wraith's Full Auto and Tesla Bullets/Capacitor — turning a defensive slot into a hard counter to mixed-damage on-hit carries.",
   "affected_heroes": [
    {
     "hero": "Warden",
     "relationship": "situational",
     "effect": "down",
     "why": "Mercurial Magnum on-hit spirit damage is now actually blocked — third hit to his build this patch."
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
   "item": "Diviner's Kevlar",
   "direction": "rework",
   "magnitude": "moderate",
   "summary": "Adding +10% ultimate CDR pushes it from a generic defense item into a coordination/initiation enabler — it now wants heroes whose win condition is a big ult on a clock.",
   "affected_heroes": [
    {
     "hero": "Dynamo",
     "relationship": "core",
     "effect": "up",
     "why": "Ult-initiator whose whole value is the AoE-CC ult; CDR makes his threat cycle faster."
    },
    {
     "hero": "Silver",
     "relationship": "core",
     "effect": "up",
     "why": "Tank-carry that already buys it, now with better ult uptime on top of her other buffs."
    }
   ],
   "build_shift": "Slot stays Vitality, but the item's identity tilts from survivability toward ult-uptime — direct competition with pure CDR items."
  },
  {
   "item": "Golden Goose Egg",
   "direction": "nerf",
   "magnitude": "major",
   "summary": "Damage penalty -10->-15%, souls/min 90->80, and stored souls now count toward net worth — the last clause is the killer: it interacts directly with the patch's comeback change and removes the item's whole point of hiding net worth from bounty math.",
   "affected_heroes": [],
   "build_shift": "Effectively unbuyable — the patch's worst item, and the clause tying stored souls to net worth is a targeted deletion of the 'lose lane, bank souls, ignore come back' pattern."
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
   "item": "Radiant Regeneration",
   "direction": "nerf",
   "magnitude": "minor",
   "summary": "Per-boon scaling 2->1.7 caps out less late; it's the second cut in two patches to a healing-support item, softly taxing sustain supports without removing the slot.",
   "affected_heroes": [
    {
     "hero": "Kelvin",
     "relationship": "core",
     "effect": "down",
     "why": "Healer whose item path is being progressively trimmed on top of 08-22's nerf."
    }
   ],
   "build_shift": ""
  },
  {
   "item": "Tankbuster",
   "direction": "nerf",
   "magnitude": "minor",
   "summary": "8->7.5% current-health bonus is a nudge, but stacked on 07-28 (no longer procs off items) it's a cumulative trim to the anti-tank slot just as the patch funnels big HP pools into fights.",
   "affected_heroes": [
    {
     "hero": "Shiv",
     "relationship": "core",
     "effect": "down",
     "why": "Anti-tank bruiser loses a hair of his shred, though his current-HP knives carry the identity."
    },
    {
     "hero": "Yamato",
     "relationship": "core",
     "effect": "down",
     "why": "Small trim on a slot she relies on for the burst that the tempo meta rewards."
    }
   ],
   "build_shift": ""
  },
  {
   "item": "Decay",
   "direction": "neutral",
   "magnitude": "minor",
   "summary": "DPS -25% but duration +20% trades burst healing-cut for sustained anti-heal — worse at clipping a single big burst-heal window, better at keeping tanks suppressed over a long brawl, which fits the patch's longer fights.",
   "affected_heroes": [
    {
     "hero": "Abrams",
     "relationship": "core",
     "effect": "up",
     "why": "Anti-heal identity on a tank who lives in sustained brawls the duration buff suits."
    },
    {
     "hero": "Billy",
     "relationship": "core",
     "effect": "up",
     "why": "Frontline brawler who wants sustained suppression over long fights."
    },
    {
     "hero": "Mo & Krill",
     "relationship": "core",
     "effect": "up",
     "why": "Tank-friendly slot on a hero that brawls from minute one."
    },
    {
     "hero": "Infernus",
     "relationship": "core",
     "effect": "neutral",
     "why": "Anti-heal user whose burn carries; shape of the item shift is roughly a wash for him."
    },
    {
     "hero": "Lady Geist",
     "relationship": "core",
     "effect": "neutral",
     "why": "Rising scaler who buys it mostly as a defensive anti-heal tool."
    }
   ],
   "build_shift": "Still the go-to anti-heal slot; the DPS/duration swap slightly favors sustained-fight buyers over pick-window users."
  },
  {
   "item": "Mercurial Magnum",
   "direction": "nerf",
   "magnitude": "major",
   "summary": "Base bullet scaling 0.49->0.38 and base damage 25->20% is a heavy cut — combined with the Spiritual Overflow nerf and Plated Armor fix, the Mercurial on-hit carry build it anchored is dead in one patch.",
   "affected_heroes": [
    {
     "hero": "Warden",
     "relationship": "core",
     "effect": "down",
     "why": "His signature carry item is gutted, and his two supporting items were hit in the same patch."
    }
   ],
   "build_shift": "No longer a damage engine; the on-hit proc build has no reliable core."
  },
  {
   "item": "Focus Lens",
   "direction": "buff",
   "magnitude": "minor",
   "summary": "30->35% damage and cast range 20->25m make it a stronger spirit-amp option, but it's still cleansable, so the buff mostly helps clean engages rather than dominating. Low-confidence read — no KB user listed.",
   "affected_heroes": [],
   "build_shift": "Better range makes it a more viable opener for burst casters on cleansable targets."
  }
 ],
 "notable_item_stories": [
  "Three econ items (Cultist Sacrifice, Trophy Collector, Golden Goose Egg) get trimmed at once — the item-side echo of the patch's anti-comeback economy, with Golden Goose Egg's net-worth clause specifically deleting the bank-and-hide pattern.",
  "The Mercurial Magnum + Spiritual Overflow nerfs plus Plated Armor's on-hit fix form one coordinated stack that removes Warden's carry build in a single patch.",
  "Invisibility items diverge around Sprint Boots: Shadow Weave gains the component plus a buff while Veil Walker loses it and gets stripped, so expect cheap gun-invis to rise and the pick-hero invis to fall."
 ]
}

## Current meta.md

# Meta state
Last patch: Minor Update - 09-16-2026 (2026-09-16)

## Thesis
The 09-16 patch finished what the 07-30 comeback rework started: it gutted comeback souls and early Unstable Rift generosity, so winning lane now actually wins the game. Tempo beats scaling. Early snowballers and mobile bruisers (Paige, Apollo, Silver, Yamato, Vindicta, Holliday, Lash, Haze) rise; late scalers and flyers (Celeste, Warden, Wraith) fall. The old "overloaded DLC" S-tiers (Mirage, Venator, Doorman, Pocket) keep their kits but sit at ~46% WR — the meta stopped rewarding them.

## Economy and systems
Comeback bounty trimmed and extra comeback souls partly rerouted to the two lowest-econ players via tick gold, killing the fed AFK farmer. Guardian bounty +10%, Walker +5%, objective share 30->25%. Rift resist is now 10% +1%/min (cap 40% at 30m) instead of a flat 35% — early rift fights are real fights. Respawn at 20m 35->38s. Stuns/parry pause reload instead of resetting; dashes and light melee no longer break gun cycle time (Silver/Abrams smoothing); slows -20% globally but now hit air drag at 35% (flyers down, slow-as-CC up).

## Archetype standing
Early tempo and mobile frontline lead; late scalers lose their safety net. Tanks stay fine (Abrams/Dynamo/Mo) — core tank items untouched. Supports hold value (Ivy 53.7%, Paige rising) but healing items were trimmed (Radiant Regeneration, Restorative Locket).

## Watchlist
- Silver: Weighted Bola acts as Phantom Strike, plus +health/+sprint and the gun-cycle change. Biggest winner.
- Apollo: absent from notes, best snowballer — "super buffed" by tempo.
- Celeste: 7 nerfs plus item/scaling/air-drag hits; her 54.6% WR is a lagging pre-patch number.
- Veil Walker buyers (Holliday, Warden): item lost Sprint Boots and movespeed-on-break.

## Recent history
07-30 added Ranked Mode. 07-09/07-28 item and hero tuning; 08-12 McGinnis/Apollo; 08-22 Celeste; 09-16 tempo patch. The 07-16 creator read framed the game as a stat-check with S-tier DLC kits; current data (those kits mid at high rank) and the tempo patch are the newer, authoritative state. Snapshot is 14 days and mostly pre-patch, so treat its WRs as baseline, not post-patch.

## Current hero entries (movers only)

Seven:
  name: Seven
  role: gun carry
  archetypes:
  - gun carry
  - late scaler
  tier: B
  trend: stable
  why: "Fast-clearing solo-queue carry that is draft-dependent \u2014 good when a\
    \ tank makes space, weak into the early tempo invaders this patch encourages."
  core_items:
  - Hollow Point
  - Burst Fire
  - Titanic Magazine
  - Fortitude
  build_variants:
  - gun build
  enabled_by:
  - Hollow Point resist-shred buff
  - fast jungle clear
  countered_by:
  - early tempo invaders
  - CC-lock drafts
  last_changed_patch: Minor Update - 08-12-2026
  notes: 'Creator consensus: strongest in low elo, unremarkable at the very top.'
Vindicta:
  name: Vindicta
  role: poke/siege carry
  archetypes:
  - poke/siege
  - gun carry
  tier: A
  trend: rising
  why: 'Tempo patch winner: as a high-tempo early gun carry she profits from super-scaling
    being trimmed and from picks mattering more after 20m; only damage was nudged
    down earlier (Stake T1).'
  core_items:
  - Hollow Point
  - High-Velocity Rounds
  - Long Range
  build_variants:
  - poke build
  - gun build
  enabled_by:
  - tempo economy
  - increased respawn timer
  countered_by:
  - dive/CC comps
  - flyer counters
  last_changed_patch: Minor Update - 08-12-2026
  notes: "heresy lists a ricochet/split-shot ult buff, which the 09-16 notes actually\
    \ attribute to Venator \u2014 treat the exact owner as uncertain."
Lady Geist:
  name: Lady Geist
  role: spirit bruiser
  archetypes:
  - spirit carry
  - tank/frontline
  - late scaler
  tier: A
  trend: rising
  why: Directly buffed (Life Drain T3 spirit scaling up, Essence Bomb T3 +4%) and
    rises mostly because her scaler peers were nerfed; still a tanky hero with a fight-winning
    ult despite a soft 46.5% WR.
  core_items:
  - Boundless Spirit
  - Fortitude
  - Decay
  - Mystic Reverb
  build_variants:
  - spirit ult build
  - tank build
  enabled_by:
  - 09-16 ability buffs
  - peers nerfed
  countered_by:
  - anti-heal
  - burst before ult
  last_changed_patch: Minor Update - 09-16-2026
  notes: Snapshot WR is low but pre-patch; creator read is A-tier classic pick.
Abrams:
  name: Abrams
  role: tank initiator
  archetypes:
  - tank/frontline
  - initiator
  tier: B
  trend: rising
  why: The general dash/light-melee change (no longer breaking gun cycle) lets him
    weave shots and punches between plays in lane, a named buff that offsets the anti-heal
    meta keeping him merely B.
  core_items:
  - Witchmail
  - Decay
  - Ethereal Shift
  - Fortitude
  build_variants:
  - tank build
  - CC build
  enabled_by:
  - gun-cycle change
  - Infernal Resilience T3 buff
  countered_by:
  - Decay/anti-heal stacking
  - Venator, Rem, Viscous
  last_changed_patch: Minor Update - 09-16-2026
  notes: 'Seismic Impact T3 Unstoppable 6s->5s; creator read: fallen from S by anti-heal
    meta, not his numbers.'
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
Paradox:
  name: Paradox
  role: pick initiator
  archetypes:
  - burst caster
  - initiator
  tier: B
  trend: falling
  why: Carbine minimum-damage multiplier cut 25->10% (and no longer scaled by T3)
    plus Slowing Hex cooldown up trims her cheap quick-scope poke; the Echo Shard
    bomb and picks keep her strong, just less oppressive.
  core_items:
  - Echo Shard
  - Slowing Hex
  - Superior Cooldown
  build_variants:
  - bomb build
  - pick build
  enabled_by:
  - Echo Shard
  - Slowing Hex every game
  countered_by:
  - cleanse/dispel
  - range denial
  last_changed_patch: Minor Update - 09-16-2026
  notes: 'Creator: strong high-value pick hero whose bomb wins stalemates.'
Dynamo:
  name: Dynamo
  role: initiator/support
  archetypes:
  - initiator
  - support/healer
  tier: A
  trend: rising
  why: Balanced AoE-CC ult with clear counterplay and a shortened (250s) cooldown;
    the tempo meta rewards converting a won lane into picks, and his 52% WR backs
    it.
  core_items:
  - Refresher
  - Superior Cooldown
  - Diviner's Kevlar
  build_variants:
  - ult initiator build
  enabled_by:
  - tempo conversion
  - AoE dispel
  - Refresher
  countered_by:
  - Unstoppable
  - long-range CC
  last_changed_patch: Minor Update - 07-28-2026
  notes: 'Creator: fine and finally picked; only feels lame with Refresher.'
Haze:
  name: Haze
  role: gun carry
  archetypes:
  - gun carry
  - late scaler
  tier: A
  trend: rising
  why: "Fixation got a real buff (headshot stacks 2->3, higher T3 weapon scaling)\
    \ and gun Haze is the build a tempo meta prefers \u2014 headshots convert leads\
    \ where the old Echo-Shard sleep cheese can't carry a losing game."
  core_items:
  - Lucky Shot
  - Ricochet
  - Echo Shard
  - Tesla Bullets
  build_variants:
  - gun build
  - Echo Shard sleep build
  enabled_by:
  - Fixation buff
  - Ricochet farm
  countered_by:
  - Decay/anti-heal
  - CC lockdown
  - Plated Armor
  last_changed_patch: Minor Update - 09-16-2026
  notes: Sleep Dagger got trimmed in July; the newer read is that gun Haze, not the
    sleep combo, is the good build.
Holliday:
  name: Holliday
  role: mobile assassin
  archetypes:
  - mobile assassin
  - initiator
  tier: A
  trend: rising
  why: "Pushed toward a gun hybrid (health/boon 41->43, Crackshot T2 resist-shred,\
    \ longer lasso) and rewarded by a tempo meta where post-20 picks are worth more\
    \ \u2014 though she lost a core enabler as Veil Walker was stripped down."
  core_items:
  - Veil Walker
  - Recharging Rush
  - Rapid Recharge
  build_variants:
  - pick build
  - gun-spirit hybrid
  enabled_by:
  - tempo + longer respawn
  - bounce-pad mobility
  countered_by:
  - Veil Walker nerf
  - CC/dev buffs
  last_changed_patch: Minor Update - 09-16-2026
  notes: 'Creator: best movement in the game; the real strength is double-dipping
    bounce-pad charges, not barrels.'
Calico:
  name: Calico
  role: mobile assassin
  archetypes:
  - mobile assassin
  tier: B
  trend: stable
  why: Above-average skirmisher, but the rerouted breakable timing (3m->5m) hits her
    early underground farm and the tempo meta does her no favors; still ~50% WR on
    a high pick rate.
  core_items:
  - Rapid Recharge
  - Echo Shard
  - Superior Stamina
  build_variants:
  - skirmish build
  enabled_by:
  - early farm
  - mobility
  countered_by:
  - later breakables
  - CC
  last_changed_patch: Minor Update - 07-28-2026
  notes: 'Creator: bottom of A, no nerf needed; the breakable change is described
    as more a Calico hit than a Rem one.'
Grey Talon:
  name: Grey Talon
  role: poke/siege carry
  archetypes:
  - poke/siege
  - gun carry
  tier: C
  trend: falling
  why: "No recent changes and a 45.7% WR; his cross-map execute and poke don't convert\
    \ early leads as hard as dedicated tempo heroes do. Low confidence \u2014 no current\
    \ creator covers him."
  core_items:
  - Sharpshooter
  - Mystic Shot
  - Hollow Point
  build_variants:
  - poke build
  - gun build
  enabled_by:
  - long-range execute
  countered_by:
  - tempo divers
  - flyers
  last_changed_patch: null
  notes: No patch lines and no current source; read inferred from the snapshot, low
    confidence.
Mo & Krill:
  name: Mo & Krill
  role: tank initiator
  archetypes:
  - tank/frontline
  - initiator
  tier: B
  trend: rising
  why: 'Underplayed tank that quietly wins (~51.7% WR): Combo can now cast items and
    Burrow cooldown starts immediately, and the tempo meta favors a front-line that
    can brawl from minute one.'
  core_items:
  - Scourge
  - Decay
  - Fortitude
  build_variants:
  - frontline tank build
  enabled_by:
  - 07-28 quality changes
  - early brawl meta
  countered_by:
  - kiting/CC
  - anti-heal
  last_changed_patch: Minor Update - 07-28-2026
  notes: 'Creator: balanced but nobody plays him; Scourge on him is a big AoE.'
Shiv:
  name: Shiv
  role: anti-tank bruiser
  archetypes:
  - tank/frontline
  - mobile assassin
  tier: A
  trend: rising
  why: 'Still the anti-tank tank: Serrated Knives now do 3.5% current HP at full rage
    instead of ricocheting, and alt-fire got +4% base and higher per-boon scaling,
    so he shreds exactly the HP pools the tempo patch funnels into fights.'
  core_items:
  - Decay
  - Fortitude
  - Witchmail
  - Tankbuster
  build_variants:
  - anti-tank build
  - bruiser build
  enabled_by:
  - current-HP knives
  - alt-fire buff
  countered_by:
  - CC spam
  - kiters
  last_changed_patch: Minor Update - 09-16-2026
  notes: 'Creator: OP, only counter is CC spam; his rework was reverted in a day.'
Ivy:
  name: Ivy
  role: support/healer
  archetypes:
  - support/healer
  tier: A
  trend: falling
  why: Only slight Stone Form nerfs (radius 6->5.75m, T1 heal 7->6%) that the creator
    welcomed; she still owns the support slot at 53.7% WR with the best team-sustain
    and map control.
  core_items:
  - Healing Tempo
  - Healing Nova
  - Echo Shard
  - Capacitor
  build_variants:
  - heal support build
  - Echo Shard stone build
  enabled_by:
  - team sustain
  - map control ult
  countered_by:
  - anti-heal
  - burst
  last_changed_patch: Minor Update - 09-16-2026
  notes: 'Creator: underrated support whose buffs are noticeable on Drifter/Venator.'
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
Yamato:
  name: Yamato
  role: mobile burst assassin
  archetypes:
  - mobile assassin
  - burst caster
  tier: S
  trend: rising
  why: "Buffed again (Crimson Slash T3 heal spirit scaling +0.4, Flying Slash light-melee\
    \ scaling 1.0->1.2) atop a tempo meta that rewards her point-click burst and Refresher\
    \ Unstoppable windows \u2014 a big pick-rate uptick is expected."
  core_items:
  - Refresher
  - Tankbuster
  - Spirit Snatch
  - Mystic Reverb
  build_variants:
  - spirit burst build
  - Refresher unstoppable build
  enabled_by:
  - tempo meta
  - 09-16 buffs
  - Refresher
  countered_by:
  - Counterspell
  - Dispel Magic
  last_changed_patch: Minor Update - 09-16-2026
  notes: 'Creator: brought up to modern power level; wants the grapple charges removed.'
Viscous:
  name: Viscous
  role: tank/enabler
  archetypes:
  - tank/frontline
  - support/healer
  tier: B
  trend: falling
  why: Cube cast range 26->20m and Puddle Punch cooldown 21->24s trim his signature
    enabler, and Splatter/alt-fire nerfs cut his damage; only the Goo Ball T3 spirit-scaling
    buff helps.
  core_items:
  - Decay
  - Echo Shard
  - Fortitude
  build_variants:
  - cube support build
  - ball build
  enabled_by:
  - Cube rescue
  - Echo Shard reset
  countered_by:
  - Cube range nerf
  - AoE/spread
  last_changed_patch: Minor Update - 09-16-2026
  notes: 'Creator: broken because the Cube is too strong for its cooldown; wants power
    moved off it.'
Pocket:
  name: Pocket
  role: spirit carry
  archetypes:
  - spirit carry
  - burst caster
  tier: B
  trend: falling
  why: Affliction's DPS and duration were trimmed back in July and nothing replaced
    them; his 46.2% WR says the tempo meta doesn't reward a scaling cloak assassin
    who wants long fights.
  core_items:
  - Boundless Spirit
  - Echo Shard
  - Fortitude
  build_variants:
  - Affliction build
  - sidelane build
  enabled_by:
  - Affliction
  - sidelane wave clear
  countered_by:
  - Counterspell
  - tempo comps
  last_changed_patch: Minor Update - 07-28-2026
  notes: was an S-tier pick; now mid despite the kit being unchanged in direction.
Vyper:
  name: Vyper
  role: gun carry
  archetypes:
  - gun carry
  tier: A
  trend: stable
  why: "Top WR (54.6%) even after fresh nerfs (Slither T3 barrier 5->4s, Petrifying\
    \ Bola cd 105->115), but her kit lives on the draft \u2014 she 1v6s into low-CC\
    \ comps and is useless into the CC-heavy tempo picks."
  core_items:
  - Hollow Point
  - Burst Fire
  - Fortitude
  build_variants:
  - gun build
  enabled_by:
  - highest WR
  - no-CC lobbies
  countered_by:
  - CC/knockup comps
  - Billy, Lash, Silver
  last_changed_patch: Minor Update - 09-16-2026
  notes: 'Creator: balanced but pure coin flip on matchup.'
Mina:
  name: Mina
  role: mobile spirit assassin
  archetypes:
  - mobile assassin
  - burst caster
  tier: C
  trend: falling
  why: "Dropped with the strong heroes and given no compensation; 47.2% WR on a 39.8%\
    \ pick rate says the overloaded kit no longer converts, so one buff could flip\
    \ her \u2014 she needs a rework instead."
  core_items:
  - Superior Stamina
  - Echo Shard
  - Mystic Reverb
  build_variants:
  - mobility burst build
  enabled_by:
  - mobility + damage
  - ult silence
  countered_by:
  - tempo comps
  - CC
  last_changed_patch: Minor Update - 07-28-2026
  notes: 'Creator: bottom of B/top C; small buff would make her broken again.'
Drifter:
  name: Drifter
  role: melee bruiser
  archetypes:
  - mobile assassin
  - gun carry
  tier: A
  trend: stable
  why: Blind-pickable melee bruiser with built-in anti-heal and a huge 57.8% pick
    rate; still one of the best solo-queue picks even as widespread anti-heal caps
    his ceiling.
  core_items:
  - Decay
  - Toxic Bullets
  - Fortitude
  build_variants:
  - melee build
  - anti-heal build
  enabled_by:
  - blind-pickable
  - built-in anti-heal
  countered_by:
  - anti-heal stacking
  - CC
  last_changed_patch: null
  notes: Oldest source had him S, then A; no direct change in the last patch.
Venator:
  name: Venator
  role: gun carry
  archetypes:
  - gun carry
  tier: A
  trend: rising
  why: "Ira Domini now works with Ricochet and Split Shot (3 bolts), a straight late-damage\
    \ buff, but a 45.7% WR shows the 'no weak point' read hasn't converted in the\
    \ tempo meta \u2014 strong, not free."
  core_items:
  - Monster Rounds
  - Weakening Headshot
  - Fortitude
  - Hollow Point
  build_variants:
  - no-item stat build
  - grenade build
  enabled_by:
  - 09-16 ult buffs
  - huge HP/base stats
  countered_by:
  - tempo comps
  - kiting/CC
  last_changed_patch: Minor Update - 09-16-2026
  notes: Creator called him an S-tier no-weak-point hero; data now disagrees at high
    rank.
Paige:
  name: Paige
  role: lane-winning support
  archetypes:
  - support/healer
  - lane bully
  tier: S
  trend: rising
  why: 'The patch''s clearest winner: direct buffs (heavy-melee spirit scaling 0.3->0.45,
    Captivating Read T1 -11->-14s and T3 +1m->+2m) land in a tempo meta that rewards
    her lane-winning, and the flyers she feared were nerfed.'
  core_items:
  - Knockdown
  - Healing Tempo
  - Fortitude
  - Slowing Hex
  build_variants:
  - tempo support build
  - CC build
  enabled_by:
  - 09-16 buffs
  - tempo meta
  - flyers nerfed
  countered_by:
  - pick comps
  - burst
  last_changed_patch: Minor Update - 09-16-2026
  notes: 'Creator: best-designed new support, biggest winner, a monster now.'
Billy:
  name: Billy
  role: tank/frontline
  archetypes:
  - tank/frontline
  - lane bully
  tier: S
  trend: stable
  why: 'Still the best front-liner (52.2% WR, 31.9% PR): the Lifestrike melee-heal
    plus 48% slow buff is effectively a Billy item, and his Scourge/ult AoE frontline
    turns early tempo leads into wins.'
  core_items:
  - Scourge
  - Echo Shard
  - Lifestrike
  - Witchmail
  build_variants:
  - frontline tank build
  - Scrooge build
  enabled_by:
  - 09-16 Lifestrike buff
  - tempo brawls
  countered_by:
  - kiting
  - anti-heal
  last_changed_patch: Minor Update - 08-12-2026
  notes: "Creator: broken \u2014 too much CC, damage, frontline and movement for a\
    \ tank; a top Scourge abuser."
Graves:
  name: Graves
  role: gun carry/split pusher
  archetypes:
  - gun carry
  - split pusher
  tier: C
  trend: rising
  why: "Small help (health/boon 33->35, earlier Jar of Dead buffs) but still the worst-scaling\
    \ gun carry \u2014 48.6% WR and permanently behind until late because her base\
    \ stats are awful."
  core_items:
  - Toxic Bullets
  - Ricochet
  - Echo Shard
  build_variants:
  - on-hit build
  - summoner build
  enabled_by:
  - health/boon buff
  - Jar of Dead buffs
  countered_by:
  - anything mobile
  - dive
  last_changed_patch: Minor Update - 09-16-2026
  notes: 'Creator: effectively the worst hero, permanently behind until ~25 min.'
Apollo:
  name: Apollo
  role: lane bully initiator
  archetypes:
  - initiator
  - lane bully
  tier: S
  trend: rising
  why: "Absent from the notes but the biggest winner: a top early-game snowballer\
    \ (ganks, instant jungle clears, escape, high flat damage/heal) whose tempo playstyle\
    \ is exactly what the economy patch rewards \u2014 the creator calls him 'super\
    \ buffed'."
  core_items:
  - Dispel Magic
  - Restorative Locket
  - Fortitude
  build_variants:
  - tempo lane build
  - spirit support build
  enabled_by:
  - economy/tempo patch
  - Riposte buffs
  countered_by:
  - super-scalers that out-late him
  last_changed_patch: Minor Update - 08-12-2026
  notes: "Note-absence hiding a buff \u2014 the archetype-level winner of the patch."
Silver:
  name: Silver
  role: gun tank carry
  archetypes:
  - gun carry
  - tank/frontline
  tier: S
  trend: rising
  why: "Huge patch: Weighted Bola now acts as a Phantom-Strike-style grounded interrupt,\
    \ health/boon 28->31, sprint 1.5->2.5, and dashes/light melee no longer break\
    \ her gun cycle \u2014 the single biggest winner, even though her 46.7% WR is\
    \ pre-patch."
  core_items:
  - Hollow Point
  - Fortitude
  - Diviner's Kevlar
  - Berserker
  build_variants:
  - gun tank build
  enabled_by:
  - Weighted Bola interrupt
  - gun-cycle change
  - sprint/health buffs
  countered_by:
  - CC/debuff spam
  - kiting
  last_changed_patch: Minor Update - 09-16-2026
  notes: Weighted Bola listed as a straight upgrade enabling picks she couldn't before.
Celeste:
  name: Celeste
  role: spirit burst carry
  archetypes:
  - spirit carry
  - burst caster
  - mobile assassin
  tier: A
  trend: falling
  why: Seven direct nerfs plus indirect hits (item nerfs, scaling nerfs, and slows
    now affecting air drag while she flies); her 54.6% WR is a lagging pre-patch reading
    and she should settle lower.
  core_items:
  - Echo Shard
  - Boundless Spirit
  - Fortitude
  build_variants:
  - spirit carry build
  - ult build
  enabled_by:
  - high base power
  - ult damage at Mid Boss
  countered_by:
  - 09-16/08-22 nerfs
  - slow-affects-air-drag
  - Paige rise
  last_changed_patch: Minor Update - 09-16-2026
  notes: 'Creator: nerfed seven ways, and the indirect hits matter more than the notes.'


## Current item entries (changed items only; may be empty for items not yet in the KB)

Ballistic Enchantment:
  name: Ballistic Enchantment
  role: utility spirit item
  bought_by: []
  slot: Spirit
  tier: 3
  notes: '09-16: duration 14->20s.'

Cultist Sacrifice:
  name: Cultist Sacrifice
  role: econ spirit item
  bought_by: []
  slot: Spirit
  tier: 3
  notes: '09-16: bounty 180->170%; soul-gen trimmed as part of the economy tightening.'

Decay:
  name: Decay
  role: anti-heal spirit item
  bought_by:
  - Infernus
  - Lady Geist
  - Abrams
  - Mo & Krill
  - Shiv
  - Viscous
  - Drifter
  - Rem
  - Billy
  slot: Spirit
  tier: 3
  notes: "09-16: DPS -25% but duration +20% \u2014 trades burst healing-cut for better\
    \ late scaling. Still the go-to anti-heal slot."

Diviner's Kevlar:
  name: Diviner's Kevlar
  role: ultimate/defense item
  bought_by:
  - Dynamo
  - Silver
  slot: Vitality
  tier: 3
  notes: '09-16: now grants +10% Ultimate Ability CDR; 07-28: spirit power +35->+40.'

Focus Lens:
  name: Focus Lens
  role: spirit amp item
  bought_by: []
  slot: Spirit
  tier: 3
  notes: '09-16: damage 30->35%, cast range 20->25m; still cleansable, so niche.'

Fortitude:
  name: Fortitude
  role: sustain vitality item
  bought_by:
  - Infernus
  - Seven
  - Abrams
  - Mo & Krill
  - Shiv
  - Warden
  - Victor
  - Paige
  - The Doorman
  - Billy
  - Apollo
  - Rem
  - Silver
  - Venator
  - Celeste
  - Dynamo
  - Kelvin
  - Vindicta
  - Vyper
  slot: Vitality
  tier: 3
  notes: '09-16: max-health regen 2->2.25%. The default survivability slot on almost
    every bruiser.'

Golden Goose Egg:
  name: Golden Goose Egg
  role: econ item
  bought_by: []
  slot: Vitality
  tier: 4
  notes: "09-16: damage penalty -10->-15%, souls/min 90->80, stored souls now count\
    \ toward net worth \u2014 effectively unbuyable; the patch's worst item."

Hollow Point:
  name: Hollow Point
  role: early weapon shred item
  bought_by:
  - Seven
  - Vindicta
  - Vyper
  - Venator
  - Silver
  - Grey Talon
  slot: Weapon
  tier: 2
  notes: '09-16: bullet resist reduction 9->10%. The cheap early-gun item of the tempo
    meta.'

Leech:
  name: Leech
  role: lifesteal item
  bought_by: []
  slot: Vitality
  tier: 4
  notes: '09-16: bullet+spirit lifesteal 25->28%; still generally weak.'

Lifestrike:
  name: Lifestrike
  role: melee heal/CC weapon item
  bought_by:
  - Billy
  slot: Weapon
  tier: 3
  notes: '09-16: melee-heal 100+1.5 -> 120+1.75 and 30->35%; with slows now affecting
    air drag, its 48% slow makes it a strong CC item, especially spammed by Billy.'

Mercurial Magnum:
  name: Mercurial Magnum
  role: spirit on-hit item
  bought_by:
  - Warden
  slot: Spirit
  tier: 3
  notes: "09-16: base bullet damage scaling 0.49->0.38 and base damage 25->20% \u2014\
    \ a heavy nerf that helps kill the Mercurial + Spiritual Overflow build."

Plated Armor:
  name: Plated Armor
  role: on-hit defense item
  bought_by: []
  slot: Vitality
  tier: 3
  notes: "09-16 bug fix: now actually blocks on-hit spirit damage from Mercurial Magnum,\
    \ Vindicta's Flight, Wraith's Full Auto, Tesla Bullets/Capacitor \u2014 a big\
    \ indirect nerf to those builds and an anti-mixed-damage counter."

Radiant Regeneration:
  name: Radiant Regeneration
  role: healing spirit item
  bought_by:
  - Kelvin
  slot: Spirit
  tier: 3
  notes: "08-22 heal on cast 70->65 and 09-16 per-boon scaling 2->1.7 \u2014 cumulative\
    \ nerf to healing supports."

Restorative Locket:
  name: Restorative Locket
  role: sustain utility item
  bought_by:
  - Apollo
  slot: Vitality
  tier: 3
  notes: '09-16: heal per boon 0.5->0.45, stack range 35->32m; 08-22 spirit resist
    10->8%. Still viable for the stamina/utility.'

Shadow Weave:
  name: Shadow Weave
  role: invis weapon item
  bought_by: []
  slot: Weapon
  tier: 3
  notes: "09-16: now builds from Sprint Boots, sprint speed 1.5->2, cooldown 45->37s\
    \ \u2014 buffed, but creators still call it poor."

Slowing Hex:
  name: Slowing Hex
  role: CC active
  bought_by:
  - Wraith
  - Paradox
  - Paige
  slot: Spirit
  tier: 3
  notes: '09-16: cooldown 27->29s. Still a near-every-game buy on pick heroes, now
    also a real slow given air-drag change.'

Spiritual Overflow:
  name: Spiritual Overflow
  role: spirit proc/steroid item
  bought_by:
  - Warden
  slot: Spirit
  tier: 3
  notes: '09-16: buildup 35% slower, spirit power 40->30, fire rate 30->25% (on top
    of 07-28 changes); the Mercurial-carry build is dead.'

Tankbuster:
  name: Tankbuster
  role: anti-tank weapon item
  bought_by:
  - Shiv
  - Yamato
  slot: Weapon
  tier: 3
  notes: "07-28: no longer procs off items; 09-16 current-health bonus 8->7.5% \u2014\
    \ cumulative trim to the anti-tank slot."

Toxic Bullets:
  name: Toxic Bullets
  role: anti-heal DoT weapon item
  bought_by:
  - Infernus
  - Drifter
  - Graves
  slot: Weapon
  tier: 2
  notes: '09-16: spirit scaling 0.005->0.006%. Core burn/anti-heal slot and one of
    the few real answers to inflated HP.'

Trophy Collector:
  name: Trophy Collector
  role: econ item
  bought_by: []
  slot: Vitality
  tier: 2
  notes: '09-16: souls/min 18->16; part of the soul-economy trim.'

Veil Walker:
  name: Veil Walker
  role: invisibility utility item
  bought_by:
  - Holliday
  - Warden
  slot: Vitality
  tier: 3
  notes: "09-16 nerf: no longer builds from Sprint Boots (lost +2 sprint/regen), movespeed\
    \ removed when invis drops, spirit power 10->6 \u2014 no longer an auto-buy, now\
    \ a pick-hero item."

Weakening Headshot:
  name: Weakening Headshot
  role: shred weapon item
  bought_by:
  - Venator
  slot: Weapon
  tier: 3
  notes: '09-16: bullet resist reduction -13%->-12%, a nudge down.'


## What to do

Produce the post-patch knowledge base state. This KB is read by the analyst on the *next* patch, so write it as durable state, not as a patch summary.

1. **meta.md**: rewrite the whole document in this structure (markdown, <= 400 words):
   - `# Meta state` line with `Last patch: Minor Update - 09-16-2026 (2026-09-16)`
   - `## Thesis` — 2-4 sentences: how games are won right now (tempo vs scaling, fight shape, what archetypes carry).
   - `## Economy and systems` — bullets describing the current state of comeback, bounties, objectives, respawn, movement/slows, in present tense with current numbers where known.
   - `## Archetype standing` — one bullet per archetype in play: up/down/stable and why.
   - `## Watchlist` — 3-6 bullets: heroes/items/systems that are uncertain and should be checked against data.
   - `## Recent history` — keep at most 5 bullets, newest first, one line per patch: "Minor Update - 09-16-2026: <headline>". Carry forward existing bullets from the current meta.md, drop the oldest beyond 5.
2. **hero_updates**: for each mover, the fields that changed. Allowed fields: role, archetypes, tier, trend, why, core_items, build_variants, enabled_by, countered_by, notes. Set `last_changed_patch` to "Minor Update - 09-16-2026" for heroes that had direct changes. `why` is 1-2 sentences of present-tense state ("strong because X; weak to Y"), not a changelog. `notes` may hold a short changelog line (keep the last 3 lines, newest first). Do not touch heroes that did not move.
3. **item_updates**: for each changed item, the fields that changed. Allowed fields: role, bought_by, slot, tier, notes. `bought_by` must list hero names that build it as core or common situational pick, updated for this patch.
4. **change_log**: one line per KB edit you made, for the human to skim.

Tier is one of S/A/B/C/D. Trend is rising/stable/falling.

## Output schema

{
  "meta_md": "full markdown text",
  "hero_updates": {"Hero Name": {"tier": "A", "trend": "falling", "why": "...", "core_items": ["..."], "last_changed_patch": "...", "notes": "..."}},
  "item_updates": {"Item Name": {"role": "...", "bought_by": ["..."], "notes": "..."}},
  "change_log": ["Hero Name: tier S -> A (Card Trick heal nerfs + Veil Walker loss)", "..."]
}
