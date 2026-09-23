# Task: per-hero analysis (all heroes)

Patch: Minor Update - 09-16-2026 (2026-09-16)

## Systems analysis

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

## Item analysis

{
 "items": [
  {
   "item": "Weakening Headshot",
   "direction": "nerf",
   "magnitude": "minor",
   "summary": "A -13%->-12% shred trim is cosmetic on its own, but it lands on Venator whose whole identity is 'no weak point' — removing a point of resist-shred slightly narrows his already-struggling tempo conversion (45.7% WR).",
   "affected_heroes": [
    {
     "hero": "Venator",
     "relationship": "core",
     "effect": "down",
     "why": "His core resist-shred item got a point weaker, piling onto a WR that already hasn't matched his reputation."
    }
   ],
   "build_shift": ""
  },
  {
   "item": "Hollow Point",
   "direction": "buff",
   "magnitude": "minor",
   "summary": "9->10% resist-shred is a small number but it's on the cheap T2 early-gun item, exactly where the tempo patch wants damage online. Reinforces the win-lane-harder path rather than the super-scaling one.",
   "affected_heroes": [
    {
     "hero": "Vindicta",
     "relationship": "core",
     "effect": "up",
     "why": "Tempo early-gun carry whose T2 shred got stronger in the meta that already favors her."
    },
    {
     "hero": "Seven",
     "relationship": "core",
     "effect": "up",
     "why": "Loves the early shred but still draft-dependent and pace-sensitive."
    },
    {
     "hero": "Vyper",
     "relationship": "core",
     "effect": "up",
     "why": "Top-WR gun carry gets a small boost to her lane-dominant opening."
    },
    {
     "hero": "Silver",
     "relationship": "core",
     "effect": "up",
     "why": "The patch's biggest winner also buys the buffed early-gun shred."
    },
    {
     "hero": "Venator",
     "relationship": "core",
     "effect": "neutral",
     "why": "Compensates the small Weakening Headshot nerf but doesn't fix his conversion problem."
    },
    {
     "hero": "Grey Talon",
     "relationship": "core",
     "effect": "neutral",
     "why": "C-tier poke carry that still can't convert the early lead the item wants to create."
    }
   ],
   "build_shift": "Solidifies cheap T2 weapon shred as the default first-gun slot in the tempo meta."
  },
  {
   "item": "Toxic Bullets",
   "direction": "buff",
   "magnitude": "minor",
   "summary": "Spirit scaling 0.005->0.006% is a nudge, but anti-heal DoT gains value as the patch funnels fights into inflated-HP bruisers and tanks; it's one of the few clean answers to big health pools.",
   "affected_heroes": [
    {
     "hero": "Infernus",
     "relationship": "core",
     "effect": "up",
     "why": "Burn carry whose scaling gets a hair better; still out-paced by the tempo meta."
    },
    {
     "hero": "Drifter",
     "relationship": "core",
     "effect": "up",
     "why": "Blind-pickable bruiser with built-in anti-heal stacks another anti-heal DoT."
    },
    {
     "hero": "Graves",
     "relationship": "core",
     "effect": "neutral",
     "why": "Gets the buff but her core problem is base stats, not this item."
    }
   ],
   "build_shift": ""
  },
  {
   "item": "Shadow Weave",
   "direction": "buff",
   "magnitude": "moderate",
   "summary": "Now builds from Sprint Boots, sprint 1.5->2 and cooldown 45->37s — cheaper, faster, more uptime invis. Despite creators still calling it poor, the path change lowers the entry cost for gun carries who want a repositioning tool in a pick-heavy meta.",
   "affected_heroes": [],
   "build_shift": "Gains the Sprint Boots component while Veil Walker loses it — the two invis items now diverge on the same tier-3 Vitality path, and this is the cheaper of the two."
  },
  {
   "item": "Cultist Sacrifice",
   "direction": "nerf",
   "magnitude": "minor",
   "summary": "180->170% bounty is a small number but it stacks with the whole patch's anti-greed direction: econ items are worse when comeback souls are gone and tempo wins games, so a soul-printing buy is now a tempo tax.",
   "affected_heroes": [],
   "build_shift": ""
  },
  {
   "item": "Ballistic Enchantment",
   "direction": "buff",
   "magnitude": "minor",
   "summary": "14->20s duration is a real uptime gain on a niche spirit utility item, but with no clear user base in the KB this stays a fringe pickup. Low confidence on who it helps.",
   "affected_heroes": [],
   "build_shift": ""
  },
  {
   "item": "Spiritual Overflow",
   "direction": "nerf",
   "magnitude": "major",
   "summary": "35% slower buildup plus spirit power 40->30 and fire rate 30->25% is a triple gut on top of July's cuts — this is the proc-carry steroid that powered the Warden Mercurial build, and it no longer pays off inside a fight's window.",
   "affected_heroes": [
    {
     "hero": "Warden",
     "relationship": "core",
     "effect": "down",
     "why": "Loses his primary damage steroid on top of Mercurial Magnum and Plated Armor hits — a three-item pile-on."
    }
   ],
   "build_shift": "With slower buildup, the item wants longer fights the tempo meta no longer provides; effectively removed from the spirit-carry proc build."
  },
  {
   "item": "Restorative Locket",
   "direction": "nerf",
   "magnitude": "minor",
   "summary": "Heal per boon 0.5->0.45 and stack range 35->32m trims both throughput and uptime; on a tempo support it's a soft power cut stacked on 08-22's resist nerf.",
   "affected_heroes": [
    {
     "hero": "Apollo",
     "relationship": "core",
     "effect": "down",
     "why": "The patch's archetype winner takes a small item-side offset to his lane-bully sustain."
    }
   ],
   "build_shift": ""
  },
  {
   "item": "Trophy Collector",
   "direction": "nerf",
   "magnitude": "minor",
   "summary": "Souls/min 18->16 is another piece of the item-side economy tightening — pure-farm econ buys lose value in the same patch that delayed tunnel breakables and cut comeback souls.",
   "affected_heroes": [],
   "build_shift": ""
  },
  {
   "item": "Veil Walker",
   "direction": "nerf",
   "magnitude": "major",
   "summary": "Losing the Sprint Boots component kills +2 sprint/regen, movespeed now drops when invis ends, and spirit power 10->6 — the escape-and-reposition package is gutted. It goes from auto-buy to a pick-hero-only tool.",
   "affected_heroes": [
    {
     "hero": "Holliday",
     "relationship": "core",
     "effect": "down",
     "why": "Loses a core enabler just as the tempo meta otherwise favors her pick play."
    },
    {
     "hero": "Warden",
     "relationship": "core",
     "effect": "down",
     "why": "Compounds his Mercurial/Overflow losses — now stripped on item and hero side."
    }
   ],
   "build_shift": "No longer on the Sprint Boots path, so it competes for a Vitality slot without the mobility subsidy; Shadow Weave now inherits that component."
  },
  {
   "item": "Fortitude",
   "direction": "buff",
   "magnitude": "minor",
   "summary": "2->2.25% max-health regen is a rounding-level buff, but it's on the default survivability slot for nearly every bruiser and tank, and the patch's slower respawn/longer-fight direction makes sustained regen more valuable than burst.",
   "affected_heroes": [
    {
     "hero": "Abrams",
     "relationship": "core",
     "effect": "up",
     "why": "Bruiser already helped by the gun-cycle change; slight extra regen keeps him brawling."
    },
    {
     "hero": "Mo & Krill",
     "relationship": "core",
     "effect": "up",
     "why": "Tank that lives in minute-one brawls the patch rewards."
    },
    {
     "hero": "Lycan-style bruisers (Seven, Infernus, Shiv, Silver)",
     "relationship": "core",
     "effect": "up",
     "why": "Near-universal slot — anyone on Fortitude gets a tiny durability tax cut in longer fights."
    }
   ],
   "build_shift": ""
  },
  {
   "item": "Lifestrike",
   "direction": "buff",
   "magnitude": "moderate",
   "summary": "Melee heal 100+1.5->120+1.75 and 30->35% is a real sustain gain, but the bigger story is synergy: with slows now affecting air drag, its 48% slow becomes a genuine anti-air lockdown, so it reads as a CC item as much as a heal.",
   "affected_heroes": [
    {
     "hero": "Billy",
     "relationship": "core",
     "effect": "up",
     "why": "Effectively a Billy item — the heal buff plus new anti-air slow feeds his already-dominant S-tier frontline."
    }
   ],
   "build_shift": "Upgrades from a melee-sustain slot to a CC/anti-air option in the same patch slows gained air-drag effect."
  },
  {
   "item": "Leech",
   "direction": "buff",
   "magnitude": "minor",
   "summary": "25->28% bullet+spirit lifesteal raises ceiling but the KB still calls it weak, and in a tempo meta that ends fights fast there's little window to lifesteal back — the buff doesn't address why nobody buys it.",
   "affected_heroes": [],
   "build_shift": ""
  },
  {
   "item": "Plated Armor",
   "direction": "buff",
   "magnitude": "moderate",
   "summary": "The fix is a real balance shift, not cosmetic: it now blocks on-hit spirit damage from Mercurial Magnum, Vindicta's Flight, Wraith's Full Auto and Tesla Bullets/Capacitor — turning a defensive slot into a hard counter to mixed-damage on-hit carries.",
   "affected_heroes": [
    {
     "hero": "Warden",
     "relationship": "situational",
     "effect": "down",
     "why": "Mercurial Magnum on-hit spirit damage is now actually blocked — third hit to his build this patch."
    },
    {
     "hero": "Wraith",
     "relationship": "situational",
     "effect": "down",
     "why": "Full Auto spirit damage now gets eaten, worsening her already-falling trajectory."
    },
    {
     "hero": "Vindicta",
     "relationship": "situational",
     "effect": "down",
     "why": "Flight on-hit is now counterable by a defensive pick, trimming the tempo winner's tools."
    }
   ],
   "build_shift": "Becomes the defensive answer to on-hit/mixed-damage builds, competing with generic resist slots for tank-side buyers."
  },
  {
   "item": "Diviner's Kevlar",
   "direction": "rework",
   "magnitude": "moderate",
   "summary": "Adding +10% ultimate CDR pushes it from a generic defense item into a coordination/initiation enabler — it now wants heroes whose win condition is a big ult on a clock.",
   "affected_heroes": [
    {
     "hero": "Dynamo",
     "relationship": "core",
     "effect": "up",
     "why": "Ult-initiator whose whole value is the AoE-CC ult; CDR makes his threat cycle faster."
    },
    {
     "hero": "Silver",
     "relationship": "core",
     "effect": "up",
     "why": "Tank-carry that already buys it, now with better ult uptime on top of her other buffs."
    }
   ],
   "build_shift": "Slot stays Vitality, but the item's identity tilts from survivability toward ult-uptime — direct competition with pure CDR items."
  },
  {
   "item": "Golden Goose Egg",
   "direction": "nerf",
   "magnitude": "major",
   "summary": "Damage penalty -10->-15%, souls/min 90->80, and stored souls now count toward net worth — the last clause is the killer: it interacts directly with the patch's comeback change and removes the item's whole point of hiding net worth from bounty math.",
   "affected_heroes": [],
   "build_shift": "Effectively unbuyable — the patch's worst item, and the clause tying stored souls to net worth is a targeted deletion of the 'lose lane, bank souls, ignore come back' pattern."
  },
  {
   "item": "Slowing Hex",
   "direction": "nerf",
   "magnitude": "minor",
   "summary": "27->29s cooldown trims the pick-engage frequency on near-every-game pick heroes, but the global slow change cuts the other way: its slow now drags flyers out of the air, adding a new anti-air use that partially offsets the CD tax.",
   "affected_heroes": [
    {
     "hero": "Paradox",
     "relationship": "core",
     "effect": "down",
     "why": "Loses some uptime on her cheap pick-enabler on top of her Carbine trim."
    },
    {
     "hero": "Wraith",
     "relationship": "core",
     "effect": "down",
     "why": "CC-build staple gets shorter engage windows during an already-falling patch."
    },
    {
     "hero": "Paige",
     "relationship": "core",
     "effect": "neutral",
     "why": "Loses a little CD but gains the new anti-air slow on the flyers she was buffed to punish."
    }
   ],
   "build_shift": ""
  },
  {
   "item": "Radiant Regeneration",
   "direction": "nerf",
   "magnitude": "minor",
   "summary": "Per-boon scaling 2->1.7 caps out less late; it's the second cut in two patches to a healing-support item, softly taxing sustain supports without removing the slot.",
   "affected_heroes": [
    {
     "hero": "Kelvin",
     "relationship": "core",
     "effect": "down",
     "why": "Healer whose item path is being progressively trimmed on top of 08-22's nerf."
    }
   ],
   "build_shift": ""
  },
  {
   "item": "Tankbuster",
   "direction": "nerf",
   "magnitude": "minor",
   "summary": "8->7.5% current-health bonus is a nudge, but stacked on 07-28 (no longer procs off items) it's a cumulative trim to the anti-tank slot just as the patch funnels big HP pools into fights.",
   "affected_heroes": [
    {
     "hero": "Shiv",
     "relationship": "core",
     "effect": "down",
     "why": "Anti-tank bruiser loses a hair of his shred, though his current-HP knives carry the identity."
    },
    {
     "hero": "Yamato",
     "relationship": "core",
     "effect": "down",
     "why": "Small trim on a slot she relies on for the burst that the tempo meta rewards."
    }
   ],
   "build_shift": ""
  },
  {
   "item": "Decay",
   "direction": "neutral",
   "magnitude": "minor",
   "summary": "DPS -25% but duration +20% trades burst healing-cut for sustained anti-heal — worse at clipping a single big burst-heal window, better at keeping tanks suppressed over a long brawl, which fits the patch's longer fights.",
   "affected_heroes": [
    {
     "hero": "Abrams",
     "relationship": "core",
     "effect": "up",
     "why": "Anti-heal identity on a tank who lives in sustained brawls the duration buff suits."
    },
    {
     "hero": "Billy",
     "relationship": "core",
     "effect": "up",
     "why": "Frontline brawler who wants sustained suppression over long fights."
    },
    {
     "hero": "Mo & Krill",
     "relationship": "core",
     "effect": "up",
     "why": "Tank-friendly slot on a hero that brawls from minute one."
    },
    {
     "hero": "Infernus",
     "relationship": "core",
     "effect": "neutral",
     "why": "Anti-heal user whose burn carries; shape of the item shift is roughly a wash for him."
    },
    {
     "hero": "Lady Geist",
     "relationship": "core",
     "effect": "neutral",
     "why": "Rising scaler who buys it mostly as a defensive anti-heal tool."
    }
   ],
   "build_shift": "Still the go-to anti-heal slot; the DPS/duration swap slightly favors sustained-fight buyers over pick-window users."
  },
  {
   "item": "Mercurial Magnum",
   "direction": "nerf",
   "magnitude": "major",
   "summary": "Base bullet scaling 0.49->0.38 and base damage 25->20% is a heavy cut — combined with the Spiritual Overflow nerf and Plated Armor fix, the Mercurial on-hit carry build it anchored is dead in one patch.",
   "affected_heroes": [
    {
     "hero": "Warden",
     "relationship": "core",
     "effect": "down",
     "why": "His signature carry item is gutted, and his two supporting items were hit in the same patch."
    }
   ],
   "build_shift": "No longer a damage engine; the on-hit proc build has no reliable core."
  },
  {
   "item": "Focus Lens",
   "direction": "buff",
   "magnitude": "minor",
   "summary": "30->35% damage and cast range 20->25m make it a stronger spirit-amp option, but it's still cleansable, so the buff mostly helps clean engages rather than dominating. Low-confidence read — no KB user listed.",
   "affected_heroes": [],
   "build_shift": "Better range makes it a more viable opener for burst casters on cleansable targets."
  }
 ],
 "notable_item_stories": [
  "Three econ items (Cultist Sacrifice, Trophy Collector, Golden Goose Egg) get trimmed at once — the item-side echo of the patch's anti-comeback economy, with Golden Goose Egg's net-worth clause specifically deleting the bank-and-hide pattern.",
  "The Mercurial Magnum + Spiritual Overflow nerfs plus Plated Armor's on-hit fix form one coordinated stack that removes Warden's carry build in a single patch.",
  "Invisibility items diverge around Sprint Boots: Shadow Weave gains the component plus a buff while Veil Walker loses it and gets stripped, so expect cheap gun-invis to rise and the pick-hero invis to fall."
 ]
}

