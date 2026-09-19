import json
import logging
import time
from pathlib import Path

from patchwhisperer import config
from patchwhisperer.analysis import context as ctx
from patchwhisperer.analysis.llm import SYSTEM_PROMPT, render_prompt
from patchwhisperer.analysis.schemas import (
    AnalysisBundle,
    HeroAnalysis,
    ItemAnalysis,
    KBUpdate,
    PoolVerdicts,
    Synthesis,
    SystemsAnalysis,
)
from patchwhisperer.kb.schema import ItemState
from patchwhisperer.kb.store import KBStore
from patchwhisperer.parse.models import Patch

log = logging.getLogger(__name__)

HOTFIX_SKIPPED = "(hotfix: stage skipped)"

_HERO_FIELDS = {
    "role",
    "archetypes",
    "tier",
    "trend",
    "why",
    "core_items",
    "build_variants",
    "enabled_by",
    "countered_by",
    "last_changed_patch",
    "notes",
}
_ITEM_FIELDS = {"role", "bought_by", "slot", "tier", "notes"}
_TIERS = {"S", "A", "B", "C", "D", "?"}
_TRENDS = {"rising", "stable", "falling", "?"}


def patch_id_of(patch: Patch) -> str:
    return f"{patch.date:%Y-%m-%d}-{patch.gid}"


STAGE_SECONDS: dict[int, float] = {}


def _run_stage(
    llm,
    kb: KBStore,
    patch_id: str,
    n: int,
    name: str,
    schema,
    **values,
):
    prompt = render_prompt(name, **values)
    pdir = kb.patch_dir(patch_id)
    t0 = time.time()
    result = llm.complete_json(
        SYSTEM_PROMPT,
        prompt,
        schema,
        max_tokens=config.STAGE_MAX_TOKENS[n],
        raw_path=pdir / f"stage{n}.raw.txt",
    )
    elapsed = time.time() - t0
    STAGE_SECONDS[n] = elapsed
    log.info("stage %d (%s) done in %.1fs", n, name, elapsed)
    (pdir / f"stage{n}.prompt.md").write_text(prompt)
    (pdir / f"stage{n}.json").write_text(result.model_dump_json(indent=1))
    return result


def run_analysis(
    patch: Patch,
    kb: KBStore,
    snapshot: dict,
    pool: list[str],
    llm,
    *,
    update_kb: bool = True,
) -> AnalysisBundle:
    STAGE_SECONDS.clear()
    patch_id = patch_id_of(patch)
    meta_md = kb.load_meta() if kb.meta_path.exists() else "(empty)"
    common = {"patch_title": patch.title, "patch_date": f"{patch.date:%Y-%m-%d}"}
    sys_changes = ctx.system_changes(patch)
    it_changes = ctx.item_changes(patch)
    h_changes = ctx.hero_changes(patch)
    changed_items = sorted({c.entity_name for c in it_changes})
    changed_heroes = sorted({c.entity_name for c in h_changes})
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

        item_hero_names = ctx.hero_names_affected_by_items(kb, changed_items)
        items = _run_stage(
            llm,
            kb,
            patch_id,
            2,
            "stage2_items",
            ItemAnalysis,
            **common,
            stage1_json=s1,
            item_changes=ctx.format_changes(it_changes),
            items_kb=ctx.items_kb(kb, changed_items),
            heroes_kb_subset=ctx.heroes_kb_subset(kb, item_hero_names),
        )
        s2 = items.model_dump_json(indent=1)

        heroes = _run_stage(
            llm,
            kb,
            patch_id,
            3,
            "stage3_heroes",
            HeroAnalysis,
            **common,
            stage1_json=s1,
            stage2_json=s2,
            hero_changes=ctx.format_changes(h_changes),
            heroes_kb=ctx.heroes_kb(kb),
            snapshot=snap_txt,
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

    kb_update = None
    if update_kb and not patch.is_hotfix():
        kb_update = _run_stage(
            llm,
            kb,
            patch_id,
            6,
            "stage6_kb_update",
            KBUpdate,
            **common,
            stage4_json=synthesis.model_dump_json(indent=1),
            stage3_movers_json=s3m,
            stage2_json=s2,
            meta_md=meta_md,
            heroes_kb_movers=ctx.heroes_kb_movers(kb, heroes),
            items_kb=ctx.items_kb(kb, changed_items),
        )

    bundle = AnalysisBundle(
        patch_id=patch_id,
        patch_title=patch.title,
        systems=systems,
        items=items,
        heroes=heroes,
        synthesis=synthesis,
        pool=pool_verdicts,
        kb_update=kb_update,
        usage={**llm.usage, "stage_seconds": dict(STAGE_SECONDS)},
    )
    pdir = kb.patch_dir(patch_id)
    (pdir / "analysis.json").write_text(bundle.model_dump_json(indent=1))
    return bundle


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
                if key == "tier" and value not in _TIERS:
                    log.warning("hero %s: dropping invalid tier %r", name, value)
                    continue
                if key == "trend" and value not in _TRENDS:
                    log.warning("hero %s: dropping invalid trend %r", name, value)
                    continue
                setattr(hero, key, value)
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
                setattr(item, key, value)
            items[name] = item
        kb.save_items(items)
        changed.append(kb.items_path)

    return changed


def dump_json(data) -> str:
    return json.dumps(data, indent=1, default=str)
