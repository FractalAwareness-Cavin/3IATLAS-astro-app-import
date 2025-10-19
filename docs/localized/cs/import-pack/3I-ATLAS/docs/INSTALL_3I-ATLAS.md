# 3I/ATLAS — importní balíček (v0.2)

Tento balíček použijte, když potřebujete **hotové orbitální elementy MPC**
nebo pomocníka pro konkrétní platformu, abyste dostali 3I/ATLAS do astronomického softwaru.
Vše funguje offline a vychází z řešení JPL SBDB 27 (2025-10-10).

> **Ve zkratce**
> - **Stellarium** → importujte dodanou řádku přes *Solar System Editor → Import elements in MPC format*.
> - **KStars** → spusťte pomocný program bez instalace (Windows/macOS/Linux) nebo vložte poskytnutý řádek `comets.dat`.
> - **SkySafari** → použijte *Settings → Solar System → Update Orbit Data* (Plus/Pro) a řádku MPC si ponechte jako referenci.
> - **Solar Fire** → slučte blok `[3I_ATLAS]` do `extras.dat` (nejdříve zálohujte); pomocné skripty jsou součástí.
> - **Astro Gold / TimePassages** → zatím neumí import pohyblivých těles; viz poznámky v hlavním repozitáři pro řešení s pevnými body.

## Co je uvnitř

- `templates/stellarium/3I_ATLAS_mpc_elements.txt` — MPC jednořádkové elementy pro 3I/ATLAS.
- `templates/skysafari/3I_ATLAS_mpc_1line.txt` — stejná řádka pro archiv/referenci.
- `templates/kstars/3I_ATLAS_comets_dat_snippet.txt` — řádek připravený k přidání do `comets.dat` (využívá i Cartes du Ciel / WinStars).
- `templates/solar_fire/3I_ATLAS_extras_dat_PLACEHOLDER.txt` — blok `[3I_ATLAS]` připravený pro `extras.dat` Solar Fire.
- `tools/3i_elements_to_formats.py` — volitelný konvertor, pokud vložíte novější MPC řádek.
- `tools/update_orbital_elements.py` — získá nejnovější řešení JPL SBDB a přepíše všechny šablony.
- `docs/WORKFLOWS.md` — postupy krok za krokem pro Stellarium, KStars, Cartes du Ciel, WinStars, SkySafari, Solar Fire.

## Rychlý start

Jste aktuální? Pokračujte rovnou do `docs/WORKFLOWS.md`. Kdykoli JPL zveřejní novou
orbtu, proveďte aktualizaci:
```bash
python tools/update_orbital_elements.py --dry-run  # náhled nejnovějších elementů
python tools/update_orbital_elements.py            # přepíše šablony
```
Pokud chcete soubory měnit ručně, `tools/3i_elements_to_formats.py`
vytvoří fragmenty pro Stellarium/KStars/Solar Fire z libovolného MPC řádku.

## Upozornění

- **Solar Fire `extras.dat`**: pořadí polí se může lišit podle verze. Při ručních úpravách
využijte vestavěnou nápovědu „Format of the Orbital Elements File“ a vždy si vytvořte zálohu.
- **SkySafari**: manuální import souborů neexistuje; spoléhejte na *Update Orbit Data*.
- **Astro Gold / TimePassages**: v době psaní neposkytují proces importu pohyblivých těles. Použijte jejich pevné vlastní body nebo kontaktujte dodavatele.
- **Ověření**: spusťte `tools/verify_ephemeris.py`, chcete-li porovnat vybrané řádky z
`apps-using-mpc-files/geocentric_mpc_ephemeris.txt` s daty Horizons v reálném čase a ověřit efemeridy.
