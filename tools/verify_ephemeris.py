#!/usr/bin/env python3
"""Compare selected rows from geocentric_mpc_ephemeris.txt with live Horizons data."""
import argparse
import datetime as dt
import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

AU_KM = 149597870.7
EPHEMERIS_FILE = Path(__file__).resolve().parents[1] / 'apps-using-mpc-files' / 'geocentric_mpc_ephemeris.txt'


def parse_local_ephemeris():
    rows = {}
    pattern = re.compile(r'[-+]?\d+\.\d+|[-+]?\d+')
    with EPHEMERIS_FILE.open('r', encoding='utf-8') as f:
        for line in f:
            if not line.strip() or line.startswith('Date'):
                continue
            nums = pattern.findall(line)
            if len(nums) < 14:
                continue
            year = int(nums[0])
            month = int(nums[1])
            day_float = float(nums[2])
            delta_au = float(nums[9])
            rows[(year, month, day_float)] = {
                'line': line.rstrip(),
                'delta_au': delta_au
            }
    return rows


def horizons_range_for_date(date: dt.date):
    params = {
        'format': 'json',
        'COMMAND': "'DES=1004083;'",
        'CENTER': "'500@399'",
        'MAKE_EPHEM': 'YES',
        'EPHEM_TYPE': 'VECTORS',
        'START_TIME': f"'{date.isoformat()}'",
        'STOP_TIME': f"'{(date + dt.timedelta(days=1)).isoformat()}'",
        'STEP_SIZE': "'1 d'"
    }
    url = 'https://ssd.jpl.nasa.gov/api/horizons.api?' + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url) as resp:
        data = json.load(resp)
    result = data.get('result', '')
    for line in result.split('\n'):
        if 'RG=' in line:
            try:
                rg_str = line.split('RG=')[1].split()[0]
                rg_km = float(rg_str.replace('E', 'e'))
                return rg_km
            except Exception:
                continue
    raise RuntimeError('Could not parse range from Horizons result for ' + date.isoformat())


def main():
    parser = argparse.ArgumentParser(description='Validate geocentric MPC ephemeris against Horizons.')
    parser.add_argument('--start', type=str, default='2025-10-01', help='Start date (YYYY-MM-DD)')
    parser.add_argument('--days', type=int, default=5, help='Number of days to check')
    parser.add_argument('--tolerance', type=float, default=5e-4, help='Allowed difference in AU (default 5e-4 AU ≈ 75,000 km)')
    args = parser.parse_args()

    start_date = dt.datetime.strptime(args.start, '%Y-%m-%d').date()
    local_rows = parse_local_ephemeris()
    ok = True
    for offset in range(args.days):
        date = start_date + dt.timedelta(days=offset)
        key = (date.year, date.month, float(date.day))
        local = local_rows.get(key)
        if not local:
            print(f'[WARN] No local ephemeris row for {date}')
            ok = False
            continue
        horizon_range_km = horizons_range_for_date(date)
        local_km = local['delta_au'] * AU_KM
        diff_au = abs(local_km - horizon_range_km) / AU_KM
        status = 'OK' if diff_au <= args.tolerance else 'DIFF'
        print(f"{date}: local delta={local['delta_au']:.6f} AU, Horizons delta={horizon_range_km/AU_KM:.6f} AU, |Δ|={diff_au:.6e} AU [{status}]")
        if status != 'OK':
            ok = False
    if not ok:
        sys.exit(1)

if __name__ == '__main__':
    main()
