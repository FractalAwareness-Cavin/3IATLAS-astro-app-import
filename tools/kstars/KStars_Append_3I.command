#!/usr/bin/env bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
echo "[macOS helper] KStars append for 3I/ATLAS — see README for full instructions."
"$SCRIPT_DIR/append_line.sh" "$@"
echo
read -n1 -r -p "Press any key to close..."
