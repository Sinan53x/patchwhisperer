# Task: per-hero analysis (all heroes)

Patch: Halloween 2026 + Gameplay Update (2026-10-30)

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

## Direct hero changes in this patch (grouped by hero; heroes not listed had no direct changes)

Mid-Boss:
  - [rework] Mid-Boss: Adjusted the terrain layout where the midboss is, the area is a little bigger now and has more cover
  - [buff] Mid-Boss: Health increased by 20%
  - [buff] Mid-Boss: Health gained per minute increased by 20%
  - [rework] Mid-Boss: Resistance reductions are now only 50% as effective against the Mid-Boss
  - [rework] Mid-Boss: Roar now happens at 25% HP instead of 50%
  - [nerf] Mid-Boss: Bounty reduced from 3000 (+50/min) to 1500 (+25/min)
  - [rework] Mid-Boss: The Rejuvenator now drops as 3 crystals placed evenly around the Mid-Boss pit (random positions), instead of 1 crystal in the center
  - [neutral] Mid-Boss: Each Rejuvenator crystal breaks in 1 heavy melee and grants the team 1 Rejuvenator (total per Mid-Boss kill unchanged at 3)
  - [rework] Mid-Boss: The full heal for breaking a Rejuvenator now applies to each crystal (previously only on the first hit)
  - [rework] Mid-Boss: Rejuvenator crystals now give a bounty to the player that breaks them (500 +9/min)
  - [neutral] Mid-Boss: Rejuvenator crystal drop time increased from 6s to 7.5s
Haunts - Past Dues:
  - [rework] Haunts - Past Dues: Now channels their special attack, creating a build-up aura on the ground that applies sleep slowly to Heroes standing within it over time. Killing the channeling creature destroys the aura.
Abrams:
  - [buff] Abrams: Base gun damage increased by 5%
  - [neutral] Siphon Life: Abrams: Siphon Life - T3 increased from +18 DPS to +22
  - [fix] Shoulder Charge: Abrams: Shoulder Charge - Fixed enemies being held in place longer if you don't hit a wall
Apollo:
  - [rework] Riposte: Apollo: Riposte - Pommel Hit changed from a stun to an immobilize and parry disable
  - [buff] Riposte: Apollo: Riposte - Pommel Hit disable duration increased from 0.8s to 1.5s
  - [buff] Riposte: Apollo: Riposte - T2 disable duration increased from +0.4s to +0.6s
  - [fix] Riposte: Apollo: Riposte - Fixed the counterattack dash sometimes missing its target or launching Apollo away when the target moves, rounds a corner, or is displaced
  - [fix] Riposte: Apollo: Riposte - Fixed the counterattack dash missing when Apollo is right on top of the target
  - [rework] Flawless Advance: Apollo: Flawless Advance - Being stunned or put to sleep during the ability now refunds that stab and keeps your remaining recasts instead of putting it on cooldown
  - [rework] Itani Lo Sahn: Apollo: Itani Lo Sahn - No longer interrupted by Sleep
Baba:
  - [nerf] Baba: Spirit Resist scaling reduced from 0.1 to 0.07
  - [nerf] Threadsap: Baba: Threadsap - Spirit Steal duration reduced from 22s to 16s
  - [neutral] Threadsap: Baba: Threadsap - When a victim cleanses the Threadsap debuff, the matching spirit Baba gained is also removed
  - [neutral] Granny Long Legs: Baba: Granny Long Legs - Light Melee knockback distance reduced from 10m to 8m
  - [buff] Granny Long Legs: Baba: Granny Long Legs - Heavy Melee cooldown reduced from 1.4s to 1.2s (default is 1.0s)
  - [nerf] Granny Long Legs: Baba: Granny Long Legs - Heavy Melee slow duration reduced from 4s to 2s
  - [rework] Granny Long Legs: Baba: Granny Long Legs - Heavy melee stomp now only hits the closest Rejuvenator in range
  - [rework] Baba's Brew: Baba: Baba's Brew - No longer has an initial brew time
  - [rework] Baba's Brew: Baba: Baba's Brew - Brew order is now random each time she casts it
  - [nerf] Baba's Brew: Baba: Baba's Brew - Cycle time between each type of brew increased from 1s to 1.5s
  - [rework] Baba's Brew: Baba: Baba's Brew - UI indicator color now matches the current brew
  - [nerf] Baba's Brew: Baba: Baba's Brew - Silence duration reduced from 3s to 2.75s
Billy:
  - [buff] Rising Ram: Billy: Rising Ram - T3 increased from +10% Max Health for 16s to +15% for 20s
  - [buff] Blasted: Billy: Blasted - Cooldown reduced from 27s to 25s
Calico:
  - [buff] Leaping Slash: Calico: Leaping Slash - T3 increased from +60 Damage to +90
  - [buff] Ava: Calico: Ava - T3 increased from 6s duration to 8s
Celeste:
  - [nerf] Shining Wonder: Celeste: Shining Wonder - Damage reduced from 140 to 125
