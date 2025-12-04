import sys

def buildingTeams():
    """
    A feladat célja: Két csapatra (1-es és 2-es) osztani a diákokat úgy,
    hogy barátok ne kerüljenek egy csapatba.
    Matematikai háttér: Ez a "Páros Gráf" (Bipartite Graph) probléma.
    Eldöntjük, hogy a gráf színezhető-e 2 színnel.
    """

    # --- 1. ADATBEOLVASÁS ---
    # Egyszerre olvassuk be az összes adatot, mert ez Pythonban sokkal gyorsabb, mint soronként.
    adatok = sys.stdin.read().split()

    if not adatok:
        return

    # N = diákok (csúcsok) száma, M = barátságok (élek) száma.
    diakok_szama = int(adatok[0])
    baratsagok_szama = int(adatok[1])

    # --- 2. GRÁF FELÉPÍTÉSE ---
    # Szomszédsági listát (Adjacency List) használunk, mert a gráf ritka lehet.
    # A lista indexe a diák sorszáma, az értéke pedig egy lista a barátairól.
    # (N + 1) méretűt készítünk, hogy kényelmesen, 1-től indexelhessünk (a 0. indexet nem használjuk).
    szomszedok = [[] for _ in range(diakok_szama + 1)]

    adat_index = 2
    for _ in range(baratsagok_szama):
        u = int(adatok[adat_index])
        v = int(adatok[adat_index + 1])
        adat_index += 2

        # Mivel a barátság kölcsönös (irányítatlan gráf), mindkét irányba felvesszük az élet.
        szomszedok[u].append(v)
        szomszedok[v].append(u)

    # --- 3. CSAPATBEOSZTÁS (SZÍNEZÉS) ---
    # Ez a tömb tárolja, ki melyik csapatban van.
    # 0: Még nincs beosztva (látogatatlan).
    # 1: 1-es csapat.
    # 2: 2-es csapat.
    csapat = [0] * (diakok_szama + 1)

    # Végigmegyünk minden diákon 1-től N-ig.
    # FONTOS: Nem elég csak az 1. diáktól indítani a keresést, mert a gráf nem biztos, hogy összefüggő!
    # Lehetnek elszigetelt baráti társaságok (komponensek), mindegyiket külön kell színeznünk.
    for i in range(1, diakok_szama + 1):

        # Ha 'i' diák még nincs beosztva, akkor ő egy új komponens (csoport) kezdőpontja.
        if csapat[i] == 0:
            # --- BFS (Szélességi bejárás) INDÍTÁSA ---
            # A kezdő diákot betesszük az 1-es csapatba.
            csapat[i] = 1
            sor = [i]  # A BFS várakozási sora (queue).

            # Addig megyünk, amíg van feldolgozandó diák a sorban.
            while sor:
                aktualis_diak = sor.pop(0)  # Kivesszük a sor elejét.

                # Megnézzük, melyik csapatban van a jelenlegi diák.
                jelenlegi_csapat = csapat[aktualis_diak]

                # Kiszámoljuk, melyik csapatba KELL kerülnie a barátainak.
                # Ha mi az 1-esben vagyunk, ők a 2-esbe (3-1=2).
                # Ha mi a 2-esben vagyunk, ők az 1-esbe (3-2=1).
                kovetkezo_csapat = 3 - jelenlegi_csapat

                # Megvizsgáljuk az aktuális diák összes barátját.
                for szomszed in szomszedok[aktualis_diak]:

                    # ESET A: A barátnak még nincs csapata (most találkozunk vele először).
                    if csapat[szomszed] == 0:
                        csapat[szomszed] = kovetkezo_csapat  # Beosztjuk a másik csapatba.
                        sor.append(szomszed)  # Betesszük a sorba, hogy később az ő barátait is megvizsgáljuk.

                    # ESET B: A barátnak már van csapata, és az UGYANAZ, mint a miénk.
                    # Ez baj! Két barát került egy csapatba -> Ellentmondás.
                    elif csapat[szomszed] == jelenlegi_csapat:
                        print("IMPOSSIBLE")
                        return  # Azonnal kilépünk, nincs megoldás.

    # --- 4. KIMENET ---
    # Ha a ciklusok hiba nélkül lefutottak, sikerült a beosztás.
    # A '*' operátor kicsomagolja a listát, így szóközzel elválasztva írja ki az elemeket.
    # A [1:] miatt a 0. indexű (használaton kívüli) elemet kihagyjuk.
    print(*(csapat[1:]))

buildingTeams()