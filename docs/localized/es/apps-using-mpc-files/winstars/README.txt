3I/ATLAS — Importación rápida en WinStars
=========================================

WinStars (v3) puede ingerir elementos de cometas MPC mediante el editor integrado.

### Método 1 — pegar la línea única
1. Inicia WinStars.
2. Abre **Preferences → Solar system → Import orbital elements** (o **Add object**).
3. Elige **MPC single line** y pega el contenido de `3I_ATLAS_mpc_1line.txt`.
4. Confirma y verifica que 3I/ATLAS esté habilitada en la lista de cuerpos visibles.

### Método 2 — reemplazar el archivo de cometas (avanzado)
1. Cierra WinStars.
2. Haz copia del archivo de cometas:
   - Windows: `%APPDATA%\WinStars3\databases\comets.txt`
   - Linux: `~/.config/WinStars3/databases/comets.txt`
3. Añade la línea de `3I_ATLAS_mpc_1line.txt` a ese archivo.
4. Reinicia WinStars; 3I/ATLAS aparecerá en la lista de cometas.

El archivo de una línea usa la solución 27 del JPL SBDB (2025-10-10). Actualízalo cuando haya una nueva solución.
