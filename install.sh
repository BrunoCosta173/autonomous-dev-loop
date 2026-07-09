#!/bin/sh
set -eu

ARCHIVE_URL=${AUTONOMOUS_DEV_LOOP_ARCHIVE_URL:-"https://github.com/BrunoCosta173/autonomous-dev-loop/archive/refs/heads/main.tar.gz"}
SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" 2>/dev/null && pwd || pwd)

if [ -f "$SCRIPT_DIR/scripts/install.py" ] && [ -f "$SCRIPT_DIR/.agents/skills/autonomous-dev-loop/SKILL.md" ]; then
  exec python3 "$SCRIPT_DIR/scripts/install.py" "$@"
fi

if ! command -v python3 >/dev/null 2>&1; then
  echo "Error: python3 is required." >&2
  exit 1
fi

if ! command -v tar >/dev/null 2>&1; then
  echo "Error: tar is required for one-command installation." >&2
  exit 1
fi

TMP_DIR=$(mktemp -d "${TMPDIR:-/tmp}/autonomous-dev-loop.XXXXXX")
cleanup() {
  if [ -n "${TMP_DIR:-}" ] && [ -d "$TMP_DIR" ]; then
    rm -rf "$TMP_DIR"
  fi
}
trap cleanup EXIT
trap 'cleanup; exit 130' HUP INT TERM

ARCHIVE="$TMP_DIR/source.tar.gz"
if command -v curl >/dev/null 2>&1; then
  curl -fsSL "$ARCHIVE_URL" -o "$ARCHIVE"
elif command -v wget >/dev/null 2>&1; then
  wget -qO "$ARCHIVE" "$ARCHIVE_URL"
else
  echo "Error: curl or wget is required for one-command installation." >&2
  exit 1
fi

tar -xzf "$ARCHIVE" -C "$TMP_DIR"

REPO_ROOT=
for candidate in "$TMP_DIR"/autonomous-dev-loop-*; do
  if [ -d "$candidate" ]; then
    REPO_ROOT=$candidate
    break
  fi
done

if [ -z "$REPO_ROOT" ] || [ ! -f "$REPO_ROOT/scripts/install.py" ]; then
  echo "Error: could not find installer in downloaded archive." >&2
  exit 1
fi

python3 "$REPO_ROOT/scripts/install.py" "$@"
