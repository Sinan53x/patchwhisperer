# Task: turn a ranked-season announcement into structured season data

Post: Ranked - Beta Season 2 (2026-11-05)

## Announcement body

[img src="{STEAM_CLAN_LOC_IMAGE}/45164767/128f6aad08d9391a99f7e91565ea3a4b8dbef37e.png"]Today marks the end of our first Ranked Beta Season. Players who participated in Beta Season 1 will receive their commemorative Hideout plaque of their highest achieved rank once the new season rolls over.
Beta Season 2 begins now, and will end on Thursday March 11th 2027, lasting four months.
Seasonal Rank Reset
Ranked players will see their rank soft reset at the start of this new season, and can begin their climb through Beta Season 2. This soft reset is significantly smaller than the previous one. On average, players can expect to see their rank decrease by around 1 badge as part of the soft reset. We will also be using the players' winrate in the previous season to make further adjustments of 1-2 subranks to help place players in the correct relative spots. Existing Ranked players will not have to complete calibration again at the start of this season, players who did not participate in Ranked last season will need to calibrate as usual.
Global Rank Redistribution
After monitoring the Ranked playerbase throughout this first season, and accommodating for the recent influx of new players in the game, we will be running a global redistribution at the start of this new season. This means that some players may see their rank actually increase rather than decrease at the start of the new season despite the soft reset.
To summarize, both of these rank adjustments are being made as a two-step operation. The first is taking everyone's existing ranks and redistributing the curve as described above. Second is taking the new post-redistribution numbers and applying the soft reset of ranks by about -1 badge on average. The final result of this is going to be different for everyone, some may gain ranks despite the soft reset and others may get moved down slightly more.
We are making a few changes to the way the Ranked system works for Beta Season 2 based on how things played out in Beta Season 1, as well as all of the useful feedback we've heard from the community.
Rank Loss Protection (Shields):
Players within the Phantom, Ascendant, and Eternus ranks will no longer have any rank loss protection shields (previously 5 on full ranks and 2 on subranks).
For all other players, we have reduced the number of rank loss protection shields. For full rank boundary, the shield count is reduced from 5 to 3 (i.e. if you are at Mystic I with 0 rank points, you will now maintain the Mystic badge for only 3 losses before dropping to Sentinel instead of 5). For subranks (i.e. Mystic III → Mystic II), the shield count is reduced from 2 to 1.
Per Match: The points for a game has been increased from 300 to 350.
Ranking Up: The points required to reach a new badge from a final subrank have been decreased from 2000 to 1500. The points between subranks remain unchanged at 1000.
We have increased the number of hero bans per match in Ranked from 3 to 4.
The highest players can be placed in the new season will be Ascendant I, with some potential for up to Ascendant III based on performance in the previous season (up from Oracle VI max last season).
We still feel strongly that it is very important that players in Ranked have deep knowledge and confidence piloting a hero they are using for the sake of all players involved, however we also recognize that there is room for improvement in how we measure this. Unlocking a hero in Ranked now uses a point system, rather than only progressing based on wins. Unlocking a hero now requires 35 points, you will gain 2 points for a win and 1 point for a loss. With the previous 15 win system (assuming 50% WR), it would have required an equivalent of 45 points (15 wins = 30 points, 15 losses = 15 points, 30+15=45).
We've reworked the backend to how leaderboards work to fix numerous bugs.
Each Ranked season now has its own leaderboard.
To show up on a leaderboard, you must play at least 50 Ranked matches in that season within the last 30 days. Ranking is based on your current badge progress.
To show up on a hero-specific leaderboard, you must play at least 15 Ranked matches with that hero within the last 30 days. Ranking is based on your current badge progress and your recent win/loss performance on that hero.
Beta Season 2 begins today, we'll see you there!

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
  Rank names, low to high: Initiate, Seeker, Alchemist, Arcanist, Ritualist, Emissary, Archon, Oracle, Phantom, Ascendant, Eternus.
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