## Direct hero changes in this patch (grouped by hero; heroes not listed had no direct changes)

Abrams:
  - [neutral] Infernal Resilience: Abrams: Infernal Resilience T3 increased from +8% to +9%
  - [neutral] Seismic Impact: Abrams: Seismic Impact T3 reduced from 6s Unstoppable to 5s
Celeste:
  - [nerf] Celeste: Stamina cooldown increased from 5 to 5.3
  - [nerf] Light Eater: Celeste: Light Eater spirit lifesteal reduced from 20% to 18%
  - [neutral] Light Eater: Celeste: Light Eater T3 decreased from +25 to +22
  - [nerf] Dazzling Trick: Celeste: Dazzling Trick cooldown increased from 34s to 38s
  - [neutral] Radiant Daggers: Celeste: Radiant Daggers T2 reduced from +80 to +70
  - [nerf] Shining Wonder: Celeste: Shining Wonder radius reduced from 16.5m to 15.5m
  - [neutral] Shining Wonder: Celeste: Shining Wonder T3 Max Bounces reduced from +8 to +6
Graves:
  - [buff] Graves: Health per boon increased from 33 to 35
Haze:
  - [neutral] Fixation: Haze: Fixation headshot stack count increased from +2 to +3
  - [buff] Fixation: Haze: Fixation T3 weapon scaling increased from 0.0003 to 0.00035
