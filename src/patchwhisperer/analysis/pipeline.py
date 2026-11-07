import json
import logging
import re
import time
from pathlib import Path

from pydantic import ValidationError

from patchwhisperer import config
from patchwhisperer.analysis import context as ctx
from patchwhisperer.analysis.llm import SYSTEM_PROMPT, render_prompt
from patchwhisperer.analysis.schemas import (
    AnalysisBundle,
    ChangeRow,
    HeroAnalysis,
    HeroAudit,
    ItemAnalysis,
    KBHeroUpdate,
    KBUpdate,
    PoolVerdicts,
    Synthesis,
    SystemsAnalysis,
)
from patchwhisperer.analysis.tiers import sync_kb_tiers
from patchwhisperer.kb.schema import Build, ItemState
from patchwhisperer.kb.store import KBStore
from patchwhisperer.parse.models import Change, Patch

log = logging.getLogger(__name__)

HOTFIX_SKIPPED = "(hotfix: stage skipped)"

_HERO_FIELDS = {
    "role",
    "archetypes",
    "trend",
    "why",
    "core_items",
    "build_variants",
    "enabled_by",
    "countered_by",
    "last_changed_patch",
    "notes",
    "builds",
    "confidence",
}
_ITEM_FIELDS = {"role", "bought_by", "slot", "tier", "notes"}
_TRENDS = {"rising", "stable", "falling", "?"}


def patch_id_of(patch: Patch) -> str:
    return f"{patch.date:%Y-%m-%d}-{patch.gid}"


STAGE_SECONDS: dict[str, float] = {}


_NUM_TOKEN = re.compile(r"[+-]?\d+(?:\.\d+)?[a-zA-Z%]*")


def _has_number(token: str, haystack: str) -> bool:
    # a trailing "." is fine (sentence end); a decimal tail like ".5" is not
    return bool(re.search(rf"(?<![\d.]){re.escape(token)}(?!\d|\.\d)", haystack))


def guard_rows(
    rows: list[ChangeRow], raw_lines: list[str], owner: str = ""
) -> list[ChangeRow]:
    """Drop rows whose numbers do not appear verbatim in the entity's raw note
    lines. If every row is dropped, fall back to the raw lines themselves so a
    real change is never lost to a hallucinated number."""
    if not rows:
        return rows
    haystack = "\n".join(raw_lines)
    kept = []
    for r in rows:
        fields = " ".join(x for x in (r.old, r.new, r.text) if x)
        # compare unsigned: notes say "increased by 5%", rows may render "+5%"
        missing = [
            t
            for t in _NUM_TOKEN.findall(fields)
            if not _has_number(t.lstrip("+-"), haystack)
        ]
        if missing:
            log.warning(
                "%s: dropping row with number(s) not in the notes %s: %r",
                owner,
                missing,
                r.label,
            )
        else:
            kept.append(r)
    if not kept:
        return [ChangeRow(label="Change", text=line) for line in raw_lines]
    # a line whose numbers appear in no surviving row was silently dropped
    covered = " ".join(x for r in kept for x in (r.old, r.new, r.text) if x)
    for line in raw_lines:
        numbers = [t.lstrip("+-") for t in _NUM_TOKEN.findall(line)]
        if numbers and not any(_has_number(n, covered) for n in numbers):
            kept.append(ChangeRow(label="Change", text=line))
    return kept


def _raw_lines(changes: list[Change]) -> dict[str, list[str]]:
    out: dict[str, list[str]] = {}
    for c in changes:
        out.setdefault(c.entity_name, []).append(c.raw)
    return out


def _guard_item_rows(items: ItemAnalysis, raw: dict[str, list[str]]):
    for it in items.items:
        it.rows = guard_rows(it.rows, raw.get(it.item, []), owner=it.item)
    return items


def _guard_hero_rows(heroes: HeroAnalysis, raw: dict[str, list[str]]):
    for h in heroes.heroes:
        h.rows = guard_rows(h.rows, raw.get(h.hero, []), owner=h.hero)
    return heroes


