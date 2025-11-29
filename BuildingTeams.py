import sys


def buildingTeams():
    try:
        adatok = sys.stdin.read().split()
        if not adatok:
            return

        diakok_szama = int(adatok[0])
        baratsagok_szama = int(adatok[1])

        szomszedok = [[] for _ in range(diakok_szama + 1)]

        adat_index = 2
        for _ in range(baratsagok_szama):
            diak_a = int(adatok[adat_index])
            diak_b = int(adatok[adat_index + 1])
            szomszedok[diak_a].append(diak_b)
            szomszedok[diak_b].append(diak_a)
            adat_index += 2

    except Exception:
        print("IMPOSSIBLE")
        return

    csapat = [0] * (diakok_szama + 1)

    for diak_index in range(1, diakok_szama + 1):
        if csapat[diak_index] == 0:
            sor = [diak_index]
            csapat[diak_index] = 1

            while sor:
                aktualis_diak = sor.pop(0)
                aktualis_csapat = csapat[aktualis_diak]
                kovetkezo_csapat = 3 - aktualis_csapat

                for szomszed_diak in szomszedok[aktualis_diak]:
                    if csapat[szomszed_diak] == 0:
                        csapat[szomszed_diak] = kovetkezo_csapat
                        sor.append(szomszed_diak)
                    elif csapat[szomszed_diak] == aktualis_csapat:
                        print("IMPOSSIBLE")
                        return

    print(*(csapat[1:]))


if __name__ == "__main__":
    buildingTeams()