Deadman Danny:
  - [rework] Chimera Mk1: Deadman Danny: Chimera Mk1 - Jetpack can no longer be used while cursed
  - [fix] Close The Deal: Deadman Danny: Chimera Mk1 - Fixed bug causing it to not deal damage when held through a Close The Deal
  - [rework] Chimera Mk1: Deadman Danny: Chimera Mk1 - Items and abilities that pull to the ground now work more reliably against Danny
  - [rework] Chimera Mk1: Deadman Danny: Chimera Mk1 - Slows now reduce the jetpack's in-air impulse more effectively, and even more if movement abilities are silenced
  - [fix] Close The Deal: Deadman Danny: Close the Deal - Fixed some incorrect behavior when used at the top of the belltower
  - [buff] Chimera Mk1: Deadman Danny: Chimera Mk1 - Cooldown reduction per boon reduced from -0.4s to -0.25s
  - [buff] Chimera Mk1: Deadman Danny: Chimera Mk1 - Cooldown refund on hit from T3 reduced from 50% to 30%
The Doorman:
  - [buff] Luggage Cart: Doorman: Luggage Cart - T2 increased from +75 Damage on Wall Impact to +90
  - [nerf] Luggage Cart: Doorman: Luggage Cart - T3 increased from -15s Cooldown to -18s
Drifter:
  - [buff] Drifter: Base gun damage increased by 3%
  - [buff] Bloodscent: Drifter: Bloodscent - T3 increased from +11% Amplified Damage to +12%
  - [buff] Eternal Night: Drifter: Eternal Night - T3 increased from +2.5s Duration to +2.75s
Graves:
  - [nerf] Graves: Move speed reduced from 7 to 6.7
  - [nerf] Graves: Bullet damage per boon reduced by 4%
  - [rework] Grasping Hands: Graves: Grasping Hands - Can now be more easily double jumped over
  - [neutral] Grasping Hands: Graves: Grasping Hands - Deploy time increased from 0.6s to 0.8s
  - [rework] Borrowed Decree: Graves: Borrowed Decree - T2 no longer has -0.3s Time To Spawn
  - [rework] Borrowed Decree: Graves: Borrowed Decree - T3 now also provides -0.3s Time To Spawn
Grey Talon:
  - [rework] Charged Shot: Grey Talon: Charged Shot - T2 now also has -2s Charge Delay
  - [rework] Charged Shot: Grey Talon: Charged Shot - T3 no longer has -3s Charge Delay
  - [rework] Charged Shot: Grey Talon: Charged Shot - T3 now also lets the shot bounce once off a wall (can't hit a target more than once)
  - [rework] Guided Owl: Grey Talon: Guided Owl - Now launches in the exact direction you're aiming, including steep downward angles (previously always launched at least 45° upward)
Infernus:
  - [buff] Napalm: Infernus: Napalm - T2 lifesteal increased from 15% to 20%
  - [rework] Concussive Combustion: Infernus: Concussive Combustion - T3 now increases spirit scaling by 0.4
Haze:
  - [fix] Smoke Bomb: Haze: Smoke Bomb - Fixed T3 dispelling debuffs that can't be dispelled (like the Specter Crash from Nurse's Wretched Vapors)
Kelvin:
  - [nerf] Frozen Shelter: Kelvin: Frozen Shelter - Cooldown increased from 185s to 190s
  - [nerf] Frozen Shelter: Kelvin: Frozen Shelter - T1 increased from -20s Cooldown to -30s
  - [rework] Frozen Shelter: Kelvin: Frozen Shelter - T2 now also reduces enemy fire rate by -20%
  - [buff] Frozen Shelter: Kelvin: Frozen Shelter - T3 regen increased from +65 to +75
Lady Geist:
  - [buff] Essence Bomb: Lady Geist: Essence Bomb spirit scaling increased from 1.22 to 1.35
Lash:
  - [rework] Grapple: Lash: Grapple - T3 now also increases Jump Velocity by +4m
  - [rework] Death Slam: Lash: Death Slam - Targeting indicator changed from a cone to a cylinder to more accurately match the ability's range (visual change only)
McGinnis:
  - [buff] Mini Turret: McGinnis: Mini Turret - Damage vs troopers increased from 50% to 65%
  - [buff] Mini Turret: McGinnis: Mini Turret - Health per boon increased from 9 to 10
Mirage:
  - [neutral] Traveler: Mirage: Traveler - Channel time increased from 2s to 3s
  - [nerf] Traveler: Mirage: Traveler - Onterrupt/cancel cooldown increased from 4s to 5s
  - [rework] Traveler: Mirage: Traveler - Now gets interrupted if you are Stunned/Immobilized/Slept or have slowing hex on you
  - [rework] Traveler: Mirage: Traveler - Now grants the old T2 barrier in the base ability (with no scaling)
  - [rework] Traveler: Mirage: Traveler - The minimap now moves to the center of the screen and is enlarged while targeting
  - [neutral] Traveler: Mirage: Traveler - Added a targeting reticle under your cursor on the minimap that your allies can see, so they can tell where you're thinking of going before you click
  - [rework] Traveler: Mirage: Traveler - Your destination is now marked on your and your allies' minimaps until you arrive, and stays there briefly after landing
  - [buff] Traveler: Mirage: Traveler - T2 changed from "400 Barrier that scales with spirit" to "-65s Cooldown"
  - [neutral] Traveler: Mirage: Traveler - T3 changed from "-90s Cooldown" to "Cannot be interrupted by damage"
  - [rework] Traveler: Mirage: Traveler - T3 now also adds barrier spirit scaling (0.8)
