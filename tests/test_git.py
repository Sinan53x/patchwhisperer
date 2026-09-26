import subprocess

from patchwhisperer.kb.git import git_commit_kb, kb_commit_message


def _repo(tmp_path):
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    subprocess.run(
        [
            "git",
            "-c",
            "user.name=t",
            "-c",
            "user.email=t@t",
            "commit",
            "-qm",
            "init",
            "--allow-empty",
        ],
        cwd=tmp_path,
        check=True,
    )
    return tmp_path


def test_commit_returns_hash(tmp_path):
    repo = _repo(tmp_path)
    f = repo / "heroes.yaml"
    f.write_text("Wraith: {}\n")
    h = git_commit_kb(repo, [f], "kb: test patch")
    assert h and len(h) >= 7


def test_nothing_to_commit(tmp_path):
    repo = _repo(tmp_path)
    f = repo / "heroes.yaml"
    f.write_text("x\n")
    assert git_commit_kb(repo, [f], "kb: a") is not None
    assert git_commit_kb(repo, [f], "kb: b") is None


def test_directory_path_stages_new_files(tmp_path):
    repo = _repo(tmp_path)
    pdir = repo / "patches" / "p1"
    pdir.mkdir(parents=True)
    (pdir / "stage1.json").write_text("{}\n")
    (pdir / "stage1.prompt.md").write_text("x\n")
    h = git_commit_kb(repo, [pdir], "kb: dir test")
    assert h is not None
    out = subprocess.run(
        ["git", "show", "--name-only", "--format=", "HEAD"],
        cwd=repo,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.split()
    assert "patches/p1/stage1.json" in out
    assert "patches/p1/stage1.prompt.md" in out


def test_message_format():
    msg = kb_commit_message("Minor Update - 09-16-2026", ["a", "b"])
    assert msg == "kb: Minor Update - 09-16-2026\n\na\nb"
