import sys # A 'sys' modul importálása a gyorsabb bemenet/kimenet (I/O) kezeléséhez.

INF = 10 ** 9 # Végtelen érték: egy nagyon nagy szám, ami a 'végtelent' szimulálja.
# A minimális költség számításánál jelzi az elérhetetlen állapotokat.

def buyingApples(): # A fő függvény, ami a teljes program logikáját tartalmazza.
    # A standard bemenetről olvassuk be az összes adatot, és szóközök mentén felosztjuk egy listába.
    adatok = sys.stdin.read().split() # Beolvassa a bemenetet, és felosztja azt elemekre egy listában.
    if not adatok: # Ellenőrzés, hogy van-e adat a bemenetben.
        return # Ha nincs adat, visszatérés.

    teszt_esetek_szama = int(adatok[0]) # A tesztesetek számának beolvasása.
    eredmenyek = [] # Egy lista a végső eredmények tárolására.

    adat_index = 1 # Index az adatok listában az aktuális bemeneti elemre.

    for _ in range(teszt_esetek_szama): # Ciklus az összes teszteset feldolgozására.
        max_csomag = int(adatok[adat_index]) # max_csomag (N) beolvasása: a maximális megengedett csomagok száma.
        cel_tomeg = int(adatok[adat_index + 1]) # cel_tomeg (K) beolvasása: a pontosan megvásárolandó alma tömege (kg).
        adat_index += 2 # Az index léptetése.

        # Az árak beolvasása. A lista 0. indexe nem használt (vagy a 0 kg-os csomag ára 0).
        csomag_arak = [0] + [int(adatok[adat_index + i]) for i in range(cel_tomeg)] # Beolvassa a K kg-ig terjedő csomagárakat.
        # A -1 értékek jelzik az elérhetetlen csomagokat.
        adat_index += cel_tomeg # Az index léptetése az árak számával.

        # Dinamikus Programozás (DP) tábla inicializálása:
        # min_koltseg_dp[tomeg_kg][csomag_db] tárolja a minimum költséget.
        # Méret: (cel_tomeg+1) sor x (max_csomag+1) oszlop.
        min_koltseg_dp = [[INF] * (max_csomag + 1) for _ in range(cel_tomeg + 1)] # Minden cella kezdetben INF.

        # Alapállapot beállítása:
        min_koltseg_dp[0][0] = 0 # 0 kg alma, 0 csomag, 0 költség.

        # Fő DP ciklusok (Tölti fel a DP táblát):
        for tomeg_kg in range(1, cel_tomeg + 1): # tomeg_kg (i): Az aktuális összesített tömeg (1 kg-tól K kg-ig).
            for csomag_db in range(1, max_csomag + 1): # csomag_db (j): A felhasznált csomagok száma (1-től N-ig).
                for utolso_csomag_tomeg in range(1, min(tomeg_kg, cel_tomeg) + 1): # utolso_csomag_tomeg (x): A legutóbb hozzáadott csomag tömege.
                    # Csak azokat a csomagokat vizsgáljuk, melyek tömege kisebb vagy egyenlő a tomeg_kg-nál.

                    # Ellenőrzés 1: Kapható-e az 'utolso_csomag_tomeg'-es csomag? (Ár != -1)
                    # Ellenőrzés 2: Elérhető volt-e az előző állapot? (Költség != INF)
                    if csomag_arak[utolso_csomag_tomeg] != -1 and min_koltseg_dp[tomeg_kg - utolso_csomag_tomeg][
                        csomag_db - 1] != INF:

                        # Új költség = (Előző állapot költsége) + (Utolsó csomag ára).
                        uj_koltseg = min_koltseg_dp[tomeg_kg - utolso_csomag_tomeg][csomag_db - 1] + csomag_arak[
                            utolso_csomag_tomeg]

                        # Frissítés: Ha az új költség jobb (kisebb), mint az eddigi minimum a jelenlegi állapotra.
                        if uj_koltseg < min_koltseg_dp[tomeg_kg][csomag_db]:
                            min_koltseg_dp[tomeg_kg][csomag_db] = uj_koltseg

        # A végső minimum költség megkeresése cel_tomeg (K) kg-ra (legfeljebb max_csomag (N) csomaggal):
        vegso_minimum_koltseg = INF # Inicializálás végtelenre.

        for csomag_db in range(1, max_csomag + 1): # Végigmegyünk az összes érvényes csomagszámon (1-től N-ig).
            # Kikeressük a legkisebb költséget a 'cel_tomeg' sorból.
            if min_koltseg_dp[cel_tomeg][csomag_db] < vegso_minimum_koltseg: # Ha találtunk jobb megoldást.
                vegso_minimum_koltseg = min_koltseg_dp[cel_tomeg][csomag_db] # Frissítjük a minimumot.

        # Eredmény rögzítése:
        if vegso_minimum_koltseg == INF: # Ha INF maradt, akkor nem lehetséges a cél elérése.
            eredmenyek.append("-1") # Hozzáadjuk a "-1"-et az eredmények listájához.
        else:
            eredmenyek.append(str(vegso_minimum_koltseg)) # Hozzáadjuk a minimális költséget (stringként) a listához.

    print('\n'.join(eredmenyek) + '\n') # Az összes teszteset eredményének kiírása, soronként, egyetlen stringben.

buyingApples() # Meghívja a fő függvényt a futtatáshoz.