Mo & Krill:
  - [neutral] Mo & Krill: Spirit per boon reduced from 1.1 to 0.6
  - [nerf] Mo & Krill: Spirit damage on all abilities reduced by 10% (base values and growth/upgrades)
  - [buff] Mo & Krill: Bullet damage per boon increased by 4%
Nurse Harrow:
  - [nerf] Nurse Harrow: Base gun damage reduced by 10%
  - [fix] Leech Therapy: Nurse Harrow: Leech Therapy - Fixed enemies being unable to see the glow on the hunting leeches
  - [fix] Leech Therapy: Nurse Harrow: Leech Therapy - Fixed leeches attaching to targets while the game is paused
  - [fix] Leech Therapy: Nurse Harrow: Leech Therapy - Fed leeches duration on the ground changed from a fixed 180s to 120s + 3s/min
  - [buff] Wretched Vapors: Nurse: Wretched Vapors - T3 increased from +15% Rush Speed to +20%
  - [nerf] Healing Needles: Nurse: Healing Needles - Heal Per Shot reduced from 25 to 22
  - [nerf] Healing Needles: Nurse: Healing Needles - T2 Heal Per Shot reduced from +20 to +16
  - [buff] Healing Needles: Nurse: Healing Needles - Spirit scaling increased from 0.2 to 0.24
  - [nerf] Lurking Terrors: Nurse Harrow: Lurking Terrors - Fear buildup time increased from 1.3s to 2s
  - [rework] Lurking Terrors: Nurse Harrow: Lurking Terrors - Enemies no longer build fear when Nurse is more than 50 degrees above or below their view
  - [nerf] Lurking Terrors: Nurse Harrow: Lurking Terrors - T3 changed from "Immune to damage while channeling" to "Takes 50% Reduced Damage while channeling"
  - [rework] Leech Therapy: Nurse Harrow: Leech Therapy - Leeches on the ground are now removed on round reset
  - [nerf] Lurking Terrors: Nurse: Lurking Terrors - Duration reduced from 7s to 5s
  - [nerf] Lurking Terrors: Nurse: Lurking Terrors - T3 reduced from +3s Duration to +2s
Paige:
  - [nerf] Paige: Base bullet damage reduced from 35 to 32
  - [buff] Paige: Bullet damage growth per boon increased from 0.52 to 0.61
  - [nerf] Bookwyrm: Paige: Bookwyrm - T2 Trail Duration reduced from +2s to +1s
Paradox:
  - [buff] Paradoxical Swap: Paradox: Paradoxical Swap - Cooldown reduced from 110s to 95s
Rat King:
  - [nerf] Rat King: Base bullet damage reduced by 5%
  - [nerf] Rat King: Bullet damage growth reduced by 20%
  - [nerf] Scrap Grenade: Rat King: Scrap Grenade - Damage reduced from 70 to 60
  - [nerf] Scrap Grenade: Rat King: Scrap Grenade - T2 damage reduced from +70 to +60
  - [nerf] Scrap Grenade: Rat King: Scrap Grenade - T3 damage reduced from 300 to 275
  - [neutral] Scrap Grenade: Rat King: Scrap Grenade - Fuse timers increased by 0.1s (first bounce from 0.8s to 0.9s, later bounces from 0.7s to 0.8s, T3 final explosion from 1.5s to 1.6s)
  - [rework] Scrap Grenade: Rat King: Scrap Grenade - Meleeing the grenade now gives it at least 0.4s before it explodes (if less than 0.4s was left on its fuse, the fuse is extended to 0.4s)
  - [nerf] Rule, Ratannia!: Rat King: Rule, Ratannia! - Knockup duration reduced by 50%
  - [nerf] Rule, Ratannia!: Rat King: Rule, Ratannia! - Cooldown increased from 160s to 180s
  - [rework] Rule, Ratannia!: Rat King: Rule, Ratannia! - Now goes on cooldown when stunned/slept before placing it. In that case, the flag is placed in that position but without any of the initial impact effects (damage/knockup)
  - [nerf] Scrap Grenade: Rat King: Scrap Grenade - Radius reduced from 8m to 6m
  - [nerf] Scrap Grenade: Rat King: Scrap Grenade - Large explosion radius reduced from 14m to 10m
  - [nerf] Rule, Ratannia!: Rat King: Rule, Ratannia! - Radius reduced from 20m to 16m
  - [nerf] Rule, Ratannia!: Rat King: Rule, Ratannia! - T2 Radius reduced from +8m to +6m
  - [nerf] Rule, Ratannia!: Rat King: Rule, Ratannia! - Duration reduced from 12s to 9s
