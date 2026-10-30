# Task: synthesis (the verdict and the meta thesis)

Patch: Halloween 2026 + Gameplay Update (2026-10-30)
Change counts: General 268, total 268

## Update summary

(n/a)

## Previous meta thesis (knowledge base, pre-patch)

# Meta state
Last patch: Shh... This Won't Hurt a Bit. (2026-10-20)

## Thesis
Souls sit off-lane now: four corridors, nine Haunt types and contested hubs pay better than lane static, so income is a coverage problem a five-man team cannot solve — AoE camp clearers and heavy-melee crate openers bank first, single-target lane bullies and split pushers starve. Fights get scheduled at Bell Tower, Sunken Plaza and Buff Container spawns instead of picked in lane. Tempo still closes most lobbies before a late spike, but the wider map hands late scalers a longer leash than Paint the Town did.

## Economy and systems
- Comeback bounties stay trimmed; extra comeback souls reroute to the two lowest-econ players via tick gold. Leads stick.
- Guardian bounty +10%, Walker +5%, objective share 30->25% (09-16, holds).
- Kill income is contested: the Soul Bag must be last-hit after the kill, so secure-burst conversions stay unreliable.
- Objective parries no longer reset the parry cooldown — Guardian and Shrine dives are one-shot commitments.
- Respawn 38s at 20m; slows -20% globally, air drag 35% — grounded kiting strong, flyers taxed.
- The Broker spawns ~30 min then ~every 15 min, relocates per match and is not on the map; Corrupted rolls are symmetric, public and a runtime read.
- Cast-on-press: abilities fire on the input, not the next window — tightens combos and clutch parries for high-execution kits.

## Map
Lanes renamed; four districts plus off-lane corridors. Every neutral camp is one of nine Haunt creature types — they group, chase and hit harder, souls varying by type. Farm: Tough Crates (58 souls, guaranteed) need Heavy Melee; Barrel Mimics turn breakable-chaining into a fight rather than free tempo; Haunt camps; Sinner's Sacrifice variants; Buff Containers roll permanent Move Speed and Bullet/Spirit Resist alongside ability range, so tanks contest them. Pickups: Healing Snacks (10% max HP) and Steam Vents (invisibility roams). Hubs: Sunken Plaza (~5-8 min, stamina strip) and Bell Tower (8+, ~280 souls, one rope, three vaults, map-wide bell broadcast). Green lane holds a roof/tree above the bridge. Side asymmetry: Arch Mother's side owns Sunken Plaza plus the theater.

## Archetype standing
- AoE/sustain camp clearers: up — grouped, chasing Haunts make AoE the fastest income (Seven, Yamato, McGinnis, Infernus, Mina).
- Heavy-melee frontline/tanks: up — Tough Crates plus camp chip damage reward Heavy Melee and regen (Mo & Krill, Abrams, Rat King, Drifter).
- Sustain bruisers: up — harder camps reward regen stacks (Victor, Shiv, Kelvin).
- Roamers/pick assassins: up — corridors, Steam Vents and new hiding spots add angles (Holliday, Lash, Paradox, Drifter); Bebop's hook cannot convert on spread farm.
- Lane bullies: up — crate routes from ~2:30 convert lane pressure (Paige, Apollo), though Apollo's Guardian dive is now one-shot.
- Late scalers / split pushers: down — lane shoving converts to less income; the ~30-min Broker stock is the only real late spike (Mirage, Warden, Celeste, Graves).
- Flyers: down — air drag unchanged while vents hand divers an approach (Grey Talon, Celeste, Deadman Danny).
- Non-melee assassins: down — Calico's cat form still cannot heavy-melee the crate economy.
- Pre-placed trap/zone heroes: down — Graves' gun deletes Venator traps.

## Watchlist
- Per-Haunt-type souls and clear speed: if one type dominates, routes re-converge and the no-memorization intent fails.
- Average game length and share of games reaching the ~30-min Broker — the cleanest tempo-vs-stall test.
- Buff Container contest rate, especially Bullet Resist and Move Speed rolls.
- Steam Vent kill participation: if vent ganks spike, grouping discipline becomes the skill gap.
- Graves snapshot (56.5% WR / 40.9% PR) still conflicts with the KB (48.5% / 21%) — recheck.
- Rat King win rate against pick rate — an A-to-S jump this fast needs data.

## Recent history
- Shh... This Won't Hurt a Bit. (2026-10-20): off-lane corridors and hub fights priced in; Haunt behaviors, Barrel Mimics, Steam Vents, Healing Snacks, instant casts; Graves gun destroys Venator traps; Corrupted items at the Broker.
- Paint the Town (2026-10-16): nine Haunt camp types replace all neutrals, contested Soul Bags, objective-parry cooldown reset removed, permanent-stat Buff Containers, Corrupted tier, six vote-gated new heroes.
- Minor Update - 10-14-2026: Baba frontline cut; Deadman Danny buff package; Radiant Regeneration third trim.
- Minor Update - 10-05-2026: trooper-speed regression fixed; Rat King and Sinclair trimmed.
- City Never Sleeps: renamed lanes, four districts, Haunt camps replace neutrals, Tough Crate/Broker economy.


## Systems analysis

