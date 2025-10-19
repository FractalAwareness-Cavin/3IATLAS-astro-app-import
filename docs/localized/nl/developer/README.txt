DEVELOPER-TOOLKIT
=================

Deze map bevat alles wat nodig is om het ephemeridenpakket
vanaf nul opnieuw op te bouwen.

Inhoud
------
- `raw/` – JSON-responses opgehaald via de NASA/JPL Horizons-API.
- `scripts/generate_ephemeris.py` – Python-script dat de CSV-bestanden,
  Solar Fire-tekstbestanden, MPC-uitvoer en samenvattingen van teken-ingressen opnieuw genereert.
- `scripts/build_swisseph.sh` – helper die CSV-tabellen omzet in Swiss-Ephemeris-`.se1`-binaries
  (vereist `mksweph`).
- `vendor/` – meegeleverde `pyswisseph`-module zodat siderische uitgaven werken
  zonder extra installaties.

Opnieuw genereren
-----------------
```
cd developer/scripts
python3 generate_ephemeris.py
```
Het script haalt Horizons opnieuw op (internet vereist) en werkt de
mappen in de hoofdmap van de repository bij.

Swiss-Ephemeris-binaries
------------------------
Wanneer je de proprietaire tool `mksweph` hebt:
```
cd developer/scripts
bash build_swisseph.sh
```
De `.se1`-bestanden worden weggeschreven naar `../swisseph/` voor distributie.

Pas het script gerust aan voor andere cadence, coördinatenstelsels of centrale lichamen;
de ruwe JSON's houden de herkomst naar Horizons bij.

Uitgebreide gebruiksinformatie, waaronder de SBDB-updater en verificatiehulpen,
vind je in `scripts/README.md`.
