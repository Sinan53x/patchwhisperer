# Task: update the knowledge base after this patch

Patch: {{patch_title}} ({{patch_date}})

## Synthesis

{{stage4_json}}

## Hero analysis (movers only)

{{stage3_movers_json}}

## Item analysis

{{stage2_json}}

## Current meta.md

{{meta_md}}

## Current hero entries (movers only)

{{heroes_kb_movers}}

## Current item entries (changed items only; may be empty for items not yet in the KB)

{{items_kb}}

## What to do

Produce the post-patch knowledge base state. This KB is read by the analyst on the *next* patch, so write it as durable state, not as a patch summary.

1. **meta.md**: rewrite the whole document in this structure (markdown, <= 400 words):
   - `# Meta state` line with `Last patch: {{patch_title}} ({{patch_date}})`
   - `## Thesis` — 2-4 sentences: how games are won right now (tempo vs scaling, fight shape, what archetypes carry).
   - `## Economy and systems` — bullets describing the current state of comeback, bounties, objectives, respawn, movement/slows, in present tense with current numbers where known.
   - `## Archetype standing` — one bullet per archetype in play: up/down/stable and why.
   - `## Watchlist` — 3-6 bullets: heroes/items/systems that are uncertain and should be checked against data.
   - `## Recent history` — keep at most 5 bullets, newest first, one line per patch: "{{patch_title}}: <headline>". Carry forward existing bullets from the current meta.md, drop the oldest beyond 5.
2. **hero_updates**: for each mover, the fields that changed. Allowed fields: role, archetypes, tier, trend, why, core_items, builds (full replacement list of {name, damage, core_items, popularity, notes}), matchups ({beats, loses_to}), enabled_by, countered_by, notes. When an item change kills or creates a build, update `builds`, not just `notes`. When another hero's change alters a matchup, update `matchups`. Set `last_changed_patch` to "{{patch_title}}" for heroes that had direct changes. `why` is 1-2 sentences of present-tense state ("strong because X; weak to Y"), not a changelog. `notes` may hold a short changelog line (keep the last 3 lines, newest first). Do not touch heroes that did not move.
3. **item_updates**: for each changed item, the fields that changed. Allowed fields: role, bought_by, slot, tier, notes. `bought_by` must list hero names that build it as core or common situational pick, updated for this patch.
4. **change_log**: one line per KB edit you made, for the human to skim.

Tier is one of S/A/B/C/D. Trend is rising/stable/falling.

## Output schema

{
  "meta_md": "full markdown text",
  "hero_updates": {"Hero Name": {"tier": "A", "trend": "falling", "why": "...", "core_items": ["..."], "last_changed_patch": "...", "notes": "..."}},
  "item_updates": {"Item Name": {"role": "...", "bought_by": ["..."], "notes": "..."}},
  "change_log": ["Hero Name: tier S -> A (Card Trick heal nerfs + Veil Walker loss)", "..."]
}
