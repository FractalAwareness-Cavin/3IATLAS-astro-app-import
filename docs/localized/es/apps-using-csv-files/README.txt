DATOS CSV DE 3I/ATLAS
=====================

Esta carpeta contiene las tablas CSV generadas a partir de NASA/JPL Horizons.
Cada archivo usa fechas TDB a las 00:00 y el marco eclíptico de J2000,
a menos que se indique lo contrario.

Archivos
--------
- `geocentric_daily.csv` – longitudes/latitudes/distancias eclípticas tropicales
  más coordenadas cartesianas y componentes de velocidad heliocéntricas.
- `geocentric_sidereal_lahiri_daily.csv` – longitudes siderales derivadas con
  el ayanāṃśa de Lahiri (columna `lambda_sidereal_deg`) y el ayanāṃśa diario en
  `ayanamsa_deg`.
- `geocentric_sidereal_fagan_bradley_daily.csv` – igual que el anterior pero con
  el ayanāṃśa Fagan/Bradley.
- `geocentric_*_sign_ingresses.csv` – marcas temporales cuando la longitud geocéntrica
  cruza cada frontera tropical/sideral de 30°.
- `heliocentric_daily.csv`, `barycentric_daily.csv` – vectores de posición/velocidad
  en los marcos heliocéntrico y baricéntrico del sistema solar.

Sugerencias de uso
------------------
- Importa los archivos en hojas de cálculo (Excel, LibreOffice), cuadernos científicos
  o entornos de scripting (Python/pandas, R, etc.).
- Las longitudes están en grados; envuélvelas o conviértelas a radianes según convenga.
- Las distancias están en unidades astronómicas (UA); las velocidades en km/s.
- Usa las tablas siderales cuando necesites longitudes ya corregidas; de lo contrario
  resta tu ayanāṃśa preferido de la longitud tropical.
- La cadencia de los datos es diaria; interpola si necesitas una resolución superior.
