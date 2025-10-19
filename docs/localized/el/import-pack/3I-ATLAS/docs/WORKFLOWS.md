# Ροές εφαρμογών για 3I/ATLAS

Όλες οι τιμές αυτού του πακέτου προέρχονται από τη λύση 27 του JPL SBDB (2025-10-10).
Ενημερώστε τα αρχεία με το script μετατροπής όταν κυκλοφορήσει νεότερη λύση.

## Stellarium (Windows/macOS/Linux)

**Δέχεται:** στοιχεία κομήτη MPC μίας γραμμής  
**Βήματα:**
1. **Configuration → Plugins → Solar System Editor** → ενεργοποιήστε το **Load at startup** (επανεκκίνηση αν χρειάζεται).  
2. **Solar System Editor → Configure → Solar System → Import elements in MPC format → File**.  
3. Επιλέξτε `templates/stellarium/3I_ATLAS_mpc_elements.txt`.  
4. Πατήστε **Add object(s)** και αναζητήστε **3I/ATLAS**.

## KStars (Windows/macOS/Linux)

**Δέχεται:** γραμμή `comets.dat`  
**Βοηθοί:**
- Windows: `tools/kstars/KStars_Append_3I-DRYRUN.bat` (προεπισκόπηση) και έπειτα `…-APPLY.bat`.  
- macOS: διπλό κλικ στο `tools/kstars/KStars_Append_3I.command`.  
- Linux: εκτελέστε `bash tools/kstars/KStars_Append_3I.sh`.  
Όλοι οι βοηθοί δημιουργούν αντίγραφο ασφαλείας πριν την προσθήκη.

Χειροκίνητα:
1. Δημιουργήστε αντίγραφο του `comets.dat` (`~/.local/share/kstars/comets.dat` σε Linux, `%LOCALAPPDATA%\kstars\comets.dat` σε Windows, `~/Library/Application Support/kstars/comets.dat` σε macOS).  
2. Προσθέστε τη μία γραμμή από `templates/kstars/3I_ATLAS_comets_dat_snippet.txt`.  
3. Επανεκκινήστε το KStars και βρείτε **3I/ATLAS**.

## SkySafari / SkyVoyager (iOS/Android)

**Δέχεται:** καμία χειροκίνητη εισαγωγή  
Χρησιμοποιήστε *Settings → Solar System → Update Orbit Data* (επίπεδα Plus/Pro). Κρατήστε
το `templates/skysafari/3I_ATLAS_mpc_1line.txt` μόνο για αναφορά.

## Cartes du Ciel (SkyCharts)

**Δέχεται:** αρχεία στοιχείων MPC  
Ακολουθήστε τις οδηγίες στο `apps-using-mpc-files/cartes-du-ciel/README.txt`
(εισαγωγή μέσω GUI ή χειροκίνητη προσθήκη στο `comet.dat`).

## WinStars 3

**Δέχεται:** αρχεία στοιχείων MPC  
Δείτε το `apps-using-mpc-files/winstars/README.txt` για τα βήματα γρήγορης εισαγωγής.

## Solar Fire (Windows)

**Δέχεται:** στοιχεία τροχιάς `extras.dat` (Other Bodies)  
**Βοηθοί:**
- Windows: `tools/solarfire/SF_Merge_3I-DRYRUN.bat` (προεπισκόπηση) και στη συνέχεια `…-APPLY.bat` για αυτόματη συγχώνευση του `[3I_ATLAS]`.  
Και τα δύο scripts δημιουργούν αντίγραφο ασφαλείας του `extras.dat` με χρονοσήμανση.

Χειροκίνητα:
1. Κλείστε το Solar Fire και κρατήστε αντίγραφο του `Documents\Solar Fire User Files\Userdata\extras.dat`.  
2. Αντιγράψτε ή συγχωνεύστε το μπλοκ `[3I_ATLAS]` από `templates/solar_fire/3I_ATLAS_extras_dat_PLACEHOLDER.txt`.  
3. Εκκινήστε ξανά και ενεργοποιήστε το **3I/ATLAS** μέσα από **Extra Bodies** στο παράθυρο επιλογής σημείων.

## Εφαρμογές χωρίς δυνατότητα εισαγωγής

Τα Astro Gold (macOS/iOS/iPadOS) και TimePassages Desktop (macOS/Windows) προσφέρουν
μόνο πρόσθετα σημεία που παρέχει ο κατασκευαστής και δεν δέχονται
efemérides κινούμενων σωμάτων από τον χρήστη. Συμβουλευτείτε τον φάκελο `Time-Passages-Astro-Gold/`
για λύσεις με σταθερά σημεία και στοιχεία επικοινωνίας με τον προμηθευτή.
