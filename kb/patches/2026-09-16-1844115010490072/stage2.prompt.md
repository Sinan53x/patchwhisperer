# Task: item analysis

Patch: Minor Update - 09-16-2026 (2026-09-16)

## Systems analysis of this patch (already done)

{
 "systems_changed": [
  {
   "system": "comeback economy",
   "change_summary": "The flat 'behind on net worth' bonus souls are removed from hero-kill and Rift bounties, comeback bounties are trimmed in general, and 70% of the removed value is rerouted through tick gold to the two lowest-net-worth players. Losing lane no longer prints a lump of catch-up souls when you land a kill.",
   "driving_changes": [
    "Removed a fixed amount of extra bonus souls you would get for being behind even a very slightly amount in net worth for both hero kill bounties as well as Unstable Rift bounties",
    "Slightly reduced comeback bounties in general",
    "A portion of the comeback souls earned by players above enemy teams average net worth is instead distributed via the tick gold system that is given to the lowest 2 players (70% of the extra comeback value goes to them)"
   ],
   "magnitude": "major",
   "effect_on_play": "Comebacks now come from sustained econ trickle to the genuinely poor, not from one lucky kill on the fed enemy. Being ahead is stickier; a single teamfight can no longer flip a 15k deficit."
  },
  {
   "system": "objective bounties",
   "change_summary": "Guardian bounty +10% and Walker bounty +5%, but the share that goes to nearby heroes drops from 30% to 25% (rest split across all six players). Objectives are worth more overall, but the individual who last-hits or sits on them pockets less.",
   "driving_changes": [
    "Guardian bounty increased by 10%",
    "Walker bounty increased by 5%",
    "Share for objectives bounty to nearby heroes reduced from 30% to 25% (the remaining gets split between all 6 players)"
   ],
   "magnitude": "moderate",
   "effect_on_play": "Taking structures is still the primary snowball engine and now pays the whole team a bit more, which rewards coordinated early pushes and discourages the solo split-pusher farming a lane of towers alone."
  },
  {
   "system": "respawn timers",
   "change_summary": "Respawn at 20 minutes rises 35s->38s (late-game max values unchanged). Deaths in the mid-game window cost more map time.",
   "driving_changes": [
    "Respawn Time at 20 minutes increased from 35s to 38s (does not affect the max values later on, just a little higher earlier)"
   ],
   "magnitude": "minor",
   "effect_on_play": "Small but in the same direction as the economy changes: a mid-game pick converts into a real objective window, so aggressive tempo teams profit more from kills than from farming."
  },
  {
   "system": "parry / reload / gun-cycle",
   "change_summary": "Parry now pauses reload instead of resetting it, and parrying mid-dash cancels the dash and momentum to parry on the spot; stuns pause reload rather than restarting it; dashes and light melee no longer pause gun cycle time.",
   "driving_changes": [
    "Using parry now pauses reloading",
    "Parrying while doing a regular dash will now cancel the dash (and momentum) and parry on the spot",
    "Getting stunned now pauses your reload rather than restarting it",
    "Dashes and light melee's no longer pause your gun's cycle time (this is a general change that affects high-cycle time weapons the most like Silver or Abrams)"
   ],
   "magnitude": "moderate",
   "effect_on_play": "Net gun-DPS goes up for everyone but disproportionately for high-cycle-time weapons that weave dashes/melee between shots. Defensive parry is smoother but the dash-cancel is a small mobility tax on reactive parries; overall this raises sustained gun-carry output in skirmishes."
  },
  {
   "system": "movement / slows",
   "change_summary": "Every move slow cut ~20% and ground-dash slows cut ~10%, but slows now apply 35% of their value to air drag. Kiting is easier on the ground; flyers get dragged out of the sky.",
   "driving_changes": [
    "All move slow values reduced by ~20% globally",
    "All ground dash slows reduced by ~10% globally",
    "Slows now also affect air drag by 35% of the slow value (convar citadel_enable_slows_affect_air_drag to toggle the slow drag behavior on and off)"
   ],
   "magnitude": "moderate",
   "effect_on_play": "Ground chases and escapes are more survivable, so slow-as-utility (Slowing Hex, Bola-style effects) loses some raw lockdown but gains a new anti-air use. Flyers and anyone reliant on air mobility are hit by an entirely new penalty vector."
  },
  {
   "system": "map / neutral economy",
   "change_summary": "Underground-tunnel breakables spawn at 5m instead of 3m and respawn at 5m instead of 3m. The early 'free farm' window in the tunnels is pushed back and thins out.",
   "driving_changes": [
    "Breakables in the underground tunnels initial spawn time increased from 3m to 5m",
    "Breakables in the underground tunnels respawn rate increased from 3m to 5m"
   ],
   "magnitude": "minor",
   "effect_on_play": "Slightly less early neutral souls available, which tightens the early econ curve and further discourages passive farm-heavy openings in favor of lane pressure."
  }
 ],
 "tempo_shift": {
  "direction": "toward_tempo",
  "confidence": 0.92,
  "why": "Every systems lever points one way: comeback souls removed, objective bounties up, respawns longer, and early neutral farm delayed, so winning lane and converting kills into structures is now the dominant path. The Rift resist curve (10% +1%/min) makes early Rift fights real fights rather than a scaled comeback button."
 },
 "archetype_effects": [
  {
   "archetype": "gun carry",
   "direction": "up",
   "magnitude": "moderate",
   "why": "Dashes/light melee no longer pause gun cycle time and stuns/parry pause rather than reset reload, raising sustained weapon DPS, most for high-cycle-time guns (Silver, Abrams)."
  },
  {
   "archetype": "late scaler",
   "direction": "down",
   "magnitude": "major",
   "why": "Comeback souls gutted plus lower early Rift resist and higher mid-game respawns remove the safety net that let farm-heavy scalers stall into a flip."
  },
  {
   "archetype": "mobile assassin",
   "direction": "up",
   "magnitude": "moderate",
   "why": "Tempo shift rewards early kills and picks, and the global slow reduction eases ground chases and escapes, though new air-drag slows punish air-entry versions."
  },
  {
   "archetype": "lane bully",
   "direction": "up",
   "magnitude": "moderate",
   "why": "Removed comeback bounties and delayed tunnel farm mean a won lane keeps its lead instead of feeding the enemy a catch-up payout."
  },
  {
   "archetype": "split pusher",
   "direction": "neutral",
   "magnitude": "minor",
   "why": "Objective bounties are up but the nearby-hero share fell 30%->25%, so tower-taking pays the team more but the solo pusher personally less; roughly a wash."
  },
  {
   "archetype": "poke/siege",
   "direction": "down",
   "magnitude": "moderate",
   "why": "Slows now affect air drag by 35%, creating a new anti-air penalty for flyers and airborne poke that ground-based poking doesn't face."
  },
  {
   "archetype": "tank/frontline",
   "direction": "up",
   "magnitude": "minor",
   "why": "Global slow reduction plus longer enemy respawns make diving and holding space more rewarding, and tanks are the natural buyers of the strong objective-push timing."
  },
  {
   "archetype": "burst caster",
   "direction": "neutral",
   "magnitude": "minor",
   "why": "Parry pausing reload and the dash-cancel give reactive defense a small edge against burst windows, offset by new anti-air slow utility; net roughly flat."
  },
  {
   "archetype": "spirit carry",
   "direction": "down",
   "magnitude": "minor",
   "why": "Spirit carries are typically scaling-oriented and lose the comeback and Rift-safety levers the patch removed, in line with the general anti-scaling tilt."
  },
  {
   "archetype": "initiator",
   "direction": "up",
   "magnitude": "minor",
   "why": "Respawn at 20m up to 38s and stronger objective bounties mean a good engage converts into a longer, more valuable map-time swing."
  },
  {
   "archetype": "support/healer",
   "direction": "neutral",
   "magnitude": "minor",
   "why": "No direct systems lever here beyond the tempo shift; the healing-item trims are item-side and out of scope for this systems read."
  }
 ],
 "intent_read": "Valve is deliberately deleting the comeback lever that made losing lane recoverable, tightening early econ (tunnel breakables, Rift resist) and paying teams for structures so that the player who wins the early game actually wins the game. The reload/parry/gun-cycle smoothing and the air-drag slow look like they're separately modernizing combat feel and clipping flyers, but both feed the same tempo-first direction."
}

