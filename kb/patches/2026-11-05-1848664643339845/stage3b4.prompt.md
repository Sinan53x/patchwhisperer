# Task: per-hero analysis (hero batch)

Patch: Minor Update - 11-04-2026 (2026-11-05)

## Systems analysis

{
 "systems_changed": [],
 "tempo_shift": {
  "direction": "neutral",
  "confidence": 0.85,
  "why": "No systems changes: the patch touches only one item (Healbane) and seven heroes, with no economy, objective, respawn, movement, slow, parry, reload, or map/jungle edits. The 10-30 comeback-and-Haunt framework stands unchanged, so tempo direction is inherited, not shifted."
 },
 "archetype_effects": [],
 "intent_read": "This is a maintenance/micro patch, not a systems patch: Valve is trimming individual outliers (Apollo, Baba, Celeste, Deadman Danny, Mo & Krill, Nurse Harrow, Rat King) and adjusting Healbane rather than reshaping how souls are earned or where fights happen. Any archetype movement here comes from hero and item numbers, not from systems, so it belongs in the hero/item analysis stage, not this one."
}

## Item analysis

{
 "items": [
  {
   "item": "Healbane",
   "direction": "nerf",
   "magnitude": "moderate",
   "summary": "The 10-30 anti-heal coverage plan gets trimmed: one Healbane is unchanged, but a second source adds less and a fourth caps at 72% instead of 82%. That is a soft buff to dedicated healers and a soft nerf to teams stacking Healbane as a team slot.",
   "affected_heroes": [
    {
     "hero": "Seven",
     "relationship": "core",
     "effect": "down",
     "why": "His Healbane is the team's anti-sustain coverage; the lower 4-stack cap reduces the payoff when allies also buy it."
    },
    {
     "hero": "Infernus",
     "relationship": "core",
     "effect": "down",
     "why": "Healbane plus Toxic Bullets was his anti-heal package into healer comps; harsher multi-source diminishing returns trims that combo."
    },
    {
     "hero": "Drifter",
     "relationship": "situational",
     "effect": "down",
     "why": "His built-in heal cut plus Healbane/Toxic Bullets was a real anti-sustain answer; the stacking nerf weakens that composition."
    },
    {
     "hero": "Yamato",
     "relationship": "core",
     "effect": "down",
     "why": "Healbane is a bruiser-sustain cut in her on-hit core; it loses value mainly when the team stacks anti-heal."
    },
    {
     "hero": "Mirage",
     "relationship": "core",
     "effect": "neutral",
     "why": "Healbane is a sustain/anti-heal slot in his spirit-amp core; single-source use is unchanged."
    },
    {
     "hero": "Apollo",
     "relationship": "situational",
     "effect": "up",
     "why": "He buys Healbane in the utility build, but as a Locket/heal-sustain hero he benefits more from enemy anti-heal stacking being weaker."
    },
    {
     "hero": "Kelvin",
     "relationship": "core",
     "effect": "up",
     "why": "Dome/regen sustain is his win condition; weaker stacked anti-heal lets his heals survive coordinated Healbane buys."
    },
    {
     "hero": "Ivy",
     "relationship": "situational",
     "effect": "up",
     "why": "Tether healing was the main casualty of 10-30 anti-heal stacking; this patch gives it some relief."
    },
    {
     "hero": "Mo & Krill",
     "relationship": "core",
     "effect": "up",
     "why": "Scorn sustain gets more value when enemy anti-heal caps lower; his own Healbane is secondary."
    },
    {
     "hero": "Shiv",
     "relationship": "core",
     "effect": "up",
     "why": "His regen/sustain shell was taxed by stacked anti-heal; the lower 4-stack cap helps him start fights healthier."
    }
   ],
   "build_shift": "No component or slot change: Healbane remains a Vitality T2. The shift is strategic — one Healbane is still the same, but a second or third buyer now adds less, so teams should stop treating it as a coverage slot and let one dedicated buyer hold it.",
   "rows": [
    {
     "label": "2 stacks",
     "old": "57.8%",
     "new": "54.7%",
     "text": null,
     "effect": "bad",
     "ability": null
    },
    {
     "label": "4 stacks",
     "old": "82.2%",
     "new": "72%",
     "text": null,
     "effect": "bad",
     "ability": null
    }
   ]
  }
 ],
 "notable_item_stories": [
  "Healbane is the patch's only item move, so the item meta is otherwise frozen; the change mainly rebalances sustain comps against anti-heal comps.",
  "Expect fewer double-Healbane buys in coordinated play: one dedicated buyer is enough, and over-stacking anti-heal is now less efficient."
 ]
}

## Direct hero changes in this patch (grouped by hero; heroes not listed had no direct changes)

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

