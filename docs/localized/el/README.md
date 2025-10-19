# Πακέτο επιμηρίδων 3I/ATLAS

Ημερήσιες επιμηρίδες για τον διαστρικό κομήτη **3I/ATLAS (C/2025 N1)**, εξαγόμενες απευθείας από το NASA/JPL Horizons και οργανωμένες ώστε οι αστρολόγοι να μπορούν να τον εντάξουν στις αγαπημένες τους εφαρμογές. Η κάλυψη περιλαμβάνει ολόκληρη τη διέλευση από την ηλιοσφαίρα (2016‑01‑01 → 2040‑12‑31). Η παρούσα έκδοση βασίζεται στη **λύση Horizons #27 (2025‑10‑10)**· τρέξτε `tools/update_orbital_elements.py` όποτε η JPL δημοσιεύσει νεότερη λύση για να ενημερώσετε τα βοηθητικά αρχεία.

## Γρήγορη εκκίνηση
1. Κατεβάστε το πακέτο που αντιστοιχεί στην εφαρμογή σας (βλ. **Άμεσες λήψεις**) ή κλωνοποιήστε το αποθετήριο.
2. Αποσυμπιέστε ώστε να δείτε το `README` κάθε φακέλου.
3. Ακολουθήστε τη λίστα βημάτων στο `README` ή εκτελέστε τα helper scripts για Solar Fire, KStars και Stellarium.
4. Προαιρετική συντήρηση: `python tools/update_orbital_elements.py` φέρνει την τελευταία λύση SBDB και `python tools/verify_ephemeris.py` συγκρίνει με το Horizons πριν διανέμετε ενημερώσεις.

