"""
posudek.py
Vytvořte algoritmus pro posouzení, zdali lze dvě vložené celočíselné hodnoty dělit beze zbytku. 
Výstupem programu bude jeden ze dvou stavů: lze dělit beze zbytku, nelze dělit beze zbytku.
"""

a = int(input("Zadej první celé číslo: "))
b = int(input("Zadej druhé celé číslo: "))

if b == 0:
    print("Nulou dělit nelze!")
elif a % b == 0:
    print("Lze dělit beze zbytku.")
else:
    print("Nelze dělit beze zbytku.")