## Knowledge base: the heroes in this batch plus their matchup partners (pre-patch)

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
Abrams:
  name: Abrams
  role: tank initiator
  archetypes:
  - tank/frontline
  - initiator
  tier: B
  trend: stable
  why: "Melee tank who still owns the routes ranged kits cannot contest \u2014 Tough\
    \ Crates and Barrel Mimics \u2014 and the patch's in-fight props (Torment Pulse\
    \ +4% melee resist, Battle Vest 18->22%, Bullet Lifesteal) suit his brawl better\
    \ than his old aura did. Hunter's Aura's LOS gate is the cost: it no longer shreds\
    \ through walls on the Shoulder Charge approach, so his engage pays one window\
    \ later than it used to."
  core_items:
  - Close Quarters
  - Monster Rounds
  - Melee Lifesteal
  - Stalker
  - Melee Charge
  - Bullet Resist Shredder
  - Hunter's Aura
  - Extra Regen
  - Warp Stone
  - Duration Extender
  - Dispel Magic
  - Superior Duration
  - Phantom Strike
  - Spirit Resilience
  build_variants:
  - Melee brawler (gun)
  - CC/sustain tank (spirit)
  enabled_by:
  - gun-cycle change (dashes/light melee no longer break gun cycle)
  - melee core -> cheap heavy-melee access to Tough Crates (58 souls) and Barrel Mimics,
    which punish squishy clearers but not his Siphon sustain
  - parry-cooldown change makes dives on him riskier
  - Infernal Resilience T3 buff
  - Fortitude max-health regen 2->2.25% (09-16)
  - early-tempo/early-snowball meta
  - core tank items untouched
  - Rem (heal enabler)
  countered_by:
  - Decay / anti-heal stacking
  - kiting mobile gun carries (Vyper, Wraith)
  - spirit burst (Celeste)
  - Shiv (anti-tank bruiser)
  - Ivy (peel/slow)
  last_changed_patch: Halloween 2026 + Gameplay Update
  notes: 'Halloween 2026 + Gameplay Update (10-30, direct): base gun damage +5% and
    Siphon Life T3 +18->+22 DPS are small fight-length gains, but the Shoulder Charge
    fix removes his free hold on enemies who never hit a wall; Hunter''s Aura is now
    LOS-gated, so Battle Vest/Bullet Lifesteal (which never turn off) compete for
    the same slot.

    Shh... This Won''t Hurt a Bit. (10-20, indirect): Barrel Mimics convert breakable-chaining
    into a sustain check his heavy-melee + Siphon core passes, making the uncontestable
    crate route safer than it is for squishy gun clearers.

    Paint the Town (10-16, indirect): his melee core remains the cheap route into
    the Haunt/crate farm and the objective-parry change keeps dives on him risky;
    frontline up, anti-tank Shiv his real counter.'
  builds:
  - name: Melee brawler (gun)
    damage: gun
    core_items:
    - Close Quarters
    - Monster Rounds
    - Melee Lifesteal
    - Stalker
    - Melee Charge
    - Battle Vest
    - Bullet Resist Shredder
    - Hunter's Aura
    popularity: primary
    notes: "Still the ~80-90% default: cheap Close Quarters/Monster Rounds spike the\
      \ early melee trade, then Battle Vest (18->22% weapon damage) carries the brawl\
      \ while Hunter's Aura is taken later \u2014 its new LOS gate means it no longer\
      \ pays before contact, which is exactly the approach distance he buys tank stats\
      \ to survive."
  - name: CC/sustain tank (spirit)
    damage: spirit
    core_items:
    - Extra Regen
    - Warp Stone
    - Duration Extender
    - Dispel Magic
    - Superior Duration
    - Phantom Strike
    - Spirit Resilience
    popularity: secondary
    notes: Late-game defensive layer (avg buy 17-26m) that extends Seismic Impact/Siphon
      Life with Superior Duration + Duration Extender and blinks him onto targets
      via Warp Stone/Phantom Strike; the answer to being kited and anti-healed.
  matchups:
    beats:
    - Venator
    - Yamato
    - Apollo
    - Mirage
    - Mina
    loses_to:
    - Ivy
    - Vyper
    - Celeste
    - Wraith
    - Paige
  matchup_notes: "He wins any trade he can force: Venator (62%), Yamato (58%) and\
    \ Apollo (56%) are squishier carries whose burst Infernal Resilience + Siphon\
    \ out-sustain once he closes \u2014 note this directly contradicts the prior entry's\
    \ claim that Venator counters him. He loses to disengage and spirit burst: Ivy\
    \ (41%) peels/slows his engage, while Vyper (45%), Wraith (45%) and Celeste (45%)\
    \ out-range or out-burst a static frontline."
  confidence: 0.7
  released_on: null
  provisional: false
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
Paradox:
  name: Paradox
  role: pick/sniper initiator
  archetypes:
  - burst caster
  - initiator
  - poke/siege
  tier: B
  trend: stable
  why: 'Carbine pick/sniper who traded pick quality for frequency: Paradoxical Swap
    at 95s buys her an extra pick per fight cycle, but Express Shot -5% secondary
    fire and HVR 60->45% velocity weaken the crit-carbine burst that pick converts,
    and Steam Vents now sell stamina instead of the invisibility approach her roams
    used. The ability-burst line gains relative value over the crit line; anything
    that closes distance still kills her.'
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
    \ velocity 60->45% cut the carbine crit burst, and the Steam Vent rework (stamina\
    \ regen instead of invisibility) removes the approach her roams leaned on \u2014\
    \ ability burst (Slowing Hex/Compress Cooldown/Tankbuster) now outranks the HVR/Express\
    \ Shot crit line.\nShh... This Won't Hurt a Bit. (10-20, indirect): instant casts\
    \ tighten her carbine->swap combo, and Barrel Mimics leave squishy crate clearers\
    \ stationary for picks; mobile divers still close on her.\nPaint the Town (10-16,\
    \ indirect): new districts, more hiding spots and Steam-Vent invisibility sharpen\
    \ her roamer pick setups and keep her ahead of Bebop in that slot; the sniper\
    \ line still folds to mobile divers."
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
  tier: B
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
Haze:
  name: Haze
  role: gun carry
  archetypes:
  - gun carry
  tier: B
  trend: stable
  why: "Tempo gun carry whose own damage is untouched \u2014 Fixation still decides\
    \ her games \u2014 but the answers to it got cheaper: Return Fire now returns\
    \ Fixation damage on frontline tanks who already bought it, Bullet Resilience\
    \ is 30->35%, and Smoke Bomb T3 no longer dispels undispellable debuffs. Same\
    \ carry, one fewer escape and a real counter-slot on the enemy front line."
  core_items:
  - Extra Spirit
  - Rapid Rounds
  - Active Reload
  - Swift Striker
  - Surge of Power
  - Tesla Bullets
  - Ricochet
  - Burst Fire
  - Capacitor
  build_variants:
  - Gun carry (Fixation)
  - Ricochet AoE / late pivot
  enabled_by:
  - Fixation buff (headshot stacks 2->3, higher T3 weapon scaling)
  - tempo meta (comeback souls gutted, lane win converts)
  - gun-cycle smoothing (dash/light melee no longer break gun cycle)
  - Ricochet farm
  countered_by:
  - Plated Armor (gun resist)
  - CC lockdown
  - mobile dive (Holliday, Calico, Yamato)
  - lane bullies (Paige, Apollo)
  - Celeste burst
  - weak T4 gun items (Ricochet/Capacitor)
  last_changed_patch: Halloween 2026 + Gameplay Update
  notes: "Halloween 2026 + Gameplay Update (10-30, direct): Smoke Bomb T3 no longer\
    \ dispels undispellable debuffs (e.g. Specter Crash), and Return Fire now returns\
    \ Fixation damage plus shows its 10% bullet resist on the tooltip, handing frontline\
    \ tanks the anti-Haze slot they were already buying; Bullet Resilience 30->35%\
    \ adds a second cheap answer.\n09-16 (indirect): Plated Armor's on-hit fix now\
    \ blanks Tesla Bullets spirit damage, weakening her Ricochet/Tesla late pivot.\n\
    Role reframed per reader: farm-carry is meta-dependent, not her identity \u2014\
    \ historically a Smoke Bomb roamer/ganker on isolated targets, and T4 weakness\
    \ gates the late-scaler label."
  builds:
  - name: Gun carry (Fixation)
    damage: gun
    core_items:
    - Extra Spirit
    - Rapid Rounds
    - Active Reload
    - Swift Striker
    - Surge of Power
    - Burst Fire
    popularity: primary
    notes: "Default build: cheap early attack speed/reload items (buy_min 3.6-8.3)\
      \ land Fixation headshots faster, then Surge of Power/Burst Fire convert a lane\
      \ lead into single-target kills \u2014 pick it from a winning or even lane."
  - name: Ricochet AoE / late pivot
    damage: gun
    core_items:
    - Tesla Bullets
    - Ricochet
    - Capacitor
    popularity: secondary
    notes: Late waveclear/clustered-fight pivot (buy_min 17-22, ~55% Ricochet share);
      it farms well but lives on the weak T4 gun items that stop her scaling, so it
      is a fallback when the game stretches, not a win condition.
  matchups:
    beats:
    - Lady Geist
    - Grey Talon
    - Silver
    - Paradox
    - Pocket
    loses_to:
    - Celeste
    - Ivy
    - Victor
    - Vyper
    - Paige
  matchup_notes: "She out-tempos immobile, kit-dependent heroes \u2014 Lady Geist\
    \ (57%) and Grey Talon (56%) cannot punish her lane before their tools scale,\
    \ and Silver (56%) is a slow gun tank she pokes out on Fixation. Her losses are\
    \ the meta's strong mobile/lane heroes: Celeste (42%) out-bursts her before stacks\
    \ build, Vyper (45%) and Ivy (43%) dive or out-sustain her low-mobility frame,\
    \ and Paige (46%) wins the lane outright."
  confidence: 0.68
  released_on: null
  provisional: false
