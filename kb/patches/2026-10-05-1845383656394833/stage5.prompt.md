# Task: verdicts for the reader's hero pool

Patch: Minor Update - 10-05-2026 (2026-10-05)

## Synthesis

{
 "patch_size": "minor",
 "size_why": "The defining move is a regression repair (trooper speed restored) plus targeted trims to two outliers (Rat King, Sinclair); there are no systems, economy, objective, or item changes, so the way games are won is untouched. Twenty-five line items sounds broad, but they cluster as tuning/fixes, not structural shifts.",
 "headline": "A regression-repair patch: lane wave tempo is fixed and two outliers are trimmed, but the map-economy lead engine is deliberately left alone.",
 "meta_thesis": {
  "previous": "Games are won in the map economy — guaranteed Tough Crate routes, Haunt camp farming and telegraphed hub fights — not the lane, with no comeback valve and late scalers only relieved by The Broker's ~30-min stall window.",
  "new": "The shape is unchanged: the map-economy lead engine still decides games, and this patch only restores intended lane wave cadence and trims two outliers. Restored trooper speed marginally re-weights the lane versus camp farming, but no economy, objective, item or comeback lever moved.",
  "relationship": "continuation",
  "why": "Drivers are the trooper-speed regression fix (restores baseline lane cadence, not a new tempo lever) and the Rat King/Sinclair kit trims; nothing touches souls, bounties, objectives or The Broker."
 },
 "winners": [
  {
   "hero": "Apollo",
   "why": "On-schedule wave crashes restore his lane-bully punish windows, and Rat King's frontline trim thins the competing A-tier bruiser pool.",
   "indirect": true
  },
  {
   "hero": "Paige",
   "why": "Lane-cadence fix maximizes the wave pressure her tempo-support identity trades on; still S.",
   "indirect": true
  },
  {
   "hero": "Billy",
   "why": "Restored wave timing helps his lane-bully all-in, though his real slide (slot lost to Mo & Krill) is unchanged.",
   "indirect": true
  },
  {
   "hero": "Mirage",
   "why": "Reliable trooper pathing lets split-push side-lane pressure convert on schedule instead of stalling.",
   "indirect": true
  }
 ],
 "losers": [
  {
   "hero": "Rat King",
   "why": "Banner ult gutted — cooldown 130->160, DR 20->15%, radius 24->20m, charge 12->10s, plus T1/T2/T3 talent strips (total DR 35->25%) — hitting the 61% WR outlier.",
   "indirect": false
  },
  {
   "hero": "Sinclair",
   "why": "Broad trim across lane, utility and ult — HP regen 2->1, gun falloff and bullet damage down, Rabbit Hex radius down, ult copy duration 12->9s / cooldown 40%->60%, Vexing Bolt halved on objectives.",
   "indirect": false
  },
  {
   "hero": "Sinclair duration build",
   "why": "With Hex radius and copy duration both cut, the duration-spirit build now leans entirely on stealing a strong enemy kit to function.",
   "indirect": false
  }
 ],
 "non_obvious_calls": [
  {
   "claim": "The trooper 'bug fix' is effectively a partial, unintended walk-back of the City Never Sleeps lane de-emphasis — it re-weights lane tempo upward against camp farming.",
   "why": "Restoring wave-crash timing re-opens dive/punish windows, benefiting lane bullies and split pushers the KB had ranked below AoE camp clearers.",
   "confidence": 0.45
  },
  {
   "claim": "Rat King stays A-tier despite the ult gutting; don't move him down a tier.",
   "why": "Base-kit buffs (Scrap Grenade 65->70, Rat Swarm 28->24s, bounce targeting fixed) offset the banner nerf, so this is a correction toward 50%, not a burial.",
   "confidence": 0.55
  },
  {
   "claim": "The quiet kill in this patch is Sinclair's Vexing Bolt doing half damage to objectives — a kit-steal pick's only structure pressure removed.",
   "why": "He was already C-tier per the KB; stripping objective damage leaves the pick with almost no win-condition beyond stealing a meta kit.",
   "confidence": 0.5
  },
  {
   "claim": "The single largest number swing here is Rat King's total banner DR going 35->25%, a team-fight-identity nerf, not a solo-stat trim.",
   "why": "Base 20->15% plus T3 15->10% compounds to a 10-point swing, hitting the AoE damage-reduction aura his comp play revolved around.",
   "confidence": 0.6
  }
 ],
 "uncertainties": [
  "The summary reports 25 general changes but only the trooper fix and two hero kits surfaced — other tuning may have landed unlisted.",
  "Whether the trooper speed fix over-corrects to faster-than-baseline waves rather than restoring the intended cadence.",
  "Whether Rat King's nerf is large enough to move a 61% WR toward 50% or just trims the ceiling.",
  "Whether Sinclair was already weak enough that this is a correction or a full burial, since no snapshot WR was given."
 ],
 "what_to_watch": [
  "Rat King win rate post-patch — does it fall below ~55%, validating the nerf?",
  "Sinclair pick rate — near-zero confirms the kit-steal slot is dead.",
  "Lane-phase dive/kill stats vs camp-farm souls — did restoring wave speed actually re-raise lane-bully WRs?",
  "Any follow-up hotfix to Tough Crates, still the KB's flagged farm-route risk."
 ]
}

