3I/ATLAS — KStars Quick Append (Windows/macOS/Linux)
====================================================

The helpers in `tools/` back up your `comets.dat`, remove any older 3I/ATLAS entry, and append the refreshed line sourced from **JPL SBDB solution 27 (2025-10-10)**.

Files inside this zip
---------------------
- `tools/MacOS_SEEREADME_KStars_Append_3I.command`
- `tools/Linux_KStars_Append_3I.sh`
- `tools/Windows_KStars_Append_3I-DRYRUN.bat`
- `tools/Windows_KStars_Append_3I-APPLY.bat`
- `tools/Windows_KStars_Append_3I.ps1`
- `tools/append_line.sh`
- `3I_ATLAS_comets_dat_line.txt` (manual snippet)
- `3I_ATLAS_mpc_1line.txt` (shared MPC element)

Run the helper (all platforms)
------------------------------
1. **Preview first.**
   - Windows: double-click `tools/Windows_KStars_Append_3I-DRYRUN.bat`.
   - macOS: double-click `tools/MacOS_SEEREADME_KStars_Append_3I.command`. If Gatekeeper warns “Apple could not verify…”, click **Done**, open **System Settings → Privacy & Security**, scroll to the bottom, and press **Open Anyway**. macOS reopens the helper automatically—choose **Open** in the confirmation dialog and approve with Touch ID or your account password if prompted. Those requests come from macOS; the helper never sees or stores your credentials. Terminal opens automatically afterwards—when you are ready, type `y` and press **Enter**.
   - Linux: open a terminal and run `bash tools/Linux_KStars_Append_3I.sh --dry-run`.
   You will see the detected `comets.dat` path and the single line that will be appended.
2. **Apply when satisfied.**
   - Windows: run `tools/Windows_KStars_Append_3I-APPLY.bat`.
   - macOS: run the `.command` file again and answer **y** at the prompt.
   - Linux: run `bash tools/Linux_KStars_Append_3I.sh --apply`.
   Each script creates a timestamped backup before writing.

After appending
---------------
1. Restart KStars so it reloads `comets.dat`.
2. Use **Pointing → Find Object…** (or the search icon / `Ctrl+F`) to look up `3I/ATLAS`, then press **Ok** to center and track it. If warned that the comet is below the horizon, acknowledge the message.
3. Right-click the comet and choose **Center & Track** to keep it in view, or open **Tools → Solar System** (`Ctrl+Y`) for the Solar System Viewer if you want to inspect the orbit from above.

Manual alternative
------------------
Copy `3I_ATLAS_comets_dat_line.txt`, back up your existing `comets.dat`, remove any older 3I/ATLAS lines, append the new one, then restart KStars. Typical locations:
- Linux: `~/.local/share/kstars/comets.dat`
- macOS: `~/Library/Application Support/kstars/comets.dat`
- Windows: `%APPDATA%\kstars\comets.dat`
