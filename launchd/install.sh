#!/bin/sh
# Install the PatchWhisperer launchd agent. Safe to re-run.
set -eu

REPO="$(cd "$(dirname "$0")/.." && pwd)"
LABEL=com.patchwhisperer
DEST="$HOME/Library/LaunchAgents/$LABEL.plist"
LOGS="$HOME/Library/Logs/patchwhisperer"

mkdir -p "$LOGS" "$HOME/Library/LaunchAgents"
sed "s|__REPO__|$REPO|g" "$REPO/launchd/$LABEL.plist" > "$DEST"

launchctl bootout "gui/$(id -u)/$LABEL" 2>/dev/null || true
launchctl bootstrap "gui/$(id -u)" "$DEST"
launchctl kickstart -k "gui/$(id -u)/$LABEL"

echo "installed $LABEL (repo: $REPO)"
echo "logs: tail -f $LOGS/stdout.log $LOGS/stderr.log"
echo "NOTE: to keep the Mac awake for the poller, run: sudo pmset -a sleep 0"
