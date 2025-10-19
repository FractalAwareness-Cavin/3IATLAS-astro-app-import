3I/ATLAS ΓΙΑ SOLAR FIRE (WINDOWS)
=================================

Το Solar Fire δεν εισάγει προϋπολογισμένες επιμηρίδες για νέα σώματα· διαβάζει τα στοιχεία τροχιάς από το `extras.dat`. Ο παρών φάκελος διατηρεί την εγγραφή του 3I/ATLAS σύμφωνη με τη λύση 27 του JPL SBDB.

Δοκιμασμένο σε
-------------
- Solar Fire 9: `Documents\Solar Fire 9 User Files\Points & Colors\extras.dat`
- Solar Fire 10: `Documents\Solar Fire User Files\Points & Colors\extras.dat`
- Solar Fire 11: `Documents\Solar Fire User Files\Points & Colors\extras.dat`

Περιεχόμενα
-----------
- `extras.dat`: έτοιμο μπλοκ `[3I_ATLAS]` (δείτε παρακάτω) με σχόλια για χειροκίνητες συγχωνεύσεις.
- `geocentric_daily_solarfire.txt` και παρόμοια αρχεία: προαιρετικοί πίνακες αναφοράς για ελέγχους εκτός Solar Fire.

Παράδειγμα μπλοκ
----------------
Επικολλήστε το παρακάτω στο `extras.dat` ή αφήστε το helper να το συγχωνεύσει αυτόματα:

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
; Το Solar Fire αγνοεί τον ημιάξονα όταν υπάρχει Tp για κομήτες.
; Το αντικείμενο είναι υπερβολικό (e>1). Ελέγξτε τη συμβατότητα με την έκδοσή σας.
```

Βήματα εγκατάστασης
-------------------
1. Κλείστε το Solar Fire.
2. Εκτελέστε τα βοηθητικά scripts (`tools/solarfire/SF_Merge_3I-DRYRUN.bat`, μετά `tools/solarfire/SF_Merge_3I-APPLY.bat`) **ή** κρατήστε αντίγραφο ασφαλείας του τρέχοντος `extras.dat`.
3. Ανοίξτε τη διαδρομή που αντιστοιχεί στην έκδοσή σας (βλ. παραπάνω) και προσθέστε το μπλοκ, διατηρώντας τυχόν άλλα custom bodies.
4. Επανεκκινήστε το Solar Fire, ανοίξτε **File → File Types…**, και βεβαιωθείτε ότι το **Extra Bodies** δείχνει στο ενημερωμένο αρχείο.
5. Στον διάλογο επιλογής σημείων, ενεργοποιήστε το `3I/ATLAS` κάτω από **Extra Bodies / Other Bodies**.

Mini-FAQ
--------
- **Το 3I/ATLAS δεν εμφανίζεται μετά τη συγχώνευση.** Βεβαιωθείτε ότι επεξεργαστήκατε τον σωστό φάκελο `extras.dat` (το Solar Fire διατηρεί ξεχωριστούς φακέλους ανά major έκδοση) και ότι το σώμα είναι ενεργό από το **Extra Bodies**.
- **Το script αναφέρει «access denied».** Κλείστε το Solar Fire πριν τρέξετε το APPLY· δεν μπορεί να αντικαταστήσει ανοιχτό `extras.dat`.
- **Χρειάζομαι νεότερα στοιχεία.** Εκτελέστε `python tools/update_orbital_elements.py` στη ρίζα του αποθετηρίου και ξανατρέξτε το helper για να αντικαταστήσετε το μπλοκ με την πιο πρόσφατη λύση SBDB.
