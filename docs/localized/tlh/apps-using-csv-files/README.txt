NOTE (tlh): tlhIngan Hol mu'ghom wIghajbe' 'ej qaStaHvIS poH naQvam, HolwIj qumuvtaH 'Iw HIq. English content retained until translation volunteers arrive.

3I/ATLAS CSV DATA
=================

This folder holds the raw CSV tables generated from NASA/JPL Horizons.
Each file uses TDB dates at 00:00 and the ecliptic of J2000 frame unless
stated otherwise.

Files
-----
- `geocentric_daily.csv` – tropical ecliptic longitude/latitude/distances
  plus heliocentric Cartesian coordinates and velocity components.
- `geocentric_sidereal_lahiri_daily.csv` – sidereal longitudes derived with
  the Lahiri ayanāṃśa (column `lambda_sidereal_deg`) and the daily ayanāṃśa in
  `ayanamsa_deg`.
- `geocentric_sidereal_fagan_bradley_daily.csv` – same as above using the
  Fagan/Bradley ayanāṃśa.
- `geocentric_*_sign_ingresses.csv` – timestamps when the geocentric longitude
  crosses each 30° tropical/sidereal boundary.
- `heliocentric_daily.csv`, `barycentric_daily.csv` – position/velocity vectors
  in the heliocentric and solar-system-barycentric frames.

Usage hints
-----------
- Import into spreadsheets (Excel, LibreOffice), scientific notebooks, or
  scripting environments (Python/pandas, R, etc.).
- Longitudes are in degrees; wrap or convert to radians as needed.
- Distances are in astronomical units (AU); velocities in km/s.
- Use the sidereal tables when you need pre-shifted longitudes—otherwise
  subtract your preferred ayanāṃśa from the tropical longitude.
- The data cadence is 1 day; interpolate if you need higher resolution.