{
 "systems_changed": [
  {
   "system": "Jungle / Haunt camps",
   "change_summary": "Haunt base bounty and growth +10%, but Haunt HP and damage +10%. Camps pay more at every stage of the game and hit back harder, so clear speed and sustain become the real gate on jungle income.",
   "driving_changes": [
    "Haunts base bounty and growth increased by 10%",
    "Haunts HP and Damage output increased by 10%"
   ],
   "magnitude": "major",
   "effect_on_play": "AoE/sustain clearers bank faster and chain camps without backing; slow or single-target clearers lose HP per camp and start skipping camps, and the gap between the two widens every minute. Jungle income is now a clear-quality test, not a routing test."
  },
  {
   "system": "Comeback economy (non-hero souls)",
   "change_summary": "Comeback gold from non-hero sources caps at 30% (was 26%), and the behind-multiplier now also boosts tick souls for the two poorest players. The trailing team gets paid continuously off farm, not only on kills.",
   "driving_changes": [
    "Comeback gold from non-hero sources increased from a max of 26% to 30% (when behind by ~20% Net Worth)",
    "The bonus NPC souls multiplier when behind now also increases tick souls for the 2 poorest players"
   ],
   "magnitude": "major",
   "effect_on_play": "A losing econ now compounds instead of stagnating, so the KB's 'leads stick' premise is reversed. A team that is ahead must convert into Guardians/Walkers fast, because the losing team's item floor keeps rising while they farm."
  },
  {
   "system": "Haunted Souls securing",
   "change_summary": "Secure rate is 25% slower at baseline but up to 50% faster scaled to net-worth deficit, maxing at a 20% gap. Contested farm souls favor the team that is behind and are harder for the leader to lock down.",
   "driving_changes": [
    "Haunted Souls secure rate is now 25% slower",
    "Haunted Souls secure rate is now up to 50% faster than baseline based on how far behind you are in Net Worth compared to the enemy team's average (max rate at a 20% Net Worth gap)"
   ],
   "magnitude": "major",
   "effect_on_play": "Camp contests turn into a lever for the losing side: a diver who is behind can steal the Haunt soul the leader is channelling. Leaders must kill and secure in one clean pass rather than drag out camp fights."
  },
  {
   "system": "Breakables / crate economy",
   "change_summary": "Breakable growth values cut 10% and the box-respawn stall bug fixed. Crates stay the guaranteed-souls floor but no longer scale into the mid game.",
   "driving_changes": [
    "Breakables growth values reduced by 10%",
    "Fixed some boxes taking longer to respawn if another box's or powerup's pickup was left on the ground"
   ],
   "magnitude": "moderate",
   "effect_on_play": "Heavy-melee crate routing is a lane-phase income tool now, not a 20-minute side stream; crate openers must graduate to Haunt camps or fights to keep pace."
  },
  {
   "system": "Halloween Cauldrons / Candy (Sugar Rush)",
   "change_summary": "New Heavy-Melee-breakable cauldrons drop Candy stashed in the player's pocket, consumed later for a temporary Sugar Rush buff. Event runs through Nov 2, so it is a timed layer on the map, not a permanent one.",
   "driving_changes": [
    "With a Heavy Melee, break the cauldron to pick up a piece of Candy and stash it in your pocket for later",
    "you can consume the candy to grant yourself a boost of energy with the temporary Sugar Rush buff",
    "The Halloween festivities are available in-game now through November 2nd, 2026."
   ],
   "magnitude": "minor",
   "effect_on_play": "Heavy Melee gains a second detour reason alongside crates, and fights can be pre-loaded with a stored buff instead of bought from a shop. Sugar Rush's exact stats are unclear from the notes; treat it as a tempo consumable, not a build item."
  },
  {
   "system": "Steam Vents / movement utility",
   "change_summary": "Steam Vents now grant +150% stamina regeneration, reworking the stealth-roam role the KB had priced in. Vents become a stamina battery rather than a free approach.",
   "driving_changes": [
    "Steam Vents now increase stamina regeneration by 150%"
   ],
   "magnitude": "moderate",
   "effect_on_play": "Vent play converts from invisibility ganks into extra dashes mid-fight or mid-rotation, which helps stamina-hungry divers and tanks more than it helps gankers; the KB's 'vent gank' discipline test loses its main driver."
  },
  {
   "system": "Air drag / slows",
   "change_summary": "Move-slow-to-air-drag ratio 0.35 -> 0.5, so slows bite harder on airborne movement.",
   "driving_changes": [
    "Move slow to air drag ratio increased from 0.35 to 0.5"
   ],
   "magnitude": "moderate",
   "effect_on_play": "Flyers and airborne escapes bleed more speed under a slow, so slow application gets stronger and grounded kiting harder to escape. This deepens the flyer tax; heroes that live in the air need a slow cleanse or a different exit."
  },
  {
   "system": "Tunnels",
   "change_summary": "Tunnel move speed +70% -> +50%. The fastest corridor rotation on the map is slower.",
   "driving_changes": [
    "Move speed in tunnels reduced from +70% to +50%"
   ],
   "magnitude": "minor",
   "effect_on_play": "Flank and respawn-to-hub timings lengthen by a beat; teams already staged at Bell Tower/Sunken Plaza get a small edge over teams rotating through tunnels."
  },
  {
   "system": "Ranked draft / new-hero eligibility",
   "change_summary": "The latest six heroes lose the 'new' flag: normal unlock requirements in ranked, and they can now be banned.",
   "driving_changes": [
    "Latest 6 heroes are no longer categorized as \"new\" anymore. This means they have normal hero unlocking requirements for ranked and can now be banned."
   ],
   "magnitude": "moderate",
   "effect_on_play": "Their pick rates get capped by bans and their win rates regress toward the field; the vote-gated six stop being a free pick and enter normal draft counterplay, which disproportionately hits whichever of the six the snapshot shows as overtuned."
  }
 ],
 "tempo_shift": {
  "direction": "toward_scaling",
  "confidence": 0.6,
  "why": "Three coordinated comeback levers (30% non-hero comeback cap, tick souls to the two poorest, 25%-to-50% faster secure when behind) attack the lead-holding pattern the KB called out, and Haunt bounty/growth +10% gives the trailing team a compounding farm floor toward the ~30-min Broker. The opposing pull (Haunts hit +10% harder, faster clearers snowball harder) is real but narrower in scope."
 },
 "archetype_effects": [
  {
   "archetype": "tank/frontline",
   "direction": "up",
   "magnitude": "moderate",
   "why": "Haunt damage +10% and Healing Snacks 10%->14% max HP pay regen and HP stacking, and Heavy Melee now opens both crates and candy cauldrons."
  },
  {
   "archetype": "spirit carry",
   "direction": "up",
   "magnitude": "moderate",
   "why": "Haunt bounty and growth +10% is pure profit for AoE camp clearers, who dodge most of the Haunt HP +10% cost because they one-cycle the camp."
  },
  {
   "archetype": "late scaler",
   "direction": "up",
   "magnitude": "moderate",
   "why": "30% non-hero comeback gold plus tick souls to the two poorest gives a trailing scaler a guaranteed item floor to reach the ~30-min Broker, which the KB called the only real late spike."
  },
  {
   "archetype": "lane bully",
   "direction": "down",
   "magnitude": "minor",
   "why": "Breakables growth -10% trims the guaranteed crate souls that converted early lane pressure, while the lane itself is untouched and Haunt income rose relative to it."
  },
  {
   "archetype": "mobile assassin",
   "direction": "neutral",
   "magnitude": "minor",
   "why": "Steam Vents trade stealth approach for +150% stamina regen (more dashes in-fight) while tunnels drop +70%->+50% and the air-drag ratio 0.35->0.5 taxes airborne exits — gankers gain fight mobility, lose the free angle."
  },
  {
   "archetype": "split pusher",
   "direction": "down",
   "magnitude": "minor",
   "why": "Breakables growth -10% and slower tunnel rotations both cut the side-lane payout and rotation speed that split pushing was converting into income."
  }
 ],
 "intent_read": "Valve is removing the structural reason leads were unbreakable: instead of a kill-bounty comeback, the comeback valve now sits inside farm itself (secure rate for the trailing side, tick souls to the two poorest, 30% non-hero comeback gold). At the same time, Haunt HP/damage +10% keeps the off-lane map the skill test — income still comes from the jungle, but the jungle now actively redistributes it toward the team that is behind."
}

## Item analysis

