from __future__ import annotations

import csv
import json
import math
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, List

AU_KM = 149_597_870.7
PI2 = math.tau

ROOT_DIR = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT_DIR / "raw"
DATA_DIR = ROOT_DIR / "data"
TEXT_DIR = ROOT_DIR / "text"
VENDOR_DIR = ROOT_DIR / "vendor"
if VENDOR_DIR.exists():
    sys.path.insert(0, str(VENDOR_DIR))

try:  # optional Swiss Ephemeris dependency
    import swisseph as swe  # type: ignore
except ImportError:  # pragma: no cover - optional dependency
    swe = None

DATA_DIR.mkdir(parents=True, exist_ok=True)
TEXT_DIR.mkdir(parents=True, exist_ok=True)

TARGETS: Dict[str, List[Path]] = {
    "heliocentric": sorted(RAW_DIR.glob("heliocentric_daily_*.json")) or [RAW_DIR / "heliocentric_daily.json"],
    "geocentric": sorted(RAW_DIR.glob("geocentric_daily_*.json")) or [RAW_DIR / "geocentric_daily.json"],
    "barycentric": sorted(RAW_DIR.glob("barycentric_daily_*.json")) or [RAW_DIR / "barycentric_daily.json"],
}


def parse_vectors(raw_text: str) -> List[Dict[str, float]]:
    """Parse Horizons vector block into structured records."""
    entries: List[Dict[str, float]] = []
    current: Dict[str, float] | None = None

    for line in raw_text.splitlines():
        if line.startswith("$$EOE"):
            break
        line = line.rstrip()
        if not line:
            continue
        if "= A.D." in line:
            jd_str, cal = line.split("=", 1)
            jd = float(jd_str.strip())
            calendar = cal.replace("A.D.", "").strip()
            current = {"jd": jd, "calendar": calendar}
            continue
        if current is None:
            continue
        if line.startswith(" X ="):
            parts = line.replace("=", " ").split()
            current["X_km"] = float(parts[1])
            current["Y_km"] = float(parts[3])
            current["Z_km"] = float(parts[5])
        elif line.startswith(" VX="):
            parts = line.replace("=", " ").split()
            current["VX_kms"] = float(parts[1])
            current["VY_kms"] = float(parts[3])
            current["VZ_kms"] = float(parts[5])
        elif line.startswith(" LT="):
            parts = line.replace("=", " ").split()
            current["RG_km"] = float(parts[3])
            current["RR_kms"] = float(parts[5])
            entries.append(current)
            current = None
    return entries


def cartesian_to_spherical(record: Dict[str, float]) -> Dict[str, float]:
    x_au = record["X_km"] / AU_KM
    y_au = record["Y_km"] / AU_KM
    z_au = record["Z_km"] / AU_KM
    r_au = math.sqrt(x_au * x_au + y_au * y_au + z_au * z_au)

    lon = math.atan2(y_au, x_au)
    if lon < 0:
        lon += PI2
    lat = math.asin(z_au / r_au) if r_au else 0.0

    record.update(
        {
            "x_au": x_au,
            "y_au": y_au,
            "z_au": z_au,
            "distance_au": r_au,
            "lambda_deg": math.degrees(lon),
            "beta_deg": math.degrees(lat),
        }
    )
    return record


def write_csv(label: str, entries: Iterable[Dict[str, float]]) -> None:
    csv_path = DATA_DIR / f"{label}_daily.csv"
    fieldnames = [
        "date_tdb",
        "jd_tdb",
        "lambda_deg",
        "beta_deg",
        "distance_au",
        "x_au",
        "y_au",
        "z_au",
        "vx_km_s",
        "vy_km_s",
        "vz_km_s",
        "radial_velocity_km_s",
    ]

    with csv_path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for entry in entries:
            writer.writerow(
                {
                    "date_tdb": entry["calendar"],
                    "jd_tdb": f"{entry['jd']:.5f}",
                    "lambda_deg": f"{entry['lambda_deg']:.6f}",
                    "beta_deg": f"{entry['beta_deg']:.6f}",
                    "distance_au": f"{entry['distance_au']:.6f}",
                    "x_au": f"{entry['x_au']:.6f}",
                    "y_au": f"{entry['y_au']:.6f}",
                    "z_au": f"{entry['z_au']:.6f}",
                    "vx_km_s": f"{entry['VX_kms']:.6f}",
                    "vy_km_s": f"{entry['VY_kms']:.6f}",
                    "vz_km_s": f"{entry['VZ_kms']:.6f}",
                    "radial_velocity_km_s": f"{entry['RR_kms']:.6f}",
                }
            )