Holliday:
  - [buff] Holliday: Health per boon increased from 41 to 43
  - [rework] Crackshot: Holliday: Crackshot T2 now also applies -6% Bullet Resistance for 5s
  - [buff] Bounce Pad: Holliday: Lasso duration extention by Bounce Pad increased from +1s to +1.25s
Ivy:
  - [nerf] Stone Form: Ivy: Stone Form radius reduced from 6m to 5.75m
  - [nerf] Stone Form: Ivy: Stone Form T1 max health heal reduced from 7% to 6%
Kelvin:
  - [rework] Frozen Shelter: Kelvin: Frozen Shelter base ability health regen now scales with spirit power (0.2)
Lady Geist:
  - [buff] Life Drain: Lady Geist: Life Drain T3 spirit scaling increased from +0.3 to +0.45
  - [buff] Essence Bomb: Lady Geist: Essence Bomb T3 damage increased from 26% to 30%
Lash:
  - [nerf] Lash: Gun falloff range reduced from 18m->54m to 16m->48m
  - [buff] Ground Strike: Lash: Ground Strike T3 spirit scaling increased from +0.03 to +0.04
  - [buff] Ground Strike: Lash: Ground Strike T3 damage per meter scaling increased from 110% to 120%
  - [nerf] Grapple: Lash: Grapple T2 Weapon Damage buff duration reduced from 10s to 6s
  - [nerf] Flog: Lash: Flog heal reduced from 50% to 40%
  - [neutral] Flog: Lash: Flog angle increased from 38 to 40
  - [neutral] Flog: Lash: Flog T3 reduced from +40 degrees angle to +25
  - [nerf] Flog: Lash: Flog T3 reduced from +20% heal to +15%
