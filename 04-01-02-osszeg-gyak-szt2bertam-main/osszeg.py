# osszeg-gyak.py

# 1. feladat
# Határozza meg a számok összegét
import math


def feladat01_osszeg() -> int:
    szamok = [1.2, 2.3, 3.2, 4.1, 2.4, 2.3, 1.9, 0.1]
    osszeg = 0
    for szam in szamok:
        osszeg = osszeg + szam
    return osszeg

# 2. feladat
# Határozza meg a pozitív számok összegét
def feladat02_osszeg() -> int:
    szamok = [1.2, -2.3, 3.2, -4.1, -2.4, 2.3, 1.9, 0.1]
    pozszamosszeg = 0
    for szam in szamok:
        if szam > 0:
            pozszamosszeg = pozszamosszeg + szam
    return pozszamosszeg

# 3. feladat
# Határozza meg a páros számok összegét
def feladat03_osszeg() -> int:
    szamok = [2, 3, 4, 9, 1, 8, 6, 1]
    parosszamokosszege = 0
    for szam in szamok:
        if szam % 2 == 0:
            parosszamokosszege = parosszamokosszege + szam
    return parosszamokosszege

# 4. feladat
# Képezze úgy az összeget, hogy a két listából az adott pozicióból mindig a nagyobb számot vegye!
def feladat04_osszeg() -> int:
    szamok1 = [2, 3, 4, 9, 1, 8, 6, 1]
    szamok2 = [3, 1, 4, 1, 5, 4, 7, 0]
    nagyobbszamok = 0
    for i in range[0, len(szamok1)]:
        if (szamok1[i] > szamok2[i]):
            nagyobbszamok = nagyobbszamok + szamok1[i]
        else:
            nagyobbszamok = nagyobbszamok + szamok2[i]
    return nagyobbszamok