def write_solar_fire(label: str, entries: Iterable[Dict[str, float]]) -> None:
    txt_path = TEXT_DIR / f"{label}_daily_solarfire.txt"
    with txt_path.open("w") as out:
        out.write("# YYYY MM DD HHMM  Lon(deg)  Lat(deg)  Dist(AU)\n")
        for entry in entries:
            date_part = entry["calendar"].split()[0]
            year, mon, day = date_part.split("-")
            if mon.isalpha():
                month_map = {
                    "Jan": "01",
                    "Feb": "02",
                    "Mar": "03",
                    "Apr": "04",
                    "May": "05",
                    "Jun": "06",
                    "Jul": "07",
                    "Aug": "08",
                    "Sep": "09",
                    "Oct": "10",
                    "Nov": "11",
                    "Dec": "12",
                }
                month_num = month_map[mon]
                day_num = day
            else:
                month_num = mon
                day_num = day
            out.write(
                f"{year} {month_num} {day_num} 0000  "
                f"{entry['lambda_deg']:.6f}  {entry['beta_deg']:.6f}  {entry['distance_au']:.6f}\n"
            )


def write_sign_ingresses(
    label: str,
    entries: List[Dict[str, float]],
    longitude_key: str,
    suffix: str,
) -> None:
    signs = [
        "Aries",
        "Taurus",
        "Gemini",
        "Cancer",
        "Leo",
        "Virgo",
        "Libra",
        "Scorpio",
        "Sagittarius",
        "Capricorn",
        "Aquarius",
        "Pisces",
    ]

    def sign_index(lon_deg: float) -> int:
        lon = lon_deg % 360.0
        return int(lon // 30)

    rows = []
    prev_entry = entries[0]
    prev_sign = sign_index(prev_entry[longitude_key])
    for entry in entries[1:]:
        current_sign = sign_index(entry[longitude_key])
        if current_sign != prev_sign:
            rows.append(
                {
                    "datetime_tdb": entry["calendar"],
                    "jd_tdb": f"{entry['jd']:.5f}",
                    "longitude_deg": f"{entry[longitude_key]:.6f}",
                    "sign": signs[current_sign],
                }
            )
            prev_sign = current_sign
        prev_entry = entry

    csv_path = DATA_DIR / f"{label}_{suffix}_sign_ingresses.csv"
    with csv_path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["datetime_tdb", "jd_tdb", "longitude_deg", "sign"])
        writer.writeheader()
        writer.writerows(rows)


def normalize_entries(raw_entries: List[Dict[str, float]]) -> List[Dict[str, float]]:
    return [cartesian_to_spherical(dict(entry)) for entry in raw_entries]


def vector_sub(a: Iterable[float], b: Iterable[float]) -> List[float]:
    return [ai - bi for ai, bi in zip(a, b)]


def dot(a: Iterable[float], b: Iterable[float]) -> float:
    return sum(ai * bi for ai, bi in zip(a, b))


def norm(a: Iterable[float]) -> float:
    return math.sqrt(dot(a, a))


