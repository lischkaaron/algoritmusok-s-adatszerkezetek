import sys # Importáljuk a sys modult a standard bemenet kezeléséhez.


def buildingTeams(): # Definiáljuk a fő függvényt, ami elvégzi a csapatbeosztást.
    # A standard bemenetről olvassuk be az összes adatot, és szóközök mentén felosztjuk egy listába.
    adatok = sys.stdin.read().split() # Beolvassuk a bemenetet.
    if not adatok: # Ellenőrizzük, hogy van-e bemenet.
        return # Ha nincs, azonnal visszatérünk.

    # Az első elem a diákok száma (n).
    diakok_szama = int(adatok[0]) # Beolvassuk N-et.
    # A második elem a barátságok száma (m).
    baratsagok_szama = int(adatok[1]) # Beolvassuk M-et.

    # Létrehozzuk a szomszédsági listát a gráf ábrázolásához.
    # N+1 méretű listát használunk, hogy a diákok 1-től N-ig legyenek indexelve.
    szomszedok = [[] for _ in range(diakok_szama + 1)] # Inicializáljuk a szomszédsági listát.

    adat_index = 2 # Az adatok listában a barátságok a 2. indexről kezdődnek.
    # Végigmegyünk az összes barátságon (m alkalommal).
    for _ in range(baratsagok_szama): # Ciklus M barátságon keresztül.
        # Beolvassuk az első diákot.
        diak_a = int(adatok[adat_index]) # Diák A beolvasása.
        # Beolvassuk a második diákot.
        diak_b = int(adatok[adat_index + 1]) # Diák B beolvasása.

        # Hozzáadjuk 'b' diákot 'a' szomszédaihoz (barátság létrehozása).
        szomszedok[diak_a].append(diak_b) # A -> B él hozzáadása.
        # Hozzáadjuk 'a' diákot 'b' szomszédaihoz (a barátság kétirányú).
        szomszedok[diak_b].append(diak_a) # B -> A él hozzáadása.

        adat_index += 2 # Ugrás a következő barátság párra.

    # Létrehozzuk a csapatbeosztást tároló listát.
    # 0 = még nincs beosztva, 1 = 1-es csapat, 2 = 2-es csapat.
    csapat = [0] * (diakok_szama + 1) # Inicializáljuk a csapat-állapotokat.

    # Végigmegyünk az összes diákon 1-től N-ig.
    for diak_index in range(1, diakok_szama + 1): # Ciklus minden diákra (és komponensre).
        # Ha a diák még nincs beosztva (azaz új összefüggő komponenst találtunk).
        if csapat[diak_index] == 0: # Kezdőpont egy új komponensben.
            # Inicializálunk egy BFS (szélességi bejárás) sort.
            sor = [diak_index] # A sorba tesszük a kezdő diákot.
            # Beosztjuk az aktuális diákot az 1-es csapatba.
            csapat[diak_index] = 1 # Beosztjuk az 1. csapatba.

            # Amíg van diák a sorban (BFS futtatása).
            while sor: # Futtatjuk a BFS-t.
                # Kivesszük az első diákot a sorból.
                aktualis_diak = sor.pop(0) # Pop a sor elejéről.
                # Lekérdezzük a diák jelenlegi csapatát (1 vagy 2).
                aktualis_csapat = csapat[aktualis_diak] # Az aktuális csapat lekérése.
                # Meghatározzuk a szomszédok kötelező csapatát (1->2, 2->1 a 3-való kivonás trükkjével).
                kovetkezo_csapat = 3 - aktualis_csapat # A szomszédoknak ez kell, hogy legyen a csapata.

                # Végigmegyünk az aktuális diák összes szomszédján (barátján).
                for szomszed_diak in szomszedok[aktualis_diak]: # Iterálás a szomszédokon.
                    # Ha a szomszéd még nincs beosztva.
                    if csapat[szomszed_diak] == 0: # Ha a szomszédot nem láttuk még.
                        # Beosztjuk a szomszédot az eltérő csapatba.
                        csapat[szomszed_diak] = kovetkezo_csapat # Színezés a másik csapattal.
                        # Hozzáadjuk a sort a további bejáráshoz.
                        sor.append(szomszed_diak) # Berakjuk a szomszédot a sorba.
                    # Ha a szomszéd be van osztva ÉS ugyanabban a csapatban van, mint az aktuális diák.
                    elif csapat[szomszed_diak] == aktualis_csapat: # Ha a két barát ugyanabba a csapatba került.
                        # Ez egy ellentmondás, két barát került egy csapatba (a gráf nem páros).
                        print("IMPOSSIBLE") # Kiírjuk a megoldás hiányát.
                        return # Kilépünk, mivel nincs megoldás.

    # Ha a bejárás lezajlott ellentmondás nélkül, a gráf páros, és találtunk megoldást.
    # Kiírjuk a csapatbeosztást az 1-es indextől (kihagyjuk a 0-át), szóközzel elválasztva.
    print(*(csapat[1:])) # Kiírjuk a végső csapatbeosztást.

buildingTeams() # Meghívja a fő függvényt a futtatáshoz.