# Task: first evaluation of a newly released hero

Hero: {{hero}}
Date: {{today}}

## Kit (from game data; descriptions are the in-game tooltips)

{{kit}}

## Early ranked data (first days after release; inflated by novelty, one-tricks and unfamiliar opponents — treat as weak evidence)

{{early_stats}}

## Release announcement

{{release_post}}

## Current meta thesis and map state

{{meta_md}}

## Current tier list (for cross-hero reasoning)

{{tier_list}}

## Reader corrections (authoritative)

{{corrections}}

## What creators have said about this hero (may be empty)

{{creator_claims}}

## Other announced heroes not yet released

{{upcoming}}

## Item names in the game (canonical spelling; do not invent items)

{{item_names}}

## What to do

Produce the first knowledge-base entry and a short reader card for this hero. You have the kit, not months of data, so reason from mechanics: what the abilities do together, the power pattern (lane bully, scaler, teamfight, pick, split push), what the hero needs to function (farm, setup, peel) and what shuts it down (specific heroes, items such as anti-heal, silence, knockdown, Plated Armor, Phantom Strike). Then place it in the *current* meta and map (see thesis and map state): which objectives, farm sources and fight shapes it exploits or struggles with, and which strong heroes it threatens or is threatened by. Use the popular-items data to describe the builds people are actually running, and judge whether they make sense.

Keep the KB entry in the same shape as other heroes. Tier is provisional: pick the tier the kit and early signals justify and set `confidence` <= 0.5. In `notes` say what would change your mind within a week.

The card is what a player reads in 20 seconds: headline, 3-5 kit bullets, one or two sentences on meta fit, who it beats and who beats it, build read, provisional tier with confidence, and 2-3 things to watch before the 7-day data check-in.

## Output schema

{
  "enrichment": {
    "role": "short label",
    "archetypes": ["from: gun carry, spirit carry, burst caster, tank/frontline, lane bully, late scaler, mobile assassin, support/healer, split pusher, initiator, poke/siege"],
    "tier": "S|A|B|C|D",
    "trend": "rising|stable|falling",
    "why": "2-3 sentences, present tense",
    "builds": [{"name": "string", "damage": "gun|spirit|hybrid", "core_items": ["..."], "popularity": "primary|secondary|niche", "notes": "1 sentence"}],
    "core_items": ["..."],
    "matchups": {"beats": ["hero"], "loses_to": ["hero"]},
    "matchup_notes": "1-3 sentences",
    "enabled_by": ["..."],
    "countered_by": ["..."],
    "notes": "up to 3 lines",
    "confidence": 0.0
  },
  "card": {
    "headline": "<= 20 words",
    "kit_read": ["3-5 bullets"],
    "meta_fit": "1-2 sentences",
    "threatens": ["Hero — why", "..."],
    "threatened_by": ["Hero or item — why", "..."],
    "build_read": "1-2 sentences",
    "provisional_tier": "S|A|B|C|D",
    "confidence": 0.0,
    "what_to_watch": ["2-3 items"]
  }
}