def write_mpc_ephemeris(
    geocentric_entries: List[Dict[str, float]],
    heliocentric_entries: List[Dict[str, float]],
) -> None:
    obliquity = math.radians(23.439291111)
    cos_eps = math.cos(obliquity)
    sin_eps = math.sin(obliquity)

    heli_map = {entry["jd"]: entry for entry in heliocentric_entries}

    dest = DATA_DIR / "geocentric_mpc_ephemeris.txt"
    with dest.open("w") as out:
        out.write(
            "Date (UT)    R.A. (J2000)   Dec. (J2000)    Delta    r    Elong  Phase   Mag\n"
        )
        for entry in geocentric_entries:
            helio = heli_map.get(entry["jd"])
            if helio is None:
                continue

            geo_vec = [entry["x_au"], entry["y_au"], entry["z_au"]]
            helio_vec = [helio["x_au"], helio["y_au"], helio["z_au"]]
            earth_vec = vector_sub(helio_vec, geo_vec)

            x_ecl, y_ecl, z_ecl = geo_vec
            x_eq = x_ecl
            y_eq = y_ecl * cos_eps - z_ecl * sin_eps
            z_eq = y_ecl * sin_eps + z_ecl * cos_eps

            distance = norm((x_eq, y_eq, z_eq))
            ra = math.atan2(y_eq, x_eq)
            if ra < 0:
                ra += 2 * math.pi
            dec = math.asin(z_eq / distance)

            ra_hours = math.degrees(ra) / 15.0
            ra_h = int(ra_hours)
            ra_min_total = (ra_hours - ra_h) * 60.0
            ra_m = int(ra_min_total)
            ra_s = (ra_min_total - ra_m) * 60.0
            ra_s = round(ra_s, 1)
            if ra_s >= 60.0:
                ra_s -= 60.0
                ra_m += 1
            if ra_m >= 60:
                ra_m -= 60
                ra_h = (ra_h + 1) % 24

            dec_deg = math.degrees(dec)
            dec_sign = "+" if dec_deg >= 0 else "-"
            dec_abs = abs(dec_deg)
            dec_d = int(dec_abs)
            dec_min_total = (dec_abs - dec_d) * 60.0
            dec_m = int(dec_min_total)
            dec_s = (dec_min_total - dec_m) * 60.0
            dec_s = int(round(dec_s, 0))
            if dec_s >= 60.0:
                dec_s -= 60.0
                dec_m += 1
            if dec_m >= 60:
                dec_m -= 60
                dec_d += 1
            dec_m = int(dec_m)
            dec_s = int(dec_s)

            delta = entry["distance_au"]
            r = helio["distance_au"]

            earth_to_sun = [-v for v in earth_vec]
            earth_to_object = geo_vec
            cos_elong = dot(earth_to_sun, earth_to_object) / (
                norm(earth_to_sun) * norm(earth_to_object)
            )
            cos_elong = max(-1.0, min(1.0, cos_elong))
            elong = math.degrees(math.acos(cos_elong))

            object_to_sun = [-v for v in helio_vec]
            object_to_earth = [-v for v in geo_vec]
            cos_phase = dot(object_to_sun, object_to_earth) / (
                norm(object_to_sun) * norm(object_to_earth)
            )
            cos_phase = max(-1.0, min(1.0, cos_phase))
            phase = math.degrees(math.acos(cos_phase))

            mag = 99.9

            dt = datetime.strptime(entry["calendar"].split()[0], "%Y-%b-%d")
            day_decimal = dt.day + 0.0

            out.write(
                f"{dt.year:4d} {dt.month:02d} {day_decimal:4.1f}  "
                f"{ra_h:02d} {ra_m:02d} {ra_s:04.1f}  "
                f"{dec_sign}{dec_d:02d} {dec_m:02d} {dec_s:02d}  "
                f"{delta:7.4f} {r:7.4f} {elong:6.1f} {phase:6.1f} {mag:5.1f}\n"
            )


