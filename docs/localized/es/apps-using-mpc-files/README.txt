3I/ATLAS – GUÍA DE IMPORTACIÓN MPC
==================================

`geocentric_mpc_ephemeris.txt` contiene efemérides diarias al estilo MPC (UT 0h, RA/Dec J2000, delta, r, elongación, fase). Úsala en cualquier software que acepte el formato clásico de cometas de 80 columnas. Los paquetes listos están en las releases (ver `README.md` en la raíz) o en `apps-using-mpc-files/`.

Paquetes de la release
----------------------
- `Stellarium_quick-import.zip`: importa el archivo MPC de un solo objeto mediante el complemento Solar System Editor.
- `KStars_quick-append_Win-Mac-Linux.zip`: scripts de vista previa/aplicación para `comets.dat` en cada plataforma.
- `3I-ATLAS_apps_using_mpc_files.zip`: incluye esta carpeta, con plantillas de una línea para Cartes du Ciel y WinStars.

Stellarium (Win/macOS/Linux)
----------------------------
1. Descomprime `Stellarium_quick-import.zip` o copia `geocentric_mpc_ephemeris.txt` en una ruta conocida.
2. En Stellarium presiona `F2`, abre **Plugins → Solar System Editor**, marca **Load at startup** y pulsa **Configure**. Reinicia si acabas de habilitar el complemento.
3. Tras el reinicio abre **Solar System Editor → Solar System** y pulsa **Import orbital elements in MPC format**.
4. Elige **Select file**, apunta a `geocentric_mpc_ephemeris.txt` (o al archivo de una línea), pon **Object name** en `3I/ATLAS` y deja **Object type** en *Comet*.
5. Pulsa **Add objects**, cierra los diálogos y busca `3I/ATLAS` con `F3` para confirmar.

KStars (Win/macOS/Linux)
------------------------
1. Descomprime `KStars_quick-append_Win-Mac-Linux.zip` y ejecuta el script adecuado (`*.bat`, `*.command`, `*.sh` o `*.ps1`). Empieza por DRYRUN; si el resultado es correcto, ejecuta APPLY para añadir la cometa a `comets.dat`.
2. Alternativa manual: **Settings → Configure KStars → Solar System** (en versiones antiguas **Data → Solar System Updates**). En la pestaña **Comets** pulsa **Import**, elige `geocentric_mpc_ephemeris.txt` y confirma.
3. Reinicia KStars si se solicita, luego busca `3I/ATLAS` o revisa el visor del sistema solar.

Cartes du Ciel / SkyCharts
--------------------------
1. Copia `apps-using-mpc-files/cartes-du-ciel/3I_ATLAS_mpc_1line.txt` (incluido en el zip de la release).
2. Inicia Cartes du Ciel y abre **Setup → Solar system** (`Ctrl+F3`).
3. En la pestaña **Comets** selecciona **Update → Import from MPC file**, elige `3I_ATLAS_mpc_1line.txt` y confirma.
4. Marca **3I/ATLAS** en la lista y pulsa **OK**; la cometa aparecerá en búsquedas y cartas.
5. ¿Prefieres editar a mano? Añade la misma línea a `comet.dat` (ver el README específico).

WinStars 3 (Win/macOS/Linux)
----------------------------
1. Ten a mano `apps-using-mpc-files/winstars/3I_ATLAS_mpc_1line.txt` o descomprime el paquete MPC.
2. En WinStars abre **Preferences → Solar system → Import orbital elements** (o **Add object**).
3. Selecciona **MPC single line**, pega el contenido y guarda.
4. Asegúrate de que `3I/ATLAS` esté habilitada en la lista de cuerpos; reinicia si el caché de catálogo estaba abierto.

SkySafari / SkyVoyager Plus/Pro (iOS/Android/macOS)
---------------------------------------------------
1. Copia el archivo de una línea (`3I_ATLAS_mpc_1line.txt`) en un editor accesible desde el dispositivo.
2. En SkySafari abre **Settings → Solar System → Solar System Data** y toca **Import Comet Data** (o **Update Orbit Data → Custom Comet/Asteroid** en versiones antiguas).
3. Pega la línea MPC, confirma que el nombre es `3I/ATLAS` y valida.
4. Busca `3I/ATLAS` y añádela a tus listas de observación si quieres.
5. La app refresca periódicamente los feeds MPC; repite el proceso tras actualizar la órbita.

Otro software compatible con MPC
--------------------------------
1. Copia `geocentric_mpc_ephemeris.txt` o la plantilla de una sola línea correspondiente.
2. Usa la función de importación de cometas/asteroides, selecciona el archivo y pon el nombre `3I/ATLAS`.
3. Reinicia el programa si almacena datos del sistema solar en caché y comprueba que el cuerpo esté activo.

Mantén actualizados los archivos de una línea ejecutando `python tools/update_orbital_elements.py` cada vez que el JPL publique una nueva solución SBDB, y verifica posiciones con `python tools/verify_ephemeris.py` para mayor tranquilidad.
