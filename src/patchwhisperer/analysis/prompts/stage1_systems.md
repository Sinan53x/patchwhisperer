# Task: systems analysis

Patch: {{patch_title}} ({{patch_date}})

## Current meta thesis (knowledge base, written before this patch)

{{meta_md}}

## Changes in the General / systems sections of this patch

{{system_changes}}

## Item and hero sections (for context only; do not analyze them here)

Items changed: {{item_names}}
Heroes changed: {{hero_names}}

## Update summary

{{digest_summary}}

## Creator sources published after this patch (optional corroboration; the notes, KB and snapshot remain primary — if a source contradicts them, say so and keep your own read)

{{creator_sources}}

## What to do

Analyze only the systems-level changes. For each distinct system that moved (economy, comeback, objectives, respawn, movement, slows, parry/melee, reload, map/jungle/objectives, matchmaking), explain what changed and what it does to how the game is played. Then read the patch's tempo direction: does it reward early aggression and snowballing (toward tempo) or late scaling and comebacks (toward scaling)? Finally, map the effect onto hero archetypes.

For a major content update the input is prose, not number tweaks; still produce one `systems_changed` entry per system that moved and read tempo from how soul income and fight locations changed.

Archetype vocabulary (use these labels): gun carry, spirit carry, burst caster, tank/frontline, lane bully, late scaler, mobile assassin, support/healer, split pusher, initiator, poke/siege.

If there are no systems changes, return empty lists and a neutral tempo shift with why = "no systems changes".

## Output schema

{
  "systems_changed": [
    {"system": "string", "change_summary": "1-2 sentences", "driving_changes": ["raw change text", "..."], "magnitude": "minor|moderate|major", "effect_on_play": "1-2 sentences"}
  ],
  "tempo_shift": {"direction": "toward_tempo|toward_scaling|neutral", "confidence": 0.0, "why": "1-2 sentences"},
  "archetype_effects": [
    {"archetype": "string from vocabulary", "direction": "up|down|neutral", "magnitude": "minor|moderate|major", "why": "1 sentence naming the driver"}
  ],
  "intent_read": "1-3 sentences on what problem Valve appears to be solving"
}