Holliday:
  name: Holliday
  role: mobile assassin
  archetypes:
  - mobile assassin
  - initiator
  tier: A
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
Bebop:
  name: Bebop
  role: hook initiator
  archetypes:
  - initiator
  - burst caster
  tier: B
  trend: falling
  why: "Single-target hook initiator whose one job \u2014 punishing a body standing\
    \ in lane \u2014 is worth less every patch: souls sit in spread corridors, Steam\
    \ Vents hand hooked targets a disengage his combo cannot chase, and Paradox owns\
    \ the roamer slot. His Veil Walker is still stripped and the farm economy gives\
    \ a hook nothing to punish."
  core_items:
  - Headshot Booster
  - Spirit Strike
  - Slowing Hex
  - Veil Walker
  - Headhunter
  - Spirit Snatch
  - Stalker
  - Fleetfoot
  - Siphon Bullets
  build_variants:
  - Hook combo
  - Gun
  - Beam/spirit burst
  enabled_by:
  - hook pick potential
  - Slowing Hex
  - Spirit Snatch
  - Veil Walker
  - tempo/early-snowball meta
  countered_by:
  - Billy
  - Kelvin
  - Dynamo
  - burst-proof tanks (Abrams, Mo & Krill)
  - cleanse/dispel items
  last_changed_patch: null
  notes: 'Shh... This Won''t Hurt a Bit. (10-20, indirect): Steam Vents give every
    hooked target a free disengage he cannot chase, and a spread corridor farm offers
    a single-target hook nothing to punish.

    Paint the Town (10-16, indirect): a single-target hook cannot punish Haunt/crate
    routing, contested Soul Bags only partly extend his fights, and the roamer slot
    has tilted to Paradox.

    City Never Sleeps: no direct line; the farm/sustain economy plus Paradox''s rise
    down-rank him in the roamer slot.'
  builds:
  - name: Hook combo
    damage: hybrid
    core_items:
    - Headshot Booster
    - Spirit Strike
    - Slowing Hex
    - Veil Walker
    - Headhunter
    - Spirit Snatch
    popularity: primary
    notes: 'The default Bebop: hook into Slowing Hex, then Sticky Bomb/uppercut burst
      while Veil Walker covers the dive; buys a gun T1 (Headshot Booster) in lane
      but the pick tools are spirit-tagged.'
  - name: Gun
    damage: gun
    core_items:
    - Headshot Booster
    - Stalker
    - Headhunter
    - Fleetfoot
    - Siphon Bullets
    popularity: secondary
    notes: Right-click DPS behind hook lockdown; creators call it the strongest build,
      but only Headshot Booster/Headhunter reach the share of the combo core, so the
      data ranks it second.
  - name: Beam/spirit burst
    damage: spirit
    core_items:
    - Spirit Strike
    - Slowing Hex
    - Spirit Snatch
    - Siphon Bullets
    popularity: niche
    notes: Hyper Beam-focused spirit burst; creators flag it as easily counterable,
      and it only scales late off Siphon Bullets (28.5 min), so few commit to it.
  matchups:
    beats:
    - Holliday
    - Infernus
    - Venator
    - Sinclair
    - Shiv
    loses_to:
    - Kelvin
    - Billy
    - Celeste
    - Dynamo
    - Vyper
  matchup_notes: 'Bebop''s hook punishes squishy carries that must stand their ground
    to deal damage (Infernus 57%, Venator 56%) and out-picks mobile assassins like
    Holliday (57%). He folds to anything that ignores a single-target combo: burst-proof
    tanks (Billy 43%), sustain that erases the burst (Kelvin 42%), and a better initiator
    dictating fights (Dynamo 44%).'
  confidence: 0.6
  released_on: null
  provisional: false