## Περιεχόμενα
- [Γρήγορη εκκίνηση](#γρήγορη-εκκίνηση)
- [Υποστηριζόμενες εφαρμογές (εισαγωγή κινητών σωμάτων)](#υποστηριζόμενες-εφαρμογές-εισαγωγή-κινητών-σωμάτων)
- [Από πού να ξεκινήσω;](#από-πού-να-ξεκινήσω)
- [Άμεσες λήψεις](#άμεσες-λήψεις)
- [Οδηγός φακέλων](#οδηγός-φακέλων)
- [Γλωσσάρι](#γλωσσάρι)
- [Οδηγίες ανά εφαρμογή](#οδηγίες-ανά-εφαρμογή)
  - [Πακέτο εισαγωγής & scripts](#πακέτο-εισαγωγής--scripts)
  - [Κατάσταση Astro Gold](#κατάσταση-astro-gold)
  - [Solar Fire (Windows)](#solarfire-instructions-windows)
  - [Εισαγωγή σε μορφή MPC](#εισαγωγή-σε-μορφή-mpc)
  - [Astro Gold & TimePassages](#astro-gold--timepassages)
  - [Σημειώσεις για CSV](#σημειώσεις-για-csv)
- [Συνταγή Horizons](#συνταγή-horizons)
- [Αναδημιουργία επιμηρίδων](#αναδημιουργία-επιμηρίδων)
- [Scripts συντήρησης](#scripts-συντήρησης)
- [Βασικά ορόσημα](#βασικά-ορόσημα)
- [Σημειώσεις & προειδοποιήσεις](#σημειώσεις--προειδοποιήσεις)
- [Αντιμετώπιση προβλημάτων](#αντιμετώπιση-προβλημάτων)
- [Προαιρετικά: εγκατάσταση εργαλείων Horizons](#προαιρετικά-εγκατάσταση-εργαλείων-horizons)

Υποστηριζόμενες εφαρμογές (εισαγωγή κινητών σωμάτων)
----------------------------------------------------
- **Stellarium** (Win/macOS/Linux): εισαγωγή μέσω Solar System Editor σε μορφή MPC.
- **KStars** (Win/macOS/Linux): προσθήκη στη `comets.dat` (με βοηθούς).
- **Solar Fire** (Windows): συγχώνευση μπλοκ `[3I_ATLAS]` στο `extras.dat`.
- **Cartes du Ciel / SkyCharts** (Win/macOS/Linux): εισαγωγή αρχείων MPC ή επεξεργασία `comet.dat`.
- **WinStars 3** (Win/macOS/Linux): επικόλληση της MPC γραμμής στον editor.
- **SkySafari / SkyVoyager Plus/Pro** (iOS/Android/macOS): ενημέρωση τροχιακών δεδομένων από MPC feeds.

Χωρίς εισαγωγή κινητών σωμάτων:
- **Astro Gold** (macOS/iOS/iPadOS) και **TimePassages** (macOS/Windows). Δείτε λύσεις με σταθερά σημεία.

Για απορίες γράψτε στο [cavinbirdseyetarot@gmail.com](mailto:cavinbirdseyetarot@gmail.com).



## Από πού να ξεκινήσω

Επιλέξτε τον φάκελο που ταιριάζει στην εφαρμογή σας ή κατεβάστε ένα από τα zip. Αν δεν είστε σίγουροι, ανοίξτε την εφαρμογή και δείτε τι μορφές δέχεται μέσω *File → Import*.

- `solar-fire/`: είσοδος `extras.dat` και επιμηρίδες αναφοράς.
- `apps-using-mpc-files/`: `geocentric_mpc_ephemeris.txt` σε κλασική μορφή MPC 80 στηλών (UT 0h, J2000 RA/Dec, Δ, r, επιμήκυνση, φάση).
- `apps-using-csv-files/`: CSV με διανύσματα ηλιο/γεω/βαρυκεντρικά, εισόδους σε ζώδια, πλάτη.
- `developer/`: εξαγωγές Horizons JSON, scripts αναδημιουργίας, ενσωματωμένο `pyswisseph`, Swiss Ephemeris helper.
- `Time-Passages-Astro-Gold/`: περιορισμοί Astro Gold/TimePassages και οδηγίες για σταθερά σημεία.

#### Άμεσες λήψεις
- [Solar Fire merge helper (Windows)](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/SolarFire_merge-helper_Windows.zip)
- [KStars quick append (Win/macOS/Linux)](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/KStars_quick-append_Win-Mac-Linux.zip)
- [Stellarium quick import](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/Stellarium_quick-import.zip)
- [MPC ephemeris (80 columns)](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/3I-ATLAS_apps_using_mpc_files.zip)
- [CSV research kit](https://github.com/FractalAwareness-Cavin/3IATLAS-astro-app-import/releases/download/v1.0.0/3I-ATLAS_apps_using_csv_files.zip)

Κάθε zip αντικατοπτρίζει τον ομώνυμο φάκελο και περιλαμβάνει `README.txt` με συγκεκριμένα βήματα· αποσυμπιέστε πριν τρέξετε scripts ή αντιγράψετε αρχεία.

## Οδηγός φακέλων

- **solar-fire/**: δεδομένα `extras.dat` για Solar Fire και πίνακες αναφοράς.
- **apps-using-mpc-files/**: πλήρης MPC επιμηρίδα, leading lines, οδηγίες ανά εφαρμογή.
- **apps-using-csv-files/**: CSV με διανύσματα, εισόδους σε ζώδια, πλατος, ταχύτητες.
- **developer/**: scripts, vendored `pyswisseph`, raw Horizons, Swiss Ephemeris helper.
- **Time-Passages-Astro-Gold/**: λύσεις για εφαρμογές χωρίς import.
- **import-pack/**: συμπαγές bundle με templates, scripts, τεκμηρίωση.

## Γλωσσάρι

- **MPC 80 columns**: κλασική μορφή Minor Planet Center.
- **Horizons SBDB**: βάση μικρών σωμάτων NASA/JPL.
- **Επιμήκυνση**: γωνιακή απόσταση από τον Ήλιο όπως φαίνεται από τη Γη.
- **Δ (delta)**: γεωκεντρική απόσταση.
- **r**: ηλιοκεντρική απόσταση.
- **UT**: Universal Time / UTC.

## Οδηγίες ανά εφαρμογή

### Πακέτο εισαγωγής & scripts

Δείτε `import-pack/3I-ATLAS/README.md` για templates, scripts, διαδικασίες ενημέρωσης.

### Κατάσταση Astro Gold

Δεν υπάρχει εισαγωγή κινητών σωμάτων· ακολουθήστε τις οδηγίες σταθερού σημείου (`Time-Passages-Astro-Gold/`).

### SolarFire instructions Windows

`solar-fire/README.txt` περιγράφει τη συγχώνευση `[3I_ATLAS]` σε `extras.dat`. Οι βοηθοί στο `tools/solarfire/` παρέχουν Dry-Run/Apply.

### Εισαγωγή σε μορφή MPC

Στους υποφακέλους `apps-using-mpc-files/` θα βρείτε README για Stellarium, KStars, Cartes du Ciel, WinStars και τα σχετικά αρχεία.

### Astro Gold & TimePassages

Χωρίς δυναμικό import· δημιουργήστε σταθερά σημεία για συγκεκριμένες ημερομηνίες.

### Σημειώσεις για CSV

`apps-using-csv-files/README.txt` εξηγεί στήλες/μονάδες για spreadsheets, notebooks ή scripts. Για σιδηρικές μελέτες αφαιρέστε την αγαπημένη σας ayanāṃśa από την τροπική μακρότητα.

## Συνταγή Horizons

`developer/raw/` περιέχει JSON που παρήχθησαν από Horizons με:

```
COMMAND='DES=1004083;'
MAKE_EPHEM='YES'
EPHEM_TYPE='VECTORS'
CENTER='500@399'
REF_PLANE='ECLIPTIC'
REF_SYSTEM='J2000'
START_TIME='2016-01-01'
STOP_TIME='2040-12-31'
STEP_SIZE='1 d'
TABLE_TYPE='VECTORS'
```

Προσαρμόστε παράθυρα χρόνου ή κέντρο παρατήρησης και ανανεώστε τα JSON πριν την επαναδημιουργία.

## Αναδημιουργία επιμηρίδων

### `developer/scripts/generate_ephemeris.py`

- Διαβάζει τα JSON και ανανεώνει:
  - Πίνακες CSV (`apps-using-csv-files/`)
  - Κείμενα Solar Fire (`solar-fire/`)
  - MPC επιμηρίδα (`apps-using-mpc-files/geocentric_mpc_ephemeris.txt`)
  - Περιλήψεις εισόδων στα ζώδια.
- Δημιουργεί φακέλους στόχους αν λείπουν.

```
cd developer/scripts
python3 generate_ephemeris.py
```

### `developer/scripts/build_swisseph.sh`

- Απαιτεί το εργαλείο `mksweph`.
- Μετατρέπει CSV σε Swiss Ephemeris `.se1` (`developer/swisseph/`).

```
cd developer/scripts
bash build_swisseph.sh
```

### `tools/update_orbital_elements.py`

- Φέρνει τη νεότερη λύση SBDB και ενημερώνει αρχεία MPC, αποσπάσματα KStars, μπλοκ Solar Fire.

```
python tools/update_orbital_elements.py
```

Χρησιμοποιήστε `--dry-run` για προεπισκόπηση χωρίς εγγραφή.

### `tools/verify_ephemeris.py`

- Συγκρίνει γραμμές `apps-using-mpc-files/geocentric_mpc_ephemeris.txt` με live Horizons.

```
python tools/verify_ephemeris.py --start 2025-10-01 --days 5 --tolerance 5e-4
```

Προεπιλογές: 2025-10-01, 5 ημέρες, ανοχή `5e-4` α. μ. (~75.000 km). Επιστρέφει σφάλμα αν βρει αποκλίσεις — χρήσιμο για CI.

## Scripts συντήρησης

- **`tools/3i_elements_to_formats.py`**: μετατρέπει νέα MPC μονής γραμμής σε templates (Stellarium, KStars, Solar Fire).
- **`tools/kstars/`**: βοηθοί ανά λειτουργικό για backup/append στο `comets.dat`.
- **`tools/solarfire/`**: scripts Windows για συγχώνευση `extras.dat`.

## Βασικά ορόσημα

- 2024-10-xx — πρώτη εξαγωγή Horizons, οργάνωση φακέλων.
- 2025-10-xx — ενημέρωση στη λύση SBDB 27.
- 2025-10-xx — προσθήκη scripts ελέγχου και πακέτου εισαγωγής.

## Σημειώσεις & προειδοποιήσεις

- **Solar Fire**: πάρε backup του `extras.dat` πριν τη συγχώνευση.
- **SkySafari**: δεν δέχεται χειροκίνητο import αρχείων — χρησιμοποίησε *Update Orbit Data*.
- **Astro Gold / TimePassages**: μόνο σταθερά σημεία προς το παρόν.
- **Επαλήθευση**: `tools/verify_ephemeris.py` ελέγχει γρήγορα ενάντια σε Horizons.

## Αντιμετώπιση προβλημάτων

- **Δεν βρίσκω 3I/ATLAS μετά την εισαγωγή.** Κάνε επανεκκίνηση και βεβαιώσου ότι η γραφή είναι `3I/ATLAS`.
- **Θέσεις μετατοπισμένες.** Τα MPC αρχεία είναι στο **UT 0h**· εργάσου σε UTC ή εφάρμοσε διόρθωση ζώνης.
- **Solar Fire δείχνει την παλιά λίστα.** Έλεγξε το σωστό `extras.dat` (κάθε major έκδοση έχει δικό της φάκελο) ή τρέξε ξανά το APPLY script.
- **Θέλω έλεγχο δεδομένων.** `python tools/verify_ephemeris.py` συγκρίνει με Horizons σε πραγματικό χρόνο.

Καλή χαρτογράφηση του 3I/ATLAS!

## Προαιρετικά: εγκατάσταση εργαλείων Horizons

Δεν απαιτείται (τα δεδομένα περιλαμβάνονται), αλλά αν θέλεις να παράγεις νέο υλικό:

### macOS / Linux
1. Βεβαιώσου ότι `python3 --version` ≥ 3.10.
2. Εγκατάστησε Astroquery:
   ```bash
   python3 -m pip install astroquery --user
   ```
3. Εκτέλεσε ερώτημα Horizons:
   ```bash
   python3 - <<'PY'
   from astroquery.jplhorizons import Horizons
   obj = Horizons(id='DES=1004083;', location='500@399', epochs={'start':'2025-01-01', 'stop':'2025-01-10', 'step':'1d'})
   print(obj.vectors())
   PY
   ```

Εναλλακτικά:

```bash
curl "https://ssd.jpl.nasa.gov/api/horizons.api?format=json&COMMAND='DES=1004083;'&MAKE_EPHEM=YES&EPHEM_TYPE=VECTORS&CENTER='500@399'&REF_PLANE=ECLIPTIC&STEP_SIZE=1%20d&START_TIME=2025-01-01&STOP_TIME=2025-01-03"
```

### Windows
1. Κατέβασε Python 3 από https://www.python.org/downloads/ (τσεκάρισε “Add Python to PATH”).
2. Σε PowerShell:
   ```powershell
   py -m pip install astroquery
   py - <<'PY'
   from astroquery.jplhorizons import Horizons
   obj = Horizons(id='DES=1004083;', location='500@399', epochs={'start':'2025-01-01', 'stop':'2025-01-10', 'step':'1d'})
   print(obj.vectors())
   PY
   ```
3. Χρήστες WSL μπορούν να ακολουθήσουν τις οδηγίες macOS/Linux.

### Κλασικό CLI (Telnet)
```bash
telnet horizons.jpl.nasa.gov 6775
```
Ακολουθήστε τα prompts, δηλώνοντας `DES=1004083;` και τις επιλογές εξόδου.

### Εγκατάσταση Python 3.10+ σε Linux

Χρησιμοποιήστε τον διαχειριστή πακέτων (apt, dnf, zypper, pacman…). Αν δεν διατίθεται η έκδοση, στραφείτε σε pyenv ή μεταγλώττιση από πηγή. Ακόμη και αν υπάρχει συστημικό Python, προτιμήστε δική σας εγκατάσταση ≥3.10 και virtual environments (`python3 -m venv`).
