import sys  # Importáljuk a sys modult a standard bemenet kezeléséhez.


def buildingTeams():  # Definiáljuk a fő függvényt, ami elvégzi a csapatbeosztást.
    # A standard bemenetről olvassuk be az összes adatot, és szóközök mentén felosztjuk egy listába.
    adatok = sys.stdin.read().split()
    if not adatok:
        return  # Ha nincs bemenet, azonnal visszatérünk.

    # Az első elem a diákok száma (n).
    diakok_szama = int(adatok[0])
    # A második elem a barátságok száma (m).
    baratsagok_szama = int(adatok[1])

    # Létrehozzuk a szomszédsági listát a gráf ábrázolásához.
    # N+1 méretű listát használunk, hogy a diákok 1-től N-ig legyenek indexelve (az index 0 üresen marad).
    szomszedok = [[] for _ in range(diakok_szama + 1)]

    adat_index = 2  # Az adatok listában a barátságok a 2. indexről kezdődnek.
    # Végigmegyünk az összes barátságon (m alkalommal).
    for _ in range(baratsagok_szama):
        # Beolvassuk az első diákot.
        diak_a = int(adatok[adat_index])
        # Beolvassuk a második diákot.
        diak_b = int(adatok[adat_index + 1])

        # Hozzáadjuk 'b' diákot 'a' szomszédaihoz (barátság létrehozása).
        szomszedok[diak_a].append(diak_b)
        # Hozzáadjuk 'a' diákot 'b' szomszédaihoz (a barátság kétirányú).
        szomszedok[diak_b].append(diak_a)

        adat_index += 2  # Ugrás a következő barátság párra.

    # Létrehozzuk a csapatbeosztást tároló listát.
    # 0 = még nincs beosztva, 1 = 1-es csapat, 2 = 2-es csapat.
    csapat = [0] * (diakok_szama + 1)

    # Végigmegyünk az összes diákon 1-től N-ig.
    for diak_index in range(1, diakok_szama + 1):
        # Ha a diák még nincs beosztva (azaz új összefüggő komponenst találtunk).
        if csapat[diak_index] == 0:
            # Inicializálunk egy BFS (szélességi bejárás) sort.
            sor = [diak_index]
            # Beosztjuk az aktuális diákot az 1-es csapatba.
            csapat[diak_index] = 1

            # Amíg van diák a sorban (BFS futtatása).
            while sor:
                # Kivesszük az első diákot a sorból.
                aktualis_diak = sor.pop(0)
                # Lekérdezzük a diák jelenlegi csapatát (1 vagy 2).
                aktualis_csapat = csapat[aktualis_diak]
                # Meghatározzuk a szomszédok kötelező csapatát (1->2, 2->1 a 3-való kivonás trükkjével).
                kovetkezo_csapat = 3 - aktualis_csapat

                # Végigmegyünk az aktuális diák összes szomszédján (barátján).
                for szomszed_diak in szomszedok[aktualis_diak]:
                    # Ha a szomszéd még nincs beosztva.
                    if csapat[szomszed_diak] == 0:
                        # Beosztjuk a szomszédot az eltérő csapatba.
                        csapat[szomszed_diak] = kovetkezo_csapat
                        # Hozzáadjuk a sort a további bejáráshoz.
                        sor.append(szomszed_diak)
                        # Ha a szomszéd be van osztva ÉS ugyanabban a csapatban van, mint az aktuális diák.
                    elif csapat[szomszed_diak] == aktualis_csapat:
                        # Ez egy ellentmondás, két barát került egy csapatba (a gráf nem páros).
                        print("IMPOSSIBLE")
                        return  # Kilépünk, mivel nincs megoldás.

    # Ha a bejárás lezajlott ellentmondás nélkül, a gráf páros, és találtunk megoldást.
    # Kiírjuk a csapatbeosztást az 1-es indextől (kihagyjuk a 0-át), szóközzel elválasztva.
    print(*(csapat[1:]))

buildingTeams()