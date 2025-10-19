DANE CSV 3I/ATLAS
=================

Ten katalog zawiera surowe tabele CSV wygenerowane w NASA/JPL Horizons.
Każdy plik korzysta z dat TDB o 00:00 i układu ekliptycznego J2000,
chyba że zaznaczono inaczej.

Pliki
-----
- `geocentric_daily.csv` – długość/szerokość/odległość w ekliptyce tropikalnej
  oraz heliocentryczne współrzędne kartezjańskie i składowe prędkości.
- `geocentric_sidereal_lahiri_daily.csv` – długości gwiazdowe wyliczone z
  ayanāṃśa Lahiri (kolumna `lambda_sidereal_deg`) oraz dzienna ayanāṃśa w
  `ayanamsa_deg`.
- `geocentric_sidereal_fagan_bradley_daily.csv` – jak wyżej, lecz z
  ayanāṃśa Fagana/Bradley'a.
- `geocentric_*_sign_ingresses.csv` – znaczniki czasu, gdy długość geocentryczna
  przekracza kolejną granicę 30° w układzie tropikalnym/gwiazdowym.
- `heliocentric_daily.csv`, `barycentric_daily.csv` – wektory położenia/prędkości
  w układach heliocentrycznym i barycentrycznym Układu Słonecznego.

Wskazówki
---------
- Importuj do arkuszy kalkulacyjnych (Excel, LibreOffice), notatników naukowych
  lub środowisk skryptowych (Python/pandas, R itp.).
- Długości są podane w stopniach; dokonaj zawinięcia lub konwersji na radiany wedle potrzeb.
- Odległości są w jednostkach astronomicznych (AU); prędkości w km/s.
- Korzystaj z tabel gwiazdowych, gdy potrzebujesz długości już przesuniętych—
  w przeciwnym razie odejmij preferowaną ayanāṃśa od długości tropikalnej.
- Kadencja danych to 1 dzień; interpoluj, jeśli potrzebujesz większej rozdzielczości.
