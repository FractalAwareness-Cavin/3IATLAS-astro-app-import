#!/usr/bin/env bash
set -euo pipefail

if ! command -v mksweph >/dev/null 2>&1; then
  echo "mksweph not found. Install Swiss Ephemeris tools from https://www.astro.com/ftp/swisseph/" >&2
  exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
DATA_DIR="$ROOT_DIR/for-csv"
OUT_DIR="$ROOT_DIR/swisseph"

mkdir -p "$OUT_DIR"

mksweph -i "$DATA_DIR/geocentric_daily.csv" \
        -o "$OUT_DIR/3I_ATLAS_geocentric.se1" \
        -n "3I/ATLAS" \
        -b 2016-01-01 -e 2040-12-31

mksweph -i "$DATA_DIR/geocentric_sidereal_lahiri_daily.csv" \
        -o "$OUT_DIR/3I_ATLAS_Lahiri.se1" \
        -n "3I/ATLAS (Lahiri)" \
        -b 2016-01-01 -e 2040-12-31

mksweph -i "$DATA_DIR/geocentric_sidereal_fagan_bradley_daily.csv" \
        -o "$OUT_DIR/3I_ATLAS_FaganBradley.se1" \
        -n "3I/ATLAS (Fagan-Bradley)" \
        -b 2016-01-01 -e 2040-12-31

echo "Swiss Ephemeris binaries written to $OUT_DIR"
