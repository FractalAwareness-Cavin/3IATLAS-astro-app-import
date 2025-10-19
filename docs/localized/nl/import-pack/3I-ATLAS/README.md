# 3I/ATLAS-importpakket

Snelstartsjablonen, hulpscripts en documentatie om
**3I/ATLAS (C/2025 N1)** in MPC-compatibele astronomiesoftware te brengen.

## Inhoud
- `docs/INSTALL_3I-ATLAS.md` — overzicht, aandachtspunten en quickstart (huidige versie v0.2).
- `docs/WORKFLOWS.md` — stap-voor-stap-instructies voor Stellarium, KStars,
  SkySafari, Solar Fire en notities over niet-ondersteunde apps.
- `templates/` — kant-en-klare MPC-eenregelige elementen, KStars-`comets.dat`-regel
  en Solar Fire-blok `[3I_ATLAS]` (allemaal gebaseerd op JPL SBDB-oplossing 27).
- `tools/3i_elements_to_formats.py` — optionele converter: plak een nieuw
  MPC-eenregelig element en de sjablonen worden automatisch herschreven.
- `tools/kstars/` — Windows/macOS/Linux-hulpen die de KStars-regel back-uppen
  en toevoegen.
- `tools/solarfire/` — Windows-hulpen die het `extras.dat`-blok voor 3I/ATLAS
  veiligstellen en samenvoegen.

## Gebruiksinstanties
- Stellarium: importeer de meegeleverde regel via **Solar System Editor → Import elements in MPC format → File**.
- KStars: voer het script voor je besturingssysteem uit of voeg de meegeleverde `comets.dat`-regel handmatig toe.
- SkySafari: gebruik **Settings → Solar System → Update Orbit Data** (Plus/Pro-niveaus).  
- Solar Fire: voeg het `[3I_ATLAS]`-blok samen in `extras.dat` (maak eerst een back-up).  
- Astro Gold / TimePassages: momenteel geen import van bewegende objecten; zie de repository-notities voor vaste aangepaste punten.

Werk de sjablonen bij met het conversiescript zodra er een nieuwe orbitale oplossing beschikbaar is.
