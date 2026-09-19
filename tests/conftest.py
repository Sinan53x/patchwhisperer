import json
from datetime import UTC, datetime
from pathlib import Path

import pytest

from patchwhisperer.parse.entities import EntityIndex
from patchwhisperer.sources.steam_news import SteamPost

FIXTURES = Path(__file__).parent / "fixtures"


@pytest.fixture(scope="session")
def entity_index() -> EntityIndex:
    assets = FIXTURES / "assets"
    return EntityIndex(
        json.loads((assets / "heroes.json").read_text()),
        json.loads((assets / "items.json").read_text()),
        {
            int(k): v
            for k, v in json.loads((assets / "abilities.json").read_text()).items()
        },
    )


def load_post(date: str) -> SteamPost:
    it = json.loads((FIXTURES / "steam" / f"{date}.json").read_text())
    return SteamPost(
        gid=str(it["gid"]),
        title=it["title"],
        date=datetime.fromtimestamp(it["date"], tz=UTC),
        url=it["url"],
        author=it["author"],
        contents=it["contents"],
    )
