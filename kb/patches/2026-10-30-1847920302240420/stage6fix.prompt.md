# Task: update hero knowledge-base entries after this patch

Patch: Halloween 2026 + Gameplay Update (2026-10-30)

## Synthesis

{
 "patch_size": "major",
 "size_why": "The change count is inflated by broad tuning, but two structural moves decide it: a three-part comeback package (non-hero gold 26%→30%, Haunted Souls secure up to 50% faster when behind, tick souls to the two poorest) reverses the 'leads stick' economy, and Radiant Regeneration plus Healing Booster being gutted in the same patch as anti-heal buffs and Healbane stacking deletes the regen-stack build family. Haunt bounty/HP/damage all +10% also reprices the entire off-lane farm the last two patches were built around.",
 "headline": "The comeback valve is open again, and regen stacking is dead — anti-heal and lifesteal own the sustain slot now.",
 "meta_thesis": {
  "previous": "Souls sit off-lane in a coverage problem no five-man can solve; AoE clearers and Heavy Melee crate openers bank first, lane bullies convert pressure, leads stick, and tempo usually closes the lobby before a late spike.",
  "new": "Off-lane farm is richer but a farm lead is now a soft lead: trailing teams secure contested Haunted Souls faster, get tick souls to their two poorest, and can farm their way back, so games run longer and sustained-farm carries and late spikes get a real window. Sustain itself migrates from regen stacking to in-fight lifesteal, because anti-heal is everywhere.",
  "relationship": "reversal",
  "why": "The KB's core economic read ('comeback bounties trimmed, extra souls reroute to the two lowest-econ players, leads stick') is directly undone by non-hero comeback gold 26%→30%, Haunted Souls securing up to 50% faster at a 20% net-worth gap, and tick souls now feeding the two poorest — while the tempo assassins who converted early leads lose Steam Vent invisibility and tunnel speed +70%→+50%."
 },
 "winners": [
  {
   "hero": "Apollo",
   "why": "Riposte disable 0.8s→1.5s plus dash reliability and CC refunds on Flawless Advance/Itani Lo Sahn remove his whiff windows; the longer immobilize also fits a patch where fights are picked, not sieged.",
   "indirect": false
  },
  {
   "hero": "Warden",
   "why": "Flask travel +40% and shred -25%→-30%, Willpower +15%→+20%, and Last Stand T2 +40.5→+50 DPS with -30s→-40s cooldown — and Steam Vents losing invisibility hands Shadow Weave back its exclusivity as the only invis-engage tool.",
   "indirect": false
  },
  {
   "hero": "Seven",
   "why": "Haunt bounty and growth +10% is the single biggest income lever and his AoE clear converts it best, while Spirit Lifesteal 13%→15% and Decay -50%→-55% buff his exact core slots against the +10% camp damage.",
   "indirect": true
  },
  {
   "hero": "Victor",
   "why": "Spirit Lifesteal, Infuser (70%→75% active, 6→8 spirit) and Torment Pulse 18%→22% melee resist all land on his slots; the Healing Booster trim is real but roughly cancelled.",
   "indirect": false
  },
  {
   "hero": "Infernus",
   "why": "Napalm T2 lifesteal 15%→20%, Concussive Combustion T3 +0.4 spirit scaling, and both Toxic Bullets 35%→40% and Decay buffed — the anti-heal patch is aimed at the fronts his burn out-ranges.",
   "indirect": false
  }
 ],
 "losers": [
  {
   "hero": "Rat King",
   "why": "Scrap Grenade damage and radius (8m→6m, 14m→10m) and Rule, Ratannia! (half knockup, 160s→180s, 20m→16m, 12s→9s, CD if stunned pre-place) are gutted exactly as Haunt camps gain +10% HP — his one-button clear stops being one-button.",
   "indirect": false
  },
  {
   "hero": "Baba",
   "why": "Random brew order each cast plus 1s→1.5s cycle removes on-demand silence/barrier, and both Radiant Regeneration (~94% buy) and Healing Booster are gutted in the same patch as anti-heal buffs — the regen wall was her identity.",
   "indirect": false
  },
  {
   "hero": "Celeste",
   "why": "Her entire shell was Radiant Regeneration plus Healing Booster, both gutted, into a patch where Decay/Toxic Bullets/stacking Healbane punish regen flyers; Shining Wonder 140→125 and the 0.35→0.5 air-drag ratio compound it.",
   "indirect": false
  },
  {
   "hero": "Lady Geist",
   "why": "Radiant Regeneration in ~98% of her games loses spirit-regen scaling 0.35→0.25, heal-on-cast 65→40 and its out-of-combat trigger; Essence Bomb 1.22→1.35 is a real buff but it buys burst, not the grind she wins with.",
   "indirect": false
  },
  {
   "hero": "Mo & Krill",
   "why": "Spirit per boon 1.1→0.6 plus all ability spirit damage -10% halves the stat both builds run on; +4% bullet per boon is a pivot, not a replacement.",
   "indirect": false
  }
 ],
 "non_obvious_calls": [
  {
   "claim": "Paige leaves S tier even though her direct nerfs read like a lane-damage trim.",
   "why": "Base bullet damage 35→32 (growth 0.52→0.61 only breaks even around boon 33) plus the comeback package and breakables growth -10% mean she wins lane by less and converts it into less — the snowball, not the poke, was her tier.",
   "confidence": 0.6
  },
  {
   "claim": "A whole build family dies this patch, and the heroes listed for it are collateral rather than targets.",
   "why": "Radiant Regeneration (fourth trim, in-combat only) and Healing Booster (loses Extra Regen +3 flat regen) are gutted while Decay, Toxic Bullets, Crippling Headshot and stacking Healbane all buff anti-heal — regen-stack sustain is replaced by Bullet/Spirit Lifesteal, Leech, Infuser and Vampiric Burst, so Baba/Celeste/Shiv/Lady Geist fall because their shell is gone, not because their kits were read.",
   "confidence": 0.7
  },
  {
   "claim": "The Steam Vent rework is a targeted nerf to the roam-assassin class that the last two patches had just promoted.",
   "why": "Vents go from invisibility to +150% stamina regen and tunnels +70%→+50% speed, hitting Holliday, Calico, Lash and Bebop — heroes who bank on free approach and fast rotations — right as the comeback package blunts the early leads they convert.",
   "confidence": 0.6
  },
  {
   "claim": "Return Fire reflecting Fixation is a Haze nerf disguised as a tank item buff.",
   "why": "Her stacking DoT is her only real scaling line, and the KB already flags her T4 gun items as the ceiling; putting a targeted counter-item on every frontline means she can no longer close kills into tanks alone.",
   "confidence": 0.55
  }
 ],
 "uncertainties": [
  "Whether the comeback package actually flips leads or just lengthens games — the KB's prior comeback bounties were trimmed because they didn't move the needle.",
  "Net effect of Haunt bounty +10% against HP and damage +10%: richer camps may still net-lose income for weak clearers, widening the coverage gap the KB already flagged rather than narrowing it.",
  "How strong the new Halloween Cauldron Candy/Sugar Rush buff is — no numbers were given, so the frontline value is a guess.",
  "Nurse Harrow's KB entry is thin and I have no prior tier, so my C-lean read is low confidence.",
  "Whether the Rat King and Baba nerfs overshoot: both were tuned down in prior patches, so stacking another cut could bench them outright."
 ],
 "what_to_watch": [
  "Average game length — the cleanest test of whether the comeback valve actually slows tempo.",
  "Win rate of teams down 5k+ net worth at 15 minutes, before and after — that single number settles the comeback debate.",
  "Radiant Regeneration and Healing Booster pick rates versus Bullet/Spirit Lifesteal and Leech — the build-family migration in one chart.",
  "Rat King and Baba win rates at their new tiers: if they stay near 50%, the nerfs were cosmetic; if they crater, the regen-stack removal was the real killer.",
  "Post-rework Steam Vent kill participation and tunnel-rotation frequency — did removing invisibility actually reduce gank rate, or did stamina regen replace it?",
  "Per-Haunt-type bounty and clear time: if one camp type dominates now that bounties are up 10%, farm routes re-converge and the no-memorization intent fails.",
  "High-MMR anti-heal item purchase rate (Decay/Toxic Bullets/Healbane) — a spike confirms sustain comps are being punished structurally, not just on paper."
 ]
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

## Hero analysis (this batch only)

[
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
  ],
  "change_kind": "nerf",
  "change_size": "moderate"
 },
 {
  "hero": "Apollo",
  "in_notes": true,
  "direction": "neutral",
  "magnitude": "moderate",
  "confidence": 0.6,
  "direct_reasons": [
   "Riposte Pommel Hit disable 0.8s->1.5s (T2 +0.4s->+0.6s) nearly doubles his lockdown window, even though it is now an immobilize plus parry disable rather than a stun.",
   "Riposte dash fixes stop the counterattack whiffing on moving, cornered or displaced targets - reliability he did not have.",
   "Flawless Advance now refunds the stab and keeps remaining recasts when stunned or slept, and Itani Lo Sahn is no longer interrupted by Sleep - two hard removals of his worst punish windows."
  ],
  "indirect_reasons": [
   "Stun to immobilize is the main change: immobilize does not interrupt channeled ults such as Seven, Bebop and Harrow, so he loses that answer.",
   "Healing Booster losing its Extra Regen component and flat +3 regen thins the sustain shell his spirit bruiser build leans on.",
   "Healbane now stacking is a team anti-heal gain but its heal-on-kill 275->170+3/boon is a personal sustain loss - roughly neutral for him.",
   "His losing lanes split: Warden and Abrams both buffed, but Wraith (Card Trick heal, Project Mind cooldown) and Mo & Krill (spirit damage -10%) both nerfed."
  ],
  "build_changes": [
   "Re-weight sustain toward Restorative Locket/Dispel Magic rather than Healing Booster; the longer Riposte disable makes pick-oriented spirit burst better than the old tank-and-outlast line."
  ],
  "tier_before": "S",
  "tier_after": "S",
  "one_liner": "Riposte no longer stuns: it immobilizes and disables parry, so it can't interrupt channels. Longer disable softens it.",
  "verdict": "watch",
  "rows": [
   {
    "label": "Pommel Hit",
    "old": "Stun",
    "new": "Immobilize + parry disable",
    "text": null,
    "effect": "bad",
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
  ],
  "change_kind": "rework",
  "change_size": "major"
 },
 {
  "hero": "Silver",
  "in_notes": true,
  "direction": "neutral",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [
   "Base health regen 2.5\u21923 is trivial on a tank that already builds Restorative Shot/Melee Lifesteal.",
   "Go For The Throat now counts Point Blank and Opening Rounds weapon damage, and Point Blank's slow went 2s\u21922.5s \u2014 that combo is now a real damage package, not a flex.",
   "Both Entangling Bola fixes (Unstoppable flyers, Grey Talon during Rain of Arrows) make her grounding reliable, which matters into Vindicta/Grey Talon/Danny."
  ],
  "indirect_reasons": [
   "Hunter's Aura now needs line of sight \u2014 the through-wall shred she bought it for in clumped fights is gone (core gun-tank slot).",
   "Spirit Shielding 18%\u219215% spirit resist trims a core defensive layer into a spirit-burst patch.",
   "Anti-heal is the patch's clearest theme (Decay/Toxic Bullets/Crippling Headshot up, Healbane stacking) and it attacks her Melee Lifesteal/Restorative Shot sustain directly.",
   "Counter-side offsets: Rat King (62% vs her) ate a huge nerf, the mobile-assassin archetype is down (Steam Vents lose invis, tunnels +70%\u2192+50%), and the tank/frontline archetype is up (Cauldrons, Healing Snacks 10%\u219214%)."
  ],
  "build_changes": [
   "Buy Point Blank as a core slot: its slow extends and its weapon damage now feeds Go For The Throat.",
   "Deliberately delay Hunter's Aura \u2014 it no longer shreds through walls, so it is an LOS-fight item only now."
  ],
  "tier_before": "S",
  "tier_after": "A",
  "one_liner": "Still fine, but Hunter's Aura no longer shreds through walls and the anti-heal patch bites her sustain.",
  "verdict": "watch",
  "rows": [
   {
    "label": "Health regen",
    "old": "2.5",
    "new": "3",
    "text": null,
    "effect": "good",
    "ability": null
   },
   {
    "label": "Weapon damage",
    "old": null,
    "new": null,
    "text": "Now counts Point Blank and Opening Rounds",
    "effect": "good",
    "ability": "Go For The Throat"
   },
   {
    "label": "Bug fixes",
    "old": null,
    "new": null,
    "text": "Unstoppable flyers stay up; grounds Talon's ult",
    "effect": "neutral",
    "ability": "Entangling Bola"
   }
  ],
  "change_kind": "buff",
  "change_size": "minor"
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
  "one_liner": "Small damage nerf in the notes; the regen item cuts and anti-heal are what really hurt.",
  "verdict": "watch",
  "rows": [
   {
    "label": "Damage",
    "old": "140",
    "new": "125",
    "text": null,
    "effect": "bad",
    "ability": "Shining Wonder"
   }
  ],
  "change_kind": "nerf",
  "change_size": "minor"
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
    "label": "If stunned first",
    "old": null,
    "new": null,
    "text": "Goes on cooldown; flag drops with no impact",
    "effect": "bad",
    "ability": "Rule, Ratannia!"
   }
  ],
  "change_kind": "nerf",
  "change_size": "major"
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
  ],
  "change_kind": "nerf",
  "change_size": "major"
 },
 {
  "hero": "Solomon",
  "in_notes": true,
  "direction": "neutral",
  "magnitude": "moderate",
  "confidence": 0.4,
  "direct_reasons": [
   "Base bullet damage 30\u219225 and -20% headshot damage hurt the HVR/Opening Rounds lane phase \u2014 a lane crutch he needed at a 46% win rate.",
   "Rook Battery spirit scaling 1.3\u21920.9 is a real damage cut and the T3 cooldown trim softened (-12s\u2192-10s).",
   "Setup Bishop got the compensation: on-square spirit scaling 0.64\u21920.85, T1 slow +15%\u2192+25%, T3 resist shred -2.5%\u2192-5% per stack applied on impact, so his zone is now the damage.",
   "Develop Queen: 210s\u2192240s cooldown and 1s\u21921.2s stun-tile delay are bad, but checkmate under 100 HP is now in the base kit and T2 adds +150 threshold, plus Move Piece 50m\u219265m with better placement."
  ],
  "indirect_reasons": [
   "Three of his five losing matchups got hit: Rat King (huge nerf package), Baba (brew/regen gutted) and Celeste (Shining Wonder + regen items).",
   "The mobile-dive archetype he dies to is down (Steam Vents lose invisibility, tunnels +70%\u2192+50%), and Yamato's Flying Slash range 26m\u219223m (T3 +15\u2192+8m) shortens the dive that beat him 38%.",
   "Divine Barrier 45s\u219255s cooldown trims his situational late item, and anti-heal stacking hurts any heal/sustain layer he buys."
  ],
  "build_changes": [
   "Max Setup Bishop over Rook Battery \u2014 the bishop is now the damage (0.85 scaling, faster T3 shred).",
   "Treat his gun line as a lane crutch only after the 30\u219225 bullet and -20% headshot cuts."
  ],
  "tier_before": "C",
  "tier_after": "C",
  "one_liner": "His zone got better and his counters got nerfed, but the gun and Rook Battery both lost real damage.",
  "verdict": "watch",
  "rows": [
   {
    "label": "Base bullet damage",
    "old": "30",
    "new": "25",
    "text": null,
    "effect": "bad",
    "ability": null
   },
   {
    "label": "Headshot damage",
    "old": null,
    "new": null,
    "text": "-20%",
    "effect": "bad",
    "ability": null
   },
   {
    "label": "Square height",
    "old": "4m",
    "new": "1m",
    "text": null,
    "effect": "neutral",
    "ability": "Setup Bishop"
   },
   {
    "label": "On-square scaling",
    "old": "0.64",
    "new": "0.85",
    "text": null,
    "effect": "good",
    "ability": "Setup Bishop"
   },
   {
    "label": "T1 slow",
    "old": "+15%",
    "new": "+25%",
    "text": null,
    "effect": "good",
    "ability": "Setup Bishop"
   },
   {
    "label": "T3 shred",
    "old": "-2.5%",
    "new": "-5% per stack",
    "text": null,
    "effect": "good",
    "ability": "Setup Bishop"
   },
   {
    "label": "T3 shred timing",
    "old": null,
    "new": null,
    "text": "Applies on impact, not by squares",
    "effect": "neutral",
    "ability": "Setup Bishop"
   },
   {
    "label": "Damage scaling",
    "old": "1.3",
    "new": "0.9",
    "text": null,
    "effect": "bad",
    "ability": "Rook Battery"
   },
   {
    "label": "T3 cooldown",
    "old": "-12s",
    "new": "-10s",
    "text": null,
    "effect": "bad",
    "ability": "Rook Battery"
   },
   {
    "label": "Cooldown",
    "old": "210s",
    "new": "240s",
    "text": null,
    "effect": "bad",
    "ability": "Develop Queen"
   },
   {
    "label": "Damage scaling",
    "old": "1.4",
    "new": "1.6",
    "text": null,
    "effect": "good",
    "ability": "Develop Queen"
   },
   {
    "label": "Stun delay",
    "old": "1s",
    "new": "1.2s",
    "text": null,
    "effect": "bad",
    "ability": "Develop Queen"
   },
   {
    "label": "Checkmate",
    "old": null,
    "new": null,
    "text": "Base kit: heroes under 100 HP",
    "effect": "good",
    "ability": "Develop Queen"
   },
   {
    "label": "T2 checkmate",
    "old": null,
    "new": null,
    "text": "Threshold +150",
    "effect": "good",
    "ability": "Develop Queen"
   },
   {
    "label": "Piece range",
    "old": "50m",
    "new": "65m",
    "text": null,
    "effect": "good",
    "ability": "Move Piece"
   },
   {
    "label": "Placement",
    "old": null,
    "new": null,
    "text": "Lands closer to aim, works near walls",
    "effect": "good",
    "ability": "Move Piece"
   }
  ],
  "change_kind": "rework",
  "change_size": "major"
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
    "label": "Bug fix",
    "old": null,
    "new": null,
    "text": "Now deals damage when held through Close The Deal",
    "effect": "good",
    "ability": "Chimera Mk1"
   }
  ],
  "change_kind": "nerf",
  "change_size": "moderate"
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
    "label": "Sketches",
    "old": null,
    "new": null,
    "text": "Healing amp for healers, Spirit Power for three heroes",
    "effect": "neutral",
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
    "text": "Ink can be destroyed again",
    "effect": "bad",
    "ability": "Abstract Landscape"
   }
  ],
  "change_kind": "nerf",
  "change_size": "major"
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
  ],
  "change_kind": "nerf",
  "change_size": "major"
 }
]

