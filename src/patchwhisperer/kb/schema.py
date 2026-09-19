from typing import Literal

from pydantic import BaseModel

Tier = Literal["S", "A", "B", "C", "D", "?"]
Trend = Literal["rising", "stable", "falling", "?"]


class HeroState(BaseModel):
    name: str
    role: str = ""
    archetypes: list[str] = []
    tier: Tier = "?"
    trend: Trend = "?"
    why: str = ""
    core_items: list[str] = []
    build_variants: list[str] = []
    enabled_by: list[str] = []
    countered_by: list[str] = []
    last_changed_patch: str | None = None
    notes: str = ""


class ItemState(BaseModel):
    name: str
    role: str = ""
    bought_by: list[str] = []
    slot: str | None = None
    tier: int | None = None
    notes: str = ""
