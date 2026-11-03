from typing import Literal

from pydantic import BaseModel, Field, model_validator

Magnitude = Literal["minor", "moderate", "major"]
UpDown = Literal["up", "down", "neutral"]
Tier = Literal["S", "A", "B", "C", "D"]
Verdict = Literal["keep", "watch", "bench"]
Effect = Literal["good", "bad", "neutral"]
ChangeKind = Literal["buff", "nerf", "rework", "adjusted", "none"]


class ChangeRow(BaseModel):
    """One visual line of a change: either old -> new, or a plain statement."""

    label: str = Field(min_length=1)
    old: str | None = None
    new: str | None = None
    text: str | None = None
    effect: Effect = "neutral"
    ability: str | None = None

    @model_validator(mode="after")
    def _delta_or_text(self):
        has_delta = bool(self.old and self.new)
        if has_delta == bool(self.text):
            raise ValueError("ChangeRow needs old and new, or text, not both")
        return self


class SystemChange(BaseModel):
    system: str = ""
    change_summary: str = ""
    driving_changes: list[str] = []
    magnitude: Magnitude = "minor"
    effect_on_play: str = ""


class TempoShift(BaseModel):
    direction: Literal["toward_tempo", "toward_scaling", "neutral"] = "neutral"
    confidence: float = 0.0
    why: str = ""


class ArchetypeEffect(BaseModel):
    archetype: str = ""
    direction: UpDown = "neutral"
    magnitude: Magnitude = "minor"
    why: str = ""


class SystemsAnalysis(BaseModel):
    systems_changed: list[SystemChange] = []
    tempo_shift: TempoShift = Field(default_factory=TempoShift)
    archetype_effects: list[ArchetypeEffect] = []
    intent_read: str = ""


class AffectedHero(BaseModel):
    hero: str = ""
    relationship: Literal["core", "situational", "new_option"] = "situational"
    effect: UpDown = "neutral"
    why: str = ""


class ItemEntry(BaseModel):
    item: str = ""
    direction: Literal["buff", "nerf", "rework", "neutral"] = "neutral"
    magnitude: Magnitude = "minor"
    summary: str = ""
    affected_heroes: list[AffectedHero] = []
    build_shift: str = ""
    rows: list[ChangeRow] = []


class ItemAnalysis(BaseModel):
    items: list[ItemEntry] = []
    notable_item_stories: list[str] = []


class HeroEntry(BaseModel):
    hero: str = Field(min_length=1)
    in_notes: bool = False
    direction: UpDown = "neutral"
    magnitude: Literal["none", "minor", "moderate", "major"] = "none"
    confidence: float = 0.0
    direct_reasons: list[str] = []
    indirect_reasons: list[str] = []
    build_changes: list[str] = []
    tier_before: Literal["S", "A", "B", "C", "D", "?"] = "?"
    tier_after: Tier | Literal["?"] = "?"
    one_liner: str = ""
    verdict: Verdict | None = None
    rows: list[ChangeRow] = []
    # what the notes did, kept apart from direction, which also weighs items and systems
    change_kind: ChangeKind = "none"
    change_size: Literal["none", "minor", "moderate", "major"] = "none"


class HeroFix(BaseModel):
    hero: str = Field(min_length=1)
    issue: str = ""
    change_kind: ChangeKind | None = None
    change_size: Literal["minor", "moderate", "major"] | None = None
    verdict: Verdict | None = None
    one_liner: str | None = None
    rows: list[ChangeRow] | None = None


class HeroAudit(BaseModel):
    fixes: list[HeroFix] = []


class HeroAnalysis(BaseModel):
    # no minimum: coverage against the KB roster is checked in the pipeline
    heroes: list[HeroEntry] = []

    def movers(self) -> list[HeroEntry]:
        return [h for h in self.heroes if h.direction != "neutral"]


class MetaThesis(BaseModel):
    previous: str = ""
    new: str = ""
    relationship: Literal["continuation", "shift", "reversal"] = "continuation"
    why: str = ""


class Mover(BaseModel):
    hero: str = ""
    why: str = ""
    indirect: bool = False


class NonObviousCall(BaseModel):
    claim: str = ""
    why: str = ""
    confidence: float = 0.0