Calico:
  name: Calico
  role: mobile assassin
  archetypes:
  - mobile assassin
  tier: A
  trend: rising
  why: "Melee-spirit assassin whose burst window grew \u2014 Leaping Slash T3 +60->+90\
    \ and Ava T3 6->8s \u2014 on a jungle that pays 10% more per camp she takes by\
    \ kill rather than clear. The Steam Vent rework removes one invisibility approach\
    \ and the comeback levers punish a snowball that stalls, so she is a sharper diver\
    \ with less margin; stacked-HP frontlines still cap her."
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
  - off-map soul generation as a 3/4
  - Sprint Boots
  - mobile assassin archetype
  - Leaping Slash T3 +60->+90 damage
  - Ava T3 6->8s dive window
  countered_by:
  - CC/lockdown (Dynamo, Mo & Krill)
  - tank frontline she cannot burst (Abrams, Victor)
  - long-range kiting gun carries (Vyper, Warden)
  - burst vs low HP (Yamato)
  last_changed_patch: Halloween 2026 + Gameplay Update
  notes: 'Halloween 2026 + Gameplay Update (10-30, direct): Leaping Slash T3 +60->+90
    damage and Ava T3 6->8s sharpen her melee-spirit burst and second pick; the Steam
    Vent rework (stamina regen instead of invisibility) trims one roam route, and
    the raised non-hero comeback gold + tick souls punish a snowball that stalls.

    Shh... This Won''t Hurt a Bit. (10-20, indirect): districts and vent invisibility
    extend her roam; cat form still can''t heavy-melee Tough Crates, and the frontline
    meta gives her more unburstable bodies.

    Paint the Town (10-16, indirect): tempo snowball plus new district/Steam-Vent
    routes suit her roam; cat form still cannot heavy-melee Tough Crates, so lean
    kills/off-map souls.'
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
Grey Talon:
  name: Grey Talon
  role: poke/siege carry
  archetypes:
  - poke/siege
  - gun carry
  tier: C
  trend: falling
  why: 'Sub-50% poke carry with no camp or crate route: Steam Vents give divers free
    invisibility onto an immobile flyer, and Healing Snacks blunt the chip he converts
    into lane leads. Air-drag and Silver''s bola are unchanged, so C holds.'
  core_items:
  - High-Velocity Rounds
  - Opening Rounds
  - Mystic Burst
  - Extra Charge
  - Long Range
  - Sharpshooter
  - Improved Spirit
  - Boundless Spirit
  - Tankbuster
  - Rapid Recharge
  build_variants:
  - "Hybrid owl (gun lane \u2192 spirit execute)"
  - Spirit charge/burst
  - Gun carry
  enabled_by:
  - Sharpshooter (weapon scaling)
  - Extra Charge + Rapid Recharge (Rain of Arrows/charge uptime)
  - long-range poke teammates (Vindicta, McGinnis)
  countered_by:
  - Lash
  - Wraith
  - Paradox
  - Haze
  - Silver (Weighted Bola anti-air)
  - air-drag slows (09-16)
  last_changed_patch: null
  notes: "Shh... This Won't Hurt a Bit. (10-20, indirect): Steam Vents give roamers\
    \ a free approach on an immobile flyer, and Healing Snacks blunt the poke he turns\
    \ into lane leads; no camp or crate route suits him.\nPaint the Town (10-16, indirect):\
    \ flyer tax unchanged (air-drag slows, Silver's Weighted Bola) and rising Lash\
    \ (36% for Grey Talon) is his worst lane \u2014 stays C.\nFlyer penalty applied\
    \ per reader correction \u2014 09-16 air-drag slow and Silver's Weighted Bola\
    \ both count against him."
  builds:
  - name: "Hybrid owl (gun lane \u2192 spirit execute)"
    damage: hybrid
    core_items:
    - High-Velocity Rounds
    - Opening Rounds
    - Mystic Burst
    - Long Range
    - Extra Charge
    - Sharpshooter
    - Improved Spirit
    - Boundless Spirit
    popularity: primary
    notes: "Opens with cheap weapon items to win lane, then stacks spirit/charge to\
      \ scale Rain of Arrows and the Guided Owl execute \u2014 the standard line,\
      \ and what vegas described."
  - name: Spirit charge/burst
    damage: spirit
    core_items:
    - Mystic Burst
    - Extra Charge
    - Improved Spirit
    - Extra Spirit
    - Compress Cooldown
    - Rapid Recharge
    - Tankbuster
    - Boundless Spirit
    popularity: secondary
    notes: "Charge-reset spam (Extra Charge, Rapid Recharge, Compress Cooldown) maximizes\
      \ Rain of Arrows/snare uptime and burst \u2014 best into grouped or tanky teams,\
      \ worst when dove."
  - name: Gun carry
    damage: gun
    core_items:
    - High-Velocity Rounds
    - Opening Rounds
    - Long Range
    - Sharpshooter
    - Swift Striker
    popularity: niche
    notes: Pure weapon scaling with no charge investment; only correct if the lane
      is free and the enemy can't close distance, which is rare at high rank.
  matchups:
    beats:
    - Warden
    - Vindicta
    - Drifter
    - Calico
    loses_to:
    - Lash
    - Wraith
    - Paradox
    - Haze
  matchup_notes: "His 'wins' are even at best \u2014 49% into Warden and Vindicta\
    \ (the latter a fellow flyer also hurt by anti-air) \u2014 while he kites melee\
    \ bruisers like Drifter/Calico with pure range. He hard-loses to mobile initiators\
    \ and closers: Lash (36%) dashes past his poke and bursts him before the Owl lands,\
    \ and Wraith/Paradox/Haze shut the same gap. Bebop sits at 46% both ways \u2014\
    \ treated as even."
  confidence: 0.55
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
  tier: B
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
Warden:
  name: Warden
  role: gun carry
  archetypes:
  - gun carry
  - late scaler
  tier: C
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
Yamato:
  name: Yamato
  role: mobile burst assassin
  archetypes:
  - mobile assassin
  - burst caster
  tier: B
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
Lash:
  name: Lash
  role: mobile initiator
  archetypes:
  - mobile assassin
  - initiator
  tier: S
  trend: rising
  why: "Highest-pick S-tier initiator: his spirit stomp core is untouched, Grapple\
    \ T3 now adds +4m jump velocity, and Steam Vents refill stamina at +150% instead\
    \ of granting a stealth approach \u2014 the dive-and-re-enter loop he wins on\
    \ got more fuel. Silver and air-drag slows remain the counter."
  core_items:
  - Mystic Burst
  - Extra Charge
  - Quicksilver Reload
  - Bullet Resist Shredder
  - Tankbuster
  - Headshot Booster
  - Recharging Rush
  - Headhunter
  - Sharpshooter
  build_variants:
  - Stomp spirit
  - Gun Lash
  - Bruiser flex
  enabled_by:
  - Ground Strike T3 scaling + per-meter damage buffs
  - Tempo meta (comeback souls gutted, early leads stick)
  - Mobility + CC kit (Grapple, Death Slam, Flog)
  - Extra Charge (near-mandatory spirit T1)
  countered_by:
  - Silver (Weighted Bola grounds/interrupts airborne engage)
  - Air-drag slows (new global slow-vs-air change)
  - 'Zone/anti-dive control: Dynamo, McGinnis, Seven'
  - Flog heal nerf + healing-item trims (Radiant Regeneration, Restorative Locket)
  last_changed_patch: Halloween 2026 + Gameplay Update
  notes: "Halloween 2026: Grapple T3 adds +4m jump velocity; Steam Vents converted\
    \ from an invisibility approach to +150% stamina regen, which feeds his dash-and-re-enter\
    \ pattern rather than the set-up gankers who used to ride vents. Spirit stomp\
    \ core untouched.\nShh... This Won't Hurt a Bit. (10-20, indirect): districts\
    \ and Steam Vents extend his dive routes beyond three lanes, and hub fights at\
    \ Bell Tower/Sunken Plaza concentrate teams into Ground Strike; objective parries\
    \ no longer reset.\nPaint the Town: no direct change; new districts/Steam Vents\
    \ extend his dive routes and the green-lane roof/tree keeps permanent lane high\
    \ ground \u2014 still S."
  builds:
  - name: Stomp spirit
    damage: spirit
    core_items:
    - Mystic Burst
    - Extra Charge
    - Quicksilver Reload
    - Bullet Resist Shredder
    - Tankbuster
    popularity: primary
    notes: "Ground-Strike spam; the 09-16 T3 scaling/per-meter buffs made this the\
      \ best Lash \u2014 dump the stomp on a grouped team, reset with Grapple."
  - name: Gun Lash
    damage: gun
    core_items:
    - Headshot Booster
    - Recharging Rush
    - Headhunter
    - Sharpshooter
    popularity: secondary
    notes: The old standard (Recharging Rush -> Headhunter); nerfed for him on 09-16
      and called 'killed' by the newest creator, yet still near half of 30-day games.
  - name: Bruiser flex
    damage: hybrid
    core_items:
    - Extra Stamina
    - Stamina Mastery
    - Siphon Bullets
    - Dispel Magic
    popularity: niche
    notes: Stamina plus late Siphon Bullets turn him into a sustained dive bruiser;
      a shared defensive layer over either damage path, not a standalone build.
  matchups:
    beats:
    - Grey Talon
    - Lady Geist
    - Paradox
    - Venator
    - Mirage
    loses_to:
    - Seven
    - Dynamo
    - McGinnis
    - Vyper
    - Paige
  matchup_notes: "Talon (64%) is his best lane \u2014 an immobile poke carry Lash\
    \ grapples onto and closes before he can kite, and Talon also eats the new air-drag/slow\
    \ change; Lady Geist (59%) is a slow bruiser with no answer to the dive. He loses\
    \ lane-to-late vs Seven (42%) and McGinnis (44%) \u2014 sustained AoE, turret/wall\
    \ zoning and stuns punish his engage \u2014 while Dynamo (44%) simply out-initiates\
    \ him in the 5v5."
  confidence: 0.6
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
  tier: B
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
Vyper:
  name: Vyper
  role: gun carry
  archetypes:
  - gun carry
  tier: B
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
  tier: C
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
  tier: A
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
Venator:
  name: Venator
  role: gun carry
  archetypes:
  - gun carry
  - tank/frontline
  tier: B
  trend: falling
  why: "Gun-bruiser whose zoning just gained a popular hard counter \u2014 Graves'\
    \ gun deletes his pre-placed traps \u2014 while permanent Bullet Resist rolls\
    \ tax his gun and spread corridors add flank angles on a slow body. He still out-tanks\
    \ fellow gun carries, but he is no longer a safe default."
  core_items:
  - Restorative Shot
  - Close Quarters
  - Monster Rounds
  - Weakening Headshot
  - Battle Vest
  - Bullet Lifesteal
  - Fleetfoot
  - Berserker
  - Extra Charge
  - Rapid Recharge
  build_variants:
  - Gun bruiser
  - Grenade pivot
  enabled_by:
  - 09-16 Ira Domini + Ricochet/Split Shot buff
  - huge HP/base stats
  - vitality items untouched this patch
  - built-in anti-heal (grenade) into a sustain/tank meta
  countered_by:
  - mobile initiators (Lash, Yamato)
  - gap-closing tanks (Abrams)
  - CC and kiting comps
  - poke that out-ranges him (Vindicta)
  last_changed_patch: Shh... This Won't Hurt a Bit.
  notes: "10-20 Shh...: Graves' gun destroys his traps \u2014 the pre-placed lane-vision/zoning\
    \ habit now has a popular counter; tier A->B. Against a Graves, hold traps for\
    \ fight setup instead of pre-placing them.\n09-16: Ira Domini now works with Ricochet/Split\
    \ Shot (3 bolts); Weakening Headshot -13->-12% nudges his lane shred relative\
    \ to buffed Hollow Point.\nTwo-build reality: gun bruiser primary (70-90% shares),\
    \ ~40% grenade pivot is the secondary late option."
  builds:
  - name: Gun bruiser
    damage: gun
    core_items:
    - Restorative Shot
    - Close Quarters
    - Monster Rounds
    - Intensifying Magazine
    - Weakening Headshot
    - Battle Vest
    - Bullet Lifesteal
    - Fleetfoot
    - Berserker
    popularity: primary
    notes: Frontline M1 build that stacks health, lifesteal and fire-rate so he can
      stand in melee range; Monster Rounds + Weakening Headshot win lane, Battle Vest/Bullet
      Lifesteal/Berserker turn him into an unkillable bruiser.
  - name: Grenade pivot
    damage: hybrid
    core_items:
    - Extra Charge
    - Spirit Resilience
    - Rapid Recharge
    popularity: secondary
    notes: Late re-buy (~20-23 min) into grenade charges and cooldown; the creators'
      anti-tank finisher that drops a Consecrating Grenade on Mid Boss/urn and shreds
      Metal Skin.
  matchups:
    beats:
    - Infernus
    - Haze
    - Wraith
    - Mo & Krill
    loses_to:
    - Abrams
    - Warden
    - Vindicta
    - Drifter
    - Lash
    - Graves
  matchup_notes: "Beats fellow gun carries by out-tanking and out-sustaining them\
    \ \u2014 Haze 48% and Wraith 47% match the reader note that he is the better pick\
    \ in that slot. Loses to gap-closing frontline CC (Abrams 38%, Lash 43%) that\
    \ locks him out of his own range. Vindicta's 39% is likely a lagging pre-patch\
    \ number \u2014 she is falling and flyers were hurt this patch."
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
    \ 0.52->0.61 pays back later) and Bookwyrm T2 trail +2s->+1s; HVR velocity 60->45\
    \ weakens her 1.2-min buy \u2014 Opening Rounds before HVR is now the safer opener,\
    \ and comeback gold blunts the lead she converts.\n10-20 Shh...: no direct change;\
    \ Healing Snacks let her lane pressure stick instead of resetting on a recall,\
    \ and lane-adjacent crate routes from ~2:30 pay the lane winner immediately \u2014\
    \ S held.\nCity Never Sleeps: no direct change; lane-adjacent crate routes and\
    \ Healing Snacks reward her lane pressure, and the contested hubs suit her carry-snowball."
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
Billy:
  name: Billy
  role: tank/frontline
  archetypes:
  - tank/frontline
  - lane bully
  tier: A
  trend: stable
  why: Lane-bully frontline whose all-in got a longer, bigger durability window (Rising
    Ram T3 +10%->+15% max HP for 16s->20s) plus a 25s Blasted cooldown, and the melee-front
    archetype is up on Torment Pulse's +4% melee resist; he still bleeds to anti-tank
    Shiv and to ranged kiting, and the new tick-soul economy trims the lane lead he
    snowballs.
  core_items:
  - Spirit Snatch
  - Stalker
  - Close Quarters
  - Monster Rounds
  - Grit
  - Spirit Shielding
  - Spirit Strike
  - Bullet Resist Shredder
  - Slowing Hex
  build_variants:
  - Melee-range hybrid bruiser
  - Spirit shred/slow bruiser
  enabled_by:
  - 09-16 tempo patch (lane leads snowball)
  - Spirit Snatch
  - untouched core tank/Vitality items
  - lane-bully meta
  - Torment Pulse +4% melee resist (AoE aura gains in exactly the corridor/melee fights
    he starts)
  - anti-tank counter Shiv hit by Radiant Regeneration's in-combat gate and Healbane
    kill-heal 275->170
  - Lifestrike melee-heal + flyer-dragging slow buff (low confidence - item sits outside
    his top-15 30-day buys)
  - Fortitude regen buff
  countered_by:
  - "anti-tank bruisers (Shiv \u2014 softened by the Radiant Regeneration trim)"
  - stacking anti-heal (multi-source Healbane, Toxic Bullets 40%)
  - kiting / sustained ranged gun (Seven; Warden's HVR velocity 60->45 and Shadow
    Weave rework make that lane softer)
  - sustain-peel (Ivy)
  last_changed_patch: Halloween 2026 + Gameplay Update
  notes: '10-30 Halloween + Gameplay Update: Rising Ram T3 +10%->+15% max HP for 16s->20s
    and Blasted 27->25s; Torment Pulse +4% melee resist plus the Radiant Regeneration/Healbane
    trims on Shiv help, but tick souls to the two poorest blunt the lane lead he converts
    and Spirit Shielding''s -3% spirit resist taxes his shred build.

    10-20 Shh...: no direct change; harder Haunt camps reward sustained frontline
    presence, but Mo & Krill still owns the front-line slot and ranged corridor clear
    beats his all-in.

    10-16 Paint the Town: no direct change; behavior-varied Haunt camps and contested
    soul sources reward sustained presence, so his lane-bully all-in fits the economy
    less.'
  builds:
  - name: Melee-range hybrid bruiser
    damage: hybrid
    core_items:
    - Close Quarters
    - Monster Rounds
    - Grit
    - Stalker
    - Spirit Snatch
    popularity: primary
    notes: Closes distance early and brawls with point-blank gun + melee, then Spirit
      Snatch (95% buy) converts lane kills into the HP buffer that lets him front-line.
  - name: Spirit shred/slow bruiser
    damage: spirit
    core_items:
    - Spirit Shielding
    - Spirit Strike
    - Bullet Resist Shredder
    - Slowing Hex
    - Spirit Snatch
    popularity: secondary
    notes: Spirit-damage variant that shreds and slows to stay glued to squishy carries;
      pick it when the enemy frontline, not their backline, is the problem.
  matchups:
    beats:
    - Dynamo
    - Bebop
    - Mina
    - Paradox
    - Pocket
    loses_to:
    - Shiv
    - Ivy
    - Warden
    - Seven
    - Vindicta
  matchup_notes: "He farms squishy, low-mobility heroes who can't escape a melee bruiser\
    \ that out-stats them \u2014 Dynamo, Bebop, Paradox, Pocket and Mina all sit at\
    \ 55-58%. He bleeds to anti-tank and sustain: Shiv's execute kit is his worst\
    \ lane (43%) and Shiv is rising, while Ivy and Warden out-sustain/out-range his\
    \ all-in (45% each) and Seven/Vindicta poke the big slow body from range (48%)."
  confidence: 0.58
  released_on: null
  provisional: false
