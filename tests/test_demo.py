from pathlib import Path

from typer.testing import CliRunner

from patchwhisperer.cli import app

runner = CliRunner()


def test_demo_offline_run():
    kb_files = ["heroes.yaml", "items.yaml", "meta.md", "corrections.md"]
    before = {f: Path("kb", f).read_bytes() for f in kb_files}
    result = runner.invoke(app, ["demo"])
    assert result.exit_code == 0, result.output
    assert "**[MAJOR]**" in result.output
    assert "Discord TL;DR" in result.output
    assert "no API calls made" in result.output
    after = {f: Path("kb", f).read_bytes() for f in kb_files}
    assert before == after
