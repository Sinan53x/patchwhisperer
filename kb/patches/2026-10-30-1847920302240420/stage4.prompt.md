# Task: synthesis (the verdict and the meta thesis)

Patch: Halloween 2026 + Gameplay Update (2026-10-30)
Change counts: General 269, total 269

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

## Item analysis

{
 "items": [
  {
   "item": "High-Velocity Rounds",
   "direction": "nerf",
   "magnitude": "minor",
   "summary": "Base bullet velocity 60→45% makes the cheap T2 pickup land fewer max-range shots; upgrades keep their velocity, so the cut bites the early lane-poke window, not the finished build. Poke carries who open on it feel it most in the first ten minutes.",
   "affected_heroes": [
    {
     "hero": "Vindicta",
     "relationship": "core",
     "effect": "down",
     "why": "Gun-poke build opens HVR for max-range trading; slower bullets cost early picks."
    },
    {
     "hero": "Grey Talon",
     "relationship": "core",
     "effect": "down",
     "why": "Hybrid owl opens HVR; velocity loss hurts his long-range lane poke."
    },
    {
     "hero": "Paradox",
     "relationship": "core",
     "effect": "down",
     "why": "Carbine sniper core; slower bullets make max-range carbine picks less reliable."
    },
    {
     "hero": "Deadman Danny",
     "relationship": "core",
     "effect": "down",
     "why": "HVR is his lone weapon staple; velocity cut trims his poke."
    }
   ],
   "build_shift": "Pushes buyers to upgrade faster to recover velocity rather than sit on the base item.",
   "rows": [
    {
     "label": "Bullet velocity",
     "old": "60%",
     "new": "45%",
     "text": null,
     "effect": "bad",
     "ability": null
    },
    {
     "label": "Upgrades",
     "old": null,
     "new": null,
     "text": "Unaffected by velocity cut",
     "effect": "neutral",
     "ability": null
    }
   ]
  },
  {
   "item": "Express Shot",
   "direction": "nerf",
   "magnitude": "minor",
   "summary": "5% off secondary-fire damage and growth trims the carbine-crit payoff; Paradox's sniper line and Viscous's spirit-hybrid poke lose top-end, not identity.",
   "affected_heroes": [
    {
     "hero": "Paradox",
     "relationship": "core",
     "effect": "down",
     "why": "Express Shot rewards carbine crits in her sniper build."
    },
    {
     "hero": "Viscous",
     "relationship": "core",
     "effect": "down",
     "why": "Spirit-hybrid Splatter/Punch shell runs Express Shot."
    },
    {
     "hero": "Deadman Danny",
     "relationship": "situational",
     "effect": "down",
     "why": "Hybrid charged-shot variant uses it."
    }
   ],
   "build_shift": "",
   "rows": [
    {
     "label": "Secondary fire",
     "old": null,
     "new": null,
     "text": "Damage and growth -5%",
     "effect": "bad",
     "ability": null
    }
   ]
  },
  {
   "item": "Point Blank",
   "direction": "buff",
   "magnitude": "minor",
   "summary": "+0.5s slow extends the stick on a close-range item; helps melee/close bruisers hold a target but won't move it into core.",
   "affected_heroes": [
    {
     "hero": "Abrams",
     "relationship": "new_option",
     "effect": "up",
     "why": "Close-range bruiser who wants targets stuck in melee range."
    }
   ],
   "build_shift": "",
   "rows": [
    {
     "label": "Slow duration",
     "old": "2s",
     "new": "2.5s",
     "text": null,
     "effect": "good",
     "ability": null
    }
   ]
  },
  {
   "item": "Hunter's Aura",
   "direction": "rework",
   "magnitude": "moderate",
   "summary": "Requiring line of sight removes the through-wall shred that made this a frontline stat-check; buyers now only get value on targets they can actually see, so it's weaker in corridor and objective fights where walls break LOS.",
   "affected_heroes": [
    {
     "hero": "Abrams",
     "relationship": "core",
     "effect": "down",
     "why": "Melee brawler core; loses the through-wall shred in clumped fights."
    },
    {
     "hero": "Silver",
     "relationship": "core",
     "effect": "down",
     "why": "Gun-tank core; aura no longer reaches targets behind cover."
    },
    {
     "hero": "Yamato",
     "relationship": "core",
     "effect": "down",
     "why": "Late spirit-burst build runs Hunter's Aura for shred."
    }
   ],
   "build_shift": "",
   "rows": [
    {
     "label": "Line of sight",
     "old": null,
     "new": null,
     "text": "No longer affects enemies through walls",
     "effect": "bad",
     "ability": null
    }
   ]
  },
  {
   "item": "Shadow Weave",
   "direction": "rework",
   "magnitude": "moderate",
   "summary": "Trades fire rate and melee damage for a bigger +50% ambush weapon-damage amp that needs 6s stealthed to charge and now applies to the ability that breaks stealth — a slower, burstier ambush. With Steam Vents losing invisibility this patch, Shadow Weave is again the only invis-engage tool, partly offsetting the tempo cost.",
   "affected_heroes": [
    {
     "hero": "Warden",
     "relationship": "core",
     "effect": "neutral",
     "why": "Bigger ambush amp but the 6s buildup slows his walk-up cage; regains exclusivity as vents lose invis."
    }
   ],
   "build_shift": "Becomes a pure gun-carry ambush item rather than a melee/cage tool.",
   "rows": [
    {
     "label": "Ambush fire rate",
     "old": null,
     "new": null,
     "text": "Removed",
     "effect": "bad",
     "ability": null
    },
    {
     "label": "Ambush melee",
     "old": null,
     "new": null,
     "text": "Removed",
     "effect": "bad",
     "ability": null
    },
    {
     "label": "Ambush weapon dmg",
     "old": null,
     "new": null,
     "text": "+50% (new)",
     "effect": "good",
     "ability": null
    },
    {
     "label": "Charge time",
     "old": null,
     "new": null,
     "text": "Builds over 6s stealthed",
     "effect": "bad",
     "ability": null
    },
    {
     "label": "Ability break",
     "old": null,
     "new": null,
     "text": "Ambush bonus applies to breaking ability",
     "effect": "good",
     "ability": null
    }
   ]
  },
  {
   "item": "Toxic Bullets",
   "direction": "buff",
   "magnitude": "minor",
   "summary": "35→40% anti-heal strengthens the sustained-heal cut on Infernus's burn-gun and Mirage's hybrid; in a patch that also buffs Decay and makes Healbane stack, anti-heal is being pushed hard.",
   "affected_heroes": [
    {
     "hero": "Infernus",
     "relationship": "core",
     "effect": "up",
     "why": "Burn gun-carry leans on Toxic Bullets for anti-heal."
    },
    {
     "hero": "Mirage",
     "relationship": "core",
     "effect": "up",
     "why": "Spirit-amp hybrid runs Toxic Bullets."
    },
    {
     "hero": "Drifter",
     "relationship": "situational",
     "effect": "up",
     "why": "Anti-heal bruiser variant."
    },
    {
     "hero": "Graves",
     "relationship": "situational",
     "effect": "up",
     "why": "On-hit gun build uses Toxic Bullets vs tanks."
    }
   ],
   "build_shift": "",
   "rows": [
    {
     "label": "Anti-heal",
     "old": "35%",
     "new": "40%",
     "text": null,
     "effect": "good",
     "ability": null
    }
   ]
  },
  {
   "item": "Armor Piercer",
   "direction": "buff",
   "magnitude": "minor",
   "summary": "55→60% proc is a small consistency gain on a %-pen item; won't change who buys it.",
   "affected_heroes": [],
   "build_shift": "",
   "rows": [
    {
     "label": "Proc chance",
     "old": "55%",
     "new": "60%",
     "text": null,
     "effect": "good",
     "ability": null
    }
   ]
  },
  {
   "item": "Glass Cannon",
   "direction": "buff",
   "magnitude": "minor",
   "summary": "80→85% weapon damage nudges the glass-cannon capstone; still a win-more late buy.",
   "affected_heroes": [],
   "build_shift": "",
   "rows": [
    {
     "label": "Weapon damage",
     "old": "80%",
     "new": "85%",
     "text": null,
     "effect": "good",
     "ability": null
    }
   ]
  },
  {
   "item": "Spiritual Overflow",
   "direction": "buff",
   "magnitude": "minor",
   "summary": "+2 spirit power from component changes is a token recovery after the 09-16 gutting; Infernus already dropped it, so it stays a fringe slot.",
   "affected_heroes": [
    {
     "hero": "Baba",
     "relationship": "situational",
     "effect": "up",
     "why": "Spirit-stacking bruiser can slot it."
    },
    {
     "hero": "Warden",
     "relationship": "situational",
     "effect": "up",
     "why": "Spirit on-hit line uses it."
    },
    {
     "hero": "Infernus",
     "relationship": "situational",
     "effect": "neutral",
     "why": "Already dropped it post-09-16; small recovery won't restore it."
    }
   ],
   "build_shift": "",
   "rows": [
    {
     "label": "Spirit power",
     "old": "6",
     "new": "8",
     "text": null,
     "effect": "good",
     "ability": null
    }
   ]
  },
  {
   "item": "Crippling Headshot",
   "direction": "buff",
   "magnitude": "minor",
   "summary": "-35→-40% anti-heal adds to the patch's anti-heal stack; marginal on its own.",
   "affected_heroes": [],
   "build_shift": "",
   "rows": [
    {
     "label": "Anti-heal",
     "old": "-35%",
     "new": "-40%",
     "text": null,
     "effect": "good",
     "ability": null
    }
   ]
  },
  {
   "item": "Golden Goose Egg",
   "direction": "buff",
   "magnitude": "minor",
   "summary": "-15→-12% damage penalty is a small relief, but the 09-16 nerf (souls/min, net-worth counting) still leaves it unbuyable.",
   "affected_heroes": [],
   "build_shift": "",
   "rows": [
    {
     "label": "Damage penalty",
     "old": "-15%",
     "new": "-12%",
     "text": null,
     "effect": "good",
     "ability": null
    }
   ]
  },
  {
   "item": "Spirit Sap",
   "direction": "nerf",
   "magnitude": "moderate",
   "summary": "+4s cooldown and -5m range cut both the uptime and the reach of a spirit poke/sap tool; whoever used it to chip from range loses a real chunk of value.",
   "affected_heroes": [],
   "build_shift": "",
   "rows": [
    {
     "label": "Cooldown",
     "old": "18s",
     "new": "22s",
     "text": null,
     "effect": "bad",
     "ability": null
    },
    {
     "label": "Cast range",
     "old": "40m",
     "new": "35m",
     "text": null,
     "effect": "bad",
     "ability": null
    }
   ]
  },
  {
   "item": "Mystic Slow",
   "direction": "buff",
   "magnitude": "minor",
   "summary": "-10→-12% dash-distance slow makes the slow slightly harder to dash out of; small.",
   "affected_heroes": [],
   "build_shift": "",
   "rows": [
    {
     "label": "Dash distance slow",
     "old": "-10%",
     "new": "-12%",
     "text": null,
     "effect": "good",
     "ability": null
    }
   ]
  },
  {
   "item": "Decay",
   "direction": "buff",
   "magnitude": "minor",
   "summary": "-50→-55% heal cut strengthens the default anti-heal spirit slot; with Healbane now stacking and Toxic Bullets buffed, anti-heal is the patch's clearest item theme.",
   "affected_heroes": [
    {
     "hero": "Infernus",
     "relationship": "core",
     "effect": "up",
     "why": "Anti-heal spirit slot."
    },
    {
     "hero": "Lady Geist",
     "relationship": "core",
     "effect": "up",
     "why": "Runs Decay into sustain comps."
    },
    {
     "hero": "Abrams",
     "relationship": "core",
     "effect": "up",
     "why": "Anti-heal answer to enemy fronts."
    },
    {
     "hero": "Mo & Krill",
     "relationship": "core",
     "effect": "up",
     "why": "Anti-heal into sustain."
    },
    {
     "hero": "Shiv",
     "relationship": "core",
     "effect": "up",
     "why": "Anti-heal bruiser."
    },
    {
     "hero": "Viscous",
     "relationship": "core",
     "effect": "up",
     "why": "Anti-heal enabler."
    },
    {
     "hero": "Drifter",
     "relationship": "core",
     "effect": "up",
     "why": "Anti-heal bruiser."
    },
    {
     "hero": "Rem",
     "relationship": "core",
     "effect": "up",
     "why": "Anti-heal support slot."
    },
    {
     "hero": "Billy",
     "relationship": "core",
     "effect": "up",
     "why": "Anti-heal frontline."
    }
   ],
   "build_shift": "",
   "rows": [
    {
     "label": "Heal reduction",
     "old": "-50%",
     "new": "-55%",
     "text": null,
     "effect": "good",
     "ability": null
    }
   ]
  },
  {
   "item": "Radiant Regeneration",
   "direction": "nerf",
   "magnitude": "major",
   "summary": "Fourth cumulative trim and the biggest yet — spirit-damage regen scaling 0.35→0.25, heal-on-cast 65→40 with 1.7→1.4 boon scaling, and the heal now only fires in combat. The regen sustain shell Baba, Lady Geist, Shiv, Celeste and Kelvin build around is materially weaker; spirit-stackers lose the most.",
   "affected_heroes": [
    {
     "hero": "Baba",
     "relationship": "core",
     "effect": "down",
     "why": "94% buy; regen stack is her whole shell."
    },
    {
     "hero": "Lady Geist",
     "relationship": "core",
     "effect": "down",
     "why": "~98% buy; spirit Soul-Exchange variant loses most."
    },
    {
     "hero": "Shiv",
     "relationship": "core",
     "effect": "down",
     "why": "Near-universal regen core chipped again."
    },
    {
     "hero": "Celeste",
     "relationship": "core",
     "effect": "down",
     "why": "Sustain-burst carrier stacks it."
    },
    {
     "hero": "Kelvin",
     "relationship": "core",
     "effect": "down",
     "why": "Rival sustain trimmed, but his own regen layer also shrinks."
    }
   ],
   "build_shift": "Pushes sustain toward lifesteal items (Spirit/Bullet Lifesteal, Leech buffed) and Healing Booster's out-of-combat regen.",
   "rows": [
    {
     "label": "Spirit-dmg regen scaling",
     "old": "0.35",
     "new": "0.25",
     "text": null,
     "effect": "bad",
     "ability": null
    },
    {
     "label": "Heal on cast",
     "old": "65",
     "new": "40",
     "text": null,
     "effect": "bad",
     "ability": null
    },
    {
     "label": "Heal boon scaling",
     "old": "1.7",
     "new": "1.4",
     "text": null,
     "effect": "bad",
     "ability": null
    },
    {
     "label": "Heal trigger",
     "old": null,
     "new": null,
     "text": "Only in combat now",
     "effect": "bad",
     "ability": null
    }
   ]
  },
  {
   "item": "Silence Wave",
   "direction": "buff",
   "magnitude": "minor",
   "summary": "+40 bonus health makes the silence utility item a slightly better frontline buy; won't change its role.",
   "affected_heroes": [],
   "build_shift": "",
   "rows": [
    {
     "label": "Bonus health",
     "old": "+50",
     "new": "+90",
     "text": null,
     "effect": "good",
     "ability": null
    }
   ]
  },
  {
   "item": "Torment Pulse",
   "direction": "buff",
   "magnitude": "minor",
   "summary": "18→22% melee resistance helps the spirit-bruiser frontlines survive melee dives a touch better.",
   "affected_heroes": [
    {
     "hero": "Mo & Krill",
     "relationship": "core",
     "effect": "up",
     "why": "Spirit bruiser runs Torment Pulse."
    },
    {
     "hero": "Shiv",
     "relationship": "core",
     "effect": "up",
     "why": "Cooldown spirit shred build."
    },
    {
     "hero": "Victor",
     "relationship": "core",
     "effect": "up",
     "why": "Spirit sustain bruiser."
    },
    {
     "hero": "Yamato",
     "relationship": "core",
     "effect": "up",
     "why": "Late spirit-burst build."
    },
    {
     "hero": "Baba",
     "relationship": "core",
     "effect": "up",
     "why": "Regen bruiser AoE aura."
    },
    {
     "hero": "Celeste",
     "relationship": "core",
     "effect": "up",
     "why": "Sustain-burst carrier."
    }
   ],
   "build_shift": "",
   "rows": [
    {
     "label": "Melee resistance",
     "old": "18%",
     "new": "22%",
     "text": null,
     "effect": "good",
     "ability": null
    }
   ]
  },
  {
   "item": "Echo Shard",
   "direction": "buff",
   "magnitude": "moderate",
   "summary": "Post-cast 0.5→0.2s tightens the double-cast window, making the reset item's combo execution faster for every buyer; it's the meta's connective item, so this quietly speeds up the whole caster roster.",
   "affected_heroes": [
    {
     "hero": "Paradox",
     "relationship": "situational",
     "effect": "up",
     "why": "Echo Shard bomb combo executes faster."
    },
    {
     "hero": "Haze",
     "relationship": "situational",
     "effect": "up",
     "why": "Reset combos benefit from shorter lockout."
    },
    {
     "hero": "Bebop",
     "relationship": "situational",
     "effect": "up",
     "why": "Double-cast hook/bomb lines speed up."
    },
    {
     "hero": "Pocket",
     "relationship": "situational",
     "effect": "up",
     "why": "Burst reset combos."
    }
   ],
   "build_shift": "",
   "rows": [
    {
     "label": "Post-cast time",
     "old": "0.5s",
     "new": "0.2s",
     "text": null,
     "effect": "good",
     "ability": null
    }
   ]
  },
  {
   "item": "Focus Lens",
   "direction": "buff",
   "magnitude": "minor",
   "summary": "-5s cooldown plus the barrier-damage fix makes the spirit-amp slightly more reliable; still a situational standoff pick.",
   "affected_heroes": [],
   "build_shift": "",
   "rows": [
    {
     "label": "Cooldown",
     "old": "45s",
     "new": "40s",
     "text": null,
     "effect": "good",
     "ability": null
    },
    {
     "label": "Barrier damage",
     "old": null,
     "new": null,
     "text": "Now counts toward repeat damage",
     "effect": "good",
     "ability": null
    }
   ]
  },
  {
   "item": "Lightning Scroll",
   "direction": "rework",
   "magnitude": "moderate",
   "summary": "Now scaling 0.35 off spirit power turns a flat-damage item into a spirit-build tool, and the extra dash slow helps it stick; spirit casters gain a real option, gun builds lose interest.",
   "affected_heroes": [],
   "build_shift": "Moves from a flat-damage pickup to a spirit-scaling slot competing with other spirit poke items.",
   "rows": [
    {
     "label": "Damage scaling",
     "old": null,
     "new": null,
     "text": "Now scales with Spirit Power (0.35)",
     "effect": "good",
     "ability": null
    },
    {
     "label": "Dash distance slow",
     "old": "-10%",
     "new": "-12%",
     "text": null,
     "effect": "good",
     "ability": null
    }
   ]
  },
  {
   "item": "Rebuttal",
   "direction": "nerf",
   "magnitude": "minor",
   "summary": "Parry cooldown reduction drops from -1.75s to -1.25s, so you parry less often — a straight trim to the parry-utility item despite the buff tag.",
   "affected_heroes": [],
   "build_shift": "",
   "rows": [
    {
     "label": "Parry CD reduction",
     "old": "-1.75s",
     "new": "-1.25s",
     "text": null,
     "effect": "bad",
     "ability": null
    }
   ]
  },
  {
   "item": "Battle Vest",
   "direction": "buff",
   "magnitude": "minor",
   "summary": "18→22% weapon damage strengthens Venator's gun-bruiser core and any frontline M1 build; small but on a core slot.",
   "affected_heroes": [
    {
     "hero": "Venator",
     "relationship": "core",
     "effect": "up",
     "why": "Gun-bruiser core runs Battle Vest."
    }
   ],
   "build_shift": "",
   "rows": [
    {
     "label": "Weapon damage",
     "old": "18%",
     "new": "22%",
     "text": null,
     "effect": "good",
     "ability": null
    }
   ]
  },
  {
   "item": "Bullet Lifesteal",
   "direction": "buff",
   "magnitude": "moderate",
   "summary": "+4% weapon damage and +2% lifesteal make the cheap T2 sustain item a better early buy; Venator and Infernus get more from their lane-sustain slot, and it competes harder with the regen items just nerfed.",
   "affected_heroes": [
    {
     "hero": "Venator",
     "relationship": "core",
     "effect": "up",
     "why": "Gun-bruiser lane-sustain slot."
    },
    {
     "hero": "Infernus",
     "relationship": "core",
     "effect": "up",
     "why": "Standard early lifesteal on gun carries."
    }
   ],
   "build_shift": "Absorbs some of the demand lost by Radiant Regeneration/Healing Booster nerfs.",
   "rows": [
    {
     "label": "Weapon damage",
     "old": "6%",
     "new": "10%",
     "text": null,
     "effect": "good",
     "ability": null
    },
    {
     "label": "Bullet lifesteal",
     "old": "13%",
     "new": "15%",
     "text": null,
     "effect": "good",
     "ability": null
    }
   ]
  },
  {
   "item": "Healbane",
   "direction": "rework",
   "magnitude": "moderate",
   "summary": "Multiple Healbanes now stack with diminishing returns — a team-wide anti-heal buff — but heal-on-kill drops 275→170+3/boon, cutting the self-sustain that made it a solo bruiser pick. Net: better as a team anti-heal tool, worse as personal sustain.",
   "affected_heroes": [
    {
     "hero": "Apollo",
     "relationship": "core",
     "effect": "neutral",
     "why": "Team anti-heal up, personal heal-on-kill down."
    },
    {
     "hero": "Kelvin",
     "relationship": "core",
     "effect": "neutral",
     "why": "Anti-heal value up, self-sustain down."
    },
    {
     "hero": "Shiv",
     "relationship": "core",
     "effect": "neutral",
     "why": "Anti-heal doubles as sustain; kill-heal trimmed."
    },
    {
     "hero": "Mo & Krill",
     "relationship": "core",
     "effect": "neutral",
     "why": "Self-sustain from kills reduced."
    },
    {
     "hero": "Infernus",
     "relationship": "core",
     "effect": "neutral",
     "why": "Anti-heal role intact, kill-heal down."
    },
    {
     "hero": "Yamato",
     "relationship": "core",
     "effect": "neutral",
     "why": "Anti-heal into bruisers; kill-heal trimmed."
    }
   ],
   "build_shift": "",
   "rows": [
    {
     "label": "Stacking",
     "old": null,
     "new": null,
     "text": "Multiple sources stack (diminishing)",
     "effect": "good",
     "ability": null
    },
    {
     "label": "Heal on kill",
     "old": "275",
     "new": "170 + 3/Boon",
     "text": null,
     "effect": "bad",
     "ability": null
    }
   ]
  },
  {
   "item": "Healing Booster",
   "direction": "rework",
   "magnitude": "moderate",
   "summary": "Losing the Extra Regen component and +3 flat regen guts the sustain shell's backbone; the +1→+2 out-of-combat regen doesn't replace it. Combined with the Radiant Regeneration nerf, regen-stacking supports lose a real chunk of sustain.",
   "affected_heroes": [
    {
     "hero": "Kelvin",
     "relationship": "core",
     "effect": "down",
     "why": "Extra Regen/Healing Booster core loses its cheap upgrade path and flat regen."
    },
    {
     "hero": "Apollo",
     "relationship": "core",
     "effect": "down",
     "why": "Spirit bruiser runs Healing Booster for sustain."
    },
    {
     "hero": "Victor",
     "relationship": "core",
     "effect": "down",
     "why": "Sustain stack leans on Healing Booster."
    },
    {
     "hero": "Baba",
     "relationship": "core",
     "effect": "down",
     "why": "Regen bruiser shell."
    },
    {
     "hero": "Rem",
     "relationship": "core",
     "effect": "down",
     "why": "Heal support sustain layer."
    },
    {
     "hero": "Ivy",
     "relationship": "core",
     "effect": "down",
     "why": "Heal/anti-heal support package."
    },
    {
     "hero": "Celeste",
     "relationship": "core",
     "effect": "down",
     "why": "Sustain-burst carrier."
    },
    {
     "hero": "Solomon",
     "relationship": "core",
     "effect": "down",
     "why": "Sustain layer."
    }
   ],
   "build_shift": "No longer a cheap Extra Regen upgrade; must be bought standalone and now competes with buffed lifesteal items.",
   "rows": [
    {
     "label": "Component",
     "old": null,
     "new": null,
     "text": "No longer builds from Extra Regen",
     "effect": "bad",
     "ability": null
    },
    {
     "label": "Flat regen",
     "old": null,
     "new": null,
     "text": "Removed (+3)",
     "effect": "bad",
     "ability": null
    },
    {
     "label": "Out-of-combat regen",
     "old": "+1",
     "new": "+2",
     "text": null,
     "effect": "good",
     "ability": null
    }
   ]
  },
  {
   "item": "Return Fire",
   "direction": "rework",
   "magnitude": "minor",
   "summary": "Now reflects Haze's Fixation damage and the tooltip lists its 10% bullet resist — a targeted answer to Haze's stacking DoT, giving tanks a real counter-item into her.",
   "affected_heroes": [
    {
     "hero": "Haze",
     "relationship": "situational",
     "effect": "down",
     "why": "Fixation damage now gets returned by tanks holding Return Fire."
    }
   ],
   "build_shift": "",
   "rows": [
    {
     "label": "Fixation",
     "old": null,
     "new": null,
     "text": "Now returns Haze's Fixation damage",
     "effect": "good",
     "ability": null
    },
    {
     "label": "Tooltip",
     "old": null,
     "new": null,
     "text": "Lists 10% bullet resist",
     "effect": "neutral",
     "ability": null
    }
   ]
  },
  {
   "item": "Spirit Lifesteal",
   "direction": "buff",
   "magnitude": "moderate",
   "summary": "+2 spirit power and +2% lifesteal strengthen the spirit-carry sustain slot; Seven and Victor get more out of it, and it absorbs some of the demand regen items just lost.",
   "affected_heroes": [
    {
     "hero": "Seven",
     "relationship": "core",
     "effect": "up",
     "why": "Spirit AoE carry sustain slot."
    },
    {
     "hero": "Victor",
     "relationship": "core",
     "effect": "up",
     "why": "Sustain bruiser core."
    },
    {
     "hero": "Infernus",
     "relationship": "core",
     "effect": "up",
     "why": "Dashfernus spirit sustain."
    },
    {
     "hero": "Warden",
     "relationship": "core",
     "effect": "up",
     "why": "Cage bruiser sustain."
    },
    {
     "hero": "Wraith",
     "relationship": "situational",
     "effect": "up",
     "why": "Sustain gun variant."
    },
    {
     "hero": "Violet",
     "relationship": "situational",
     "effect": "up",
     "why": "Spirit lifesteal buyer."
    }
   ],
   "build_shift": "",
   "rows": [
    {
     "label": "Spirit power",
     "old": "6",
     "new": "8",
     "text": null,
     "effect": "good",
     "ability": null
    },
    {
     "label": "Spirit lifesteal",
     "old": "13%",
     "new": "15%",
     "text": null,
     "effect": "good",
     "ability": null
    }
   ]
  },
  {
   "item": "Spirit Shielding",
   "direction": "nerf",
   "magnitude": "minor",
   "summary": "18→15% spirit resist trims the defensive layer Billy and Silver lean on; small but on core slots into a spirit-burst-heavy meta.",
   "affected_heroes": [
    {
     "hero": "Billy",
     "relationship": "core",
     "effect": "down",
     "why": "Spirit shred/slow build runs Spirit Shielding."
    },
    {
     "hero": "Silver",
     "relationship": "core",
     "effect": "down",
     "why": "Gun-tank defensive layer."
    },
    {
     "hero": "Celeste",
     "relationship": "core",
     "effect": "down",
     "why": "Anti-CC tech includes Spirit Shielding."
    },
    {
     "hero": "Vyper",
     "relationship": "situational",
     "effect": "down",
     "why": "Defensive buy."
    }
   ],
   "build_shift": "",
   "rows": [
    {
     "label": "Spirit resist",
     "old": "18%",
     "new": "15%",
     "text": null,
     "effect": "bad",
     "ability": null
    }
   ]
  },
  {
   "item": "Bullet Resilience",
   "direction": "buff",
   "magnitude": "minor",
   "summary": "30→35% bullet resist plus 3→5 out-of-combat regen makes the anti-gun defensive item a bit stronger into gun-carry lobbies.",
   "affected_heroes": [],
   "build_shift": "",
   "rows": [
    {
     "label": "Bullet resistance",
     "old": "30%",
     "new": "35%",
     "text": null,
     "effect": "good",
     "ability": null
    },
    {
     "label": "Out-of-combat regen",
     "old": "3",
     "new": "5",
     "text": null,
     "effect": "good",
     "ability": null
    }
   ]
  },
  {
   "item": "Fury Trance",
   "direction": "buff",
   "magnitude": "moderate",
   "summary": "More move speed, lifesteal and weapon damage on the active steroid make it a stronger mid-fight burst tool; still niche but now worth a look on aggressive gun bruisers.",
   "affected_heroes": [],
   "build_shift": "",
   "rows": [
    {
     "label": "Active move speed",
     "old": "+1m",
     "new": "+1.5m",
     "text": null,
     "effect": "good",
     "ability": null
    },
    {
     "label": "Bullet lifesteal",
     "old": "14%",
     "new": "15%",
     "text": null,
     "effect": "good",
     "ability": null
    },
    {
     "label": "Weapon damage",
     "old": "6%",
     "new": "10%",
     "text": null,
     "effect": "good",
     "ability": null
    }
   ]
  },
  {
   "item": "Healing Nova",
   "direction": "rework",
   "magnitude": "moderate",
   "summary": "Switching from boon scaling (6) to spirit scaling (1.1) rewards spirit-stacking healers and punishes boon-stackers; Kelvin's spirit build gains, while a pure-boon support loses throughput.",
   "affected_heroes": [
    {
     "hero": "Kelvin",
     "relationship": "core",
     "effect": "up",
     "why": "Spirit-stacking healer scales the nova better."
    },
    {
     "hero": "Ivy",
     "relationship": "situational",
     "effect": "neutral",
     "why": "Heal support; depends on spirit investment."
    },
    {
     "hero": "Rem",
     "relationship": "situational",
     "effect": "neutral",
     "why": "Spirit heal support; scaling swap is a wash."
    }
   ],
   "build_shift": "Rewards spirit investment over boon-stacking on support healers.",
   "rows": [
    {
     "label": "Scaling",
     "old": "Boons (6)",
     "new": "Spirit Power (1.1)",
     "text": null,
     "effect": "neutral",
     "ability": null
    }
   ]
  },
  {
   "item": "Metal Skin",
   "direction": "rework",
   "magnitude": "minor",
   "summary": "+20% gravity while active makes the defensive active worse for flyers and mobility heroes who pop it mid-air; a small tax on an already situational item.",
   "affected_heroes": [],
   "build_shift": "",
   "rows": [
    {
     "label": "Gravity",
     "old": null,
     "new": null,
     "text": "+20% while active",
     "effect": "bad",
     "ability": null
    }
   ]
  },
  {
   "item": "Infuser",
   "direction": "buff",
   "magnitude": "moderate",
   "summary": "More active lifesteal, spirit lifesteal and spirit power make Victor's sustain-bruiser slot stronger and push the item toward spirit builds generally.",
   "affected_heroes": [
    {
     "hero": "Victor",
     "relationship": "core",
     "effect": "up",
     "why": "Spirit sustain bruiser runs Infuser."
    }
   ],
   "build_shift": "",
   "rows": [
    {
     "label": "Active lifesteal",
     "old": "70%",
     "new": "75%",
     "text": null,
     "effect": "good",
     "ability": null
    },
    {
     "label": "Spirit lifesteal",
     "old": "13%",
     "new": "15%",
     "text": null,
     "effect": "good",
     "ability": null
    },
    {
     "label": "Spirit power",
     "old": "6",
     "new": "8",
     "text": null,
     "effect": "good",
     "ability": null
    }
   ]
  },
  {
   "item": "Juggernaut",
   "direction": "buff",
   "magnitude": "minor",
   "summary": "+8→+15 health regen nearly doubles the regen on the item; helps sustained frontline buyers but won't make it core.",
   "affected_heroes": [],
   "build_shift": "",
   "rows": [
    {
     "label": "Health regen",
     "old": "+8",
     "new": "+15",
     "text": null,
     "effect": "good",
     "ability": null
    }
   ]
  },
  {
   "item": "Leech",
   "direction": "buff",
   "magnitude": "minor",
   "summary": "+2% on both lifesteals is a small nudge; KB already had it losing to cheaper lifesteal, and this doesn't change that.",
   "affected_heroes": [],
   "build_shift": "",
   "rows": [
    {
     "label": "Bullet lifesteal",
     "old": "28%",
     "new": "30%",
     "text": null,
     "effect": "good",
     "ability": null
    },
    {
     "label": "Spirit lifesteal",
     "old": "28%",
     "new": "30%",
     "text": null,
     "effect": "good",
     "ability": null
    }
   ]
  },
  {
   "item": "Vampiric Burst",
   "direction": "buff",
   "magnitude": "moderate",
   "summary": "More active lifesteal, bullet lifesteal and weapon damage make the burst-steroid a stronger all-in tool for aggressive carries.",
   "affected_heroes": [],
   "build_shift": "",
   "rows": [
    {
     "label": "Active lifesteal",
     "old": "70%",
     "new": "75%",
     "text": null,
     "effect": "good",
     "ability": null
    },
    {
     "label": "Bullet lifesteal",
     "old": "13%",
     "new": "15%",
     "text": null,
     "effect": "good",
     "ability": null
    },
    {
     "label": "Weapon damage",
     "old": "6%",
     "new": "10%",
     "text": null,
     "effect": "good",
     "ability": null
    }
   ]
  },
  {
   "item": "Spellbreaker",
   "direction": "rework",
   "magnitude": "moderate",
   "summary": "The proc now keeps reducing follow-up spirit damage in the same stack (e.g. charged shot + Tankbuster), so it's a real answer to multi-hit spirit burst rather than a single-hit shield.",
   "affected_heroes": [],
   "build_shift": "",
   "rows": [
    {
     "label": "Proc",
     "old": null,
     "new": null,
     "text": "Reduces follow-up spirit damage in same stack",
     "effect": "good",
     "ability": null
    }
   ]
  },
  {
   "item": "Divine Barrier",
   "direction": "nerf",
   "magnitude": "minor",
   "summary": "45→55s cooldown cuts the uptime of the cleanse-shield; Rem's late-fight Divine Barrier (his best-WR item) loses a cast window per fight.",
   "affected_heroes": [
    {
     "hero": "Rem",
     "relationship": "core",
     "effect": "down",
     "why": "Divine Barrier is his best-WR late item; longer cooldown trims it."
    },
    {
     "hero": "Solomon",
     "relationship": "situational",
     "effect": "down",
     "why": "Listed buyer, though absent from high-rank usage."
    }
   ],
   "build_shift": "",
   "rows": [
    {
     "label": "Cooldown",
     "old": "45s",
     "new": "55s",
     "text": null,
     "effect": "bad",
     "ability": null
    }
   ]
  }
 ],
 "notable_item_stories": [
  "Anti-heal is the patch's clearest theme: Decay, Toxic Bullets and Crippling Headshot buffed and Healbane now stacking, while Radiant Regeneration and Healing Booster are gutted — sustain is attacked from both sides.",
  "Regen is out, lifesteal is in: Radiant Regeneration and Healing Booster nerfed while Bullet/Spirit Lifesteal, Leech, Infuser and Vampiric Burst all buffed, shifting sustain from regen stacking to in-fight lifesteal.",
  "Invisibility consolidates: Steam Vents lose invisibility and Shadow Weave is reworked into the sole invis-engage tool, restoring Warden's exclusivity even as the item's ambush pattern slows."
 ]
}