Graves:
  name: Graves
  role: gun carry/summoner split pusher
  archetypes:
  - gun carry
  - split pusher
  - late scaler
  tier: B
  trend: stable
  why: "Trap-clearing gun carry whose ~25-minute window is now funded by the comeback\
    \ package (30% non-hero cap, tick souls to the two poorest, faster deficit secure)\
    \ and whose summoner core got faster with Echo Shard 0.5->0.2s \u2014 but move\
    \ speed 7->6.7, -4% bullet damage per boon and a slower, double-jumpable Grasping\
    \ Hands trim the kiting and poke she needs to reach it."
  core_items:
  - Restorative Shot
  - Mystic Shot
  - Extra Spirit
  - Arcane Surge
  - Improved Spirit
  - Heroic Aura
  - Toxic Bullets
  - Superior Duration
  - Echo Shard
  build_variants:
  - Summoner/cooldown spirit
  - On-hit gun
  enabled_by:
  - Jar of Dead buffs
  - health/boon buffs (33->35)
  - stall supports (Kelvin, Ivy)
  - late-game scaling
  - Venator in the lobby (gun deletes his traps)
  countered_by:
  - mobile assassins (Holliday, Lash, Yamato, Mina, Calico, Drifter)
  - dive
  - out-scaling gun carries (Haze, Silver, Wraith, Warden)
  - slows
  - anti-gun-carry defences (Bullet Resilience 30->35%, Return Fire's now-visible
    10% bullet resist)
  - Barrel Mimics (crate chains while low HP)
  last_changed_patch: Halloween 2026 + Gameplay Update
  notes: "10-30 Halloween + Gameplay Update: direct nerfs parsed \u2014 move speed\
    \ 7->6.7, bullet damage per boon -4%, Grasping Hands deploy 0.6->0.8s and easier\
    \ to double-jump, Borrowed Decree spawn-time cut moved T2->T3. Offsets: Echo Shard\
    \ post-cast 0.5->0.2s for the summoner core and the comeback package funding her\
    \ ~25-min window. Tier B held, trend rising -> stable; the 56.5%/40.9% snapshot\
    \ still conflicts with the KB's 48.5%/21% and needs a recheck.\n10-20 Shh...:\
    \ tier C->B, trend rising \u2014 trap-clearing into Venator is a real draft lever,\
    \ but Barrel Mimics punish her low-HP, two-stamina crate chains and the corridor\
    \ economy still taxes her scaling window.\n10-16 Paint the Town: her gun destroys\
    \ Venator's traps - genuine utility into an A-tier hero - but the earlier, contested\
    \ soul economy still deletes her ~25-min scaling line."
  builds:
  - name: Summoner/cooldown spirit
    damage: spirit
    core_items:
    - Extra Spirit
    - Arcane Surge
    - Improved Spirit
    - Echo Shard
    - Superior Duration
    popularity: primary
    notes: Cooldown/duration stack (Echo Shard + Superior Duration + Arcane Surge)
      to spam Jar of Dead summons and Grasping Hands; the most-bought cluster and
      why she is not a pure gun hero.
  - name: On-hit gun
    damage: gun
    core_items:
    - Restorative Shot
    - Mystic Shot
    - Heroic Aura
    - Toxic Bullets
    popularity: secondary
    notes: Lane-sustain into sustained on-hit; Heroic Aura's fire-rate aura plus Toxic
      Bullets vs tanks, but she lacks the scaling to out-carry a real gun carry.
  matchups:
    beats:
    - Paradox
    - Bebop
    - Venator
    loses_to:
    - Warden
    - Wraith
    - Calico
  matchup_notes: "Beats Paradox (53%) and Bebop (52%): both stand still to channel\
    \ or duel, so Grasping Hands and summon pressure land easily. Loses to Warden\
    \ (42%) and Wraith (44%) \u2014 gun carries that out-range and out-scale her,\
    \ Warden's Binding Word pinning her immobile frame. Calico/Lash/Drifter are near-even\
    \ but all mobile dive, so they reach her before she scales."
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
Rem:
  name: Rem
  role: support/healer
  archetypes:
  - support/healer
  tier: B
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
Silver:
  name: Silver
  role: gun tank carry
  archetypes:
  - gun carry
  - tank/frontline
  tier: A
  trend: stable
  why: Front-line gun tank still carried by tempo and Weighted Bola anti-air, but
    Hunter's Aura now needs line of sight and Spirit Shielding lost 3% resist, so
    her clumped-fight shred and defensive layer are both thinner; Point Blank is now
    a real damage slot because Go For The Throat counts it.
  core_items:
  - Restorative Shot
  - Melee Lifesteal
  - Stalker
  - Grit
  - Point Blank
  - Hunter's Aura
  - Spirit Shielding
  - Cold Front
  - Slowing Hex
  - Mystic Burst
  - Tankbuster
  - Unstoppable
  build_variants:
  - Gun tank
  - Utility/anti-CC bruiser
  enabled_by:
  - frontline/tank archetype up (Heavy-Melee Cauldrons, Healing Snacks 10->14%)
  - Weighted Bola grounded interrupt (anti-air)
  - gun-cycle smoothing (dash/light melee don't break cycle)
  - health/boon and sprint buffs
  - front-line initiators who start fights for her (Dynamo, Apollo, Lash)
  countered_by:
  - CC/debuff spam (Mo & Krill, Bebop, Paradox, The Doorman)
  - kiting and slows
  - anti-heal stacking (Decay -55%, Toxic Bullets 40%, Healbane) vs her Melee Lifesteal/Restorative
    Shot sustain
  - anti-tank bruisers (Shiv) and enemy Tankbuster buyers
  - Hunter's Aura no longer shreds through walls; Spirit Shielding 18->15%
  - matches up badly vs Lash and Drifter
  last_changed_patch: Halloween 2026 + Gameplay Update
  notes: '10-30 Halloween + Gameplay Update: S -> A. Hunter''s Aura now requires line
    of sight (no through-wall shred) and Spirit Shielding 18->15% trim her core slots;
    anti-heal stacking attacks her Melee Lifesteal/Restorative Shot. Offsets: Go For
    The Throat now counts Point Blank/Opening Rounds, Point Blank slow 2->2.5s, Bola
    grounding fixes, and Rat King''s nerf eases her worst matchup.

    10-16 Paint the Town: no direct change; the contested, earlier soul economy rewards
    her front-line tempo and Weighted Bola anti-air, so tier S holds.

    09-29 City Never Sleeps: no direct change; the frontline/tank archetype is up,
    but the move from lane tempo to farm-route tempo is roughly neutral for a lane-fight
    gun tank, and heavy-melee crate routes need a heavy melee she does not build toward
    (peercontent, low confidence).'
  builds:
  - name: Gun tank
    damage: gun
    core_items:
    - Restorative Shot
    - Melee Lifesteal
    - Stalker
    - Grit
    - Point Blank
    - Hunter's Aura
    - Spirit Shielding
    popularity: primary
    notes: "The default shell \u2014 lane-sustain bruiser (97% Stalker, 96% Melee\
      \ Lifesteal, 90% Restorative Shot) that scales into a front-line DPS tank. Point\
      \ Blank is now a core slot: its slow extends to 2.5s and its weapon damage feeds\
      \ Go For The Throat. Delay Hunter's Aura \u2014 it no longer shreds through\
      \ walls, so it is an LOS-fight item only."
  - name: Utility/anti-CC bruiser
    damage: hybrid
    core_items:
    - Cold Front
    - Slowing Hex
    - Mystic Burst
    - Tankbuster
    - Unstoppable
    popularity: secondary
    notes: "Splashes spirit chip and CC between gun cycles and stacks anti-CC when\
      \ you must survive the frontline \u2014 Unstoppable (42% share, 49.5% WR) and\
      \ Debuff Reducer are the highest-WR items on her."
  matchups:
    beats: []
    loses_to:
    - Lash
    - Drifter
  matchup_notes: "The only two qualified pairs are both 45% \u2014 Lash and Drifter,\
    \ mobile melee bruisers who can stick to her and out-trade; Silver has no positive\
    \ matchup with enough games. That is a ceiling note, not a floor: she wins through\
    \ tempo and pick pressure (15.1% PR) rather than countering specific heroes. Weighted\
    \ Bola's ground/interrupt should now help her against flyers (Vindicta, Grey Talon),\
    \ but that is inference, not data."
  confidence: 0.62
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
  tier: A
  trend: falling
  why: Still a 116-heavy-melee frontline who opens Tough Crates and wants the forced
    hub fights, but Scrap Grenade's radius (8m->6m, large 14m->10m) and the banner
    ult's knockup/radius/duration cuts end his one-button camp clear and his teamfight
    reset, right as Haunt camps gained +10% HP.
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
    T3 300->275), radius 8m->6m / large 14m->10m, fuse +0.1s; Rule, Ratannia! knockup
    halved, 160->180s, 20m->16m, 12s->9s and now goes on cooldown if he is stunned
    before placing; base bullet -5% and growth -20%. Haunt camps +10% HP finish the
    one-button clear. Offsets: Heavy-Melee Cauldrons, Healing Snacks 10->14%.

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
      \ the work. Scrap Grenade is no longer a one-button camp clear (radius 8m->6m,\
      \ large 14m->10m, fuse +0.1s): pull camps with melee first, then grenade the\
      \ clump."
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
  tier: D
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
  tier: C
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
  tier: C
  trend: stable
  why: 'Spirit mark-burster whose dive got taxed twice: slows now cut jetpack impulse
    and Steam Vents lost invisibility, so the free approach and the escape are both
    gone; the Close The Deal damage fix is the only gain on a 730-HP flyer with the
    air-drag tax intact.'
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
    \ jetpack unusable while cursed, CDR per boon -0.4->-0.25s, T3 refund 50->30%,\
    \ slows now cut jetpack impulse harder (worse under movement-ability silence),\
    \ grounding pulls land more reliably. Steam Vents lose invisibility and HVR 60->45%\
    \ velocity hits his lone weapon staple; the Close The Deal damage fix is the only\
    \ gain. C held, trend rising -> stable.\n7-day check-in (2026-10-20): tier C ->\
    \ C, WR 45%, PR 69% over 446352 matches. Corrected: the usage data kills the 'shred/mark\
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
  tier: C
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
    \ 6->5s duration, 0.04->0.01 scaling, ends on death, 0.5->0.75s re-apply and T3\
    \ ink destructible again; Still Life stun 1.0->0.9s, LOS required at channel end,\
    \ T1 regen only while drawing (0.25->0.15). Spirit Lifesteal 6->8 spirit / 13->15%\
    \ is the replacement sustain; anti-heal stacking taxes the rest.\n7-day check-in\
    \ (2026-10-23): tier B -> C, WR 50%, PR 64% over 539876 matches. Data corrects\
    \ the day-0 read: B/rising was a tooltip judgment, so C is a correction, not a\
    \ decline \u2014 46.1% WR at 70.9% PR, and she loses to frontline brawlers rather\
    \ than punishing melee. Watch whether her WR climbs with reps; the tooltip read\
    \ also claimed Seven and the gun line as wins, but Seven is 49% over 170 and Living\
    \ Ink/HVR no longer appear in her item data at all. 10-20 Shh...: no Violet changes;\
    \ her position moves on systems (Haunt grouping, Tough Crates, hub fights) and\
    \ on the dive/frontline meta around her."
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
  tier: B
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
    \ duration 7->5s (T3 +3->+2s), T3 immunity -> 50% damage reduction, no fear from\
    \ >50\xB0 above/below the target's view; base gun damage -10%, Healing Needles\
    \ 25->22 (T2 +20->+16) but spirit scaling 0.2->0.24; Leech Therapy ground leeches\
    \ 180s -> 120s + 3s/min and cleared on round reset. Anti-heal buffs land on a\
    \ dedicated healer. B held, trend stable -> falling.\n7-day check-in (2026-10-27):\
    \ tier B -> B, WR 51%, PR 63% over 607252 matches. Data overrides the day-0 read:\
    \ Swift Striker, High-Velocity Rounds and Active Reload show no meaningful share\
    \ (Titanic Magazine is the weapon core at 98% / 6.7m), and the 7-day spread contains\
    \ none of the dash assassins the fear-cone thesis predicted. Extra Regen is not\
    \ the trap the previous note called it \u2014 97% at 2.1m with a baseline win\
    \ rate makes it a mandatory lane tax for 0 base regen, indifferent rather than\
    \ informative. Changelog: released 2026-10-20 in Shh... This Won't Hurt a Bit.,\
    \ first full-week check (7.3k matches, no creator content); nearly every item\
    \ WR sits at 50.5-51%, so build-level signals are weak and confidence is capped."
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


