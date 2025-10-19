KIT DE HERRAMIENTAS PARA DESARROLLADORES
=======================================

Esta carpeta reúne todo lo necesario para regenerar el paquete de efemérides
desde cero.

Contenido
---------
- `raw/` – respuestas JSON obtenidas de la API NASA/JPL Horizons.
- `scripts/generate_ephemeris.py` – script de Python que reconstruye los CSV,
  los archivos de texto de Solar Fire, la salida MPC y los resúmenes de ingreso en signos.
- `scripts/build_swisseph.sh` – asistente para convertir tablas CSV en binarios
  Swiss Ephemeris `.se1` (requiere `mksweph`).
- `vendor/` – módulo `pyswisseph` incluido para que las salidas siderales funcionen
  sin instalaciones adicionales.

Regeneración
------------
```
cd developer/scripts
python3 generate_ephemeris.py
```
El script vuelve a consultar Horizons (se necesita conexión) y actualiza
las carpetas en la raíz del repositorio.

Binarios de Swiss Ephemeris
---------------------------
Si tienes acceso a la utilidad propietaria `mksweph`:
```
cd developer/scripts
bash build_swisseph.sh
```
Esto escribe archivos `.se1` en `../swisseph/` para su distribución.

Siéntete libre de modificar el script para cambiar cadencia, sistemas de coordenadas
o cuerpos de referencia; los JSON brutos permiten rastrear la información hasta Horizons.

Para notas de uso detalladas, incluido el actualizador SBDB y las herramientas de verificación,
consulta `scripts/README.md`.
