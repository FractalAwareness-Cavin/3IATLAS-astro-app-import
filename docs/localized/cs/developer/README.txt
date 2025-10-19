VÝVOJÁŘSKÁ SADA NÁSTROJŮ
=======================

Tento adresář obsahuje vše potřebné k úplnému znovuvytvoření balíčku
efemerid.

Obsah
-----
- `raw/` – JSON odpovědi získané z API NASA/JPL Horizons.
- `scripts/generate_ephemeris.py` – Python skript, který znovu sestaví CSV,
  textové soubory pro Solar Fire, výstup MPC a souhrny vstupů do znamení.
- `scripts/build_swisseph.sh` – pomocník převádějící tabulky CSV na binárky
  Swiss Ephemeris `.se1` (vyžaduje `mksweph`).
- `vendor/` – přibalený modul `pyswisseph`, aby siderické výstupy fungovaly
  bez další instalace.

Regenerace
----------
```
cd developer/scripts
python3 generate_ephemeris.py
```
Skript znovu dotáže Horizons (vyžaduje internet) a aktualizuje složky
v kořeni repozitáře.

Binárky Swiss Ephemeris
-----------------------
Máte-li proprietární nástroj `mksweph`:
```
cd developer/scripts
bash build_swisseph.sh
```
Soubory `.se1` se uloží do `../swisseph/` pro distribuci.

Skript si upravte dle potřeby – změňte kadenci, souřadnicové systémy
nebo centrální tělesa; surové JSONy zajišťují zpětnou dohledatelnost k Horizons.

Podrobnější pokyny, včetně aktualizátoru SBDB a kontrolních skriptů,
najdete v `scripts/README.md`.
