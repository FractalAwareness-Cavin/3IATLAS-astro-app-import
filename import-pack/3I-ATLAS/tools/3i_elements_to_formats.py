#!/usr/bin/env python3
'''
3I/ATLAS helper: turn a single MPC 1-line comet element into files for Stellarium, KStars, etc.

Usage:
python tools/3i_elements_to_formats.py --paste         # prompts for the 1-line, then writes files
python tools/3i_elements_to_formats.py --line "C/2025 N1 (ATLAS) …"

Outputs:
templates/stellarium/3I_ATLAS_mpc_elements.txt
templates/skysafari/3I_ATLAS_mpc_1line.txt
templates/kstars/3I_ATLAS_comets_dat_snippet.txt
'''
import argparse, re, sys, os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
def out(path):
    p = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    return p

def parse_mpc_comet_line(line: str):
    raw = " ".join(line.strip().split())
    parts = raw.split()
    # Heuristic: find a date token and five consecutive floats (q,e,i,ω,Ω) somewhere after it
    date_token = None
    # date tokens like: YYYY MM DD.ddddd  OR  YYYYMMDD.ddddd  OR  YYYY-MM-DD.ddddd
    dt_re2 = re.compile(r"^\d{8}\.\d+$")
    dt_re3 = re.compile(r"^\d{4}-\d{2}-\d{2}(\.\d+)?$")
    # try to assemble YYYY MM DD(.dddd) triplet
    for idx in range(len(parts)-2):
        if re.fullmatch(r"\d{4}", parts[idx]):
            try:
                int(parts[idx+1]); float(parts[idx+2]); date_token = f"{parts[idx]} {parts[idx+1]} {parts[idx+2]}"; break
            except Exception:
                pass
    if not date_token:
        for p in parts:
            if dt_re2.match(p) or dt_re3.match(p):
                date_token = p; break
    q=e=i=argperi=node=None
    for idx in range(len(parts)-4):
        try:
            fives = list(map(float, parts[idx:idx+5]))
            q,e,i,argperi,node = fives
            break
        except Exception:
            continue
    return {"raw": raw, "date_token": date_token, "q": q, "e": e, "i": i, "argperi": argperi, "node": node}

def mjd_from_datestr(date_token: str):
    if not date_token:
        return None
    s = date_token.replace("-", " ").replace("/", " ")
    fields = [f for f in s.split() if f]
    try:
        if len(fields) >= 3 and len(fields[0])==4:
            y,m = int(fields[0]), int(fields[1]); d = float(fields[2])
        elif re.match(r"^\d{8}\.\d+$", date_token):
            y = int(date_token[0:4]); m=int(date_token[4:6]); d=float(date_token[6:8]+"."+date_token[9:])
        else:
            return None
    except Exception:
        return None
    # Gregorian calendar → JD → MJD
    day = int(d); frac = float(d) - day
    a = (14 - m)//12
    y2 = y + 4800 - a
    m2 = m + 12*a - 3
    JD = day + ((153*m2 + 2)//5) + 365*y2 + y2//4 - y2//100 + y2//400 - 32045
    JD = JD + frac
    MJD = JD - 2400000.5
    try:
        return int(round(MJD, 0))
    except Exception:
        return None

def write_files(mpc_line: str, parsed: dict):
    # Stellarium & SkySafari (archive)
    with open(out("templates/stellarium/3I_ATLAS_mpc_elements.txt"), "w", encoding="utf-8") as f:
        f.write("# 3I/ATLAS — MPC 1-line (generated)\n")
        f.write(mpc_line.strip()+"\n")
    with open(out("templates/skysafari/3I_ATLAS_mpc_1line.txt"), "w", encoding="utf-8") as f:
        f.write("# 3I/ATLAS — MPC 1-line (archive)\n")
        f.write(mpc_line.strip()+"\n")
    # KStars snippet (best-effort)
    mjd = mjd_from_datestr(parsed.get("date_token"))
    line = " | ".join([
        "3I/ATLAS",
        str(mjd if mjd is not None else 60977),
        f"{parsed.get('q') or ''}",
        f"{parsed.get('e') or ''}",
        f"{parsed.get('i') or ''}",
        f"{parsed.get('node') or ''}",
        f"{parsed.get('argperi') or ''}",
        parsed.get("date_token") or "20251030.00000",
        "MPC",
        "0"
    ])
    with open(out("templates/kstars/3I_ATLAS_comets_dat_snippet.txt"), "w", encoding="utf-8") as f:
        f.write("# 3I/ATLAS — KStars comets.dat line (generated)\n")
        f.write(line+"\n")
    print("[OK] Wrote Stellarium/SkySafari/KStars files.")
    print("KStars (paste into comets.dat):")
    print(line)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--paste", action="store_true", help="Read the MPC 1-line from stdin")
    ap.add_argument("--line", type=str, help="Provide the MPC 1-line on the command")
    args = ap.parse_args()
    if not (args.paste or args.line):
        ap.print_help(); sys.exit(1)
    mpc_line = args.line.strip() if args.line else sys.stdin.readline().strip()
    if not mpc_line:
        print("No MPC 1-line provided."); sys.exit(2)
    parsed = parse_mpc_comet_line(mpc_line)
    write_files(mpc_line, parsed)

if __name__ == "__main__":
    main()
