# Task: item analysis

Patch: {{patch_title}} ({{patch_date}})

## Reader corrections (authoritative, overrides the knowledge base)

{{corrections}}

## Systems analysis of this patch (already done)

{{stage1_json}}

## Item changes in this patch (grouped by item)

{{item_changes}}

## Knowledge base: the changed items (who buys them and why)

{{items_kb}}

## Knowledge base: heroes whose core_items or build_variants include a changed item

{{heroes_kb_subset}}

## What to do

For each changed item, decide the net direction and magnitude, then trace the consequence to heroes: who has it as a core slot, who used it situationally, and who might now pick it up. Note build-path changes (component changes, slot moves, what it now competes with). Think about the systems context: an item that was good because of the old economy may be worse even if its numbers went up, and vice versa.

Group multiple lines for the same item into one entry. Skip pure bug fixes unless the fix meaningfully changes an interaction (then say which heroes it affects).

Magnitude guide: minor = tuning that will not change who buys it; moderate = changes timing or priority in builds; major = adds or removes the item from core builds, or changes what it does.

## Change rows

`rows` is a list of scannable one-line changes for a phone screen. Give rows for **every item**.

- `label`: 1-3 plain words naming what changed ("Channel time", "T3", "New interrupts", "Teamplay").
- Prefer `old` + `new` when the note gives before/after values; otherwise `text` of at most 8 words. Never both.
- `effect`: judged for the player who buys this item: "good", "bad", or "neutral". A longer channel time is bad.
- `ability`: the exact ability name when the change applies to one.
- Merge lines that say the same thing. Keep every gameplay-relevant change. Never add anything not in the notes; every number in a row must come from the notes verbatim.

Example (Mirage's Traveler):

```json
{"label": "Channel time", "old": "2s", "new": "3s", "effect": "bad", "ability": "Traveler"}
{"label": "T3", "old": "-90s cooldown", "new": "Damage can't interrupt it", "effect": "good", "ability": "Traveler"}
{"label": "Base ability", "text": "Now includes a barrier (no scaling)", "effect": "good", "ability": "Traveler"}
```

## Output schema

{
  "items": [
    {
      "item": "canonical item name",
      "direction": "buff|nerf|rework|neutral",
      "magnitude": "minor|moderate|major",
      "summary": "1-2 sentences of consequence, not restatement",
      "affected_heroes": [
        {"hero": "hero name", "relationship": "core|situational|new_option", "effect": "up|down|neutral", "why": "1 sentence"}
      ],
      "build_shift": "optional 1 sentence on component/slot/competition changes, or empty string",
      "rows": [{"label": "1-3 words", "old": "before", "new": "after", "effect": "good|bad|neutral", "ability": "optional exact name"}]
    }
  ],
  "notable_item_stories": ["0-3 one-sentence cross-item stories, e.g. 'invisibility items were buffed together, expect Shadow Weave on more gun carries'"]
}
