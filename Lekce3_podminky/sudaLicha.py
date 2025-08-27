"""
sudaLicha.py
Vytvoř program, který dle zadaného čísla vyhodnotí, zdali je sudé či liché.

vstup: číslo
výstup: sudá/lichá

sudá čísla jsou dělitelná 2 beze zbytku, tzn. zbytek po dělení číslem 2 je roven nule zbytek = číslo % 2
když zbytek == 0, tak číslo je sudé
jinak je číslo liché
"""

cislo = int(input("Zadej celé číslo: "))

if cislo % 2 == 0:
    print("Číslo je sudé.")
else:
    print("Číslo je liché.")