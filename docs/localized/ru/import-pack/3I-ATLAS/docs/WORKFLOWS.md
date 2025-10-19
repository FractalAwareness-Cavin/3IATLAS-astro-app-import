# Рабочие процессы приложений для 3I/ATLAS

Все значения в этом пакете основаны на решении JPL SBDB №27 (2025-10-10).
Обновляйте файлы с помощью конвертера, когда выходит более свежая орбитальная модель.

## Stellarium (Windows/macOS/Linux)

**Принимает:** кометные элементы MPC в одну строку  
**Шаги:**
1. **Configuration → Plugins → Solar System Editor** → отметьте **Load at startup** (при необходимости перезапустите).  
2. **Solar System Editor → Configure → Solar System → Import elements in MPC format → File**.  
3. Выберите `templates/stellarium/3I_ATLAS_mpc_elements.txt`.  
4. Нажмите **Add object(s)** и найдите **3I/ATLAS**.

## KStars (Windows/macOS/Linux)

**Принимает:** строку `comets.dat`  
**Помощники:**
- Windows: `tools/kstars/KStars_Append_3I-DRYRUN.bat` (предпросмотр), затем `…-APPLY.bat`.  
- macOS: дважды щелкните `tools/kstars/KStars_Append_3I.command`.  
- Linux: выполните `bash tools/kstars/KStars_Append_3I.sh`.  
Все помощники делают резервную копию перед добавлением.

Вручную:
1. Создайте резервную копию `comets.dat` (`~/.local/share/kstars/comets.dat` в Linux, `%LOCALAPPDATA%\kstars\comets.dat` в Windows, `~/Library/Application Support/kstars/comets.dat` в macOS).  
2. Добавьте строку из `templates/kstars/3I_ATLAS_comets_dat_snippet.txt`.  
3. Перезапустите KStars и найдите **3I/ATLAS**.

## SkySafari / SkyVoyager (iOS/Android)

**Принимает:** нет ручного импорта  
Используйте *Settings → Solar System → Update Orbit Data* (уровни Plus/Pro). Храните
`templates/skysafari/3I_ATLAS_mpc_1line.txt` только для справки.

## Cartes du Ciel (SkyCharts)

**Принимает:** файлы элементов MPC  
Следуйте инструкциям в `apps-using-mpc-files/cartes-du-ciel/README.txt`
(импорт через GUI или ручное добавление в `comet.dat`).

## WinStars 3

**Принимает:** файлы элементов MPC  
См. `apps-using-mpc-files/winstars/README.txt` для быстрых шагов импорта.

## Solar Fire (Windows)

**Принимает:** орбитальные элементы `extras.dat` (Other Bodies)  
**Помощники:**
- Windows: `tools/solarfire/SF_Merge_3I-DRYRUN.bat` (предпросмотр), затем `…-APPLY.bat` для автоматического объединения `[3I_ATLAS]`.  
Оба скрипта создают резервную копию `extras.dat` с отметкой времени.

Вручную:
1. Закройте Solar Fire и сохраните `Documents\Solar Fire User Files\Userdata\extras.dat`.  
2. Скопируйте или объедините блок `[3I_ATLAS]` из `templates/solar_fire/3I_ATLAS_extras_dat_PLACEHOLDER.txt`.  
3. Перезапустите программу и включите **3I/ATLAS** в разделе **Extra Bodies**.

## Приложения без импорта

Astro Gold (macOS/iOS/iPadOS) и TimePassages Desktop (macOS/Windows) предоставляют
только предустановленные точки от разработчика и не принимают пользовательские эфемериды
движущихся тел. См. каталог `Time-Passages-Astro-Gold/` для обходных решений
(фиксированные точки) и контактной информации производителя.
