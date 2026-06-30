#!/usr/bin/env bash
set -euo pipefail

SOURCE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_ROOT="${CODEX_HOME:-$HOME/.codex}/skills"
TARGET_DIR="$TARGET_ROOT/write-a-story"

if [ "$SOURCE_DIR" = "$TARGET_DIR" ]; then
  echo "Already running from target skill directory: $TARGET_DIR" >&2
  echo "Nothing to install." >&2
  exit 0
fi

mkdir -p "$TARGET_ROOT"
rm -rf "$TARGET_DIR"
mkdir -p "$TARGET_DIR"

if command -v rsync >/dev/null 2>&1; then
  rsync -a --exclude ".git" "$SOURCE_DIR/" "$TARGET_DIR/"
else
  cp -R "$SOURCE_DIR"/. "$TARGET_DIR"/
  rm -rf "$TARGET_DIR/.git"
fi

python3 "$TARGET_DIR/scripts/verify_skill.py" "$TARGET_DIR"

echo "Installed write-a-story to: $TARGET_DIR"
echo "Restart Codex, then invoke it with: \$write-a-story"