{
 "items": [
  {
   "item": "High-Velocity Rounds",
   "direction": "nerf",
   "magnitude": "moderate",
   "summary": "Velocity-only trim: the item keeps its slot but stops guaranteeing max-range hits land, so poke carries lose effective DPS without losing a build slot. The 15-point cut bites the heroes who buy it for range upkeep, not the brawlers buying it for cheap weapon stats at 2-3 minutes.",
   "affected_heroes": [
    {
     "hero": "Vindicta",
     "relationship": "core",
     "effect": "down",
     "why": "HVR is her gun-poke velocity backbone; at 60->45% she misses more max-range shots exactly where her new-roofs hub-poke value lives."
    },
    {
     "hero": "Grey Talon",
     "relationship": "core",
     "effect": "down",
     "why": "Already C-tier with no camp or crate route; leading arrows at range got harder on top of the flyer tax."
    },
    {
     "hero": "Warden",
     "relationship": "core",
     "effect": "down",
     "why": "He buys it as a stat package, so the velocity loss is a small tax on a hero the tempo meta already kills."
    },
    {
     "hero": "Victor",
     "relationship": "core",
     "effect": "neutral",
     "why": "His 2.4-min buy is a lane last-hit stat-stick; bullet velocity is incidental to the spirit-sustain plan."
    },
    {
     "hero": "Rat King",
     "relationship": "core",
     "effect": "neutral",
     "why": "Monster Rounds -> HVR -> Opening Rounds is a lane package, and his damage is grenade/AoE, not leading shots."
    }
   ],
   "build_shift": "It is still the only cheap velocity slot, but at 45% the brawlier T2s buffed this patch (Battle Vest, Bullet Lifesteal) compete harder for the same weapon slot."
  },
  {
   "item": "Express Shot",
   "direction": "nerf",
   "magnitude": "minor",
   "summary": "5% off secondary-fire damage and growth trims the carbine/crit burst of its three users without removing it from their builds; it is a pick-damage cut, not a DPS cut.",
   "affected_heroes": [
    {
     "hero": "Paradox",
     "relationship": "core",
     "effect": "down",
     "why": "Express Shot rewards Kinetic Carbine crits, so the cut lands on the pick burst her whole roamer identity converts into kills."
    },
    {
     "hero": "Deadman Danny",
     "relationship": "situational",
     "effect": "down",
     "why": "His surviving gun skeleton already runs below his spirit build; a secondary-fire trim confirms spirit as the only path."
    },
    {
     "hero": "Viscous",
     "relationship": "core",
     "effect": "down",
     "why": "Express Shot rides in the spirit-hybrid Splatter/Punch shell; small, but he has no other damage line to trade into."
    }
   ],
   "build_shift": ""
  },
  {
   "item": "Point Blank",
   "direction": "buff",
   "magnitude": "minor",
   "summary": "Half a second more slow is worth more than the line reads because the air-drag ratio went 0.35->0.5 in the same patch: the same slow now bleeds more speed from anyone airborne, so close-range slow application is stickier than before. Low confidence on buyers — no KB usage.",
   "affected_heroes": [
    {
     "hero": "Venator",
     "relationship": "new_option",
     "effect": "up",
     "why": "Gun bruiser whose whole plan is standing in melee range; a longer close-range slow keeps targets inside his M1 window (not in his current KB core — inference only)."
    }
   ],
   "build_shift": "Slows as a category got stronger via air drag, so any slow rider on a weapon item is priced higher than it was on 10-29."
  },
  {
   "item": "Hunter's Aura",
   "direction": "nerf",
   "magnitude": "moderate",
   "summary": "LOS gating converts the aura from a debuff you carried through walls into a frontline-only effect: it no longer pays until contact, which removes the pre-fight value of stacking it before you commit. That lands squarely on the melee-front archetype the patch otherwise lifted.",
   "affected_heroes": [
    {
     "hero": "Abrams",
     "relationship": "core",
     "effect": "down",
     "why": "His primary melee-brawler build buys it mid-game; Shoulder Charge/Siphon engages through geometry now lose the aura until he is literally on top of the target."
    },
    {
     "hero": "Silver",
     "relationship": "core",
     "effect": "down",
     "why": "Gun tank wants the shred aura up while she walks in; LOS gating delays it by exactly the approach distance she pays tank stats to survive."
    },
    {
     "hero": "Yamato",
     "relationship": "situational",
     "effect": "down",
     "why": "Her late spirit-burst line uses it as a shred amplifier; fights started through walls or from stealth now begin without it."
    }
   ],
   "build_shift": "Auras that require LOS compete worse against self-buffs (Battle Vest, Bullet Lifesteal) that never turn off."
  },
  {
   "item": "Shadow Weave",
   "direction": "rework",
   "magnitude": "major",
   "summary": "It stopped being a burst-window item and became a setup item: you lose fire rate and melee damage, gain +50% ambush weapon damage that only reaches full power after 6 seconds of stealth. Reactive stealth-then-hit use now gets a fraction of the payout, and the patch already handed every hero a vent-based approach, so Warden's exclusivity erodes further.",
   "affected_heroes": [
    {
     "hero": "Warden",
     "relationship": "core",
     "effect": "down",
     "why": "His cage-bruiser build bought it for the fire rate a gun carry wants and for an engage-on-demand; he now must pre-stealth 6s before landing Willpower, which tempo comps punish, and abilities breaking stealth gaining the bonus does not help a gun-first kit."
    }
   ],
   "build_shift": "Ambush has a wind-up now, so the item rewards premeditated roams over reactive disengage — the same currency Steam Vents just repriced from free approach to stamina."
  },
  {
   "item": "Toxic Bullets",
   "direction": "buff",
   "magnitude": "minor",
   "summary": "40% anti-heal on the burn slot is the biggest single anti-heal number in the patch, and it stacks into Healbane's new multi-source reduction. With Radiant Regeneration and Healing Booster trimmed, the sustained anti-heal buyer is now the answer to the healing archetype rather than a counter-pick.",
   "affected_heroes": [
    {
     "hero": "Infernus",
     "relationship": "core",
     "effect": "up",
     "why": "Burn + 40% heal cut is his best line into the sustain fronts and healing supports that survive his poke; his gun build's weakest slot gets a real reason to exist."
    },
    {
     "hero": "Mirage",
     "relationship": "core",
     "effect": "up",
     "why": "He buys it in the near-universal spirit-amp hybrid core; the deeper heal cut is the one thing on his item list that got better in a patch that buried him."
    },
    {
     "hero": "Drifter",
     "relationship": "situational",
     "effect": "up",
     "why": "Anti-heal bruiser variant layered on built-in anti-heal; stacking sources now composes instead of overwriting."
    },
    {
     "hero": "Graves",
     "relationship": "situational",
     "effect": "up",
     "why": "Her on-hit gun path uses it vs tanks; the deeper cut helps her lane but does not fix her scaling window."
    }
   ],
   "build_shift": ""
  },
  {
   "item": "Decay",
   "direction": "nerf",
   "magnitude": "minor",
   "summary": "The notes' [nerf] tag points at the holder's side of the trade deepening (-50%->-55% incoming heal reduction) while the anti-heal it applies to enemies is untouched; if the number is actually the enemy-side debuff, flip the read. Either way it is a 5-point move on the default anti-heal slot, and Healbane now stacking means it is no longer the only answer.",
   "affected_heroes": [
    {
     "hero": "Mo & Krill",
     "relationship": "core",
     "effect": "down",
     "why": "Scorn sustain plus his own incoming heals — the item's drawback costs him the most of any buyer."
    },
    {
     "hero": "Shiv",
     "relationship": "core",
     "effect": "down",
     "why": "Regen-ramp bruiser whose entire survivability model is healing received; a deeper incoming-heal penalty cuts into the ramp."
    },
    {
     "hero": "Lady Geist",
     "relationship": "core",
     "effect": "down",
     "why": "Her Soul Exchange/Life Drain plan already pays a regen tax from Radiant Regeneration trims; a second heal penalty stacks on the same stat."
    },
    {
     "hero": "Abrams",
     "relationship": "core",
     "effect": "down",
     "why": "Siphon-based sustain buys Decay for anti-heal and eats the drawback on the same resource he fights with."
    }
   ],
   "build_shift": "Anti-heal moves toward Healbane (now stacking) and Toxic Bullets, which carry no self-cost; Decay becomes the anti-heal of last resort."
  },
  {
   "item": "Radiant Regeneration",
   "direction": "nerf",
   "magnitude": "major",
   "summary": "Fourth cumulative trim, now structural: heal-on-cast only fires in combat, cut 65->40 with boon scaling 1.7->1.4 and spirit 0.35->0.25. The regen shell stops paying between fights — which is exactly the farm-route sustain the +10% Haunt damage now demands — so the regen-bruiser archetype loses its out-of-combat engine, not just some fight healing.",
   "affected_heroes": [
    {
     "hero": "Baba",
     "relationship": "core",
     "effect": "down",
     "why": "94% buy rate and her C-tier status rests on out-sustaining camp chip; the in-combat gate plus the 10-14 barrier cuts leave her with neither sustain nor burst."
    },
    {
     "hero": "Lady Geist",
     "relationship": "core",
     "effect": "down",
     "why": "98% of her games buy it; the trimmed spirit scaling hurts her Spirit Soul-Exchange variant most, since that build stacks the stat the item now scales with worst."
    },
    {
     "hero": "Shiv",
     "relationship": "core",
     "effect": "down",
     "why": "Extended-fight regen is his win condition; losing cast-heals while rotating or clearing removes the health buffer he starts fights with."
    },
    {
     "hero": "Celeste",
     "relationship": "core",
     "effect": "down",
     "why": "Regen-stacked sustain-burst core takes another hit on top of the air-drag tax, deepening her late-scaler problem."
    },
    {
     "hero": "Kelvin",
     "relationship": "core",
     "effect": "down",
     "why": "His Extra Regen/Healing Booster core is untouched, but he is still a heavy user — and his relative edge over rival sustain shrinks now that everyone's regen got worse."
    }
   ],
   "build_shift": "It stays core by buy rate, but each point of spirit buys less healing, which quietly raises the value of Healbane/Decay and pre-ramp burst against every holder."
  },
  {
   "item": "Silence Wave",
   "direction": "buff",
   "magnitude": "minor",
   "summary": "+40 bonus health makes the silence slot less of a survivability gamble, which matters because the patch schedules forced hub fights and the dive class that punishes utility buys is up. No KB usage data — treat as a cheap utility option, low confidence.",
   "affected_heroes": [],
   "build_shift": ""
  },
  {
   "item": "Torment Pulse",
   "direction": "buff",
   "magnitude": "minor",
   "summary": "+4% melee resistance on an AoE aura is a direct tax on the melee-front meta (Shiv, Rat King, Billy, Drifter) prowling corridor and hub fights; small number, but it lands in exactly the fights this map forces and it stacks with the tank archetype already being up.",
   "affected_heroes": [
    {
     "hero": "Mo & Krill",
     "relationship": "core",
     "effect": "up",
     "why": "Default spirit-bruiser front line that brawls in melee range; resist on his aura is free durability in the matchup he already wins."
    },
    {
     "hero": "Victor",
     "relationship": "core",
     "effect": "up",
     "why": "His sustain stack is designed to outlast divers; melee resist compounds with Spirit Lifesteal/Healing Booster sustain."
    },
    {
     "hero": "Baba",
     "relationship": "core",
     "effect": "up",
     "why": "One of the few things still going her way: her aura build takes less damage from the melee bruisers that beat her."
    },
    {
     "hero": "Shiv",
     "relationship": "core",
     "effect": "up",
     "why": "He fights other frontlines in melee; the resist helps him survive the current-HP knife ramp."
    },
    {
     "hero": "Yamato",
     "relationship": "core",
     "effect": "up",
     "why": "Late spirit-burst build uses it as AoE shred and now as melee defence for her all-in."
    },
    {
     "hero": "Celeste",
     "relationship": "core",
     "effect": "up",
     "why": "Her loss pattern is mobile melee closing the gap; the resist blunts exactly that burst window."
    }
   ],
   "build_shift": ""
  },
  {
   "item": "Echo Shard",
   "direction": "buff",
   "magnitude": "minor",
   "summary": "Post-cast 0.5->0.2s narrows the punish window on the second cast. That matters only for combos where the doubled ability is the finisher, and it does nothing for the heroes whose Echo Shard line has already fallen out of usage.",
   "affected_heroes": [
    {
     "hero": "Graves",
     "relationship": "core",
     "effect": "up",
     "why": "Her summoner/cooldown spirit build runs Echo Shard as the primary cluster; a shorter post-cast means the double Jar of Dead/Grasping Hands sequence is less punishable, which is the only tempo she owns."
    },
    {
     "hero": "Paradox",
     "relationship": "situational",
     "effect": "up",
     "why": "Her Echo Shard bomb line is historical per usage data; better timing does not bring it back."
    },
    {
     "hero": "Bebop",
     "relationship": "situational",
     "effect": "up",
     "why": "Hook-into-double-cast becomes safer, but his comp slot depends on CC landing, not on cast timing."
    }
   ],
   "build_shift": ""
  },
  {
   "item": "Focus Lens",
   "direction": "buff",
   "magnitude": "minor",
   "summary": "The barrier fix is the real change, not the 45->40s cooldown: the repeat-damage stack now ramps through shields (Divine Barrier, Reactive Barrier), which is where standoff spirit-amp damage previously wasted its window. Still cleansable, so still situational.",
   "affected_heroes": [],
   "build_shift": ""
  },
  {
   "item": "Lightning Scroll",
   "direction": "rework",
   "magnitude": "minor",
   "summary": "Adding 0.35 spirit scaling turns a flat utility dash-slow into something spirit carries can scale, and -10->-12% dash-distance slow lands alongside the 0.35->0.5 air-drag ratio — dash denial is being priced as a real stat this patch. Low confidence: no KB buyers to anchor it.",
   "affected_heroes": [],
   "build_shift": ""
  },
  {
   "item": "Rebuttal",
   "direction": "neutral",
   "magnitude": "minor",
   "summary": "The wording reads as less parry cooldown reduction (1.75->1.25s) while the notes tag it a buff, so I will not pretend to know the direction; either way it is a small nudge to the parry economy and appears in no KB build. Skip it unless you run parry-centric dives.",
   "affected_heroes": [],
   "build_shift": ""
  },
  {
   "item": "Battle Vest",
   "direction": "buff",
   "magnitude": "minor",
   "summary": "18->22% weapon damage on a health-first front-line item tilts the cheap weapon pool toward brawling in the same patch that trimmed the poke items (HVR velocity, Express Shot). The buyer stands closer and trades longer, which is where the corridor economy now pays.",
   "affected_heroes": [
    {
     "hero": "Venator",
     "relationship": "core",
     "effect": "up",
     "why": "His gun-bruiser build is built to stand in melee range; the extra weapon damage is the only buff his item set got this patch."
    }
   ],
   "build_shift": "Battle Vest plus Bullet Lifesteal now form a stronger early bruiser package than the velocity/poke openers."
  },
  {
   "item": "Bullet Lifesteal",
   "direction": "buff",
   "magnitude": "minor",
   "summary": "+4% weapon damage and +2% lifesteal compound on gun bruisers who fight to the death, but the sustain half is taxed by the patch's own anti-heal rise (Healbane stacking, Toxic Bullets 40%) — so it is a damage item now more than a sustain item.",
   "affected_heroes": [
    {
     "hero": "Venator",
     "relationship": "core",
     "effect": "up",
     "why": "Frontline M1 build stacks it with Battle Vest/Berserker; both halves of the buff are exactly what that shell buys."
    },
    {
     "hero": "Infernus",
     "relationship": "core",
     "effect": "up",
     "why": "Standard early gun lifesteal on a hero who otherwise lost ground this patch; small, but it is the sustain that keeps his low-HP kite alive."
    }
   ],
   "build_shift": ""
  },
  {
   "item": "Healbane",
   "direction": "rework",
   "magnitude": "major",
   "summary": "Multi-source anti-heal now stacks with diminishing returns, converting the item from a personal slot into a team coverage plan: two anti-heal sources beat one strong healer, which is the patch's structural answer to Healing Snacks and the trimmed heal items. The heal-on-kill cut (275 -> 170 + 3/boon) instead taxes the frontline buyers' own sustain — those two halves pull in opposite directions on the same hero.",
   "affected_heroes": [
    {
     "hero": "Mo & Krill",
     "relationship": "core",
     "effect": "down",
     "why": "He buys it for anti-heal and lives on Scorn sustain; the kill-heal cut removes the self-sustain that made the slot free for him."
    },
    {
     "hero": "Shiv",
     "relationship": "core",
     "effect": "down",
     "why": "Double duty as anti-heal and regen-ramp tool; the heal-on-kill nerf is a direct cut to a hero who wins by never leaving the fight."
    },
    {
     "hero": "Kelvin",
     "relationship": "core",
     "effect": "down",
     "why": "His entire kit sells healing; enemy anti-heal stacking now composes instead of overwriting, which is the single worst system change for a dedicated healer."
    },
    {
     "hero": "Ivy",
     "relationship": "core",
     "effect": "down",
     "why": "Same story one tier down — tether heals are now reduced by stacked sources, and her own Healbane buy lost kill-heal."
    },
    {
     "hero": "Seven",
     "relationship": "core",
     "effect": "up",
     "why": "He is the one buyer who wants the enemy's sustain gone rather than his own sustain up; stacking lets him plus one teammate fully blank a healing comp."
    },
    {
     "hero": "Apollo",
     "relationship": "core",
     "effect": "down",
     "why": "Locket/Healbane sustain package takes the kill-heal cut while his lane-bully model depends on never backing."
    },
    {
     "hero": "Yamato",
     "relationship": "core",
     "effect": "down",
     "why": "Buys it to cut bruiser sustain through her burst window; the self-heal trim slightly worsens her all-in exit."
    }
   ],
   "build_shift": "Anti-heal is now a team-level purchase rather than a slot: expect double anti-heal comps into Kelvin/Ivy/Rem instead of one Healbane plus damage."
  },
  {
   "item": "Healing Booster",
   "direction": "rework",
   "magnitude": "moderate",
   "summary": "Detaching it from Extra Regen and stripping the +3 flat regen turns a cheap value component into a standalone buy; +2 out-of-combat regen does not replace what it lost. Regen-stackers' early curve slows at the exact moment harder Haunts demand more sustain per camp.",
   "affected_heroes": [
    {
     "hero": "Baba",
     "relationship": "core",
     "effect": "down",
     "why": "Regen wall build loses both this and Radiant Regeneration in the same patch; her farm-route identity is being dismantled item by item."
    },
    {
     "hero": "Celeste",
     "relationship": "core",
     "effect": "down",
     "why": "Sustain-burst core is regen-first and both its regen pieces were cut."
    },
    {
     "hero": "Victor",
     "relationship": "core",
     "effect": "down",
     "why": "His A-tier status runs through Spirit Lifesteal + Healing Booster sustain; the component loss delays the shell even though Infuser/Spirit Lifesteal went up."
    },
    {
     "hero": "Kelvin",
     "relationship": "core",
     "effect": "down",
     "why": "73-81% buy rate item in his default support path; he now pays more for the same heal amplification."
    },
    {
     "hero": "Rem",
     "relationship": "core",
     "effect": "down",
     "why": "Percent-max-HP heal support who buys it for heal amp; the regen loss matters less, the timing loss matters more."
    }
   ],
   "build_shift": "Extra Regen no longer upgrades into it, so the classic Extra Regen -> Healing Booster opener becomes two separate purchases; Extra Regen's standalone value rises while Healing Booster drops a tier in priority."
  },
  {
   "item": "Return Fire",
   "direction": "buff",
   "magnitude": "moderate",
   "summary": "Returning Fixation damage gives tanks a functional anti-Haze slot, and the tooltip fix surfaces the 10% bullet resistance the item always had — buyers were undervaluing it and it now also answers the one gun carry the patch left untouched.",
   "affected_heroes": [
    {
     "hero": "Haze",
     "relationship": "situational",
     "effect": "down",
     "why": "Her signature damage now gets reflected by the defensive item frontline tanks were already buying; a real counter-slot exists where the item used to whiff."
    }
   ],
   "build_shift": ""
  },
  {
   "item": "Spirit Lifesteal",
   "direction": "buff",
   "magnitude": "minor",
   "summary": "+2 spirit power and +2% lifesteal is a sustain buff in the patch that made Haunts hit 10% harder — for AoE spirit clearers this is the cheapest way to turn one-cycle clears into chain clears, and it sidesteps the regen items that were trimmed.",
   "affected_heroes": [
    {
     "hero": "Seven",
     "relationship": "core",
     "effect": "up",
     "why": "Fastest camp clearer on the board; more spirit power speeds the one-cycle and the lifesteal pays the +10% Haunt damage, so his income lead compounds."
    },
    {
     "hero": "Infernus",
     "relationship": "core",
     "effect": "up",
     "why": "Burn AoE clear plus lifesteal sustain on camps, the one line of his that nets positive in this patch."
    },
    {
     "hero": "Victor",
     "relationship": "core",
     "effect": "up",
     "why": "Sustain-stack identity gets a direct buff while his competing regen items were cut."
    },
    {
     "hero": "Warden",
     "relationship": "core",
     "effect": "up",
     "why": "Small sustain gain on a hero whose problem is tempo, not sustain — does not move his tier."
    },
    {
     "hero": "Violet",
     "relationship": "core",
     "effect": "up",
     "why": "Cheap spirit item in her ramp, but it sits at her 46% baseline like everything else she buys."
    }
   ],
   "build_shift": "In-fight lifesteal now substitutes for the out-of-combat regen that Radiant Regeneration and Healing Booster no longer provide."
  },
  {
   "item": "Spirit Shielding",
   "direction": "nerf",
   "magnitude": "minor",
   "summary": "3% spirit resist off the default anti-spirit pickup, in a patch where spirit burst is the main counter to the front-line archetype that buys it. It stays the slot; the number is just worse.",
   "affected_heroes": [
    {
     "hero": "Silver",
     "relationship": "core",
     "effect": "down",
     "why": "Gun tank's only spirit mitigation in the primary build; her loss pattern is spirit burst (Celeste, Lash) and this makes it slightly worse."
    },
    {
     "hero": "Celeste",
     "relationship": "core",
     "effect": "down",
     "why": "She buys it to survive spirit trades she already loses to sustain; another small negative on a falling hero."
    },
    {
     "hero": "Billy",
     "relationship": "core",
     "effect": "down",
     "why": "Spirit-shred/slow variant uses it as its defensive layer into caster comps."
    },
    {
     "hero": "Vyper",
     "relationship": "situational",
     "effect": "down",
     "why": "Minor for a mobile carry that rarely gets caught by spirit burst anyway."
    }
   ],
   "build_shift": ""
  },
  {
   "item": "Bullet Resilience",
   "direction": "buff",
   "magnitude": "minor",
   "summary": "30->35% bullet resist plus doubled out-of-combat regen is a cheap answer to the gun-carry tier (Paige, Silver, Rat King, Venator) that the same patch buffed through Battle Vest and Bullet Lifesteal. No KB buyers yet, so it is a slot waiting to be discovered rather than a mover.",
   "affected_heroes": [],
   "build_shift": ""
  },
  {
   "item": "Fury Trance",
   "direction": "buff",
   "magnitude": "minor",
   "summary": "Weapon damage 6->10% plus a 1.5m active move speed turns a barely-bought steroid into a real chase/escape tool; the move speed is the part that matters in corridor fights where the exits are long.",
   "affected_heroes": [],
   "build_shift": "Active-steroid items (Fury Trance, Vampiric Burst) are being repriced as a tier; neither has KB usage to displace a core slot yet."
  },
  {
   "item": "Healing Nova",
   "direction": "rework",
   "magnitude": "moderate",
   "summary": "Spirit scaling instead of boon scaling moves the item from 'any support, any build' to 'spirit supports only' — it becomes a Kelvin/Rem item and quietly leaves gun-support builds. That is a real slot change, not a number tweak.",
   "affected_heroes": [
    {
     "hero": "Kelvin",
     "relationship": "core",
     "effect": "up",
     "why": "His default stacks spirit power (Extra/Improved Spirit), so 1.1 spirit scaling beats the flat boon number he used to get."
    },
    {
     "hero": "Rem",
     "relationship": "core",
     "effect": "up",
     "why": "Spirit heal support stacks the exact stat the nova now scales with."
    },
    {
     "hero": "Ivy",
     "relationship": "core",
     "effect": "down",
     "why": "Her real build is gun-first with little spirit power, so the nova is now a weak purchase for the hero who used to take it as a team-heal button."
    }
   ],
   "build_shift": "Healing Nova now competes with spirit items for the same slot on spirit supports and loses its place on weapon supports."
  },
  {
   "item": "Metal Skin",
   "direction": "rework",
   "magnitude": "minor",
   "summary": "+20% gravity while active means the item no longer doubles as a vertical escape or hover tool — it now taxes the float-and-exit play right as air drag makes airborne escapes worse anyway. Low confidence: no KB buyers.",
   "affected_heroes": [],
   "build_shift": ""
  },
  {
   "item": "Infuser",
   "direction": "buff",
   "magnitude": "minor",
   "summary": "Spirit power 6->8 plus a 75% active lifesteal window make the burst-sustain active better on spirit frontlines — and the spirit power half pays even when the active is on cooldown, which is what separates it from the pure-lifesteal items.",
   "affected_heroes": [
    {
     "hero": "Victor",
     "relationship": "core",
     "effect": "up",
     "why": "Sits in his spirit sustain bruiser core; both the spirit power and the active lifesteal feed the exact grind-down pattern that made him A-tier."
    }
   ],
   "build_shift": ""
  },
  {
   "item": "Juggernaut",
   "direction": "buff",
   "magnitude": "minor",
   "summary": "Health regen +8->+15 nearly doubles the regen rider, making it the cheap regen buy at exactly the moment Radiant Regeneration and Healing Booster lost theirs. That is a redirect for regen-stackers, not a new core.",
   "affected_heroes": [],
   "build_shift": "Cheap regen value is being pushed down the item pool (Juggernaut, Bullet Resilience) as the T3/T4 regen items were trimmed."
  },
  {
   "item": "Leech",
   "direction": "buff",
   "magnitude": "minor",
   "summary": "28->30% on both lifesteal types does not fix its problem: it was already losing to cheaper lifesteal, and this patch buffed every one of those cheaper options (Bullet Lifesteal, Spirit Lifesteal, Infuser) by comparable margins. Relative position is flat.",
   "affected_heroes": [],
   "build_shift": ""
  },
  {
   "item": "Vampiric Burst",
   "direction": "buff",
   "magnitude": "minor",
   "summary": "Same package as Fury Trance — weapon damage 6->10%, lifesteal and active lifesteal up. The T3 active-steroid tier is being made buyable in a patch where fight-sustain beats regen, but no KB usage exists to say who takes it.",
   "affected_heroes": [],
   "build_shift": ""
  },
  {
   "item": "Spellbreaker",
   "direction": "rework",
   "magnitude": "minor",
   "summary": "Extending the reduction to all spirit damage in the same stack turns it from a single-hit shield into a counter to one-shot spirit combos and charged-shot/tankbuster stacks — a real anti-burst pick into the spirit-burst class the patch otherwise favours.",
   "affected_heroes": [],
   "build_shift": ""
  },
  {
   "item": "Divine Barrier",
   "direction": "nerf",
   "magnitude": "moderate",
   "summary": "45->55s on the save slot is a 22% cut in defensive uptime, and it lands in a patch that schedules more forced fights (Bell Tower, Sunken Plaza, container contests) — fewer barriers per fight cycle on a hero whose job is one save per fight.",
   "affected_heroes": [
    {
     "hero": "Rem",
     "relationship": "core",
     "effect": "down",
     "why": "It is the late payoff item of his vitality shell (45% buy, 55.8% WR) and his only burst-stop besides the cleanse; a 10s longer cooldown means the second hub fight happens without it."
    },
    {
     "hero": "Solomon",
     "relationship": "situational",
     "effect": "neutral",
     "why": "KB usage says Divine Barrier does not appear in his high-rank buys, so the nerf is theoretical for him."
    }
   ],
   "build_shift": ""
  },
  {
   "item": "Golden Goose Egg",
   "direction": "buff",
   "magnitude": "minor",
   "summary": "Three points off the damage penalty does not rescue it: the economy now pays a losing team through tick souls and raised non-hero comeback gold, so buying a soul-generation item to close a deficit is the least necessary it has ever been.",
   "affected_heroes": [],
   "build_shift": ""
  },
  {
   "item": "Armor Piercer",
   "direction": "buff",
   "magnitude": "minor",
   "summary": "More reliable armor pierce lands in the same patch bullet resistance rose (Bullet Resilience 35%, Return Fire's 10% now visible on the tooltip) — a small counterweight for gun carries into frontline stat-stacking.",
   "affected_heroes": [],
   "build_shift": ""
  },
  {
   "item": "Glass Cannon",
   "direction": "buff",
   "magnitude": "minor",
   "summary": "80->85% weapon damage on the all-in gun item pairs awkwardly with the lifesteal buffs: if you can heal back the trade, the extra damage is free; if anti-heal is on you, the no-HP build dies faster than ever.",
   "affected_heroes": [],
   "build_shift": ""
  },
  {
   "item": "Spiritual Overflow",
   "direction": "buff",
   "magnitude": "minor",
   "summary": "A component spirit power bump 6->8 raises the floor for spirit-stacking users without restoring the on-hit proc package gutted on 09-16 — it is a stat patch on an item whose identity was removed.",
   "affected_heroes": [
    {
     "hero": "Infernus",
     "relationship": "core",
     "effect": "up",
     "why": "Still in his listed core, but his KB build notes drop it for Swift Striker/Titanic; a spirit stat bump does not bring the proc line back."
    },
    {
     "hero": "Warden",
     "relationship": "situational",
     "effect": "up",
     "why": "Small gain on the late capstone his notes already say was nerfed out of his plan."
    },
    {
     "hero": "Baba",
     "relationship": "core",
     "effect": "up",
     "why": "Marginal spirit power on a hero whose spirit stack just lost its healing scaling — the stat gain is offset by what spirit power now buys her."
    }
   ],
   "build_shift": ""
  },
  {
   "item": "Crippling Headshot",
   "direction": "buff",
   "magnitude": "minor",
   "summary": "35->40% anti-heal adds another stacking source to the patch's defining answer (healing reduction), on a headshot weapon item — so the poke carries who buy it now contribute to composed multi-source anti-heal instead of a redundant debuff.",
   "affected_heroes": [],
   "build_shift": ""
  }
 ],
 "notable_item_stories": [
  "Anti-heal rose everywhere (Healbane now stacks, Toxic Bullets 40%, Crippling Headshot 40%) while the healing items were cut (Radiant Regeneration, Healing Booster, Healing Nova reworked) — drafting a sustain comp this patch means drafting into a multi-source counter.",
  "The whole lifesteal cluster (Bullet/Spirit Lifesteal, Infuser, Leech, Vampiric Burst, Fury Trance) was buffed together, shifting survivability from out-of-combat regen (nerfed) into in-fight sustain — which is also the only reliable way to clear Haunts that now hit 10% harder.",
  "Invisibility and ambush are being repriced at once: Shadow Weave now needs 6s of charged stealth while Steam Vents sell stamina instead of a free approach, and Hunter's Aura lost wall-piercing — pre-fight information and setup are worth less than contact value, which is why Battle Vest and Bullet Lifesteal rose as the poke/utility items fell."
 ]
}