class Synthesis(BaseModel):
    patch_size: Literal["major", "significant", "minor", "hotfix"] = "minor"
    size_why: str = ""
    headline: str = Field(min_length=1)
    meta_thesis: MetaThesis = Field(default_factory=MetaThesis)
    winners: list[Mover] = []
    losers: list[Mover] = []
    non_obvious_calls: list[NonObviousCall] = []
    uncertainties: list[str] = []
    what_to_watch: list[str] = []


class PoolVerdict(BaseModel):
    hero: str = ""
    verdict: Verdict = "watch"
    one_liner: str = ""
    direct: str = ""
    indirect: str = ""
    build_adjustments: list[str] = []
    confidence: float = 0.0


class PoolVerdicts(BaseModel):
    verdicts: list[PoolVerdict] = []


class KBUpdate(BaseModel):
    meta_md: str = ""
    hero_updates: dict[str, dict] = {}
    item_updates: dict[str, dict] = {}
    change_log: list[str] = []

    @model_validator(mode="after")
    def _non_empty(self):
        if not (self.meta_md or self.hero_updates or self.item_updates):
            raise ValueError("KBUpdate must change at least one artifact")
        return self


class ContentDigest(BaseModel):
    summary: str = ""
    sections: dict[str, list[str]] = {}
    new_heroes: list[str] = []

    @model_validator(mode="after")
    def _non_empty(self):
        if not any(self.sections.values()):
            raise ValueError("ContentDigest must have at least one non-empty section")
        return self


class KBHeroUpdate(BaseModel):
    hero_updates: dict[str, dict] = {}
    change_log: list[str] = []


class HeroClaim(BaseModel):
    hero: str = ""
    tier: Tier | None = None
    direction: Literal["rising", "stable", "falling"] | None = None
    why: str = ""
    items: list[str] = []
    confidence: float = 0.0


class ItemClaim(BaseModel):
    item: str = ""
    standing: Literal["strong", "weak", "niche"] = "niche"
    bought_by: list[str] = []
    why: str = ""


class MapClaim(BaseModel):
    topic: str = ""
    claim: str = ""
    numbers: str = ""
    confidence: float = 0.0


class PatchCalls(BaseModel):
    size: Literal["major", "significant", "minor", "hotfix"] | None = None
    headline: str | None = None
    winners: list[str] = []
    losers: list[str] = []
    non_obvious_calls: list[str] = []


class DistilledSource(BaseModel):
    meta_thesis: str = ""
    hero_claims: list[HeroClaim] = Field(min_length=1)
    item_claims: list[ItemClaim] = []
    map_claims: list[MapClaim] = []
    reasoning_patterns: list[str] = []
    patch_calls: PatchCalls = Field(default_factory=PatchCalls)


class SeedKB(BaseModel):
    meta_md: str = ""
    heroes: dict[str, dict] = Field(min_length=30)
    items: dict[str, dict] = {}


class EnrichBuild(BaseModel):
    name: str = ""
    damage: Literal["gun", "spirit", "hybrid"] = "hybrid"
    core_items: list[str] = []
    popularity: Literal["primary", "secondary", "niche"] = "secondary"
    notes: str = ""


class EnrichMatchups(BaseModel):
    beats: list[str] = []
    loses_to: list[str] = []


class HeroEnrichment(BaseModel):
    role: str = ""
    archetypes: list[str] = []
    tier: Tier | Literal["?"] = "?"
    trend: Literal["rising", "stable", "falling"] = "stable"
    why: str = ""
    builds: list[EnrichBuild] = []
    core_items: list[str] = []
    matchups: EnrichMatchups | None = None
    matchup_notes: str = ""
    enabled_by: list[str] = []
    countered_by: list[str] = []
    notes: str = ""
    confidence: float = 0.0


class NewHeroCard(BaseModel):
    headline: str = Field(min_length=1)
    kit_read: list[str] = Field(min_length=1)
    meta_fit: str = ""
    threatens: list[str] = []
    threatened_by: list[str] = []
    build_read: str = ""
    provisional_tier: Tier | Literal["?"] = "?"
    confidence: float = 0.0
    what_to_watch: list[str] = []


class NewHeroEvaluation(BaseModel):
    enrichment: HeroEnrichment = Field(default_factory=HeroEnrichment)
    card: NewHeroCard


class AnalysisBundle(BaseModel):
    patch_id: str
    patch_title: str
    systems: SystemsAnalysis | None = None
    items: ItemAnalysis | None = None
    heroes: HeroAnalysis | None = None
    synthesis: Synthesis
    pool: PoolVerdicts | None = None
    kb_update: KBUpdate | None = None
    usage: dict = {}
