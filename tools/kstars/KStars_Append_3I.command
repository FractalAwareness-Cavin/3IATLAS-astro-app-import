#!/usr/bin/env bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
"$SCRIPT_DIR/append_line.sh" "$@"
echo
read -n1 -r -p "Press any key to close..."
