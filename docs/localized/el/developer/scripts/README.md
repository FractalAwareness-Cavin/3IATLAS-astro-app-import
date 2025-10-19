# Scripts προγραμματιστή

Οι βοηθητικές εφαρμογές για την αναδημιουργία και επαλήθευση του κιτ επιμηρίδων 3I/ATLAS βρίσκονται στους φακέλους `developer/scripts/` και `tools/`. Ακολουθήστε αυτόν τον οδηγό όταν χρειάζεται να ανανεώσετε το dataset ή να ελέγξετε τις αλλαγές πριν από μια νέα κυκλοφορία.

## Προαπαιτούμενα
- Python 3.10 ή νεότερη (`python3 --version` για επιβεβαίωση).
- Προαιρετικά: ένα εικονικό περιβάλλον (`python3 -m venv .venv && source .venv/bin/activate`) αν σκοπεύετε να εγκαταστήσετε επιπλέον πακέτα.
- Πρόσβαση στο διαδίκτυο κατά την εκτέλεση του SBDB updater ή του ελεγκτή Horizons.
- Προαιρετικά: `mksweph` αν θέλετε να δημιουργήσετε δυαδικά Swiss Ephemeris μέσω `build_swisseph.sh`.

Το αποθετήριο περιλαμβάνει το `pyswisseph` στον φάκελο `developer/vendor/`, οπότε οι αστρικές έξοδοι λειτουργούν χωρίς πρόσθετες εγκαταστάσεις.

## Προεπιλεγμένη συνταγή Horizons

Τα ακατέργαστα JSON στο `developer/raw/` δημιουργήθηκαν από το NASA/JPL Horizons με τις ακόλουθες παραμέτρους:

```
COMMAND='DES=1004083;'
MAKE_EPHEM='YES'
EPHEM_TYPE='VECTORS'
CENTER='500@399'        # κέντρο Γης
REF_PLANE='ECLIPTIC'
REF_SYSTEM='J2000'
START_TIME='2016-01-01'
STOP_TIME='2040-12-31'
STEP_SIZE='1 d'
TABLE_TYPE='VECTORS'
```

Τροποποιήστε τα αν χρειάζεστε διαφορετικό χρονικό διάστημα ή σημείο παρατήρησης· ενημερώστε ύστερα τα JSON πριν την επαναδημιουργία αποτελεσμάτων.

## `generate_ephemeris.py`
Θέση: `developer/scripts/generate_ephemeris.py`

- Διαβάζει τα dumps διανυσμάτων JSON στο `developer/raw/` και αναδομεί όλα τα παράγωγα προϊόντα:
  - Πίνακες CSV στο `apps-using-csv-files/`
  - Αρχεία κειμένου για το Solar Fire στο `solar-fire/`
  - Εφημερίδα MPC (`apps-using-mpc-files/geocentric_mpc_ephemeris.txt`)
  - Περιλήψεις εισόδων στα ζώδια.
- Φορτώνει αυτόματα το ενσωματωμένο `pyswisseph` ώστε να συμπληρώνονται τα αστρικά πεδία.
- Δημιουργεί τους φακέλους προορισμού αν δεν υπάρχουν.

Χρήση:

```
cd developer/scripts
python3 generate_ephemeris.py
```

Το script λειτουργεί με προκαθορισμένες ρυθμίσεις. Για να αλλάξετε το χρονικό εύρος ή την καμπάνια, ενημερώστε πρώτα τα JSON (ή τις σταθερές στην αρχή του αρχείου).

## `build_swisseph.sh`
Θέση: `developer/scripts/build_swisseph.sh`

- Απαιτεί το ιδιόκτητο εργαλείο `mksweph`.
- Μετατρέπει τις εξόδους CSV σε δυαδικά `.se1` του Swiss Ephemeris και τα αποθηκεύει στο `developer/swisseph/`.

Χρήση:

```
cd developer/scripts
bash build_swisseph.sh
```

Το βοηθητικό πρόγραμμα δεν θα εκτελεστεί αν το `mksweph` δεν υπάρχει στο `PATH`.

## `tools/update_orbital_elements.py`
Θέση: `tools/update_orbital_elements.py`

- Ανακτά την τελευταία τροχιακή λύση SBDB για το 3I/ATLAS και ενημερώνει όλα τα πρότυπα μίας γραμμής:
  - Αρχεία MPC (`apps-using-mpc-files/*/3I_ATLAS_mpc_1line.txt`)
  - Αποσπάσματα KStars (`apps-using-mpc-files/kstars/` και πρότυπα του import pack)
  - Μπλοκ `extras.dat` για το Solar Fire.
- Εκτυπώνει τα ληφθέντα στοιχεία στο stdout για έλεγχο.

Χρήση (από τη ρίζα του αποθετηρίου):

```
python tools/update_orbital_elements.py
```

Προσθέστε `--dry-run` για προεπισκόπηση των τιμών χωρίς αλλαγή αρχείων.

## `tools/verify_ephemeris.py`
Θέση: `tools/verify_ephemeris.py`

- Ελέγχει επιλεγμένες γραμμές του `apps-using-mpc-files/geocentric_mpc_ephemeris.txt` έναντι των ζωντανών δεδομένων Horizons.
- Συγκρίνει την γεωκεντρική απόσταση («delta») σε ρυθμιζόμενο χρονικό εύρος και επισημαίνει γραμμές που υπερβαίνουν την ανοχή.

Χρήση (από τη ρίζα του αποθετηρίου):

```
python tools/verify_ephemeris.py --start 2025-10-01 --days 5 --tolerance 5e-4
```

Παράμετροι:
- `--start`: πρώτη ημερομηνία ελέγχου (προεπιλογή `2025-10-01`).
- `--days`: αριθμός συνεχόμενων ημερών (προεπιλογή `5`).
- `--tolerance`: μέγιστη επιτρεπτή διαφορά σε αστρονομικές μονάδες (προεπιλογή `5e-4`, περίπου 75 000 km).

Το script επιστρέφει μη μηδενικό κωδικό αν βρει αποκλίσεις, διευκολύνοντας τη χρήση σε CI.
