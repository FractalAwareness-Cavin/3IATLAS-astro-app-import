KStars Quick Append Helpers
===========================

The download bundle `KStars_quick-append_Win-Mac-Linux.zip` (and the repo copy under `tools/kstars/`) adds the 3I/ATLAS comet line to `comets.dat`. Every script backs up your file, removes older `3I/ATLAS` entries, and appends the refreshed line from **JPL SBDB solution 27 (2025-10-10)**.

Files by platform
-----------------
- `tools/MacOS_SEEREADME_KStars_Append_3I.command` – macOS launcher; calls the shared shell backend.
- `tools/Linux_KStars_Append_3I.sh` – Linux wrapper around `append_line.sh`.
- `tools/Windows_KStars_Append_3I-DRYRUN.bat` / `tools/Windows_KStars_Append_3I-APPLY.bat` – Windows preview/apply wrappers.
- `tools/Windows_KStars_Append_3I.ps1` – PowerShell backend used by both batch files.
- `tools/append_line.sh` – cross-platform backend (also used inside the repo).
- `3I_ATLAS_comets_dat_line.txt` – raw line for manual edits.
- `3I_ATLAS_mpc_1line.txt` – MPC single-line element shared with other apps.

Recommended workflow
--------------------
1. **Preview first.**  
   - Windows: run `Windows_KStars_Append_3I-DRYRUN.bat`.  
   - macOS: double-click `MacOS_SEEREADME_KStars_Append_3I.command` (it defaults to a dry-run).  
   - Linux: `bash tools/Linux_KStars_Append_3I.sh --dry-run`.
   The helper prints the detected `comets.dat` path and the single line that will be appended.
2. **Apply when ready.**  
   - Windows: run `Windows_KStars_Append_3I-APPLY.bat`.  
   - macOS: relaunch the `.command` script and answer **y** when prompted.  
   - Linux: `bash tools/Linux_KStars_Append_3I.sh --apply`.
3. Restart KStars. Use the built-in tools to jump to the comet:
   - Press the search icon (or **Pointing → Find Object…** / `Ctrl+F`), type `3I/ATLAS`, and press **Ok**. If KStars warns that the comet is below the horizon, acknowledge it and continue.
   - Once the comet is in view, right-click and choose **Center & Track** to keep it locked.
   - For a heliocentric overview, open **Tools → Solar System** (`Ctrl+Y`) to launch the Solar System Viewer and inspect the orbit alongside the planets.

Manual alternative
------------------
Copy `3I_ATLAS_comets_dat_line.txt`, back up your existing `comets.dat` (`~/.local/share/kstars/comets.dat` on Linux, `~/Library/Application Support/kstars/comets.dat` on macOS, `%APPDATA%\kstars\comets.dat` on Windows), remove any older 3I/ATLAS entries, append the new line, and restart KStars.

macOS Gatekeeper
----------------
If macOS reports that it “cannot verify `MacOS_SEEREADME_KStars_Append_3I.command`”:
1. Run the `.command` file once and click **Done** in the warning dialog.
2. Open **System Settings → Privacy & Security**, scroll to the bottom, and click **Open Anyway**.
3. macOS reopens the helper automatically; choose **Open** and approve with Touch ID or your password (the helper never sees your credentials). Terminal will then ask whether to apply the change—type `y` and press **Enter** when ready.

Regenerate the comet line
-------------------------
When JPL publishes a newer solution, run `python tools/update_orbital_elements.py` from the repo root. That script refreshes the helper payload and the manual snippet before you rebuild a download zip.