## Item changes in this patch (grouped by item)

Weakening Headshot:
  - [nerf] Weakening Headshot: Bullet Resist Reduction reduced from -13% to -12%
Hollow Point:
  - [buff] Hollow Point: Bullet Resist Reduction increased from 9% to 10%
Toxic Bullets:
  - [buff] Toxic Bullets: Spirit scaling increased from 0.005% to 0.006%
Shadow Weave:
  - [rework] Shadow Weave: Now builds from Sprint Boots
  - [buff] Shadow Weave: Sprint speed increased from 1.5 to 2
  - [buff] Shadow Weave: Cooldown reduced from 45s to 37s
Cultist Sacrifice:
  - [nerf] Cultist Sacrifice: Bounty reduced from 180% to 170%
Ballistic Enchantment:
  - [buff] Ballistic Enchantment: Duration increased from 14s to 20s
Spiritual Overflow:
  - [neutral] Spiritual Overflow: Buildup is 35% slower
  - [nerf] Spiritual Overflow: Spirit Power on proc reduced from 40 to 30
  - [nerf] Spiritual Overflow: Fire Rate reduced from 30% to 25%
Restorative Locket:
  - [nerf] Restorative Locket: Heal per boon reduced from 0.5 to 0.45
  - [nerf] Restorative Locket: Stack range reduced from 35m to 32m
