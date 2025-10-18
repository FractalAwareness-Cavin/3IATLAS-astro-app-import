# App workflows for 3I/ATLAS

## Stellarium (Windows/macOS/Linux)

**Accepts:** MPC 1‑line comet elements  
**Method:** *Configuration → Plugins → Solar System Editor (enable, restart) → Configure → Solar System → Import elements in MPC format → File → Select your file → Add object(s).*  
**Files:** `templates/stellarium/3I_ATLAS_mpc_elements.txt`  
**Tip:** If the online lists don’t include 3I yet, use the **File** option.

## KStars (Windows/macOS/Linux)

**Accepts:** `comets.dat` line (KStars format)  
**Methods:**

* *Data → Download New Data…* (when upstream includes 3I).  
* **Manual:** append/replace your local `comets.dat` with the generated line (backup first).

**User file locations (typical):**

* Linux: `~/.local/share/kstars/comets.dat`  
* Windows: `%LOCALAPPDATA%\kstars\comets.dat`  
* macOS: `~/Library/Application Support/kstars/comets.dat`

## SkySafari / SkyVoyager (iOS/Android)

**Accepts:** No manual import  
**Method:** *Settings → Solar System → Update Orbit Data* (Plus/Pro tiers).  
Keep `templates/skysafari/3I_ATLAS_mpc_1line.txt` for reference only.

## Solar Fire (Windows)

**Accepts:** `extras.dat` (Other Bodies)  
**Method (summary):**

1. Backup: usually `Documents\Solar Fire User Files\Points & Colors\extras.dat`.  
2. Inspect via **File Manager → Extra Bodies File…** (to see field order in your version).  
3. Edit `extras.dat` *only after confirming field order*.  
4. In **Displayed Points…**, enable *Other Bodies* and tick your object. Restart Solar Fire if needed.

## Astro Gold (macOS / iOS)

**Accepts:** Built‑ins only; no user import for moving bodies  
**Method:**

* macOS: *Astro Gold → Preferences → Displayed Points → Add Extra Points*  
* iOS: *Settings → Chart Points*  
  “Custom Points” are **fixed**; not orbiting bodies.

## TimePassages (macOS / Windows)

**Accepts:** Built‑ins only; “Custom Points” are fixed  
**Method:**

* macOS: *TimePassages → Preferences → Edit Chart Points*  
* Windows: *Edit → Chart Points*  
  Also toggle *Display → Chart Points* to show them.