## Win/pick-rate snapshot (last 14 days before this patch, ranked matches, high-rank filter)

hero | WR% | PR% | matches
Graves | 57.4 | 44.1 | 1126713
Paige | 55.6 | 27.7 | 709176
Rat King | 55.2 | 51.9 | 1327715
Seven | 54.6 | 32.4 | 827738
Baba | 54.3 | 13.9 | 356149
Victor | 54.3 | 32.7 | 835914
Kelvin | 54.2 | 13.4 | 342986
Haze | 53.3 | 44.3 | 1131130
Ivy | 52.5 | 19.3 | 492060
Deadman Danny | 52.4 | 39.8 | 1016075
Abrams | 52.3 | 31.2 | 798245
Lady Geist | 51.7 | 23.8 | 609127
Dynamo | 51.7 | 21.0 | 537294
Nurse Harrow | 51.4 | 47.0 | 1201479
Violet | 50.9 | 35.9 | 916926
Drifter | 50.7 | 39.3 | 1003788
Lash | 50.6 | 30.7 | 783656
Wraith | 50.5 | 35.4 | 904704
Mo & Krill | 49.7 | 19.4 | 496799
McGinnis | 49.3 | 12.5 | 320328
Vindicta | 49.2 | 30.0 | 765788
Infernus | 49.2 | 36.8 | 941194
Warden | 49.2 | 14.9 | 381586
Apollo | 49.0 | 27.7 | 707096
Billy | 48.8 | 32.9 | 840777
Bebop | 48.4 | 37.7 | 963219
Celeste | 48.2 | 33.7 | 862010
Calico | 48.1 | 15.1 | 386120
Grey Talon | 47.4 | 17.9 | 456777
Yamato | 47.2 | 27.8 | 711320
Holliday | 47.1 | 19.7 | 504171
Venator | 46.7 | 41.6 | 1062166
Solomon | 46.5 | 15.0 | 383823
Silver | 46.2 | 31.5 | 805935
Paradox | 46.1 | 25.0 | 638146
Vyper | 46.1 | 14.1 | 361629
Viscous | 46.0 | 12.8 | 326435
The Doorman | 45.6 | 15.1 | 385544
Rem | 45.2 | 30.7 | 784289
Shiv | 45.0 | 27.6 | 706081
Mina | 44.7 | 37.6 | 960007
Sinclair | 44.7 | 10.0 | 255986
Pocket | 44.3 | 17.1 | 437041
Mirage | 44.1 | 11.9 | 305042

