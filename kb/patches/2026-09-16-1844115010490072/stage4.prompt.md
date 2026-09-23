# Task: synthesis (the verdict and the meta thesis)

Patch: Minor Update - 09-16-2026 (2026-09-16)
Change counts: General 17, Items 36, Heroes 69, total 122

## Previous meta thesis (knowledge base, pre-patch)

# Meta state
Last patch: Minor Update - 09-16-2026 (2026-09-16)

## Thesis
The 09-16 patch finished what the 07-30 comeback rework started: it gutted comeback souls and early Unstable Rift generosity, so winning lane now actually wins the game. Tempo beats scaling. Early snowballers and mobile bruisers (Paige, Apollo, Silver, Yamato, Vindicta, Holliday, Lash, Haze) rise; late scalers and flyers (Celeste, Warden, Wraith) fall. The old "overloaded DLC" S-tiers (Mirage, Venator, Doorman, Pocket) keep their kits but sit at ~46% WR — the meta stopped rewarding them.

## Economy and systems
Comeback bounty trimmed and extra comeback souls partly rerouted to the two lowest-econ players via tick gold, killing the fed AFK farmer. Guardian bounty +10%, Walker +5%, objective share 30->25%. Rift resist is now 10% +1%/min (cap 40% at 30m) instead of a flat 35% — early rift fights are real fights. Respawn at 20m 35->38s. Stuns/parry pause reload instead of resetting; dashes and light melee no longer break gun cycle time (Silver/Abrams smoothing); slows -20% globally but now hit air drag at 35% (flyers down, slow-as-CC up).

## Archetype standing
Early tempo and mobile frontline lead; late scalers lose their safety net. Tanks stay fine (Abrams/Dynamo/Mo) — core tank items untouched. Supports hold value (Ivy 53.7%, Paige rising) but healing items were trimmed (Radiant Regeneration, Restorative Locket).

## Watchlist
- Silver: Weighted Bola acts as Phantom Strike, plus +health/+sprint and the gun-cycle change. Biggest winner.
- Apollo: absent from notes, best snowballer — "super buffed" by tempo.
- Celeste: 7 nerfs plus item/scaling/air-drag hits; her 54.6% WR is a lagging pre-patch number.
- Veil Walker buyers (Holliday, Warden): item lost Sprint Boots and movespeed-on-break.

## Recent history
07-30 added Ranked Mode. 07-09/07-28 item and hero tuning; 08-12 McGinnis/Apollo; 08-22 Celeste; 09-16 tempo patch. The 07-16 creator read framed the game as a stat-check with S-tier DLC kits; current data (those kits mid at high rank) and the tempo patch are the newer, authoritative state. Snapshot is 14 days and mostly pre-patch, so treat its WRs as baseline, not post-patch.

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

## Hero analysis (only heroes with direction != neutral)

