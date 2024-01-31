# Aplicație pentru Gestiunea Tractoarelor la o Fermă

## Descriere
Aceasta este o aplicație pentru gestionarea tractoarelor la o fermă. La pornirea aplicației, se încarcă toate tractoarele dintr-un fișier text. Aplicația oferă următoarele funcționalități:

1. **Adăugare de Tractor** (1p)
   - Se introduc următoarele informații: id, denumire, preț, model, dată (zi:lună:an) la care expiră revizia.
   - Aplicația salvează imediat tractorul în fișier.

2. **Ștergere Tractoare** (1.5p)
   - Utilizatorul introduce o cifră.
   - Se șterg toate tractoarele pentru care prețul conține cifra dată.
   - Se afișează un mesaj cu numărul tractoarelor șterse.
   - Modificările se reflectă imediat în fișier.

3. **Filtrare Tractoare** (1p)
   - Utilizatorul poate seta un filtru constând într-un text și un număr.
   - Aplicația afișează filtrul curent și lista tractoarelor care îndeplinesc criteriile.
   - Lista este tipărită după acționarea oricărui element de meniu.
   - Sunt incluse tractoarele care în denumire conțin textul și au prețul mai mic decât prețul din filtru.
   - Tractoarele cu revizia expirată au un "*" în fața denumirii. (1p)
   - Filtrarea nu afectează fișierul cu tractoare.

4. **Undo Ultima Operație** (1p)
   - Aplicația reface ultima operație (adăugare sau ștergere).
   - Dacă ultima operație era adăugare, tractorul dispare; dacă era ștergere, tractoarele reapar în aplicație.
   - Modificarea se reflectă și în fișier.

## Of. 1p Arhitectură (1.5p)
   - Se acordă 1.5 puncte pentru arhitectură.

## Specificații și Teste (2p)
   - Punctajul se acordă proporțional cu funcționalitățile rezolvate.
   - Dacă datele nu se scriu/citesc din fișier, punctajul maxim este 50% din punctaj la fiecare funcționalitate.
