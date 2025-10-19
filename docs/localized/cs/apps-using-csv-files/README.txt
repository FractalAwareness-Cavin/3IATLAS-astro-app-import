CSV DATA 3I/ATLAS
=================

Tato složka obsahuje nezpracované CSV tabulky vygenerované službou NASA/JPL Horizons.
Každý soubor používá data TDB ve 00:00 a ekliptický rámec J2000,
pokud není uvedeno jinak.

Soubory
-------
- `geocentric_daily.csv` – tropická ekliptická délka/šířka/vzdálenost
  plus heliocentrické kartézské souřadnice a složky rychlosti.
- `geocentric_sidereal_lahiri_daily.csv` – siderické délky vypočtené s ayanámsou
  Lahiri (sloupec `lambda_sidereal_deg`) a denní ayanámsou v
  `ayanamsa_deg`.
- `geocentric_sidereal_fagan_bradley_daily.csv` – totéž, ale s ayanámsou
  Fagan/Bradley.
- `geocentric_*_sign_ingresses.csv` – časová razítka, kdy geocentrická délka
  překročí každou tropickou/siderickou hranici 30°.
- `heliocentric_daily.csv`, `barycentric_daily.csv` – vektory polohy/rychlosti
  v heliocentrickém a barycentrickém rámci sluneční soustavy.

Tipy k použití
--------------
- Importujte do tabulkových procesorů (Excel, LibreOffice), vědeckých notebooků
  nebo skriptovacích prostředí (Python/pandas, R atd.).
- Délky jsou ve stupních; pokud potřebujete, normalizujte je nebo převeďte na radiány.
- Vzdálenosti jsou v astronomických jednotkách (AU); rychlosti v km/s.
- Využijte siderické tabulky, chcete-li mít předem posunuté délky—jinak
  odečtěte preferovanou ayanámsu od tropické délky.
- Datová perioda je 1 den; interpolujte, pokud potřebujete jemnější
  časové rozlišení.