Paige:
  - [buff] Melee: Paige: Heavy Melee spirit scaling increased from 0.3 to 0.45
  - [nerf] Captivating Read: Paige: Captivating Read T1 increased from -11s Cooldown to -14s
  - [neutral] Captivating Read: Paige: Captivating Read T3 increased from +1m to +2m
  - [fix] Rallying Charge: Paige: Fixed some collision issues with Rallying Charge
Paradox:
  - [nerf] Kinetic Carbine: Paradox: Kinetic Carbine min damage multiplier reduced from 25% to 10% (max damage multiplier unaffected)
  - [rework] Kinetic Carbine: Paradox: Kinetic Carbine min damage multiplier no longer gets increased by the T3
Rem:
  - [fix] Rem: Fixed a bug where multiple helpers could be sent to follow a single player for no effect
  - [rework] Lil Helpers: Rem: Lil Helpers now have a target UI when instant cast mode is selected
Shiv:
  - [buff] Shiv: Alt fire base damage increased by 4%
  - [buff] Shiv: Alt fire damage per boon increased from +0.2 to +0.24
  - [rework] Serrated Knives: Shiv: Serrated Knives while rage is full now deals 3.5% current HP damage on impact instead of ricocheting (0.01 spirit scaling)
Silver:
  - [buff] Silver: Health per boon increased from 28 to 31
  - [buff] Silver: Sprint speed increased from 1.5 to 2.5
  - [rework] Melee: Silver: Dashes and light melee's no longer pause your gun's cycle time
  - [rework] Boot Kick: Silver: Boot Kick can only target heroes and objectives now
  - [rework] Entangling Bola: Silver: Entangling Bola can only target heroes now
  - [rework] Silver: Weighted Bola now increases gravity during the debuff duration, and interrupts flying abilities (same rules as Phantom Strike)
