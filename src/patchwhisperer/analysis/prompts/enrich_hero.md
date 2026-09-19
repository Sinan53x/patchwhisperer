# Task: enrich one hero's knowledge-base entry

Hero: {{hero}}
As of: {{as_of_date}} (state after {{latest_patch_title}})

## Current entry (may be shallow or partly wrong)

{{hero_entry}}

## Abilities

{{abilities}}

## Item usage, last {{days}} days, ranked matches, high-rank filter (share = fraction of this hero's games where the item was bought; buy_min = average purchase time)

{{item_usage}}

## Matchups, same window (win rate of {{hero}} against each enemy; only pairs with enough games)

Beats: {{beats}}
Loses to: {{loses_to}}

## Win/pick rate

{{hero_snapshot}}

## What creators said about this hero (dated, newest first)

{{creator_claims}}

## Current tier list of all other heroes (for cross-hero reasoning)

{{tier_list}}

## Reader corrections (authoritative; if they contradict data or creators, follow them and say so in notes)

{{corrections}}

## Current meta thesis

{{meta_md}}

## What to do

Rewrite the entry so a strong player would recognise it as accurate. Concretely:

1. **Builds.** Derive the real builds from item usage plus creator claims. Cluster items into 1-3 builds (e.g. "gun build", "spirit build", "Dashfernus"). For each: damage type (gun|spirit|hybrid), its core items (only items with meaningful share; order by buy_min), how popular it is (primary|secondary|niche) based on share, and a one-line note (what it does, when to pick it). Items with high share and early buy_min are core; late buy_min items are luxury. If usage data contradicts a creator's claim, prefer the data and note the disagreement.
2. **core_items** = union of core items across primary and secondary builds.
3. **Matchups.** `beats` and `loses_to` from the data (hero names), plus any creator-stated counters. Then reason about *why* for the top 2-3 in each list in `matchup_notes`.
4. **Cross-hero effects.** Look at the tier list: which strong heroes' kits or common items specifically punish this hero (anti-air, anti-heal, silence, burst vs low HP) and which enable them? Record in `countered_by` / `enabled_by` (heroes, items, or systems), and let it inform the tier.
5. **Tier and trend.** Re-evaluate using win rate, pick rate, creator consensus (newest weighted most), matchups, and cross-hero effects. Explain in `why` (2-3 sentences, present tense). Do not restate the changelog.
6. **notes**: up to 3 short lines: disagreements resolved, low-confidence areas, changelog line for the last patch.

Use canonical hero and item names from the lists provided. Do not invent items.

## Output schema

{
  "role": "short label",
  "archetypes": ["from: gun carry, spirit carry, burst caster, tank/frontline, lane bully, late scaler, mobile assassin, support/healer, split pusher, initiator, poke/siege"],
  "tier": "S|A|B|C|D",
  "trend": "rising|stable|falling",
  "why": "2-3 sentences",
  "builds": [
    {"name": "string", "damage": "gun|spirit|hybrid", "core_items": ["..."], "popularity": "primary|secondary|niche", "notes": "1 sentence"}
  ],
  "core_items": ["..."],
  "matchups": {"beats": ["hero", "..."], "loses_to": ["hero", "..."]},
  "matchup_notes": "1-3 sentences",
  "enabled_by": ["..."],
  "countered_by": ["..."],
  "notes": "up to 3 lines",
  "confidence": 0.0
}
