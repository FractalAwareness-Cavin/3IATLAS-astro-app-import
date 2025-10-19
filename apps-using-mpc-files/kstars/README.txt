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
3. Restart KStars. Open **Tools → Solar System… → Comets**, raise the magnitude limit if necessary, tick `3I/ATLAS`, and click **OK**.

Manual alternative
------------------
Copy `3I_ATLAS_comets_dat_line.txt`, back up your existing `comets.dat` (`~/.local/share/kstars/comets.dat` on Linux, `~/Library/Application Support/kstars/comets.dat` on macOS, `%APPDATA%\kstars\comets.dat` on Windows), remove any older 3I/ATLAS entries, append the new line, and restart KStars.

macOS Gatekeeper
----------------
If macOS reports that it “cannot verify `MacOS_SEEREADME_KStars_Append_3I.command`”:
1. Open **System Settings → Privacy & Security**, set **Allow applications downloaded from** to *App Store & identified developers* if needed.
2. Run the `.command` file once; when the warning appears choose **Cancel** (or **Done**).
3. Back in **Privacy & Security**, click **Open Anyway** for the helper. Approve the prompt on the next launch.

Regenerate the comet line
-------------------------
When JPL publishes a newer solution, run `python tools/update_orbital_elements.py` from the repo root. That script refreshes the helper payload and the manual snippet before you rebuild a download zip.
