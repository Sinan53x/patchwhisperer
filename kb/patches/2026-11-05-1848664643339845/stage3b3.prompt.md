# Task: per-hero analysis (hero batch)

Patch: Minor Update - 11-04-2026 (2026-11-05)

## Systems analysis

{
 "systems_changed": [],
 "tempo_shift": {
  "direction": "neutral",
  "confidence": 0.9,
  "why": "No systems changes: the General/systems sections are empty, and the only non-hero change is an item (Healbane), which moves builds rather than soul income, fight locations, or timers. Tempo therefore inherits the 10-30 state — comeback levers plus richer Haunts — unchanged."
 },
 "archetype_effects": [],
 "intent_read": "A hero-and-item micro-patch on top of the 10-30 gameplay update: the hero list (Apollo, Baba, Celeste, Deadman Danny, Mo & Krill, Nurse Harrow, Rat King) plus Healbane reads as targeted cleanup of outliers from that update rather than a new systemic direction. Valve is not touching economy, comeback, map or objectives, so the 10-30 thesis — leads must be converted fast, the jungle keeps paying the trailing team — still stands. Any movement this patch comes from individual kits and anti-heal itemization, not from how the game generates souls or where fights happen."
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

Infernus:
  name: Infernus
  role: gun/spirit carry
  archetypes:
  - gun carry
  - spirit carry
  - mobile assassin
  - late scaler
  tier: B
  trend: rising
  why: 'Burn carry and one of the patch''s few clean sustain winners: Haunt bounty/growth
    +10% pays a one-cycle burn clear that barely eats the Haunt HP/damage increase,
    and Spirit Lifesteal (+2 spirit/+2%), Toxic Bullets'' 40% heal-cut and Napalm
    T2 lifesteal 15->20% all feed his farm-and-kite shell. He still folds to displacement-plus-burst
    that negates low-HP kiting (Dynamo, Bebop), and the slower comeback economy means
    his late spike now arrives on time more often.'
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
  last_changed_patch: Halloween 2026 + Gameplay Update
  notes: 'Halloween 2026 + Gameplay Update (10-30, direct): Napalm T2 lifesteal 15->20
    and Concussive Combustion T3 +0.4 spirit scaling lift the Dashfernus line; Spirit
    Lifesteal +2 spirit/+2% lifesteal and Toxic Bullets'' 40% heal-cut pay his camp
    route, and Haunt bounty/growth +10% is nearly free for a one-cycle burn clear.

    Shh... This Won''t Hurt a Bit. (10-20, indirect): Healing Snacks heal through
    burn and Buff-Container Spirit Resist is permanent and unstrippable, so the camp-AoE
    gain no longer nets out positive; Barrel Mimics punish the crate walks he has
    no heavy melee for.

    Paint the Town (10-16, indirect): grouped Haunt camps suit his burn AoE and Buff
    Containers roll Ability Range/Move Speed for his spirit build; the tempo shift
    still ends games before his late spike.'
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
Abrams:
  name: Abrams
  role: tank initiator
  archetypes:
  - tank/frontline
  - initiator
  tier: A
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
Haze:
  name: Haze
  role: gun carry
  archetypes:
  - gun carry
  tier: S
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
Bebop:
  name: Bebop
  role: hook initiator
  archetypes:
  - initiator
  - burst caster
  tier: C
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
  tier: C
  trend: rising
  why: "Melee-spirit assassin whose burst window grew \u2014 Leaping Slash T3 +60->+90\
    \ and Ava T3 6->8s \u2014 on a jungle that pays 10% more per camp she takes by\
    \ kill rather than clear. The comeback levers punish a snowball that stalls, so\
    \ she is a sharper diver with less margin; stacked-HP frontlines still cap her."
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
    damage and Ava T3 6->8s sharpen her melee-spirit burst and second pick; the raised
    non-hero comeback gold + tick souls punish a snowball that stalls.

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
Warden:
  name: Warden
  role: gun carry
  archetypes:
  - gun carry
  - late scaler
  tier: B
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
Lash:
  name: Lash
  role: mobile initiator
  archetypes:
  - mobile assassin
  - initiator
  tier: B
  trend: rising
  why: "Highest-pick S-tier initiator: his spirit stomp core is untouched, Grapple\
    \ T3 now adds +4m jump velocity, and Steam Vents now add +150% stamina regen \u2014\
    \ the dive-and-re-enter loop he wins on got more fuel. Silver and air-drag slows\
    \ remain the counter."
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
  notes: "Halloween 2026: Grapple T3 adds +4m jump velocity; Steam Vents now add +150%\
    \ stamina regen, which feeds his dash-and-re-enter pattern. Spirit stomp core\
    \ untouched.\nShh... This Won't Hurt a Bit. (10-20, indirect): districts and Steam\
    \ Vents extend his dive routes beyond three lanes, and hub fights at Bell Tower/Sunken\
    \ Plaza concentrate teams into Ground Strike; objective parries no longer reset.\n\
    Paint the Town: no direct change; new districts/Steam Vents extend his dive routes\
    \ and the green-lane roof/tree keeps permanent lane high ground \u2014 still S."
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
Sinclair:
  name: Sinclair
  role: burst cast/steal
  archetypes:
  - burst caster
  - mobile assassin
  tier: D
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
Venator:
  name: Venator
  role: gun carry
  archetypes:
  - gun carry
  - tank/frontline
  tier: D
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
The Doorman:
  name: The Doorman
  role: utility initiator
  archetypes:
  - initiator
  - burst caster
  tier: D
  trend: stable
  why: Popular but not-winning setup initiator (46.5% WR) whose Call Bell damage is
    fine but whose engage still arrives late; Luggage Cart T2 wall impact 75->90 gives
    the Bell Tower rope-kidnap real damage, yet tempo dive reaches him before the
    door is placed.
  core_items:
  - Mystic Burst
  - Extra Charge
  - Mystic Expansion
  - Rapid Recharge
  - Tankbuster
  - Boundless Spirit
  - Vortex Web
  - Slowing Hex
  - Veil Walker
  build_variants:
  - Bell carry (AoE spirit)
  - Kidnap / utility (Doorway pick)
  enabled_by:
  - Doorway isolate (answers Silver by removing the carry from a fight)
  - Bell Tower single rope + ~280 souls (Doorway kidnap)
  - AoE/charge spirit items (Mystic Expansion, Greater Expansion, Extra Charge)
  - high pick rate keeps a large coordinated-player base
  countered_by:
  - dive tempo (Yamato, Lash, Apollo, Holliday)
  - Doorway range cut 70->65m (08-12)
  - 'tempo meta: early snowball beats his delayed payoff'
  - Vortex Web/Slowing Hex being low-WR bait items
  last_changed_patch: Halloween 2026 + Gameplay Update
  notes: "10-30 Halloween + Gameplay Update: Luggage Cart T2 wall impact 75->90 is\
    \ a real engage buff (T3 is tagged nerf while the number moves -15s->-18s \u2014\
    \ direction unclear, treat as neutral); Shadow Weave's 6s pre-stealth wind-up\
    \ slows the invis-kidnap line and does not help his setup.\n10-20 Shh...: no direct\
    \ change; Bell Tower's single rope + ~280 souls keeps the Doorway kidnap real\
    \ \u2014 pre-place the door at the base before roping up.\nPaint the Town: no\
    \ direct change; Bell Tower's single rope and ~280-soul payout give his Doorway\
    \ a real kidnap objective play, but tempo dive still beats his setup."
  builds:
  - name: Bell carry (AoE spirit)
    damage: spirit
    core_items:
    - Mystic Burst
    - Extra Charge
    - Mystic Expansion
    - Rapid Recharge
    - Tankbuster
    - Boundless Spirit
    popularity: primary
    notes: Extra charges + AoE expansion + cooldown turn Call Bell into the 50-70k
      damage build creators call the real one; highest-WR staples (Tankbuster 51.2%,
      Boundless Spirit 57.4%).
  - name: Kidnap / utility (Doorway pick)
    damage: spirit
    core_items:
    - Vortex Web
    - Slowing Hex
    - Veil Walker
    - Improved Spirit
    - Greater Expansion
    popularity: secondary
    notes: Doorway-isolate pick build; hit by the 09-16 Veil Walker rework (lost Sprint
      Boots + movespeed-on-break, weakening the escape). Its staples were already
      his worst-WR buys (Vortex Web 45.1%, Slowing Hex 45.3%), matching the creator
      'kidnap build is the noob trap' claim; Shadow Weave is the nominal invis replacement
      but he gains far less from it than a gun carry.
  matchups:
    beats:
    - Silver
    loses_to:
    - Yamato
    - Lash
    - Apollo
  matchup_notes: 'No enemy pair cleared the sample threshold, so this is inference
    - low confidence. Doorway still isolates a carry, so he keeps a real answer to
    Silver, the meta''s top gun tank. He loses to dive tempo (Yamato, Lash, Apollo):
    they reach a squishy caster before Luggage Cart/Doorway set up - the same ''tempo
    beats setup'' pattern the 09-16 patch rewards.'
  confidence: 0.55
  released_on: null
  provisional: false
Billy:
  name: Billy
  role: tank/frontline
  archetypes:
  - tank/frontline
  - lane bully
  tier: C
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
  tier: S
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
Rem:
  name: Rem
  role: support/healer
  archetypes:
  - support/healer
  tier: D
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
  tier: D
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


## Win/pick-rate snapshot (last 14 days before this patch, ranked matches, high-rank filter)

hero | WR% | PR% | matches
Graves | 57.5 | 44.1 | 1169299
Paige | 55.6 | 27.8 | 736041
Rat King | 55.2 | 51.8 | 1371942
Seven | 54.7 | 32.5 | 859884
Baba | 54.4 | 13.9 | 368733
Kelvin | 54.3 | 13.4 | 355999
Victor | 54.3 | 32.7 | 866995
Haze | 53.2 | 44.3 | 1172144
Deadman Danny | 52.5 | 39.5 | 1046042
Ivy | 52.5 | 19.3 | 510355
Abrams | 52.3 | 31.3 | 829005
Lady Geist | 51.8 | 23.9 | 632381
Dynamo | 51.7 | 21.1 | 558002
Nurse Harrow | 51.3 | 46.6 | 1233133
Violet | 50.8 | 35.6 | 941789
Drifter | 50.7 | 39.4 | 1042956
Lash | 50.6 | 30.6 | 811432
Wraith | 50.4 | 35.4 | 936739
Mo & Krill | 49.7 | 19.3 | 511872
McGinnis | 49.3 | 12.6 | 334135
Warden | 49.2 | 15.0 | 397206
Infernus | 49.2 | 36.9 | 977074
Vindicta | 49.2 | 30.0 | 795091
Apollo | 49.0 | 27.6 | 732110
Billy | 48.8 | 33.0 | 874484
Bebop | 48.4 | 37.7 | 999672
Celeste | 48.2 | 33.8 | 894236
Calico | 48.1 | 15.1 | 400335
Grey Talon | 47.4 | 17.9 | 474188
Yamato | 47.2 | 27.8 | 737626
Holliday | 47.1 | 19.7 | 522857
Venator | 46.7 | 41.6 | 1101907
Solomon | 46.5 | 15.0 | 396838
Silver | 46.2 | 31.6 | 837108
Paradox | 46.1 | 25.0 | 662199
Vyper | 46.0 | 14.2 | 375079
Viscous | 45.9 | 12.8 | 339490
The Doorman | 45.6 | 15.1 | 401214
Rem | 45.2 | 30.7 | 814441
Shiv | 45.0 | 27.6 | 731168
Mina | 44.7 | 37.6 | 995850
Sinclair | 44.7 | 10.0 | 265700
Pocket | 44.3 | 17.1 | 453831
Mirage | 44.1 | 12.0 | 317388

## Heroes to analyze in this call

Vyper, Sinclair, Mina, Drifter, Venator, Victor, Paige, The Doorman, Billy, Graves, Apollo, Rem

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

## 2026-11-04

- Steam Vents still grant invisibility. Halloween only added +150% stamina regen on top.
  Never say they lost invisibility.
- General: an added effect is not a replacement. Say something was removed only when the
  notes say so.
- Lines under a "Street Brawl" header apply only to that mode. Never present them as
  main-game changes.
- Tiers come from measured match data, not from the notes. A heavily nerfed hero can still
  be the strongest hero: Baba took big nerfs on 10-30 and still has the top win rate.


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
