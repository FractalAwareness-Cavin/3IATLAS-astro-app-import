# Kit de efemérides 3I/ATLAS

Efemérides diarias para el cometa interestelar **3I/ATLAS (C/2025 N1)**, generadas directamente desde NASA/JPL Horizons y organizadas para que astrólogos y astrónomas puedan integrarlo en sus aplicaciones favoritas. La cobertura abarca todo el paso por la heliosfera (2016‑01‑01 → 2040‑12‑31). Esta versión usa la **solución Horizons nº 27 (2025‑10‑10)**; ejecuta `tools/update_orbital_elements.py` cuando JPL publique una solución más reciente y quieras actualizar los archivos auxiliares.

## Guía rápida
1. Descarga el paquete que coincida con tu aplicación (ver **Descargas directas**), o clona este repositorio.
2. Descomprime el paquete para acceder al `README` específico de cada carpeta.
3. Sigue la lista de pasos del `README` o ejecuta los scripts incluidos para Solar Fire, KStars y Stellarium.
4. Mantenimiento opcional: ejecuta `python tools/update_orbital_elements.py` para traer la última solución SBDB y `python tools/verify_ephemeris.py` para comprobar algunas fechas antes de redistribuir.

## Tabla de contenidos
- [Guía rápida](#guía-rápida)
- [Aplicaciones compatibles (importación de cuerpos móviles)](#aplicaciones-compatibles-importación-de-cuerpos-móviles)
- [¿Por dónde empiezo?](#por-dónde-empiezo)
- [Descargas directas](#descargas-directas)
- [Guía de carpetas](#guía-de-carpetas)
- [Glosario](#glosario)
- [Instrucciones por aplicación](#instrucciones-por-aplicación)
  - [Paquete de importación y scripts](#paquete-de-importación-y-scripts)
  - [Estado de Astro Gold](#estado-de-astro-gold)
  - [Solar Fire (Windows)](#solarfire-instructions-windows)
  - [Importación en formato MPC](#importación-en-formato-mpc)
  - [Astro Gold & TimePassages](#astro-gold--timepassages)
  - [Notas sobre CSV](#notas-sobre-csv)
- [Receta Horizons](#receta-horizons)
- [Regenerar las efemérides](#regenerar-las-efemérides)
- [Scripts de mantenimiento](#scripts-de-mantenimiento)
- [Hitos clave](#hitos-clave)
- [Notas y advertencias](#notas-y-advertencias)
- [Solución de problemas](#solución-de-problemas)
- [Opcional: instalar herramientas Horizons](#opcional-instalar-herramientas-horizons)

Aplicaciones compatibles (importación de cuerpos móviles)
--------------------------------------------------------
- **Stellarium** (Win/macOS/Linux): importación mediante Solar System Editor en formato MPC.
- **KStars** (Win/macOS/Linux): añadir a `comets.dat` (se incluyen asistentes).
- **Solar Fire** (Windows): fusionar el bloque `[3I_ATLAS]` en `extras.dat`.
- **Cartes du Ciel / SkyCharts** (Win/macOS/Linux): importar archivos MPC o editar `comet.dat`.
- **WinStars 3** (Win/macOS/Linux): pegar la línea MPC en el editor de objetos.
- **SkySafari / SkyVoyager Plus/Pro** (iOS/Android/macOS): usar la actualización de datos orbitales desde feeds MPC.

Sin importación de cuerpos móviles:
- **Astro Gold** (macOS/iOS/iPadOS) y **TimePassages** (macOS/Windows). Consulta las soluciones de puntos fijos si necesitas referencias estáticas.

¿Algo no queda claro? Escríbeme a [cavinbirdseyetarot@gmail.com](mailto:cavinbirdseyetarot@gmail.com) y seguiré mejorando la documentación.



## ¿Por dónde empiezo?

Usa la carpeta que coincide con tu software o descarga una de las siguientes. Si dudas, abre tu aplicación y revisa *Archivo → Importar* (o similar) para ver qué formatos admite.

- `solar-fire/`: entrada `extras.dat` para Solar Fire y efemérides de referencia.
- `apps-using-mpc-files/`: archivo MPC de 80 columnas `geocentric_mpc_ephemeris.txt` (diario, UT 0h, RA/Dec J2000, Δ, r, elongación, fase).
- `apps-using-csv-files/`: vectores heliocéntricos, geocéntricos y baricéntricos en CSV, cambios de signo, latitudes.
- `developer/`: volcados JSON de Horizons, scripts de regeneración, `pyswisseph` incluido y helper de Swiss Ephemeris.
- `Time-Passages-Astro-Gold/`: limitaciones actuales de Astro Gold/TimePassages y métodos con puntos fijos.

#### Descargas directas
- [Asistente de fusión Solar Fire (Windows)](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/SolarFire_merge-helper_Windows.zip)
- [Paquete de anexado rápido KStars (Win/macOS/Linux)](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/KStars_quick-append_Win-Mac-Linux.zip)
- [Importación rápida Stellarium](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/Stellarium_quick-import.zip)
- [Efeméride MPC (80 columnas)](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/3I-ATLAS_apps_using_mpc_files.zip)
- [Kit de investigación CSV](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/3I-ATLAS_apps_using_csv_files.zip)

Cada archivo refleja la carpeta correspondiente e incluye un `README.txt` con pasos específicos; descomprime antes de ejecutar scripts o copiar archivos.

## Guía de carpetas

- **solar-fire/**: extras de Solar Fire (`extras.dat`) y efemérides de control.
- **apps-using-mpc-files/**: efeméride MPC diaria completa, líneas individuales y guías por app.
- **apps-using-csv-files/**: tablas CSV heliocéntricas/geocéntricas/baricéntricas, ingresos en signo y métricas.
- **developer/**: scripts, `pyswisseph` vendorizado, datos sin procesar, utilidades de Swiss Ephemeris.
- **Time-Passages-Astro-Gold/**: soluciones para programas sin importación.
- **import-pack/**: paquete compacto con plantillas, scripts y docs listo para distribución.

## Glosario

- **MPC 80 columnas**: formato clásico del Minor Planet Center.
- **Horizons SBDB**: base de datos de cuerpos menores de NASA/JPL.
- **Elongación**: separación angular Sol-objeto vista desde la Tierra.
- **Δ (delta)**: distancia geocéntrica.
- **r**: distancia heliocéntrica.
- **UT**: Tiempo Universal / UTC.

## Instrucciones por aplicación

### Paquete de importación y scripts

Consulta `import-pack/3I-ATLAS/README.md` para conocer plantillas, scripts y flujo de actualización.

### Estado de Astro Gold

Sin importación de cuerpos móviles; revisa `Time-Passages-Astro-Gold/` para puntos fijos personalizados.

### SolarFire instructions Windows

`solar-fire/README.txt` explica cómo fusionar `[3I_ATLAS]` en `extras.dat`. Usa los helpers de `tools/solarfire/` para previsualizar y aplicar.

### Importación en formato MPC

Los subdirectorios bajo `apps-using-mpc-files/` incluyen `README` específicos y archivos listos para Stellarium, KStars, Cartes du Ciel, WinStars.

### Astro Gold & TimePassages

No admiten cuerpos móviles por ahora; crea puntos fijos con fechas concretas.

### Notas sobre CSV

`apps-using-csv-files/README.txt` detalla columnas y unidades para usar los datos en hojas de cálculo, cuadernos científicos o scripts. Para trabajo sidéreo, resta tu ayanāṃśa preferido de la longitud tropical.

## Receta Horizons

`developer/raw/` contiene JSON generados con Horizons usando:

```
COMMAND='DES=1004083;'
MAKE_EPHEM='YES'
EPHEM_TYPE='VECTORS'
CENTER='500@399'
REF_PLANE='ECLIPTIC'
REF_SYSTEM='J2000'
START_TIME='2016-01-01'
STOP_TIME='2040-12-31'
STEP_SIZE='1 d'
TABLE_TYPE='VECTORS'
```

Ajusta valores si necesitas otra ventana temporal o punto de observación y vuelve a generar los JSON antes de rehacer las salidas.

## Regenerar las efemérides

### `developer/scripts/generate_ephemeris.py`

- Lee los JSON de `developer/raw/` y vuelve a escribir:
  - Tablas CSV (`apps-using-csv-files/`)
  - Tablas de texto para Solar Fire (`solar-fire/`)
  - Efeméride MPC (`apps-using-mpc-files/geocentric_mpc_ephemeris.txt`)
  - Resúmenes de ingresos en signo.
- Crea los directorios destino si faltan.

```
cd developer/scripts
python3 generate_ephemeris.py
```

### `developer/scripts/build_swisseph.sh`

- Requiere la utilidad propietaria `mksweph`.
- Convierte los CSV en binarios `.se1` de Swiss Ephemeris (`developer/swisseph/`).

```
cd developer/scripts
bash build_swisseph.sh
```

### `tools/update_orbital_elements.py`

- Obtiene la solución SBDB más reciente y actualiza archivos MPC, snippets de KStars y bloques de Solar Fire.

```
python tools/update_orbital_elements.py
```

Agrega `--dry-run` para ver valores sin modificar archivos.

### `tools/verify_ephemeris.py`

- Compara filas de `apps-using-mpc-files/geocentric_mpc_ephemeris.txt` contra datos en vivo de Horizons.

```
python tools/verify_ephemeris.py --start 2025-10-01 --days 5 --tolerance 5e-4
```

Por defecto: inicio `2025-10-01`, 5 días, tolerancia `5e-4` UA (~75 000 km). Falla con código distinto de cero si encuentra discrepancias—ideal para CI.

## Scripts de mantenimiento

- **`tools/3i_elements_to_formats.py`**: convierte un nuevo MPC de una línea en plantillas (Stellarium, KStars, Solar Fire).
- **`tools/kstars/`**: scripts por sistema operativo para respaldar y anexar `comets.dat`.
- **`tools/solarfire/`**: helpers de Windows que fusionan `extras.dat` automáticamente.

## Hitos clave

- 2024-10-xx: primera extracción Horizons y estructura de carpetas.
- 2025-10-xx: actualización a solución SBDB 27.
- 2025-10-xx: añadidos scripts de verificación y paquete de importación.

## Notas y advertencias

- **Solar Fire**: haz copia de `extras.dat` antes de fusionar.
- **SkySafari**: no admite importación de archivos; usa *Update Orbit Data*.
- **Astro Gold / TimePassages**: sin importación dinámica; depende de puntos fijos.
- **Validación**: `tools/verify_ephemeris.py` compara rápidas contra Horizons.

## Solución de problemas

- **3I/ATLAS no aparece tras el import.** Reinicia la app y verifica la ortografía `3I/ATLAS`.
- **Las posiciones parecen desplazadas.** El archivo MPC está en **UT 0h**; trabaja en UTC o aplica la corrección horaria.
- **Solar Fire sigue mostrando la lista anterior.** Comprueba la ruta de `extras.dat` (cada versión tiene carpeta propia) o ejecuta de nuevo el helper APPLY.
- **Quiero contrastar los datos.** `python tools/verify_ephemeris.py` compara con Horizons en vivo.

¡Que disfrutes chartando 3I/ATLAS!

## Opcional: instalar herramientas Horizons

No es obligatorio (el kit ya trae los datos), pero si quieres generar efemérides:

### macOS / Linux
1. Asegura `python3 --version` ≥ 3.10.
2. Instala Astroquery:
   ```bash
   python3 -m pip install astroquery --user
   ```
3. Consulta Horizons:
   ```bash
   python3 - <<'PY'
   from astroquery.jplhorizons import Horizons
   obj = Horizons(id='DES=1004083;', location='500@399', epochs={'start':'2025-01-01', 'stop':'2025-01-10', 'step':'1d'})
   print(obj.vectors())
   PY
   ```

Alternativa:

```bash
curl "https://ssd.jpl.nasa.gov/api/horizons.api?format=json&COMMAND='DES=1004083;'&MAKE_EPHEM=YES&EPHEM_TYPE=VECTORS&CENTER='500@399'&REF_PLANE=ECLIPTIC&STEP_SIZE=1%20d&START_TIME=2025-01-01&STOP_TIME=2025-01-03"
```

### Windows
1. Instala Python 3 desde https://www.python.org/downloads/ (marca “Add Python to PATH”).
2. En PowerShell:
   ```powershell
   py -m pip install astroquery
   py - <<'PY'
   from astroquery.jplhorizons import Horizons
   obj = Horizons(id='DES=1004083;', location='500@399', epochs={'start':'2025-01-01', 'stop':'2025-01-10', 'step':'1d'})
   print(obj.vectors())
   PY
   ```
3. Con WSL, sigue las instrucciones de macOS/Linux.

### CLI clásica (Telnet)
```bash
telnet horizons.jpl.nasa.gov 6775
```
Sigue las indicaciones introduciendo `DES=1004083;` y las opciones deseadas.

### Instalar Python 3.10+ en Linux

Consulta la documentación de tu distribución (apt, dnf, zypper, pacman…). Si no hay versión reciente, usa pyenv o compila desde la fuente. Incluso si tu sistema ya trae Python, conviene instalar una versión propia ≥3.10 y trabajar con entornos virtuales (`python3 -m venv`).