Seven:
  - [buff] Static Charge: Seven: Static Charge - T3 stun duration increased from 0.9s to 1.1s
Shiv:
  - [nerf] Shiv: Alt Fire damage per boon reduced by 5%
  - [fix] Shiv: Fixed the Alt Fire last-shot sound only playing when you had 1 bullet left
  - [buff] Serrated Knives: Shiv: Serrated Knives - Rage damage increased from 3.5% Current Health to 4%
  - [rework] Serrated Knives: Shiv: Serrated Knives - T3 now also increases rage damage spirit scaling by +0.01
  - [fix] Bloodletting: Shiv: Bloodletting - Fixed damage ticks playing audio
  - [nerf] Killing Blow: Shiv: Killing Blow - Recast duration reduced from 16s to 12s
Silver:
  - [buff] Silver: Base health regen increased from 2.5 to 3
  - [fix] Entangling Bola: Silver: Entangling Bola - Fixed Unstoppable flying targets being made to fall
  - [fix] Entangling Bola: Silver: Entangling Bola - Fixed not grounding Grey Talon during his Rain of Arrows
  - [rework] Silver: Go For The Throat - Now counts weapon damage from Point Blank and Opening Rounds
Solomon:
  - [rework] Solomon: Gun now deals -20% headshot damage
  - [nerf] Solomon: Base bullet damage reduced from 30 to 25
  - [neutral] Solomon: Polished slide animations, added new ability and item aim poses, and adjusted run-to-stop timing
  - [neutral] Setup Bishop: Solomon: Setup Bishop - Square height reduced from 4m to 1m
  - [buff] Setup Bishop: Solomon: Setup Bishop - On Square spirit scaling increased from 0.64 to 0.85
  - [buff] Setup Bishop: Solomon: Setup Bishop - T1 increased from +15% slow to +25%
  - [rework] Setup Bishop: Solomon: Setup Bishop - T3 Spirit Resist reduction is now applied on impact instead of by squares
  - [nerf] Setup Bishop: Solomon: Setup Bishop - T3 increased from -2.5% to -5% Spirit Resist per stack (max reduction unchanged)
  - [nerf] Rook Battery: Solomon: Rook Battery - Damage scaling reduced from 1.3 to 0.9
  - [buff] Rook Battery: Solomon: Rook Battery - T3 reduced from -12s cooldown to -10s
  - [nerf] Develop Queen: Solomon: Develop Queen - Cooldown increased from 210s to 240s
  - [buff] Develop Queen: Solomon: Develop Queen - Damage scaling increased from 1.4 to 1.6
  - [nerf] Develop Queen: Solomon: Develop Queen - Delay for stun tiles increased from 1s to 1.2s
  - [neutral] Develop Queen: Solomon: Develop Queen - Improved warning effects on the stun tiles to make it clear its just those tiles rather than the full area
  - [fix] Develop Queen: Solomon: Develop Queen - Fixed hitting things outside of the intended square volumes
  - [rework] Develop Queen: Solomon: Develop Queen - Base ability now has the checkmate behavior for heroes under 100 Health (scales +5/boon)
  - [rework] Develop Queen: Solomon: Develop Queen - T2 now increases checkmate threshold by 150
  - [buff] Solomon: Move Piece - Range to grab pieces increased from 50m to 65m
  - [rework] Solomon: Move Piece - Improved placement: pieces no longer fall through geometry or end up under the map, land closer to where you aim, and can now be placed closer to walls and in hallways
Venator:
  - [nerf] Ira Domini: Venator: Ira Domini - Blessed stake damage reduced from 115 to 95
  - [buff] Ira Domini: Venator: Ira Domini - Blessed stake damage boon scaling increased from 3 to 3.6
Victor:
  - [buff] Aura of Suffering: Victor: Aura of Suffering - T3 increased from +15% Damage to +16%
Violet:
  - [neutral] Violet: Some moderate performance improvements (still more to do here)
  - [nerf] Still Life: Violet: Still Life - Stun duration reduced from 1.0s to 0.9s
  - [rework] Still Life: Violet: Still Life - Line of sight is now required when the channel ends, even during the grace period
  - [rework] Still Life: Violet: Still Life - Now shows a text bar to the victim
  - [rework] Still Life: Violet: Still Life - Sketches now grant +2% healing amp from Nurse Harrow, Kelvin, Ivy, Dynamo, Paige, and Rem instead
  - [neutral] Still Life: Violet: Still Life - Sketches changed to give Spirit Power instead of Weapon Damage for Grey Talon, Infernus and Mina
  - [rework] Still Life: Violet: Still Life - T1 health regen is now only granted while drawing (still refreshes for 4s on pickup)
  - [nerf] Still Life: Violet: Still Life - T1 health regen scaling reduced from 0.25 to 0.15
  - [buff] Still Life: Violet: Still Life - T3 stun duration increased from +0.35s to +0.45s
  - [nerf] Abstract Landscape: Violet: Abstract Landscape - Cooldown increased from 165s to 180s
  - [nerf] Abstract Landscape: Violet: Abstract Landscape - Duration spirit scaling reduced from 0.04 to 0.01
  - [rework] Abstract Landscape: Violet: Abstract Landscape - Now ends early if Violet dies
  - [nerf] Abstract Landscape: Violet: Abstract Landscape - Cooldown between times you can be affected by it increased from 0.5s to 0.75s
  - [rework] Abstract Landscape: Violet: Abstract Landscape - T3 no longer has "Ink is no longer destroyed"
  - [nerf] Abstract Landscape: Violet: Abstract Landscape - Duration reduced from 6s to 5s
  - [neutral] Abstract Landscape: Violet: Abstract Landscape - T3 reduced from +4s to +3s
