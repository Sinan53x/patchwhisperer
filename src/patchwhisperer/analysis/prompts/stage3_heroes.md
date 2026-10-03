# Task: per-hero analysis (all heroes)

Patch: {{patch_title}} ({{patch_date}})

## Systems analysis

{{stage1_json}}

## Item analysis

{{stage2_json}}

## Direct hero changes in this patch (grouped by hero; heroes not listed had no direct changes)

{{hero_changes}}

## Knowledge base: current state of every hero (pre-patch)

{{heroes_kb}}

## Win/pick-rate snapshot (last 14 days before this patch, ranked matches, high-rank filter)

{{snapshot}}

## What to do

Produce an entry for **every hero in the knowledge base**, including heroes with no direct changes. For each hero combine:

- direct changes (kit, stats, talents) and their magnitude relative to how the hero is actually played (a nerf to an ability nobody maxes is minor);
- indirect effects from the item analysis (core items buffed/nerfed, build paths changed) and from the systems analysis (archetype up/down, tempo shift);
- the prior state: tier, trend, win rate. A hero at 54%+ win rate absorbing a moderate nerf is likely still strong; a hero at 47% taking the same nerf drops out.
- **cross-hero effects**: changes to *other* heroes matter. If a hero who counters this one (see `matchups.loses_to`, `countered_by`) got stronger or gained a tool that specifically punishes this hero (anti-air, anti-heal, silence, grounding), that is an indirect nerf; if a counter got weaker, an indirect buff. Name the other hero and the mechanic.
- **builds, not just kits**: judge a change against the hero's actual `builds` (gun vs spirit, primary vs niche). A nerf to an item only the niche build buys is minor; a nerf to the primary build's core item is not.
- **map and objectives**: for content/map updates, judge how the kit interacts with the new soul sources and fight locations (camp clear speed and AoE vs grouped Haunts, heavy melee for Tough Crates, mobility between districts, verticality for Bell Tower, stamina for Sunken Plaza, sustain vs harder camps, invisibility/vision for Steam Vents, split-push vs more spread-out objectives).

New heroes listed under direct changes but absent from the knowledge base: include them with `tier_before` "?", `in_notes` true, low `confidence`, and say the read is provisional.

## Reader corrections (authoritative)

{{corrections}}

## Creator sources published after this patch (optional corroboration; the notes, KB and snapshot remain primary — if a source contradicts them, say so and keep your own read)

{{creator_sources}}

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