Trophy Collector:
  - [nerf] Trophy Collector: Souls per minute reduced from 18 to 16
Veil Walker:
  - [rework] Veil Walker: No longer builds from Sprint Boots
  - [rework] Veil Walker: No longer grants +2 Sprint and +2 Out of Combat Regen (due to loss of component)
  - [rework] Veil Walker: Movement speed bonus is now removed when the invisibility is removed
  - [nerf] Veil Walker: Spirit Power reduced from 10 to 6
Fortitude:
  - [buff] Fortitude: Max Health regen increased from 2% to 2.25%
Lifestrike:
  - [buff] Lifestrike: Heal on Melee hit increased from 100+1.5 to 120+1.75
  - [buff] Lifestrike: Melee hit heal increased from 30% to 35%
Leech:
  - [buff] Leech: Bullet and Spirit Lifesteal increased from 25% to 28%
Plated Armor:
  - [fix] Plated Armor: Fixed on-hit damage prevention not blocking the following on-hit spirit damage effects: Mercurial Magnum, Vindicta's Flight, Wraith's Full Auto, and Tesla Bullets/Capacitor
Diviner's Kevlar:
  - [rework] Diviner's Kevlar: Now grants +10% Ultimate Ability Cooldown Reduction
Golden Goose Egg:
  - [nerf] Golden Goose Egg: Damage Penalty increased from -10% to -15%
  - [rework] Golden Goose Egg: Stored souls now count towards net worth (affects comeback reward calculations)
  - [nerf] Golden Goose Egg: Souls per minute reduced from 90 to 80
Slowing Hex:
  - [nerf] Slowing Hex: Cooldown increased from 27s to 29s
Radiant Regeneration:
  - [nerf] Radiant Regeneration: Healing on Ability Cast per boon scaling reduced from 2 to 1.7
Tankbuster:
  - [nerf] Tankbuster: Current Health Bonus damage reduced from 8% to 7.5%
Decay:
  - [neutral] Decay: DPS reduced by 25%
  - [buff] Decay: Duration increased by 20%
Mercurial Magnum:
  - [nerf] Mercurial Magnum: Base bullet damage scaling reduced from 0.49 to 0.38
  - [nerf] Mercurial Magnum: Base bullet damage reduced from 25% to 20%
Focus Lens:
  - [buff] Focus Lens: Damage increased from 30% to 35%
  - [buff] Focus Lens: Cast range increased from 20m to 25m

## Knowledge base: the changed items (who buys them and why)

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


## Knowledge base: heroes whose core_items or build_variants include a changed item