def uncovered_heroes(
    analysis: HeroAnalysis, expected: list[str], changed: set[str]
) -> list[str]:
    """Expected heroes with no usable entry. An entry only counts when its
    name matches and, for heroes with direct changes, `one_liner` and
    `verdict` are non-empty. Duplicates and foreign names are ignored."""
    expected_set = set(expected)
    entries: dict[str, object] = {}
    for h in analysis.heroes:
        if h.hero not in expected_set:
            log.warning("stage 3: ignoring entry for unexpected hero %r", h.hero)
            continue
        if h.hero in entries:
            log.warning("stage 3: ignoring duplicate entry for %r", h.hero)
            continue
        entries[h.hero] = h
    out = []
    for name in expected:
        e = entries.get(name)
        if e is None or (
            name in changed and (not e.one_liner.strip() or e.verdict is None)
        ):
            out.append(name)
    return out


def _merge_hero_analyses(
    analyses: list[HeroAnalysis], expected: list[str]
) -> HeroAnalysis:
    expected_set = set(expected)
    entries: dict[str, object] = {}
    # later analyses win so a retry can replace an incomplete entry
    for a in analyses:
        for h in a.heroes:
            if h.hero not in expected_set:
                log.warning("stage 3: ignoring entry for unexpected hero %r", h.hero)
                continue
            entries[h.hero] = h
    return HeroAnalysis(heroes=[entries[n] for n in expected if n in entries])


def _run_stage(
    llm,
    kb: KBStore,
    patch_id: str,
    n: int,
    name: str,
    schema,
    *,
    tag: str | None = None,
    budget_key=None,
    prefix: str = "stage",
    post=None,
    **values,
):
    tag = tag or str(n)
    prompt = render_prompt(name, **values)
    pdir = kb.patch_dir(patch_id)
    t0 = time.time()
    result = llm.complete_json(
        SYSTEM_PROMPT,
        prompt,
        schema,
        max_tokens=config.STAGE_MAX_TOKENS[budget_key if budget_key is not None else n],
        raw_path=pdir / f"{prefix}{tag}.raw.txt",
    )
    if post is not None:
        result = post(result)
    elapsed = time.time() - t0
    STAGE_SECONDS[tag] = elapsed
    log.info("stage %s (%s) done in %.1fs", tag, name, elapsed)
    (pdir / f"{prefix}{tag}.prompt.md").write_text(prompt)
    (pdir / f"{prefix}{tag}.json").write_text(result.model_dump_json(indent=1))
    return result


def apply_hero_fixes(
    heroes: HeroAnalysis, audit: HeroAudit, raw: dict[str, list[str]]
) -> HeroAnalysis:
    by_name = {h.hero: h for h in heroes.heroes}
    for fix in audit.fixes:
        entry = by_name.get(fix.hero)
        if entry is None:
            log.warning("audit: ignoring fix for unknown hero %r", fix.hero)
            continue
        log.info("audit: %s: %s", fix.hero, fix.issue)
        for field in ("change_kind", "change_size", "verdict", "one_liner"):
            value = getattr(fix, field)
            if value:
                setattr(entry, field, value)
        if fix.rows:
            entry.rows = guard_rows(fix.rows, raw.get(fix.hero, []), owner=fix.hero)
    return heroes


