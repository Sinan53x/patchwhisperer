# Task: build the initial knowledge base

Today's game state date: {{as_of_date}}. The most recent patch is {{latest_patch_title}} ({{latest_patch_date}}). Build the KB describing the state **after** that patch.

## Distilled creator sources (newest first; older tier lists show trajectory, the newest source is the most authoritative)

{{sources_json}}

## Recent patch notes (newest first, parsed changes grouped by entity)

{{patches_json}}

## Win/pick-rate snapshot (last 14 days, ranked, high-rank filter)

{{snapshot}}

## Heroes that must all have an entry

{{hero_names}}

## Item names in the game (for canonical spelling)

{{item_names}}

## What to do

Synthesize one coherent current state. Where sources disagree, prefer the newer source and the data, and record the disagreement in `notes`. Where a hero has no creator coverage, infer from the snapshot and recent patch notes and set a low-confidence `why` that says so.

1. **meta_md** in exactly the structure used by the KB (see below), <= 550 words.
2. **heroes**: an entry for every hero listed. `role` is a short label (e.g. "gun carry", "spirit burst caster", "tank initiator"). `archetypes` uses this vocabulary: gun carry, spirit carry, burst caster, tank/frontline, lane bully, late scaler, mobile assassin, support/healer, split pusher, initiator, poke/siege. `core_items` 3-6 canonical item names the hero almost always builds. `build_variants` short labels ("gun build", "spirit ult build"). `enabled_by` items or systems that make the hero good right now; `countered_by` heroes/items that beat them. `why` present-tense 1-2 sentences. `trend` from the trajectory across sources.
3. **items**: entries for every item that appears in any hero's `core_items` or `build_variants`, plus every item touched in the recent patches. `bought_by` lists heroes that build it.

meta.md structure:
```
# Meta state
Last patch: <title> (<date>)

## Thesis
## Economy and systems
## Map — current map state in present tense: lanes/districts, objectives with timings and values where known, farm sources (Haunt tiers, crates/boxes, Sinner's Sacrifice variants, Buff Containers), pickups (Healing Snacks, Steam Vents), side asymmetry, key routes. Keep it when nothing changed.
## Archetype standing
## Watchlist
## Recent history
```

## Output schema

{
  "meta_md": "full markdown",
  "heroes": {"Hero Name": {"name": "Hero Name", "role": "...", "archetypes": ["..."], "tier": "S|A|B|C|D", "trend": "rising|stable|falling", "why": "...", "core_items": ["..."], "build_variants": ["..."], "enabled_by": ["..."], "countered_by": ["..."], "last_changed_patch": "title or null", "notes": "..."}},
  "items": {"Item Name": {"name": "Item Name", "role": "...", "bought_by": ["..."], "slot": "Weapon|Vitality|Spirit|null", "tier": 1, "notes": "..."}}
}
