# Task: item analysis

Patch: Minor Update - 10-14-2026 (2026-10-15)

## Systems analysis of this patch (already done)

{
 "systems_changed": [],
 "tempo_shift": {
  "direction": "neutral",
  "confidence": 0.9,
  "why": "no systems changes — the General/systems section is empty, so the map-economy lead engine, comeback valve, respawn timers, slows and objective bounties all carry over unchanged from 10-05."
 },
 "archetype_effects": [],
 "intent_read": "This is a narrow housekeeping patch: one item (Radiant Regeneration) and three hero kits (Baba, Deadman Danny, Street Brawl) were touched, with nothing at the economy, objective, movement or map layer. Valve is not trying to move the meta here — the templated Tough Crate/Sunken Plaza/Bell Tower income engine and the no-comeback valve stand as the KB thesis describes, so any meta movement must come from the item and hero changes alone."
}

## Item changes in this patch (grouped by item)

Radiant Regeneration:
  - [nerf] Radiant Regeneration: Spirit scaling reduced from 0.04 to 0.035

## Knowledge base: the changed items (who buys them and why)

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
  notes: "08-22 heal on cast 70->65 plus 09-16 per-boon scaling 2->1.7 \u2014 a cumulative\
    \ nerf to healing supports; they can no longer absorb an early deficit."


## Knowledge base: heroes whose core_items or build_variants include a changed item

Lady Geist:
  name: Lady Geist
  role: spirit bruiser
  archetypes:
  - tank/frontline
  - late scaler
  - spirit carry
  tier: A
  trend: rising
  why: 'Regen spirit bruiser climbing the front-line slot: the patch''s harder-hitting
    Haunt camps reward her Extra Regen/Mystic Regeneration sustain stack, Buff-Container
    Spirit Resist adds free defense, and her spirit-caster rivals (Celeste, Pocket,
    Mina) keep fading. Capped by the intact no-comeback economy that guts her 0-6-then-farm
    pattern and by the 09-16 Radiant Regeneration trim.'
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
  notes: 'City Never Sleeps (09-29, indirect): harder Haunt camps reward her sustain
    stack and Buff-Container Spirit Resist adds free defense; the no-comeback economy
    still caps her farm-then-scale pattern.

    09-16: Life Drain T3 spirit scaling 0.3->0.45 and Essence Bomb T3 26->30% buff
    her bomb/drain, but Radiant Regeneration 2->1.7 per-boon trims her 98%-buy regen
    core.

    WR 46.6% / PR 14.4% is a 14-day pre-patch snapshot; direction is split (vegas
    stable, heresy rising).'
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
Shiv:
  name: Shiv
  role: anti-tank spirit bruiser
  archetypes:
  - tank/frontline
  - mobile assassin
  tier: A
  trend: rising
  why: 'Rising anti-tank: the tank/frontline wave (Abrams, Mo & Krill, Billy) feeds
    his current-HP Serrated Knives, and harder camps reward his regen sustain. Burst
    and hook CC (Yamato, Drifter, Bebop) still kill him before regen ramps, and his
    core Radiant Regeneration was trimmed.'
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
  notes: "City Never Sleeps: rising anti-tank \u2014 the bigger front line feeds current-HP\
    \ Serrated Knives and harder camps reward his regen.\nSpirit/regen rebuild confirmed\
    \ (Mystic Regeneration/Extra Regen core); Mystic Vulnerability/Torment Pulse/Escalating\
    \ Exposure run 40-55%.\n09-16: knives current-HP rework + alt-fire buff; Radiant\
    \ Regeneration and Restorative Locket trimmed."
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
  why: 'Late-scaling flying spirit burst is the wrong profile for a lane-wins tempo
    meta: comeback souls are gone, early-Rift fights are real, and the new air-drag
    slow bleeds her mid-flight. Seven direct 09-16 nerfs stack on Radiant Regeneration
    and Restorative Locket trims, which is why she sits at B rather than A; the 54.6%
    WR / 26.4% PR is a pre-patch baseline, and she still bursts squishy melee threats
    (Yamato, Pocket) but folds to sustain and mobile initiators.'
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
  notes: "09-16: tier held at B (down from A) \u2014 the seven-nerf stack below plus\
    \ the air-drag flyer tax; Witchmail remains her anti-slow answer.\n54.6% WR /\
    \ 26.4% PR is a 14-day, mostly pre-patch snapshot \u2014 treat as a ceiling, not\
    \ current strength.\n09-16: seven direct nerfs plus indirect item, scaling, and\
    \ air-drag hits."
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
  matchup_notes: "She wins the burst race vs squishy close-range threats \u2014 61%\
    \ vs Pocket and 59% vs Yamato (S-tier, but she lands her damage before he closes).\
    \ Sustained healers out-last her damage window (Ivy 47%), while mobile initiators/bruisers\
    \ who survive the first burst and close the gap (Lash, Calico) beat her 52-53%."
  confidence: 0.6
  released_on: null
  provisional: false
Baba:
  name: Baba
  role: bulky spirit bruiser-caster
  archetypes:
  - spirit carry
  - tank/frontline
  - lane bully
  - initiator
  tier: B
  trend: stable
  why: "Baba is one of the patch's most-picked heroes (51.0% WR, 64.1% PR over 4.7k\
    \ games), and the usage data \u2014 not her old theorycrafted shell \u2014 defines\
    \ her: a regen-stacking spirit bruiser (Extra Charge, Mystic Regeneration, Radiant\
    \ Regeneration) who out-sustains the Haunt/crate economy and forces hub fights\
    \ her AoE hex and silence win. She holds B rather than rising because sustain\
    \ supports (Kelvin, Dynamo, Paige) match her grind and mobile gun pressure (Holliday,\
    \ Wraith) out-pokes her before the ult channel completes. The map-economy patch\
    \ still suits her heavy-melee plus AoE farm profile."
  core_items:
  - Extra Charge
  - Extra Regen
  - Mystic Regeneration
  - Spirit Strike
  - Radiant Regeneration
  - Healing Booster
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
  last_changed_patch: Mind the Birds!
  notes: "7-day check-in (2026-10-13): tier B -> B, WR 51%, PR 64% over 305220 matches.\n\
    1) Usage overrides the prior entry: Boundless Spirit/Arcane Surge and the on-hit/melee\
    \ shells (High-Velocity Rounds, Lifestrike, Colossus) barely register in high-rank\
    \ buys \u2014 the real core is regen + cooldown-spirit items. 2) Matchups replaced\
    \ by 7-day data (beats Solomon/Apollo/Calico; loses to Kelvin/Dynamo/Paige), which\
    \ differs sharply from the day-0 guesses. 3) Changelog: no Baba kit change since\
    \ Mind the Birds!; 10-05 was a trooper-speed fix only, leaving her map-economy\
    \ engine intact."
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
    popularity: primary
    notes: 'The every-game shell: stack regen and HP to out-sustain Haunt chip and
      hub fights, with Torment Pulse turning her into an AoE aura; Extra Charge (98%),
      Mystic Regeneration (95%) and Radiant Regeneration (94%) are near-universal.'
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
      hex/silence; Duration Extender (59.3%) and Superior Cooldown (58.8%) are her
      best-winrate items, while Rapid Recharge (48.2%) is a trap.
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
