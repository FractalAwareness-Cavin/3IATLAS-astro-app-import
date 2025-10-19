3I/ATLAS CSV-DATEN
==================

Dieser Ordner enthält die Roh-CSV-Tabellen, die mit NASA/JPL Horizons erzeugt wurden.
Jede Datei nutzt TDB-Daten um 00:00 und das ekliptische J2000-Referenzsystem,
sofern nicht anders angegeben.

Dateien
-------
- `geocentric_daily.csv` – tropische ekliptische Länge/Breite/Entfernung
  sowie heliozentrische kartesische Koordinaten und Geschwindigkeitskomponenten.
- `geocentric_sidereal_lahiri_daily.csv` – siderische Längen basierend auf
  dem Lahiri-Ayanāṃśa (Spalte `lambda_sidereal_deg`) plus tägliches Ayanāṃśa in
  `ayanamsa_deg`.
- `geocentric_sidereal_fagan_bradley_daily.csv` – wie oben, aber mit dem
  Fagan/Bradley-Ayanāṃśa.
- `geocentric_*_sign_ingresses.csv` – Zeitstempel, wann die geozentrische Länge
  jede tropische/siderische 30°-Grenze überschreitet.
- `heliocentric_daily.csv`, `barycentric_daily.csv` – Positions-/Geschwindigkeitsvektoren
  im heliozentrischen bzw. baryzentrischen Bezugssystem.

Nutzungshinweise
----------------
- Import in Tabellenkalkulationen (Excel, LibreOffice), wissenschaftliche Notebooks
  oder Skriptumgebungen (Python/pandas, R usw.).
- Längen sind in Grad; wickeln oder in Radiant umrechnen, wenn nötig.
- Entfernungen sind in Astronomischen Einheiten (AE); Geschwindigkeiten in km/s.
- Verwenden Sie die siderischen Tabellen, wenn Sie vorgedrehte Längen brauchen—
  andernfalls ziehen Sie Ihr bevorzugtes Ayanāṃśa von der tropischen Länge ab.
- Die Daten haben eine Tagesauflösung; interpolieren Sie, falls Sie höhere
  zeitliche Auflösung benötigen.
