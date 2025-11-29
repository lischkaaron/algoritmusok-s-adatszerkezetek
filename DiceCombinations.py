import sys


# A 'sys' modul importálása, amely hozzáférést biztosít a rendszer-specifikus paraméterekhez és funkciókhoz,
# különösen a standard bemenet ('sys.stdin') olvasásához.

def diceCombinations():
    # Definiálja a fő függvényt, amely a dobókocka kombinációk számítását végzi.

    # A standard bemenetről olvassuk be az összes adatot, és szóközök mentén felosztjuk egy listába.
    adatok = sys.stdin.read().split()
    if not adatok:
        # Ellenőrzi, hogy van-e adat a bemenetben. Ha nincs, kilép a függvényből.
        return

    celosszeg = int(adatok[0])
    # Az 'adatok' lista első elemét (ami a célösszeg) egész számmá konvertálja.

    modulus = 10 ** 9 + 7
    # Definiálja a modulust. A feladat általában nagy számok kezelésére kéri,
    # az eredményt ezzel az értékkel kell elosztani, és csak a maradékot kell kiírni.

    # --- Dinamikus Programozás (DP) inicializálása ---

    db_lehetoseg = [0] * (celosszeg + 1)
    # Létrehoz egy 'db_lehetoseg' nevű listát (DP táblát) a célösszeg + 1 méretben.
    # Minden index (i) tárolni fogja a 'i' összeg eléréséhez szükséges kombinációk számát.
    # Az indexek 0-tól 'celosszeg'-ig fognak futni.

    db_lehetoseg[0] = 1
    # Az alap eset (base case) beállítása: A 0 összeg eléréséhez pontosan 1 mód van
    # (nem dobunk egyet sem, vagyis az üres dobássorozat).

    # --- DP átmenetek kiszámítása ---

    for aktualis_osszeg in range(1, celosszeg + 1):
        # Végigmegy az összes lehetséges összeg (1-től a célösszegig).

        for dobas_ertek in range(1, 7):
            # Végigmegy a dobókocka lehetséges értékein (1-től 6-ig).

            elozo_osszeg = aktualis_osszeg - dobas_ertek
            # Kiszámítja az 'előző összeget', amiből az aktuális összeg elérhető
            # egyetlen 'dobas_ertek' hozzáadásával.

            if elozo_osszeg >= 0:
                # Csak akkor folytatja a számítást, ha az 'előző összeg' 0 vagy nagyobb.
                # (Pl. az 1 összeg nem érhető el 6-ból egy dobással.)

                # Dinamikus programozási átmenet:
                # A 'aktualis_osszeg' elérésének kombinációi =
                # (jelenlegi kombinációk száma) + (az 'elozo_osszeg' kombinációinak száma).
                # Az 'elozo_osszeg' kombinációi + 1 (dobás) adja az új kombinációkat.
                db_lehetoseg[aktualis_osszeg] = (db_lehetoseg[aktualis_osszeg] + db_lehetoseg[elozo_osszeg]) % modulus
                # Az eredményt a modulu-val veszi, hogy elkerülje az integer túlcsordulást.

    print(db_lehetoseg[celosszeg])
    # A DP tábla utolsó elemét (a célösszeghez tartozó kombinációk számát) kiírja a standard kimenetre.

diceCombinations()