3I/ATLAS VOOR SOLAR FIRE (WINDOWS)
==================================

Solar Fire importeert geen vooraf berekende efemeriden voor nieuwe objecten; het leest orbitalelementen uit `extras.dat`. Deze map houdt de 3I/ATLAS-invoer in lijn met JPL SBDB-oplossing 27.

Getest op
---------
- Solar Fire 9: `Documents\Solar Fire 9 User Files\Points & Colors\extras.dat`
- Solar Fire 10: `Documents\Solar Fire User Files\Points & Colors\extras.dat`
- Solar Fire 11: `Documents\Solar Fire User Files\Points & Colors\extras.dat`

Inhoud
------
- `extras.dat`: kant-en-klare `[3I_ATLAS]`-sectie (zie hieronder) plus toelichting voor handmatige merges.
- `geocentric_daily_solarfire.txt` en vergelijkbare bestanden: optionele referentietabellen om posities buiten Solar Fire te controleren.

Voorbeeldblok
-------------
Plak dit blok in je bestaande `extras.dat` of laat de helper het automatisch samenvoegen:

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
; Solar Fire negeert de halve hoofdas als Tp voor kometen aanwezig is.
; Dit object is hyperbolisch (e>1). Controleer de compatibiliteit met jouw versie.
```

Installatie
-----------
1. Sluit Solar Fire.
2. Voer de hulpscripts uit (`tools/solarfire/SF_Merge_3I-DRYRUN.bat`, daarna `tools/solarfire/SF_Merge_3I-APPLY.bat`) **of** maak een back-up van je huidige `extras.dat`.
3. Open het pad dat bij jouw versie hoort (zie boven) en voeg het blok toe. Laat andere aangepaste objecten staan.
4. Start Solar Fire opnieuw, open **File → File Types…** en zorg dat **Extra Bodies** naar het bijgewerkte bestand verwijst.
5. Vink in het selectievenster `3I/ATLAS` aan onder **Extra Bodies / Other Bodies**.

Mini-FAQ
--------
- **3I/ATLAS verschijnt niet.** Controleer of je de juiste `extras.dat`-map hebt bewerkt (Solar Fire gebruikt aparte gebruikersmappen per hoofdversie) en of het object in **Extra Bodies** is geactiveerd.
- **Helper geeft "access denied".** Sluit Solar Fire voordat je het APPLY-script draait; een geopend `extras.dat` kan niet worden overschreven.
- **Nieuwere elementen nodig.** Voer `python tools/update_orbital_elements.py` uit in de hoofdmap van het repo en laat daarna de helper opnieuw lopen voor de laatste SBDB-oplossing.