## Heroes to analyze in this call

Silver, Celeste, Rat King, Baba, Solomon, Deadman Danny, Violet, Nurse Harrow

## What to do

Produce an entry for **each hero listed above, and only those heroes**. For each hero combine:

- direct changes (kit, stats, talents) and their magnitude relative to how the hero is actually played (a nerf to an ability nobody maxes is minor);
- indirect effects from the item analysis (core items buffed/nerfed, build paths changed) and from the systems analysis (archetype up/down, tempo shift);
- the prior state: tier, trend, win rate. A hero at 54%+ win rate absorbing a moderate nerf is likely still strong; a hero at 47% taking the same nerf drops out.
- **cross-hero effects**: changes to *other* heroes matter. If a hero who counters this one (see `matchups.loses_to`, `countered_by`) got stronger or gained a tool that specifically punishes this hero (anti-air, anti-heal, silence, grounding), that is an indirect nerf; if a counter got weaker, an indirect buff. Name the other hero and the mechanic.
- **builds, not just kits**: judge a change against the hero's actual `builds` (gun vs spirit, primary vs niche). A nerf to an item only the niche build buys is minor; a nerf to the primary build's core item is not.
- **map and objectives**: for content/map updates, judge how the kit interacts with the new soul sources and fight locations (camp clear speed and AoE vs grouped Haunts, heavy melee for Tough Crates, mobility between districts, verticality for Bell Tower, stamina for Sunken Plaza, sustain vs harder camps, invisibility/vision for Steam Vents, split-push vs more spread-out objectives).

