import re

_TAG_RE = re.compile(r"\[/?[a-zA-Z][a-zA-Z0-9*]*(?:=[^\]]*)?\]")
_HEADER_RE = re.compile(r"^\[\s*(?P<section>.+?)\s*\]$")


def _strip_tags(text: str) -> str:
    return _TAG_RE.sub("", text).strip()


def bbcode_to_lines(contents: str) -> list[tuple[str, str]]:
    """Split BBCode patch-note contents into (section, line) pairs.

    Paragraphs are [p]...[/p]. A paragraph whose stripped text looks like
    "[ Section ]" is a header. Lines starting with "- " are changes, as are
    "[*]" list entries; other non-empty paragraphs are kept too.
    """
    contents = contents.replace("\\[", "[").replace("\\]", "]")
    # expand [list][*]item[/list] blocks into "- item" paragraphs
    contents = re.sub(
        r"\[list\](.*?)\[/list\]",
        lambda m: "".join(
            f"[p]- {entry}[/p]" for entry in m.group(1).split("[*]") if entry.strip()
        ),
        contents,
        flags=re.DOTALL,
    )
    lines: list[tuple[str, str]] = []
    section = "General"

    paragraphs = re.findall(r"\[p\](.*?)\[/p\]", contents, flags=re.DOTALL)
    if not paragraphs:
        paragraphs = [contents]

    for para in paragraphs:
        para = para.replace("\r", "")

        text = _strip_tags(para)
        if not text:
            continue
        header = _HEADER_RE.match(text)
        if header:
            section = header.group("section").strip()
            continue

        for raw_line in text.split("\n"):
            line = raw_line.strip()
            if not line:
                continue
            continuation = not line.startswith("- ") and (
                line[0].islower() or line[0] in "),"
            )
            if line.startswith("- "):
                line = line[2:].strip()
            if not line:
                continue
            if continuation and lines and lines[-1][0] == section:
                prev_section, prev = lines[-1]
                lines[-1] = (prev_section, f"{prev} {line}")
            else:
                lines.append((section, line))

    return lines
