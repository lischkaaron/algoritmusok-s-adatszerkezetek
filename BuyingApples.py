import sys

# A 'sys' modul importálása a bemenet/kimenet kezeléséhez.

INF = 10 ** 9


# Végtelen érték: jelzi az elérhetetlen, túl nagy költséget.

def buyingApples():
    # A fő függvény, ami kezeli az összes tesztesetet.
    try:
        input = sys.stdin.read
        data = input().split()
        # Teljes bemenet beolvasása és szavakra bontása.
    except:
        return
        # Hibakezelés (pl. ha nincs bemenet).

    if not data:
        return

    teszt_esetek_szama = int(data[0])
    # A tesztesetek számának beolvasása.
    eredmenyek = []
    # Egy lista a végeredmények tárolására.

    adat_index = 1
    # Index a bemeneti adatok feldolgozásához.

    for _ in range(teszt_esetek_szama):
        # Ciklus az összes teszteset feldolgozására.
        max_csomag = int(data[adat_index])
        # max_csomag beolvasása: a maximális megengedett csomagok száma (N).
        cel_tomeg = int(data[adat_index + 1])
        # cel_tomeg beolvasása: a pontosan megvásárolandó tömeg (K).
        adat_index += 2

        csomag_arak = [0] + [int(data[adat_index + i]) for i in range(cel_tomeg)]
        # Az árak beolvasása. csomag_arak[x] az x kg-os csomag ára.
        adat_index += cel_tomeg

        # Dinamikus Programozás (DP) tábla inicializálása:
        # min_koltseg_dp[tomeg_kg][csomag_db] tárolja a minimum költséget.
        # Méret: (cel_tomeg+1) x (max_csomag+1).
        min_koltseg_dp = [[INF] * (max_csomag + 1) for _ in range(cel_tomeg + 1)]

        min_koltseg_dp[0][0] = 0
        # Alapállapot: 0 kg, 0 csomag, 0 költség.

        # DP tábla feltöltése:
        for tomeg_kg in range(1, cel_tomeg + 1):
            # tomeg_kg: Az aktuális összesített tömeg (1-től K-ig).
            for csomag_db in range(1, max_csomag + 1):
                # csomag_db: A felhasznált csomagok száma (1-től N-ig).
                for utolso_csomag_tomeg in range(1, min(tomeg_kg, cel_tomeg) + 1):
                    # utolso_csomag_tomeg: A legutóbb hozzáadott csomag tömege (1-től tomeg_kg-ig).

                    # Kapható-e az utolsó csomag (nem -1) és elérhető volt-e az előző állapot?
                    if csomag_arak[utolso_csomag_tomeg] != -1 and min_koltseg_dp[tomeg_kg - utolso_csomag_tomeg][
                        csomag_db - 1] != INF:

                        # Új költség = (Előző állapot költsége) + (Utolsó csomag ára).
                        uj_koltseg = min_koltseg_dp[tomeg_kg - utolso_csomag_tomeg][csomag_db - 1] + csomag_arak[
                            utolso_csomag_tomeg]

                        # Frissítés: Ha az új költség jobb (kisebb), mint az eddigi minimum.
                        if uj_koltseg < min_koltseg_dp[tomeg_kg][csomag_db]:
                            min_koltseg_dp[tomeg_kg][csomag_db] = uj_koltseg

        # A végső minimum költség megkeresése K kg-ra (legfeljebb N csomaggal):
        vegso_minimum_koltseg = INF

        for csomag_db in range(1, max_csomag + 1):
            # Végigmegyünk az összes érvényes csomagszámon (1-től N-ig).
            if min_koltseg_dp[cel_tomeg][csomag_db] < vegso_minimum_koltseg:
                # Kikeressük a legkisebb költséget a K kg-ot tartalmazó sorból.
                vegso_minimum_koltseg = min_koltseg_dp[cel_tomeg][csomag_db]

        # Eredmény rögzítése:
        if vegso_minimum_koltseg == INF:
            eredmenyek.append("-1")
            # Nem lehet megvásárolni.
        else:
            eredmenyek.append(str(vegso_minimum_koltseg))
            # Kiírjuk a minimális költséget.

    sys.stdout.write('\n'.join(eredmenyek) + '\n')
    # Az eredmények kiírása.


buyingApples()
# A függvény meghívása.