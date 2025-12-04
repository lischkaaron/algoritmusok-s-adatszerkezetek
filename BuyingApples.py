import sys  # A 'sys' modul importálása a gyorsabb bemenet/kimenet (I/O) kezeléséhez.


# INF változó törölve lett.

def buyingApples():  # A fő függvény, ami a teljes program logikáját tartalmazza.
    # A standard bemenetről olvassuk be az összes adatot, és szóközök mentén felosztjuk egy listába.
    adatok = sys.stdin.read().split()  # Beolvassa a bemenetet, és felosztja azt elemekre egy listában.
    if not adatok:  # Ellenőrizzük, hogy van-e bemenet.
        return  # Ha nincs, azonnal visszatérünk.

    teszt_esetek_szama = int(adatok[0])  # A tesztesetek számának beolvasása.
    eredmenyek = []  # Egy lista a végső eredmények tárolására.

    adat_index = 1  # Index az adatok listában az aktuális bemeneti elemre.

    for _ in range(teszt_esetek_szama):  # Ciklus az összes teszteset feldolgozására.
        max_csomag = int(adatok[adat_index])  # max_csomag (N) beolvasása.
        cel_tomeg = int(adatok[adat_index + 1])  # cel_tomeg (K) beolvasása.
        adat_index += 2  # Az index léptetése.

        # Az árak beolvasása.
        csomag_arak = [0] + [int(adatok[adat_index + i]) for i in range(cel_tomeg)]
        adat_index += cel_tomeg  # Az index léptetése.

        # Dinamikus Programozás (DP) tábla inicializálása:
        # Most -1 jelenti az "üres" vagy "elérhetetlen" állapotot az INF helyett.
        min_koltseg_dp = [[-1] * (max_csomag + 1) for _ in range(cel_tomeg + 1)]

        # Alapállapot beállítása:
        min_koltseg_dp[0][0] = 0  # 0 kg alma, 0 csomag, 0 költség.

        # Fő DP ciklusok (Tölti fel a DP táblát):
        for tomeg_kg in range(1, cel_tomeg + 1):  # tomeg_kg (i)
            for csomag_db in range(1, max_csomag + 1):  # csomag_db (j)
                for utolso_csomag_tomeg in range(1, min(tomeg_kg, cel_tomeg) + 1):  # utolso_csomag_tomeg (x)

                    # Ellenőrzés 1: Kapható-e a csomag? (Ár != -1)
                    # Ellenőrzés 2: Elérhető volt-e az előző állapot? (Költség != -1, azaz nem üres)
                    if csomag_arak[utolso_csomag_tomeg] != -1 and min_koltseg_dp[tomeg_kg - utolso_csomag_tomeg][
                        csomag_db - 1] != -1:

                        # Új költség kiszámítása
                        uj_koltseg = min_koltseg_dp[tomeg_kg - utolso_csomag_tomeg][csomag_db - 1] + csomag_arak[
                            utolso_csomag_tomeg]

                        # 1. Ha a jelenlegi hely még -1 (üres), akkor mindenképp beírjuk az új költséget.
                        # 2. VAGY ha már van ott érték, de az új költség kisebb (olcsóbb), akkor felülírjuk.
                        jelenlegi_ertek = min_koltseg_dp[tomeg_kg][csomag_db]

                        if jelenlegi_ertek == -1 or uj_koltseg < jelenlegi_ertek:
                            min_koltseg_dp[tomeg_kg][csomag_db] = uj_koltseg

        # A végső minimum költség megkeresése cel_tomeg (K) kg-ra:
        vegso_minimum_koltseg = -1  # -1-ről indítjuk (ez jelenti, hogy "nincs még találat")

        for csomag_db in range(1, max_csomag + 1):
            aktualis_koltseg = min_koltseg_dp[cel_tomeg][csomag_db]

            # Csak akkor foglalkozunk vele, ha érvényes szám (nem -1)
            if aktualis_koltseg != -1:
                # Ha még nincs találatunk (vegso == -1), vagy ez jobb, mint az eddigi:
                if vegso_minimum_koltseg == -1 or aktualis_koltseg < vegso_minimum_koltseg:
                    vegso_minimum_koltseg = aktualis_koltseg

        # Eredmény rögzítése:
        # Mivel a vegso_minimum_koltseg eleve -1 maradt, ha nem találtunk megoldást,
        # egyszerűen stringgé alakítjuk. Ha találtunk, akkor a pozitív szám lesz benne.
        eredmenyek.append(str(vegso_minimum_koltseg))

    print('\n'.join(eredmenyek) + '\n')


buyingApples()