def _audit_heroes(
    llm,
    kb: KBStore,
    patch_id: str,
    heroes: HeroAnalysis,
    h_changes: list[Change],
    common: dict,
) -> HeroAnalysis:
    """Second-reader pass over stage 3. It only improves accuracy, so a failed
    call keeps the unaudited entries instead of losing the patch."""
    changed = {c.entity_name for c in h_changes}
    entries = [h for h in heroes.heroes if h.hero in changed]
    raw = _raw_lines(h_changes)
    size = config.STAGE3_HERO_BATCH
    for i in range(0, len(entries), size):
        batch = entries[i : i + size]
        names = {h.hero for h in batch}
        try:
            audit = _run_stage(
                llm,
                kb,
                patch_id,
                3,
                "stage3_audit",
                HeroAudit,
                tag=f"3a{i // size + 1}",
                budget_key="3b",
                **common,
                hero_changes=ctx.format_changes(
                    [c for c in h_changes if c.entity_name in names]
                ),
                entries_json=json.dumps(
                    [h.model_dump(exclude={"indirect_reasons", "build_changes"}) for h in batch],
                    indent=1,
                ),
            )
        except Exception:
            log.exception("stage 3 audit failed for batch %d", i // size + 1)
            continue
        apply_hero_fixes(heroes, audit, raw)
    return heroes


def _run_hero_analysis(
    llm,
    kb: KBStore,
    patch_id: str,
    h_changes: list[Change],
    s1: str,
    s2: str,
    snap_txt: str,
    common: dict,
) -> HeroAnalysis:
    """Stage 3 in sequential hero batches, then a coverage gate: one retry for
    heroes the model omitted, and a raise if any remain uncovered."""
    pdir = kb.patch_dir(patch_id)
    expected = ctx.expected_hero_names(kb, h_changes)
    changed = {c.entity_name for c in h_changes}
    raw_h = _raw_lines(h_changes)

    def call(names: list[str], tag: str) -> HeroAnalysis:
        kb_names = ctx.hero_names_with_matchups(kb, names)
        return _run_stage(
            llm,
            kb,
            patch_id,
            3,
            "stage3_heroes",
            HeroAnalysis,
            tag=tag,
            budget_key="3b",
            post=lambda r: _guard_hero_rows(r, raw_h),
            **common,
            stage1_json=s1,
            stage2_json=s2,
            hero_changes=ctx.format_changes(h_changes),
            heroes_kb=ctx.heroes_kb_subset(kb, kb_names),
            snapshot=snap_txt,
            batch_heroes=", ".join(names),
        )

    batch_size = config.STAGE3_HERO_BATCH
    parts = [
        call(expected[i : i + batch_size], f"3b{i // batch_size + 1}")
        for i in range(0, len(expected), batch_size)
    ]
    heroes = _merge_hero_analyses(parts, expected)
    missing = uncovered_heroes(heroes, expected, changed)
    if missing:
        log.warning("stage 3: %d heroes uncovered, retrying: %s", len(missing), missing)
        heroes = _merge_hero_analyses([heroes, call(missing, "3r")], expected)
        missing = uncovered_heroes(heroes, expected, changed)
    if missing:
        raise RuntimeError(f"stage 3 did not cover heroes: {missing}")
    heroes = _audit_heroes(llm, kb, patch_id, heroes, h_changes, common)
    (pdir / "stage3.json").write_text(heroes.model_dump_json(indent=1))
    return heroes


def run_analysis(
    patch: Patch,
    kb: KBStore,
    snapshot: dict,
    pool: list[str],
    llm,
    *,
    update_kb: bool = True,
    creator_sources: str = "",
) -> AnalysisBundle:
    STAGE_SECONDS.clear()
    sync_kb_tiers(kb, snapshot)
    patch_id = patch_id_of(patch)
    pdir = kb.patch_dir(patch_id)
    (pdir / "patch.json").write_text(
        patch.model_dump_json(indent=1, exclude={"raw_bbcode"})
    )
    meta_md = kb.load_meta() if kb.meta_path.exists() else "(empty)"
    common = {
        "patch_title": patch.title,
        "patch_date": f"{patch.date:%Y-%m-%d}",
        "creator_sources": creator_sources or "(none)",
        "digest_summary": patch.digest_summary or "(n/a)",
        "corrections": kb.load_corrections(),
    }
    sys_changes = ctx.system_changes(patch)
    it_changes = ctx.item_changes(patch)
    h_changes = ctx.hero_changes(patch)
    changed_items = sorted({c.entity_name for c in it_changes})
    changed_heroes = sorted({c.entity_name for c in h_changes})
    raw_item_lines = _raw_lines(it_changes)
    snap_txt = ctx.snapshot_table(snapshot) if snapshot else "(no snapshot)"

    if patch.is_hotfix():
        systems = None
        items = None
        heroes = None
        s1 = s2 = s3m = HOTFIX_SKIPPED
        synthesis = _run_stage(
            llm,
            kb,
            patch_id,
            4,
            "stage4_synthesis",
            Synthesis,
            **common,
            change_counts=ctx.change_counts(patch),
            meta_md=meta_md,
            stage1_json=s1,
            stage2_json=s2,
            stage3_movers_json=s3m,
        )
    else:
        systems = _run_stage(
            llm,
            kb,
            patch_id,
            1,
            "stage1_systems",
            SystemsAnalysis,
            **common,
            meta_md=meta_md,
            system_changes=ctx.format_changes(sys_changes),
            item_names=", ".join(changed_items) or "(none)",
            hero_names=", ".join(changed_heroes) or "(none)",
        )
        s1 = systems.model_dump_json(indent=1)

        if it_changes:
            item_hero_names = ctx.hero_names_affected_by_items(kb, changed_items)
            items = _run_stage(
                llm,
                kb,
                patch_id,
                2,
                "stage2_items",
                ItemAnalysis,
                post=lambda r: _guard_item_rows(r, raw_item_lines),
                **common,
                stage1_json=s1,
                item_changes=ctx.format_changes(it_changes),
                items_kb=ctx.items_kb(kb, changed_items),
                heroes_kb_subset=ctx.heroes_kb_subset(kb, item_hero_names),
            )
            s2 = items.model_dump_json(indent=1)
        else:
            items = ItemAnalysis()
            s2 = '{"items": [], "notable_item_stories": []}'
            STAGE_SECONDS["2"] = 0.0

        heroes = _run_hero_analysis(
            llm, kb, patch_id, h_changes, s1, s2, snap_txt, common
        )
        s3m = ctx.stage3_movers_json(heroes)

        synthesis = _run_stage(
            llm,
            kb,
            patch_id,
            4,
            "stage4_synthesis",
            Synthesis,
            **common,
            change_counts=ctx.change_counts(patch),
            meta_md=meta_md,
            stage1_json=s1,
            stage2_json=s2,
            stage3_movers_json=s3m,
        )

    pool_verdicts = None
    if pool:
        pool_verdicts = _run_stage(
            llm,
            kb,
            patch_id,
            5,
            "stage5_pool",
            PoolVerdicts,
            **common,
            stage4_json=synthesis.model_dump_json(indent=1),
            stage3_pool_json=ctx.stage3_pool_json(heroes, pool)
            if heroes
            else HOTFIX_SKIPPED,
            stage2_pool_json=ctx.stage2_pool_json(items, pool)
            if items
            else HOTFIX_SKIPPED,
            heroes_kb_pool=ctx.heroes_kb_pool(kb, pool),
            pool=", ".join(pool),
        )

    # stage 3 owns the per-hero verdict; keep the pool copy identical so
    # the pool section and hero entries can never disagree
    if pool_verdicts and heroes:
        by_hero = {h.hero: h for h in heroes.heroes}
        rewritten = False
        for v in pool_verdicts.verdicts:
            src = by_hero.get(v.hero)
            if src is not None and src.verdict is not None and src.verdict != v.verdict:
                v.verdict = src.verdict
                rewritten = True
        if rewritten:
            (pdir / "stage5.json").write_text(
                pool_verdicts.model_dump_json(indent=1)
            )

    bundle = AnalysisBundle(
        patch_id=patch_id,
        patch_title=patch.title,
        systems=systems,
        items=items,
        heroes=heroes,
        synthesis=synthesis,
        pool=pool_verdicts,
        kb_update=None,
        usage={**llm.usage, "stage_seconds": dict(STAGE_SECONDS)},
    )
    if update_kb and not patch.is_hotfix():
        bundle.kb_update = run_kb_update(patch, kb, bundle, llm)
        bundle.usage = {**llm.usage, "stage_seconds": dict(STAGE_SECONDS)}
    (pdir / "analysis.json").write_text(bundle.model_dump_json(indent=1))
    return bundle


def run_kb_update(patch: Patch, kb: KBStore, bundle: AnalysisBundle, llm) -> KBUpdate:
    if patch.is_hotfix():
        raise ValueError("hotfix patches have no KB update")
    meta_md = kb.load_meta() if kb.meta_path.exists() else "(empty)"
    common = {"patch_title": patch.title, "patch_date": f"{patch.date:%Y-%m-%d}"}
    changed_items = sorted({c.entity_name for c in ctx.item_changes(patch)})
    stage4_json = bundle.synthesis.model_dump_json(indent=1)
    stage2_json = bundle.items.model_dump_json(indent=1)
    meta_update = _run_stage(
        llm,
        kb,
        bundle.patch_id,
        6,
        "stage6_kb_update",
        KBUpdate,
        **common,
        stage4_json=stage4_json,
        stage3_movers_json=ctx.stage3_movers_json(bundle.heroes),
        stage2_json=stage2_json,
        meta_md=meta_md,
        items_kb=ctx.items_kb(kb, changed_items),
    )
    hero_updates: dict[str, dict] = {}
    change_log = list(meta_update.change_log)
    movers = [h for h in bundle.heroes.heroes if h.direction != "neutral"]
    batch_size = config.STAGE6_HERO_BATCH
    for i in range(0, len(movers), batch_size):
        batch = movers[i : i + batch_size]
        out = _run_stage(
            llm,
            kb,
            bundle.patch_id,
            6,
            "stage6_kb_heroes",
            KBHeroUpdate,
            tag=f"6h{i // batch_size + 1}",
            budget_key="6h",
            **common,
            stage4_json=stage4_json,
            stage2_json=stage2_json,
            stage3_json=json.dumps([h.model_dump() for h in batch], indent=1),
            heroes_kb=ctx.heroes_kb_subset(
                kb, [h.hero for h in batch]
            ),
        )
        hero_updates.update(out.hero_updates)
        change_log += out.change_log
    return KBUpdate(
        meta_md=meta_update.meta_md,
        hero_updates=hero_updates,
        item_updates=meta_update.item_updates,
        change_log=change_log,
    )


def apply_kb_update(kb: KBStore, update: KBUpdate) -> list[Path]:
    changed: list[Path] = []
    if update.meta_md:
        kb.save_meta(update.meta_md)
        changed.append(kb.meta_path)

    if update.hero_updates:
        heroes = kb.load_heroes()
        for name, fields in update.hero_updates.items():
            if name not in heroes:
                log.warning("hero update for unknown hero %r, skipping", name)
                continue
            hero = heroes[name]
            for key, value in fields.items():
                if key not in _HERO_FIELDS:
                    log.warning("hero %s: dropping unknown field %r", name, key)
                    continue
                if key == "trend" and value not in _TRENDS:
                    log.warning("hero %s: dropping invalid trend %r", name, value)
                    continue
                if key == "builds":
                    try:
                        value = [Build(**b) for b in value]
                    except (TypeError, ValidationError) as e:
                        log.warning("hero %s: dropping invalid builds: %s", name, e)
                        continue
                try:
                    setattr(hero, key, value)
                except ValidationError as e:
                    log.warning(
                        "hero %s: dropping invalid %s %r: %s", name, key, value, e
                    )
        kb.save_heroes(heroes)
        changed.append(kb.heroes_path)

    if update.item_updates:
        items = kb.load_items()
        for name, fields in update.item_updates.items():
            item = items.get(name, ItemState(name=name))
            for key, value in fields.items():
                if key not in _ITEM_FIELDS:
                    log.warning("item %s: dropping unknown field %r", name, key)
                    continue
                try:
                    setattr(item, key, value)
                except ValidationError as e:
                    log.warning(
                        "item %s: dropping invalid %s %r: %s", name, key, value, e
                    )
            items[name] = item
        kb.save_items(items)
        changed.append(kb.items_path)

    return changed


def dump_json(data) -> str:
    return json.dumps(data, indent=1, default=str)
