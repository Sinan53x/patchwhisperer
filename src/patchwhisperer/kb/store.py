from pathlib import Path

import yaml
from pydantic import BaseModel

from patchwhisperer.kb.schema import HeroState, ItemState


def slugify(text: str) -> str:
    return "".join(c.lower() if c.isalnum() else "-" for c in text).strip("-")


def _dump(models: dict[str, BaseModel]) -> str:
    return yaml.safe_dump(
        {k: v.model_dump() for k, v in models.items()},
        sort_keys=False,
        allow_unicode=True,
    )


class KBStore:
    def __init__(self, root: Path) -> None:
        self.root = Path(root)

    @property
    def heroes_path(self) -> Path:
        return self.root / "heroes.yaml"

    @property
    def items_path(self) -> Path:
        return self.root / "items.yaml"

    @property
    def meta_path(self) -> Path:
        return self.root / "meta.md"

    def load_heroes(self) -> dict[str, HeroState]:
        data = yaml.safe_load(self.heroes_path.read_text()) or {}
        return {k: HeroState(**v) for k, v in data.items()}

    def save_heroes(self, heroes: dict[str, HeroState]) -> None:
        self.heroes_path.write_text(_dump(heroes))

    def load_items(self) -> dict[str, ItemState]:
        if not self.items_path.exists():
            return {}
        data = yaml.safe_load(self.items_path.read_text()) or {}
        return {k: ItemState(**v) for k, v in data.items()}

    def save_items(self, items: dict[str, ItemState]) -> None:
        self.items_path.write_text(_dump(items))

    def load_meta(self) -> str:
        return self.meta_path.read_text()

    def load_corrections(self) -> str:
        p = self.root / "corrections.md"
        return p.read_text() if p.exists() else ""

    def save_meta(self, text: str) -> None:
        self.meta_path.write_text(text)

    def add_bought_by(self, hero_name: str, item_names: list[str]) -> bool:
        items = self.load_items()
        changed = False
        for item_name in item_names:
            item = items.get(item_name, ItemState(name=item_name))
            if hero_name not in item.bought_by:
                item.bought_by = sorted(set(item.bought_by) | {hero_name})
                items[item_name] = item
                changed = True
        if changed:
            self.save_items(items)
        return changed

    def patch_dir(self, patch_id: str) -> Path:
        d = self.root / "patches" / patch_id
        d.mkdir(parents=True, exist_ok=True)
        return d

    def write_patch_artifact(
        self, patch_id: str, name: str, content: str | dict
    ) -> Path:
        p = self.patch_dir(patch_id) / name
        if isinstance(content, dict):
            import json

            p.write_text(json.dumps(content, indent=1, default=str))
        else:
            p.write_text(content)
        return p