## Hero analysis (only heroes with direction != neutral)

[
 {
  "hero": "Infernus",
  "in_notes": true,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.55,
  "direct_reasons": [
   "Napalm T2 lifesteal 15%->20% pays the camp-route sustain his burn clear already wants.",
   "Concussive Combustion T3 adds +0.4 spirit scaling, which lands on the Dashfernus line rather than the gun line."
  ],
  "indirect_reasons": [
   "Spirit Lifesteal +2 spirit/+2% lifesteal and the Toxic Bullets 40% heal-cut are both in his core, and Haunt bounty/growth is +10% for an AoE one-cycler.",
   "Haunts hitting 10% harder costs him less than slow clearers because the camp dies in one pass."
  ],
  "build_changes": [
   "Toxic Bullets is now a damage slot into sustain comps, not filler; keep Spirit Lifesteal in both builds."
  ],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Burn clear pays 10% more and his sustain items got buffed \u2014 Dashfernus quietly up."
 },
 {
  "hero": "Seven",
  "in_notes": true,
  "direction": "up",
  "magnitude": "moderate",
  "confidence": 0.6,
  "direct_reasons": [
   "Static Charge T3 stun 0.9s->1.1s adds real lockdown to the ability he already uses to hold camps and fights."
  ],
  "indirect_reasons": [
   "Haunt bounty and growth +10% is pure profit for the fastest one-cycle clearer on the board; the HP/damage +10% barely touches him.",
   "Spirit Lifesteal (+2/+2%) and Healbane's new multi-source stacking are both core, and Healbane's kill-heal cut matters less than blanking enemy sustain."
  ],
  "build_changes": [
   "Keep the Monster Rounds/Cultist Sacrifice opener and chain camps before first back \u2014 jungle income now scales harder per minute."
  ],
  "tier_before": "A",
  "tier_after": "S",
  "one_liner": "Jungle pays 10% more and he clears it fastest \u2014 Seven is the farm winner."
 },
 {
  "hero": "Vindicta",
  "in_notes": false,
  "direction": "down",
  "magnitude": "moderate",
  "confidence": 0.6,
  "direct_reasons": [],
  "indirect_reasons": [
   "High-Velocity Rounds velocity 60%->45% removes the max-range guarantee her gun-poke build is built on, and it is her first core buy.",
   "Air drag ratio 0.35->0.5 taxes every airborne exit she has, and Silver's Bola fix makes flyer grounding more reliable."
  ],
  "build_changes": [
   "Accept a shorter effective range: Opening Rounds/Long Range before HVR, and buy Counterspell earlier than planned into dive."
  ],
  "tier_before": "A",
  "tier_after": "B",
  "one_liner": "Poke carry lost its velocity crutch and the air got slower \u2014 A down to B."
 },
 {
  "hero": "Lady Geist",
  "in_notes": true,
  "direction": "down",
  "magnitude": "moderate",
  "confidence": 0.6,
  "direct_reasons": [
   "Essence Bomb spirit scaling 1.22->1.35 is a genuine buff, but only to the spirit Soul-Exchange variant's kill window."
  ],
  "indirect_reasons": [
   "Radiant Regeneration now heals only in combat at 65->40 base, 1.7->1.4 boon and 0.35->0.25 spirit scaling \u2014 98% of her games buy it.",
   "Decay's incoming-heal penalty deepens (-50%->-55%) on a core anti-heal slot she fights out of."
  ],
  "build_changes": [
   "Move the regen budget to Juggernaut (+8->+15 regen) and in-fight Spirit/Bullet Lifesteal; Healing Booster no longer upgrades from Extra Regen, so buy it later or skip it."
  ],
  "tier_before": "A",
  "tier_after": "B",
  "one_liner": "Her regen wall lost its out-of-combat half \u2014 thinner than the tier says."
 },
 {
  "hero": "Abrams",
  "in_notes": true,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [
   "Base gun damage +5% barely registers on a heavy-melee tank; Siphon Life T3 +18->+22 DPS is a small fight-length gain.",
   "Shoulder Charge fix removes the free hold on enemies who never hit a wall \u2014 that was a bug in his favour."
  ],
  "indirect_reasons": [
   "Hunter's Aura is now LOS-gated, so his primary melee build loses the shred it carried through walls on the approach.",
   "Decay's deeper self-heal penalty lands on the same Siphon resource he fights with, though Torment Pulse's +4% melee resist helps his brawls."
  ],
  "build_changes": [
   "Take Hunter's Aura later or swap to Battle Vest/Bullet Lifesteal, which never turn off; keep heavy melee for crates and candy cauldrons."
  ],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Crate-and-Siphon tank is fine, but his aura now needs contact to pay."
 },
 {
  "hero": "Wraith",
  "in_notes": true,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.55,
  "direct_reasons": [
   "Card Trick heal 60->45 trims the only sustain on her gun line.",
   "Project Mind cooldown 46->50s and initial cast 0.75->1s slow the repositioning her whole survival plan uses."
  ],
  "indirect_reasons": [
   "Her fire-rate gun core (Monster Rounds, Quicksilver Reload, Rapid Rounds, Swift Striker, Ricochet) is untouched, so this is a kit-only trim.",
   "Paige's base bullet damage 35->32 eases her worst matchup slightly."
  ],
  "build_changes": [],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Two small cuts on a hero already sliding toward pure gun \u2014 still playable."
 },
 {
  "hero": "McGinnis",
  "in_notes": true,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [
   "Mini Turret damage vs troopers 50%->65% and health per boon 9->10 speed her lane farm and turret uptime."
  ],
  "indirect_reasons": [
   "Haunt bounty/growth +10% rewards a kit that clears grouped camps from cover without taking the +10% Haunt damage herself.",
   "None of her core items moved, so the turret buff is the whole delta."
  ],
  "build_changes": [
   "Spirit turret/ult (Extra Charge + Rapid Recharge) scales better now that turret HP per boon went up."
  ],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Turret farms lane and camps faster, and the jungle pays more \u2014 quiet riser."
 },
 {
  "hero": "Paradox",
  "in_notes": true,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.45,
  "direct_reasons": [
   "Paradoxical Swap 110->95s cooldown is a real extra pick per fight cycle."
  ],
  "indirect_reasons": [
   "Express Shot -5% secondary-fire damage cuts into the carbine crit burst her roamer identity converts, and HVR velocity 60->45 hurts her max-range setup.",
   "Steam Vents swap invisibility for stamina, deleting a KB-cited pick-setup tool her identity leaned on."
  ],
  "build_changes": [
   "The Ability burst line (Slowing Hex, Compress Cooldown, Tankbuster) gains relative value over the HVR/Express Shot crit line; delay HVR."
  ],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "More swaps but worse picks \u2014 the carbine roamer traded power for frequency."
 },
 {
  "hero": "Haze",
  "in_notes": true,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [
   "Smoke Bomb T3 no longer dispels undispellable debuffs (e.g. Specter Crash) \u2014 a straight nerf to the cleanse she escapes dives with."
  ],
  "indirect_reasons": [
   "Return Fire now returns Fixation damage, creating the functional anti-Haze slot frontline tanks already bought.",
   "Bullet Resilience 30->35% plus doubled out-of-combat regen adds another cheap answer to gun carries."
  ],
  "build_changes": [
   "Keep the Fixation gun core, but respect Return Fire on the enemy frontline \u2014 don't stand through it holding M1."
  ],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Her damage is unchanged but tanks finally have a real item to answer it."
 },
 {
  "hero": "Calico",
  "in_notes": true,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.55,
  "direct_reasons": [
   "Leaping Slash T3 +60->+90 damage and Ava T3 6->8s are straight buffs to her melee-spirit burst and dive window."
  ],
  "indirect_reasons": [
   "Steam Vents no longer grant invisibility, trimming one of her roam routes, but her spirit melee core (Melee Lifesteal, Stalker, Spirit Strike, Cold Front) is untouched.",
   "Warden's Flask/Willpower buffs sharpen one of her worst lanes; Rat King's nerfs remove a frontline she struggled to burst."
  ],
  "build_changes": [
   "Keep the melee spirit assassin core; Ava T3 at 8s is now worth committing to for a second pick."
  ],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Bigger slash, longer cat \u2014 Calico's dive got a bit sharper."
 },
 {
  "hero": "Mo & Krill",
  "in_notes": true,
  "direction": "down",
  "magnitude": "moderate",
  "confidence": 0.6,
  "direct_reasons": [
   "Spirit per boon 1.1->0.6 and -10% spirit damage on every ability gut his spirit bruiser; bullet damage per boon +4% is the compensation, pointing at a gun-hybrid re-spec.",
   "Combo (the grab) is unchanged, so his lockdown identity survives the damage cut."
  ],
  "indirect_reasons": [
   "Torment Pulse +4% melee resist is a genuine buff to his front line.",
   "Decay's deeper self-heal penalty and Healbane's heal-on-kill 275->170 both hit the sustain slots he buys."
  ],
  "build_changes": [
   "Shift one slot toward gun (Bullet Lifesteal/Battle Vest) to offset the spirit cut; keep Torment Pulse and use Decay only when the anti-heal matters."
  ],
  "tier_before": "A",
  "tier_after": "B",
  "one_liner": "The grab still wins fights, but everything he does after it hit softer."
 },
 {
  "hero": "Shiv",
  "in_notes": true,
  "direction": "down",
  "magnitude": "moderate",
  "confidence": 0.6,
  "direct_reasons": [
   "Serrated Knives rage 3.5%->4% current HP plus T3 +0.01 spirit scaling buff his anti-tank knife; alt fire damage per boon -5% and Killing Blow recast 16->12s are the offsets.",
   "He wins the knife exchange but has a shorter execute window."
  ],
  "indirect_reasons": [
   "Radiant Regeneration now only heals in combat with heavy cuts \u2014 it is in essentially every Shiv game and is his fight-start health buffer.",
   "Healbane's heal-on-kill 275->170 taxes his regen ramp, partly offset by Torment Pulse's +4% melee resist."
  ],
  "build_changes": [
   "Swap Radiant Regeneration value into Juggernaut regen plus in-fight Spirit Lifesteal; treat Radiant as a combat-only heal, not a rotation heal."
  ],
  "tier_before": "A",
  "tier_after": "B",
  "one_liner": "Knife got better, regen got worse \u2014 the ramp hero loses his pre-fight health."
 },
 {
  "hero": "Ivy",
  "in_notes": false,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [],
  "indirect_reasons": [
   "Healbane now stacks across sources \u2014 the single worst system change for a healer whose tethers are her value.",
   "Healing Nova moving to spirit scaling makes it weak on her gun-first build, and Healing Booster lost its Extra Regen link and +3 regen."
  ],
  "build_changes": [
   "Skip Healing Nova entirely; if you need the anti-heal trade, buy Healbane yourself rather than amplifying tethers."
  ],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Best peel in the game, but every healing item she bought got worse."
 },
 {
  "hero": "Warden",
  "in_notes": true,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.45,
  "direct_reasons": [
   "Alchemical Flask travels 40% faster with -30% weapon damage (from -25%), Willpower +15->+20% speed, and Last Stand T2 +40.5->50 DPS with -40s cooldown.",
   "The flask speed makes the debuff land on reaction rather than prediction."
  ],
  "indirect_reasons": [
   "Shadow Weave rework takes the fire rate he bought it for and now demands 6s of pre-stealth before Willpower \u2014 a real nerf to his cage-bruiser shell.",
   "HVR velocity 60->45 trims his poke item, and Steam Vents no longer give everyone the invis-engage he pays for."
  ],
  "build_changes": [
   "Drop Shadow Weave to a late pickup; pre-stealth 6s before the cage engage or skip it for a damage T4."
  ],
  "tier_before": "C",
  "tier_after": "C",
  "one_liner": "Kit got real buffs, but his signature invis item got reworked out from under him."
 },
 {
  "hero": "Yamato",
  "in_notes": true,
  "direction": "down",
  "magnitude": "moderate",
  "confidence": 0.6,
  "direct_reasons": [
   "Flying Slash range 26->23m with T3 +15->+8m cuts her engage reach roughly a quarter, and targets now see the mark on cast.",
   "Shadow Transformation 150->160s and moved to T2 delays the all-in; Power Slash +6% spirit scaling is the offset."
  ],
  "indirect_reasons": [
   "Healbane's heal-on-kill cut and Hunter's Aura's LOS gate both hit her late spirit line; Torment Pulse's melee resist helps her commit.",
   "The dive that closes distance now has to close more of it \u2014 the exact range mobile burst buys."
  ],
  "build_changes": [
   "Close the gap with stamina/route instead of old T3 range; keep Torment Pulse, drop Hunter's Aura down the order."
  ],
  "tier_before": "A",
  "tier_after": "B",
  "one_liner": "Her engage range got cut and her ult got slower \u2014 the assassin lost reach."
 },
 {
  "hero": "Lash",
  "in_notes": true,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [
   "Grapple T3 now adds +4m jump velocity, a small but free mobility gain on his escape-and-re-enter."
  ],
  "indirect_reasons": [
   "Steam Vents' +150% stamina regen feeds a dive that lives on dashes and re-engages.",
   "His spirit stomp core (Mystic Burst, Extra Charge, Quicksilver Reload, Bullet Resist Shredder, Tankbuster) is untouched."
  ],
  "build_changes": [],
  "tier_before": "S",
  "tier_after": "S",
  "one_liner": "Nothing hurt the best initiator, and vents now feed him stamina."
 },
 {
  "hero": "Viscous",
  "in_notes": true,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [
   "Splatter T1 +36->+45 damage and +5% alt-fire damage growth per boon improve his lane poke where he actually spends points.",
   "Goo Ball fixes remove the melee/Ethereal Shift exploitation during cast delay \u2014 a nerf, not the story."
  ],
  "indirect_reasons": [
   "Express Shot -5% secondary-fire damage sits in his hybrid Splatter/Punch shell.",
   "Harder Haunt camps reward Cube sustain and Goo Ball suits the spread corridors."
  ],
  "build_changes": [],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Small poke buffs on a hero still waiting for a reason to be picked."
 },
 {
  "hero": "Pocket",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [],
  "indirect_reasons": [
   "30% non-hero comeback gold plus tick souls to the two poorest is the farm-based bail-out his slow Affliction line needed.",
   "None of his spirit core (Cold Front, Tankbuster, Superior Cooldown, Spirit Burn) moved, so he is purely a systems winner."
  ],
  "build_changes": [
   "Farm corridors instead of forcing early fights \u2014 the losing-team soul floor now compounds while he scales."
  ],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Comeback gold finally pays a scaler who farms from behind."
 },
 {
  "hero": "Drifter",
  "in_notes": true,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.55,
  "direct_reasons": [
   "Base gun damage +3%, Bloodscent T3 +11%->+12% amp and Eternal Night T3 +2.5->2.75s are all on the lines he actually plays.",
   "Small numbers, but they land on his melee-duel win condition rather than a side stat."
  ],
  "indirect_reasons": [
   "Toxic Bullets 40% heal-cut stacks with his built-in anti-heal and now composes with Healbane across sources.",
   "The rising frontline archetype and Torment Pulse's melee resist suit his brawls; tough crates and candy cauldrons open on his heavy melee."
  ],
  "build_changes": [
   "Anti-heal bruiser variant is now a real comp answer: double anti-heal sources beat one strong healer."
  ],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Nothing flashy, but anti-heal stacking is a buff to the hero who already had it."
 },
 {
  "hero": "Victor",
  "in_notes": true,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.55,
  "direct_reasons": [
   "Aura of Suffering T3 +15%->+16% damage is cosmetic on its own."
  ],
  "indirect_reasons": [
   "Spirit Lifesteal +2 spirit/+2% lifesteal and Infuser 6->8 spirit with a 75% active lifesteal window all feed his grind-down core, and Torment Pulse's melee resist adds durability.",
   "Healing Booster losing its Extra Regen link and +3 regen is the one cost."
  ],
  "build_changes": [
   "Keep Spirit Lifesteal/Infuser core; buy Healing Booster standalone later rather than as the Extra Regen upgrade."
  ],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Lifesteal items got buffed and camps hit harder \u2014 Victor's grind got better."
 },
 {
  "hero": "Paige",
  "in_notes": true,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [
   "Base bullet damage 35->32 is roughly a 9% lane-phase cut for a hero whose entire value is winning lane; growth 0.52->0.61 only pays back later.",
   "Bookwyrm T2 trail duration +2s->+1s."
  ],
  "indirect_reasons": [
   "HVR velocity 60->45 weakens her 1.2-minute first buy.",
   "Comeback tick souls to the two poorest and 30% non-hero comeback gold blunt the lane lead she converts into a snowball."
  ],
  "build_changes": [
   "If the velocity loss is felt, take Opening Rounds before HVR; her lane is still hers, the conversion is slower."
  ],
  "tier_before": "S",
  "tier_after": "S",
  "one_liner": "Lane bully took a lane cut and the comeback economy ate her snowball."
 },
 {
  "hero": "The Doorman",
  "in_notes": true,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.45,
  "direct_reasons": [
   "Luggage Cart T2 wall impact +75->+90 damage is a straight buff to his only reliable engage damage.",
   "The T3 line is tagged nerf but the number moves -15s->-18s (more reduction) \u2014 direction unclear, treat as neutral."
  ],
  "indirect_reasons": [
   "Bell Tower hub fights and the single-rope ~280-soul payout still suit his Doorway kidnap, and none of his charge/expansion core moved.",
   "Steam Vents' stamina change does nothing for his setup, so he neither gains nor loses there."
  ],
  "build_changes": [],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Slightly better cart, same setup problem \u2014 still a tempo victim."
 },
 {
  "hero": "Billy",
  "in_notes": true,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [
   "Rising Ram T3 +10%->+15% max HP for 16s->20s is real frontline durability on his all-in; Blasted 27->25s cooldown adds engage frequency.",
   "The HP window now outlasts most single burst rotations."
  ],
  "indirect_reasons": [
   "Tank/frontline archetype is up on harder Haunt camps, and Torment Pulse's +4% melee resist suits the fights he starts.",
   "His anti-tank counter Shiv ate Radiant Regeneration and Healbane cuts."
  ],
  "build_changes": [],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Bigger HP window and a shorter dash cooldown \u2014 the lane bully is back a notch."
 },
 {
  "hero": "Graves",
  "in_notes": true,
  "direction": "down",
  "magnitude": "moderate",
  "confidence": 0.6,
  "direct_reasons": [],
  "indirect_reasons": [],
  "build_changes": [],
  "tier_before": "?",
  "tier_after": "?",
  "one_liner": ""
 }
]

