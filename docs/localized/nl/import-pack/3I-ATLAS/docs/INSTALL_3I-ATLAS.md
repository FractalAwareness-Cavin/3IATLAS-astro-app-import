# 3I/ATLAS — importpakket (v0.2)

Gebruik dit pakket wanneer je **MPC-baanparameters klaar voor gebruik** nodig hebt
of een platformspecifieke helper om 3I/ATLAS in astronomiesoftware te laden.
Alles werkt offline en is gebaseerd op JPL SBDB-oplossing 27 (2025-10-10).

> **Kort gezegd**
> - **Stellarium** → importeer de meegeleverde regel via *Solar System Editor → Import elements in MPC format*.
> - **KStars** → draai de helper zonder installatie (Windows/macOS/Linux) of plak de meegeleverde `comets.dat`-regel.
> - **SkySafari** → gebruik *Settings → Solar System → Update Orbit Data* (Plus/Pro) en bewaar de eenregelige MPC voor referentie.
> - **Solar Fire** → voeg het `[3I_ATLAS]`-blok samen met `extras.dat` (maak eerst een back-up); hulpscripts zijn inbegrepen.
> - **Astro Gold / TimePassages** → ondersteunen momenteel geen import van bewegende objecten; zie het hoofdrepo voor oplossingen met vaste punten.

## Inhoud

- `templates/stellarium/3I_ATLAS_mpc_elements.txt` — MPC-eenregelige elementen voor 3I/ATLAS.
- `templates/skysafari/3I_ATLAS_mpc_1line.txt` — dezelfde regel voor archief/referentie.
- `templates/kstars/3I_ATLAS_comets_dat_snippet.txt` — regel die rechtstreeks aan `comets.dat` kan worden toegevoegd (ook bruikbaar voor Cartes du Ciel / WinStars).
- `templates/solar_fire/3I_ATLAS_extras_dat_PLACEHOLDER.txt` — `[3I_ATLAS]`-blok voor `extras.dat` in Solar Fire.
- `tools/3i_elements_to_formats.py` — optionele converter voor een nieuw MPC-eenregelig element.
- `tools/update_orbital_elements.py` — haalt de nieuwste JPL SBDB-oplossing op en overschrijft alle sjablonen.
- `docs/WORKFLOWS.md` — stap-voor-stap-instructies voor Stellarium, KStars, Cartes du Ciel, WinStars, SkySafari, Solar Fire.

## Snel starten

Al up-to-date? Ga direct naar `docs/WORKFLOWS.md`. Wanneer JPL een nieuwe baan publiceert, werk je bij met:
```bash
python tools/update_orbital_elements.py --dry-run  # bekijk de nieuwste elementen
python tools/update_orbital_elements.py            # overschrijft de sjablonen
```
Als je bestanden liever handmatig vervangt, genereert `tools/3i_elements_to_formats.py`
de fragmenten voor Stellarium/KStars/Solar Fire op basis van elke MPC-regel.

## Aandachtspunten

- **Solar Fire `extras.dat`**: de volgorde van velden verschilt per versie. Raadpleeg
het ingebouwde hulponderwerp "Format of the Orbital Elements File" bij handmatige bewerking en maak altijd eerst een back-up.
- **SkySafari**: er is geen handmatige bestandsimport; gebruik *Update Orbit Data*.
- **Astro Gold / TimePassages**: bieden op dit moment geen importworkflow voor bewegende objecten. Gebruik hun vaste aangepaste punten of vraag ondersteuning aan de leverancier.
- **Validatie**: voer `tools/verify_ephemeris.py` uit om geselecteerde regels uit
`apps-using-mpc-files/geocentric_mpc_ephemeris.txt` te vergelijken met live Horizons-data als je de efemeriden wilt controleren.
