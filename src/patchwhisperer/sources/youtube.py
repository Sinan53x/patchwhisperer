import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

from pydantic import BaseModel

TIMESTAMP_RE = re.compile(
    r"^\d{2}:\d{2}:\d{2}[.,]\d{3}\s+-->\s+\d{2}:\d{2}:\d{2}[.,]\d{3}"
)
TAG_RE = re.compile(r"<[^>]+>")


class Transcript(BaseModel):
    video_id: str
    title: str
    author: str
    text: str
    upload_date: str | None = None


def _yt_dlp() -> str:
    for cand in ("/opt/homebrew/bin/yt-dlp", shutil.which("yt-dlp") or ""):
        if cand and Path(cand).exists():
            return cand
    raise RuntimeError("yt-dlp not found")


def _vtt_to_text(vtt: str) -> str:
    seen = set()
    out = []
    for line in vtt.splitlines():
        line = line.strip()
        if (
            not line
            or line == "WEBVTT"
            or TIMESTAMP_RE.match(line)
            or line.startswith(("Kind:", "Language:", "NOTE"))
        ):
            continue
        line = TAG_RE.sub("", line)
        if line and line not in seen:
            seen.add(line)
            out.append(line)
    return "\n".join(out)


def fetch_transcript(url: str) -> Transcript:
    yt = _yt_dlp()
    with tempfile.TemporaryDirectory() as tmp:
        meta = subprocess.run(
            [yt, "-J", "--skip-download", url],
            capture_output=True,
            text=True,
            check=True,
        )
        info = json.loads(meta.stdout)
        subprocess.run(
            [
                yt,
                "--write-auto-sub",
                "--sub-lang",
                "en",
                "--skip-download",
                "--sub-format",
                "vtt",
                "-o",
                f"{tmp}/%(id)s",
                url,
            ],
            capture_output=True,
            text=True,
            check=True,
        )
        vtt_files = list(Path(tmp).glob("*.vtt"))
        if not vtt_files:
            raise RuntimeError(f"no subtitles downloaded for {url}")
        text = _vtt_to_text(vtt_files[0].read_text())
    return Transcript(
        video_id=info["id"],
        title=info.get("title", ""),
        author=info.get("uploader", ""),
        text=text,
        upload_date=info.get("upload_date"),
    )
