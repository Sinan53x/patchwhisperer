# Task: item analysis

Patch: Halloween 2026 + Gameplay Update (2026-10-30)

## Systems analysis of this patch (already done)

{
 "systems_changed": [
  {
   "system": "Jungle / Haunt camps (economy + difficulty)",
   "change_summary": "Haunt base bounty and growth rise 10% while Haunt HP and damage also rise 10%, making camps both richer and more punishing to clear.",
   "driving_changes": [
    "Haunts base bounty and growth increased by 10%",
    "Haunts HP and Damage output increased by 10%"
   ],
   "magnitude": "major",
   "effect_on_play": "Off-lane farm is now the highest-value income on the map, but only for comps that clear grouped, chasing camps without bleeding HP. Weak-clear/single-target heroes fall further behind the AoE/sustain clearers, widening the coverage gap the KB already flagged."
  },
  {
   "system": "Comeback economy",
   "change_summary": "A three-part anti-snowball package: non-hero comeback gold cap rises 26%→30%, Haunted Souls secure up to 50% faster when behind (max at 20% NW gap), and the behind-multiplier now also feeds tick souls to the two poorest players.",
   "driving_changes": [
    "Comeback gold from non-hero sources increased from a max of 26% to 30% (when behind by ~20% Net Worth)",
    "Haunted Souls secure rate is now up to 50% faster than baseline based on how far behind you are in Net Worth compared to the enemy team's average (max rate at a 20% Net Worth gap)",
    "The bonus NPC souls multiplier when behind now also increases tick souls for the 2 poorest players"
   ],
   "magnitude": "major",
   "effect_on_play": "This directly reverses the KB's 'leads stick' read: losing teams now convert camp souls more reliably and get passive tick catch-up, so a farm lead is a soft lead. It rewards teams that keep farming from behind instead of conceding, and lengthens games."
  },
  {
   "system": "Haunted Souls secure mechanic",
   "change_summary": "Baseline secure rate is 25% slower, but scales up to 50% faster than baseline the further behind you are in net worth.",
   "driving_changes": [
    "Haunted Souls secure rate is now 25% slower",
    "Haunted Souls secure rate is now up to 50% faster than baseline based on how far behind you are in Net Worth compared to the enemy team's average (max rate at a 20% Net Worth gap)"
   ],
   "magnitude": "moderate",
   "effect_on_play": "Contested camp souls become a skill/timing check for the leader (slower baseline secure = easier to steal) and a gift for the trailing team. It makes camp contests less of a straight stat-check and more of a comeback lever."
  },
  {
   "system": "Breakables / crate economy + Halloween Cauldrons",
   "change_summary": "Breakables growth values drop 10%, while new Halloween Cauldrons (broken with Heavy Melee) drop Candy granting a temporary Sugar Rush buff.",
   "driving_changes": [
    "Breakables growth values reduced by 10%",
    "With a Heavy Melee, break the cauldron to pick up a piece of Candy and stash it in your pocket for later... consume the candy to grant yourself a boost of energy with the temporary Sugar Rush buff"
   ],
   "magnitude": "moderate",
   "effect_on_play": "Crate scaling is trimmed, so Heavy Melee crate routes pay slightly less late, but Cauldrons add a fresh Heavy Melee-gated pickup that rewards the same frontline/tank kits with a stashed tempo buff. Heavy Melee access stays a real economy skill."
  },
  {
   "system": "Sustain pickups",
   "change_summary": "Healing Snacks heal rises from 10% to 14% max HP.",
   "driving_changes": [
    "Healing Snacks heal increased from 10% Max HP to 14%"
   ],
   "magnitude": "minor",
   "effect_on_play": "Camps and extended off-lane routes are more survivable, reinforcing sustain bruisers and tanks who already clear Haunts; it slightly lowers the cost of contesting hubs and Buff Containers."
  },
  {
   "system": "Movement / Steam Vents / tunnels / air drag",
   "change_summary": "Steam Vents are reworked to grant +150% stamina regen (from the KB's invisibility roams), tunnel move speed drops +70%→+50%, and the slow-to-air-drag ratio rises 0.35→0.5.",
   "driving_changes": [
    "Steam Vents now increase stamina regeneration by 150%",
    "Move speed in tunnels reduced from +70% to +50%",
    "Move slow to air drag ratio increased from 0.35 to 0.5"
   ],
   "magnitude": "moderate",
   "effect_on_play": "Vents shift from a stealth-gank tool to a stamina/kiting tool, cutting the free approach angle roamers had; tunnel rotations slow, tightening map tempo; and the higher air-drag ratio taxes flyers harder whenever they're slowed."
  },
  {
   "system": "Ranked roster / bans",
   "change_summary": "The latest six heroes lose 'new' status, gaining normal ranked unlock requirements and becoming bannable.",
   "driving_changes": [
    "Latest 6 heroes are no longer categorized as \"new\" anymore. This means they have normal hero unlocking requirements for ranked and can now be banned."
   ],
   "magnitude": "minor",
   "effect_on_play": "Ranked draft can now suppress the strongest of the recent six, so their pick/win rates should compress toward the field; it also raises the barrier to entry on those kits in ranked."
  }
 ],
 "tempo_shift": {
  "direction": "toward_scaling",
  "confidence": 0.6,
  "why": "The comeback package (non-hero comeback gold 26%→30%, Haunted Souls securing up to 50% faster when behind, tick souls to the two poorest) plus trimmed breakable growth directly softens leads the KB said were sticking, giving trailing teams a farm-based path back. Richer-but-tougher Haunts reward sustained farming over early lane tempo."
 },
 "archetype_effects": [
  {
   "archetype": "tank/frontline",
   "direction": "up",
   "magnitude": "moderate",
   "why": "Heavy Melee Cauldrons add a new candy/Sugar Rush pickup and Healing Snacks 10%→14% makes camp chip damage cheaper to absorb."
  },
  {
   "archetype": "late scaler",
   "direction": "up",
   "magnitude": "moderate",
   "why": "Comeback gold 26%→30%, faster Haunted Souls secure when behind, and tick souls to the poorest give trailing scalers a real catch-up route."
  },
  {
   "archetype": "mobile assassin",
   "direction": "down",
   "magnitude": "moderate",
   "why": "Steam Vents reworked from invisibility to stamina regen removes the free approach, and tunnels +70%→+50% slows rotations."
  },
  {
   "archetype": "poke/siege",
   "direction": "down",
   "magnitude": "minor",
   "why": "Higher air-drag ratio (0.35→0.5) taxes flyers harder under slows, and slower tunnel speed blunts long-range repositioning."
  },
  {
   "archetype": "lane bully",
   "direction": "neutral",
   "magnitude": "minor",
   "why": "Breakables growth -10% trims crate scaling, offset by Cauldron Heavy Melee value; net roughly flat."
  },
  {
   "archetype": "split pusher",
   "direction": "down",
   "magnitude": "minor",
   "why": "Breakables growth -10% and slower tunnel rotations reduce the value of shoving-and-rotating over farming Haunts."
  }
 ],
 "intent_read": "Valve is deliberately re-opening the comeback valve it closed in prior patches: the multi-pronged behind-team package (gold cap, Haunted Souls secure, tick souls) plus trimmed breakable growth targets the 'leads stick' problem the KB flagged. The Haunt bounty/HP bump and Cauldrons push income further off-lane and toward Heavy Melee/AoE clearers, while the Steam Vent and tunnel changes pull back the free-roam gank tempo that made corridors so strong."
}

## Item changes in this patch (grouped by item)

High-Velocity Rounds:
  - [neutral] High-Velocity Rounds: Bullet Velocity reduced from 60% to 45% (upgrades unaffected)
Express Shot:
  - [nerf] Express Shot: Secondary Fire Weapon Damage and growth reduced by 5%
Point Blank:
  - [buff] Point Blank: Slow duration increased from 2s to 2.5s
Hunter's Aura:
  - [rework] Hunter's Aura: No longer affects or counts enemies outside of line of sight or through walls
Shadow Weave:
  - [rework] Shadow Weave: No longer has Ambush Fire Rate or Melee Damage
  - [rework] Shadow Weave: Now has +50% Ambush Weapon Damage
  - [rework] Shadow Weave: Ambush bonuses now build up over 6s of being stealthed before reaching full power (invis progress UI pulses when it is charged up)
  - [rework] Shadow Weave: Abilities used to break stealth now benefit from the Ambush bonus on their own damage (previously the bonus was applied after the ability had already gone off)
