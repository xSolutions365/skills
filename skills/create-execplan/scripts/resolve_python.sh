#!/usr/bin/env bash
set -euo pipefail

if command -v python >/dev/null 2>&1; then
  command -v python
  exit 0
fi

if command -v python3 >/dev/null 2>&1; then
  command -v python3
  exit 0
fi

echo "No supported Python runtime found. Install python or python3." >&2
exit 1
