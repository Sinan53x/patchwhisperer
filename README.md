# PatchWhisperer

A Deadlock Discord bot that turns Valve patch notes into meta analysis backed by a
persistent, git-versioned knowledge base.

## Setup

```sh
uv sync
cp .env.example .env   # fill in tokens
```

## CLI

```sh
pw fetch [--count N]     # list recent patch posts
pw parse <gid|latest>    # parse a patch into structured changes
pw kb init               # seed kb/heroes.yaml from live assets
pw ingest <youtube_url>  # fetch transcript into kb/sources/raw/
pw snapshot              # top-10 heroes by win rate (last 14 days)
```

## Tests

```sh
uv run pytest
```