[
 {
  "hero": "Seven",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [],
  "indirect_reasons": [
   "Hollow Point resist-shred 9->10% buffs his core T2 gun slot.",
   "Gun-carry archetype up from the dash/no-pause gun-cycle change.",
   "Tunnel breakables delayed 3m->5m slow his early solo farm."
  ],
  "build_changes": [],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Early-gun shred buff lands, but delayed tunnel farm and tempo divers still cap him."
 },
 {
  "hero": "Vindicta",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.6,
  "direct_reasons": [],
  "indirect_reasons": [
   "Hollow Point resist-shred buff hits her core first-gun slot.",
   "Tempo economy (comeback souls cut) suits her early-lead playstyle.",
   "Poke/siege archetype down via air-drag slows, a soft offset."
  ],
  "build_changes": [],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Tempo patch keeps Vindicta in A; the shred buff makes her lane pick stronger."
 },
 {
  "hero": "Lady Geist",
  "in_notes": true,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.7,
  "direct_reasons": [
   "Life Drain T3 spirit scaling +0.3->+0.45 boosts her ult heal/drain.",
   "Essence Bomb T3 damage +26%->30% raises her burst.",
   "Decay DPS down/duration up suits her sustained-brawl anti-heal slot."
  ],
  "indirect_reasons": [
   "Spirit-carry archetype down from removed comeback/Rift levers."
  ],
  "build_changes": [],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Direct buffs on an already-rising pick; she stays a top spirit bruiser."
 },
 {
  "hero": "Abrams",
  "in_notes": true,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.6,
  "direct_reasons": [
   "Infernal Resilience T3 heal +8%->+9% is a small sustain bump.",
   "Seismic Impact T3 Unstoppable 6s->5s is a real ult-window nerf."
  ],
  "indirect_reasons": [
   "Dash/melee no longer pausing gun cycle lets him weave shots between punches.",
   "Fortitude and Decay both buffed, his core brawler items."
  ],
  "build_changes": [],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Tiny numbers up, gun-cycle smoothing helps, but anti-heal meta keeps him B."
 },
 {
  "hero": "Wraith",
  "in_notes": true,
  "direction": "down",
  "magnitude": "moderate",
  "confidence": 0.7,
  "direct_reasons": [
   "Card Trick heart heal 75->60 and its spirit scaling 0.75->0.5 cut her sustain.",
   "Card Trick Diamond resist-shred -8%->-7% (and T3 -5%->-4%) weakens her debuff.",
   "Full Auto spirit damage per bullet 0.03->0.045 is a small compensation."
  ],
  "indirect_reasons": [
   "Plated Armor now blocks Full Auto's on-hit spirit damage \u2014 a direct counter.",
   "Slowing Hex cooldown 27->29s trims her CC-build uptime.",
   "Late-scaler archetype down with comeback souls removed."
  ],
  "build_changes": [
   "De-prioritize Card Trick maxing; lean Full Auto gun build over CC build."
  ],
  "tier_before": "B",
  "tier_after": "C",
  "one_liner": "Card Trick gutted plus Plated Armor counter; Wraith slides out of B."
 },
 {
  "hero": "Paradox",
  "in_notes": true,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.65,
  "direct_reasons": [
   "Kinetic Carbine min damage multiplier 25%->10% cuts her quick-scope poke.",
   "Carbine min multiplier no longer increased by T3, removing a poke-scaling path."
  ],
  "indirect_reasons": [
   "Slowing Hex cooldown 27->29s trims her pick-engage frequency.",
   "Global slow -20% reduces lockdown, offset by new anti-air on Slowing Hex."
  ],
  "build_changes": [
   "Lean on Echo Shard bomb over Carbine poke."
  ],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Carbine poke trimmed; still a strong bomb-pick initiator, just less oppressive."
 },
 {
  "hero": "Dynamo",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.6,
  "direct_reasons": [],
  "indirect_reasons": [
   "Diviner's Kevlar now grants +10% ultimate CDR, a core item for his ult build.",
   "Tempo meta converts won lanes into picks, his win condition."
  ],
  "build_changes": [
   "Diviner's Kevlar is now a stronger buy for faster ult cycles."
  ],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Ult-initiator gets a Kevlar CDR bump on top of a meta that loves his picks."
 },
 {
  "hero": "Haze",
  "in_notes": true,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.65,
  "direct_reasons": [
   "Fixation headshot stacks +2->+3 raises her stacking damage.",
   "Fixation T3 weapon scaling 0.0003->0.00035 adds late gun scaling."
  ],
  "indirect_reasons": [
   "Gun-carry archetype up from the gun-cycle/reload changes.",
   "Plated Armor's on-hit fix is a soft counter to her on-hit builds."
  ],
  "build_changes": [
   "Gun Haze with Fixation maxing is clearly the build over Echo Shard sleep."
  ],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Fixation buffs make gun Haze the play in a tempo meta she likes."
 },
 {
  "hero": "Holliday",
  "in_notes": true,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.6,
  "direct_reasons": [
   "Health per boon 41->43 adds lane durability.",
   "Crackshot T2 now applies -6% bullet resist for 5s, real pick damage.",
   "Bounce Pad lasso extension +1s->+1.25s improves her catch."
  ],
  "indirect_reasons": [
   "Veil Walker nerf removes a core enabler (Sprint Boots component lost).",
   "Tempo economy rewards her post-20 pick play."
  ],
  "build_changes": [
   "Consider a gun-hybrid Crackshot build; Veil Walker is now a worse slot."
  ],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Direct buffs and tempo favor her, but the Veil Walker strip bites."
 },
 {
  "hero": "Calico",
  "in_notes": false,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [],
  "indirect_reasons": [
   "Tunnel breakables spawn/respawn 3m->5m delays her early underground farm.",
   "Mobile-assassin archetype up but her power is early-farm dependent."
  ],
  "build_changes": [],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Breakable timing pushes back her early farm; a quiet nerf to a ~50% skirmisher."
 },
 {
  "hero": "Grey Talon",
  "in_notes": false,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.4,
  "direct_reasons": [],
  "indirect_reasons": [
   "Hollow Point shred buff helps his core slot.",
   "Poke/siege archetype down via new air-drag slows on flyers/airborne poke.",
   "47.7% WR pre-patch with no compensation."
  ],
  "build_changes": [],
  "tier_before": "C",
  "tier_after": "C",
  "one_liner": "Item buff can't fix a C-tier poke carry the tempo meta punishes."
 },
 {
  "hero": "Mo & Krill",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.55,
  "direct_reasons": [],
  "indirect_reasons": [
   "Fortitude regen buff and Decay duration buff hit his core frontline items.",
   "Tank/frontline and early-brawl archetype favored by the tempo shift."
  ],
  "build_changes": [],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Quietly winning tank gets small item help in a meta that rewards minute-one brawls."
 },
 {
  "hero": "Shiv",
  "in_notes": true,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.65,
  "direct_reasons": [
   "Alt fire base damage +4% and per-boon +0.2->+0.24 boost his sustained shred.",
   "Serrated Knives at full rage now deals 3.5% current HP on impact instead of ricocheting."
  ],
  "indirect_reasons": [
   "Tankbuster current-HP 8%->7.5% is a small trim to his anti-tank slot.",
   "Fortitude regen buff helps his bruiser builds."
  ],
  "build_changes": [],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Current-HP knives plus alt-fire buffs keep Shiv shredding the HP pools the patch inflates."
 },
 {
  "hero": "Ivy",
  "in_notes": true,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.6,
  "direct_reasons": [
   "Stone Form radius 6m->5.75m and T1 heal 7%->6% trim her survivability tool."
  ],
  "indirect_reasons": [
   "Support archetype neutral; no item economy lever against her."
  ],
  "build_changes": [],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Small Stone Form nerf won't move the support queen off the top slot."
 },
 {
  "hero": "Warden",
  "in_notes": true,
  "direction": "down",
  "magnitude": "major",
  "confidence": 0.8,
  "direct_reasons": [
   "Bullet damage per boon 0.28->0.25 and fire-rate spirit scaling 0.25->0.21 cut his carry damage.",
   "Alchemical Flask range and speed reduced 30%, gutting his catch/farm.",
   "Willpower T3 spirit scaling +2.7->+2.1 and debuff resist 40%->30% nerf his kit."
  ],
  "indirect_reasons": [
   "Mercurial Magnum scaling 0.49->0.38 and Spiritual Overflow triple-nerf remove his proc build.",
   "Veil Walker stripped (lost Sprint Boots) removes his escape enabler.",
   "Plated Armor now blocks Mercurial on-hit spirit damage, a hard counter.",
   "Late-scaler archetype down with comeback souls removed."
  ],
  "build_changes": [
   "Proc/on-hit Warden (Mercurial + Spiritual Overflow) is dead; pivot to pure silence-cage utility or drop."
  ],
  "tier_before": "B",
  "tier_after": "C",
  "one_liner": "Warden's carry build deleted on all sides \u2014 a four-item pile-on; cage only."
 },
 {
  "hero": "Yamato",
  "in_notes": true,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.7,
  "direct_reasons": [
   "Crimson Slash T3 now adds +0.4 heal spirit scaling.",
   "Flying Slash light-melee scaling 1.0->1.2 raises her burst."
  ],
  "indirect_reasons": [
   "Tankbuster 8%->7.5% is a small trim on her anti-tank slot.",
   "Mobile-assassin and tempo archetypes up."
  ],
  "build_changes": [],
  "tier_before": "S",
  "tier_after": "S",
  "one_liner": "More buffs atop an S-tier pick; expect her pick rate to climb further."
 },
 {
  "hero": "Viscous",
  "in_notes": true,
  "direction": "down",
  "magnitude": "moderate",
  "confidence": 0.7,
  "direct_reasons": [
   "The Cube cast range 26m->20m badly weakens his signature rescue.",
   "Puddle Punch cooldown 21s->24s cuts his dueling frequency.",
   "Alt fire damage growth -10% and Splatter T1 +2m->+1.5m trim his damage.",
   "Splatter detonation cooldown 0.15->0.12 and Goo Ball T3 +0.2 spirit scaling are partial offsets."
  ],
  "indirect_reasons": [
   "Tank/enabler archetype roughly neutral in the tempo shift."
  ],
  "build_changes": [],
  "tier_before": "B",
  "tier_after": "C",
  "one_liner": "Cube range and Puddle Punch nerfs hit his identity; only the ball buff helps."
 },
 {
  "hero": "Pocket",
  "in_notes": false,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [],
  "indirect_reasons": [
   "Spirit-carry and burst-caster archetypes down/neutral in the tempo shift.",
   "Fortitude regen buff is his only item-side help; 45.8% WR pre-patch."
  ],
  "build_changes": [],
  "tier_before": "B",
  "tier_after": "B",
  "one_liner": "Cloak assassin still wants long fights the tempo meta doesn't allow."
 },
 {
  "hero": "Vyper",
  "in_notes": true,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.6,
  "direct_reasons": [
   "Slither T3 barrier duration 5s->4s trims her defensive window.",
   "Petrifying Bola cooldown 105s->115s raises her ult timer."
  ],
  "indirect_reasons": [
   "Hollow Point shred buff helps her core gun slot.",
   "Gun-carry archetype up; still coin-flip on enemy CC."
  ],
  "build_changes": [],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Two small nerfs, one item buff; still the top-WR coin-flip carry."
 },
 {
  "hero": "Mina",
  "in_notes": false,
  "direction": "down",
  "magnitude": "minor",
  "confidence": 0.45,
  "direct_reasons": [],
  "indirect_reasons": [
   "Mobile-assassin archetype up, but she has no kit change to convert it.",
   "45.2% WR on 41.6% pick rate pre-patch, falling."
  ],
  "build_changes": [],
  "tier_before": "C",
  "tier_after": "C",
  "one_liner": "No changes given to a falling assassin; still needs a rework."
 },
 {
  "hero": "Drifter",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.55,
  "direct_reasons": [],
  "indirect_reasons": [
   "Toxic Bullets scaling buff and Decay duration buff hit his core anti-heal items.",
   "Fortitude regen buff helps his melee-bruiser brawls.",
   "Melee/bruiser archetype favored by the tempo shift."
  ],
  "build_changes": [],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Blind-pickable bruiser gets item tailwinds in a brawl-friendly patch."
 },
 {
  "hero": "Venator",
  "in_notes": true,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.6,
  "direct_reasons": [
   "Ira Domini now works with Ricochet (all shots bounce) and Split Shot (3 bolts) \u2014 real late damage.",
   "Weakening Headshot shred -13%->-12% trims his core item slightly."
  ],
  "indirect_reasons": [
   "Hollow Point shred buff helps his first-gun slot.",
   "Tempo meta and his 44.7% WR still work against his 'no weak point' read."
  ],
  "build_changes": [
   "Ricochet/Split Shot ult builds are now live; keep Weakening Headshot despite the trim."
  ],
  "tier_before": "A",
  "tier_after": "A",
  "one_liner": "Ult gains ricochet and split shot, but the data still says he doesn't convert."
 },
 {
  "hero": "Paige",
  "in_notes": true,
  "direction": "up",
  "magnitude": "major",
  "confidence": 0.75,
  "direct_reasons": [
   "Heavy Melee spirit scaling 0.3->0.45 is a large damage buff.",
   "Captivating Read T1 cooldown -11s->-14s and T3 +1m->+2m improve her engage.",
   "Rallying Charge collision fix removes clunk."
  ],
  "indirect_reasons": [
   "Restorative Locket heal/boon 0.5->0.45 and range 35->32m trims her sustain item.",
   "Slowing Hex cd 27->29s is a small tax, offset by new anti-air slow on flyers.",
   "Lane-bully/support archetypes up; tempo meta rewards her lane win."
  ],
  "build_changes": [
   "Keep Slowing Hex \u2014 its anti-air slow now punishes flyers she was buffed to beat."
  ],
  "tier_before": "S",
  "tier_after": "S",
  "one_liner": "Buff-stacked lane-winning support; still the patch's clearest S-tier winner."
 },
 {
  "hero": "Billy",
  "in_notes": false,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.6,
  "direct_reasons": [],
  "indirect_reasons": [
   "Lifestrike melee heal 100+1.5->120+1.75 and 30%->35% is effectively a Billy buff.",
   "Lifestrike's 48% slow now drags flyers out of the air, new anti-air CC.",
   "Decay duration buff and Fortitude regen buff hit his frontline items."
  ],
  "build_changes": [
   "Lifestrike now doubles as anti-air lockdown; value it over pure healing slots."
  ],
  "tier_before": "S",
  "tier_after": "S",
  "one_liner": "Lifestrike buff + new anti-air slow feed an already-dominant frontline."
 },
 {
  "hero": "Graves",
  "in_notes": true,
  "direction": "up",
  "magnitude": "minor",
  "confidence": 0.5,
  "direct_reasons": [
   "Health per boon 33->35 adds early durability."
  ],
  "indirect_reasons": [
   "Toxic Bullets scaling buff and Fortitude regen buff help her item path.",
   "Gun-carry archetype up, but her 56.7% snapshot WR is a lagging pre-patch read."
  ],
  "build_changes": [],
  "tier_before": "C",
  "tier_after": "C",
  "one_liner": "Small health/boon plus item buffs, but her awful base stats still cap her."
 },
 {
  "hero": "Apollo",
  "in_notes": false,
  "direction": "up",
  "magnitude": "moderate",
  "confidence": 0.65,
  "direct_reasons": [],
  "indirect_reasons": [
   "Restorative Locket heal/boon 0.5->0.45 and range 35->32m nerfs his sustain item.",
   "Tempo economy (comeback souls cut, objectives up) is exactly his lane-bully snowball playstyle.",
   "Initiator/lane-bully archetypes up in the tempo shift."
  ],
  "build_changes": [],
  "tier_before": "S",
  "tier_after": "S",
  "one_liner": "Absent from notes but the archetype winner; only his Locket slot takes a trim."
 },
 {
  "hero": "Silver",
  "in_notes": true,
  "direction": "up",
  "magnitude": "major",
  "confidence": 0.8,
  "direct_reasons": [
   "Health per boon 28->31 and sprint speed 1.5->2.5 are big stat buffs.",
   "Weighted Bola now increases gravity and interrupts flying abilities (Phantom-Strike rules) \u2014 a new pick tool.",
   "Dashes/light melee no longer pause gun cycle, directly boosting her high-cycle gun.",
   "Boot Kick and Entangling Bola now only target heroes/objectives, removing wasted hits."
  ],
  "indirect_reasons": [
   "Hollow Point shred buff and Fortitude regen buff hit her core slots.",
   "Diviner's Kevlar +10% ult CDR helps her existing buy.",
   "Gun-carry and tank archetypes both up."
  ],
  "build_changes": [
   "Weighted Bola is now a core grounded-interrupt pick; build around gun-tank with Diviner's Kevlar."
  ],
  "tier_before": "S",
  "tier_after": "S",
  "one_liner": "The patch's biggest winner headlined by a Phantom-Strike-style grounded Bola."
 },
 {
  "hero": "Celeste",
  "in_notes": true,
  "direction": "down",
  "magnitude": "major",
  "confidence": 0.8,
  "direct_reasons": [
   "Stamina cooldown 5->5.3, Light Eater spirit lifesteal 20%->18%, Dazzling Trick cd 34s->38s.",
   "Shining Wonder radius 16.5m->15.5m, T3 bounces +8->+6, Radiant Daggers T2 +80->+70, Light Eater T3 +25->+22."
  ],
  "indirect_reasons": [
   "Slows now affect air drag by 35%, punishing her flying kit.",
   "Spirit-carry archetype down with comeback/Rift levers removed.",
   "Paige's rise and the anti-scaling tilt squeeze her slot."
  ],
  "build_changes": [],
  "tier_before": "A",
  "tier_after": "B",
  "one_liner": "Nerfed seven ways plus air-drag slows on a flyer; drops out of A."
 }
]

## What to do

Write the verdict a strong player wants in the first 30 seconds.

1. **Patch size.** Classify: `major` (systems rework or many structural changes; the way games are played changes), `significant` (meaningful systems or economy moves plus broad tuning; the tier list will move), `minor` (tuning; a few heroes move a tier, no systems shift), `hotfix` (a handful of fixes/tweaks). Justify in one or two sentences naming the drivers. Change counts alone do not decide size; a 5-line economy change can be major.
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