Toxic Bullets:
  - [buff] Toxic Bullets: Anti Heal increased from 35% to 40%
Armor Piercer:
  - [neutral] Armor Piercer: Chance increased from 55% to 60%
Glass Cannon:
  - [buff] Glass Cannon: Weapon Damage increased from 80% to 85%
Spiritual Overflow:
  - [buff] Spiritual Overflow: Spirit power increased from 6 to 8 (from component changes)
Crippling Headshot:
  - [buff] Crippling Headshot: Anti-Heal increased from -35% to -40%
Golden Goose Egg:
  - [buff] Golden Goose Egg: Damage Penalty reduced from -15% to -12%
Spirit Sap:
  - [nerf] Spirit Sap: Cooldown increased from 18s to 22s
  - [nerf] Spirit Sap: Cast range reduced from 40m to 35m
Mystic Slow:
  - [buff] Mystic Slow: Dash Distance slow increased from -10% to -12%
Decay:
  - [nerf] Decay: Incoming Heal reduction increased from -50% to -55%
Radiant Regeneration:
  - [nerf] Radiant Regeneration: Regen on Spirit Damage scaling reduced from 0.35 to 0.25
  - [rework] Radiant Regeneration: Heal on Ability Cast now only triggers when you are in combat (like Spellslinger)
  - [nerf] Radiant Regeneration: Heal on Ability Cast reduced from 65 to 40
  - [nerf] Radiant Regeneration: Heal on Ability Cast boon scaling reduced from 1.7 to 1.4
Silence Wave:
  - [buff] Silence Wave: Bonus Health increased from +50 to +90
Torment Pulse:
  - [neutral] Torment Pulse: Melee Resistance increased from 18% to 22%
Echo Shard:
  - [buff] Echo Shard: Post cast time reduced from 0.5s to 0.2s
Focus Lens:
  - [buff] Focus Lens: Cooldown reduced from 45s to 40s
  - [fix] Focus Lens: Fixed damage dealt to a barrier not counting toward the repeated damage
Lightning Scroll:
  - [rework] Lightning Scroll: Damage now scales with Spirit Power (0.35)
  - [buff] Lightning Scroll: Dash Distance slow increased from -10% to -12%
Rebuttal:
  - [buff] Rebuttal: Parry Cooldown reduction reduced from -1.75s to -1.25s
Battle Vest:
  - [buff] Battle Vest: Weapon Damage increased from 18% to 22%
Bullet Lifesteal:
  - [buff] Bullet Lifesteal: Weapon Damage increased from 6% to 10%
  - [buff] Bullet Lifesteal: Bullet Lifesteal increased from 13% to 15%
