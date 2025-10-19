3I/ATLAS — Solar Fire Merge Helper (Windows)
===========================================

Solar Fire stores custom bodies in `extras.dat`. These helpers back up your current file, remove any prior `[3I_ATLAS]` block, and append the refreshed elements from **JPL SBDB solution 27 (2025-10-10)**. The same scripts live in the repository under `tools/solarfire/`.

Files
-----
- `extras.dat` — standalone `[3I_ATLAS]` block if you prefer a manual merge.
- `tools/SF_Merge_3I-DRYRUN.bat` — preview helper; wraps the PowerShell backend.
- `tools/SF_Merge_3I-APPLY.bat` — apply helper; writes the block after backing up your file.
- `tools/SF_Merge_3I.ps1` — PowerShell backend used by both batch files (run directly if you prefer PowerShell).

Recommended workflow
--------------------
1. Quit Solar Fire so `extras.dat` is not locked.
2. Run `tools/SF_Merge_3I-DRYRUN.bat` to confirm the target path and review the block that will be merged.
3. Run `tools/SF_Merge_3I-APPLY.bat` (or invoke `tools/SF_Merge_3I.ps1 -Apply`) to append the block. The helper creates a timestamped backup before writing.
4. Relaunch Solar Fire, open **File → File Types… → Extra Bodies**, and ensure the path points at the updated file. In your chart, tick `3I/ATLAS` under **Extra Bodies / Other Bodies**.

Manual merge
------------
If you want to edit by hand, copy the `[3I_ATLAS]` section from the bundled `extras.dat` into the user file for your version (for example `Documents\Solar Fire User Files\Points & Colors\extras.dat` or `Documents\Solar Fire 9 User Files\Points & Colors\extras.dat`). Keep existing entries intact and restart Solar Fire afterwards.
