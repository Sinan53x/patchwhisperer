# Task: fact-check hero entries against the patch notes

Patch: {{patch_title}} ({{patch_date}})

A separate analyst wrote the entries below. Find mistakes by comparing each entry with its hero's note lines. The notes are the only source of truth for what changed.

## Note lines

{{hero_changes}}

## Reader corrections (authoritative)

{{corrections}}

## Entries to check

{{entries_json}}

## What counts as a mistake

- `change_kind` or `change_size` does not match the hero's own lines. They ignore items and systems. `buff` means clearly stronger, `nerf` clearly weaker, `rework` means an ability works differently, `adjusted` means trade-offs or only fixes.
- A mechanical loss is underplayed. A stun becoming an immobilize can no longer interrupt channels, so it is `bad` and leads the `one_liner`.
- A row's `effect` is backwards for that hero's player: a longer cooldown is `bad`, a shorter one is `good`.
- A row misstates its line, or a gameplay relevant line has no row.
- The `one_liner` contradicts the notes, for example says a cooldown got shorter when it went up, or states a fact with no source.

Report only real mistakes. Most entries are fine, and an empty list is a good answer. Never add a number absent from the notes. When you fix `rows`, return that hero's complete row list.

## Output schema

{
  "fixes": [
    {
      "hero": "exact hero name",
      "issue": "one sentence naming the mistake",
      "change_kind": "buff|nerf|rework|adjusted, or omit",
      "change_size": "minor|moderate|major, or omit",
      "verdict": "keep|watch|bench, or omit",
      "one_liner": "replacement, or omit",
      "rows": [{"label": "1-3 words", "old": "before", "new": "after", "effect": "good|bad|neutral", "ability": "optional"}]
    }
  ]
}
