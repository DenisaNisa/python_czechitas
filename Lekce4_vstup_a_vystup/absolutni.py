"""
absolutni.py
Vytvoř algoritmus pro vyhodnocení absolutní hodnoty. Vstupem algoritmu bude celočíselná hodnota. Absolutní hodnotu vyhodnocuj bez užití funkce knihovny math.
"""

cislo = int(input("Zadej celé číslo: "))

if cislo < 0:
    absolutni = -cislo # když je číslo záporné, otočíme znaménko
else:
    absolutni = cislo # jinak necháme, jak je

print("Absolutní hodnota je:", absolutni)