## Hero analysis entries for the pool heroes

[
 {
  "hero": "Billy",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.4,
  "direct_reasons": [],
  "indirect_reasons": [
   "Trooper fix restores wave timing that his lane-bully all-in depends on."
  ],
  "build_changes": [],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Marginal lane-cadence help; his real slide (slot lost to Mo & Krill) is unchanged."
 },
 {
  "hero": "Mirage",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.4,
  "direct_reasons": [],
  "indirect_reasons": [
   "Trooper fix restores intended wave pathing, so pushed side-lane pressure converts on schedule for a split pusher."
  ],
  "build_changes": [],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Tiny split-push QoL from the trooper fix; the tempo economy still buries his scaling."
 },
 {
  "hero": "Infernus",
  "in_notes": false,
  "direction": "neutral",
  "magnitude": "none",
  "confidence": 0.75,
  "direct_reasons": [],
  "indirect_reasons": [],
  "build_changes": [],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "No change; burn gun/spirit carry unaffected, and the unverified napalm-amp removal isn't in these notes."
 },
 {
  "hero": "Wraith",
  "in_notes": false,
  "direction": "neutral",
  "magnitude": "none",
  "confidence": 0.75,
  "direct_reasons": [],
  "indirect_reasons": [],
  "build_changes": [],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "No change; pure-gun rebuild after 09-16 stands."
 },
 {
  "hero": "Paradox",
  "in_notes": false,
  "direction": "neutral",
  "magnitude": "none",
  "confidence": 0.75,
  "direct_reasons": [],
  "indirect_reasons": [],
  "build_changes": [],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "No change; roamer pick initiator unchanged."
 },
 {
  "hero": "Haze",
  "in_notes": false,
  "direction": "neutral",
  "magnitude": "none",
  "confidence": 0.75,
  "direct_reasons": [],
  "indirect_reasons": [],
  "build_changes": [],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "No change; Fixation tempo carry, weak T4 gun ceiling still caps her."
 },
 {
  "hero": "Holliday",
  "in_notes": false,
  "direction": "neutral",
  "magnitude": "none",
  "confidence": 0.75,
  "direct_reasons": [],
  "indirect_reasons": [],
  "build_changes": [],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "No change; mobile pick assassin holds A."
 },
 {
  "hero": "Shiv",
  "in_notes": false,
  "direction": "neutral",
  "magnitude": "none",
  "confidence": 0.75,
  "direct_reasons": [],
  "indirect_reasons": [],
  "build_changes": [],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "No change; anti-tank bruiser keeps rising."
 },
 {
  "hero": "Warden",
  "in_notes": false,
  "direction": "neutral",
  "magnitude": "none",
  "confidence": 0.75,
  "direct_reasons": [],
  "indirect_reasons": [],
  "build_changes": [],
  "tier_before": "C",
  "tier_after": "C",
  "one_liner": "No change; late gun scaler still punished by tempo."
 },
 {
  "hero": "Yamato",
  "in_notes": false,
  "direction": "neutral",
  "magnitude": "none",
  "confidence": 0.75,
  "direct_reasons": [],
  "indirect_reasons": [],
  "build_changes": [],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "No change; camp-clear burst assassin holds high A."
 },
 {
  "hero": "Mina",
  "in_notes": false,
  "direction": "neutral",
  "magnitude": "none",
  "confidence": 0.75,
  "direct_reasons": [],
  "indirect_reasons": [],
  "build_changes": [],
  "tier_before": "C",
  "tier_after": "C",
  "one_liner": "No change; single-target burst still can't kill tanks."
 },
 {
  "hero": "Drifter",
  "in_notes": false,
  "direction": "neutral",
  "magnitude": "none",
  "confidence": 0.75,
  "direct_reasons": [],
  "indirect_reasons": [],
  "build_changes": [],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "No change; blind-pickable bruiser holds A."
 },
 {
  "hero": "Venator",
  "in_notes": false,
  "direction": "neutral",
  "magnitude": "none",
  "confidence": 0.75,
  "direct_reasons": [],
  "indirect_reasons": [],
  "build_changes": [],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "No change; default gun carry unchanged."
 }
]

