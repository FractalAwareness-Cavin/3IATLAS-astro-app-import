# 3I/ATLAS — Paquete de importación (v0.2)

Usa este paquete cuando necesites **elementos orbitales MPC listos para usar**
o un asistente específico de plataforma para llevar 3I/ATLAS a software de astronomía.
Todo funciona sin conexión y se basa en la solución 27 del JPL SBDB (2025-10-10).

> **TL;DR**
> - **Stellarium** → importa la línea proporcionada mediante *Solar System Editor → Import elements in MPC format*.
> - **KStars** → ejecuta el asistente sin instalación (Windows/macOS/Linux) o pega la línea `comets.dat` incluida.
> - **SkySafari** → usa *Settings → Solar System → Update Orbit Data* (Plus/Pro) y guarda la línea MPC como referencia.
> - **Solar Fire** → fusiona el bloque `[3I_ATLAS]` en `extras.dat` (haz una copia de seguridad primero); se incluyen scripts auxiliares.
> - **Astro Gold / TimePassages** → actualmente no admiten importación de cuerpos móviles; consulta las notas del repositorio principal para soluciones con puntos fijos.

## Contenido

- `templates/stellarium/3I_ATLAS_mpc_elements.txt` — elemento MPC de una línea para 3I/ATLAS.
- `templates/skysafari/3I_ATLAS_mpc_1line.txt` — la misma línea para archivo/referencia.
- `templates/kstars/3I_ATLAS_comets_dat_snippet.txt` — línea lista para añadir a `comets.dat` (también válida para Cartes du Ciel / WinStars).
- `templates/solar_fire/3I_ATLAS_extras_dat_PLACEHOLDER.txt` — bloque `[3I_ATLAS]` listo para `extras.dat` de Solar Fire.
- `tools/3i_elements_to_formats.py` — conversor opcional si pegas una nueva línea MPC.
- `tools/update_orbital_elements.py` — obtiene la última solución del JPL SBDB y reescribe todas las plantillas.
- `docs/WORKFLOWS.md` — instrucciones paso a paso para Stellarium, KStars, Cartes du Ciel, WinStars, SkySafari, Solar Fire.

## Inicio rápido

¿Ya estás al día? Ve directo a `docs/WORKFLOWS.md`. Para actualizar cada vez que JPL
publique una nueva órbita, ejecuta el actualizador:
```bash
python tools/update_orbital_elements.py --dry-run  # vista previa de los últimos elementos
python tools/update_orbital_elements.py            # reescribe las plantillas
```
Si prefieres reemplazar los archivos manualmente, `tools/3i_elements_to_formats.py`
producirá los fragmentos para Stellarium/KStars/Solar Fire a partir de cualquier línea MPC.

## Advertencias

- **Solar Fire `extras.dat`**: el orden de los campos puede variar según la versión. Consulta
a la ayuda incorporada “Format of the Orbital Elements File” para ediciones manuales y haz siempre una copia de seguridad.
- **SkySafari**: no existe importación manual de archivos; confía en *Update Orbit Data*.
- **Astro Gold / TimePassages**: en el momento de redactar esto no exponen un flujo de importación de cuerpos móviles. Usa sus puntos personalizados fijos o pide soporte al proveedor.
- **Validación**: ejecuta `tools/verify_ephemeris.py` para comparar filas seleccionadas de
`apps-using-mpc-files/geocentric_mpc_ephemeris.txt` con datos en vivo de Horizons si
quieres verificar la efeméride.
