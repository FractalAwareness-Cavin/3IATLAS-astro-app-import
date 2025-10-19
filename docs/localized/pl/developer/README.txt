NARZĘDZIA DLA DEWELOPERÓW
========================

Ten katalog zawiera wszystko, co potrzebne, by odtworzyć pakiet efemeryd
od podstaw.

Zawartość
---------
- `raw/` – odpowiedzi JSON pobrane z API NASA/JPL Horizons.
- `scripts/generate_ephemeris.py` – skrypt Pythona, który odbudowuje pliki CSV,
  teksty dla Solar Fire, wyjście MPC oraz podsumowania wejść do znaków.
- `scripts/build_swisseph.sh` – pomocnik zamieniający tabele CSV na binaria
  Swiss Ephemeris `.se1` (wymaga `mksweph`).
- `vendor/` – dołączony moduł `pyswisseph`, aby wyjścia gwiazdowe działały
  bez dodatkowych instalacji.

Odtwarzanie
-----------
```
cd developer/scripts
python3 generate_ephemeris.py
```
Skrypt ponownie odpytuje Horizons (wymaga internetu) i aktualizuje
foldery w katalogu głównym repozytorium.

Binaria Swiss Ephemeris
-----------------------
Jeśli masz dostęp do narzędzia `mksweph`:
```
cd developer/scripts
bash build_swisseph.sh
```
Pliki `.se1` trafią do `../swisseph/` w celu dystrybucji.

Dostosuj skrypt według potrzeb – zmień kadencję, układy współrzędnych
czy ciała centralne; surowe JSON-y zachowują ścieżkę do Horizons.

Szczegółowe uwagi, w tym aktualizator SBDB i narzędzia weryfikacyjne,
znajdziesz w `scripts/README.md`.
