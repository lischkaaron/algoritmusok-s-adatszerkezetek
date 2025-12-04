import sys

def buyingApples():
    """
    A függvény célja: Meghatározni a minimális költséget K kg alma megvásárlásához,
    legfeljebb N darab csomag felhasználásával.
    Módszer: Dinamikus Programozás (DP).
    """

    # --- 1. ADATBEOLVASÁS ---
    # Beolvassuk a teljes bemenetet egyetlen hosszú stringként, majd feldaraboljuk szóközök/újsorok mentén.
    adatok = sys.stdin.read().split()

    if not adatok:
        return

    # Az első szám a tesztesetek (különböző feladatok) száma.
    teszt_esetek_szama = int(adatok[0])
    eredmenyek = []  # Ide gyűjtjük majd a végeredményeket minden tesztesethez.

    # Ez a változó mutatja, hol tartunk éppen az 'adatok' lista feldolgozásában.
    adat_index = 1

    # --- 2. TESZTESETEK FELDOLGOZÁSA ---
    for _ in range(teszt_esetek_szama):

        # A feladat paramétereinek kinyerése:
        # N = max_csomag: Legfeljebb ennyi csomagot vehetünk.
        # K = cel_tomeg: Pontosan ennyi kg almát kell vennünk.
        max_csomag = int(adatok[adat_index])
        cel_tomeg = int(adatok[adat_index + 1])
        adat_index += 2  # Léptetjük az indexet a következő adatra.

        # Árak beolvasása:
        # A lista indexe jelenti a súlyt (pl. csomag_arak[3] a 3 kg-os csomag ára).
        # A [0] helyre egy 0-t teszünk (dummy elem), hogy az indexelés 1-től indulhasson (1 kg..K kg).
        csomag_arak = [0] + [int(adatok[adat_index + i]) for i in range(cel_tomeg)]
        adat_index += cel_tomeg  # Léptetjük az indexet az árak után.

        # --- 3. DINAMIKUS PROGRAMOZÁS (DP) TÁBLA ÉPÍTÉSE ---
        # A táblázat (mátrix) felépítése:
        #   - Sorok (i): Elért súly (0-tól cel_tomeg-ig).
        #   - Oszlopok (j): Felhasznált csomagok száma (0-tól max_csomag-ig).
        #   - Cella értéke: A minimális költség az adott súlyhoz, adott csomagszámmal.
        #   - Kezdőérték: -1, ami itt a "még nem elért" vagy "lehetetlen" állapotot jelöli (végtelen helyett).
        min_koltseg_dp = [[-1] * (max_csomag + 1) for _ in range(cel_tomeg + 1)]

        # Báziseset beállítása:
        # 0 kg alma 0 csomaggal pontosan 0 forintba kerül. Innen indulunk.
        min_koltseg_dp[0][0] = 0

        # --- 4. A MEGOLDÁSKERESÉS (A Mátrix kitöltése) ---
        # Végigmegyünk minden lehetséges súlyon 1-től a célértékig (K).
        for aktualis_suly in range(1, cel_tomeg + 1):

            # Végigmegyünk a csomagok darabszámán 1-től a maximumig (N).
            for csomagok_szama in range(1, max_csomag + 1):

                # Belső ciklus: Kipróbáljuk az utolsó lépést.
                # "Mi van, ha az utolsó választott csomag súlya 'utolso_meret' kg volt?"
                # Csak akkora csomagot próbálunk, ami nem nagyobb, mint a jelenlegi 'aktualis_suly'.
                for utolso_meret in range(1, min(aktualis_suly, cel_tomeg) + 1):

                    # Két fontos feltételt ellenőrzünk:
                    # 1. Létezik-e ilyen méretű csomag a boltban? (Ha az ára -1, akkor nem kapható).
                    # 2. El tudtunk-e jutni a "maradék" súlyhoz eggyel kevesebb csomaggal?
                    #    (Példa: Ha 5kg-nál vagyunk és 2kg-osat próbálunk, elértük-e már korábban a 3kg-t?)
                    elozo_suly = aktualis_suly - utolso_meret
                    elozo_darab = csomagok_szama - 1

                    csomag_elerheto = (csomag_arak[utolso_meret] != -1)
                    Elozo_allapot_elerheto = (min_koltseg_dp[elozo_suly][elozo_darab] != -1)

                    if csomag_elerheto and Elozo_allapot_elerheto:
                        # Ha lehetséges a lépés, kiszámoljuk az új költséget:
                        # (Előző állapot költsége) + (Mostani csomag ára)
                        potencialis_uj_koltseg = min_koltseg_dp[elozo_suly][elozo_darab] + csomag_arak[utolso_meret]

                        # Megnézzük, mit írtunk eddig ebbe a cellába.
                        jelenlegi_ertek_a_cellaban = min_koltseg_dp[aktualis_suly][csomagok_szama]

                        # Frissítjük a cellát, ha:
                        # A) Még üres volt (-1).
                        # B) VAGY találtunk egy olcsóbb megoldást ugyanerre a súlyra és darabszámra.
                        if jelenlegi_ertek_a_cellaban == -1 or potencialis_uj_koltseg < jelenlegi_ertek_a_cellaban:
                            min_koltseg_dp[aktualis_suly][csomagok_szama] = potencialis_uj_koltseg

        # --- 5. EREDMÉNY KIVÁLASZTÁSA ---
        # A célunk pontosan 'cel_tomeg' (K) elérése volt.
        # Megnézzük a mátrix utolsó sorát (ahol a súly == K).
        # Bármelyik oszlop jó nekünk, hiszen a feladat azt mondta: "LEGFELJEBB N csomag".
        # Tehát lehet 1, 2, ... vagy N csomaggal is elérni a célt, nekünk a legolcsóbb kell ezek közül.

        vegso_minimum_koltseg = -1  # Alapértelmezett: nem találtunk megoldást.

        for db in range(1, max_csomag + 1):
            koltseg_adott_darabszamnal = min_koltseg_dp[cel_tomeg][db]

            if koltseg_adott_darabszamnal != -1:  # Ha érvényes megoldás
                if vegso_minimum_koltseg == -1 or koltseg_adott_darabszamnal < vegso_minimum_koltseg:
                    vegso_minimum_koltseg = koltseg_adott_darabszamnal

        # Az eredményt stringként tároljuk a kimenethez.
        # Ha maradt -1, az azt jelenti: lehetetlen ennyi almát venni a feltételekkel.
        eredmenyek.append(str(vegso_minimum_koltseg))

    # Kiírjuk az összes eredményt új sorokkal elválasztva.
    print('\n'.join(eredmenyek) + '\n')


buyingApples()

