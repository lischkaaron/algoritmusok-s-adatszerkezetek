import sys

# A 'sys' modul importálása a gyorsabb bemenet/kimenet (I/O) kezeléséhez.

INF = 10 ** 9


# Végtelen érték: egy nagyon nagy szám, ami a 'végtelent' szimulálja
# a minimális költség számításánál, jelezve az elérhetetlen állapotokat.

def buyingApples():
    # A fő függvény, ami a teljes program logikáját tartalmazza és kezeli az összes tesztesetet.
    try:
        input = sys.stdin.read
        # A teljes standard bemenet beolvasása egy stringként.
        data = input().split()
        # A bemeneti string szavakra (elemekre) bontása egy listába.
    except:
        return
        # Kezeli az üres vagy hibás bemenetet.

    if not data:
        return
        # Ha nincs adat, visszatérés.

    teszt_esetek_szama = int(data[0])
    # A tesztesetek számának beolvasása.
    eredmenyek = []
    # Egy lista a végső eredmények tárolására.

    adat_index = 1
    # Index a 'data' listában az aktuális bemeneti elemre.

    for _ in range(teszt_esetek_szama):
        # Ciklus az összes teszteset feldolgozására.
        max_csomag = int(data[adat_index])
        # max_csomag (N) beolvasása: a maximális megengedett csomagok száma (a barátok száma).
        cel_tomeg = int(data[adat_index + 1])
        # cel_tomeg (K) beolvasása: a pontosan megvásárolandó alma tömege (kg).
        adat_index += 2

        csomag_arak = [0] + [int(data[adat_index + i]) for i in range(cel_tomeg)]
        # Az árak beolvasása. A lista 0. indexe nem használt, csomag_arak[x] az x kg-os csomag ára.
        # A -1 értékek jelzik az elérhetetlen csomagokat.
        adat_index += cel_tomeg

        # Dinamikus Programozás (DP) tábla inicializálása:
        # min_koltseg_dp[tomeg_kg][csomag_db] tárolja a minimum költséget.
        # Méret: (cel_tomeg+1) sor x (max_csomag+1) oszlop. Minden cella kezdetben INF.
        min_koltseg_dp = [[INF] * (max_csomag + 1) for _ in range(cel_tomeg + 1)]

        min_koltseg_dp[0][0] = 0
        # Alapállapot: 0 kg alma, 0 csomag, 0 költség.

        # Fő DP ciklusok (Tölti fel a DP táblát):
        for tomeg_kg in range(1, cel_tomeg + 1):
            # tomeg_kg (i): Az aktuális összesített tömeg, amit el akarunk érni (1 kg-tól K kg-ig).
            for csomag_db in range(1, max_csomag + 1):
                # csomag_db (j): A felhasznált csomagok száma (1-től N-ig).
                for utolso_csomag_tomeg in range(1, min(tomeg_kg, cel_tomeg) + 1):
                    # utolso_csomag_tomeg (x): A legutóbb hozzáadott csomag tömege.
                    # Csak azokat a csomagokat vizsgáljuk, melyek tömege kisebb vagy egyenlő a tomeg_kg-nál.

                    # Ellenőrzés 1: Kapható-e az utolso_csomag_tomeg-es csomag? (Nem -1 az ára)
                    # Ellenőrzés 2: Elérhető volt-e az előző állapot? (A költség nem INF)
                    if csomag_arak[utolso_csomag_tomeg] != -1 and min_koltseg_dp[tomeg_kg - utolso_csomag_tomeg][
                        csomag_db - 1] != INF:

                        # Új költség = (Előző állapot költsége) + (Utolsó csomag ára).
                        uj_koltseg = min_koltseg_dp[tomeg_kg - utolso_csomag_tomeg][csomag_db - 1] + csomag_arak[
                            utolso_csomag_tomeg]

                        # Frissítés: Ha az új költség jobb (kisebb), mint az eddigi minimum a jelenlegi állapotra.
                        if uj_koltseg < min_koltseg_dp[tomeg_kg][csomag_db]:
                            min_koltseg_dp[tomeg_kg][csomag_db] = uj_koltseg

        # A végső minimum költség megkeresése cel_tomeg (K) kg-ra (legfeljebb max_csomag (N) csomaggal):
        vegso_minimum_koltseg = INF

        for csomag_db in range(1, max_csomag + 1):
            # Végigmegyünk az összes érvényes csomagszámon (1-től N-ig) a cel_tomeg sorban.
            if min_koltseg_dp[cel_tomeg][csomag_db] < vegso_minimum_koltseg:
                # Kikeressük a legkisebb költséget a cel_tomeg sorból.
                vegso_minimum_koltseg = min_koltseg_dp[cel_tomeg][csomag_db]

        # Eredmény rögzítése:
        if vegso_minimum_koltseg == INF:
            eredmenyek.append("-1")
            # Ha INF maradt, akkor nem lehetséges a cel_tomeg kg alma megvásárlása.
        else:
            eredmenyek.append(str(vegso_minimum_koltseg))
            # Hozzáadjuk a minimális költséget az eredmények listájához.

    sys.stdout.write('\n'.join(eredmenyek) + '\n')
    # Az összes teszteset eredményének kiírása, soronként.


buyingApples()
# A 'solve' függvény meghívása a program indításához.