## Hero analysis (only heroes with direction != neutral)

[
 {
  "hero": "Infernus",
  "in_notes": true,
  "direction": "up",
  "magnitude": "moderate",
  "confidence": 0.62,
  "direct_reasons": [
   "Napalm T2 lifesteal 15%\u219220% directly feeds the Dashfernus sustain loop that already posts his better win rate.",
   "Concussive Combustion T3 now adds +0.4 spirit scaling, a real damage bump for the spirit build rather than a cosmetic talent."
  ],
  "indirect_reasons": [
   "Toxic Bullets anti-heal 35%\u219240% and Decay -50%\u2192-55% strengthen the anti-heal package he already buys, and the patch's anti-heal theme punishes the sustain fronts his burn out-ranges.",
   "Spirit Lifesteal 13%\u219215% and Bullet Lifesteal buffs land on his sustain slots exactly as regen items (Radiant Regeneration, Healing Booster) are gutted \u2014 his build is on the winning side of the sustain shift.",
   "Spiritual Overflow's +2 spirit is a token recovery; he dropped it post-09-16 and this does not restore it."
  ],
  "build_changes": [
   "Keep Toxic Bullets and Spirit Lifesteal as fixed slots \u2014 both were buffed this patch.",
   "Take Napalm T2 earlier in the Dashfernus line; the 20% lifesteal is now a genuine lane-sustain talent."
  ],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Burn carry quietly gained: anti-heal and lifesteal both moved his way.",
  "verdict": "keep",
  "rows": [
   {
    "label": "T2 lifesteal",
    "old": "15%",
    "new": "20%",
    "text": null,
    "effect": "good",
    "ability": "Napalm"
   },
   {
    "label": "T3",
    "old": null,
    "new": null,
    "text": "Adds +0.4 spirit scaling",
    "effect": "good",
    "ability": "Concussive Combustion"
   }
  ]
 },
 {
  "hero": "Seven",
  "in_notes": false,
  "direction": "up",
  "magnitude": "moderate",
  "confidence": 0.6,
  "direct_reasons": [],
  "indirect_reasons": [
   "Haunt bounty and growth +10% on the camps he clears fastest is the single largest income lever in the patch, and his AoE clear converts it better than anyone.",
   "Haunt HP and damage +10% is the offset \u2014 but Spirit Lifesteal 13%\u219215% and Decay -50%\u2192-55% both buff his exact core slots, so he absorbs the harder camps better than most clearers.",
   "The comeback package (non-hero gold 26%\u219230%, faster Haunted Souls when behind, tick souls to the two poorest) directly reverses the KB's 'a behind Seven cannot brawl back' cap \u2014 he now has a farm route from behind."
  ],
  "build_changes": [
   "Spirit Lifesteal is now a stronger second-item commitment against the tougher camps.",
   "Decay is a better slot into the sustain comps the anti-heal patch encourages."
  ],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Richer camps plus a real comeback route \u2014 the farm carry got both ends fixed.",
  "verdict": "keep",
  "rows": []
 },
 {
  "hero": "Vindicta",
  "in_notes": false,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.55,
  "direct_reasons": [],
  "indirect_reasons": [
   "High-Velocity Rounds base bullet velocity 60%\u219245% trims her opening max-range poke \u2014 the exact window her gun build buys it for.",
   "Move slow to air-drag ratio 0.35\u21920.5 taxes her harder whenever she is slowed mid-flight, compounding the existing flyer tax.",
   "Steam Vents losing invisibility removes a free-approach tool from the roamers that dive her, which partly offsets the above."
  ],
  "build_changes": [
   "Upgrade off base High-Velocity Rounds faster to recover velocity rather than sitting on the T2."
  ],
  "tier_before": "A",
  "tier_after": "B",
  "one_liner": "Slower bullets and heavier air drag on a 48.7% flyer \u2014 the A was already generous.",
  "verdict": "watch",
  "rows": []
 },
 {
  "hero": "Lady Geist",
  "in_notes": true,
  "direction": "down",
  "magnitude": "moderate",
  "confidence": 0.65,
  "direct_reasons": [
   "Essence Bomb spirit scaling 1.22\u21921.35 is a genuine buff to the Spirit Soul-Exchange variant's burst."
  ],
  "indirect_reasons": [
   "Radiant Regeneration is gutted \u2014 spirit-damage regen 0.35\u21920.25, heal-on-cast 65\u219240, boon scaling 1.7\u21921.4, and the heal now only fires in combat \u2014 on an item she buys in ~98% of games.",
   "Healing Booster loses its Extra Regen component and +3 flat regen, gutting the second leg of her regen shell.",
   "Decay -50%\u2192-55% and Healbane stacking help her anti-heal slot, but they cut against her own sustain identity as much as they help her kill other fronts."
  ],
  "build_changes": [
   "Shift sustain weight from Radiant Regeneration/Healing Booster toward Spirit Lifesteal (13%\u219215%) and Bullet Lifesteal.",
   "The Spirit Soul-Exchange variant now has the better damage line (Essence Bomb 1.35) but the weaker sustain line \u2014 commit to burst, not grind."
  ],
  "tier_before": "A",
  "tier_after": "B",
  "one_liner": "Her regen shell took its fourth and biggest hit; the bomb buff does not cover it.",
  "verdict": "watch",
  "rows": [
   {
    "label": "Spirit scaling",
    "old": "1.22",
    "new": "1.35",
    "text": null,
    "effect": "good",
    "ability": "Essence Bomb"
   }
  ]
 },
 {
  "hero": "Abrams",
  "in_notes": true,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.6,
  "direct_reasons": [
   "Base gun damage +5% and Siphon Life T3 +18\u2192+22 DPS both nudge his brawl damage without changing his role.",
   "The Shoulder Charge fix removes the extra hold he got from not hitting a wall \u2014 a small real loss to his engage."
  ],
  "indirect_reasons": [
   "Hunter's Aura now requires line of sight, removing the through-wall shred that made his melee-brawler core a stat-check in clumped fights \u2014 his single biggest item hit.",
   "Healing Snacks 10%\u219214% max HP and the new Heavy-Melee Cauldrons (Candy/Sugar Rush) reward exactly the frontline kit that already owns the crate route.",
   "Decay -50%\u2192-55% buffs his anti-heal answer to enemy fronts; Point Blank's slow 2s\u21922.5s is a small new stick option."
  ],
  "build_changes": [
   "Hunter's Aura is now a fight-only item \u2014 stop valuing it as a corridor/objective shred and consider a competing slot.",
   "Point Blank is a live option for holding targets in melee range."
  ],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Frontline economy and Cauldrons help; Hunter's Aura losing through-wall shred hurts.",
  "verdict": "keep",
  "rows": [
   {
    "label": "Base gun damage",
    "old": null,
    "new": null,
    "text": "+5%",
    "effect": "good",
    "ability": null
   },
   {
    "label": "T3",
    "old": "+18 DPS",
    "new": "+22 DPS",
    "text": null,
    "effect": "good",
    "ability": "Siphon Life"
   },
   {
    "label": "Shoulder Charge",
    "old": null,
    "new": null,
    "text": "No longer holds enemies in place",
    "effect": "bad",
    "ability": "Shoulder Charge"
   }
  ]
 },
 {
  "hero": "Wraith",
  "in_notes": true,
  "direction": "down",
  "magnitude": "moderate",
  "confidence": 0.62,
  "direct_reasons": [
   "Card Trick heal 60\u219245 cuts the self-sustain that keeps her alive through the dive she already loses to.",
   "Project Mind cooldown 46s\u219250s and initial cast time 0.75s\u21921s make her escape/rotate tool slower on both ends."
  ],
  "indirect_reasons": [
   "Spirit Lifesteal 13%\u219215% is a small lift to her situational sustain-gun variant, but it does not offset three direct nerfs.",
   "The patch's anti-heal theme (Decay, Toxic Bullets, Healbane stacking) further devalues the Card Trick heal she just lost."
  ],
  "build_changes": [
   "Lean harder into the pure-gun fire-rate line; the on-hit spirit package is already weakened and the heal is now worse."
  ],
  "tier_before": "B",
  "tier_after": "C",
  "one_liner": "Heal cut and a slower escape on a hero already sliding \u2014 the floor is thinner.",
  "verdict": "watch",
  "rows": [
   {
    "label": "Heal",
    "old": "60",
    "new": "45",
    "text": null,
    "effect": "bad",
    "ability": "Card Trick"
   },
   {
    "label": "Cooldown",
    "old": "46s",
    "new": "50s",
    "text": null,
    "effect": "bad",
    "ability": "Project Mind"
   },
   {
    "label": "Cast time",
    "old": "0.75s",
    "new": "1s",
    "text": null,
    "effect": "bad",
    "ability": "Project Mind"
   }
  ]
 },
 {
  "hero": "McGinnis",
  "in_notes": true,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.55,
  "direct_reasons": [
   "Mini Turret damage vs troopers 50%\u219265% speeds her lane push and camp-adjacent farm.",
   "Mini Turret health per boon 9\u219210 makes turret stacks survive dive and camp chip slightly longer."
  ],
  "indirect_reasons": [
   "Haunt bounty +10% rewards turrets clearing grouped camps from cover, though the +10% camp damage chips the turrets themselves.",
   "Breakables growth -10% trims the crate income her static setup does not contest anyway \u2014 a wash."
  ],
  "build_changes": [],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Turrets farm and push a bit better; still a low-pick niche controller.",
  "verdict": "keep",
  "rows": [
   {
    "label": "Turret vs troopers",
    "old": "50%",
    "new": "65%",
    "text": null,
    "effect": "good",
    "ability": "Mini Turret"
   },
   {
    "label": "Turret HP/boon",
    "old": "9",
    "new": "10",
    "text": null,
    "effect": "good",
    "ability": "Mini Turret"
   }
  ]
 },
 {
  "hero": "Haze",
  "in_notes": true,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.55,
  "direct_reasons": [
   "Smoke Bomb T3 no longer dispels undispellable debuffs \u2014 a small trim to her escape/cleanse window."
  ],
  "indirect_reasons": [
   "Return Fire now reflects Fixation damage, handing tanks a targeted counter-item into her stacking DoT.",
   "The patch's anti-heal and lifesteal shift does nothing for her weak T4 gun items, which the KB already flags as her scaling ceiling."
  ],
  "build_changes": [
   "Expect Return Fire on enemy fronts \u2014 do not rely on Fixation stacks alone to close kills into tanks."
  ],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "A counter-item now exists for Fixation; her ceiling is unchanged and still low.",
  "verdict": "watch",
  "rows": [
   {
    "label": "T3",
    "old": null,
    "new": null,
    "text": "No longer dispels undispellable debuffs",
    "effect": "neutral",
    "ability": "Smoke Bomb"
   }
  ]
 },
 {
  "hero": "Holliday",
  "in_notes": false,
  "direction": "down",
  "magnitude": "moderate",
  "confidence": 0.6,
  "direct_reasons": [],
  "indirect_reasons": [
   "Steam Vents reworked from invisibility to +150% stamina regen removes the free roam approach the KB credits for her pick routes.",
   "Tunnel move speed +70%\u2192+50% slows the rotations her lasso picks depend on.",
   "The comeback package lengthens games and softens lane leads \u2014 directly against a tempo assassin sitting at 46.3% WR."
  ],
  "build_changes": [
   "Lean on the stamina hybrid line (Sprint Boots, Extra Stamina, Recharging Rush) now that vents give stamina rather than stealth."
  ],
  "tier_before": "A",
  "tier_after": "B",
  "one_liner": "Her two roam tools \u2014 vent invis and fast tunnels \u2014 both got pulled back.",
  "verdict": "watch",
  "rows": []
 },
 {
  "hero": "Bebop",
  "in_notes": false,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [],
  "indirect_reasons": [
   "The comeback package (non-hero gold cap 26%\u219230%, Haunted Souls up to 50% faster when behind, tick souls to the two poorest) directly softens the early lead his hook is supposed to convert.",
   "Haunt bounty +10% pays camp clearers; Bebop has no AoE clear and no crate route, so his income gap widens against the farm heroes.",
   "Steam Vents now grant +150% stamina regen instead of invisibility \u2014 a hooked target still gets a disengage tool, so his core problem is unchanged.",
   "Echo Shard post-cast 0.5s\u21920.2s speeds his double-cast hook/bomb line, a small offset."
  ],
  "build_changes": [
   "Echo Shard is now a more attractive situational slot for the hook-bomb combo than it was."
  ],
  "tier_before": "B",
  "tier_after": "C",
  "one_liner": "Still hooks, still can't punish a farm meta that now forgives losing teams.",
  "verdict": "watch",
  "rows": []
 },
 {
  "hero": "Calico",
  "in_notes": false,
  "direction": "down",
  "magnitude": "moderate",
  "confidence": 0.6,
  "direct_reasons": [],
  "indirect_reasons": [
   "Steam Vents lose invisibility (now +150% stamina regen), removing the free roam approach the KB credits with extending her gank routes.",
   "Tunnel move speed +70%\u2192+50% slows the district-to-district rotations her kill-based income depends on.",
   "The comeback package (gold cap 26%\u219230%, faster Haunted Souls when behind) blunts the tempo snowball she converts kills into.",
   "Haunt bounty +10% is a real offset: camps are income she can take, unlike Tough Crates her cat form can't heavy-melee."
  ],
  "build_changes": [
   "Lean harder on Haunt camp income between ganks now that vent invisibility is gone."
  ],
  "tier_before": "A",
  "tier_after": "B",
  "one_liner": "Lost her free approach and her snowball; still dives squishies, just slower to get there.",
  "verdict": "watch",
  "rows": []
 },
 {
  "hero": "Mo & Krill",
  "in_notes": true,
  "direction": "down",
  "magnitude": "moderate",
  "confidence": 0.65,
  "direct_reasons": [
   "Spirit per boon 1.1\u21920.6 nearly halves his spirit scaling, the stat both his builds are built on.",
   "Spirit damage on all abilities reduced 10% (base and growth) compounds the boon cut.",
   "Bullet damage per boon +4% is a partial pivot toward gun, not a replacement for the spirit loss."
  ],
  "indirect_reasons": [
   "Torment Pulse melee resistance 18%\u219222% and Decay heal cut -50%\u2192-55% both buff his core bruiser slots.",
   "Tank/frontline archetype up (Healing Snacks 10%\u219214%, Heavy Melee Cauldrons) and richer-but-tougher Haunts reward his sustained frontline.",
   "Healbane rework keeps his anti-heal role but trims heal-on-kill 275\u2192170+3/boon, cutting his self-sustain."
  ],
  "build_changes": [
   "Shift value toward gun/utility (Quicksilver Reload, Trophy Collector) and away from spirit-stacking damage items.",
   "Torment Pulse and Decay are now stronger relative buys in the same slots."
  ],
  "tier_before": "A",
  "tier_after": "B",
  "one_liner": "Still the default front line, but his damage just got a lot smaller.",
  "verdict": "watch",
  "rows": [
   {
    "label": "Spirit per boon",
    "old": "1.1",
    "new": "0.6",
    "text": null,
    "effect": "bad",
    "ability": null
   },
   {
    "label": "Spirit damage",
    "old": null,
    "new": null,
    "text": "All abilities -10%",
    "effect": "bad",
    "ability": null
   },
   {
    "label": "Bullet per boon",
    "old": null,
    "new": null,
    "text": "+4%",
    "effect": "good",
    "ability": null
   }
  ]
 },
 {
  "hero": "Shiv",
  "in_notes": true,
  "direction": "down",
  "magnitude": "moderate",
  "confidence": 0.6,
  "direct_reasons": [
   "Alt fire damage per boon -5% trims his ranged poke.",
   "Serrated Knives rage damage 3.5%\u21924% current health plus T3 +0.01 spirit scaling strengthens his anti-tank identity.",
   "Killing Blow recast window 16s\u219212s shortens his execute follow-up."
  ],
  "indirect_reasons": [
   "Radiant Regeneration is gutted a fourth time (spirit-dmg regen 0.35\u21920.25, heal-on-cast 65\u219240, in-combat only) \u2014 it is in his near-universal regen core.",
   "The patch's anti-heal stack (Decay 55%, Toxic Bullets 40%, Healbane now stacking) attacks the regen shell he wins extended fights with.",
   "Torment Pulse melee resistance 18%\u219222% and Decay buff help his bruiser slots.",
   "Tank/frontline archetype up and richer Haunt camps reward his sustain brawling."
  ],
  "build_changes": [
   "Move sustain off Radiant Regeneration toward Spirit/Bullet Lifesteal and Leech, which were all buffed.",
   "Keep Torment Pulse and Decay; they gained while his regen layer lost."
  ],
  "tier_before": "A",
  "tier_after": "B",
  "one_liner": "Knives hit tanks harder, but the regen shell that kept him alive got gutted.",
  "verdict": "watch",
  "rows": [
   {
    "label": "Alt fire",
    "old": null,
    "new": null,
    "text": "Damage per boon -5%",
    "effect": "bad",
    "ability": null
   },
   {
    "label": "Rage damage",
    "old": "3.5% current HP",
    "new": "4% current HP",
    "text": null,
    "effect": "good",
    "ability": "Serrated Knives"
   },
   {
    "label": "T3",
    "old": null,
    "new": null,
    "text": "+0.01 rage spirit scaling",
    "effect": "good",
    "ability": "Serrated Knives"
   },
   {
    "label": "Recast window",
    "old": "16s",
    "new": "12s",
    "text": null,
    "effect": "bad",
    "ability": "Killing Blow"
   }
  ]
 },
 {
  "hero": "Ivy",
  "in_notes": false,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.55,
  "direct_reasons": [],
  "indirect_reasons": [
   "Healing Booster loses its Extra Regen component and +3 flat regen, gutting the cheap upgrade path her heal/anti-heal build sits on.",
   "Anti-heal is the patch's clearest theme (Decay 55%, Toxic Bullets 40%, Healbane stacking), which cuts directly into her tether healing.",
   "Healing Snacks 10%\u219214% max HP cheapens the dedicated healing she sells.",
   "Her actual primary gun core (Titanic Magazine, Tesla Bullets, Active Reload) is untouched, which caps the damage."
  ],
  "build_changes": [
   "Buy Healing Booster standalone rather than as an Extra Regen upgrade, or drop it for buffed lifesteal in the heal build."
  ],
  "tier_before": "A",
  "tier_after": "B",
  "one_liner": "Best peel in the game, but every heal item she bought got worse.",
  "verdict": "watch",
  "rows": []
 },
 {
  "hero": "Warden",
  "in_notes": true,
  "direction": "up",
  "magnitude": "moderate",
  "confidence": 0.6,
  "direct_reasons": [
   "Alchemical Flask travels 40% faster and its weapon-damage reduction rises -25%\u2192-30%, making his poke land and stick.",
   "Willpower speed bonus +15%\u2192+20% improves his walk-up to the silence cage.",
   "Last Stand T2 goes +40.5\u2192+50 DPS and -30s\u2192-40s cooldown, a real mid-game power spike."
  ],
  "indirect_reasons": [
   "Steam Vents lose invisibility, restoring Shadow Weave as the only invis-engage tool \u2014 the exclusivity the KB said he had lost.",
   "Shadow Weave's rework (+50% ambush weapon damage, applies to the breaking ability) suits his gun-carry ambush more than the old melee/fire-rate version.",
   "Tempo shift toward scaling plus the comeback package (gold cap 30%, faster Haunted Souls when behind) gives his late gun spike room to arrive.",
   "High-Velocity Rounds velocity 60%\u219245% trims his early poke; Spirit Lifesteal +2 spirit/+2% lifesteal helps his sustain slot."
  ],
  "build_changes": [
   "Shadow Weave is back to being a real core in the cage-bruiser line \u2014 but plan the 6s stealth buildup before engaging.",
   "Upgrade off base High-Velocity Rounds faster to offset the velocity cut."
  ],
  "tier_before": "C",
  "tier_after": "B",
  "one_liner": "Got his invis-engage back and a real Last Stand spike; still waits on a clock.",
  "verdict": "watch",
  "rows": [
   {
    "label": "Travel speed",
    "old": null,
    "new": null,
    "text": "40% faster",
    "effect": "good",
    "ability": "Alchemical Flask"
   },
   {
    "label": "Weapon dmg shred",
    "old": "-25%",
    "new": "-30%",
    "text": null,
    "effect": "good",
    "ability": "Alchemical Flask"
   },
   {
    "label": "Speed bonus",
    "old": "+15%",
    "new": "+20%",
    "text": null,
    "effect": "good",
    "ability": "Willpower"
   },
   {
    "label": "T2 DPS",
    "old": "+40.5",
    "new": "+50",
    "text": null,
    "effect": "good",
    "ability": "Last Stand"
   },
   {
    "label": "T2 cooldown",
    "old": "-30s",
    "new": "-40s",
    "text": null,
    "effect": "good",
    "ability": "Last Stand"
   }
  ]
 },
 {
  "hero": "Yamato",
  "in_notes": true,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.55,
  "direct_reasons": [
   "Flying Slash cast range 26m\u219223m and T3 +15m\u2192+8m shorten her engage and escape reach.",
   "Shadow Transformation cooldown 150s\u2192160s (moved to T2) delays her fight-winning window.",
   "Power Slash spirit scaling +6% is a small damage gain on her primary damage tool."
  ],
  "indirect_reasons": [
   "Hunter's Aura now requires line of sight, removing the through-wall shred her late spirit-burst build buys it for.",
   "Torment Pulse melee resistance 18%\u219222% buffs her late spirit build; Healbane rework is neutral for her.",
   "Haunt bounty +10% and tougher camps reward her punch AoE, still the fastest grouped-camp clear in the game.",
   "Mobile assassin archetype down (vents lose invisibility, tunnels +70%\u2192+50%) trims the roam tempo she lives on."
  ],
  "build_changes": [
   "Re-evaluate Hunter's Aura in the late spirit-burst line; it no longer shreds through walls in corridor fights."
  ],
  "tier_before": "A",
  "tier_after": "B",
  "one_liner": "Camp clear still elite, but her engage range and ult timer both got shorter.",
  "verdict": "watch",
  "rows": [
   {
    "label": "Spirit scaling",
    "old": null,
    "new": null,
    "text": "+6%",
    "effect": "good",
    "ability": "Power Slash"
   },
   {
    "label": "Cast range",
    "old": "26m",
    "new": "23m",
    "text": null,
    "effect": "bad",
    "ability": "Flying Slash"
   },
   {
    "label": "T3 range",
    "old": "+15m",
    "new": "+8m",
    "text": null,
    "effect": "bad",
    "ability": "Flying Slash"
   },
   {
    "label": "Cooldown",
    "old": "150s",
    "new": "160s",
    "text": null,
    "effect": "bad",
    "ability": "Shadow Transformation"
   }
  ]
 },
 {
  "hero": "Lash",
  "in_notes": true,
  "direction": "down",
  "magnitude": "moderate",
  "confidence": 0.6,
  "direct_reasons": [
   "Grapple T3 now also grants +4m jump velocity \u2014 a small mobility gain on his engage.",
   "Death Slam's cone-to-cylinder indicator is visual only."
  ],
  "indirect_reasons": [
   "Steam Vents lose invisibility (now +150% stamina regen), removing the free dive approach the KB credits with extending his routes.",
   "Tunnel move speed +70%\u2192+50% slows the rotations that set up Ground Strike.",
   "The comeback package (gold cap 26%\u219230%, faster Haunted Souls when behind, tick souls to the two poorest) blunts the early snowball an S-tier tempo initiator converts.",
   "Haunt bounty +10% pays camp clearers; Lash has no AoE farm route to take it."
  ],
  "build_changes": [],
  "tier_before": "S",
  "tier_after": "A",
  "one_liner": "Still the best dive in the game, but the map stopped handing him free entries.",
  "verdict": "watch",
  "rows": [
   {
    "label": "T3",
    "old": null,
    "new": null,
    "text": "Also +4m jump velocity",
    "effect": "good",
    "ability": "Grapple"
   },
   {
    "label": "Indicator",
    "old": null,
    "new": null,
    "text": "Cone to cylinder (visual)",
    "effect": "neutral",
    "ability": "Death Slam"
   }
  ]
 },
 {
  "hero": "Pocket",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [],
  "indirect_reasons": [
   "The comeback package (non-hero gold cap 26%\u219230%, Haunted Souls up to 50% faster when behind, tick souls to the two poorest) restores the bail-out his farm-and-scale line lost \u2014 the KB's stated reason he rarely spikes.",
   "Haunt bounty +10% rewards his Monster Rounds/Cultist Sacrifice farm route.",
   "Echo Shard post-cast 0.5s\u21920.2s speeds reset combos, though usage data shows it near-zero on him.",
   "Mobile assassin archetype down (vents lose invisibility) trims the roamers that dive him."
  ],
  "build_changes": [
   "Farming from behind is now a legitimate path back \u2014 don't concede the camp route when losing lane."
  ],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Finally has a comeback valve for the slow Affliction line.",
  "verdict": "watch",
  "rows": []
 },
 {
  "hero": "Sinclair",
  "in_notes": false,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.45,
  "direct_reasons": [],
  "indirect_reasons": [
   "High-Velocity Rounds bullet velocity 60%->45% hits the ~79% HVR/Opening Rounds lane opener that is his only real lane pressure.",
   "His dive counters got direct buffs: Drifter base gun damage +3% and Eternal Night T3 +2.75s, Calico Leaping Slash T3 +90 and Ava T3 8s.",
   "Lightning Scroll now scales 0.35 off spirit power, giving his duration/cooldown spirit shell a poke option it did not have."
  ],
  "build_changes": [
   "Delay the HVR lane opener or accept weaker max-range poke; consider Lightning Scroll as a spirit-scaling poke slot in the duration build."
  ],
  "tier_before": "C",
  "tier_after": "C",
  "one_liner": "HVR lane package nerfed and his dive counters buffed; still a coin-flip C.",
  "verdict": "watch",
  "rows": []
 },
 {
  "hero": "Drifter",
  "in_notes": true,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.55,
  "direct_reasons": [
   "Base gun damage +3% and Bloodscent T3 +11%->+12% amplified damage sharpen the melee-proc trade he already wins early.",
   "Eternal Night T3 +2.5s->+2.75s extends his ult window slightly."
  ],
  "indirect_reasons": [
   "Decay heal cut -50%->-55% strengthens his anti-heal bruiser variant, and Healbane now stacking makes team anti-heal a real lever.",
   "Healing Snacks 10%->14% max HP and the new Heavy-Melee Cauldrons reward his melee core and camp-chip sustain.",
   "Mo & Krill's spirit damage -10% softens one of his listed counters; Apollo's Riposte is now an immobilize rather than a stun, so it no longer fully locks his dive."
  ],
  "build_changes": [
   "Anti-heal bruiser variant gains: Decay is now a stronger slot into sustain comps."
  ],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Small gun/T3 buffs plus Decay and anti-heal stacking - still a blind-pick bruiser.",
  "verdict": "keep",
  "rows": [
   {
    "label": "Base gun damage",
    "old": null,
    "new": null,
    "text": "Increased by 3%",
    "effect": "good",
    "ability": null
   },
   {
    "label": "T3",
    "old": "+11% amplified",
    "new": "+12% amplified",
    "text": null,
    "effect": "good",
    "ability": "Bloodscent"
   },
   {
    "label": "T3",
    "old": "+2.5s duration",
    "new": "+2.75s duration",
    "text": null,
    "effect": "good",
    "ability": "Eternal Night"
   }
  ]
 },
 {
  "hero": "Venator",
  "in_notes": true,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [
   "Ira Domini blessed stake damage 115->95 but boon scaling 3->3.6: a weaker early stake that overtakes the old value later, so his lane poke is trimmed and his mid-game is not.",
   "Battle Vest weapon damage 18%->22% and Bullet Lifesteal 6%->10% weapon damage / 13%->15% lifesteal both buff his gun-bruiser primary shell."
  ],
  "indirect_reasons": [
   "Graves - his hard counter whose gun deletes his traps - took move speed 7->6.7, bullet damage per boon -4% and a slower Grasping Hands deploy.",
   "High-Velocity Rounds 60%->45% does not touch him (he opens Restorative Shot/Close Quarters/Monster Rounds), while it does hit Vindicta, another listed counter.",
   "Warden (flask, Willpower, Last Stand T2) and Abrams (base gun damage +5%, Siphon T3 +22) both got stronger, and both are losing lanes for him."
  ],
  "build_changes": [
   "Lean harder into Battle Vest + Bullet Lifesteal as the lane-sustain spine; treat Ira Domini as a mid-game spike rather than an early bully tool."
  ],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Battle Vest and Bullet Lifesteal buffs offset a weaker early stake; Graves nerf helps.",
  "verdict": "keep",
  "rows": [
   {
    "label": "Stake damage",
    "old": "115",
    "new": "95",
    "text": null,
    "effect": "bad",
    "ability": "Ira Domini"
   },
   {
    "label": "Stake boon scaling",
    "old": "3",
    "new": "3.6",
    "text": null,
    "effect": "good",
    "ability": "Ira Domini"
   }
  ]
 },
 {
  "hero": "Victor",
  "in_notes": true,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.55,
  "direct_reasons": [
   "Aura of Suffering T3 +15%->+16% damage is a token bump on his grind-down frontline."
  ],
  "indirect_reasons": [
   "Three of his core sustain items were buffed: Spirit Lifesteal 6->8 spirit / 13%->15%, Infuser 70%->75% active lifesteal and 6->8 spirit, Torment Pulse 18%->22% melee resist.",
   "Healing Booster lost its Extra Regen component and flat +3 regen, which is a real hit to his sustain stack - the buffs above roughly cancel it.",
   "Harder Haunt camps (bounty and HP both +10%) and Healing Snacks 10%->14% both reward his camp-grinding sustain line; Ivy, his worst lane, lost the same healing items."
  ],
  "build_changes": [
   "Shift sustain weight from Healing Booster to Spirit Lifesteal/Infuser; keep Torment Pulse as the frontline layer."
  ],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Spirit Lifesteal/Infuser/Torment Pulse buffs beat the Healing Booster trim - still A.",
  "verdict": "keep",
  "rows": [
   {
    "label": "T3",
    "old": "+15% damage",
    "new": "+16% damage",
    "text": null,
    "effect": "good",
    "ability": "Aura of Suffering"
   }
  ]
 },
 {
  "hero": "Paige",
  "in_notes": true,
  "direction": "down",
  "magnitude": "moderate",
  "confidence": 0.6,
  "direct_reasons": [
   "Base bullet damage 35->32 is a ~9% cut to the level-1 lane pressure that is her entire identity; the growth buff 0.52->0.61 only breaks even around boon 33, so she is weaker at every realistic point.",
   "Bookwyrm T2 trail duration +2s->+1s trims her zone control."
  ],
  "indirect_reasons": [
   "High-Velocity Rounds bullet velocity 60%->45% hits her 1.2-minute lane opener directly.",
   "The comeback package (non-hero gold cap 26%->30%, Haunted Souls up to 50% faster when behind, tick souls to the two poorest) directly attacks the lane-win-then-snowball conversion that made her S.",
   "Breakables growth -10% trims the lane-adjacent crate routes she converts lane pressure into; Healing Snacks 10%->14% partly offsets by letting her lane pressure stick."
  ],
  "build_changes": [
   "Do not sit on base HVR for max-range poke; upgrade it faster or open Opening Rounds first. Expect to win lane by less and convert through crate routes rather than a kill snowball."
  ],
  "tier_before": "S",
  "tier_after": "A",
  "one_liner": "Lane damage cut and comeback souls restored - her snowball converts less.",
  "verdict": "watch",
  "rows": [
   {
    "label": "Base bullet damage",
    "old": "35",
    "new": "32",
    "text": null,
    "effect": "bad",
    "ability": null
   },
   {
    "label": "Bullet damage growth",
    "old": "0.52",
    "new": "0.61",
    "text": null,
    "effect": "good",
    "ability": null
   },
   {
    "label": "T2",
    "old": "+2s trail duration",
    "new": "+1s trail duration",
    "text": null,
    "effect": "bad",
    "ability": "Bookwyrm"
   }
  ]
 },
 {
  "hero": "The Doorman",
  "in_notes": true,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.45,
  "direct_reasons": [
   "Luggage Cart T2 wall-impact damage +75->+90 and T3 cooldown -15s->-18s are both straight buffs to his setup tool."
  ],
  "indirect_reasons": [
   "The comeback package helps a 45.4% WR hero that loses to tempo rather than to numbers.",
   "His listed counters Yamato (Power Slash spirit scaling +6%) and Lash (Grapple T3 +4m jump velocity) both got small buffs, so the dive that beats his setup did not get slower."
  ],
  "build_changes": [],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Luggage Cart buffs are real but small; still a setup initiator in a tempo meta.",
  "verdict": "watch",
  "rows": [
   {
    "label": "T2",
    "old": "+75 wall impact",
    "new": "+90 wall impact",
    "text": null,
    "effect": "good",
    "ability": "Luggage Cart"
   },
   {
    "label": "T3",
    "old": "-15s cooldown",
    "new": "-18s cooldown",
    "text": null,
    "effect": "good",
    "ability": "Luggage Cart"
   }
  ]
 },
 {
  "hero": "Billy",
  "in_notes": true,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [
   "Rising Ram T3 +10% max health for 16s -> +15% for 20s is a real frontline durability buff on his engage.",
   "Blasted cooldown 27s->25s gives slightly more uptime on his all-in."
  ],
  "indirect_reasons": [
   "Spirit Shielding 18%->15% spirit resist trims his spirit shred/slow variant's defensive layer.",
   "Decay -50%->-55% heal cut strengthens his anti-heal frontline role in a patch that pushes anti-heal hard.",
   "His worst lane Shiv is roughly flat (Serrated Knives rage 3.5%->4% current HP up, alt-fire per boon -5% and Killing Blow recast 16s->12s down), while Warden and Seven both got small buffs against him."
  ],
  "build_changes": [],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Rising Ram T3 and Blasted buffs, but Warden and Shiv still out-sustain him.",
  "verdict": "keep",
  "rows": [
   {
    "label": "T3",
    "old": "+10% max HP / 16s",
    "new": "+15% max HP / 20s",
    "text": null,
    "effect": "good",
    "ability": "Rising Ram"
   },
   {
    "label": "Cooldown",
    "old": "27s",
    "new": "25s",
    "text": null,
    "effect": "good",
    "ability": "Blasted"
   }
  ]
 },
 {
  "hero": "Graves",
  "in_notes": true,
  "direction": "down",
  "magnitude": "moderate",
  "confidence": 0.6,
  "direct_reasons": [
   "Move speed 7->6.7 and bullet damage per boon -4% cut both her kiting and her damage on a hero with the worst early game of any carry.",
   "Grasping Hands deploy 0.6s->0.8s and now more easily double-jumped over removes a chunk of the zoning that keeps divers off her.",
   "Borrowed Decree T2 loses -0.3s spawn time and T3 gains it - a straight delay to her summon tempo."
  ],
  "indirect_reasons": [
   "Echo Shard post-cast 0.5s->0.2s buffs her summoner/cooldown primary build's double-cast execution.",
   "The comeback package (gold cap 26%->30%, faster Haunted Souls when behind, tick souls to the two poorest) is the bail-out her ~25-minute window never had.",
   "Her counters split: Warden buffed (flask, Willpower, Last Stand T2) and Calico buffed (Leaping Slash T3 +90, Ava T3 8s), but Wraith nerfed (Card Trick heal 60->45, Project Mind 46s->50s)."
  ],
  "build_changes": [
   "Echo Shard is now a faster, more reliable core in the summoner build; lean on it rather than on Grasping Hands zoning for safety."
  ],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Top win rate ate a broad nerf; Echo Shard buff and comeback souls soften it.",
  "verdict": "watch",
  "rows": [
   {
    "label": "Move speed",
    "old": "7",
    "new": "6.7",
    "text": null,
    "effect": "bad",
    "ability": null
   },
   {
    "label": "Bullet damage per boon",
    "old": null,
    "new": null,
    "text": "Reduced by 4%",
    "effect": "bad",
    "ability": null
   },
   {
    "label": "Deploy time",
    "old": "0.6s",
    "new": "0.8s",
    "text": null,
    "effect": "bad",
    "ability": "Grasping Hands"
   },
   {
    "label": "Counterplay",
    "old": null,
    "new": null,
    "text": "Easier to double jump over",
    "effect": "bad",
    "ability": "Grasping Hands"
   },
   {
    "label": "T2/T3",
    "old": null,
    "new": null,
    "text": "Spawn time cut moved T2->T3",
    "effect": "neutral",
    "ability": "Borrowed Decree"
   }
  ]
 },
 {
  "hero": "Apollo",
  "in_notes": true,
  "direction": "up",
  "magnitude": "moderate",
  "confidence": 0.6,
  "direct_reasons": [
   "Riposte Pommel Hit disable 0.8s->1.5s (T2 +0.4s->+0.6s) nearly doubles his lockdown window, even though it is now an immobilize plus parry disable rather than a stun.",
   "Riposte dash fixes stop the counterattack whiffing on moving, cornered or displaced targets - reliability he did not have.",
   "Flawless Advance now refunds the stab and keeps remaining recasts when stunned or slept, and Itani Lo Sahn is no longer interrupted by Sleep - two hard removals of his worst punish windows."
  ],
  "indirect_reasons": [
   "Healing Booster losing its Extra Regen component and flat +3 regen thins the sustain shell his spirit bruiser build leans on.",
   "Healbane now stacking is a team anti-heal gain but its heal-on-kill 275->170+3/boon is a personal sustain loss - roughly neutral for him.",
   "His losing lanes split: Warden and Abrams both buffed, but Wraith (Card Trick heal, Project Mind cooldown) and Mo & Krill (spirit damage -10%) both nerfed."
  ],
  "build_changes": [
   "Re-weight sustain toward Restorative Locket/Dispel Magic rather than Healing Booster; the longer Riposte disable makes pick-oriented spirit burst better than the old tank-and-outlast line."
  ],
  "tier_before": "S",
  "tier_after": "S",
  "one_liner": "Riposte is now a 1.5s immobilize and Flawless Advance refunds on CC - big pick buff.",
  "verdict": "keep",
  "rows": [
   {
    "label": "Pommel Hit",
    "old": null,
    "new": null,
    "text": "Stun -> immobilize + parry disable",
    "effect": "neutral",
    "ability": "Riposte"
   },
   {
    "label": "Disable duration",
    "old": "0.8s",
    "new": "1.5s",
    "text": null,
    "effect": "good",
    "ability": "Riposte"
   },
   {
    "label": "T2",
    "old": "+0.4s disable",
    "new": "+0.6s disable",
    "text": null,
    "effect": "good",
    "ability": "Riposte"
   },
   {
    "label": "Dash reliability",
    "old": null,
    "new": null,
    "text": "No longer misses moving/displaced targets",
    "effect": "good",
    "ability": "Riposte"
   },
   {
    "label": "CC refund",
    "old": null,
    "new": null,
    "text": "Stun/sleep refunds the stab",
    "effect": "good",
    "ability": "Flawless Advance"
   },
   {
    "label": "Sleep",
    "old": null,
    "new": null,
    "text": "No longer interrupted by Sleep",
    "effect": "good",
    "ability": "Itani Lo Sahn"
   }
  ]
 },
 {
  "hero": "Rem",
  "in_notes": false,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [],
  "indirect_reasons": [
   "Healing Booster no longer builds from Extra Regen and loses its flat +3 regen - the backbone of his sustain layer is gone.",
   "Divine Barrier cooldown 45s->55s cuts a cast window per fight off his best-WR late item.",
   "Decay -50%->-55% heal cut is a small gain on his anti-heal slot, and the comeback package helps a 45.1% WR hero; his worst lane Ivy lost the same healing items."
  ],
  "build_changes": [
   "Stop treating Healing Booster as a cheap Extra Regen upgrade; buy it standalone or route the slot into Spirit Lifesteal, which was buffed."
  ],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Healing Booster and Divine Barrier both trimmed; his sustain shell is thinner.",
  "verdict": "watch",
  "rows": []
 },
 {
  "hero": "Celeste",
  "in_notes": true,
  "direction": "down",
  "magnitude": "major",
  "confidence": 0.65,
  "direct_reasons": [
   "Shining Wonder damage 140\u2192125 is a straight cut to a kit already leaning on burst windows.",
   "Torment Pulse's melee resist 18%\u219222% is the only direct-ish help, and it does not touch her problem."
  ],
  "indirect_reasons": [
   "Radiant Regeneration's fourth and biggest trim (spirit regen scaling 0.35\u21920.25, heal-on-cast 65\u219240, boon scaling 1.7\u21921.4, in-combat only) guts her core sustain shell.",
   "Healing Booster loses Extra Regen and +3 flat regen \u2014 the second leg of that same regen stack.",
   "Spirit Shielding 18%\u219215% and HVR bullet velocity 60%\u219245% trim her defensive and early poke items.",
   "Anti-heal buffs (Decay -50\u2192-55%, Toxic Bullets 35\u219240%, Healbane stacking) land squarely on a regen-stacking flyer, and Metal Skin's +20% gravity punishes a flyer popping it mid-air."
  ],
  "build_changes": [
   "Abandon the Radiant Regeneration + Healing Booster stack; pivot to the buffed Spirit Lifesteal (+2 spirit, +2% lifesteal) and Torment Pulse for in-fight sustain.",
   "Witchmail (her highest-WR item) becomes more central now that slow/CC comps are stronger."
  ],
  "tier_before": "B",
  "tier_after": "C",
  "one_liner": "Both of her regen items got gutted and anti-heal is everywhere \u2014 the sustain-burst shell is gone.",
  "verdict": "bench",
  "rows": [
   {
    "label": "Damage",
    "old": "140",
    "new": "125",
    "text": null,
    "effect": "bad",
    "ability": "Shining Wonder"
   }
  ]
 },
 {
  "hero": "Rat King",
  "in_notes": true,
  "direction": "down",
  "magnitude": "major",
  "confidence": 0.75,
  "direct_reasons": [
   "Base bullet damage -5% and bullet damage growth -20% cut the gun-bruiser economy he farms with.",
   "Scrap Grenade loses damage (70\u219260, T2 +70\u2192+60, T3 300\u2192275) and radius (8m\u21926m, large explosion 14m\u219210m) \u2014 the camp-clear and teamfight AoE both shrink.",
   "Rule, Ratannia! loses half its knockup, 20s cooldown (160\u2192180), radius (20m\u219216m, T2 +8\u2192+6m) and duration (12s\u21929s), and now goes on cooldown if he is stunned/slept before placing.",
   "Fuse timers +0.1s give targets an extra beat to step out; only the new 0.4s minimum melee-fuse helps him."
  ],
  "indirect_reasons": [
   "Haunt camps gained +10% HP and damage while his Scrap Grenade radius shrank \u2014 the AoE-clear income advantage he was rated S for is materially slower.",
   "Richer-but-tougher Haunts plus the comeback package (gold cap 26%\u219230%, faster Haunted Souls when behind) soften the lead he converts from crate/camp tempo.",
   "Offset: Heavy Melee Cauldrons hand his 116-heavy-melee frontline a new pickup, and Healing Snacks 10%\u219214% keeps his brawl sustain ticking."
  ],
  "build_changes": [
   "Stop counting Scrap Grenade as a one-button camp clear; pull camps with melee first, then drop grenade on clumped mobs.",
   "Superior/Compress Cooldown become mandatory again to cover the 180s banner cooldown."
  ],
  "tier_before": "S",
  "tier_after": "A",
  "one_liner": "Grenade radius and the banner ult both got hit hard \u2014 still a frontline, no longer an auto-win.",
  "verdict": "watch",
  "rows": [
   {
    "label": "Base bullet damage",
    "old": null,
    "new": null,
    "text": "-5%",
    "effect": "bad",
    "ability": null
   },
   {
    "label": "Bullet dmg growth",
    "old": null,
    "new": null,
    "text": "-20%",
    "effect": "bad",
    "ability": null
   },
   {
    "label": "Damage",
    "old": "70",
    "new": "60",
    "text": null,
    "effect": "bad",
    "ability": "Scrap Grenade"
   },
   {
    "label": "T2 damage",
    "old": "+70",
    "new": "+60",
    "text": null,
    "effect": "bad",
    "ability": "Scrap Grenade"
   },
   {
    "label": "T3 damage",
    "old": "300",
    "new": "275",
    "text": null,
    "effect": "bad",
    "ability": "Scrap Grenade"
   },
   {
    "label": "Radius",
    "old": "8m",
    "new": "6m",
    "text": null,
    "effect": "bad",
    "ability": "Scrap Grenade"
   },
   {
    "label": "Large explosion",
    "old": "14m",
    "new": "10m",
    "text": null,
    "effect": "bad",
    "ability": "Scrap Grenade"
   },
   {
    "label": "Fuse timers",
    "old": "0.8s/0.7s",
    "new": "0.9s/0.8s",
    "text": null,
    "effect": "bad",
    "ability": "Scrap Grenade"
   },
   {
    "label": "Melee fuse",
    "old": null,
    "new": null,
    "text": "At least 0.4s before it explodes",
    "effect": "neutral",
    "ability": "Scrap Grenade"
   },
   {
    "label": "Knockup",
    "old": null,
    "new": null,
    "text": "Reduced by 50%",
    "effect": "bad",
    "ability": "Rule, Ratannia!"
   },
   {
    "label": "Cooldown",
    "old": "160s",
    "new": "180s",
    "text": null,
    "effect": "bad",
    "ability": "Rule, Ratannia!"
   },
   {
    "label": "Radius",
    "old": "20m",
    "new": "16m",
    "text": null,
    "effect": "bad",
    "ability": "Rule, Ratannia!"
   },
   {
    "label": "T2 radius",
    "old": "+8m",
    "new": "+6m",
    "text": null,
    "effect": "bad",
    "ability": "Rule, Ratannia!"
   },
   {
    "label": "Duration",
    "old": "12s",
    "new": "9s",
    "text": null,
    "effect": "bad",
    "ability": "Rule, Ratannia!"
   },
   {
    "label": "Interrupt",
    "old": null,
    "new": null,
    "text": "Goes on CD if stunned pre-place",
    "effect": "bad",
    "ability": "Rule, Ratannia!"
   }
  ]
 },
 {
  "hero": "Baba",
  "in_notes": true,
  "direction": "down",
  "magnitude": "major",
  "confidence": 0.65,
  "direct_reasons": [
   "Baba's Brew has no initial brew time but the order is now random each cast and the cycle went 1s\u21921.5s \u2014 she can no longer guarantee the silence/barrier she needs on demand, and silence dropped 3s\u21922.75s.",
   "Spirit Resist scaling 0.1\u21920.07 plus Threadsap's spirit-steal duration 22s\u219216s (and cleanse now wipes the stolen spirit too) cut her durability and her signature steal.",
   "Granny Long Legs heavy-melee slow 4s\u21922s and light-melee knockback 10m\u21928m trim her melee control; the 1.4s\u21921.2s heavy-melee cooldown is the only real gain.",
   "Her Granny stomp now only hits the closest Rejuvenator, so she cannot sweep the new three-crystal Mid-Boss spread."
  ],
  "indirect_reasons": [
   "Radiant Regeneration (94% buy) lost spirit-regeneration scaling 0.35\u21920.25, heal-on-cast 65\u219240 and in-fight availability \u2014 her regen wall is her identity.",
   "Healing Booster lost Extra Regen and its +3 flat regen; Torment Pulse 18%\u219222% melee resist is nowhere near enough to offset.",
   "Anti-heal is the patch's clearest item theme (Decay -55%, Healbane stacking, Toxic Bullets 40%) and it is aimed at exactly her archetype.",
   "Offset: Heavy-Melee Cauldrons and Healing Snacks 10%\u219214% both suit her, and tougher Haunt camps reward her sustain clear."
  ],
  "build_changes": [
   "Leave the regen bruiser shell \u2014 Radiant Regeneration and Healing Booster are both gutted; move to the cooldown-caster line (Superior Cooldown/Duration Extender) and buy Spirit Resilience earlier.",
   "Since brew order is random, hold casting until the right brew cycles in rather than opening fights blind."
  ],
  "tier_before": "C",
  "tier_after": "D",
  "one_liner": "Random brew order plus two gutted regen items is her whole gameplan taken away.",
  "verdict": "bench",
  "rows": [
   {
    "label": "Spirit Resist scaling",
    "old": "0.1",
    "new": "0.07",
    "text": null,
    "effect": "bad",
    "ability": null
   },
   {
    "label": "Spirit steal",
    "old": "22s",
    "new": "16s",
    "text": null,
    "effect": "bad",
    "ability": "Threadsap"
   },
   {
    "label": "Cleanse",
    "old": null,
    "new": null,
    "text": "Cleanse also removes her stolen spirit",
    "effect": "bad",
    "ability": "Threadsap"
   },
   {
    "label": "Light melee knockback",
    "old": "10m",
    "new": "8m",
    "text": null,
    "effect": "bad",
    "ability": "Granny Long Legs"
   },
   {
    "label": "Heavy melee cooldown",
    "old": "1.4s",
    "new": "1.2s",
    "text": null,
    "effect": "good",
    "ability": "Granny Long Legs"
   },
   {
    "label": "Heavy melee slow",
    "old": "4s",
    "new": "2s",
    "text": null,
    "effect": "bad",
    "ability": "Granny Long Legs"
   },
   {
    "label": "Rejuv stomp",
    "old": null,
    "new": null,
    "text": "Only hits the closest Rejuvenator",
    "effect": "bad",
    "ability": "Granny Long Legs"
   },
   {
    "label": "Initial brew time",
    "old": null,
    "new": null,
    "text": "Removed",
    "effect": "good",
    "ability": "Baba's Brew"
   },
   {
    "label": "Brew order",
    "old": null,
    "new": null,
    "text": "Random each cast",
    "effect": "bad",
    "ability": "Baba's Brew"
   },
   {
    "label": "Cycle time",
    "old": "1s",
    "new": "1.5s",
    "text": null,
    "effect": "bad",
    "ability": "Baba's Brew"
   },
   {
    "label": "Silence",
    "old": "3s",
    "new": "2.75s",
    "text": null,
    "effect": "bad",
    "ability": "Baba's Brew"
   }
  ]
 },
 {
  "hero": "Deadman Danny",
  "in_notes": true,
  "direction": "down",
  "magnitude": "moderate",
  "confidence": 0.6,
  "direct_reasons": [
   "Chimera Mk1 dominates every change: jetpack unusable while cursed, cooldown reduction per boon -0.4s\u2192-0.25s, and T3 refund on hit 50%\u219230% all cut his uptime.",
   "Slows now cut the jetpack's in-air impulse more effectively \u2014 and even harder when movement abilities are silenced \u2014 which is the exact escape a dive-pick flyer needs.",
   "Grounding pulls now work more reliably against him, so the Silver/Bola-and-slow layer lands consistently.",
   "The Close The Deal damage bug fix (held through the ability) is the only real gain."
  ],
  "indirect_reasons": [
   "High-Velocity Rounds 60%\u219245% bullet velocity hits his lone weapon staple in the early poke window.",
   "Steam Vents lose invisibility, removing the free approach angle his pick play used; Shadow Weave is now the only invis-engage tool.",
   "The global slow-to-air-drag ratio 0.35\u21920.5 taxes him every time he is slowed mid-flight.",
   "Anti-heal stacking (Decay -55%, Toxic Bullets 40%) and tougher Haunt camps (+10% HP) punish a 730-HP diver who commits to clear."
  ],
  "build_changes": [
   "Stop treating jetpack as the disengage \u2014 slows now bite it directly; lean Reactive Barrier/Grit and only fly in when the slow is on cooldown.",
   "Express Shot value drops with the 5% secondary-fire trim; the HVR velocity cut pushes upgrades earlier."
  ],
  "tier_before": "C",
  "tier_after": "C",
  "one_liner": "Slows now eat his jetpack and Steam Vents lost invisibility \u2014 his escape got taxed twice.",
  "verdict": "watch",
  "rows": [
   {
    "label": "Cursed",
    "old": null,
    "new": null,
    "text": "Jetpack unusable while cursed",
    "effect": "bad",
    "ability": "Chimera Mk1"
   },
   {
    "label": "CDR per boon",
    "old": "-0.4s",
    "new": "-0.25s",
    "text": null,
    "effect": "bad",
    "ability": "Chimera Mk1"
   },
   {
    "label": "T3 refund",
    "old": "50%",
    "new": "30%",
    "text": null,
    "effect": "bad",
    "ability": "Chimera Mk1"
   },
   {
    "label": "Slows",
    "old": null,
    "new": null,
    "text": "Slows cut jetpack impulse more",
    "effect": "bad",
    "ability": "Chimera Mk1"
   },
   {
    "label": "Grounding",
    "old": null,
    "new": null,
    "text": "Pulls to ground land more reliably",
    "effect": "bad",
    "ability": "Chimera Mk1"
   },
   {
    "label": "Close The Deal",
    "old": null,
    "new": null,
    "text": "Damage now works when held",
    "effect": "good",
    "ability": "Close The Deal"
   }
  ]
 },
 {
  "hero": "Violet",
  "in_notes": true,
  "direction": "down",
  "magnitude": "moderate",
  "confidence": 0.55,
  "direct_reasons": [
   "Abstract Landscape is nerfed across the board: 165s\u2192180s cooldown, 6s\u21925s duration, spirit scaling 0.04\u21920.01, ends early if she dies, 0.5s\u21920.75s re-apply cooldown, and T3 no longer keeps ink alive.",
   "Still Life loses reliability: stun 1.0s\u21920.9s, line of sight required at channel end even in the grace period, T1 regen only while drawing and scaling 0.25\u21920.15.",
   "T3 stun +0.35s\u2192+0.45s and the sketch-buff reshuffle are the only ups."
  ],
  "indirect_reasons": [
   "Spirit Lifesteal 6\u21928 spirit power and 13%\u219215% lifesteal is a real buff to her primary spirit-caster shell.",
   "Anti-heal stacking (Decay -55%, Healbane stacks, Toxic Bullets 40%) directly undercuts Still Life's regen talents and any Healing Booster she buys.",
   "The dive archetype that deletes her is down (Steam Vents lose invisibility, tunnel speed +70%\u2192+50%), which partially offsets; Holliday/Vindicta are untouched."
  ],
  "build_changes": [
   "Stop leaning on Still Life T1 regen as lane sustain \u2014 it only ticks while drawing now; put the points elsewhere.",
   "Keep Superior Cooldown + Escalating Exposure (untouched); add buffed Spirit Lifesteal for the sustain the regen talents lost."
  ],
  "tier_before": "B",
  "tier_after": "C",
  "one_liner": "Her ult got cut on every axis at once \u2014 the zone is still good, the cooldown is not.",
  "verdict": "watch",
  "rows": [
   {
    "label": "Stun duration",
    "old": "1.0s",
    "new": "0.9s",
    "text": null,
    "effect": "bad",
    "ability": "Still Life"
   },
   {
    "label": "Line of sight",
    "old": null,
    "new": null,
    "text": "Required at channel end",
    "effect": "bad",
    "ability": "Still Life"
   },
   {
    "label": "T1 regen",
    "old": null,
    "new": null,
    "text": "Only while drawing",
    "effect": "bad",
    "ability": "Still Life"
   },
   {
    "label": "T1 regen scaling",
    "old": "0.25",
    "new": "0.15",
    "text": null,
    "effect": "bad",
    "ability": "Still Life"
   },
   {
    "label": "T3 stun",
    "old": "+0.35s",
    "new": "+0.45s",
    "text": null,
    "effect": "good",
    "ability": "Still Life"
   },
   {
    "label": "Cooldown",
    "old": "165s",
    "new": "180s",
    "text": null,
    "effect": "bad",
    "ability": "Abstract Landscape"
   },
   {
    "label": "Duration",
    "old": "6s",
    "new": "5s",
    "text": null,
    "effect": "bad",
    "ability": "Abstract Landscape"
   },
   {
    "label": "Duration scaling",
    "old": "0.04",
    "new": "0.01",
    "text": null,
    "effect": "bad",
    "ability": "Abstract Landscape"
   },
   {
    "label": "On death",
    "old": null,
    "new": null,
    "text": "Ends early if Violet dies",
    "effect": "bad",
    "ability": "Abstract Landscape"
   },
   {
    "label": "Re-apply cooldown",
    "old": "0.5s",
    "new": "0.75s",
    "text": null,
    "effect": "bad",
    "ability": "Abstract Landscape"
   },
   {
    "label": "T3",
    "old": null,
    "new": null,
    "text": "No longer keeps ink alive",
    "effect": "bad",
    "ability": "Abstract Landscape"
   }
  ]
 },
 {
  "hero": "Nurse Harrow",
  "in_notes": true,
  "direction": "down",
  "magnitude": "moderate",
  "confidence": 0.4,
  "direct_reasons": [
   "Lurking Terrors is gutted: fear buildup 1.3s\u21922s, duration 7s\u21925s, T3 duration +3s\u2192+2s, T3 immunity \u2192 50% damage reduction while channelling, and no fear builds when she is more than 50 degrees above or below the target's view.",
   "Base gun damage -10% and Healing Needles heal-per-shot 25\u219222 (T2 +20\u2192+16) cut her throughput; only the spirit scaling 0.2\u21920.24 and Wretched Vapors T3 +15%\u2192+20% rush speed go up.",
   "Leech Therapy fed-leech ground duration drops from a flat 180s to 120s + 3s/min and leeches clear on round reset, trimming her pre-placed map presence."
  ],
  "indirect_reasons": [
   "Anti-heal is the patch's headline: Decay -50%\u2192-55%, Toxic Bullets 35%\u219240%, Crippling Headshot -35%\u2192-40% and Healbane now stacking \u2014 every one of them cuts a dedicated healer's output.",
   "Healing Snacks 10%\u219214% max HP and the tank/frontline archetype rising cheapen the dedicated healing she sells.",
   "Violet's Still Life sketches now grant +2% healing amp specifically from her (and Kelvin/Ivy/Dynamo/Paige/Rem), a small team-side nudge."
  ],
  "build_changes": [
   "Lean on the Healing Needles spirit scaling (0.2\u21920.24) rather than stacking flat heal-per-shot, which just got trimmed twice.",
   "Treat Lurking Terrors as a 5s lockdown, not a 7s one \u2014 do not channel it from odd vertical angles, fear no longer builds there."
  ],
  "tier_before": "?",
  "tier_after": "B",
  "one_liner": "Her ult lost duration, immunity and buildup speed in a patch where anti-heal is everywhere.",
  "verdict": "watch",
  "rows": [
   {
    "label": "Base gun damage",
    "old": null,
    "new": null,
    "text": "-10%",
    "effect": "bad",
    "ability": null
   },
   {
    "label": "Heal per shot",
    "old": "25",
    "new": "22",
    "text": null,
    "effect": "bad",
    "ability": "Healing Needles"
   },
   {
    "label": "T2 heal",
    "old": "+20",
    "new": "+16",
    "text": null,
    "effect": "bad",
    "ability": "Healing Needles"
   },
   {
    "label": "Spirit scaling",
    "old": "0.2",
    "new": "0.24",
    "text": null,
    "effect": "good",
    "ability": "Healing Needles"
   },
   {
    "label": "T3 rush speed",
    "old": "+15%",
    "new": "+20%",
    "text": null,
    "effect": "good",
    "ability": "Wretched Vapors"
   },
   {
    "label": "Fear buildup",
    "old": "1.3s",
    "new": "2s",
    "text": null,
    "effect": "bad",
    "ability": "Lurking Terrors"
   },
   {
    "label": "Duration",
    "old": "7s",
    "new": "5s",
    "text": null,
    "effect": "bad",
    "ability": "Lurking Terrors"
   },
   {
    "label": "T3 duration",
    "old": "+3s",
    "new": "+2s",
    "text": null,
    "effect": "bad",
    "ability": "Lurking Terrors"
   },
   {
    "label": "T3 channel",
    "old": "Immune to damage",
    "new": "50% reduced damage",
    "text": null,
    "effect": "bad",
    "ability": "Lurking Terrors"
   },
   {
    "label": "Fear angle",
    "old": null,
    "new": null,
    "text": "No fear >50\u00b0 above/below view",
    "effect": "bad",
    "ability": "Lurking Terrors"
   },
   {
    "label": "Fed leech duration",
    "old": "180s",
    "new": "120s + 3s/min",
    "text": null,
    "effect": "bad",
    "ability": "Leech Therapy"
   },
   {
    "label": "Round reset",
    "old": null,
    "new": null,
    "text": "Ground leeches removed",
    "effect": "bad",
    "ability": "Leech Therapy"
   }
  ]
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