def write_sidereal_outputs(label: str, entries: List[Dict[str, float]]) -> None:
    if swe is None:
        print("Swiss Ephemeris not installed; skipping sidereal outputs.")
        return

    sidereal_modes = {
        "sidereal_lahiri": swe.SIDM_LAHIRI,
        "sidereal_fagan_bradley": swe.SIDM_FAGAN_BRADLEY,
    }

    for suffix, mode in sidereal_modes.items():
        sidereal_entries: List[Dict[str, float]] = []
        for entry in entries:
            _, ayanamsa = swe.get_ayanamsa_ex(entry["jd"], mode)
            lon_sidereal = (entry["lambda_deg"] - ayanamsa) % 360.0
            sidereal_entry = dict(entry)
            sidereal_entry["ayanamsa_deg"] = ayanamsa
            sidereal_entry["lambda_sidereal_deg"] = lon_sidereal
            sidereal_entries.append(sidereal_entry)

        csv_path = DATA_DIR / f"{label}_{suffix}_daily.csv"
        fieldnames = [
            "date_tdb",
            "jd_tdb",
            "lambda_sidereal_deg",
            "beta_deg",
            "distance_au",
            "ayanamsa_deg",
            "x_au",
            "y_au",
            "z_au",
            "vx_km_s",
            "vy_km_s",
            "vz_km_s",
            "radial_velocity_km_s",
        ]
        with csv_path.open("w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for entry in sidereal_entries:
                writer.writerow(
                    {
                        "date_tdb": entry["calendar"],
                        "jd_tdb": f"{entry['jd']:.5f}",
                        "lambda_sidereal_deg": f"{entry['lambda_sidereal_deg']:.6f}",
                        "beta_deg": f"{entry['beta_deg']:.6f}",
                        "distance_au": f"{entry['distance_au']:.6f}",
                        "ayanamsa_deg": f"{entry['ayanamsa_deg']:.6f}",
                        "x_au": f"{entry['x_au']:.6f}",
                        "y_au": f"{entry['y_au']:.6f}",
                        "z_au": f"{entry['z_au']:.6f}",
                        "vx_km_s": f"{entry['VX_kms']:.6f}",
                        "vy_km_s": f"{entry['VY_kms']:.6f}",
                        "vz_km_s": f"{entry['VZ_kms']:.6f}",
                        "radial_velocity_km_s": f"{entry['RR_kms']:.6f}",
                    }
                )

        if label == "geocentric":
            write_sign_ingresses(label, sidereal_entries, "lambda_sidereal_deg", suffix)

        txt_path = TEXT_DIR / f"{label}_{suffix}_daily_solarfire.txt"
        with txt_path.open("w") as out:
            out.write("# YYYY MM DD HHMM  Lon_sid(deg)  Lat(deg)  Dist(AU)  Ayanamsa(deg)\n")
            for entry in sidereal_entries:
                date_part = entry["calendar"].split()[0]
                year, mon, day = date_part.split("-")
                if mon.isalpha():
                    month_map = {
                        "Jan": "01",
                        "Feb": "02",
                        "Mar": "03",
                        "Apr": "04",
                        "May": "05",
                        "Jun": "06",
                        "Jul": "07",
                        "Aug": "08",
                        "Sep": "09",
                        "Oct": "10",
                        "Nov": "11",
                        "Dec": "12",
                    }
                    month_num = month_map[mon]
                    day_num = day
                else:
                    month_num = mon
                    day_num = day
                out.write(
                    f"{year} {month_num} {day_num} 0000  "
                    f"{entry['lambda_sidereal_deg']:.6f}  {entry['beta_deg']:.6f}  "
                    f"{entry['distance_au']:.6f}  {entry['ayanamsa_deg']:.6f}\n"
                )


def main() -> None:
    generated: Dict[str, List[Dict[str, float]]] = {}
    for label, paths in TARGETS.items():
        raw_entries: List[Dict[str, float]] = []
        for path in paths:
            if not path.exists():
                raise FileNotFoundError(f"Missing Horizons export: {path}")
            raw_text = json.loads(path.read_text())["result"]
            raw_entries.extend(parse_vectors(raw_text))
        raw_entries.sort(key=lambda item: item["jd"])
        entries = normalize_entries(raw_entries)
        write_csv(label, entries)
        write_solar_fire(label, entries)
        if label == "geocentric":
            write_sign_ingresses(label, entries, "lambda_deg", "tropical")
            write_sidereal_outputs(label, entries)
        print(f"Generated outputs for {label}: {len(entries)} records")
        generated[label] = entries

    if {"geocentric", "heliocentric"}.issubset(generated):
        write_mpc_ephemeris(generated["geocentric"], generated["heliocentric"])


if __name__ == "__main__":
    main()
