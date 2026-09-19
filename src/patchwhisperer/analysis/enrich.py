from patchwhisperer.analysis.schemas import HeroEnrichment
from patchwhisperer.kb.schema import Build, HeroState, Matchups


def merge_enrichment(h: HeroState, r: HeroEnrichment) -> HeroState:
    """Apply a HeroEnrichment to a HeroState, preserving name/last_changed_patch."""
    h.role = r.role or h.role
    h.archetypes = r.archetypes or h.archetypes
    h.tier = r.tier
    h.trend = r.trend
    h.why = r.why or h.why
    h.builds = [Build(**b.model_dump()) for b in r.builds]
    h.core_items = r.core_items or h.core_items
    h.build_variants = [b.name for b in r.builds]
    if r.matchups:
        h.matchups = Matchups(**r.matchups.model_dump())
    h.matchup_notes = r.matchup_notes
    h.enabled_by = r.enabled_by
    h.countered_by = r.countered_by
    h.notes = r.notes or h.notes
    h.confidence = r.confidence
    return h
