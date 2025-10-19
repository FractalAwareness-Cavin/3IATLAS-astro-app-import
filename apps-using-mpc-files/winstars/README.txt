3I/ATLAS — WinStars Quick Import
================================

WinStars (v3) can ingest MPC comet elements via the built-in editor.

### Method 1 — paste the one-line element
1. Start WinStars.
2. Open **Preferences → Solar system → Import orbital elements** (or **Add object**).
3. Choose **MPC single line** and paste the contents of `3I_ATLAS_mpc_1line.txt`.
4. Confirm and ensure 3I/ATLAS is enabled in the list of displayed bodies.

### Method 2 — replace the comets file (advanced)
1. Quit WinStars.
2. Backup the comets data file:
   - Windows: `%APPDATA%\WinStars3\databases\comets.txt`
   - Linux: `~/.config/WinStars3/databases/comets.txt`
3. Append the single line from `3I_ATLAS_mpc_1line.txt` to that file.
4. Relaunch WinStars; 3I/ATLAS will be listed under comets.

The one-line file is based on JPL SBDB solution 27 (2025-10-10). Update it when a
new solution becomes available.