Venator:
  - [rework] Ira Domini: Venator: Ira Domini now works with Ricochet, all the shots will bounce
  - [rework] Ira Domini: Venator: Ira Domini can now split shot (releases 1 extra bolt on each side, 3 total)
Viscous:
  - [nerf] Viscous: Alt fire damage growth reduced by 10%
  - [buff] Splatter: Viscous: Splatter detonation cooldown reduced from 0.15 to 0.12
  - [neutral] Splatter: Viscous: Splatter T1 reduced from +2m to +1.5m
  - [nerf] The Cube: Viscous: The Cube cast range reduced from 26m to 20m
  - [nerf] Puddle Punch: Viscous: Puddle Punch cooldown increased from 21s to 24s
  - [rework] Goo Ball: Viscous: Goo Ball T3 now also increases spirit scaling by 0.2
Vyper:
  - [nerf] Slither: Vyper: Slither T3 barrier duration reduced from 5s to 4s
  - [nerf] Petrifying Bola: Vyper: Petrifying Bola cooldown increased from 105s to 115s
Warden:
  - [nerf] Warden: Bullet damage per boon reduced from 0.28 to 0.25
  - [nerf] Warden: Fire Rate spirit scaling reduced from 0.25 to 0.21
  - [nerf] Alchemical Flask: Warden: Alchemical Flask projectile range and speed reduced by 30%
  - [nerf] Willpower: Warden: Willpower T3 spirit scaling reduced from +2.7 to +2.1
  - [neutral] Willpower: Warden: Willpower T3 debuff resistance reduced from 40% to 30%
