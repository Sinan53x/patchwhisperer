# Task: per-hero analysis (hero batch)

Patch: {{patch_title}} ({{patch_date}})

## Systems analysis

{{stage1_json}}

## Item analysis

{{stage2_json}}

## Direct hero changes in this patch (grouped by hero; heroes not listed had no direct changes)

{{hero_changes}}

## Knowledge base: the heroes in this batch plus their matchup partners (pre-patch)

{{heroes_kb}}

## Win/pick-rate snapshot (last 14 days before this patch, ranked matches, high-rank filter)

{{snapshot}}

## Heroes to analyze in this call

{{batch_heroes}}

## What to do

Produce an entry for **each hero listed above, and only those heroes**. For each hero combine:

- direct changes (kit, stats, talents) and their magnitude relative to how the hero is actually played (a nerf to an ability nobody maxes is minor);
- indirect effects from the item analysis (core items buffed/nerfed, build paths changed) and from the systems analysis (archetype up/down, tempo shift);
- the prior state: tier, trend, win rate. A hero at 54%+ win rate absorbing a moderate nerf is likely still strong; a hero at 47% taking the same nerf drops out.
- **cross-hero effects**: changes to *other* heroes matter. If a hero who counters this one (see `matchups.loses_to`, `countered_by`) got stronger or gained a tool that specifically punishes this hero (anti-air, anti-heal, silence, grounding), that is an indirect nerf; if a counter got weaker, an indirect buff. Name the other hero and the mechanic.
- **builds, not just kits**: judge a change against the hero's actual `builds` (gun vs spirit, primary vs niche). A nerf to an item only the niche build buys is minor; a nerf to the primary build's core item is not.
- **map and objectives**: for content/map updates, judge how the kit interacts with the new soul sources and fight locations (camp clear speed and AoE vs grouped Haunts, heavy melee for Tough Crates, mobility between districts, verticality for Bell Tower, stamina for Sunken Plaza, sustain vs harder camps, invisibility/vision for Steam Vents, split-push vs more spread-out objectives).

`matchups` and `matchup_notes` are measured. Quote a matchup win rate only if it appears there, and never say a hero loses a matchup that is not in `loses_to`. Write for players: say "loses to", not "listed loss".

New heroes listed under direct changes but absent from the knowledge base: include them with `tier_before` "?", `in_notes` true, low `confidence`, and say the read is provisional.

## Reader corrections (authoritative)

{{corrections}}

## Creator sources published after this patch (optional corroboration; the notes, KB and snapshot remain primary — if a source contradicts them, say so and keep your own read)

{{creator_sources}}

For heroes with nothing relevant (no direct changes, no affected core items, archetype neutral) set direction "neutral", magnitude "none", and keep reasons empty. Do not pad.

`tier_after` is your call on the post-patch tier (S/A/B/C/D); keep `tier_before` from the KB (use "?" if unknown). Only move a tier when the reasons justify it. `confidence` reflects how sure you are about the direction, 0-1.

`verdict` answers one question for every hero: should someone who plays this hero keep playing them after this patch?

- `keep`: still a good pick; direct + indirect effects are neutral or positive, or negative but minor relative to the hero's standing.
- `watch`: real change in either direction whose size is uncertain; play but adapt (usually a build or timing change).
- `bench`: the hero lost what made them good (core build gutted, archetype hard-countered by a systems change, major kit nerf on a hero that was not over-performing).

## Change rows

`rows` is a list of scannable one-line changes for a phone screen. Give rows for **every hero with direct changes**; leave it empty for heroes without.

- `label`: 1-3 plain words naming what changed ("Channel time", "T3", "New interrupts", "Teamplay").
- Prefer `old` + `new` when the note gives before/after values; otherwise `text` of at most 8 words. Never both.
- `effect`: judged for the player of this hero: "good", "bad", or "neutral". A longer channel time is bad.
- `ability`: the exact ability name when the change applies to one.
- Merge lines that say the same thing. Keep every gameplay-relevant change. Never add anything not in the notes; every number in a row must come from the notes verbatim.

Example (Mirage's Traveler):

```json
{"label": "Channel time", "old": "2s", "new": "3s", "effect": "bad", "ability": "Traveler"}
{"label": "T3", "old": "-90s cooldown", "new": "Damage can't interrupt it", "effect": "good", "ability": "Traveler"}
{"label": "Base ability", "text": "Now includes a barrier (no scaling)", "effect": "good", "ability": "Traveler"}
```

## Reporting what the notes did

`change_kind` and `change_size` describe **only the hero's own note lines**, never items, systems or the meta. Those belong in `direction`, `indirect_reasons`, `tier_after` and `verdict`.

- `buff`: the lines clearly make the hero stronger. `nerf`: clearly weaker. `none`: no direct lines.
- `rework`: an ability works differently, not just with different numbers. Crowd control changing type, a talent swapped for a different effect, or a new or removed mechanic is a rework even when numbers around it improve.
- `adjusted`: trade-offs that roughly cancel, or only bug fixes.

Judge mechanical changes by what the ability **can no longer do**. A stun becoming an immobilize loses the stun's ability to interrupt channels, so that row is `bad` and it leads the `one_liner`, however good the longer duration looks. Never call a hero buffed while a core mechanic was taken away.

The `one_liner` leads with the biggest direct change. Any claim from items or systems names its cause. Do not state facts absent from the notes, the knowledge base or the corrections. A bug fix is `neutral` and labelled as a fix unless it clearly helps or hurts.

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
      "one_liner": "<= 20 words a player would actually say about this hero after the patch",
      "verdict": "keep|watch|bench",
      "change_kind": "buff|nerf|rework|adjusted|none",
      "change_size": "none|minor|moderate|major",
      "rows": [{"label": "1-3 words", "old": "before", "new": "after", "effect": "good|bad|neutral", "ability": "optional exact name"}]
    }
  ]
}
