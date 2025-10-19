3I/ATLAS — Importación rápida en Cartes du Ciel (SkyCharts)
==========================================================

Cartes du Ciel lee elementos de cometas estándar MPC. Usa la línea proporcionada (`../import-pack/3I-ATLAS/templates/stellarium/3I_ATLAS_mpc_elements.txt`) o la copia de esta carpeta para añadir 3I/ATLAS.

### Opción A — importar desde la interfaz
1. Inicia Cartes du Ciel.
2. Abre **Setup → Solar system** (o `Ctrl+F3`).
3. En la pestaña **Comets** pulsa **Update** (o **Import from MPC file**).
4. Elige **File on disk** y selecciona `3I_ATLAS_mpc_1line.txt`.
5. Tras el import, marca **3I/ATLAS** en la lista y pulsa **OK**.

### Opción B — edición manual
1. Cierra Cartes du Ciel.
2. Haz copia de `comet.dat`:
   - Windows: `%LOCALAPPDATA%\Skychart\cat\comet.dat`
   - Linux: `~/.skychart/cat/comet.dat`
   - macOS: `~/Library/Application Support/skychart.cat/comet.dat`
3. Añade la línea de `3I_ATLAS_mpc_1line.txt` a `comet.dat`.
4. Reinicia Cartes du Ciel y habilita **3I/ATLAS** en la lista de cometas.

La línea se basa en la solución 27 del JPL SBDB (2025-10-10). Vuelve a importarla cuando se publique una nueva solución.
