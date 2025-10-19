3I/ATLAS PRO SOLAR FIRE (WINDOWS)
=================================

Solar Fire neimportuje předpočítané efemeridy nových těles; čte orbitální prvky ze souboru `extras.dat`. Tato složka udržuje záznam 3I/ATLAS v souladu s řešením JPL SBDB 27.

Testováno na
------------
- Solar Fire 9: `Documents\Solar Fire 9 User Files\Points & Colors\extras.dat`
- Solar Fire 10: `Documents\Solar Fire User Files\Points & Colors\extras.dat`
- Solar Fire 11: `Documents\Solar Fire User Files\Points & Colors\extras.dat`

Obsah
-----
- `extras.dat`: připravený blok `[3I_ATLAS]` (viz níže) a komentáře pro ruční sloučení.
- `geocentric_daily_solarfire.txt` a podobné soubory: volitelné referenční tabulky pro kontrolu pozic mimo Solar Fire.

Ukázkový blok
-------------
Vložte tento blok do stávajícího `extras.dat` nebo využijte helper, aby jej sloučil automaticky:

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
; Solar Fire ignoruje hlavní poloosu, pokud je pro komety zadáno Tp.
; Objekt je hyperbolický (e>1). Ověřte, že je kompatibilní s vaší verzí Solar Fire.
```

Instalace
---------
1. Ukončete Solar Fire.
2. Spusťte pomocné skripty (`tools/solarfire/SF_Merge_3I-DRYRUN.bat`, poté `tools/solarfire/SF_Merge_3I-APPLY.bat`) **nebo** zálohujte aktuální `extras.dat`.
3. Otevřete cestu pro vaši verzi (viz výše) a blok přidejte; ostatní vlastní tělesa ponechejte.
4. Restartujte Solar Fire, otevřete **File → File Types…** a zkontrolujte, že **Extra Bodies** ukazuje na aktualizovaný soubor.
5. V dialogu výběru bodů zaškrtněte `3I/ATLAS` v sekci **Extra Bodies / Other Bodies**.

Mini-FAQ
--------
- **3I/ATLAS se po sloučení nezobrazuje.** Ověřte, že jste upravili správnou složku `extras.dat` (Solar Fire má oddělené uživatelské složky pro každou hlavní verzi) a že je těleso zapnuté v **Extra Bodies**.
- **Helper hlásí "access denied".** Před spuštěním APPLY scriptu zavřete Solar Fire; otevřený `extras.dat` nelze přepsat.
- **Potřebuji novější prvky.** Spusťte `python tools/update_orbital_elements.py` v kořeni repozitáře a helper poté blok nahradí nejnovějším řešením SBDB.