Wraith:
  - [nerf] Card Trick: Wraith: Card Trick heart heal reduced from 75 to 60
  - [nerf] Card Trick: Wraith: Card Trick heart heal spirit scaling reduced from 0.75 to 0.5
  - [nerf] Card Trick: Wraith: Card Trick Diamond Bullet and Spirit Resist reduction reduced from -8% to -7%
  - [nerf] Card Trick: Wraith: Card Trick T3 Diamond Bullet and Spirit Resist reduction reduced from -5% to -4%
  - [nerf] Card Trick: Wraith: Card Trick T3 Clubs slow from +20% to +15%
  - [fix] Project Mind: Wraith: Fixed Project Mind getting caught on edges/corners when aiming past it
  - [buff] Full Auto: Wraith: Full Auto spirit damage per bullet scaling increased from 0.03 to 0.045
Yamato:
  - [rework] Crimson Slash: Yamato: Crimson Slash T3 now also increases the heal spirit scaling by +0.4
  - [buff] Flying Slash: Yamato: Flying Slash light melee scaling increased from 1.0 to 1.2

## Knowledge base: current state of every hero (pre-patch)

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
Haze:
  name: Haze
  role: gun carry
  archetypes:
  - gun carry
  - late scaler
  tier: A
  trend: rising
  why: "Fixation got a real buff (headshot stacks 2->3, higher T3 weapon scaling)\
    \ and gun Haze is the build a tempo meta prefers \u2014 headshots convert leads\
    \ where the old Echo-Shard sleep cheese can't carry a losing game."
  core_items:
  - Lucky Shot
  - Ricochet
  - Echo Shard
  - Tesla Bullets
  build_variants:
  - gun build
  - Echo Shard sleep build
  enabled_by:
  - Fixation buff
  - Ricochet farm
  countered_by:
  - Decay/anti-heal
  - CC lockdown
  - Plated Armor
  last_changed_patch: Minor Update - 09-16-2026
  notes: Sleep Dagger got trimmed in July; the newer read is that gun Haze, not the
    sleep combo, is the good build.
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
Bebop:
  name: Bebop
  role: hook initiator
  archetypes:
  - initiator
  - burst caster
  tier: B
  trend: stable
  why: Solid hook-and-lockdown hero untouched by the last patches; fine in a tempo
    meta but lacks the snowball tools of the new top tier.
  core_items:
  - Extra Charge
  - Superior Cooldown
  - Echo Shard
  build_variants:
  - hook build
  - gun build
  enabled_by:
  - pick potential
  - CC chain
  countered_by:
  - cleanse/dispel
  - mobility
  last_changed_patch: null
  notes: 'Creator: balanced, correctly not buffed.'
