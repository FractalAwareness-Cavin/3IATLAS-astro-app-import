# Scripts para desarrolladores

Las utilidades para regenerar y validar el kit de efemérides 3I/ATLAS viven en `developer/scripts/` y `tools/`. Usa esta guía cuando necesites actualizar el conjunto de datos o verificar los cambios antes de publicar una nueva versión.

## Requisitos previos
- Python 3.10 o superior (`python3 --version` para comprobar).
- Opcional: un entorno virtual (`python3 -m venv .venv && source .venv/bin/activate`) si planeas instalar paquetes adicionales.
- Acceso a internet al ejecutar el actualizador SBDB o el verificador de Horizons.
- Opcional: `mksweph` si quieres generar binarios de Swiss Ephemeris con `build_swisseph.sh`.

El repositorio incluye `pyswisseph` en `developer/vendor/`, por lo que las salidas siderales funcionan sin instalaciones extra.

## Receta Horizons predeterminada

Los JSON brutos de `developer/raw/` se generaron con NASA/JPL Horizons usando estos parámetros:

```
COMMAND='DES=1004083;'
MAKE_EPHEM='YES'
EPHEM_TYPE='VECTORS'
CENTER='500@399'        # centro de la Tierra
REF_PLANE='ECLIPTIC'
REF_SYSTEM='J2000'
START_TIME='2016-01-01'
STOP_TIME='2040-12-31'
STEP_SIZE='1 d'
TABLE_TYPE='VECTORS'
```

Ajusta los valores si necesitas otra ventana temporal o un punto de vista distinto, y vuelve a generar los JSON antes de rehacer las salidas.

## `generate_ephemeris.py`
Ubicación: `developer/scripts/generate_ephemeris.py`

- Lee los volcamientos de vectores JSON en `developer/raw/` y reescribe cada producto derivado:
  - Tablas CSV en `apps-using-csv-files/`
  - Tablas de texto para Solar Fire en `solar-fire/`
  - Efeméride MPC (`apps-using-mpc-files/geocentric_mpc_ephemeris.txt`)
  - Resúmenes de tránsitos por signo.
- Carga automáticamente el módulo `pyswisseph` incluido para completar los campos siderales.
- Crea los directorios destino si no existen.

Uso:

```
cd developer/scripts
python3 generate_ephemeris.py
```

El script usa ajustes integrados. Para modificar el intervalo temporal o la cadencia, actualiza primero los JSON (o edita las constantes al inicio del script).

## `build_swisseph.sh`
Ubicación: `developer/scripts/build_swisseph.sh`

- Requiere la herramienta propietaria `mksweph`.
- Convierte las salidas CSV en binarios `.se1` de Swiss Ephemeris y los guarda en `developer/swisseph/`.

Uso:

```
cd developer/scripts
bash build_swisseph.sh
```

El asistente se niega a ejecutarse si `mksweph` no está en tu `PATH`.

## `tools/update_orbital_elements.py`
Ubicación: `tools/update_orbital_elements.py`

- Obtiene la última solución orbital SBDB para 3I/ATLAS y actualiza todos los modelos de una sola línea:
  - Archivos MPC (`apps-using-mpc-files/*/3I_ATLAS_mpc_1line.txt`)
  - Fragmentos de KStars (`apps-using-mpc-files/kstars/` y plantillas del paquete de importación)
  - Bloques `extras.dat` de Solar Fire.
- Imprime los elementos recuperados en stdout para facilitar la auditoría.

Uso (desde la raíz del repositorio):

```
python tools/update_orbital_elements.py
```

Añade `--dry-run` para previsualizar los valores sin modificar archivos.

## `tools/verify_ephemeris.py`
Ubicación: `tools/verify_ephemeris.py`

- Verifica filas de `apps-using-mpc-files/geocentric_mpc_ephemeris.txt` frente a datos en vivo de Horizons.
- Compara la distancia geocéntrica («delta») en un rango de fechas configurable y marca las filas que exceden la tolerancia.

Uso (desde la raíz del repositorio):

```
python tools/verify_ephemeris.py --start 2025-10-01 --days 5 --tolerance 5e-4
```

Argumentos:
- `--start`: primera fecha a verificar (predeterminado `2025-10-01`).
- `--days`: número de días consecutivos a revisar (predeterminado `5`).
- `--tolerance`: diferencia máxima en unidades astronómicas (predeterminado `5e-4`, ~75 000 km).

El script finaliza con un código distinto de cero si encuentra errores, por lo que se puede usar en CI.
