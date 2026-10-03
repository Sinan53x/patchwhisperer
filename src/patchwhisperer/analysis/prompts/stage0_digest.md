# Task: digest a major content update into patch-note lines

Update: {{patch_title}} ({{patch_date}})

## Steam announcement body (may be a short stub)

{{steam_body}}

## Update page content (fetched from the linked playdeadlock.com page, or manual notes)

{{update_page}}

## Known heroes (for canonical spelling)

{{hero_names}}

## What to do

Extract every change that affects how the game is played and rewrite each as one terse patch-note line in the form `Entity: change` (e.g. `Bell Tower: new objective on top of the Chinatown district; concentrated soul hotspot; collecting it rings a bell heard across the map`).

Sections:
- `Map` — lanes, districts, objectives, neutrals/Haunts, breakables/crates/boxes, Sinner's Sacrifice, Buff Containers, pickups such as Healing Snacks and Steam Vents, routes, shops including temporary ones like The Broker.
- `General` — economy, parry/melee/reload, respawn, systems, mode rules, matchmaking.
- `Items` — any item added/changed/removed, including Corrupted items.
- `Heroes` — new heroes as `Name: new hero — <kit summary from the text if given>` and any direct hero changes/fixes that alter play.

Ignore UI, HUD, settings, accessibility, audio, cosmetics, VO, sandbox/testing tools, performance, localisation, and pure bug fixes that don't change interactions. Preserve every number present. Do not invent numbers.

`new_heroes` lists names of heroes announced as new/upcoming. `summary` is 2-3 sentences on what kind of update this is.

## Output schema

{
  "summary": "string",
  "sections": {
    "Map": ["Entity: change", "..."],
    "General": ["..."],
    "Items": ["..."],
    "Heroes": ["..."]
  },
  "new_heroes": ["..."]
}
