import logging

from patchwhisperer.analysis.llm import SYSTEM_PROMPT, render_prompt
from patchwhisperer.analysis.pipeline import _NUM_TOKEN, _has_number
from patchwhisperer.analysis.schemas import SeasonBundle, SeasonRule
from patchwhisperer.kb.store import KBStore
from patchwhisperer.parse.bbcode import bbcode_to_lines
from patchwhisperer.sources.steam_news import SteamPost

log = logging.getLogger(__name__)


def _guard_rules(rules: list[SeasonRule], source: str) -> list[SeasonRule]:
    """Drop rules whose before/after numbers do not appear verbatim in the post."""
    kept = []
    for r in rules:
        fields = " ".join(x for x in (r.before, r.after) if x)
        missing = [
            t
            for t in _NUM_TOKEN.findall(fields)
            if not _has_number(t.lstrip("+-"), source)
        ]
        if missing:
            log.warning(
                "season: dropping rule with number(s) not in the post %s: %r",
                missing,
                r.label,
            )
        else:
            kept.append(r)
    return kept


def extract_season(post: SteamPost, kb: KBStore, llm) -> SeasonBundle:
    """One LLM call: Steam announcement -> season.json in the patch dir."""
    patch_id = f"{post.date:%Y-%m-%d}-{post.gid}"
    body = "\n".join(line for _, line in bbcode_to_lines(post.contents))
    prompt = render_prompt(
        "season_extract",
        post_title=post.title,
        post_date=f"{post.date:%Y-%m-%d}",
        post_body=body or "(empty)",
    )
    bundle: SeasonBundle = llm.complete_json(SYSTEM_PROMPT, prompt, SeasonBundle)
    bundle.rules = _guard_rules(bundle.rules, body)
    bundle.gid = post.gid
    bundle.title = post.title
    bundle.date = f"{post.date:%Y-%m-%d}"
    bundle.url = post.url
    pdir = kb.patch_dir(patch_id)
    (pdir / "season.prompt.md").write_text(prompt)
    (pdir / "season.json").write_text(bundle.model_dump_json(indent=1))
    return bundle