Viscous:
  - [buff] Viscous: Alt fire damage growth per boon increased by 5%
  - [buff] Splatter: Viscous: Splatter - T1 increased from +36 Damage to +45 Damage
  - [fix] Goo Ball: Viscous: Goo Ball - Fixed being able to heavy melee or activate Ethereal Shift during the cast delay
  - [fix] Goo Ball: Viscous: Goo Ball - Fixed the direction indicator not appearing
Warden:
  - [rework] Alchemical Flask: Warden: Alchemical Flask - Now travels 40% faster (overall cast range unchanged)
  - [nerf] Alchemical Flask: Warden: Alchemical Flask - Weapon Damage reduction increased from -25% to -30%
  - [buff] Willpower: Warden: Willpower - Speed bonus increased from +15% to +20%
  - [neutral] Last Stand: Warden: Last Stand - T2 increased from +40.5 DPS to +50
  - [buff] Last Stand: Warden: Last Stand - T2 cooldown reduction increased from -30s to -40s
Wraith:
  - [nerf] Card Trick: Wraith: Card Trick - Heal reduced from 60 to 45
  - [nerf] Project Mind: Wraith: Project Mind - Cooldown increased from 46s to 50s
  - [nerf] Project Mind: Wraith: Project Mind - Initial cast time for projectile increased from 0.75s to 1s
Yamato:
  - [buff] Power Slash: Yamato: Power Slash - Spirit scaling increased by 6% (base and T3)
  - [nerf] Flying Slash: Yamato: Flying Slash - Cast Range reduced from 26m to 23m
  - [rework] Flying Slash: Yamato: Flying Slash - Enemy targets are now marked with an overhead symbol as soon as the grapple is cast, instead of only when the hook lands
  - [nerf] Flying Slash: Yamato: Flying Slash - T3 Cast Range reduced from +15m to +8m
  - [nerf] Shadow Transformation: Yamato: Shadow Transformation - Cooldown increased from 150s to 160s (moved to T2)

## Knowledge base: current state of every hero (pre-patch)

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
  provisional: false
McGinnis:
  name: McGinnis
  role: poke/siege controller
  archetypes:
  - poke/siege
  - tank/frontline
  tier: B
  trend: stable
  why: Turret/wall zone controller who still wins the pre-announced hub fights, but
    four off-lane corridors pull the map's fights away from her static setup, flattening
    the Paint the Town gain. Turrets still farm grouped camps and Barrel Mimics from
    cover; still useless into mobile dive + AoE.
  core_items:
  - Intensifying Magazine
  - Monster Rounds
  - Heroic Aura
  - Extra Charge
  - Mystic Vulnerability
  - Escalating Exposure
  - Rapid Recharge
  build_variants:
  - Gun turret
  - Spirit turret/ult
  - Zoning utility
  enabled_by:
  - frontline tanks (Abrams, Dynamo, Billy) who hold space for turret and Medicinal
    Specter setups
  - telegraphed Plaza/Bell Tower hub fights (turret/wall zoning)
  - turrets clear grouped Haunt camps
  - parry-cooldown change punishes dives into her zone
  - "tempo/objective meta \u2014 Guardian bounty +10% rewards her lane siege"
  - Mini Turret HP buffs (08-12) and Medicinal Specter resist
  countered_by:
  - mobile burst divers (Yamato, Holliday, Silver) that jump the wall and delete turrets
  - AoE spirit burst (Lady Geist, Celeste, Dynamo) that clears turret stacks
  - global -20% slow nerf, which weakens her wall/Suppressor zoning
  last_changed_patch: Minor Update - 08-12-2026
  notes: 'Shh... This Won''t Hurt a Bit. (10-20, indirect): the map''s four off-lane
    corridors spread fights away from her turret/wall setup, flattening the hub-fight
    gain; turrets still clear grouped Haunt camps and Barrel Mimics from cover.

    Paint the Town (10-16, indirect): turrets clear the new grouped Haunt camps and
    zone the telegraphed Plaza/Bell Tower hubs, while the objective-parry change punishes
    dives into her wall.

    City Never Sleeps (09-29, indirect): telegraphed hub fights and the dive-punishing
    parry change favor her turret/wall zoning, and turrets clear the grouped Haunt
    camps.'
  builds:
  - name: Gun turret
    damage: gun
    core_items:
    - Monster Rounds
    - Intensifying Magazine
    - Heroic Aura
    popularity: primary
    notes: "Highest-share core (Intensifying Magazine 77%, Monster Rounds 62%) \u2014\
      \ ramp fire rate behind turret cover, Monster Rounds for lane farm, Heroic Aura\
      \ to buff team fights."
  - name: Spirit turret/ult
    damage: spirit
    core_items:
    - Extra Charge
    - Mystic Vulnerability
    - Escalating Exposure
    - Rapid Recharge
    popularity: secondary
    notes: Extra Charge+Rapid Recharge for turret uptime, Mystic Vulnerability+Escalating
      Exposure to amp turret and Heavy Barrage damage into mid-game fights.
  - name: Zoning utility
    damage: hybrid
    core_items:
    - Healbane
    - Enduring Speed
    - Extra Stamina
    - Enchanter's Emblem
    - Suppressor
    popularity: niche
    notes: Defensive/support fillers (39-47% each) that keep her alive and zoning;
      Suppressor applies her slow, Medicinal Specter covers extended fights.
  matchups:
    beats:
    - Lash
    - Drifter
    loses_to:
    - Wraith
  matchup_notes: "She beats melee divers who must walk into her zone \u2014 Lash 56%,\
    \ Drifter 52% \u2014 because Spectral Wall cuts their approach and turrets punish\
    \ the dive. She loses to Wraith (44%, i.e. Wraith wins 56%): a ranged gun carry\
    \ who out-ranges and bursts her before the wall matters. Small samples (150-230\
    \ games), so treat as directional."
  confidence: 0.55
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
  provisional: false
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
  provisional: false
