# Paquete de importación 3I/ATLAS

Plantillas de inicio rápido, scripts auxiliares y documentación para llevar
**3I/ATLAS (C/2025 N1)** a software de astronomía compatible con MPC.

## Contenido
- `docs/INSTALL_3I-ATLAS.md` — visión general, advertencias y guía rápida (actualmente v0.2).
- `docs/WORKFLOWS.md` — instrucciones paso a paso para Stellarium, KStars,
  SkySafari, Solar Fire y notas sobre aplicaciones no compatibles.
- `templates/` — elementos MPC de una línea listos para usar, entrada `comets.dat` para KStars
  y bloque `[3I_ATLAS]` para Solar Fire (todos basados en la solución 27 de JPL SBDB).
- `tools/3i_elements_to_formats.py` — conversor opcional: pega un nuevo
  elemento MPC de una línea y las plantillas se reescriben automáticamente.
- `tools/kstars/` — asistentes para Windows/macOS/Linux que realizan copia de seguridad
  y añaden la línea de KStars.
- `tools/solarfire/` — asistentes para Windows que respaldan y fusionan el bloque
  `extras.dat` para 3I/ATLAS.

## Resumen de uso
- Stellarium: importa la línea proporcionada mediante **Solar System Editor → Import elements in MPC format → File**.
- KStars: ejecuta el script correspondiente a tu sistema operativo o añade manualmente la línea proporcionada a `comets.dat`.
- SkySafari: usa **Settings → Solar System → Update Orbit Data** (niveles Plus/Pro).  
- Solar Fire: fusiona el bloque `[3I_ATLAS]` en `extras.dat` (haz una copia de seguridad primero).  
- Astro Gold / TimePassages: actualmente no permiten importar cuerpos móviles; consulta las notas del repositorio si necesitas puntos fijos personalizados.

Actualiza las plantillas con el script conversor cada vez que se publique una nueva solución orbital.
