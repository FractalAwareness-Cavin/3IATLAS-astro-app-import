#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# Default line-file search (works from repo or release zip)
LINE_FILE_DEFAULT="$SCRIPT_DIR/../3I_ATLAS_comets_dat_line.txt"
LINE_FILE_ALT="$SCRIPT_DIR/../../import-pack/3I-ATLAS/templates/kstars/3I_ATLAS_comets_dat_snippet.txt"
LINE_FILE=""
TARGET_DEFAULT="$HOME/.local/share/kstars/comets.dat"
TARGET_ALT="$HOME/Library/Application Support/kstars/comets.dat"
TARGET="$TARGET_DEFAULT"
TARGET_OVERRIDDEN=0
APPLY=0
PROMPT=1

function usage() {
  cat <<USAGE
Usage: $(basename "$0") [--target PATH] [--line-file PATH] [--apply] [--dry-run]
       --apply / -y : append immediately without interactive prompt.
       --dry-run    : preview and exit (default).
USAGE
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --target) TARGET="$2"; TARGET_OVERRIDDEN=1; shift 2;;
    --line-file) LINE_FILE="$2"; shift 2;;
    --apply|-y) APPLY=1; PROMPT=0; shift;;
    --dry-run) APPLY=0; PROMPT=0; shift;;
    --help|-h) usage; exit 0;;
    *) echo "Unknown option: $1"; usage; exit 1;;
  esac
done

if [[ -z "$LINE_FILE" ]]; then
  if [[ -f "$LINE_FILE_DEFAULT" ]]; then
    LINE_FILE="$LINE_FILE_DEFAULT"
  elif [[ -f "$LINE_FILE_ALT" ]]; then
    LINE_FILE="$LINE_FILE_ALT"
  else
    echo "ERROR: Could not locate 3I_ATLAS_comets_dat_line.txt" >&2
    exit 1
  fi
fi

LINE=$(grep -v '^[[:space:]]*#' "$LINE_FILE" | sed '/^[[:space:]]*$/d' | head -n1 || true)
if [[ -z "$LINE" ]]; then
  echo "ERROR: No usable line found in $LINE_FILE" >&2
  exit 1
fi

echo "Target comets.dat: $TARGET"
echo
printf '%s\n%s\n%s\n\n' '--- PREVIEW ---' "$LINE" '---------------'

if [[ $TARGET_OVERRIDDEN -eq 0 && ! -e "$TARGET" && -f "$TARGET_ALT" ]]; then
  echo "[INFO] Detected KStars Application Support data; using \"$TARGET_ALT\"."
  TARGET="$TARGET_ALT"
fi

if [[ $PROMPT -eq 1 ]]; then
  read -r -p "Apply changes? (y/N) " resp
  if [[ ! $resp =~ ^[Yy]$ ]]; then
    echo "[DRY-RUN] No changes made."
    exit 0
  fi
  APPLY=1
fi

if [[ $APPLY -eq 0 ]]; then
  echo "[DRY-RUN] No changes made."
  exit 0
fi

mkdir -p "$(dirname "$TARGET")"
STAMP="$(date +%Y%m%d-%H%M%S)"
BACKUP="${TARGET}.bak.${STAMP}"
if [[ -f "$TARGET" ]]; then
  cp -f "$TARGET" "$BACKUP"
  echo "[OK] Backup created at $BACKUP"
  # remove existing lines for 3I/ATLAS
  tmp="${TARGET}.tmp.$$"
  awk 'BEGIN{IGNORECASE=1} !($0 ~ /3I\/ATLAS/)' "$TARGET" > "$tmp"
  mv "$tmp" "$TARGET"
else
  echo "[INFO] Target file did not exist; creating new file."
  :
fi

if [[ -s "$TARGET" ]]; then
  printf '\n' >> "$TARGET"
fi
printf '%s\n' "$LINE" >> "$TARGET"
echo "[OK] Appended 3I/ATLAS to $TARGET"