## Item analysis entries that mention a pool hero

[]

## Knowledge base entries for the pool heroes

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
  why: "Burn gun/spirit carry whose AoE still clears the new grouped, chasing Haunt\
    \ camps, so the patch's farm-route economy is roughly neutral for him and Dashfernus\
    \ (spirit dash) stays his stronger, untouched line. Watch item: an unverified\
    \ report that his global napalm team-damage amp was removed \u2014 it is not in\
    \ these notes."
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
  - Dynamo
  - Bebop
  - Vyper
  - Paradox
  - Yamato
  - Lash
  - tempo/snowball meta
  last_changed_patch: null
  notes: "City Never Sleeps (09-29): burn AoE clears the new grouped Haunt camps;\
    \ an unverified peercontent report that his global napalm team-damage amp was\
    \ removed is not in the notes \u2014 confirm via win rate.\n09-16 (indirect):\
    \ Spiritual Overflow nerfed (40->30 spirit, 30->25% fire rate) \u2014 burn gun\
    \ build drops it for Toxic Bullets/Swift Striker; Dashfernus untouched.\nCorrection\
    \ accepted: not a pure gun hero \u2014 spirit items lead on both share and WR,\
    \ so both builds kept; spirit build edges out gun."
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
Paradox:
  name: Paradox
  role: pick/sniper initiator
  archetypes:
  - burst caster
  - initiator
  - poke/siege
  tier: B
  trend: rising
  why: 'Pick/sniper whose roamer identity is the winner here: new districts, more
    hiding spots and Steam-Vent invisibility upgrade her pick setups and put her ahead
    of Bebop in the roamer slot. Her stationary Carbine sniper line still folds to
    the meta''s mobile divers (Yamato, Lash, Holliday).'
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
  notes: 'City Never Sleeps (09-29, indirect): new districts/hiding spots/Steam Vents
    upgrade her roamer pick setups and move her ahead of Bebop in that slot; the sniper
    line still folds to mobile divers.

    Data disagrees with the old ''Echo Shard every game'' read: the real core is a
    gun/carbine sniper, and Slowing Hex is 60%, not guaranteed.

    Changelog 09-16: Kinetic Carbine min-damage multiplier 25->10% and no longer scaled
    by T3; Slowing Hex cooldown up.'
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
Haze:
  name: Haze
  role: gun carry
  archetypes:
  - gun carry
  tier: B
  trend: rising
  why: 'Haze is a tempo gun carry: the Fixation buff (headshot stacks 2->3, higher
    T3 weapon scaling) lifts exactly the early-mid damage that wins lane, and 09-16
    gutted comeback souls so a won lane converts to a win. But her ceiling still sits
    on weak T4 gun items (Ricochet/Capacitor) and the meta''s mobile divers and lane
    bullies hunt her low-mobility frame, so a 49.8% WR caps her at B. Strong tempo
    pick, not a top one.'
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
  last_changed_patch: Minor Update - 09-16-2026
  notes: "09-16 (indirect): Plated Armor's on-hit fix now blanks Tesla Bullets spirit\
    \ damage, weakening her Ricochet/Tesla late pivot.\nRole reframed per reader:\
    \ farm-carry is meta-dependent, not her identity \u2014 historically a Smoke Bomb\
    \ roamer/ganker on isolated targets, and T4 weakness gates the late-scaler label.\n\
    Changelog: Minor Update - 09-16-2026 \u2014 Fixation headshot stacks 2->3, higher\
    \ T3 weapon scaling."
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
Holliday:
  name: Holliday
  role: mobile assassin
  archetypes:
  - mobile assassin
  - initiator
  tier: A
  trend: rising
  why: 'Mobile pick assassin built for the new map: new districts, more hiding spots
    and Steam-Vent invisibility expand her roam routes, and the Bell Tower hub fights
    reward Spirit Lasso picks. She still loses to point-blank lockdown (Drifter, Bebop,
    Mo & Krill/Lash ults) that punishes her commit-heavy entry.'
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
  notes: "City Never Sleeps (09-29, indirect): new districts/hiding spots/Steam Vents\
    \ expand her roam routes and Bell Tower hub fights reward lasso picks.\nChangelog\
    \ 09-16: Crackshot T2 resist-shred, longer Spirit Lasso, health/boon 41->43; Veil\
    \ Walker lost Sprint Boots and movespeed-on-break.\nDisagreement: heresy (09-17)\
    \ frames a 'gun hybrid' \u2014 ranked data shows a spirit charge/duration build\
    \ with no gun items beyond Recharging Rush, so treat 'gun hybrid' as a skirmish\
    \ label, not a build."
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
Warden:
  name: Warden
  role: gun carry
  archetypes:
  - gun carry
  - late scaler
  tier: C
  trend: falling
  why: 'Late-scaling gun carry the no-comeback, farm-route economy refuses to wait
    for: tempo now runs through crate routes and hub objectives rather than lane brawling,
    and Shadow Weave''s invis-engage gains little from the new Steam-Vent/district
    layout. His 09-16 cuts (bullet dmg/boon, flask range/speed, Willpower T3, nerfed
    T4 gun finishers) are still unanswered.'
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
  notes: 'City Never Sleeps: no direct line; the farm-route/no-comeback economy still
    refuses to wait for a late gun scaler, and Shadow Weave gains little from the
    new Steam-Vent/district layout.

    One dominant gun build; the ''cage'' is a Willpower choice, not an item path.

    09-16: bullet dmg/boon, flask range/speed, Willpower T3 cut; Mercurial Magnum
    + Spiritual Overflow nerfed, Veil Walker stripped.'
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
Yamato:
  name: Yamato
  role: mobile burst assassin
  archetypes:
  - mobile assassin
  - burst caster
  tier: A
  trend: rising
  why: 'The patch''s camp-clear champion: Flying Strike now creates paths against
    solid targets (turrets, Shrines, objectives) for extra mobility and objective
    access, and her punch AoE gathers the new grouped, chasing Haunt camps faster
    than almost anyone. Tempo burst plus point-click Spirit Snatch still deletes squishy
    carries; sustain tanks and anti-heal cap her at the top of A, toward S.'
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
  last_changed_patch: City Never Sleeps
  notes: "City Never Sleeps: Flying Strike now creates paths against solid targets\
    \ (turrets, Shrines, objectives) \u2014 new mobility/objective access \u2014 and\
    \ she is the patch's camp-clear champion vs the grouped Haunt camps.\nTankbuster\
    \ is 39% share at a 25m average buy (late luxury, not core); the Refresher build\
    \ stays niche/creator-driven.\n09-16: Crimson Slash T3 heal spirit scaling +0.4,\
    \ Flying Slash light-melee scaling 1.0->1.2."
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
Mirage:
  name: Mirage
  role: split-push hybrid carry
  archetypes:
  - gun carry
  - split pusher
  - late scaler
  tier: B
  trend: falling
  why: 'Slow teleport/split-push scaler that the 09-16 economy punishes hardest: comeback
    souls are gone and early Rift is now a real fight, so his map-play rarely comes
    online (46.3% WR, 39-45% into mobile bruisers). Kit intact - he is beaten by the
    meta, not the notes. Toxic Bullets'' scaling buff (0.005->0.006) gives his spirit-amp
    core a small offset.'
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
  notes: 'Changelog: 09-16 - no Mirage line; tier stays B; hurt by the gutted comeback/tempo
    system changes, partially offset by the Toxic Bullets scaling buff in his spirit-amp
    core.

    Data over creators: 30-day high-rank usage shows a spirit-amp hybrid core (Mystic
    Regen/Healbane/Mystic Vulnerability), not the Echo Shard-Scourge-Inhibitor build
    the summer creators cited - Echo Shard is ~0% now.

    Low confidence on whether the new air-drag slow interacts with Dust Devil''s lift.'
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
Mina:
  name: Mina
  role: mobile spirit assassin
  archetypes:
  - mobile assassin
  - burst caster
  tier: C
  trend: stable
  why: 'Overloaded mobile burst assassin still stuck at C: the camp/uptime patch rewards
    her grouped-camp AoE clear and new-district mobility, but her single-target rotation
    does not kill through the tank front line (Billy, Mo & Krill, Victor) and Yamato
    owns the mobile-burst niche. The damage gap is a rework problem, not a numbers
    one.'
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
  notes: 'City Never Sleeps: no direct line; the camp/uptime patch rewards her grouped-camp
    AoE clear and new-district mobility, but her damage gap is unchanged.

    One spirit build (Extra Spirit/Mystic Burst/Quicksilver Reload ~100%); only late
    anti-tank items diverge.

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
Drifter:
  name: Drifter
  role: melee bruiser
  archetypes:
  - mobile assassin
  - tank/frontline
  tier: A
  trend: rising
  why: Blind-pickable spirit-melee bruiser still on the field's highest pick rate;
    the City Never Sleeps layout adds hiding spots, Steam Vents and heavy-melee Tough-Crate
    routes that suit a stealth-revealing melee roam. He still lacks hard CC and closing
    mobility, so a 51.4% WR floor and rising Dynamo/Mo & Krill/Apollo lane pressure
    cap him at A.
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
  notes: '09-29 City Never Sleeps: no direct change - new districts/Steam Vents and
    heavy-melee Tough-Crate routes fit his stealth-reveal roam (peercontent, unverified).

    Dropped KB core_items Decay/Toxic Bullets/Fortitude - none show in current 30-day
    usage; the ''Toxic Bullets bot'' framing is a 2026-04 artifact (data over creator).
    Celeste falling softens one losing matchup, but Dynamo/Mo & Krill/Apollo rising
    worsen others - net stable. 09-16 Minor Update: no direct Drifter change; gutted
    comeback souls and ramped rift resist suit his early-bruiser floor.'
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
Venator:
  name: Venator
  role: gun carry
  archetypes:
  - gun carry
  - tank/frontline
  tier: A
  trend: rising
  why: Hugely popular default gun carry (28.7% PR) at 45.7% WR - not a free win. The
    09-16 Ira Domini buff (now chains Ricochet/Split Shot into 3 bolts) raises his
    late ceiling and slots him ahead of Haze, but hard-CC frontlines (Abrams, Lash)
    and a tempo meta that ends before his tank items cap him under S. The Weakening
    Headshot -13->-12% trim slightly widens his cheap-shred gap to buffed Hollow Point.
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
  last_changed_patch: Minor Update - 09-16-2026
  notes: 'Changelog: 09-16 - Ira Domini now works with Ricochet/Split Shot (3 bolts);
    Weakening Headshot -13->-12% nudges his lane shred relative to buffed Hollow Point.
    Snapshot is 14 days and mostly pre-patch - treat WRs as baseline.

    Data over creators: Fortitude and Hollow Point dropped from core (not in usage);
    Battle Vest (90% share) is the real first buy. Creator ''S-tier, no weak point''
    read is contradicted by his 45.7% WR.

    Two-build reality: gun bruiser is primary (70-90% shares), a ~40% grenade pivot
    is the secondary late option.'
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
  matchup_notes: "Beats fellow gun carries by out-tanking and out-sustaining them\
    \ \u2014 Haze 48% and Wraith 47% match the reader note that he is the better pick\
    \ in that slot. Loses to gap-closing frontline CC (Abrams 38%, Lash 43%) that\
    \ locks him out of his own range. Vindicta's 39% is likely a lagging pre-patch\
    \ number \u2014 she is falling and flyers were hurt this patch."
  confidence: 0.6