## Current hero entries (this batch only)

Graves:
  name: Graves
  role: gun carry/summoner split pusher
  archetypes:
  - gun carry
  - split pusher
  - late scaler
  tier: B
  trend: rising
  why: 'Trap-clearing gun carry who still deletes Venator''s pre-placed traps, and
    the one archetype the new economy actually fixes: tick souls to the two poorest,
    a 30% non-hero comeback cap and up-to-50% faster secure when behind fund the ~25-minute
    window she previously never reached. The summoner/cooldown shell is her real path
    (Echo Shard post-cast 0.5->0.2s); the on-hit gun variant is taxed by Bullet Resilience
    30->35% and the now-visible 10% bullet resist on Return Fire.'
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
  notes: "10-30 Halloween + Gameplay Update: her documented 'no comeback bail-out'\
    \ weakness is reversed \u2014 30% non-hero comeback cap, tick souls to the two\
    \ poorest and faster deficit secure fund the ~25-min window; Echo Shard post-cast\
    \ 0.5->0.2s helps the summoner core and Toxic Bullets 40% helps the on-hit line,\
    \ while Bullet Resilience 30->35% taxes the gun variant. Her direct line was flagged\
    \ in-notes but not parsed by the batch analysis \u2014 direction unresolved; win/pick\
    \ snapshot 56.5%/40.9% still conflicts with the KB's 48.5%/21% and needs a recheck.\n\
    10-20 Shh...: tier C->B, trend rising \u2014 trap-clearing into Venator is a real\
    \ draft lever, but Barrel Mimics punish her low-HP, two-stamina crate chains and\
    \ the corridor economy still taxes her scaling window.\n10-16 Paint the Town:\
    \ her gun destroys Venator's traps - genuine utility into an A-tier hero - but\
    \ the earlier, contested soul economy still deletes her ~25-min scaling line."
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


