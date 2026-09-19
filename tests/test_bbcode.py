import json
import re

from conftest import FIXTURES

from patchwhisperer.parse.bbcode import bbcode_to_lines


def _contents(date: str) -> str:
    return json.loads((FIXTURES / "steam" / f"{date}.json").read_text())["contents"]


def test_sections_detected_0916() -> None:
    lines = bbcode_to_lines(_contents("09-16-2026"))
    sections = {s for s, _ in lines}
    assert {"General", "Items", "Heroes"} <= sections


def test_change_count_0916() -> None:
    lines = bbcode_to_lines(_contents("09-16-2026"))
    assert len(lines) == 122  # 17 General + 36 Items + 69 Heroes


def test_continuation_line_merged() -> None:
    lines = bbcode_to_lines(_contents("09-16-2026"))
    assert not any(line.startswith("to toggle") for _, line in lines)


def test_no_bbcode_left() -> None:
    for date in ("09-16-2026", "08-22-2026", "05-22-2026", "03-06-2026"):
        for section, line in bbcode_to_lines(_contents(date)):
            assert not re.search(r"\[/?[a-zA-Z*]", line), (date, line)
            assert section
            assert line.strip() == line


def test_list_markup_handled() -> None:
    lines = bbcode_to_lines(
        "[p][b]\\[ Heroes ][/b][/p][list][*]Abrams: x[*]Wraith: y[/list]"
    )
    assert ("Heroes", "Abrams: x") in lines
    assert ("Heroes", "Wraith: y") in lines
