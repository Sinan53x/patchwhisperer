import logging
import subprocess
from pathlib import Path

log = logging.getLogger(__name__)


def git_commit_kb(repo_root: Path, paths: list[Path], message: str) -> str | None:
    """Stage and commit KB changes; returns short hash or None if nothing to commit."""
    repo_root = Path(repo_root)
    if not paths:
        return None
    rel = [str(Path(p).relative_to(repo_root)) for p in paths]
    subprocess.run(["git", "add", "--"] + rel, cwd=repo_root, check=True)
    diff = subprocess.run(
        ["git", "diff", "--cached", "--quiet"], cwd=repo_root, check=False
    )
    if diff.returncode == 0:
        return None
    subprocess.run(
        [
            "git",
            "-c",
            "user.name=PatchWhisperer",
            "-c",
            "user.email=patchwhisperer@localhost",
            "commit",
            "-m",
            message,
        ],
        cwd=repo_root,
        check=True,
        capture_output=True,
    )
    out = subprocess.run(
        ["git", "rev-parse", "--short", "HEAD"],
        cwd=repo_root,
        check=True,
        capture_output=True,
        text=True,
    )
    try:
        subprocess.run(
            ["git", "push"], cwd=repo_root, check=True, capture_output=True, timeout=60
        )
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        log.warning("kb commit not pushed: %s", e)
    return out.stdout.strip()


def kb_commit_message(patch_title: str, change_log: list[str]) -> str:
    body = "\n".join(change_log[:5])
    return f"kb: {patch_title}\n\n{body}" if body else f"kb: {patch_title}"
