import logging

from patchwhisperer.analysis.pipeline import _run_stage, patch_id_of
from patchwhisperer.analysis.schemas import ContentDigest
from patchwhisperer.kb.store import KBStore
from patchwhisperer.parse.bbcode import bbcode_to_lines
from patchwhisperer.parse.entities import EntityIndex
from patchwhisperer.parse.models import Change, Direction, EntityType, Patch
from patchwhisperer.parse.patch_parser import (
    _direction,
    _match_field,
    parse_change_line,
    parse_patch,
)
from patchwhisperer.sources.steam_news import PostKind, SteamPost
from patchwhisperer.sources.update_page import (
    fetch_update_page_text,
    update_page_slug,
)

log = logging.getLogger(__name__)


def _entity_part(line: str, default: str) -> str:
    return line.split(":", 1)[0].strip() if ":" in line else default


def digest_to_changes(digest: ContentDigest, index: EntityIndex) -> list[Change]:
    changes: list[Change] = []
    for section, lines in digest.sections.items():
        for line in lines:
            if section == "Items":
                changes.append(parse_change_line("Items", line, index))
                continue
            if section == "Heroes":
                cand = _entity_part(line, line)
                hit = index.resolve(cand)
                if hit and hit[0] == EntityType.hero:
                    entity_type, entity_id, entity_name = hit
                    resolved = True
                else:
                    entity_type, entity_id, entity_name = (
                        EntityType.unknown,
                        None,
                        cand,
                    )
                    resolved = False
                text = line.split(":", 1)[1].strip() if ":" in line else line
                if "new hero" in line.lower():
                    direction = Direction.rework
                else:
                    direction = _direction(
                        text, _match_field(text, entity_type)
                    )
                changes.append(
                    Change(
                        section="Heroes",
                        entity_type=entity_type,
                        entity_id=entity_id,
                        entity_name=entity_name,
                        raw=line,
                        direction=direction,
                        resolved=resolved,
                    )
                )
                continue
            entity_name = _entity_part(line, section)
            field_info = _match_field(line, EntityType.system)
            changes.append(
                Change(
                    section=section,
                    entity_type=EntityType.system,
                    entity_name=entity_name,
                    field=field_info[0] if field_info else None,
                    raw=line,
                    direction=_direction(line, field_info),
                    resolved=True,
                )
            )
    return changes


def prepare_patch(
    post: SteamPost,
    index: EntityIndex,
    kb: KBStore,
    llm,
    *,
    notes: str | None = None,
) -> Patch:
    """parse_patch plus, for major updates, a stage-0 digest of the update page."""
    patch = parse_patch(post, index)
    if patch.kind != PostKind.major:
        return patch
    patch_id = patch_id_of(patch)
    pdir = kb.patch_dir(patch_id)

    update_page = notes
    if update_page is None:
        notes_path = pdir / "notes.md"
        if notes_path.exists():
            update_page = notes_path.read_text()
    if update_page is None:
        try:
            slug = update_page_slug(post.contents)
            if slug is None:
                raise RuntimeError("no playdeadlock.com link in post body")
            update_page = fetch_update_page_text(slug)
        except Exception as e:  # noqa: BLE001 - any failure falls back to steam body
            log.warning("update page fetch failed for %s: %s", patch_id, e)
            update_page = None
    if update_page:
        (pdir / "update_page.txt").write_text(update_page)

    steam_body = "\n".join(line for _, line in bbcode_to_lines(post.contents))
    digest: ContentDigest = _run_stage(
        llm,
        kb,
        patch_id,
        0,
        "stage0_digest",
        ContentDigest,
        patch_title=patch.title,
        patch_date=f"{patch.date:%Y-%m-%d}",
        steam_body=steam_body or "(empty)",
        update_page=update_page or "(unavailable)",
        hero_names=", ".join(h["name"] for h in index.heroes),
    )
    return patch.model_copy(
        update={
            "changes": patch.changes + digest_to_changes(digest, index),
            "digest_summary": digest.summary,
            "new_heroes": digest.new_heroes,
        }
    )
