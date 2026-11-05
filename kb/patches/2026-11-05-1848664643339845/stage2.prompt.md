# Task: item analysis

Patch: Minor Update - 11-04-2026 (2026-11-05)

## Reader corrections (authoritative, overrides the knowledge base)

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


## Systems analysis of this patch (already done)

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

## Item changes in this patch (grouped by item)

Healbane:
  - [rework] Healbane: Stacks now diminish 20% more aggressively (at 2 stacks 57.8%->54.7%, at 4 stacks 82.2% to 72%)

## Knowledge base: the changed items (who buys them and why)

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
  notes: "10-30 rework, the patch's key system move: multi-source anti-heal now stacks\
    \ with diminishing returns, so two sources beat one strong healer \u2014 anti-heal\
    \ is a team coverage plan, not a slot. Heal-on-kill 275->170 (+3/boon) taxes frontline\
    \ buyers' own sustain. Best-in-class for buyers who want the enemy's healing gone\
    \ (Seven); worst for heroes who live on their own heals (Mo & Krill, Shiv, Kelvin,\
    \ Ivy)."


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
Kelvin:
  name: Kelvin
  role: support/healer
  archetypes:
  - support/healer
  - late scaler
  tier: S
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