Healbane:
  - [rework] Healbane: Multiple sources now stack on the enemy with diminishing returns (previously didn't stack)
  - [nerf] Healbane: Heal on Hero Kill reduced from 275 to 170 + 3/Boon
Healing Booster:
  - [rework] Healing Booster: No longer builds from Extra Regen
  - [rework] Healing Booster: No longer grants +3 Health Regen
  - [buff] Healing Booster: Out of Combat Regen increased from +1 to +2
Return Fire:
  - [rework] Return Fire: Now returns the damage you take from Haze's Fixation
  - [fix] Return Fire: Fixed the shop tooltip not listing the 10% Bullet Resistance
Spirit Lifesteal:
  - [buff] Spirit Lifesteal: Spirit Power increased from 6 to 8
  - [buff] Spirit Lifesteal: Spirit Lifesteal increased from 13% to 15%
Spirit Shielding:
  - [nerf] Spirit Shielding: Spirit Resist reduced from 18% to 15%
Bullet Resilience:
  - [neutral] Bullet Resilience: Bullet Resistance increased from 30% to 35%
  - [buff] Bullet Resilience: Out of Combat Regen increased from 3 to 5
Fury Trance:
  - [buff] Fury Trance: Active Move Speed increased from +1m to +1.5m
  - [buff] Fury Trance: Bullet Lifesteal increased from 14% to 15%
  - [buff] Fury Trance: Weapon Damage increased from 6% to 10%
Healing Nova:
  - [rework] Healing Nova: Now scales with Spirit Power (1.1) instead of Boons (6)
Metal Skin:
  - [rework] Metal Skin: Now increases your gravity by 20% while active
Infuser:
  - [buff] Infuser: Active Lifesteal increased from 70% to 75%
  - [buff] Infuser: Spirit Lifesteal increased from 13% to 15%
  - [buff] Infuser: Spirit power increased from 6 to 8
Juggernaut:
  - [buff] Juggernaut: Health Regen increased from +8 to +15
Leech:
  - [buff] Leech: Bullet Lifesteal increased from 28% to 30%
  - [buff] Leech: Spirit Lifesteal increased from 28% to 30%
Vampiric Burst:
  - [buff] Vampiric Burst: Active Lifesteal increased from 70% to 75%
  - [buff] Vampiric Burst: Bullet Lifesteal increased from 13% to 15%
  - [buff] Vampiric Burst: Weapon Damage increased from 6% to 10%
Spellbreaker:
  - [rework] Spellbreaker: When the item procs, it continues to reduce any other spirit damage that happens as a result in that damage stack (for example, getting hit by charged shot that procs tankbuster now both get reduced)
Divine Barrier:
  - [nerf] Divine Barrier: Cooldown increased from 45s to 55s

## Knowledge base: the changed items (who buys them and why)

Armor Piercer: (not in KB yet)
Battle Vest:
  name: Battle Vest
  role: ''
  bought_by:
  - Venator
  slot: null
  tier: null
  notes: ''

Bullet Lifesteal:
  name: Bullet Lifesteal
  role: sustain weapon item
  bought_by:
  - Infernus
  - Venator
  slot: Weapon
  tier: 2
  notes: Unchanged; standard early lifesteal on gun carries.

Bullet Resilience: (not in KB yet)
Crippling Headshot: (not in KB yet)
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
  notes: '09-16: DPS -25% but duration +20%. Still the default anti-heal slot, now
    better in drawn-out fights than bursting a heal window down.'

Divine Barrier:
  name: Divine Barrier
  role: cleanse shield item
  bought_by:
  - Rem
  - Solomon
  slot: Vitality
  tier: 3
  notes: No recent change.

Echo Shard:
  name: Echo Shard
  role: ability reset item
  bought_by:
  - Paradox
  - Haze
  - Bebop
  - Calico
  - Ivy
  - Viscous
  - Pocket
  - Mirage
  - Sinclair
  - Mina
  - The Doorman
  - Victor
  - Billy
  - Graves
  - Celeste
  - Yamato
  slot: Spirit
  tier: 4
  notes: "07-28: post-cast 0.5s, lost +5% fire rate, cooldown now 30s + imbued ability\
    \ cd \u2014 a real cap on the double-cast cheese builds, though it remains the\
    \ connective tissue of the meta."

Express Shot:
  name: Express Shot
  role: ''
  bought_by:
  - Deadman Danny
  - Paradox
  - Viscous
  slot: null
  tier: null
  notes: ''

Focus Lens:
  name: Focus Lens
  role: spirit amp item
  bought_by: []
  slot: Spirit
  tier: 3
  notes: '09-16: damage 30->35%, cast range 20->25m. A standoff spirit-amp for setup
    casters; still cleansable, so situational.'

Fury Trance:
  name: Fury Trance
  role: active steroid item
  bought_by: []
  slot: Weapon
  tier: 3
  notes: '07-28: active grants +1m move speed and removes shooting move-speed penalty
    (Fleetfoot-like).'

Glass Cannon: (not in KB yet)
Golden Goose Egg:
  name: Golden Goose Egg
  role: econ item
  bought_by: []
  slot: Vitality
  tier: 4
  notes: "09-16: damage penalty -10->-15%, souls/min 90->80, stored souls now count\
    \ toward net worth \u2014 effectively unbuyable."

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
  notes: No recent change.

Healing Booster:
  name: Healing Booster
  role: ''
  bought_by:
  - Apollo
  - Baba
  - Celeste
  - Ivy
  - Kelvin
  - Rem
  - Solomon
  - Victor
  slot: null
  tier: null
  notes: ''

Healing Nova:
  name: Healing Nova
  role: team heal item
  bought_by:
  - Kelvin
  - Ivy
  - Rem
  slot: Vitality
  tier: 3
  notes: No recent change; part of the support-sustain package.

High-Velocity Rounds:
  name: High-Velocity Rounds
  role: utility weapon item
  bought_by:
  - Baba
  - Celeste
  - Deadman Danny
  - Grey Talon
  - Paige
  - Paradox
  - Rat King
  - Rem
  - Sinclair
  - Solomon
  - Victor
  - Vindicta
  - Violet
  - Viscous
  - Warden
  slot: Weapon
  tier: 2
  notes: No recent change.

Hunter's Aura:
  name: Hunter's Aura
  role: ''
  bought_by:
  - Abrams
  - Silver
  - Yamato
  slot: null
  tier: null
  notes: ''

Infuser:
  name: Infuser
  role: ''
  bought_by:
  - Victor
  slot: null
  tier: null
  notes: ''

Juggernaut: (not in KB yet)
Leech:
  name: Leech
  role: lifesteal item
  bought_by: []
  slot: Vitality
  tier: 4
  notes: '09-16: bullet+spirit lifesteal 25->28%. Still loses to cheaper lifesteal
    in the slot; a small nudge, not core.'

Lightning Scroll: (not in KB yet)
Metal Skin: (not in KB yet)
Mystic Slow: (not in KB yet)
Point Blank: (not in KB yet)
Radiant Regeneration:
  name: Radiant Regeneration
  role: healing spirit item
  bought_by:
  - Baba
  - Celeste
  - Kelvin
  - Lady Geist
  - Shiv
  slot: Spirit
  tier: 3
  notes: "Third cumulative trim to the regen shell: 08-22 heal on cast 70->65, 09-16\
    \ per-boon scaling 2->1.7, 10-14 spirit scaling 0.04->0.035. Still 94-98% buy\
    \ on holders, so it stays core, but each point of spirit power now buys less healing\
    \ \u2014 spirit-stacking users (Lady Geist Soul-Exchange, Shiv, Baba) feel it\
    \ most. No competing sustain item added, so nothing displaces it; the slot just\
    \ shrinks in value, quietly favouring anti-heal (Healbane, Decay) and pre-ramp\
    \ burst."

Rebuttal: (not in KB yet)
Return Fire: (not in KB yet)
Shadow Weave:
  name: Shadow Weave
  role: invis weapon item
  bought_by:
  - Warden
  slot: Weapon
  tier: 3
  notes: "09-16: now builds from Sprint Boots, sprint speed 1.5->2, cooldown 45->37s.\
    \ Inherits Veil Walker's Sprint Boots path and disengage niche \u2014 a real invis-engage\
    \ option for gun carries and cage bruisers."

Silence Wave: (not in KB yet)
Spellbreaker: (not in KB yet)
Spirit Lifesteal:
  name: Spirit Lifesteal
  role: ''
  bought_by:
  - Infernus
  - Seven
  - Victor
  - Violet
  - Warden
  - Wraith
  slot: null
  tier: null
  notes: ''

Spirit Sap: (not in KB yet)
Spirit Shielding:
  name: Spirit Shielding
  role: ''
  bought_by:
  - Billy
  - Celeste
  - Silver
  - Vyper
  slot: null
  tier: null
  notes: ''

Spiritual Overflow:
  name: Spiritual Overflow
  role: spirit proc/steroid item
  bought_by:
  - Baba
  - Infernus
  - Warden
  slot: Spirit
  tier: 3
  notes: '09-16: buildup 35% slower, spirit power 40->30, fire rate 30->25%. With
    Mercurial Magnum''s nerf and Plated Armor''s fix, the on-hit spirit package is
    weakened.'

Torment Pulse:
  name: Torment Pulse
  role: ''
  bought_by:
  - Baba
  - Celeste
  - Mo & Krill
  - Shiv
  - Victor
  - Yamato
  slot: null
  tier: null
  notes: ''

Toxic Bullets:
  name: Toxic Bullets
  role: anti-heal DoT weapon item
  bought_by:
  - Drifter
  - Graves
  - Infernus
  - Mirage
  slot: Weapon
  tier: 2
  notes: '09-16: spirit scaling 0.005->0.006%. With Decay''s DPS cut, now the better
    sustained anti-heal/burn option for hybrid and spirit-hybrid carries.'

Vampiric Burst: (not in KB yet)

## Knowledge base: heroes whose core_items or build_variants include a changed item

Infernus:
  name: Infernus
  role: gun/spirit carry
  archetypes:
  - gun carry
  - spirit carry
  - mobile assassin
  - late scaler
  tier: B
  trend: stable
  why: 'Burn carry whose AoE still clears the new behavior-varied Haunt types, but
    this patch''s new levers all cut against him: Healing Snacks heal through burn
    poke, permanent Spirit Resist container rolls are unstrippable, and Barrel Mimics
    tax the crate walks he has no heavy melee for. Dashfernus stays his stronger line
    and the tempo meta still ends games before a behind Infernus spikes.'
  core_items:
  - Extra Spirit
  - Improved Spirit
  - Spirit Lifesteal
  - Mystic Vulnerability
  - Healbane
  - Rapid Rounds
  - Swift Striker
  - Toxic Bullets
  - Superior Duration
  - Escalating Exposure
  - Spiritual Overflow
  - Titanic Magazine
  build_variants:
  - Dashfernus (spirit dash)
  - Burn gun carry
  enabled_by:
  - Toxic Bullets scaling buff (09-16)
  - Healbane into healer-heavy comps (77% buy)
  - "Spirit scaling \u2014 Escalating Exposure 54.0% WR leads (Spiritual Overflow\
    \ nerfed 09-16)"
  - 09-16 dash no longer breaking gun cycle time
  countered_by:
  - Decay
  - Healbane
  - Dispel Magic
  - Healing Snacks (heals through burn poke)
  - Buff-Container Spirit Resist rolls
  - Dynamo
  - Bebop
  - Vyper
  - Paradox
  - Yamato
  - Lash
  - tempo/snowball meta
  last_changed_patch: null
  notes: "Shh... This Won't Hurt a Bit. (10-20, indirect): Healing Snacks heal through\
    \ burn and Buff-Container Spirit Resist is permanent and unstrippable, so the\
    \ camp-AoE gain no longer nets out positive; Barrel Mimics punish the crate walks\
    \ he has no heavy melee for.\nPaint the Town (10-16, indirect): grouped Haunt\
    \ camps suit his burn AoE and Buff Containers roll Ability Range/Move Speed for\
    \ his spirit build; the tempo shift still ends games before his late spike.\n\
    City Never Sleeps (09-29): burn AoE clears the grouped Haunt camps; an unverified\
    \ report that his global napalm team-damage amp was removed is not in the notes\
    \ \u2014 confirm via win rate."
  builds:
  - name: Dashfernus (spirit dash)
    damage: spirit
    core_items:
    - Extra Spirit
    - Improved Spirit
    - Healbane
    - Spirit Lifesteal
    - Mystic Vulnerability
    - Rapid Recharge
    - Superior Duration
    - Escalating Exposure
    popularity: primary
    notes: 'Full-spirit mobility build: Flame Dash to kite and re-engage, burn + Mystic
      Vulnerability/Escalating Exposure for damage; posts the higher win rates of
      his two builds and is untouched by 09-16.'
  - name: Burn gun carry
    damage: gun
    core_items:
    - Extra Spirit
    - Improved Spirit
    - Rapid Rounds
    - Swift Striker
    - Extended Magazine
    - Titanic Magazine
    - Toxic Bullets
    popularity: secondary
    notes: "Gun build leaning on burn via Toxic Bullets; Spiritual Overflow was nerfed\
      \ 09-16 (spirit 40->30, fire rate 30->25%, slower buildup) so it is dropped\
      \ for Swift Striker/Titanic Magazine \u2014 still his weaker-performing item\
      \ set."
  matchups:
    beats:
    - Shiv
    - Pocket
    - Drifter
    - Seven
    - Mina
    loses_to:
    - Dynamo
    - Vyper
    - Bebop
    - Ivy
    - Paradox
  matchup_notes: 'He beats melee bruisers he can kite (Shiv 54%, Drifter 52%) and
    squishies his burn out-ranges (Pocket 54%, Seven 51%). He loses to displacement-plus-burst
    that negates his low-HP kite game: Dynamo 41% and Bebop 43% (initiations/hooks)
    and Vyper 42%, a straight gun duel his HP cap can''t win.'
  confidence: 0.6
  released_on: null
  provisional: false
Seven:
  name: Seven
  role: spirit carry
  archetypes:
  - spirit carry
  - late scaler
  tier: A
  trend: rising
  why: "Farm-first AoE carry and the clearest jungle winner on the board: nine behavior-varied\
    \ Haunt types make the fastest camp clear the largest income edge on the map,\
    \ and pre-announced Bell Tower/Sunken Plaza fights reward his AoE. He still converts\
    \ a lead only \u2014 the no-comeback economy leaves a behind Seven unable to brawl\
    \ back."
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
  last_changed_patch: Minor Update - 08-12-2026
  notes: 'Shh... This Won''t Hurt a Bit. (10-20, indirect): nine behavior-varied Haunt
    types (grouped/chasing) make the fastest camp clear the biggest income lever in
    the game; he has no crate or Barrel Mimic route and does not need one.

    Paint the Town (10-16, indirect): fastest Haunt-camp clear plus telegraphed Plaza/Bell
    Tower hub fights push him B->A; the no-comeback economy still caps a behind Seven.

    City Never Sleeps (09-29, indirect): grouped Haunt camps + guaranteed Tough-Crate
    routes reward his AoE farm-first line; the no-comeback valve still caps a behind
    Seven.'
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
  tier: A
  trend: rising
  why: 'Max-range poke/siege carry and a structural winner of the map rework: new
    roofs and high ground let her hold lanes and poke the telegraphed Sunken Plaza
    (5-8 min) and Bell Tower (8+) fights, and the tempo economy still rewards lane
    pressure. She still pays the flyer tax (Weighted Bola, air-drag slows), so she
    holds A rather than S.'
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
  - global slows now hit air drag
  - Lash (mobile initiator)
  - dive/CC comps
  - Yamato (mobile burst assassin)
  last_changed_patch: Minor Update - 08-12-2026
  notes: "City Never Sleeps (09-29, indirect): new roofs/high ground and telegraphed\
    \ Plaza/Bell Tower hub fights favor her max-range poke; flyer tax unchanged.\n\
    09-16 (indirect): global slows now bite air drag and Silver's Weighted Bola grounds\
    \ Flight \u2014 anti-flyer tax offsets her tempo gains, so she holds A.\nheresy's\
    \ 09-17 ricochet/split-shot ult buff is unattributable; the 09-16 notes give it\
    \ to Venator \u2014 treat as uncertain."
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
  trend: stable
  why: "Regen frontline bruiser whose Extra Regen/Mystic Regeneration stack clears\
    \ the patch's sustain check \u2014 harder camps and Barrel Mimic fights chip but\
    \ do not break her \u2014 while permanent container Bullet/Spirit Resist is free\
    \ frontline defense. She still folds to the same dive assassins and the cumulative\
    \ Radiant Regeneration trims keep narrowing her regen window."
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
  last_changed_patch: Minor Update - 09-16-2026
  notes: 'Shh... This Won''t Hurt a Bit. (10-20, indirect): harder camps plus Barrel
    Mimic fights make farm a sustain check her regen stack passes, and container Bullet/Spirit
    Resist rolls add free frontline stats; the same dive heroes still eat her.

    10-14: Radiant Regeneration spirit scaling 0.04->0.035 (third cumulative trim)
    narrows her ~98%-buy regen core; the Spirit Soul-Exchange variant, which stacks
    the most spirit power, loses most.

    City Never Sleeps (09-29, indirect): harder Haunt camps reward her sustain stack
    and Buff-Container Spirit Resist adds free defense; the no-comeback economy still
    caps her farm-then-scale pattern.'
  builds:
  - name: Regen gun-bruiser
    damage: hybrid
    core_items:
    - Extra Regen
    - Monster Rounds
    - Mystic Regeneration
    - Radiant Regeneration
    - Kinetic Dash
    - Berserker
    popularity: primary
    notes: "Buy regen first (Extra Regen 2.7m, Monster Rounds 3.1m) to survive a losing\
      \ lane, then Kinetic Dash + Berserker to frontline and gun-spam; Soul Exchange\
      \ is the finisher \u2014 the vegas '6000 HP fire-rate hero'."
  - name: Spirit Soul-Exchange
    damage: spirit
    core_items:
    - Mystic Regeneration
    - Radiant Regeneration
    - Mystic Burst
    - Bullet Resist Shredder
    - Spirit Resilience
    popularity: secondary
    notes: Caster-leaning variant leaning on the buffed bomb/drain and a Spirit Resilience/Healing
      Booster defensive layer; weaker lane, better burst and bigger ult finisher.
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
Abrams:
  name: Abrams
  role: tank initiator
  archetypes:
  - tank/frontline
  - initiator
  tier: B
  trend: rising
  why: "Melee tank who owns the two farm routes ranged kits cannot contest \u2014\
    \ 58-soul Tough Crates and now Barrel Mimics, which are a sustain check his Siphon/heavy-melee\
    \ core passes and low-HP gun clearers fail. Anti-heal stacking is still his ceiling."
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
  last_changed_patch: Minor Update - 09-16-2026
  notes: 'Shh... This Won''t Hurt a Bit. (10-20, indirect): Barrel Mimics convert
    breakable-chaining into a sustain check his heavy-melee + Siphon core passes,
    making the uncontestable crate route safer than it is for squishy gun clearers.

    Paint the Town (10-16, indirect): his melee core remains the cheap route into
    the Haunt/crate farm and the objective-parry change keeps dives on him risky;
    frontline up, anti-tank Shiv his real counter.

    City Never Sleeps (09-29, indirect): his melee core farms Tough Crates cheaply
    and the parry-on-objective change punishes dives on him; frontline archetype up.'
  builds:
  - name: Melee brawler (gun)
    damage: gun
    core_items:
    - Close Quarters
    - Monster Rounds
    - Melee Lifesteal
    - Stalker
    - Melee Charge
    - Bullet Resist Shredder
    - Hunter's Aura
    popularity: primary
    notes: 'The default at ~80-90% buy share: cheap Close Quarters/Monster Rounds
      spike the early melee trade, then Hunter''s Aura and Stalker (which gates his
      Shoulder Charge engage) carry it into mid.'
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
  why: 'Wraith''s spirit on-hit identity was heavily weakened by 09-16: Card Trick
    heal/scaling/resist/slow cuts plus the Mercurial Magnum nerf and Plated Armor''s
    on-hit fix (which now blanks Full Auto''s spirit damage) push her toward a pure-gun
    build. She keeps a high floor (~51% WR, near-50% PR) as a fire-rate M1/AoE-delete,
    but is outclassed in her slot by tempo carries (Silver, Venator, Haze) and punished
    by the dive the meta rewards.'
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
  last_changed_patch: Minor Update - 09-16-2026
  notes: "09-16: Card Trick heal 75->60, heal scaling 0.75->0.5, resist shred -8->-7%\
    \ (T3 -5->-4%), T3 slow +20->+15%; Mercurial Magnum + Spiritual Overflow gutted\
    \ and Plated Armor now blanks Full Auto spirit damage \u2014 on-hit-spirit core\
    \ weakened, lean pure gun.\nCreator-cited Capacitor/Slowing Hex appear in none\
    \ of the top-15 item slots; usage says the real core was spirit on-hit (Quicksilver\
    \ Reload 100%, Mercurial Magnum 93%) \u2014 Magnum now weakened.\nBuild clustering\
    \ is medium-confidence: inferred from shares/buy_min, no ability text."
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
  trend: rising
  why: 'Pick/sniper whose roamer identity keeps improving: Steam Vent invisibility,
    more off-lane hiding spots and instant-cast combo timing tighten her carbine picks,
    and Barrel Mimics leave low-HP crate clearers standing still to shoot. Anything
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
  - new districts/hiding spots/Steam Vent invisibility (roamer pick setups; ahead
    of Bebop)
  countered_by:
  - Yamato
  - Lash
  - Holliday
  - cleanse/dispel
  - Veil Walker
  - range denial
  last_changed_patch: Minor Update - 09-16-2026
  notes: 'Shh... This Won''t Hurt a Bit. (10-20, indirect): instant casts tighten
    her carbine->swap combo, and Barrel Mimics leave squishy crate clearers stationary
    for picks; mobile divers still close on her.

    Paint the Town (10-16, indirect): new districts, more hiding spots and Steam-Vent
    invisibility sharpen her roamer pick setups and keep her ahead of Bebop in that
    slot; the sniper line still folds to mobile divers.

    City Never Sleeps (09-29, indirect): new districts/hiding spots/Steam Vents upgrade
    her roamer pick setups and move her ahead of Bebop in that slot.'
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
  tier: A
  trend: rising
  why: Default sustained front line for harder Haunt camps and contested Buff Containers;
    Scorn/Burrow uptime plus T3 bullet resist let him commit. Objective parries no
    longer reset, so his Guardian dive is one-shot, and ranged poke he cannot close
    on still beats him.
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
  last_changed_patch: Minor Update - 07-28-2026
  notes: "Shh... This Won't Hurt a Bit. (10-20, indirect): harder Haunt camps and\
    \ contested Buff Containers reward his sustained frontline; objective parries\
    \ no longer reset, trimming the free Guardian-dive chain.\nPaint the Town: no\
    \ direct change; the Haunt-camp/hub economy keeps him the default sustained front\
    \ line, but objective parries no longer reset \u2014 the free dive chain is trimmed.\
    \ Ranged poke (Celeste, Vindicta) and rising Paige still beat him.\nCity Never\
    \ Sleeps: camp/uptime meta plus Billy's slide hand him the default sustained front-line\
    \ slot."
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
  tier: A
  trend: rising
  why: "Anti-tank bruiser the rising frontline feeds \u2014 current-HP Serrated Knives\
    \ shred Abrams/Mo & Krill/Billy and harder camps reward his regen stack. Steam\
    \ Vents give divers a free approach before regen ramps, so burst/hook CC still\
    \ kills him."
  core_items:
  - Mystic Regeneration
  - Extra Regen
  - Extra Charge
  - Radiant Regeneration
  - Healbane
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
  last_changed_patch: Minor Update - 09-16-2026
  notes: 'Shh... This Won''t Hurt a Bit. (10-20, indirect): harder camps reward his
    regen stack and the rising frontline feeds current-HP Serrated Knives, but vents
    hand divers a free approach before he ramps.

    Paint the Town: no direct change; harder Haunt camps reward his regen stack and
    the rising frontline feeds Serrated Knives, but a 43.4% snapshot WR keeps this
    soft.

    10-14: Radiant Regeneration spirit scaling 0.04->0.035 chips his near-universal
    regen core; kit untouched.'
  builds:
  - name: Spirit sustain bruiser
    damage: spirit
    core_items:
    - Mystic Regeneration
    - Extra Regen
    - Radiant Regeneration
    - Healbane
    - Extra Charge
    popularity: primary
    notes: Stack regen and cooldown so extended fights are unwinnable; Healbane doubles
      as anti-heal against other sustain fronts.
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
      (40% share) carries his best win rate at 59%.
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
  why: Still the best peel in the game (Stone Form i-frame/stun) and a 53.7% WR support,
    but Healing Snacks plus four spread corridors reduce the value of a grouped healer,
    and districts pull her team apart. Tether a frontline bruiser sweeping corridors
    rather than a lane partner.
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
  notes: 'Shh... This Won''t Hurt a Bit. (10-20, indirect): Healing Snacks plus spread
    corridors cut the value of a grouped healer; districts pull her team apart, so
    tether a frontline bruiser sweeping corridors instead of a lane partner.

    City Never Sleeps: no direct line; peercontent floats a small lift off camp-damage
    sustain, but the Healing Snack addition and trimmed heal items cut both ways for
    her (low confidence).

    Real build is gun-first (Extended/Titanic/Tesla 68-74%); creator heal-support
    framing is stale.'
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
  trend: falling
  why: Late-scaling gun carry the tempo economy still refuses to wait for; Steam Vents
    hand every hero the invis-engage he pays Shadow Weave for, so his one exclusivity
    is gone. No item or system route slows the clock that kills his late spike.
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
  last_changed_patch: Minor Update - 09-16-2026
  notes: "Shh... This Won't Hurt a Bit. (10-20, indirect): Steam Vents give every\
    \ hero the invis-engage he pays Shadow Weave for, flattening his one unique tool\
    \ while tempo still ends games before his late gun spike.\nPaint the Town: no\
    \ direct line; contested Soul Bags and earlier Bell Tower/Sunken Plaza objectives\
    \ close games even faster, deepening the wait a late gun scaler cannot afford\
    \ \u2014 no core item moved.\n09-16: bullet dmg/boon, flask range/speed, Willpower\
    \ T3 cut; Mercurial Magnum + Spiritual Overflow nerfed, Veil Walker stripped."
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
    notes: Stack weapon tiers to farm fast and stat-check, then play for the mid-game
      spike before tempo closes; the old T4 capstone (Mercurial Magnum/Spiritual Overflow)
      was nerfed this patch, so the late slot must be re-routed to another line.
  - name: Cage bruiser
    damage: hybrid
    core_items:
    - Shadow Weave
    - Spirit Lifesteal
    - Enduring Speed
    - Sprint Boots
    popularity: secondary
    notes: "Shadow Weave \u2014 now carrying Sprint Boots, faster sprint and a 37s\
      \ cooldown \u2014 replaces the stripped Veil Walker as the invis-engage shell\
      \ for walking up to land the silence cage."
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
  tier: A
  trend: rising
  why: "Camp-clear champion: Flying Strike now paths off solid objectives/turrets\
    \ for a second mobility vector, and her punch AoE still clears grouped Haunts\
    \ fastest. Objective parries no longer reset, so her Shrine dive is one-shot \u2014\
    \ plan the exit before committing."
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
  last_changed_patch: Shh... This Won't Hurt a Bit.
  notes: "Shh... This Won't Hurt a Bit. (10-20): Flying Strike creates paths against\
    \ solid targets (turrets, Shrines, objectives) for extra mobility/objective access;\
    \ parry no longer resets on objectives, so her Shrine/Walker dive is one-shot.\n\
    Paint the Town: no direct change; punch AoE is still the fastest clear for the\
    \ new grouped, behavior-varied Haunt camps and Flying Strike paths open the separated\
    \ Shrine/objective layout.\nCity Never Sleeps: Flying Strike creates paths against\
    \ solid targets (turrets, Shrines, objectives) \u2014 new mobility/objective access\
    \ \u2014 and she was the camp-clear champion vs grouped camps."
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
  tier: B
  trend: falling
  why: Cube rescue gains value when fights are scheduled at Bell Tower and Buff Containers,
    and harder camps reward Cube sustain while Goo Ball suits the spread vaults/corridors.
    Still a B enabler until a post-patch WR shows the 09-16 trims are absorbed.
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
  notes: 'Shh... This Won''t Hurt a Bit. (10-20, indirect): Bell Tower''s spread vaults
    and four corridors suit Goo Ball traversal, and harder camps plus forced hub fights
    raise Cube rescue value.

    City Never Sleeps: no direct line; harder camps reward Cube sustain and spread-out
    vaults suit Goo Ball, but this is a low-confidence lift.

    09-16: Cube cast range 26->20m, Puddle Punch cooldown 21->24s, Splatter/alt-fire
    nerfs; cooldown-Cube shell lost Veil Walker''s Sprint Boots.'
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
Mirage:
  name: Mirage
  role: split-push hybrid carry
  archetypes:
  - gun carry
  - split pusher
  - late scaler
  tier: C
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
Sinclair:
  name: Sinclair
  role: burst cast/steal
  archetypes:
  - burst caster
  - mobile assassin
  tier: C
  trend: falling
  why: "Coin-flip kit-steal pick trimmed across the whole kit \u2014 lane (HP regen\
    \ 2->1, bullet 17.76->16.5, falloff 25-61->20-60), utility (Rabbit Hex radius\
    \ 6.5->6m / T3 +3->+2m) and ult (copy duration 12->9s, copied-kit CD 40%->60%)\
    \ \u2014 so his already-thin win-condition leans entirely on stealing a strong\
    \ enemy kit, with Vexing Bolt's objective damage halved."
  core_items:
  - Greater Expansion
  - Superior Duration
  - Mystic Expansion
  - Duration Extender
  - Rapid Recharge
  - Extra Charge
  - High-Velocity Rounds
  - Opening Rounds
  - Monster Rounds
  build_variants:
  - Spirit Duration
  - Lane Gun-Hybrid
  enabled_by:
  - kit stealing
  - parry/bolt utility
  - urn value
  - strong enemy S-tier kits to steal (Yamato, Lash, Apollo)
  countered_by:
  - no draft (cannot force a favourable matchup)
  - mobile divers and bruisers (Lash, Yamato, Holliday, Calico, Drifter)
  - Bebop hook
  - low base survivability
  last_changed_patch: Minor Update - 10-05-2026
  notes: "10-05: broad trim \u2014 HP regen 2->1, gun falloff 25-61->20-60 (also on\
    \ Spectral Assistant), bullet 17.76->16.5, Rabbit Hex radius 6.5->6m / T3 +3->+2m,\
    \ Audience Participation copy 12->9s and copied-kit CD 40%->60%, Vexing Bolt halved\
    \ vs objectives. Still C; the objective-damage cut removes his only structure\
    \ pressure.\n\nChangelog: 09-16 - no Sinclair line; divers that beat him gained\
    \ from the tempo push, his winning matchups (Wraith, Paradox) shrink, and no spirit/duration\
    \ item moved. Net flat.\n\nData disagrees with creators: no Echo Shard in the\
    \ top-15 buys (30d, high rank); the build is duration/cooldown spirit."
  builds:
  - name: Spirit Duration
    damage: spirit
    core_items:
    - Mystic Expansion
    - Rapid Recharge
    - Extra Charge
    - Duration Extender
    - Superior Duration
    - Greater Expansion
    popularity: primary
    notes: Stacks ability/Hex duration and cooldown (Superior Duration + Greater Expansion
      ~80% share) to keep Rabbit Hex and stolen-kit CC on target; the actual zero-variance
      path, not Echo Shard.
  - name: Lane Gun-Hybrid
    damage: gun
    core_items:
    - High-Velocity Rounds
    - Monster Rounds
    - Opening Rounds
    popularity: secondary
    notes: Near-universal early weapon package (buy_min 1.5-4.3) for lane pressure
      and gun-cycle smoothing before pivoting to spirit; ~79% open with HVR/Opening
      Rounds.
  matchups:
    beats:
    - Wraith
    - Paradox
    loses_to:
    - Drifter
    - Bebop
    - Calico
    - Lash
  matchup_notes: "His only real wins are Wraith (54%) and Paradox (51%) \u2014 falling\
    \ squishy carries he can burst before they scale. He loses to Drifter (43%), Bebop\
    \ (44%) and rising divers Lash/Calico (47%): gap-closers, hooks and dive punish\
    \ his low HP and his inability to pick a favourable setup without draft."
  confidence: 0.42
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
  why: 'Blind-pickable spirit-melee bruiser with a private income lane: heavy-melee
    Tough Crates, Steam Vents and the new hiding spots all extend his stealth-reveal
    roam. He still lacks hard CC and closing mobility, so Dynamo/Mo & Krill/Apollo
    lane pressure caps him at A.'
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
  last_changed_patch: null
  notes: "10-20 Shh...: no direct change; Steam Vents, new hiding spots and heavy-melee\
    \ Tough Crates extend his stealth-roam and give his melee core uncontestable crate\
    \ income.\n09-29 City Never Sleeps: no direct change; new districts/Steam Vents\
    \ and heavy-melee Tough-Crate routes fit his roam.\nKB core_items cleaned of Decay/Toxic\
    \ Bullets/Fortitude \u2014 none in current 30-day usage; the 'Toxic Bullets bot'\
    \ framing is a 2026-04 artifact."
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
Victor:
  name: Victor
  role: tank/frontline
  archetypes:
  - tank/frontline
  tier: A
  trend: rising
  why: "Sustain frontline the camp meta feeds: harder Haunt camps, longer PvE routes\
    \ and Buff Container resist rolls all reward his Spirit Lifesteal/Healing Booster\
    \ stack \u2014 56.4% WR is still the board's second-highest. Still the one tank\
    \ burst and anti-heal can delete, and he drops the mirror to Abrams/Mo & Krill."
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
  last_changed_patch: Minor Update - 07-09-2026
  notes: "10-20 Shh...: no direct change; harder Haunt camps, longer PvE routes and\
    \ Buff Container Bullet/Spirit Resist rolls feed his sustain stack \u2014 A held.\n\
    09-29 City Never Sleeps: no direct change; hard Haunt camps fed his sustain stack,\
    \ flipping him from fair B-baseline to A on the 56.4% snapshot WR.\nData disagrees\
    \ with the 07-16 creator read: Refresher/Echo Shard appear in none of his top-15\
    \ buys."
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
  trend: rising
  why: Lane-winning support whose pressure now converts straight into the patch's
    early crate routes and Healing Snacks; she wins lane, then snowballs a carry before
    trimmed comeback souls can rescue the enemy. 52.7% WR / 29.2% PR, near-even into
    Rem/Ivy caps her dominance.
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
  - anti-heal (healing-item trims)
  last_changed_patch: Minor Update - 09-16-2026
  notes: "10-20 Shh...: no direct change; Healing Snacks let her lane pressure stick\
    \ instead of resetting on a recall, and lane-adjacent crate routes from ~2:30\
    \ pay the lane winner immediately \u2014 S held.\nCity Never Sleeps: no direct\
    \ change; lane-adjacent crate routes and Healing Snacks reward her lane pressure,\
    \ and the contested hubs suit her carry-snowball.\n09-16: heavy-melee spirit scaling\
    \ 0.3->0.45, Captivating Read T1 -11->-14s / T3 +1m->+2m; Slowing Hex cd 27->29s\
    \ a minor tax."
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
  trend: falling
  why: Lane-bully frontline whose all-in fits the contested-Haunt economy worse than
    sustained uptime; the front-line slot has moved to rising Mo & Krill and anti-tank
    Shiv remains his worst lane, so he sits below S.
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
  - Lifestrike melee-heal + flyer-dragging slow buff (low confidence - item sits outside
    his top-15 30-day buys)
  - Fortitude regen buff
  countered_by:
  - anti-tank bruisers (Shiv)
  - anti-heal
  - kiting / sustained ranged gun (Warden, Seven)
  - sustain-peel (Ivy)
  last_changed_patch: Minor Update - 08-12-2026
  notes: '10-20 Shh...: no direct change; harder Haunt camps reward sustained frontline
    presence, but Mo & Krill still owns the front-line slot and ranged corridor clear
    beats his all-in.

    10-16 Paint the Town: no direct change; behavior-varied Haunt camps and contested
    soul sources reward sustained presence, so his lane-bully all-in fits the economy
    less.

    10-05: no direct change; the trooper-speed fix marginally helps his lane-bully
    all-in, but his real slide (slot lost to Mo & Krill, anti-tank Shiv climbing)
    is unchanged.'
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
  trend: rising
  why: "Trap-clearing gun carry who finally has a job: her gun deletes Venator's pre-placed\
    \ traps, making her a real counter-pick into a high-pick hero. The economy still\
    \ denies her ~25-minute window \u2014 worst early game of any carry, no comeback\
    \ bail-out \u2014 and Barrel Mimics punish her crate chains."
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
  - Corrupted items at ~30 min (the only realistic late spike)
  countered_by:
  - mobile assassins (Holliday, Lash, Yamato, Mina, Calico, Drifter)
  - dive
  - out-scaling gun carries (Haze, Silver, Wraith, Warden)
  - slows
  - tempo/comeback-nerf meta
  - Barrel Mimics (crate chains while low HP)
  last_changed_patch: Shh... This Won't Hurt a Bit.
  notes: "10-20 Shh...: tier C->B, trend rising \u2014 trap-clearing into Venator\
    \ is a real draft lever, but Barrel Mimics punish her low-HP, two-stamina crate\
    \ chains and the corridor economy still taxes her scaling window.\n10-16 Paint\
    \ the Town: her gun destroys Venator's traps - genuine utility into an A-tier\
    \ hero - but the earlier, contested soul economy still deletes her ~25-min scaling\
    \ line.\n09-16: comeback souls trimmed and Rift resist made per-minute (comeback\
    \ path gone); health/boon 33->35 + Jar of Dead buffs are small; Toxic Bullets\
    \ scaling buff marginal."
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
  trend: rising
  why: 'Tempo lane bully the rebuilt economy favors: he routes Haunt camps and turns
    lane wins into lane-adjacent crate routes and Healing Snacks, and his spirit core
    is untouched. The objective-parry change trims his T3-bullet-resist Guardian dive
    from a chain to a single commitment.'
  core_items:
  - Extra Regen
  - Mystic Burst
  - Extra Spirit
  - Mystic Expansion
  - Spirit Strike
  - Improved Spirit
  - Healing Booster
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
  - Riposte buffs (08-12)
  - spirit item pool untouched
  - tower-dive still open with T3 bullet resist vs the parry-cooldown change
  countered_by:
  - Lash
  - Abrams
  - Mo & Krill
  - Warden
  - anti-heal vs his Locket/heal sustain
  last_changed_patch: Minor Update - 08-12-2026
  notes: "10-20 Shh...: no direct change; lane pressure converts into lane-adjacent\
    \ crate routes and Healing Snacks, but the objective-parry change makes the Guardian\
    \ dive a one-shot decision \u2014 S held.\n10-16 Paint the Town: no direct change;\
    \ the objective-parry cooldown-reset removal trims the T3-bullet-resist Guardian-dive\
    \ chain, but the crate-and-Haunt economy keeps him S.\n10-14: Baba (beats him\
    \ ~59%) took a major nerf \u2014 a marginal easing of a bad lane."
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
    - Healing Booster
    - Spirit Snatch
    - Boundless Spirit
    - Tankbuster
    popularity: primary
    notes: Lane-phase spirit poke into flat spirit burst; buy early T1s -> Improved
      Spirit -> T3/T4 spirit once ahead. Boundless Spirit and Tankbuster are late-game
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
  tier: S
  trend: rising
  why: 'Front-line gun tank built for a patch that starts fights earlier: gun cycle
    survives dashes/light melee, health/boon and sprint are up, and Weighted Bola
    grounds flyers - the contested-Haunt economy rewards her tempo; ceiling remains
    stacked CC and the Lash/Drifter pair.'
  core_items:
  - Restorative Shot
  - Melee Lifesteal
  - Stalker
  - Grit
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
  - tempo/early-snowball meta
  - Weighted Bola grounded interrupt (anti-air)
  - gun-cycle smoothing (dash/light melee don't break cycle)
  - health/boon and sprint buffs
  - front-line initiators who start fights for her (Dynamo, Apollo, Lash)
  countered_by:
  - CC/debuff spam (Mo & Krill, Bebop, Paradox, The Doorman)
  - kiting and slows
  - anti-heal vs her Melee Lifesteal/Restorative Shot sustain
  - anti-tank bruisers (Shiv) and enemy Tankbuster buyers
  - matches up badly vs Lash and Drifter
  last_changed_patch: Minor Update - 09-16-2026
  notes: '10-16 Paint the Town: no direct change; the contested, earlier soul economy
    rewards her front-line tempo and Weighted Bola anti-air, so tier S holds.


    09-29 City Never Sleeps: no direct change; the frontline/tank archetype is up,
    but the move from lane tempo to farm-route tempo is roughly neutral for a lane-fight
    gun tank, and heavy-melee crate routes need a heavy melee she does not build toward
    (peercontent, low confidence).


    09-16: health/boon 28->31, sprint 1.5->2.5, and Weighted Bola now grounds/interrupts
    flyers - direct buffs; tier S held.'
  builds:
  - name: Gun tank
    damage: gun
    core_items:
    - Restorative Shot
    - Melee Lifesteal
    - Stalker
    - Grit
    - Hunter's Aura
    - Spirit Shielding
    popularity: primary
    notes: "The default shell \u2014 lane-sustain bruiser (97% Stalker, 96% Melee\
      \ Lifesteal, 90% Restorative Shot) that scales into a front-line DPS tank; run\
      \ it unless the enemy comp forces anti-CC."
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
  tier: B
  trend: falling
  why: Late-scaling flying spirit burst with no camp-clear or crate route in a corridor
    economy that pays for both, and the air-drag flyer tax still bleeds her mid-flight.
    She bursts squishy melee but folds to sustain, to Barrel Mimic ambushes on a low-HP
    clear, and to the mobile initiators who close on her.
  core_items:
  - Extra Regen
  - High-Velocity Rounds
  - Mystic Regeneration
  - Radiant Regeneration
  - Mystic Expansion
  - Healing Booster
  - Restorative Locket
  - Torment Pulse
  - Greater Expansion
  - Witchmail
  - Spirit Shielding
  - Grit
  build_variants:
  - Spirit sustain-burst carrier
  - Anti-CC / anti-debuff tech
  enabled_by:
  - High base power + overloaded kit (mobility, four abilities)
  - Torment Pulse + Greater Expansion AoE around her ult
  - Ult damage in Mid Boss / Rift fights
  - Mystic/Radiant Regeneration sustain stack (nerfed but still core)
  countered_by:
  - "Silver \u2014 Weighted Bola grounds flyers like her"
  - Slows now bleed air drag (system)
  - 'Healing item trims: Radiant Regeneration, Restorative Locket'
  - "Scaling/comeback nerfs \u2014 late-scaler into a tempo meta"
  - "Ivy \u2014 out-sustains her burst window"
  - "Lash / Calico \u2014 mobile initiators that close and survive"
  last_changed_patch: Minor Update - 09-16-2026
  notes: '10-20 Shh...: no direct change; the off-lane/corridor economy gives her
    no camp or crate income route, and Barrel Mimics tax a low-HP clearer, so the
    tempo patch keeps her B/falling.


    10-16 Paint the Town: no direct change; the contested, earlier soul economy punishes
    her late-scaling line and buffed Deadman Danny (61% vs her) adds a direct threat;
    tier B held.


    10-14: Radiant Regeneration spirit scaling 0.04->0.035 is the third trim to her
    sustain-burst core; Deadman Danny (beats her 61%) got a buff package.'
  builds:
  - name: Spirit sustain-burst carrier
    damage: spirit
    core_items:
    - Extra Regen
    - High-Velocity Rounds
    - Mystic Regeneration
    - Radiant Regeneration
    - Mystic Expansion
    - Healing Booster
    - Restorative Locket
    - Torment Pulse
    - Greater Expansion
    popularity: primary
    notes: "Regen-stacked spirit build: HVR early for bullet velocity/movespeed, then\
      \ Torment Pulse + Greater Expansion for AoE burst around her ult \u2014 weaker\
      \ now that Radiant Regeneration and Restorative Locket were trimmed."
  - name: Anti-CC / anti-debuff tech
    damage: hybrid
    core_items:
    - Witchmail
    - Spirit Shielding
    - Grit
    popularity: secondary
    notes: "Witchmail is her highest-WR item (60.6%, bought ~24m) \u2014 the answer\
      \ into heavy slow/CC comps, which matter more now that slows bleed air drag."
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
  trend: rising
  why: 'The patch''s shape in one kit: 116 heavy melee opens Tough Crates for uncontestable
    income, Scrap Grenade clears grouped Haunt camps, and Bell Tower/Sunken Plaza
    force the stacked fights his banner ult wants. Still soft to sustain supports
    and to spirit burst that bypasses his bullet barrier, so the S is fit-driven and
    needs WR confirmation.'
  core_items:
  - Monster Rounds
  - High-Velocity Rounds
  - Opening Rounds
  - Extra Health
  - Cultist Sacrifice
  - Enduring Speed
  - Fortitude
  - Superior Cooldown
  build_variants:
  - Gun bruiser
  - Vitality frontline
  - Swarm shred
  enabled_by:
  - 'Map-economy lead engine: grouped, chasing Haunt camps reward Scrap Grenade AoE
    clear and regen sustain'
  - "Tough Crate routes needing heavy melee \u2014 116 heavy melee, 800 HP, 2.0 regen\
    \ open guaranteed ~58-soul crates"
  - "Forced telegraphed hub fights at Sunken Plaza/Bell Tower \u2014 banner ult adds\
    \ move speed, slow immunity and DR"
  - "Gun-carry meta \u2014 Rat Swarm's bullet-resist shred and Royal Pestments deflect\
    \ punish Venator/Silver/Paradox"
  countered_by:
  - "Heal/save supports that out-sustain his damage window \u2014 Ivy, Kelvin, Paige,\
    \ Dynamo"
  - "Spirit burst that bypasses the anti-bullet barrier \u2014 Celeste"
  - Silence/CC (Silence Wave, Silencer) denying banner and barrier
  - Anti-heal (Healbane, Decay) against his regen stacking
  last_changed_patch: Minor Update - 10-05-2026
  notes: '10-20 Shh...: no direct change; Tough Crates, grouped chasing Haunts, forced
    Bell Tower/Sunken Plaza hubs and Barrel Mimics all point at heavy-melee camp-clear
    frontlines, so the systems patch lifts him A -> S on fit, not numbers - confirm
    against win rate before locking.


    10-16 Paint the Town: notes entry only - added to the weekly release-vote schedule,
    no balance change; the contested-Haunt economy still matches his heavy-melee crate
    and AoE-clear kit, so tier held A.


    10-05: banner ult trimmed (CD 130->160, DR 20->15% base + T3 15->10% = 35->25%
    total, radius 24->20m, charge 12->10s, no Spirit-scaled move speed); base kit
    buffed (Scrap Grenade 65->70, Rat Swarm CD 28->24s).'
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
      \ the work."
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
      Superior/Compress Cooldown (57.9%/57.7% WR) are the post-nerf answer to the
      banner ult's 130->160s cooldown.
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
  tier: C
  trend: stable
  why: Grounded regen bruiser who farms Tough Crates and grouped Haunts and wants
    the telegraphed hub fights this map schedules; the 10-14 barrier, resist and mobility
    cuts still cap her, so she out-sustains camp chip but not focus fire or anti-heal.
  core_items:
  - Extra Charge
  - Extra Regen
  - Mystic Regeneration
  - Spirit Strike
  - Radiant Regeneration
  - Healing Booster
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
  - No-comeback economy rewards her early camp income converting into an unkillable
    mid-game frontline
  countered_by:
  - 'Anti-heal vs her regen wall: Healbane, Decay, Toxic Bullets'
  - 'Sustain supports that neutralize her grind: Kelvin, Dynamo, Paige'
  - 'Channel interrupts/silence on her ult: Knockdown, Cursed Relic, Silencer'
  - 'Burst/mobile gun pressure she can''t out-poke: Holliday, Wraith; Plated Armor
    and Bullet Resilience vs her gun damage'
  last_changed_patch: Minor Update - 10-14-2026
  notes: '10-20 Shh...: no direct change; the new corridors, grouped Haunt camps and
    forced Bell Tower/Plaza fights suit her melee-regen clear and arrest the post-10-14
    fall, but the barrier/resist cuts still bind - trend falling -> stable at C.


    10-14: major kit cut - Brew barrier scaling 1.2->0.7 and base 100->90 with CD
    25->27s (later, T2), -7% Base Bullet Resist, spirit-resist scaling 0.12->0.1,
    Granny Long Legs CD 30->32 with lower light-melee launch and decaying repeat air-melee
    momentum, Threadsap CD 26->28 with its spirit shred now ending on death; plus
    Radiant Regeneration 0.04->0.035. Tier B -> C, trend falling.


    7-day check-in (2026-10-13): tier B -> B, WR 51%, PR 64% over 305220 matches.
    Usage overrides the prior entry: the real core is regen + cooldown-spirit items
    (Extra Charge 98%, Mystic Regeneration 95%, Radiant Regeneration 94%), not the
    Boundless Spirit/on-hit shells; 7-day matchups beat Solomon/Apollo/Calico, lose
    to Kelvin/Dynamo/Paige.'
  builds:
  - name: Spirit regen bruiser
    damage: spirit
    core_items:
    - Extra Charge
    - Extra Regen
    - Mystic Regeneration
    - Spirit Strike
    - Radiant Regeneration
    - Healing Booster
    - Torment Pulse
    - Spirit Resilience
    popularity: primary
    notes: 'The every-game shell: stack regen and HP to out-sustain Haunt chip and
      hub fights, with Torment Pulse as an AoE aura (Extra Charge 98%, Mystic Regeneration
      95%, Radiant Regeneration 94%). The 10-14 cuts (barrier, bullet/spirit resist,
      mobility) make the stack shakier - buy Healing Booster/Spirit Resilience earlier
      and stop counting on out-tanking focus; Brew is now a T2 (CD 25->27s), so it
      lands later.'
  - name: Cooldown caster
    damage: spirit
    core_items:
    - Compress Cooldown
    - Spirit Snatch
    - Duration Extender
    - Superior Cooldown
    - Rapid Recharge
    popularity: secondary
    notes: Late slot conversion (~20-24 min) to spam Threadsap/Brew/ult and extend
      hex/silence; Duration Extender (59.3%) and Superior Cooldown (58.8%) stay her
      best-WR items while Rapid Recharge (48.2%) is a trap. Threadsap CD 26->28 and
      its spirit shred now ends on her death, so duration and landing the silence
      matter more than raw sustain.
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
  why: Zone-control support drafted for telegraphed hub fights - Bell Tower, Sunken
    Plaza and container contests are exactly his ground - but the mobile dive class
    that skips his Bishop/Rook zones (Holliday, Yamato, Rat King, Celeste) is up in
    the same patch, so he sits near his ~43% baseline.
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
  last_changed_patch: Released 2026-10-09
  notes: '10-20 Shh...: no direct change; the patch schedules the fights his zones
    want (Bell Tower, container contests) but also lifts the dive class that lands
    before them, so he holds C/stable.


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
  trend: rising
  why: Spirit mark-burster whose AoE finally has the right targets - grouped, chasing
    Haunt camps plus stacked hub fights - and Steam Vents give him pick angles; still
    a 730-HP flyer with the air-drag tax intact and nothing above 49% head-to-head.
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
  - Steam Vent invisibility roams for pick angles, in a meta where roamer/pick assassins
    ticked up
  countered_by:
  - "Silver's Weighted Bola \u2014 S-tier anti-air that grounds him in addition to\
    \ out-trading his gun"
  - 'Slows and slow fields (Kelvin): doubled by the global air drag, they strip his
    disengage from every dive'
  - Silence/knockdown (Silencing Hex, Knockdown) plus Bebop hook catching a committed
    dive
  - Plated Armor vs HV Rounds/Opening Rounds poke; Debuff Reducer vs his marks and
    fading slow
  - "His own whiffed-dive self-stun against the 38s respawn timer at 20 min \u2014\
    \ a single bad dive is a lost fight"
  - 'Late payoff vs tempo: Boundless Spirit''s ~47-min average buy arrives after the
    game usually ends'
  last_changed_patch: Minor Update - 10-14-2026
  notes: '10-20 Shh...: no direct change; grouped chasing Haunt camps and corridor
    farm suit his spirit AoE marks and Steam Vents add approach angles, but the flyer
    tax and Barrel Mimic risk on a 730-HP commit keep him C/rising.


    7-day check-in (2026-10-20): tier C -> C, WR 45%, PR 69% over 446352 matches.
    Corrected: the usage data kills the ''shred/mark gun'' identity - Bullet Resist
    Shredder does not appear at all, and the real build is spirit (Extra/Improved
    Spirit, Mystic Burst at 79-90%) with HV Rounds as the lone weapon staple. The
    old beats list was inverted - Celeste (33%) and Graves (32%) are among his worst
    lanes, not wins. PR 69.1% is a new-hero novelty spike (previously 0.2% on a two-day
    sample), so read WR 38.5% and ignore pick rate. Held C/rising: the build finally
    consolidated and WR gained ~3.6 points, but nothing clears 49% head-to-head and
    the flyer tax is intact; upgrade only on ~45%+ WR, drop to D if the spirit capstone
    stays a post-30-min luxury.


    Paint the Town (10-16) changelog: no Danny-specific changes; the 10-14 buff package
    is still his live state.'
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


## What to do

For each changed item, decide the net direction and magnitude, then trace the consequence to heroes: who has it as a core slot, who used it situationally, and who might now pick it up. Note build-path changes (component changes, slot moves, what it now competes with). Think about the systems context: an item that was good because of the old economy may be worse even if its numbers went up, and vice versa.

Group multiple lines for the same item into one entry. Skip pure bug fixes unless the fix meaningfully changes an interaction (then say which heroes it affects).

Magnitude guide: minor = tuning that will not change who buys it; moderate = changes timing or priority in builds; major = adds or removes the item from core builds, or changes what it does.

## Change rows

`rows` is a list of scannable one-line changes for a phone screen. Give rows for **every item**.

- `label`: 1-3 plain words naming what changed ("Channel time", "T3", "New interrupts", "Teamplay").
- Prefer `old` + `new` when the note gives before/after values; otherwise `text` of at most 8 words. Never both.
- `effect`: judged for the player who buys this item: "good", "bad", or "neutral". A longer channel time is bad.
- `ability`: the exact ability name when the change applies to one.
- Merge lines that say the same thing. Keep every gameplay-relevant change. Never add anything not in the notes; every number in a row must come from the notes verbatim.

Example (Mirage's Traveler):

```json
{"label": "Channel time", "old": "2s", "new": "3s", "effect": "bad", "ability": "Traveler"}
{"label": "T3", "old": "-90s cooldown", "new": "Damage can't interrupt it", "effect": "good", "ability": "Traveler"}
{"label": "Base ability", "text": "Now includes a barrier (no scaling)", "effect": "good", "ability": "Traveler"}
```

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
      "build_shift": "optional 1 sentence on component/slot/competition changes, or empty string",
      "rows": [{"label": "1-3 words", "old": "before", "new": "after", "effect": "good|bad|neutral", "ability": "optional exact name"}]
    }
  ],
  "notable_item_stories": ["0-3 one-sentence cross-item stories, e.g. 'invisibility items were buffed together, expect Shadow Weave on more gun carries'"]
}
