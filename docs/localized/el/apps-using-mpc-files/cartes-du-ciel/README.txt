3I/ATLAS — Γρήγορη εισαγωγή σε Cartes du Ciel (SkyCharts)
========================================================

Το Cartes du Ciel διαβάζει τυπικά στοιχεία κομητών MPC. Χρησιμοποιήστε τη γραμμή που παρέχεται (`../import-pack/3I-ATLAS/templates/stellarium/3I_ATLAS_mpc_elements.txt`) ή το αντίγραφο αυτού του φακέλου.

### Επιλογή Α — εισαγωγή μέσω GUI
1. Εκκινήστε το Cartes du Ciel.
2. Ανοίξτε **Setup → Solar system** (ή `Ctrl+F3`).
3. Στην καρτέλα **Comets** πατήστε **Update** (ή **Import from MPC file**).
4. Επιλέξτε **File on disk** και εντοπίστε `3I_ATLAS_mpc_1line.txt`.
5. Μετά την εισαγωγή, τικάρετε **3I/ATLAS** και πατήστε **OK**.

### Επιλογή Β — χειροκίνητη επεξεργασία
1. Κλείστε το Cartes du Ciel.
2. Κρατήστε αντίγραφο ασφαλείας του `comet.dat`:
   - Windows: `%LOCALAPPDATA%\Skychart\cat\comet.dat`
   - Linux: `~/.skychart/cat/comet.dat`
   - macOS: `~/Library/Application Support/skychart.cat/comet.dat`
3. Προσθέστε τη μονή γραμμή από το `3I_ATLAS_mpc_1line.txt` στο `comet.dat`.
4. Ξεκινήστε ξανά και ενεργοποιήστε το **3I/ATLAS** στη λίστα κομητών.

Η γραμμή βασίζεται στη λύση 27 του JPL SBDB (2025-10-10). Εισάγετέ τη ξανά μόλις δημοσιευτεί νέα λύση.
