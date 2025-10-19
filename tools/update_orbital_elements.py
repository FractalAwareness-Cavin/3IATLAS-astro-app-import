#!/usr/bin/env python3
"""Fetch latest orbital solution for 3I/ATLAS from JPL SBDB and refresh local templates."""
import argparse
import json
import math
import urllib.request
from pathlib import Path

AU_KM = 149597870.7
SBDB_URL = 'https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=3I/ATLAS&full-prec=true'

REPO_ROOT = Path(__file__).resolve().parents[1]

# Target files to update
MPC_FILE_PATHS = [
    REPO_ROOT / 'import-pack/3I-ATLAS/templates/stellarium/3I_ATLAS_mpc_elements.txt',
    REPO_ROOT / 'import-pack/3I-ATLAS/templates/skysafari/3I_ATLAS_mpc_1line.txt',
    REPO_ROOT / 'apps-using-mpc-files/cartes-du-ciel/3I_ATLAS_mpc_1line.txt',
    REPO_ROOT / 'apps-using-mpc-files/winstars/3I_ATLAS_mpc_1line.txt'
]
KSTARS_FILES = [
    REPO_ROOT / 'import-pack/3I-ATLAS/templates/kstars/3I_ATLAS_comets_dat_snippet.txt',
    REPO_ROOT / 'apps-using-mpc-files/kstars/3I_ATLAS_comets_dat_line.txt'
]
SOLAR_FIRE_FILES = [
    REPO_ROOT / 'solar-fire/extras.dat',
    REPO_ROOT / 'import-pack/3I-ATLAS/templates/solar_fire/3I_ATLAS_extras_dat_PLACEHOLDER.txt'
]

H_DEFAULT = 12.3
G_DEFAULT = 4.5


def fetch_sbdb():
    with urllib.request.urlopen(SBDB_URL) as resp:
        return json.load(resp)


def jd_to_calendar_decimal(jd):
    jd += 0.5
    z = int(jd)
    f = jd - z
    if z < 2299161:
        a = z
    else:
        alpha = int((z - 1867216.25) / 36524.25)
        a = z + 1 + alpha - alpha // 4
    b = a + 1524
    c = int((b - 122.1) / 365.25)
    d = int(365.25 * c)
    e = int((b - d) / 30.6001)
    day = b - d - int(30.6001 * e) + f
    month = e - 1 if e < 14 else e - 13
    year = c - 4716 if month > 2 else c - 4715
    return year, month, day


def make_mpc_line(fullname, q, e, inc, argperi, node, tp_jd, H, G):
    year, month, day = jd_to_calendar_decimal(tp_jd)
    day_decimal = day
    return f"{fullname} {year:04d} {month:02d} {day_decimal:.5f} {q:.7f} {e:.7f} {argperi:.7f} {node:.7f} {inc:.7f} {H:.1f} {G:.1f}"


def make_kstars_line(q, e, inc, argperi, node, tp_jd):
    mjd = int(round(tp_jd - 2400000.5))
    year, month, day = jd_to_calendar_decimal(tp_jd)
    day_decimal = day
    return ("3I/ATLAS | {mjd} | {q:.7f} | {e:.7f} | {inc:.7f} | {node:.7f} | {argperi:.7f} | "
            "{year:04d} {month:02d} {day:.5f} | MPC | 0").format(
        mjd=mjd, q=q, e=e, inc=inc, node=node, argperi=argperi,
        year=year, month=month, day=day_decimal)


def make_extras_block(epoch_jd, q, e, inc, argperi, node, tp_jd, H, G):
    block = f"[3I_ATLAS]\n"
    block += "Name = 3I/ATLAS\n"
    block += "Number = 0\n"
    block += f"EpochJD = {epoch_jd}\n"
    block += f"PerihelionDistance_AU = {q:.9f}\n"
    block += f"Eccentricity = {e:.9f}\n"
    block += f"Inclination_deg = {inc:.9f}\n"
    block += f"AscendingNode_deg = {node:.9f}\n"
    block += f"ArgumentOfPerihelion_deg = {argperi:.9f}\n"
    block += f"PerihelionTime_JD = {tp_jd:.9f}\n"
    block += f"AbsoluteMagnitude = {H}\n"
    block += f"SlopeParameter = {G}\n"
    block += "; Solar Fire ignores semi-major axis when Tp supplied for comets.\n"
    block += "; This object is hyperbolic (e>1). Verify compatibility with your Solar Fire version.\n"
    block += "; After copying, restart Solar Fire and enable the body under Extra Bodies.\n"
    return block


def replace_block(text, new_block):
    import re
    pattern = re.compile(r"\[3I_ATLAS\][\s\S]*?(?=\n\[|$)")
    if pattern.search(text):
        return pattern.sub(new_block.strip(), text).rstrip() + "\n"
    else:
        if not text.endswith("\n\n"):
            text = text.rstrip() + "\n\n"
        return text + new_block.strip() + "\n"


def main():
    parser = argparse.ArgumentParser(description='Update orbital templates for 3I/ATLAS from JPL SBDB.')
    parser.add_argument('--dry-run', action='store_true', help='Fetch and display values without modifying files.')
    args = parser.parse_args()

    data = fetch_sbdb()
    elements = {item['name']: float(item['value']) for item in data['orbit']['elements'] if item.get('value')}
    fullname = data['object']['fullname']
    q = elements['q']
    e = elements['e']
    inc = elements['i']
    argperi = elements['w']
    node = elements['om']
    tp = elements['tp']
    epoch = float(data['orbit']['epoch'])
    H = H_DEFAULT
    G = G_DEFAULT

    mpc_line = make_mpc_line(fullname, q, e, inc, argperi, node, tp, H, G)
    kstars_line = make_kstars_line(q, e, inc, argperi, node, tp)
    extras_block = make_extras_block(epoch, q, e, inc, argperi, node, tp, H, G)

    print('Fetched orbital elements:')
    print('  q =', q)
    print('  e =', e)
    print('  i =', inc)
    print('  Ω =', node)
    print('  ω =', argperi)
    print('  Tp JD =', tp)
    print('  Name =', fullname)

    if args.dry_run:
        print('\n[DRY-RUN] Files not modified.')
        print('MPC line:', mpc_line)
        print('KStars line:', kstars_line)
        return

    for path in MPC_FILE_PATHS:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(mpc_line + "\n", encoding='utf-8')
        print('Updated', path)

    for path in KSTARS_FILES:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(kstars_line + "\n", encoding='utf-8')
        print('Updated', path)

    for path in SOLAR_FIRE_FILES:
        text = path.read_text(encoding='utf-8')
        new_text = replace_block(text, extras_block)
        path.write_text(new_text, encoding='utf-8')
        print('Updated', path)

if __name__ == '__main__':
    main()
