# Flujos de trabajo por aplicación para 3I/ATLAS

Todos los valores de este paquete provienen de la solución 27 del JPL SBDB (2025-10-10).
Actualiza los archivos con el script conversor cuando se publique una solución más reciente.

## Stellarium (Windows/macOS/Linux)

**Acepta:** elementos de cometa MPC de una línea  
**Pasos:**
1. **Configuration → Plugins → Solar System Editor** → marca **Load at startup** (reinicia si es necesario).  
2. **Solar System Editor → Configure → Solar System → Import elements in MPC format → File**.  
3. Selecciona `templates/stellarium/3I_ATLAS_mpc_elements.txt`.  
4. Haz clic en **Add object(s)** y busca **3I/ATLAS**.

## KStars (Windows/macOS/Linux)

**Acepta:** línea `comets.dat`  
**Asistentes:**
- Windows: `tools/kstars/KStars_Append_3I-DRYRUN.bat` (vista previa) y luego `…-APPLY.bat`.  
- macOS: haz doble clic en `tools/kstars/KStars_Append_3I.command`.  
- Linux: ejecuta `bash tools/kstars/KStars_Append_3I.sh`.  
Todos los asistentes crean una copia de seguridad antes de añadir la línea.

Manual:
1. Haz una copia de seguridad de `comets.dat` (`~/.local/share/kstars/comets.dat` en Linux, `%LOCALAPPDATA%\kstars\comets.dat` en Windows, `~/Library/Application Support/kstars/comets.dat` en macOS).  
2. Añade la línea única de `templates/kstars/3I_ATLAS_comets_dat_snippet.txt`.  
3. Reinicia KStars y busca **3I/ATLAS**.

## SkySafari / SkyVoyager (iOS/Android)

**Acepta:** sin importación manual  
Usa *Settings → Solar System → Update Orbit Data* (niveles Plus/Pro). Conserva
`templates/skysafari/3I_ATLAS_mpc_1line.txt` solo como referencia.

## Cartes du Ciel (SkyCharts)

**Acepta:** archivos de elementos MPC  
Sigue las instrucciones de `apps-using-mpc-files/cartes-du-ciel/README.txt`
(importación mediante GUI o adición manual a `comet.dat`).

## WinStars 3

**Acepta:** archivos de elementos MPC  
Consulta `apps-using-mpc-files/winstars/README.txt` para los pasos de importación rápida.

## Solar Fire (Windows)

**Acepta:** elementos orbitales `extras.dat` (Other Bodies)  
**Asistentes:**
- Windows: `tools/solarfire/SF_Merge_3I-DRYRUN.bat` (vista previa) y luego `…-APPLY.bat` para fusionar automáticamente `[3I_ATLAS]`.  
Ambos scripts crean una copia de seguridad de `extras.dat` con marca de tiempo.

Manual:
1. Cierra Solar Fire y haz una copia de seguridad de `Documents\Solar Fire User Files\Userdata\extras.dat`.  
2. Copia o fusiona el bloque `[3I_ATLAS]` desde `templates/solar_fire/3I_ATLAS_extras_dat_PLACEHOLDER.txt`.  
3. Vuelve a iniciar y habilita **3I/ATLAS** en **Extra Bodies** dentro del cuadro de selección de puntos.

## Aplicaciones sin canal de importación

Astro Gold (macOS/iOS/iPadOS) y TimePassages Desktop (macOS/Windows) solo ofrecen puntos extra
proporcionados por el proveedor y no aceptan efemérides de cuerpos móviles aportadas por el usuario.
Consulta la carpeta `Time-Passages-Astro-Gold/` para soluciones con puntos fijos y enlaces de contacto con el proveedor.
