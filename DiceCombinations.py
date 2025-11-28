import sys

def diceCombinations():
    bemenet_fuggveny = sys.stdin.read
    adatok = bemenet_fuggveny().split()

    if not adatok:
        return

    celosszeg = int(adatok[0])
    modulus = 10 ** 9 + 7

    db_lehetoseg = [0] * (celosszeg + 1)
    db_lehetoseg[0] = 1

    for aktualis_osszeg in range(1, celosszeg + 1):
        for dobas_ertek in range(1, 7):

            elozo_osszeg = aktualis_osszeg - dobas_ertek

            if elozo_osszeg >= 0:
                db_lehetoseg[aktualis_osszeg] = (db_lehetoseg[aktualis_osszeg] + db_lehetoseg[elozo_osszeg]) % modulus

    print(db_lehetoseg[celosszeg])


if __name__ == "__main__":
    diceCombinations()