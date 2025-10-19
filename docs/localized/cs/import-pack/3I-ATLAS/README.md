# Importní balíček 3I/ATLAS

Šablony pro rychlý start, pomocné skripty a dokumentace pro začlenění
**3I/ATLAS (C/2025 N1)** do astronomického softwaru kompatibilního s MPC.

## Obsah
- `docs/INSTALL_3I-ATLAS.md` — přehled, upozornění a rychlý start (aktuálně verze 0.2).
- `docs/WORKFLOWS.md` — podrobný postup pro Stellarium, KStars,
  SkySafari, Solar Fire a poznámky k aplikacím bez podpory.
- `templates/` — připravené MPC jednořádkové elementy, řádek `comets.dat` pro KStars
  a blok `[3I_ATLAS]` pro Solar Fire (vše vychází z řešení JPL SBDB 27).
- `tools/3i_elements_to_formats.py` — volitelný konvertor: vložte novější
  MPC jednořádek a šablony se přepíší automaticky.
- `tools/kstars/` — pomocníci pro Windows/macOS/Linux, kteří zálohují
  a přidají řádek pro KStars.
- `tools/solarfire/` — pomocníci pro Windows, kteří zálohují a sloučí blok
  `extras.dat` pro 3I/ATLAS.

## Rychlý přehled použití
- Stellarium: importujte dodaný řádek přes **Solar System Editor → Import elements in MPC format → File**.
- KStars: spusťte skript pro svůj operační systém nebo ručně přidejte dodaný řádek do `comets.dat`.
- SkySafari: použijte **Settings → Solar System → Update Orbit Data** (úrovně Plus/Pro).  
- Solar Fire: sloučte blok `[3I_ATLAS]` do `extras.dat` (nejdříve proveďte zálohu).  
- Astro Gold / TimePassages: momentálně nemají import pohyblivých těles; pokud potřebujete pevné vlastní body, nahlédněte do poznámek v repozitáři.

Šablony aktualizujte konverzním skriptem vždy, když vyjde nové orbitální řešení.
