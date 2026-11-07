# Task: summarize a ranked-season announcement into structured season data

Post: {{post_title}} ({{post_date}})

## Announcement body

{{post_body}}

## What to do

Summarize this ranked season announcement for players skimming an archive. Extract:

- `season_name`: the season's name as given (e.g. "Beta Season 2").
- `starts`: ISO date (YYYY-MM-DD) the season starts; use the post date if it says it starts now/today.
- `ends`: ISO date the season ends, or null if none is announced.
- `headline`: one plain sentence describing the season for an archive list. No hype.
- `reset`: short plain-language bullets about the rank reset and any rank redistribution.
- `rules`: the ranked rule changes, each {"label", "before", "after", "note"}:
  - `label`: what changed (e.g. "Rank loss shields (full rank)").
  - `before` / `after`: short values only (e.g. "5 losses", "3 losses", "300", "350"). `before` is null for a brand-new rule.
  - `note`: one short line of context under the rule; empty string if nothing to add.
- `takeaways`: 2-4 short "what this means for you" lines: who gains, who should care. No hype.

## Rules

- Every number in `before`/`after` must appear verbatim in the announcement body. Never invent, round, or extrapolate a number. If a value is not in the post, leave it out.
- Dates must come from the post (or the post date for "starts today/now").
- Keep strings short; these render on a phone.

## Output schema

{
  "season_name": "string",
  "starts": "YYYY-MM-DD",
  "ends": "YYYY-MM-DD or null",
  "headline": "string",
  "reset": ["bullet", "..."],
  "rules": [{"label": "string", "before": "string or null", "after": "string", "note": "string"}],
  "takeaways": ["string", "..."]
}