Calico:
  name: Calico
  role: mobile assassin
  archetypes:
  - mobile assassin
  tier: B
  trend: stable
  why: Above-average skirmisher, but the rerouted breakable timing (3m->5m) hits her
    early underground farm and the tempo meta does her no favors; still ~50% WR on
    a high pick rate.
  core_items:
  - Rapid Recharge
  - Echo Shard
  - Superior Stamina
  build_variants:
  - skirmish build
  enabled_by:
  - early farm
  - mobility
  countered_by:
  - later breakables
  - CC
  last_changed_patch: Minor Update - 07-28-2026
  notes: 'Creator: bottom of A, no nerf needed; the breakable change is described
    as more a Calico hit than a Rem one.'
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
Ivy:
  name: Ivy
  role: support/healer
  archetypes:
  - support/healer
  tier: A
  trend: falling
  why: Only slight Stone Form nerfs (radius 6->5.75m, T1 heal 7->6%) that the creator
    welcomed; she still owns the support slot at 53.7% WR with the best team-sustain
    and map control.
  core_items:
  - Healing Tempo
  - Healing Nova
  - Echo Shard
  - Capacitor
  build_variants:
  - heal support build
  - Echo Shard stone build
  enabled_by:
  - team sustain
  - map control ult
  countered_by:
  - anti-heal
  - burst
  last_changed_patch: Minor Update - 09-16-2026
  notes: 'Creator: underrated support whose buffs are noticeable on Drifter/Venator.'
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
Lash:
  name: Lash
  role: mobile initiator
  archetypes:
  - mobile assassin
  - initiator
  tier: S
  trend: rising
  why: The patch rebalanced him into stomp Lash (Ground Strike T3 scaling and per-meter
    damage up, gun falloff cut) and away from the gun build, which the creator calls
    healthy; he still has the game's highest pick rate (62%).
  core_items:
  - Mystic Shot
  - Recharging Rush
  - Headhunter
  - Superior Stamina
  build_variants:
  - stomp build
  - gun build
  enabled_by:
  - Ground Strike buffs
  - mobility + CC
  countered_by:
  - Flog heal nerf
  - anti-air/CC
  last_changed_patch: Minor Update - 09-16-2026
  notes: 'Creator: good at every stage, can build anything; wants the 10% base spirit
    resist removed.'
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
Mirage:
  name: Mirage
  role: split-push gun carry
  archetypes:
  - gun carry
  - split pusher
  tier: B
  trend: falling
  why: "The once-perma-broken split-pusher keeps his overloaded kit, but 07-28 Scarab/Dust\
    \ Devil nerfs plus a meta that punishes slow TP play leave him at 46.4% WR \u2014\
    \ punished by the meta, not the notes."
  core_items:
  - Echo Shard
  - Scourge
  - Inhibitor
  build_variants:
  - split-push build
  - Echo Shard tornado build
  enabled_by:
  - Echo Shard double tornado
  - map pressure
  countered_by:
  - tempo comps
  - CC/picks
  last_changed_patch: Minor Update - 07-28-2026
  notes: Oldest source called him a must-remove; the new data contradicts that at
    high rank.
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
Sinclair:
  name: Sinclair
  role: burst cast/steal
  archetypes:
  - burst caster
  - mobile assassin
  tier: C
  trend: stable
  why: "Inconsistent without a draft \u2014 only pops when he steals a strong kit,\
    \ and the Echo Shard bunny build is the lone zero-variance path; 48.4% WR on a\
    \ low pick rate."
  core_items:
  - Echo Shard
  - Superior Cooldown
  build_variants:
  - Echo Shard bunny build
  - kit-steal build
  enabled_by:
  - kit stealing
  - parry/bolt utility
  countered_by:
  - unfavorable matchups
  - no draft
  last_changed_patch: null
  notes: 'Creator: nothing much to say; unlikely to be rankable until drafting exists.'