Calico:
  name: Calico
  role: mobile assassin
  archetypes:
  - mobile assassin
  tier: A
  trend: rising
  why: "Tempo roamer whose district and Steam-Vent routes sharpen her gank angles,\
    \ but cat form still cannot heavy-melee Tough Crates, so her income stays kill-based.\
    \ The rising frontline (Abrams, Rat King) caps her at A \u2014 she cannot burst\
    \ through stacked HP."
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
  - comeback-soul nerf (winning lane wins game)
  - off-map soul generation as a 3/4
  - Sprint Boots
  - mobile assassin archetype
  countered_by:
  - CC/lockdown (Dynamo, Mo & Krill)
  - tank frontline she cannot burst (Abrams, Victor)
  - long-range kiting gun carries (Vyper, Warden)
  - burst vs low HP (Yamato)
  last_changed_patch: Minor Update - 07-28-2026
  notes: 'Shh... This Won''t Hurt a Bit. (10-20, indirect): districts and vent invisibility
    extend her roam; cat form still can''t heavy-melee Tough Crates, and the frontline
    meta gives her more unburstable bodies.

    Paint the Town (10-16, indirect): tempo snowball plus new district/Steam-Vent
    routes suit her roam; cat form still cannot heavy-melee Tough Crates, so lean
    kills/off-map souls.

    10-14: Baba (beats her ~58%, her worst listed matchup) took a major nerf - eases
    with no cost to her; no direct change.'
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
  provisional: false
Lash:
  name: Lash
  role: mobile initiator
  archetypes:
  - mobile assassin
  - initiator
  tier: S
  trend: rising
  why: 'Highest-pick S-tier initiator: districts and Steam Vents extend his dive routes,
    and Bell Tower/Sunken Plaza concentrate teams into Ground Strike setups. The objective-parry
    reset removal takes a free defensive out from the fights he starts; Silver/air-drag
    remain the counter.'
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
  last_changed_patch: Minor Update - 09-16-2026
  notes: "Shh... This Won't Hurt a Bit. (10-20, indirect): districts and Steam Vents\
    \ extend his dive routes beyond three lanes, and hub fights at Bell Tower/Sunken\
    \ Plaza concentrate teams into Ground Strike; objective parries no longer reset.\n\
    Paint the Town: no direct change; new districts/Steam Vents extend his dive routes\
    \ and the green-lane roof/tree keeps permanent lane high ground \u2014 still S.\n\
    09-16: Ground Strike T3 scaling + per-meter damage up, gun falloff changed, Flog\
    \ heal nerfed."
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
  trend: falling
  why: 'Late-scaling Affliction burst carry with no comeback safety net: the gutted
    comeback souls and the Cultist Sacrifice bounty trim (180->170%) removed the bail-out
    his slow farm-and-scale line needed, so he stays popular at 46.2% WR but rarely
    spikes before tempo ends the game. Beats squishy carries he can cloak onto; folds
    to anything that out-ranges or sticks to him.'
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
  notes: 'Changelog: 09-16 - no direct line; tier stays B (falling) on the gutted
    comeback economy + Cultist Sacrifice trim. Low confidence on whether Flying Cloak
    counts as a flyer for the new air-drag slow rule.

    Creators'' ''7k on gun items'' claim is contradicted by 30-day usage: the only
    weapons with real share are farm items (Monster Rounds 92%, Cultist Sacrifice
    93%); there is no gun build. Data wins.

    Old entry''s core (Boundless Spirit, Echo Shard, Fortitude) shows zero current
    usage - replaced with the spirit stack the data actually shows.'
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
  provisional: false