## Creator sources published after this patch (optional corroboration; the notes, KB and snapshot remain primary — if a source contradicts them, say so and keep your own read)

(none)

## What to do

Write the verdict a strong player wants in the first 30 seconds.

1. **Patch size.** Classify: `major` (systems rework or many structural changes; content updates: map rework, new objectives, new heroes; the way games are played changes), `significant` (meaningful systems or economy moves plus broad tuning; the tier list will move), `minor` (tuning; a few heroes move a tier, no systems shift), `hotfix` (a handful of fixes/tweaks). Justify in one or two sentences naming the drivers. Change counts alone do not decide size; a 5-line economy change can be major.
2. **Headline.** One sentence, the thing to remember.
3. **Meta thesis.** State the previous thesis in one sentence, the new thesis in one or two, and whether this is a continuation, a shift, or a reversal. The thesis is about *how the game is won* (tempo vs scaling, which archetypes carry, what the fights look like), not a list of heroes.
4. **Winners and losers.** 3-5 each, ranked, with the driver. Include indirect movers where justified; mark them as such.
5. **Non-obvious calls.** 2-4 claims a casual reader of the notes would miss: unlisted heroes that moved, a "general" change that is really a targeted nerf, a build that died, a sleeper item. Each with a confidence.
6. **Uncertainties and what to watch.** What you are unsure about and what data would settle it in the first week.

## Output schema

{
  "patch_size": "major|significant|minor|hotfix",
  "size_why": "1-2 sentences",
  "headline": "1 sentence",
  "meta_thesis": {
    "previous": "1 sentence",
    "new": "1-2 sentences",
    "relationship": "continuation|shift|reversal",
    "why": "1-2 sentences naming the drivers"
  },
  "winners": [{"hero": "name", "why": "1 sentence", "indirect": false}],
  "losers": [{"hero": "name", "why": "1 sentence", "indirect": false}],
  "non_obvious_calls": [{"claim": "1 sentence", "why": "1 sentence", "confidence": 0.0}],
  "uncertainties": ["1 sentence each"],
  "what_to_watch": ["1 sentence each"]
}