Mina:
  name: Mina
  role: mobile spirit assassin
  archetypes:
  - mobile assassin
  - burst caster
  tier: C
  trend: falling
  why: "Dropped with the strong heroes and given no compensation; 47.2% WR on a 39.8%\
    \ pick rate says the overloaded kit no longer converts, so one buff could flip\
    \ her \u2014 she needs a rework instead."
  core_items:
  - Superior Stamina
  - Echo Shard
  - Mystic Reverb
  build_variants:
  - mobility burst build
  enabled_by:
  - mobility + damage
  - ult silence
  countered_by:
  - tempo comps
  - CC
  last_changed_patch: Minor Update - 07-28-2026
  notes: 'Creator: bottom of B/top C; small buff would make her broken again.'
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


## Win/pick-rate snapshot (last 14 days before this patch, ranked matches, high-rank filter)

hero | WR% | PR% | matches
Graves | 56.7 | 39.2 | 247426
Victor | 56.0 | 34.7 | 219180
Seven | 54.5 | 35.0 | 221235
Paige | 54.2 | 34.2 | 216208
Kelvin | 53.8 | 19.2 | 121289
Ivy | 53.7 | 30.2 | 190626
Warden | 53.6 | 41.6 | 262816
Mo & Krill | 52.6 | 33.5 | 211543
Dynamo | 52.0 | 30.6 | 192981
Celeste | 51.8 | 36.7 | 231604
Lash | 51.8 | 43.5 | 274611
Haze | 51.1 | 42.6 | 269050
Vindicta | 51.1 | 33.4 | 211038
Calico | 50.9 | 27.5 | 173869
Vyper | 50.8 | 20.2 | 127374
Wraith | 50.7 | 38.1 | 240649
Apollo | 50.7 | 27.5 | 173602
Drifter | 50.6 | 46.2 | 291348
Abrams | 50.6 | 33.7 | 212680
McGinnis | 49.9 | 17.4 | 109693
Lady Geist | 49.8 | 24.5 | 154776
Infernus | 49.2 | 45.5 | 287435
Viscous | 48.3 | 24.7 | 156217
Yamato | 48.2 | 24.1 | 151845
Rem | 48.0 | 40.3 | 254127
Billy | 47.9 | 34.8 | 219826
Grey Talon | 47.7 | 17.5 | 110220
Shiv | 47.6 | 32.6 | 206073
Holliday | 47.3 | 19.7 | 124297
Bebop | 47.1 | 49.2 | 310702
Paradox | 46.8 | 38.9 | 245347
The Doorman | 46.4 | 20.0 | 126408
Pocket | 45.8 | 26.4 | 166627
Mina | 45.2 | 41.6 | 262382
Sinclair | 45.2 | 17.8 | 112324
Venator | 44.7 | 38.7 | 244277
Silver | 44.7 | 22.1 | 139327
Mirage | 43.4 | 16.5 | 104327

## What to do

Produce an entry for **every hero in the knowledge base**, including heroes with no direct changes. For each hero combine:

- direct changes (kit, stats, talents) and their magnitude relative to how the hero is actually played (a nerf to an ability nobody maxes is minor);
- indirect effects from the item analysis (core items buffed/nerfed, build paths changed) and from the systems analysis (archetype up/down, tempo shift);
- the prior state: tier, trend, win rate. A hero at 54%+ win rate absorbing a moderate nerf is likely still strong; a hero at 47% taking the same nerf drops out.

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