New heroes listed under direct changes but absent from the knowledge base: include them with `tier_before` "?", `in_notes` true, low `confidence`, and say the read is provisional.

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


## Creator sources published after this patch (optional corroboration; the notes, KB and snapshot remain primary — if a source contradicts them, say so and keep your own read)

(none)

For heroes with nothing relevant (no direct changes, no affected core items, archetype neutral) set direction "neutral", magnitude "none", and keep reasons empty. Do not pad.

`tier_after` is your call on the post-patch tier (S/A/B/C/D); keep `tier_before` from the KB (use "?" if unknown). Only move a tier when the reasons justify it. `confidence` reflects how sure you are about the direction, 0-1.

`verdict` answers one question for every hero: should someone who plays this hero keep playing them after this patch?

- `keep`: still a good pick; direct + indirect effects are neutral or positive, or negative but minor relative to the hero's standing.
- `watch`: real change in either direction whose size is uncertain; play but adapt (usually a build or timing change).
- `bench`: the hero lost what made them good (core build gutted, archetype hard-countered by a systems change, major kit nerf on a hero that was not over-performing).

## Change rows

`rows` is a list of scannable one-line changes for a phone screen. Give rows for **every hero with direct changes**; leave it empty for heroes without.

- `label`: 1-3 plain words naming what changed ("Channel time", "T3", "New interrupts", "Teamplay").
- Prefer `old` + `new` when the note gives before/after values; otherwise `text` of at most 8 words. Never both.
- `effect`: judged for the player of this hero: "good", "bad", or "neutral". A longer channel time is bad.
- `ability`: the exact ability name when the change applies to one.
- Merge lines that say the same thing. Keep every gameplay-relevant change. Never add anything not in the notes; every number in a row must come from the notes verbatim.

Example (Mirage's Traveler):

```json
{"label": "Channel time", "old": "2s", "new": "3s", "effect": "bad", "ability": "Traveler"}
{"label": "T3", "old": "-90s cooldown", "new": "Damage can't interrupt it", "effect": "good", "ability": "Traveler"}
{"label": "Base ability", "text": "Now includes a barrier (no scaling)", "effect": "good", "ability": "Traveler"}
```

## Reporting what the notes did

`change_kind` and `change_size` describe **only the hero's own note lines**, never items, systems or the meta. Those belong in `direction`, `indirect_reasons`, `tier_after` and `verdict`.

- `buff`: the lines clearly make the hero stronger. `nerf`: clearly weaker. `none`: no direct lines.
- `rework`: an ability works differently, not just with different numbers. Crowd control changing type, a talent swapped for a different effect, or a new or removed mechanic is a rework even when numbers around it improve.
- `adjusted`: trade-offs that roughly cancel, or only bug fixes.

Judge mechanical changes by what the ability **can no longer do**. A stun becoming an immobilize loses the stun's ability to interrupt channels, so that row is `bad` and it leads the `one_liner`, however good the longer duration looks. Never call a hero buffed while a core mechanic was taken away.

The `one_liner` leads with the biggest direct change. Any claim from items or systems names its cause. Do not state facts absent from the notes, the knowledge base or the corrections. A bug fix is `neutral` and labelled as a fix unless it clearly helps or hurts.

## Output schema

{
  "heroes": [
    {
      "hero": "hero name exactly as in the knowledge base",
      "in_notes": true,
      "direction": "up|down|neutral",
      "magnitude": "none|minor|moderate|major",
      "confidence": 0.0,
      "direct_reasons": ["1 short sentence per driving change, name the stat"],
      "indirect_reasons": ["1 short sentence per item/system driver, name the item or system"],
      "build_changes": ["concrete build advice: swap X for Y, delay Z, new core W; empty if none"],
      "tier_before": "S|A|B|C|D|?",
      "tier_after": "S|A|B|C|D",
      "one_liner": "<= 20 words a player would actually say about this hero after the patch",
      "verdict": "keep|watch|bench",
      "change_kind": "buff|nerf|rework|adjusted|none",
      "change_size": "none|minor|moderate|major",
      "rows": [{"label": "1-3 words", "old": "before", "new": "after", "effect": "good|bad|neutral", "ability": "optional exact name"}]
    }
  ]
}
