# Task: synthesis (the verdict and the meta thesis)

Patch: {{patch_title}} ({{patch_date}})
Change counts: {{change_counts}}

## Reader corrections (authoritative, overrides the knowledge base)

{{corrections}}

## Update summary

{{digest_summary}}

## Previous meta thesis (knowledge base, pre-patch)

{{meta_md}}

## Systems analysis

{{stage1_json}}

## Item analysis

{{stage2_json}}

## Hero analysis (only heroes with direction != neutral)

{{stage3_movers_json}}

## Creator sources published after this patch (optional corroboration; the notes, KB and snapshot remain primary — if a source contradicts them, say so and keep your own read)

{{creator_sources}}

## What to do

Write the verdict a strong player wants in the first 30 seconds.

1. **Patch size.** Classify: `major` (systems rework or many structural changes; content updates: map rework, new objectives, new heroes; the way games are played changes), `significant` (meaningful systems or economy moves plus broad tuning; the tier list will move), `minor` (tuning; a few heroes move a tier, no systems shift), `hotfix` (a handful of fixes/tweaks). Justify in one or two sentences naming the drivers. Change counts alone do not decide size; a 5-line economy change can be major.
2. **Headline.** One sentence, the thing to remember.
3. **Meta thesis.** State the previous thesis in one sentence, the new thesis in one or two, and whether this is a continuation, a shift, or a reversal. The thesis is about *how the game is won* (tempo vs scaling, which archetypes carry, what the fights look like), not a list of heroes.
4. **Winners and losers.** 3-5 each, ranked, with the driver. Include indirect movers where justified; mark them as such.
5. **Non-obvious calls.** 2-4 claims a casual reader of the notes would miss: unlisted heroes that moved, a "general" change that is really a targeted nerf, a build that died, a sleeper item. Each with a confidence.
6. **Uncertainties and what to watch.** What you are unsure about and what data would settle it in the first week.

7. **Biggest changes.** The 4-7 things a player must know before their next game, ranked by how much they change how you play. This is the first thing on the page, read in ten seconds by someone who will not read anything else.
   - The test: would a player do something different in their next game because of this? A hero who stops being playable, an item a build depended on, an objective that now works differently, a new way to win.
   - Mix heroes, items and systems as the patch warrants, including objectives such as the Mid-Boss. Do not fill a quota.
   - Leave out plain number trims. A 10 second longer ult cooldown or a 4% stronger pickup never belongs here, however many of them there are.
   - `subject` is the exact hero, item or system name as written in the analyses above.
   - `title` is at most 10 plain words a new player understands. `why` is one short sentence with the decisive number from the notes. Report numbers only as the notes state them.
   - `effect` is `up` if this is good for the subject or for players who use it, `down` if bad, `neutral` for a change in how it works.

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
  "what_to_watch": ["1 sentence each"],
  "biggest_changes": [{"kind": "hero|item|system", "subject": "exact name", "title": "at most 10 plain words", "why": "1 short sentence", "effect": "up|down|neutral"}]
}
