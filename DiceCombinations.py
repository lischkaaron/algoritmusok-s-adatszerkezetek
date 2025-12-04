import sys

def diceCombinations():
    """
    A feladat: Hányféleképpen dobhatunk ki egy 'n' összeget (celosszeg) egy vagy több dobókockával?
    Módszer: Dinamikus Programozás (DP).
    Alapelv: Egy 'x' összeghez úgy juthattunk el, hogy előtte 'x-1', 'x-2', ... 'x-6' összegnél voltunk,
    és dobtunk egy 1-est, 2-est... vagy 6-ost.
    """

    # --- 1. ADATBEOLVASÁS ---
    # Minden bemenetet egyszerre olvasunk be a memóriába, majd feldaraboljuk.
    # Ez sokkal gyorsabb Pythonban, mint soronként olvasni (input()).
    adatok = sys.stdin.read().split()

    if not adatok:
        return

    # A célösszeg (N), amit el szeretnénk érni a dobások összegével.
    celosszeg = int(adatok[0])

    # A feladat kéri, hogy az eredményt modulo 10^9 + 7 alakban adjuk meg.
    # Ez azért kell, mert a kombinációk száma iszonyatosan nagy lehet, és nem férne el a memóriában,
    # vagy túl lassú lenne vele számolni.
    maradekos_oszto = 10 ** 9 + 7

    # --- 2. DP TÁBLA INICIALIZÁLÁSA ---
    # Létrehozunk egy tömböt, ahol az index (i) jelenti az elért összeget,
    # az érték pedig azt, hogy hányféleképpen juthatunk el oda.
    # Méret: celosszeg + 1 (hogy a 0-tól az N-ig minden index létezzen).
    db_lehetoseg = [0] * (celosszeg + 1)

    # BÁZISESET (Base Case):
    # A 0 összeget pontosan 1-féleképpen érhetjük el: úgy, hogy nem dobunk semmit (üres halmaz).
    # Ez az "indító" érték, enélkül a matematika nem működne.
    db_lehetoseg[0] = 1

    # --- 3. A MEGOLDÁS FELÉPÍTÉSE (Bottom-Up) ---
    # Végigmegyünk minden számon 1-től a célösszegig.
    # Minden 'aktualis_osszeg'-re kiszámoljuk, hányféleképpen juthatunk ide.
    for aktualis_osszeg in range(1, celosszeg + 1):

        # Belső ciklus: Megnézzük az utolsó dobást.
        # "Hogyan juthattam ide? Dobhattam 1-et, 2-t, ... vagy 6-ot."
        for dobas_ertek in range(1, 7):

            # Megnézzük, honnan jöttünk volna ezzel a dobással.
            # Pl. Ha most 5-nél vagyunk és 2-t dobtunk, akkor előtte 3-nál kellett lennünk.
            elozo_osszeg = aktualis_osszeg - dobas_ertek

            # Csak akkor számolunk, ha az 'elozo_osszeg' nem negatív.
            # (Pl. az 1-es összeget nem érhetjük el úgy, hogy 2-t dobtunk, mert -1-ről kellett volna jönnünk).
            if elozo_osszeg >= 0:

                # REKURZÍV ÖSSZEFÜGGÉS (Transition):
                # Az aktuális összeghez vezető utak száma növekszik azzal,
                # ahányféleképpen az 'elozo_osszeg'-et el tudtuk érni.
                # dp[i] += dp[i - dobás]
                db_lehetoseg[aktualis_osszeg] += db_lehetoseg[elozo_osszeg]

                # Minden összeadásnál alkalmazzuk a maradékos osztást a túlcsordulás ellen.
                db_lehetoseg[aktualis_osszeg] %= maradekos_oszto

    # --- 4. EREDMÉNY ---
    # A ciklus végére a tömb utolsó eleme tartalmazza a választ a teljes 'celosszeg'-re.
    print(db_lehetoseg[celosszeg])

diceCombinations()