Infernus:
  name: Infernus
  role: gun carry
  archetypes:
  - gun carry
  - late scaler
  tier: B
  trend: stable
  why: Balanced staple whose low HP is by design; the 09-16 Toxic Bullets scaling
    buff helps his burn but the tempo meta out-paces his scaling, hence a flat 47.7%
    WR.
  core_items:
  - Toxic Bullets
  - Fortitude
  - Bullet Lifesteal
  - Decay
  build_variants:
  - gun build
  - burn build
  enabled_by:
  - Toxic Bullets scaling buff
  - Dispel Magic being a rare buy
  countered_by:
  - Dispel Magic
  - Decay
  - high-tempo divers
  last_changed_patch: null
  notes: 'No 09-16 line. Older creator read: healthy kit that should not be buffed,
    others should come down.'
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
McGinnis:
  name: McGinnis
  role: poke/siege controller
  archetypes:
  - poke/siege
  - tank/frontline
  tier: B
  trend: stable
  why: 'Coin-flip hero: 08-12 gave turrets more HP and reworked Medicinal Specter''s
    resist, but her wall/turret kit is weak into the mobile AoE comps the tempo meta
    favors.'
  core_items:
  - Heroic Aura
  - Fortitude
  - Superior Duration
  build_variants:
  - turret build
  - AoE support build
  enabled_by:
  - turret HP buffs
  - Medicinal Specter resist
  countered_by:
  - mobile/AoE comps
  - wall-jumpers
  last_changed_patch: Minor Update - 08-12-2026
  notes: 'Creator: strong but inconsistent, never felt like she belongs.'
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
Kelvin:
  name: Kelvin
  role: support/healer
  archetypes:
  - support/healer
  - late scaler
  tier: B
  trend: rising
  why: Frozen Shelter now scales its innate regen with spirit power, so he is useful
    without maxing the dome; still a late-scaling healer, but the tempo patch gives
    his low-cost heals more early relevance.
  core_items:
  - Radiant Regeneration
  - Healing Nova
  - Healbane
  - Fortitude
  build_variants:
  - dome build
  - heal support build
  enabled_by:
  - Frozen Shelter scaling
  - 09-16 ability change
  countered_by:
  - anti-heal stacking
  - burst through dome
  last_changed_patch: Minor Update - 09-16-2026
  notes: Radiant Regeneration nerfs (08-22, 09-16) softly tax his item path.
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
Victor:
  name: Victor
  role: tank/frontline
  archetypes:
  - tank/frontline
  - late scaler
  tier: B
  trend: stable
  why: Balanced tank others should match; only ruined by Refresher/Echo Shard, and
    the tempo patch neither helped nor hurt his fast farm and solo-Walker snowball.
  core_items:
  - Refresher
  - Echo Shard
  - Fortitude
  build_variants:
  - tank build
  - Refresher initiator build
  enabled_by:
  - fast tank farm
  - Refresher ult
  countered_by:
  - burst (only burstable tank)
  - CC
  last_changed_patch: Minor Update - 07-09-2026
  notes: 'Creator: the power level other heroes should be brought down to.'
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
The Doorman:
  name: The Doorman
  role: utility initiator
  archetypes:
  - initiator
  - burst caster
  tier: B
  trend: falling
  why: Still an overloaded utility kit with the best door (a real answer to Silver),
    but the 08-12 Doorway range cut (70->65m) and a 46.3% WR on 12.7% pick rate say
    high-rank players stopped trusting him into the tempo meta.
  core_items:
  - Echo Shard
  - Superior Cooldown
  - Fortitude
  build_variants:
  - bells carry build
  - utility build
  enabled_by:
  - door/kidnap utility
  - good vs Silver
  countered_by:
  - tempo comps
  - range cut
  last_changed_patch: Minor Update - 08-12-2026
  notes: Long the top S-tier in creator reads; now mid at high rank.
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
Rem:
  name: Rem
  role: support/healer
  archetypes:
  - support/healer
  tier: B
  trend: stable
  why: The tank-enabling healer is unchanged after July's breakable/bug tweaks, which
    the creator says is not the big nerf people assume; still valuable but less mandatory
    as the meta moves from deathball tanks to tempo.
  core_items:
  - Decay
  - Divine Barrier
  - Healing Nova
  build_variants:
  - heal support build
  enabled_by:
  - percent-max-HP heal
  - cleanse
  countered_by:
  - anti-heal
  - tempo picks
  last_changed_patch: Minor Update - 09-16-2026
  notes: 09-16 change is a bug fix + target UI only; effect on strength is minor.
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


## What to do

For each changed item, decide the net direction and magnitude, then trace the consequence to heroes: who has it as a core slot, who used it situationally, and who might now pick it up. Note build-path changes (component changes, slot moves, what it now competes with). Think about the systems context: an item that was good because of the old economy may be worse even if its numbers went up, and vice versa.

Group multiple lines for the same item into one entry. Skip pure bug fixes unless the fix meaningfully changes an interaction (then say which heroes it affects).

Magnitude guide: minor = tuning that will not change who buys it; moderate = changes timing or priority in builds; major = adds or removes the item from core builds, or changes what it does.

## Output schema

{
  "items": [
    {
      "item": "canonical item name",
      "direction": "buff|nerf|rework|neutral",
      "magnitude": "minor|moderate|major",
      "summary": "1-2 sentences of consequence, not restatement",
      "affected_heroes": [
        {"hero": "hero name", "relationship": "core|situational|new_option", "effect": "up|down|neutral", "why": "1 sentence"}
      ],
      "build_shift": "optional 1 sentence on component/slot/competition changes, or empty string"
    }
  ],
  "notable_item_stories": ["0-3 one-sentence cross-item stories, e.g. 'invisibility items were buffed together, expect Shadow Weave on more gun carries'"]
}
