import logging
import subprocess
from pathlib import Path

log = logging.getLogger(__name__)


def git_sync(repo_root: Path) -> bool:
    """Pull --rebase --autostash; on failure abort any in-progress rebase.
    Never raises; returns False when the sync failed."""
    repo_root = Path(repo_root)
    try:
        subprocess.run(
            ["git", "pull", "--rebase", "--autostash"],
            cwd=repo_root,
            check=True,
            capture_output=True,
            timeout=60,
        )
        return True
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        if (repo_root / ".git" / "rebase-merge").exists() or (
            repo_root / ".git" / "rebase-apply"
        ).exists():
            subprocess.run(
                ["git", "rebase", "--abort"],
                cwd=repo_root,
                check=False,
                capture_output=True,
            )
        log.warning("git sync failed: %s", e)
        return False


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
    if git_sync(repo_root):
        try:
            subprocess.run(
                ["git", "push"],
                cwd=repo_root,
                check=True,
                capture_output=True,
                timeout=60,
            )
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
            log.warning("kb commit not pushed: %s", e)
    else:
        log.warning("kb commit left unpushed: git sync failed")
    return out.stdout.strip()


def kb_commit_message(patch_title: str, change_log: list[str]) -> str:
    body = "\n".join(change_log[:5])
    return f"kb: {patch_title}\n\n{body}" if body else f"kb: {patch_title}"
