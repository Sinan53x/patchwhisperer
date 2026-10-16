# Task: item analysis

Patch: Paint the Town (2026-10-16)

## Systems analysis of this patch (already done)

{
 "systems_changed": [
  {
   "system": "Jungle / neutral camps (Haunts rework)",
   "change_summary": "Every neutral camp is replaced by nine new Haunt creature types with new behaviors (Specimen, Gutter Ghouls, Barrel Mimics, Past Dues, Stage Hands, Crabbage Pots, Festival Spirit, Shrooms, Underhands).",
   "driving_changes": [
    "Haunts: all neutral camps replaced by new creature types with new behaviors"
   ],
   "magnitude": "major",
   "effect_on_play": "Fixed jungle routes are dead — players must re-learn which camps pay and which punish, so map knowledge and AoE/sustain kits bank faster than memorized templates. Camp-fight shape (grouping, chasing, damage) is now a per-creature read rather than one known camp."
  },
  {
   "system": "Objectives (Bell Tower / Sunken Plaza)",
   "change_summary": "Two new district objectives: Bell Tower atop Chinatown (high soul concentration but rings a map-wide bell) and Sunken Plaza beneath the Plaza (strips stamina on descent and mutes outside sound).",
   "driving_changes": [
    "Bell Tower: new objective atop the Chinatown district; highly concentrated soul hotspot, but collecting it rings a bell heard across the map",
    "Sunken Plaza: new objective beneath the Plaza district main square; descending strips your stamina and mutes outside sound"
   ],
   "magnitude": "major",
   "effect_on_play": "Both pull telegraphed group fights to fixed hubs earlier, matching the existing Sunken Plaza/Bell Tower fight-gravity. Bell Tower taxes greed by broadcasting the farm; Sunken Plaza rewards a commit but the stamina-strip and muted audio make the exit a real risk."
  },
  {
   "system": "Bounty economy (Soul Bags)",
   "change_summary": "Kills now drop a contested Soul Bag you must secure before an ally takes it; last-hit rules apply to the bounty itself.",
   "driving_changes": [
    "Soul Bags: kills now drop a Soul Bag you must secure before an ally takes it — contested-last-hit rules now apply to the bounty itself"
   ],
   "magnitude": "moderate",
   "effect_on_play": "Kill income is no longer banked on the kill alone — the killer (or a faster teammate) must secure the bag, so fights extend and bounty income becomes slightly less reliable. Marginal nerf to clean 'secure the kill, bank guaranteed' burst patterns."
  },
  {
   "system": "Economy — Buff Containers",
   "change_summary": "Buff Containers now also roll Spirit Resist, Bullet Resist, Ability Range and Move Speed as permanent bonuses, not just the old range/resist pair.",
   "driving_changes": [
    "Buff Containers: revamped golden statues now also roll Spirit Resist, Bullet Resist, Ability Range, and Move Speed as permanent bonuses"
   ],
   "magnitude": "moderate",
   "effect_on_play": "Detouring for containers now pays off across more of a build, so off-lane routing and map-control roams gain value for every archetype; move speed and resists are worth contesting, raising the number of small skirmishes around pickups."
  },
  {
   "system": "Melee / breakables (Tough Crates)",
   "change_summary": "Tough Crates stay Heavy-Melee-gated and yield extra souls, confirming melee itemization as a farm prerequisite.",
   "driving_changes": [
    "Tough Crates: breakables that require a Heavy Melee to open; yield extra souls"
   ],
   "magnitude": "moderate",
   "effect_on_play": "Reinforces the heavy-melee frontline as the crate-economy king; gun-only and non-melee kits must buy into melee or concede that income, keeping the box-farm lead engine intact after the camp rework."
  },
  {
   "system": "Traversal / movement (Steam Vents, districts, pickups)",
   "change_summary": "Steam Vents grant invisibility plus regen while stood on, four off-lane districts add farm/fight routes, Healing Snacks are hidden heal pickups, and Sunken Plaza strips stamina on descent.",
   "driving_changes": [
    "Steam Vents: new terrain pickups granting invisibility and a small amount of regen while standing on them",
    "Districts: four off-lane areas added — Theater, Chinatown, Haunted Lot, Plaza",
    "Healing Snacks: new hidden pickups around the map that heal on grab",
    "Sunken Plaza: descending strips your stamina"
   ],
   "magnitude": "moderate",
   "effect_on_play": "Movement now carries a stealth/escape layer and stat detours, so repositioning and vision play matter more than raw lane presence; invisibility vents reward mobile assassins and vision counters, and healing snacks reward sustain-light kits."
  },
  {
   "system": "Parry",
   "change_summary": "Successfully parrying objectives no longer resets Parry cooldown.",
   "driving_changes": [
    "Parry: successfully parrying objectives no longer resets your Parry cooldown"
   ],
   "magnitude": "minor",
   "effect_on_play": "Kills the free parry chain at objective fights, so objective diving is harder to sustain and the T3-bullet-resist bodies that leaned on chained parries (Apollo, Mo & Krill) lose a small edge."
  },
  {
   "system": "Ability / Item activation",
   "change_summary": "Abilities and items now fire the instant the button is pressed instead of waiting for the next input window, lowering reaction latency globally.",
   "driving_changes": [
    "Ability/Item use: now fires the instant the button is pressed instead of waiting for the next input window"
   ],
   "magnitude": "moderate",
   "effect_on_play": "Combo and defensive-item timing tightens for every hero; burst and initiation windows land more cleanly and reactive saves (parry, defensive items) are more reliable, mildly favouring fast-cast kits over slow telegraphs."
  },
  {
   "system": "Corrupted items / The Broker",
   "change_summary": "Broker trades high-tier items for Corrupted versions with shared per-match random negatives, first shipment ~30 min then roughly every 15 min; Street Brawl now grants a Corrupted item after the Round 5 draft.",
   "driving_changes": [
    "Corrupted items: high-tier items can be exchanged for Corrupted versions with random negative attributes assigned per match; the positive/negative roll is identical for all players in a given game",
    "Street Brawl: now grants a Corrupted item after the item draft in Round 5"
   ],
   "magnitude": "major",
   "effect_on_play": "Adds a mid-late risk/reward conversion layer that is identical for everyone, keeping the ~30-min mark as the key scaling/stall window and rewarding leads that convert before the shared negatives bite."
  },
  {
   "system": "Sinner's Sacrifice",
   "change_summary": "Bonus now has variable timings instead of a fixed window.",
   "driving_changes": [
    "Sinner's Sacrifice: bonus now has variable timings instead of a fixed window"
   ],
   "magnitude": "minor",
   "effect_on_play": "Removes memorized-timer contesting of the sacrifice, so players must react to it and the objective becomes higher-variance and less reliably pre-farmed."
  },
  {
   "system": "Walkers",
   "change_summary": "Walkers no longer keep firing fireballs after dying.",
   "driving_changes": [
    "Walkers: no longer keep firing fireballs after dying"
   ],
   "magnitude": "minor",
   "effect_on_play": "Removes post-death chip damage, so lingering near a killed Walker to push the wave or take a fight is safer — a small quality-of-life buff to sieging and to holding a just-cleared lane."
  }
 ],
 "tempo_shift": {
  "direction": "toward_tempo",
  "confidence": 0.6,
  "why": "New early-mid soul hotspots (Bell Tower, Sunken Plaza) and contested Soul Bags push fights over income sooner while no comeback lever is added and the Broker's ~30-min window stays the only scaling stall. The shared Corrupted layer and Buff Container stat detours add map-wide risk/reward but do not add a comeback valve."
 },
 "archetype_effects": [
  {
   "archetype": "tank/frontline",
   "direction": "up",
   "magnitude": "moderate",
   "why": "Tough Crates keep heavy-melee income king and Buff Containers now roll Bullet/Spirit Resist as permanent bonuses; the objective-parry nerf is only a minor tax."
  },
  {
   "archetype": "mobile assassin",
   "direction": "up",
   "magnitude": "moderate",
   "why": "Steam Vents grant invisibility, districts add routes, and instant ability/item activation tightens pick and escape timing."
  },
  {
   "archetype": "burst caster",
   "direction": "up",
   "magnitude": "minor",
   "why": "Instant ability/item use cleans up combo windows, and Buff Containers now roll Ability Range as a permanent bonus."
  },
  {
   "archetype": "initiator",
   "direction": "up",
   "magnitude": "minor",
   "why": "Lower activation latency makes engage windows land more reliably across the new telegraphed hubs."
  },
  {
   "archetype": "gun carry",
   "direction": "neutral",
   "magnitude": "minor",
   "why": "Instant activation helps, but the crate economy stays melee-gated and Buff Containers roll defensive stats rather than gun stats."
  },
  {
   "archetype": "lanes bully",
   "direction": "neutral",
   "magnitude": "minor",
   "why": "Lane cadence is untouched and the income engine still lives off-lane in camps and district hubs."
  },
  {
   "archetype": "late scaler",
   "direction": "down",
   "magnitude": "minor",
   "why": "No comeback lever was added and new early-mid hotspots concentrate tempo fights, while the Broker window is unchanged."
  },
  {
   "archetype": "support/healer",
   "direction": "down",
   "magnitude": "minor",
   "why": "Healing Snacks and Steam Vent regen let sustain-light kits self-sustain, trimming reliance on dedicated healing."
  },
  {
   "archetype": "split pusher",
   "direction": "neutral",
   "magnitude": "minor",
   "why": "Districts open more routes but contested Soul Bags make bounty income less reliable, roughly cancelling out."
  },
  {
   "archetype": "poke/siege",
   "direction": "up",
   "magnitude": "minor",
   "why": "Walkers no longer fire after dying, making it safer to hold a just-cleared lane and press the wave."
  }
 ],
 "intent_read": "Valve is relaunching the City Never Sleeps map as the game's main content and re-spreading soul income across many contested, discoverable sources rather than one memorized route. The reworked Haunts, new district objectives, contested Soul Bags and permanent-stat Buff Containers push players into more telegraphed, fought-over economy moments, with the shared Corrupted-item layer standardizing late risk/reward across the lobby."
}

## Item changes in this patch (grouped by item)

Corrupted items:
  - [neutral] Corrupted items: new item tier obtained by exchanging a high-tier item at The Broker; each carries random negative attributes (same set for everyone in the match) with small variability in magnitude — a high-roll/high-risk slot that competes with normal completed items

## Knowledge base: the changed items (who buys them and why)

Corrupted items:
  name: Corrupted items
  role: "Late-game merchant tier unlocked by The Broker (~30 min, then ~every 15 min);\
    \ not a buildable slot \u2014 you convert a finished high-tier item for extra\
    \ stats plus match-wide random negative attributes."
  bought_by: []
  slot: "Merchant shipment (The Broker) \u2014 no Vitality/Weapon/Spirit slot."
  tier: null
  notes: 'Rolls are symmetric: identical for all players in a match, so the tier adds
    between-match variance, not intra-match advantage to whoever reaches The Broker
    first. It rewards teams that can bank souls and stall to ~30 min, running counter
    to this patch''s early-close economy. Read it at runtime, not in a build plan;
    low-confidence (first KB entry).'


## Knowledge base: heroes whose core_items or build_variants include a changed item

(none)

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
