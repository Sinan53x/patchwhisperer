# Task: turn a ranked-season announcement into structured season data

Post: {{post_title}} ({{post_date}})

## Announcement body

{{post_body}}

## What to do

The output renders as a visual page (timeline, rank ladder, change cards, win/lose chips), so keep every string short. Extract:

- `season_name`: the season's name as given (e.g. "Beta Season 2").
- `starts`: ISO date (YYYY-MM-DD) the season starts; use the post date if it says it starts now/today.
- `ends`: ISO date the season ends, or null if none is announced.
- `headline`: one plain sentence, at most 14 words. No hype.
- `reset_steps`: 2-4 steps describing how ranks are reset, in the order they happen. Each {"title", "detail"}: `title` at most 4 words (e.g. "Redistribute the curve"), `detail` one short sentence.
- `ladder`:
  - `soft_reset`: the average rank change as a tiny phrase (e.g. "about -1 badge"), or "" if none.
  - `placement_cap_before` / `placement_cap_after`: highest possible initial placement before and after, as a rank name with optional subrank (e.g. "Oracle VI", "Ascendant I"). null if not stated.
  - `placement_cap_stretch`: a higher cap reachable under some condition (e.g. "Ascendant III"), or null.
  - `no_shield_ranks`: rank names that have no rank-loss protection at all, e.g. ["Phantom", "Ascendant", "Eternus"]. [] if none.
  Rank names, low to high: Initiate, Seeker, Acolyte, Sentinel, Mystic, Ritualist, Emissary, Oracle, Phantom, Ascendant, Eternus.
- `rules`: each ranked rule change as {"label", "category", "before", "after", "effect", "effect_label", "note"}:
  - `label`: what changed, at most 6 words (e.g. "Loss shields at a full rank").
  - `category`: one of climbing (points, thresholds), protection (shields, loss protection), draft (bans, picks), unlocks (hero unlocks, placement), leaderboards, other.
  - `before` / `after`: short values with the same unit where possible (e.g. "5 losses" -> "3 losses", "300" -> "350", "3" -> "4"). `before` is null for a brand-new rule. Use "none" when something is removed.
  - `effect`: easier if the change helps the typical player climb or progress, harsher if it punishes them more, neutral otherwise.
  - `effect_label`: 1-3 words naming that effect (e.g. "Faster climb", "Less forgiving", "One more ban").
  - `note`: one short line of context, or "".
- `winners` / `losers`: 1-3 each, {"who", "why"}: `who` is a player group in at most 4 words (e.g. "Players who grind", "Phantom and up"), `why` one short sentence.

## Rules

- Every number in `before`/`after` must appear verbatim in the announcement body. Never invent, round, or extrapolate a number. If a value is not in the post, leave it out.
- Dates must come from the post (or the post date for "starts today/now").
- Do not repeat the same fact in reset_steps and rules.

## Output schema

{
  "season_name": "string",
  "starts": "YYYY-MM-DD",
  "ends": "YYYY-MM-DD or null",
  "headline": "string",
  "reset_steps": [{"title": "string", "detail": "string"}],
  "ladder": {"soft_reset": "string", "placement_cap_before": "string or null", "placement_cap_after": "string or null", "placement_cap_stretch": "string or null", "no_shield_ranks": ["string"]},
  "rules": [{"label": "string", "category": "climbing|protection|draft|unlocks|leaderboards|other", "before": "string or null", "after": "string", "effect": "easier|harsher|neutral", "effect_label": "string", "note": "string"}],
  "winners": [{"who": "string", "why": "string"}],
  "losers": [{"who": "string", "why": "string"}]
}
