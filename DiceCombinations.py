import sys # A 'sys' modul importálása, amely hozzáférést biztosít a rendszer-specifikus paraméterekhez és funkciókhoz.


def diceCombinations(): # Definiálja a fő függvényt, amely a dobókocka kombinációk számítását végzi.
    # A standard bemenetről olvassuk be az összes adatot, és szóközök mentén felosztjuk egy listába.
    adatok = sys.stdin.read().split() # Beolvassa a bemenetet, és felosztja azt elemekre egy listában.
    if not adatok: # Ellenőrizzük, hogy van-e bemenet.
        return # Ha nincs, azonnal visszatérünk.

    celosszeg = int(adatok[0]) # Az 'adatok' lista első elemét (ami a célösszeg) egész számmá konvertálja.

    # A változó neve módosítva:
    maradekos_oszto = 10 ** 9 + 7 # Definiálja a maradékos osztás alapját (10^9 + 7), a nagy számok kezelésére.

    # --- Dinamikus Programozás (DP) inicializálása ---

    # Létrehoz egy 'db_lehetoseg' nevű listát (DP táblát) a célösszeg + 1 méretben.
    db_lehetoseg = [0] * (celosszeg + 1) # Inicializálja a listát nullákkal.
    # Minden index (i) tárolni fogja az 'i' összeg eléréséhez szükséges kombinációk számát.

    # Az alap eset (base case) beállítása:
    db_lehetoseg[0] = 1 # A 0 összeg eléréséhez pontosan 1 mód van (az üres dobássorozat).

    # --- DP átmenetek kiszámítása ---

    for aktualis_osszeg in range(1, celosszeg + 1): # Végigmegy az összes lehetséges összegen (1-től a célösszegig).

        for dobas_ertek in range(1, 7): # Végigmegy a dobókocka lehetséges értékein (1-től 6-ig).

            # Kiszámítja az 'előző összeget', amiből az aktuális összeg elérhető
            # egyetlen 'dobas_ertek' hozzáadásával.
            elozo_osszeg = aktualis_osszeg - dobas_ertek # Megtalálja az előző állapotot.

            if elozo_osszeg >= 0: # Csak akkor folytatja, ha az 'előző összeg' érvényes (0 vagy nagyobb).

                # Dinamikus programozási átmenet:
                # db_lehetoseg[aktualis_osszeg] = (jelenlegi kombinációk száma) + (az 'elozo_osszeg' kombinációinak száma)
                # Az 'elozo_osszeg' kombinációi + 1 (dobás) adja az új kombinációkat az aktuális összeghez.
                db_lehetoseg[aktualis_osszeg] = (db_lehetoseg[aktualis_osszeg] + db_lehetoseg[elozo_osszeg]) % maradekos_oszto # Hozzáadja az előző állapot eredményét.
                # Az eredményt a maradékos osztóval veszi, hogy elkerülje az integer túlcsordulást.

    # A DP tábla utolsó elemét (a célösszeghez tartozó kombinációk számát) kiírja a standard kimenetre.
    print(db_lehetoseg[celosszeg]) # Kiírja a végeredményt.

diceCombinations() # Meghívja a fő függvényt a futtatáshoz.