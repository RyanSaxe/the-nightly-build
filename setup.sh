#!/usr/bin/env sh
# Backward-compatible entry point for existing forks and setup instructions.
set -eu

SCRIPT_DIR=$(CDPATH='' cd -- "$(dirname -- "$0")" && pwd)
exec "$SCRIPT_DIR/scripts/setup.sh" "$@"