The Doorman:
  name: The Doorman
  role: utility initiator
  archetypes:
  - initiator
  - burst caster
  tier: B
  trend: stable
  why: Popular but not-winning setup initiator (46.5% WR) whose delayed payoff the
    tempo read still punishes - but Bell Tower's single rope and ~280-soul payout
    hand his Doorway a real kidnap play on the new top objective. Reach still comes
    late and early snowball beats him.
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
  last_changed_patch: Minor Update - 08-12-2026
  notes: "10-20 Shh...: no direct change; Bell Tower's single rope + ~280 souls keeps\
    \ the Doorway kidnap real \u2014 pre-place the door at the base before roping\
    \ up.\nPaint the Town: no direct change; Bell Tower's single rope and ~280-soul\
    \ payout give his Doorway a real kidnap objective play, but tempo dive still beats\
    \ his setup.\n09-16: no direct line; loses his Veil Walker disengage (Sprint Boots\
    \ + movespeed-on-break removed)."
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
Violet:
  name: Violet
  role: spirit zone-control caster
  archetypes:
  - spirit carry
  - burst caster
  - initiator
  - late scaler
  tier: C
  trend: stable
  why: "Her systems fit is genuine \u2014 AoE on grouped Haunts, 116 heavy melee on\
    \ Tough Crates, and scheduled Bell Tower/Plaza contests all pay a zone caster\
    \ \u2014 but the results are not there: 46.1% WR at a 70.9% pick rate, losing\
    \ to the meta's frontlines (Rat King 41%, Mo & Krill 41%) and to its best poke\
    \ (Vindicta 39%). Her build only converts at the T3/T4 tail (Boundless Spirit\
    \ 54.4%, Superior Cooldown 52.9%) which lands at 24-28 min, after tempo has usually\
    \ decided the lobby. Every cheap spirit and regen item she buys sits at her 46%\
    \ baseline, so the popular build is a ramp with no payoff until the game is already\
    \ lost."
  core_items:
  - Extra Spirit
  - Mystic Regeneration
  - Radiant Regeneration
  - Extra Charge
  - Improved Spirit
  - Rapid Recharge
  - Superior Cooldown
  - Boundless Spirit
  - Healing Booster
  - Tankbuster
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
  last_changed_patch: Released 2026-10-16
  notes: "7-day check-in (2026-10-23): tier B -> C, WR 50%, PR 64% over 539876 matches.\n\
    Data corrects the day-0 read: B/rising was a tooltip judgment, so C is a correction,\
    \ not a decline \u2014 46.1% WR at 70.9% PR, and she loses to frontline brawlers\
    \ rather than punishing melee. Watch whether her WR climbs with reps; the tooltip\
    \ read also claimed Seven and the gun line as wins, but Seven is 49% over 170\
    \ and Living Ink/HVR no longer appear in her item data at all. 10-20 Shh...: no\
    \ Violet changes; her position moves on systems (Haunt grouping, Tough Crates,\
    \ hub fights) and on the dive/frontline meta around her."
  builds:
  - name: Spirit caster (lead)
    damage: spirit
    core_items:
    - Extra Spirit
    - Mystic Regeneration
    - Extra Charge
    - Radiant Regeneration
    - Improved Spirit
    - Rapid Recharge
    - Superior Cooldown
    - Boundless Spirit
    popularity: primary
    notes: "Cooldown/regen ramp into T3-T4 spirit; only Superior Cooldown (52.9%)\
      \ and Boundless Spirit (54.4%) beat her 46% baseline, and both land after 24\
      \ min \u2014 the early stack is mandatory filler, not edge."
  - name: Anti-bruiser sustain
    damage: spirit
    core_items:
    - Extra Regen
    - Grit
    - Spirit Shielding
    - Healing Booster
    - Tankbuster
    popularity: secondary
    notes: "Vitality/regen shell plus Tankbuster (57% share, 49.7% WR, 24.4 min) to\
      \ chew the Rat King/Mo & Krill/Victor/Shiv frontlines \u2014 her best-converting\
      \ mid item, but the regen half dies to Healbane."
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
  trend: stable
  why: "Nurse Harrow converts firing uptime into healing, and the rising melee-frontline\
    \ meta (Shiv, Billy, Rat King, Victor) is exactly the fight shape she wins \u2014\
    \ her best win rates run 55-59% against frontliners she can kite and DoT, and\
    \ hub fights at Bell Tower and Sunken Plaza keep those fights grouped. She loses\
    \ the range war: Baba, Celeste and Wraith all trade from outside the fear cone\
    \ while 730 HP, zero regen and no dash leave her no answer. B holds \u2014 50.6%\
    \ at a 75% pick rate is her real level rather than release noise, and her item\
    \ curve (T3 spirit at 23-24 min, Ricochet at 27) is the one thing the tempo patch\
    \ punishes."
  core_items:
  - Extra Regen
  - Extended Magazine
  - Titanic Magazine
  - Extra Stamina
  - Kinetic Dash
  - Healing Booster
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
  last_changed_patch: Released 2026-10-20
  notes: "7-day check-in (2026-10-27): tier B -> B, WR 51%, PR 63% over 607252 matches.\n\
    Data overrides the day-0 read: Swift Striker, High-Velocity Rounds and Active\
    \ Reload show no meaningful share (Titanic Magazine is the weapon core at 98%\
    \ / 6.7m), and the 7-day spread contains none of the dash assassins the fear-cone\
    \ thesis predicted.\nExtra Regen is not the trap the previous note called it \u2014\
    \ 97% at 2.1m with a baseline win rate makes it a mandatory lane tax for 0 base\
    \ regen, indifferent rather than informative.\nChangelog: released 2026-10-20\
    \ in Shh... This Won't Hurt a Bit., first full-week check (7.3k matches, no creator\
    \ content); nearly every item WR sits at 50.5-51%, so build-level signals are\
    \ weak and confidence is capped."
  builds:
  - name: Mag-dump sustain
    damage: gun
    core_items:
    - Extra Regen
    - Extended Magazine
    - Titanic Magazine
    - Extra Stamina
    - Kinetic Dash
    - Healing Booster
    popularity: primary
    notes: 'The entire build lands before 10 minutes and buys uptime, not damage:
      Titanic Magazine (98%) is her fire-rate package now that Swift Striker shows
      no meaningful share, and Kinetic Dash plus Extra Stamina buy the dash her kit
      lacks.'
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
      \ win rates \u2014 ability uptime, not raw spirit, is the payload."
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
Graves | 57.5 | 44.6 | 975754
Rat King | 56.0 | 57.7 | 1263311
Paige | 55.2 | 28.7 | 627572
Victor | 54.7 | 31.1 | 680406
Seven | 54.2 | 32.5 | 711042
Kelvin | 54.0 | 12.7 | 278760
Baba | 53.7 | 15.9 | 348477
Haze | 52.9 | 43.8 | 959112
Ivy | 52.6 | 18.8 | 411145
Abrams | 51.9 | 27.8 | 608185
Dynamo | 51.8 | 20.5 | 448966
Nurse Harrow | 51.8 | 43.4 | 949091
Lady Geist | 51.3 | 22.2 | 486232
Violet | 51.3 | 54.8 | 1199212
Mo & Krill | 51.2 | 19.9 | 435108
Wraith | 50.8 | 34.2 | 748661
Lash | 50.5 | 30.3 | 663629
Deadman Danny | 50.3 | 52.8 | 1155679
Drifter | 50.3 | 35.4 | 774410
Apollo | 49.3 | 27.8 | 609028
Infernus | 49.2 | 35.0 | 766343
Vindicta | 48.7 | 30.0 | 657244
Celeste | 48.4 | 33.4 | 730428
Bebop | 48.4 | 35.3 | 772388
McGinnis | 48.4 | 11.5 | 250940
Billy | 48.3 | 29.8 | 652717
Calico | 48.0 | 13.9 | 304437
Yamato | 47.4 | 26.5 | 579560
Warden | 47.2 | 11.0 | 241141
Venator | 47.1 | 39.6 | 866985
Grey Talon | 46.7 | 15.8 | 346642
Holliday | 46.3 | 18.6 | 407285
Solomon | 46.1 | 20.6 | 449991
Vyper | 46.1 | 13.7 | 298943
Silver | 46.0 | 29.3 | 642152
Paradox | 45.7 | 23.8 | 520854
Viscous | 45.6 | 11.9 | 260723
The Doorman | 45.4 | 14.7 | 321799
Shiv | 45.1 | 25.1 | 548707
Rem | 45.1 | 31.0 | 678562
Mina | 44.8 | 38.4 | 840782
Mirage | 44.7 | 10.4 | 227138
Sinclair | 44.7 | 9.7 | 211335
Pocket | 44.5 | 16.3 | 357661

## What to do

Produce an entry for **every hero in the knowledge base**, including heroes with no direct changes. For each hero combine:

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


## Creator sources published after this patch (optional corroboration; the notes, KB and snapshot remain primary — if a source contradicts them, say so and keep your own read)

(none)

For heroes with nothing relevant (no direct changes, no affected core items, archetype neutral) set direction "neutral", magnitude "none", and keep reasons empty. Do not pad.

`tier_after` is your call on the post-patch tier (S/A/B/C/D); keep `tier_before` from the KB (use "?" if unknown). Only move a tier when the reasons justify it. `confidence` reflects how sure you are about the direction, 0-1.

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
      "one_liner": "<= 20 words a player would actually say about this hero after the patch"
    }
  ]
}
