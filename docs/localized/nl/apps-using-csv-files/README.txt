3I/ATLAS CSV-DATA
=================

Deze map bevat de ruwe CSV-tabellen die zijn gegenereerd met NASA/JPL Horizons.
Elk bestand gebruikt TDB-datums om 00:00 en het ecliptische J2000-referentieframe,
behalve wanneer anders vermeld.

Bestanden
---------
- `geocentric_daily.csv` – tropische ecliptische lengte/breedte/afstanden
  plus heliocentrische cartesische coördinaten en snelheidscomponenten.
- `geocentric_sidereal_lahiri_daily.csv` – siderische lengten op basis van
  de Lahiri-ayanāṃśa (kolom `lambda_sidereal_deg`) en de dagelijkse ayanāṃśa in
  `ayanamsa_deg`.
- `geocentric_sidereal_fagan_bradley_daily.csv` – hetzelfde, maar met de
  Fagan/Bradley-ayanāṃśa.
- `geocentric_*_sign_ingresses.csv` – tijdstempels waarop de geocentrische lengte
  elke tropische/siderische 30°-grens passeert.
- `heliocentric_daily.csv`, `barycentric_daily.csv` – positie-/snelheidsvectoren
  in het heliocentrische en barycentrische referentiekader.

Gebruikstips
------------
- Importeer in spreadsheetsoftware (Excel, LibreOffice), wetenschappelijke notebooks
  of scripttalen (Python/pandas, R, enz.).
- Lengten zijn in graden; wikkel ze of converteer naar radialen indien nodig.
- Afstanden zijn in astronomische eenheden (AE); snelheden in km/s.
- Gebruik de siderische tabellen als je voorgecorrigeerde lengten nodig hebt—
  anders trek je je favoriete ayanāṃśa van de tropische lengte af.
- De datering is dagelijks; interpoleer als je een hogere resolutie nodig hebt.
