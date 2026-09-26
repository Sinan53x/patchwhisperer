import subprocess

from patchwhisperer.kb.git import git_commit_kb, git_sync, kb_commit_message


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


def _run(args, cwd):
    return subprocess.run(
        args, cwd=cwd, check=True, capture_output=True, text=True
    ).stdout


def _clone_pair(tmp_path):
    """Bare remote + clones a/ (bot) and b/ (MacBook)."""
    remote = tmp_path / "remote.git"
    _run(["git", "init", "-q", "--bare", str(remote)], tmp_path)
    seed = tmp_path / "seed"
    seed.mkdir()
    _run(["git", "init", "-q"], seed)
    (seed / "tracked.txt").write_text("base\n")
    _run(["git", "add", "."], seed)
    _run(
        [
            "git",
            "-c",
            "user.name=t",
            "-c",
            "user.email=t@t",
            "commit",
            "-qm",
            "init",
        ],
        seed,
    )
    _run(["git", "remote", "add", "origin", str(remote)], seed)
    _run(["git", "push", "-q", "origin", "HEAD:master"], seed)
    a = tmp_path / "a"
    b = tmp_path / "b"
    _run(["git", "clone", "-q", str(remote), str(a)], tmp_path)
    _run(["git", "clone", "-q", str(remote), str(b)], tmp_path)
    for c in (a, b):
        _run(["git", "config", "user.name", "t"], c)
        _run(["git", "config", "user.email", "t@t"], c)
    return remote, a, b


def _commit_file(repo, name, content, msg="c"):
    (repo / name).write_text(content)
    _run(["git", "add", name], repo)
    _run(["git", "commit", "-qm", msg], repo)


def test_sync_pulls_and_push_rebases(tmp_path):
    remote, a, b = _clone_pair(tmp_path)
    # MacBook commits and pushes a different file
    _commit_file(b, "corrections.md", "fix wraith\n")
    _run(["git", "push", "-q"], b)
    # bot has unrelated dirty + untracked files
    (a / "tracked.txt").write_text("dirty\n")
    (a / "untracked.tmp").write_text("x\n")
    (a / "heroes.yaml").write_text("Wraith: {}\n")
    h = git_commit_kb(a, [a / "heroes.yaml"], "kb: test")
    assert h is not None
    remote_files = _run(
        ["git", "ls-tree", "-r", "--name-only", "HEAD"], remote
    ).split()
    assert "heroes.yaml" in remote_files
    assert "corrections.md" in remote_files
    # unrelated dirty/untracked files preserved
    assert (a / "tracked.txt").read_text() == "dirty\n"
    assert (a / "untracked.tmp").exists()


def test_sync_conflict_skips_push(tmp_path):
    remote, a, b = _clone_pair(tmp_path)
    _commit_file(b, "tracked.txt", "B wins\n")
    _run(["git", "push", "-q"], b)
    _commit_file(a, "tracked.txt", "A edit\n")
    assert git_sync(a) is False
    # no rebase left in progress
    assert not (a / ".git" / "rebase-merge").exists()
    assert not (a / ".git" / "rebase-apply").exists()
    # local commit still there
    assert "A edit" in _run(["git", "log", "-1", "--format=%s"], a) or (
        a / "tracked.txt"
    ).read_text() == "A edit\n"
    # push skipped: remote still has B's version only
    remote_head = _run(["git", "log", "--format=%s", "HEAD"], remote)
    assert remote_head.strip().count("\n") == 1  # init + B's commit only


def test_message_format():
    msg = kb_commit_message("Minor Update - 09-16-2026", ["a", "b"])
    assert msg == "kb: Minor Update - 09-16-2026\n\na\nb"
