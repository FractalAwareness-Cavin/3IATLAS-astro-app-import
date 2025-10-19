3I/ATLAS – ΟΔΗΓΟΣ ΕΙΣΑΓΩΓΗΣ MPC
================================

Το `geocentric_mpc_ephemeris.txt` περιέχει ημερήσιες επιμηρίδες σε μορφή MPC (UT 0h, RA/Dec J2000, delta, r, επιμήκυνση, φάση). Χρησιμοποιήστε το όπου το λογισμικό σας δέχεται κλασικά δεδομένα κομητών 80 στηλών. Έτοιμα πακέτα θα βρείτε στα releases (δείτε το `README.md` στη ρίζα) ή στον φάκελο `apps-using-mpc-files/`.

Πακέτα release
--------------
- `Stellarium_quick-import.zip`: εισάγει το αρχείο μονής κομήτης μέσω του plugin Solar System Editor.
- `KStars_quick-append_Win-Mac-Linux.zip`: βοηθητικά dry-run/apply για το `comets.dat` σε κάθε πλατφόρμα.
- `3I-ATLAS_apps_using_mpc_files.zip`: περιλαμβάνει ολόκληρο τον φάκελο, μαζί με templates μίας γραμμής για Cartes du Ciel και WinStars.

Stellarium (Win/macOS/Linux)
----------------------------
1. Αποσυμπιέστε το `Stellarium_quick-import.zip` ή αντιγράψτε το `geocentric_mpc_ephemeris.txt` σε προσβάσιμο σημείο.
2. Στο Stellarium πατήστε `F2`, ανοίξτε **Plugins → Solar System Editor**, ενεργοποιήστε το **Load at startup** και πατήστε **Configure**. Επανεκκινήστε αν μόλις το ενεργοποιήσατε.
3. Μετά την επανεκκίνηση, ανοίξτε **Solar System Editor → Solar System** και επιλέξτε **Import orbital elements in MPC format**.
4. Πατήστε **Select file**, δείξτε στο `geocentric_mpc_ephemeris.txt` (ή στο single-line αρχείο), ορίστε **Object name** σε `3I/ATLAS` και αφήστε το **Object type** σε *Comet*.
5. Πατήστε **Add objects**, κλείστε τα παράθυρα και με `F3` ελέγξτε ότι το `3I/ATLAS` αναγνωρίζεται.

KStars (Win/macOS/Linux)
------------------------
1. Αποσυμπιέστε `KStars_quick-append_Win-Mac-Linux.zip` και τρέξτε το script για την πλατφόρμα σας (`*.bat`, `*.command`, `*.sh`, `*.ps1`). Ξεκινήστε με DRYRUN και αν όλα είναι σωστά τρέξτε APPLY για να προστεθεί στον `comets.dat`.
2. Εναλλακτικά χειροκίνητα: **Settings → Configure KStars → Solar System** (παλιότερες εκδόσεις **Data → Solar System Updates**). Στο **Comets** πατήστε **Import**, επιλέξτε `geocentric_mpc_ephemeris.txt` και επιβεβαιώστε.
3. Επανεκκινήστε το KStars αν ζητηθεί και αναζητήστε `3I/ATLAS` ή ελέγξτε τον Solar System viewer.

Cartes du Ciel / SkyCharts
--------------------------
1. Αντιγράψτε `apps-using-mpc-files/cartes-du-ciel/3I_ATLAS_mpc_1line.txt` (υπάρχει και στο release zip).
2. Εκκινήστε το Cartes du Ciel και ανοίξτε **Setup → Solar system** (`Ctrl+F3`).
3. Στην καρτέλα **Comets** επιλέξτε **Update → Import from MPC file**, διαλέξτε `3I_ATLAS_mpc_1line.txt` και επιβεβαιώστε.
4. Τσεκάρετε **3I/ATLAS** στη λίστα και πατήστε **OK**. Η κομήτη εμφανίζεται σε αναζητήσεις και χάρτες.
5. Θέλετε χειροκίνητη επεξεργασία; Προσθέστε τη γραμμή στο `comet.dat` (δείτε το README του φακέλου για διαδρομές).

WinStars 3 (Win/macOS/Linux)
----------------------------
1. Κρατήστε διαθέσιμο το `apps-using-mpc-files/winstars/3I_ATLAS_mpc_1line.txt` ή αποσυμπιέστε το MPC πακέτο.
2. Στο WinStars ανοίξτε **Preferences → Solar system → Import orbital elements** (ή **Add object**).
3. Επιλέξτε **MPC single line**, επικολλήστε το περιεχόμενο και αποθηκεύστε.
4. Ελέγξτε ότι το `3I/ATLAS` είναι ενεργό στη λίστα· αν χρειαστεί επανεκκινήστε για ανανέωση cache.

SkySafari / SkyVoyager Plus/Pro (iOS/Android/macOS)
---------------------------------------------------
1. Περάστε το αρχείο `3I_ATLAS_mpc_1line.txt` σε επεξεργαστή κειμένου που βλέπει η συσκευή.
2. Στο SkySafari ανοίξτε **Settings → Solar System → Solar System Data** και πατήστε **Import Comet Data** (ή **Update Orbit Data → Custom Comet/Asteroid** σε παλαιότερες εκδόσεις).
3. Επικολλήστε τη γραμμή MPC, βεβαιωθείτε ότι το όνομα είναι `3I/ATLAS` και επιβεβαιώστε.
4. Αναζητήστε `3I/ATLAS` και προσθέστε το σε λίστες παρατήρησης αν θέλετε.
5. Η εφαρμογή ενημερώνει περιοδικά τις ροές MPC· επαναλάβετε την εισαγωγή μετά από νέα λύση.

Λογισμικό συμβατό με MPC
------------------------
1. Αντιγράψτε `geocentric_mpc_ephemeris.txt` ή το single-line template που ταιριάζει στο πρόγραμμα.
2. Χρησιμοποιήστε τη λειτουργία import κομητών/αστεροειδών, επιλέξτε το αρχείο και ονομάστε το αντικείμενο `3I/ATLAS`.
3. Επανεκκινήστε αν η εφαρμογή κάνει cache τα δεδομένα και βεβαιωθείτε ότι το σώμα είναι ενεργό.

Ενημερώνετε τα αρχεία μίας γραμμής τρέχοντας `python tools/update_orbital_elements.py` κάθε φορά που το JPL δημοσιεύει νέα λύση SBDB και ελέγχετε τις θέσεις με `python tools/verify_ephemeris.py` για επιβεβαίωση.
