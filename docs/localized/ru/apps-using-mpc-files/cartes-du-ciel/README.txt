3I/ATLAS — быстрый импорт в Cartes du Ciel (SkyCharts)
=====================================================

Cartes du Ciel читает стандартные кометные элементы MPC. Используйте однострочный файл (`../import-pack/3I-ATLAS/templates/stellarium/3I_ATLAS_mpc_elements.txt`) или копию в этой папке.

### Вариант A — импорт через GUI
1. Запустите Cartes du Ciel.
2. Откройте **Setup → Solar system** (или `Ctrl+F3`).
3. На вкладке **Comets** нажмите **Update** (или **Import from MPC file**).
4. Выберите **File on disk** и укажите `3I_ATLAS_mpc_1line.txt`.
5. После импорта отметьте **3I/ATLAS** в списке и нажмите **OK**.

### Вариант B — ручное редактирование
1. Закройте Cartes du Ciel.
2. Сделайте резервную копию `comet.dat`:
   - Windows: `%LOCALAPPDATA%\Skychart\cat\comet.dat`
   - Linux: `~/.skychart/cat/comet.dat`
   - macOS: `~/Library/Application Support/skychart.cat/comet.dat`
3. Добавьте одну строку из `3I_ATLAS_mpc_1line.txt` в `comet.dat`.
4. Перезапустите программу и включите **3I/ATLAS** в списке комет.

Строка основана на решении JPL SBDB №27 (2025-10-10). Повторите импорт, когда появится новая орбитальная модель.
