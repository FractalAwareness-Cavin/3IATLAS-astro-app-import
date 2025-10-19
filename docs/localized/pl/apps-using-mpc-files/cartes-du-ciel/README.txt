3I/ATLAS — szybki import w Cartes du Ciel (SkyCharts)
=====================================================

Cartes du Ciel obsługuje standardowe elementy MPC. Skorzystaj z dostarczonej linii (`../import-pack/3I-ATLAS/templates/stellarium/3I_ATLAS_mpc_elements.txt`) lub kopii w tym katalogu.

### Opcja A — import z GUI
1. Uruchom Cartes du Ciel.
2. Otwórz **Setup → Solar system** (lub `Ctrl+F3`).
3. W zakładce **Comets** kliknij **Update** (lub **Import from MPC file**).
4. Wybierz **File on disk** i wskaż `3I_ATLAS_mpc_1line.txt`.
5. Po imporcie zaznacz **3I/ATLAS** i kliknij **OK**.

### Opcja B — edycja ręczna
1. Zamknij Cartes du Ciel.
2. Zrób kopię `comet.dat`:
   - Windows: `%LOCALAPPDATA%\Skychart\cat\comet.dat`
   - Linux: `~/.skychart/cat/comet.dat`
   - macOS: `~/Library/Application Support/skychart.cat/comet.dat`
3. Dodaj linię z `3I_ATLAS_mpc_1line.txt` do `comet.dat`.
4. Uruchom aplikację ponownie i aktywuj **3I/ATLAS** na liście komet.

Linia bazuje na rozwiązaniu 27 JPL SBDB (2025-10-10). Ponownie zaimportuj dane, gdy pojawi się nowe rozwiązanie.
