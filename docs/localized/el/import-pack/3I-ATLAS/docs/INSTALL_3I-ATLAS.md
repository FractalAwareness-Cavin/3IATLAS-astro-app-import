# 3I/ATLAS — Πακέτο εισαγωγής (v0.2)

Χρησιμοποιήστε αυτό το πακέτο όταν χρειάζεστε **στοιχεία τροχιάς MPC έτοιμα προς χρήση**
ή έναν βοηθό προσαρμοσμένο στην πλατφόρμα σας για να περάσετε το 3I/ATLAS σε λογισμικό αστρονομίας.
Όλα λειτουργούν χωρίς σύνδεση και βασίζονται στη λύση 27 του JPL SBDB (2025-10-10).

> **Σύνοψη**
> - **Stellarium** → εισαγωγή της παρεχόμενης γραμμής μέσω *Solar System Editor → Import elements in MPC format*.
> - **KStars** → εκτελέστε τον βοηθό χωρίς εγκατάσταση (Windows/macOS/Linux) ή επικολλήστε τη γραμμή `comets.dat` που παρέχεται.
> - **SkySafari** → χρησιμοποιήστε *Settings → Solar System → Update Orbit Data* (Plus/Pro) και κρατήστε τη γραμμή MPC ως αναφορά.
> - **Solar Fire** → συγχωνεύστε το μπλοκ `[3I_ATLAS]` στο `extras.dat` (πάρτε πρώτα αντίγραφο ασφαλείας)· περιλαμβάνονται scripts βοήθειας.
> - **Astro Gold / TimePassages** → προς το παρόν δεν υποστηρίζεται εισαγωγή κινούμενων σωμάτων· δείτε τις σημειώσεις του κύριου αποθετηρίου για λύσεις με σταθερά σημεία.

## Τι περιλαμβάνει

- `templates/stellarium/3I_ATLAS_mpc_elements.txt` — στοιχείο κομήτη MPC μίας γραμμής για το 3I/ATLAS.
- `templates/skysafari/3I_ATLAS_mpc_1line.txt` — η ίδια γραμμή για αρχείο/αναφορά.
- `templates/kstars/3I_ATLAS_comets_dat_snippet.txt` — γραμμή έτοιμη για προσθήκη στο `comets.dat` (ισχύει και για Cartes du Ciel / WinStars).
- `templates/solar_fire/3I_ATLAS_extras_dat_PLACEHOLDER.txt` — έτοιμο μπλοκ `[3I_ATLAS]` για το `extras.dat` του Solar Fire.
- `tools/3i_elements_to_formats.py` — προαιρετικός μετατροπέας για νεότερη γραμμή MPC.
- `tools/update_orbital_elements.py` — αντλεί την τελευταία λύση του JPL SBDB και επανεγγράφει όλα τα πρότυπα.
- `docs/WORKFLOWS.md` — οδηγίες βήμα-βήμα για Stellarium, KStars, Cartes du Ciel, WinStars, SkySafari, Solar Fire.

## Γρήγορη εκκίνηση

Ήδη ενημερωμένοι; Μεταβείτε κατευθείαν στο `docs/WORKFLOWS.md`. Για ανανέωση κάθε φορά που ο JPL
δημοσιεύει νέα τροχιά, τρέξτε τον ενημερωτή:
```bash
python tools/update_orbital_elements.py --dry-run  # προεπισκόπηση των τελευταίων στοιχείων
python tools/update_orbital_elements.py            # επανεγγράφει τα πρότυπα
```
Αν προτιμάτε χειροκίνητη αντικατάσταση, το `tools/3i_elements_to_formats.py`
παράγει τα αποσπάσματα για Stellarium/KStars/Solar Fire από οποιαδήποτε γραμμή MPC.

## Επισημάνσεις

- **Solar Fire `extras.dat`**: η σειρά των πεδίων μπορεί να διαφέρει ανά έκδοση. Συμβουλευτείτε
το ενσωματωμένο βοήθημα «Format of the Orbital Elements File» πριν επεξεργαστείτε χειροκίνητα και κρατήστε πάντα αντίγραφο ασφαλείας.
- **SkySafari**: δεν υπάρχει χειροκίνητη εισαγωγή αρχείων· χρησιμοποιήστε *Update Orbit Data*.
- **Astro Gold / TimePassages**: κατά τη συγγραφή δεν παρέχουν ροή εισαγωγής κινούμενων σωμάτων. Χρησιμοποιήστε τα σταθερά προσαρμοσμένα σημεία τους ή απευθυνθείτε στον κατασκευαστή.
- **Επαλήθευση**: εκτελέστε `tools/verify_ephemeris.py` για να συγκρίνετε επιλεγμένες γραμμές του
`apps-using-mpc-files/geocentric_mpc_ephemeris.txt` με ζωντανά δεδομένα Horizons αν θέλετε να ελέγξετε τις επιμηρίδες.
