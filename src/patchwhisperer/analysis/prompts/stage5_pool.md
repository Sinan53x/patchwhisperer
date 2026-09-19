# Task: verdicts for the reader's hero pool

Patch: {{patch_title}} ({{patch_date}})

## Synthesis

{{stage4_json}}

## Hero analysis entries for the pool heroes

{{stage3_pool_json}}

## Item analysis entries that mention a pool hero

{{stage2_pool_json}}

## Knowledge base entries for the pool heroes

{{heroes_kb_pool}}

## The reader's pool

{{pool}}

## What to do

For each hero in the pool give a verdict a player can act on tonight:

- `keep`: still a good pick; direct + indirect effects are neutral or positive, or negative but minor relative to the hero's standing.
- `watch`: real change in either direction whose size is uncertain; play but adapt (usually a build or timing change).
- `bench`: the hero lost what made them good (core build gutted, archetype hard-countered by systems change, major kit nerf on a hero that was not over-performing).

Explain the direct effects and the indirect effects separately so the reader can see the indirect ones (they are what they would miss). Give concrete build adjustments (item to drop, item to add, talent order) only if the analysis supports them; otherwise leave the list empty. Keep every field short; the whole card must read in 20 seconds.

## Output schema

{
  "verdicts": [
    {
      "hero": "name",
      "verdict": "keep|watch|bench",
      "one_liner": "<= 20 words",
      "direct": "1-2 sentences on the hero's own changes; 'No direct changes.' if none",
      "indirect": "1-2 sentences on item/system effects; 'No meaningful indirect effects.' if none",
      "build_adjustments": ["short imperative sentences"],
      "confidence": 0.0
    }
  ]
}
