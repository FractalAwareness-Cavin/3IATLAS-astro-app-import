3I/ATLAS ДЛЯ SOLAR FIRE (WINDOWS)
=================================

Solar Fire не импортирует заранее рассчитанные эфемериды новых тел; программа считывает орбитальные элементы из `extras.dat`. Эта папка держит запись 3I/ATLAS в соответствии с решением JPL SBDB №27.

Проверено на версиях
--------------------
- Solar Fire 9: `Documents\Solar Fire 9 User Files\Points & Colors\extras.dat`
- Solar Fire 10: `Documents\Solar Fire User Files\Points & Colors\extras.dat`
- Solar Fire 11: `Documents\Solar Fire User Files\Points & Colors\extras.dat`

Содержимое
----------
- `extras.dat`: готовый блок `[3I_ATLAS]` (см. ниже) и комментарии для ручного объединения.
- `geocentric_daily_solarfire.txt` и аналогичные файлы: дополнительные таблицы для проверки позиций вне Solar Fire.

Пример блока
------------
Вставьте этот блок в существующий `extras.dat` или позвольте помощнику объединить его автоматически:

```
[3I_ATLAS]
Name = 3I/ATLAS
Number = 0
EpochJD = 2460884.5
PerihelionDistance_AU = 1.356065571
Eccentricity = 6.137350157
Inclination_deg = 175.112857794
AscendingNode_deg = 322.152284965
ArgumentOfPerihelion_deg = 128.011608252
PerihelionTime_JD = 2460977.983535961
AbsoluteMagnitude = 12.3
SlopeParameter = 4.5
; Solar Fire игнорирует большую полуось, если для комет задан Tp.
; Объект гиперболический (e>1). Проверьте совместимость с вашей версией Solar Fire.
```

Установка
---------
1. Закройте Solar Fire.
2. Запустите вспомогательные скрипты (`tools/solarfire/SF_Merge_3I-DRYRUN.bat`, затем `tools/solarfire/SF_Merge_3I-APPLY.bat`) **или** сделайте резервную копию текущего `extras.dat`.
3. Откройте путь, соответствующий вашей версии (см. выше), и добавьте блок. Сохраните остальные пользовательские тела.
4. Перезапустите Solar Fire, откройте **File → File Types…** и убедитесь, что **Extra Bodies** указывает на обновленный файл.
5. В диалоге выбора точек отметьте `3I/ATLAS` в разделе **Extra Bodies / Other Bodies**.

Мини-FAQ
--------
- **3I/ATLAS не появляется после слияния.** Убедитесь, что редактировали нужный каталог `extras.dat` (у Solar Fire отдельные пользовательские папки для каждой версии) и что тело включено в **Extra Bodies**.
- **Скрипт сообщает "access denied".** Закройте Solar Fire перед запуском APPLY: открытый `extras.dat` нельзя перезаписать.
- **Нужны более новые элементы.** Выполните `python tools/update_orbital_elements.py` из корня репозитория, затем снова запустите помощник, чтобы заменить блок свежей SBDB-версией.
