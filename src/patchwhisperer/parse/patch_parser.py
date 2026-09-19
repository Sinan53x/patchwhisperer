import re

from patchwhisperer.parse.bbcode import bbcode_to_lines
from patchwhisperer.parse.entities import EntityIndex
from patchwhisperer.parse.models import Change, Direction, EntityType, Patch
from patchwhisperer.sources.steam_news import SteamPost

ENTITY_RE = re.compile(r"^(?P<entity>[^:]{2,40}):\s+(?P<text>.+)$")
FROM_TO_RE = re.compile(r"from\s+(?P<old>.+?)\s+to\s+(?P<new>.+?)(?:\s*\(|$)")
TIER_RE = re.compile(r"\bT([123])\b")

# stat polarity: True = more is good (up=buff, down=nerf)
# False = more is bad (up=nerf, down=buff), None = always neutral
STAT_POLARITY: dict[str, bool | None] = {
    "falloff range": True,
    "respawn time": False,
    "cycle time": False,
    "reload time": False,
    "reload": False,
    "spawn time": None,
    "charge time": False,
    "wind up": False,
    "windup": False,
    "cast range": True,
    "projectile speed": True,
    "move speed": True,
    "sprint": True,
    "lifesteal": True,
    "stun": True,
    "silence": True,
    "root": True,
    "knockup": True,
    "heal on cast": True,
    "damage": True,
    "heal": True,
    "health": True,
    "hp": True,
    "regen": True,
    "range": True,
    "radius": True,
    "duration": True,
    "speed": True,
    "fire rate": True,
    "resist": True,
    "scaling": True,
    "armor": True,
    "shield": True,
    "barrier": True,
    "bonus": True,
    "souls": True,
    "bounty": True,
    "ammo": True,
    "stamina": True,
    "spirit power": True,
    "cooldown": False,
    "cost": False,
    "cast time": False,
    "delay": False,
    "falloff": False,
    "damage taken": False,
    "penalty": False,
    "buildup": False,
}

# entity-type-dependent polarity, consulted before STAT_POLARITY
CONTEXT_POLARITY: dict[str, dict[EntityType, bool | None]] = {
    "slow": {
        EntityType.hero: True,
        EntityType.item: True,
        EntityType.system: None,
        EntityType.unknown: True,
    },
}

_FIX_RE = re.compile(r"\bfixed\b|\bfix\b", re.IGNORECASE)
_REWORK_RE = re.compile(r"\bnow\b|no longer|reworked|replaced", re.IGNORECASE)
_INCREASE_RE = re.compile(r"increas|raised|up from|gains|added", re.IGNORECASE)
_DECREASE_RE = re.compile(r"reduc|decreas|lowered|down from|removed", re.IGNORECASE)


_STATS_BY_LEN = sorted(STAT_POLARITY.items(), key=lambda kv: -len(kv[0]))
_CONTEXT_STATS_BY_LEN = sorted(CONTEXT_POLARITY.items(), key=lambda kv: -len(kv[0]))


def _match_field(text: str, entity_type: EntityType) -> tuple[str, bool | None] | None:
    text_l = text.lower()
    for stat, by_type in _CONTEXT_STATS_BY_LEN:
        if re.search(rf"\b{re.escape(stat)}\b", text_l):
            return stat, by_type.get(entity_type)
    for stat, good in _STATS_BY_LEN:
        if re.search(rf"\b{re.escape(stat)}\b", text_l):
            return stat, good
    return None


def _direction(text: str, field_info: tuple[str, bool | None] | None) -> Direction:
    if _FIX_RE.search(text):
        return Direction.fix
    has_from_to = FROM_TO_RE.search(text) is not None
    if _REWORK_RE.search(text) and not has_from_to:
        return Direction.rework
    if "changed from" in text.lower() and not re.search(r"\d", text):
        return Direction.rework
    up = bool(_INCREASE_RE.search(text))
    down = bool(_DECREASE_RE.search(text))
    if up == down:
        if has_from_to and field_info:
            m = FROM_TO_RE.search(text)
            old, new = m.group("old"), m.group("new")
            nums_old = re.findall(r"-?[\d.]+", old)
            nums_new = re.findall(r"-?[\d.]+", new)
            if nums_old and nums_new:
                try:
                    up = float(nums_new[-1]) > float(nums_old[-1])
                    down = float(nums_new[-1]) < float(nums_old[-1])
                except ValueError:
                    pass
        if up == down:
            return Direction.neutral
    if field_info is None:
        return Direction.neutral
    _, good = field_info
    if good is None:
        return Direction.neutral
    if up:
        return Direction.buff if good else Direction.nerf
    return Direction.nerf if good else Direction.buff


def _parse_change(section: str, line: str, index: EntityIndex) -> Change:
    entity_type = EntityType.system
    entity_id = None
    entity_name = "General"
    ability = None
    resolved = True  # system lines have no entity to resolve
    text = line

    m = ENTITY_RE.match(line)
    if m:
        cand = m.group("entity").strip()
        text = m.group("text").strip()
        hit = index.resolve(cand)
        if hit:
            entity_type, entity_id, entity_name = hit
            resolved = True
            if entity_type == EntityType.hero:
                ability = index.ability_for(entity_id, text)
        elif cand.lower() == "general":
            entity_type = EntityType.system
            entity_name = "General"
        elif section == "Heroes":
            entity_type = EntityType.unknown
            entity_name = cand
            resolved = False
        else:
            entity_name = cand
            entity_type = EntityType.unknown
            resolved = False

    old = new = None
    ft = FROM_TO_RE.search(text)
    if ft:
        old, new = ft.group("old").strip(), ft.group("new").strip()
    tier_m = TIER_RE.search(text)
    field_info = _match_field(text, entity_type)
    direction = _direction(text, field_info)

    return Change(
        section=section,
        entity_type=entity_type,
        entity_id=entity_id,
        entity_name=entity_name,
        ability=ability,
        tier=int(tier_m.group(1)) if tier_m else None,
        field=field_info[0] if field_info else None,
        old=old,
        new=new,
        raw=line,
        direction=direction,
        resolved=resolved,
    )


def parse_patch(post: SteamPost, index: EntityIndex) -> Patch:
    changes = [
        _parse_change(section, line, index)
        for section, line in bbcode_to_lines(post.contents)
    ]
    return Patch(
        gid=post.gid,
        title=post.title,
        date=post.date,
        url=post.url,
        author=post.author,
        raw_bbcode=post.contents,
        changes=changes,
    )
