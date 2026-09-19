import json
from collections import Counter

import yaml

from patchwhisperer.kb.store import KBStore
from patchwhisperer.parse.models import Change, EntityType, Patch


def format_changes(changes: list[Change]) -> str:
    """Group change lines by entity, each line tagged with the heuristic direction."""
    by_entity: dict[str, list[Change]] = {}
    for c in changes:
        by_entity.setdefault(c.entity_name, []).append(c)
    out = []
    for name, lines in by_entity.items():
        out.append(f"{name}:")
        for c in lines:
            ability = f"{c.ability}: " if c.ability else ""
            out.append(f"  - [{c.direction.value}] {ability}{c.raw}")
    return "\n".join(out)


def system_changes(patch: Patch) -> list[Change]:
    return [
        c
        for c in patch.changes
        if c.section not in ("Heroes", "Items") and c.entity_type == EntityType.system
    ]


def item_changes(patch: Patch) -> list[Change]:
    return [
        c
        for c in patch.changes
        if c.section == "Items" or c.entity_type == EntityType.item
    ]


def hero_changes(patch: Patch) -> list[Change]:
    return [
        c
        for c in patch.changes
        if c.section == "Heroes"
        or c.entity_type in (EntityType.hero, EntityType.unknown)
    ]


def _non_empty(model: dict) -> dict:
    return {k: v for k, v in model.items() if v not in (None, "", [], {})}


def heroes_kb(kb: KBStore) -> str:
    heroes = kb.load_heroes()
    return yaml.safe_dump(
        {k: _non_empty(v.model_dump()) for k, v in heroes.items()}, sort_keys=False
    )


def heroes_kb_subset(kb: KBStore, names: list[str]) -> str:
    heroes = kb.load_heroes()
    sub = {k: v.model_dump() for k, v in heroes.items() if k in names}
    return yaml.safe_dump(sub, sort_keys=False) if sub else "(none)"


def items_kb(kb: KBStore, names: list[str]) -> str:
    items = kb.load_items()
    out = []
    for name in names:
        if name in items:
            out.append(
                yaml.safe_dump({name: items[name].model_dump()}, sort_keys=False)
            )
        else:
            out.append(f"{name}: (not in KB yet)")
    return "\n".join(out) if out else "(none)"


def snapshot_table(snapshot: dict) -> str:
    rows = sorted(snapshot.items(), key=lambda kv: kv[1]["win_rate"], reverse=True)
    lines = ["hero | WR% | PR% | matches"]
    for name, s in rows:
        lines.append(
            f"{name} | {s['win_rate'] * 100:.1f} | {s['pick_rate'] * 100:.1f} | {s['matches']}"
        )
    return "\n".join(lines)


def change_counts(patch: Patch) -> str:
    counts = Counter(c.section for c in patch.changes)
    parts = [f"{k} {v}" for k, v in counts.items()]
    return ", ".join(parts) + f", total {len(patch.changes)}"


def stage3_movers_json(heroes_analysis) -> str:
    movers = [h for h in heroes_analysis.heroes if h.direction != "neutral"]
    return json.dumps([h.model_dump() for h in movers], indent=1)


def stage3_pool_json(heroes_analysis, pool: list[str]) -> str:
    entries = [h for h in heroes_analysis.heroes if h.hero in pool]
    return json.dumps([h.model_dump() for h in entries], indent=1)


def stage2_pool_json(item_analysis, pool: list[str]) -> str:
    entries = [
        i for i in item_analysis.items if any(a.hero in pool for a in i.affected_heroes)
    ]
    return json.dumps([i.model_dump() for i in entries], indent=1)


def heroes_kb_pool(kb: KBStore, pool: list[str]) -> str:
    return heroes_kb_subset(kb, pool)


def heroes_kb_movers(kb: KBStore, heroes_analysis) -> str:
    return heroes_kb_subset(
        kb, [h.hero for h in heroes_analysis.heroes if h.direction != "neutral"]
    )


def hero_names_affected_by_items(kb: KBStore, changed_items: list[str]) -> list[str]:
    heroes = kb.load_heroes()
    names = []
    for name, h in heroes.items():
        touched = set(h.core_items) | set(h.build_variants)
        if touched & set(changed_items):
            names.append(name)
    return names