## What to do

Produce the post-patch knowledge base state for the heroes in this batch. This KB is read by the analyst on the *next* patch, so write it as durable state, not as a patch summary.

1. **hero_updates**: for each mover, the fields that changed. Allowed fields: role, archetypes, tier, trend, why, core_items, builds (full replacement list of {name, damage, core_items, popularity, notes}), matchups ({beats, loses_to}), enabled_by, countered_by, notes. When an item change kills or creates a build, update `builds`, not just `notes`. When another hero's change alters a matchup, update `matchups`. Set `last_changed_patch` to "Halloween 2026 + Gameplay Update" for heroes that had direct changes. `why` is 1-2 sentences of present-tense state ("strong because X; weak to Y"), not a changelog. `notes` may hold a short changelog line (keep the last 3 lines, newest first). Do not touch heroes not in this batch.

   For each hero, output only the fields whose value actually changes. Omit any field that stays the same — omitted fields are kept as-is in the KB. Include `builds` only if at least one build is created, killed, or its core items change; when you include it, it is a full replacement list. Include `matchups` only if a matchup changes.
2. **change_log**: one line per KB edit you made, for the human to skim.

Tier is one of S/A/B/C/D. Trend is rising/stable/falling.

## Output schema

{
  "hero_updates": {"Hero Name": {"tier": "A", "trend": "falling", "why": "...", "core_items": ["..."], "last_changed_patch": "...", "notes": "..."}},
  "change_log": ["Hero Name: tier S -> A (Card Trick heal nerfs + Veil Walker loss)", "..."]
}
