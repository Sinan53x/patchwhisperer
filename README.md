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
pw enrich --all          # refresh hero builds/matchups from item-usage + counter data
pw bot                   # run the Discord bot + patch poller
```

## Deploy (always-on host)

The bot is designed to run on one always-on machine (e.g. a Mac mini) with the
git repo as the single source of truth — KB commits are pushed automatically
after each analysis, so pull before working elsewhere.

```sh
git clone <repo-url> && cd PatchWhisperer
uv sync
# copy .env and state.db onto the host — both are gitignored
./launchd/install.sh     # launchd keepalive, logs in ~/Library/Logs/patchwhisperer
```

`git push` needs credentials on the host (e.g. `gh auth login` or an SSH remote).
Run exactly one bot instance — two instances have separate `state.db`s and will
double-post.

## Tests

```sh
uv run pytest
```
