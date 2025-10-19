3I/ATLAS — Solar Fire Merge Helper (Windows)
===========================================

Solar Fire reads user-defined bodies from `extras.dat`. The files here back up your existing list, remove any previous `[3I_ATLAS]` block, and append the latest orbital elements (JPL SBDB solution 27).

Files
-----
- `extras.dat` — ready-to-merge `[3I_ATLAS]` block.
- `tools/SF_Merge_3I-DRYRUN.bat` — Windows preview helper.
- `tools/SF_Merge_3I-APPLY.bat` — Windows apply helper.
- `tools/SF_Merge_3I.ps1` — PowerShell backend used by both batch files.

Steps
-----
1. Run `tools/SF_Merge_3I-DRYRUN.bat` to review the block.
2. Run `tools/SF_Merge_3I-APPLY.bat` to merge the block (a timestamped backup is saved automatically).
3. Restart Solar Fire and enable `3I/ATLAS` via **File → File Types… → Extra Bodies**.

Manual merge
-----------
If you prefer editing by hand, copy the `[3I_ATLAS]` section from `extras.dat` into your `Documents\Solar Fire User Files\Points & Colors\extras.dat`, preserving all other entries.