Billy:
  name: Billy
  role: tank/frontline
  archetypes:
  - tank/frontline
  - lane bully
  tier: A
  trend: falling
  why: 'Lobby-default frontline whose lane-bully all-in the map-economy patch suits
    less: the crate/camp meta wants sustained uptime, and his front-line slot has
    visibly moved to rising Mo & Krill. Anti-tank Shiv remains his worst lane and
    is climbing, so he slides off S.'
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
  notes: '09-29 City Never Sleeps: no direct change; the crate/camp-uptime meta wants
    sustained presence and his front-line slot moved to rising Mo & Krill, with anti-tank
    Shiv climbing - S was popularity-supported, so slides to A (peercontent, unverified).

    Changelog: 09-16 - no direct line; item tailwinds (Lifestrike heal/slow, Fortitude
    regen) and the lane-wins meta supported him.

    Data beats creators: Lifestrike, Echo Shard, Witchmail and Scourge/Scrooge never
    appear in his top-15 buys - real core is Spirit Snatch (95%), Stalker (90%), Close
    Quarters (88%), Monster Rounds (86%), Grit (83%).'
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


## The reader's pool

Venator, Haze, Wraith, Warden, Shiv, Yamato, Mina, Paradox, Mirage, Infernus, Holliday, Drifter, Billy

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
