from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class Direction(str, Enum):
    buff = "buff"
    nerf = "nerf"
    neutral = "neutral"
    rework = "rework"
    fix = "fix"


class EntityType(str, Enum):
    hero = "hero"
    item = "item"
    system = "system"
    unknown = "unknown"


class Change(BaseModel):
    section: str
    entity_type: EntityType
    entity_id: int | None = None
    entity_name: str
    ability: str | None = None
    tier: int | None = None
    field: str | None = None
    old: str | None = None
    new: str | None = None
    raw: str
    direction: Direction
    resolved: bool


class Patch(BaseModel):
    gid: str
    title: str
    date: datetime
    url: str
    author: str
    raw_bbcode: str
    changes: list[Change]

    def is_hotfix(self, max_changes: int = 8) -> bool:
        return len(self.changes) < max_changes and not any(
            c.section == "General" for c in self.changes
        )

    def by_entity(self) -> dict[str, list[Change]]:
        grouped: dict[str, list[Change]] = {}
        for c in self.changes:
            grouped.setdefault(c.entity_name, []).append(c)
        return grouped
