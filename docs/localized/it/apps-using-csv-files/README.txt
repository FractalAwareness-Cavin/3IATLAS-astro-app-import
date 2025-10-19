DATI CSV DI 3I/ATLAS
====================

Questa cartella contiene le tabelle CSV generate con NASA/JPL Horizons.
Ogni file usa date TDB alle 00:00 e il sistema di riferimento eclittico J2000,
se non indicato diversamente.

File
----
- `geocentric_daily.csv` – longitudine/latitudine/distante eclittiche tropicali
  più coordinate cartesiane e componenti di velocità eliocentriche.
- `geocentric_sidereal_lahiri_daily.csv` – longitudini siderali calcolate con
  l'ayanāṃśa Lahiri (colonna `lambda_sidereal_deg`) e ayanāṃśa giornaliero in
  `ayanamsa_deg`.
- `geocentric_sidereal_fagan_bradley_daily.csv` – come sopra ma con
  l'ayanāṃśa Fagan/Bradley.
- `geocentric_*_sign_ingresses.csv` – timestamp dei passaggi della longitudine geocentrica
  attraverso ogni confine tropicale/siderale di 30°.
- `heliocentric_daily.csv`, `barycentric_daily.csv` – vettori di posizione/velocità
  nei sistemi di riferimento eliocentrico e baricentrico del sistema solare.

Suggerimenti d'uso
------------------
- Importa i file in fogli di calcolo (Excel, LibreOffice), notebook scientifici
  o ambienti di scripting (Python/pandas, R, ecc.).
- Le longitudini sono espresse in gradi; esegui il wrap o convertile in radianti se necessario.
- Le distanze sono in unità astronomiche (UA); le velocità in km/s.
- Usa le tabelle siderali quando ti servono longitudini già corrette; altrimenti
  sottrai il tuo ayanāṃśa preferito dalla longitudine tropicale.
- L'intervallo dei dati è di 1 giorno; interpolare se serve una risoluzione maggiore.
