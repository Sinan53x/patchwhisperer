# Task: distill a creator video transcript into knowledge-base claims

Creator: {{author}}
Video: {{title}} ({{video_id}}), published {{published}}
Known patch context: {{patch_context}}

## Transcript (auto-captions, may contain errors; hero and item names may be misspelled)

{{transcript}}

## On-screen content transcribed by a human (tier-list placements and overlays shown in the video; authoritative over the spoken audio when they disagree)

{{visual_notes}}

## What to do

Extract what this creator believes about the game state, as dated, attributed claims. Fix obvious caption misspellings of hero/item names using this list: {{hero_names}}. Ignore banter, sponsor reads, and anything not about game state.

Capture:
1. **Meta thesis** as the creator sees it (tempo vs scaling, what wins, what the fights look like), 2-4 sentences.
2. **Hero claims**: per hero mentioned with a real opinion: tier (S/A/B/C/D if the creator ranks; else null), direction (rising/stable/falling/null), the reason in the creator's words paraphrased, and core items or builds mentioned. Merge visual tier placements from the on-screen transcription into `hero_claims.tier`.
3. **Item claims**: per item with an opinion: standing (strong/weak/niche), who buys it, why.
4. **Map claims**: claims about the map, objectives, farm routes, neutrals, pickups or economy: topic, the claim, and any numbers stated.
5. **Reasoning patterns**: 2-5 short examples of *how* the creator reasons from a change to a consequence (e.g. "frames X as a general change but it is a nerf aimed at Y's build"). These are used as exemplars of analysis style.
6. **Patch-specific calls** (if the video reviews a patch): the creator's size verdict, headline, winners, losers, non-obvious calls.

Only include claims the transcript and on-screen content support. Mark confidence low where the audio is ambiguous.

## Output schema

{
  "meta_thesis": "string",
  "hero_claims": [{"hero": "name", "tier": "S|A|B|C|D|null", "direction": "rising|stable|falling|null", "why": "1-2 sentences", "items": ["..."], "confidence": 0.0}],
  "item_claims": [{"item": "name", "standing": "strong|weak|niche", "bought_by": ["..."], "why": "1 sentence"}],
  "map_claims": [{"topic": "objectives|farm|neutrals|pickups|economy|...", "claim": "1 sentence", "numbers": "numbers stated or empty", "confidence": 0.0}],
  "reasoning_patterns": ["1-2 sentences each"],
  "patch_calls": {"size": "major|significant|minor|hotfix|null", "headline": "string|null", "winners": ["..."], "losers": ["..."], "non_obvious_calls": ["..."]}
}
