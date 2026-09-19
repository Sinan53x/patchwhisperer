from typing import Literal

from pydantic import BaseModel, Field

Tier = Literal["S", "A", "B", "C", "D", "?"]
Trend = Literal["rising", "stable", "falling", "?"]


class Build(BaseModel):
    name: str
    damage: Literal["gun", "spirit", "hybrid"]
    core_items: list[str] = []
    popularity: Literal["primary", "secondary", "niche"]
    notes: str = ""


class Matchups(BaseModel):
    beats: list[str] = []
    loses_to: list[str] = []


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
    builds: list[Build] = []
    matchups: Matchups = Field(default_factory=Matchups)
    matchup_notes: str = ""
    confidence: float | None = None


class ItemState(BaseModel):
    name: str
    role: str = ""
    bought_by: list[str] = []
    slot: str | None = None
    tier: int | None = None
    notes: str = ""
