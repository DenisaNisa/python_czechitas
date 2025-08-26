"""
faktorial.py
Na samostatném algoritmu si vyzkoušej funkci pro výpočet faktoriálu vloženého přirozeného čísla. Vstup přirozeného čísla ošetři podmínkou.

vstup: přírozené číslo
výstup: faktoriál

1.) načtení hodnoty, kontrola, zdali je číslo
celé a kladné
2.) výpočet
3.) výstup výsledku
"""
import math

cislo = int(input("Zadej celé kladné číslo: "))

if cislo > 0:
   faktorial = math.factorial(cislo)
   print(str(cislo) + "! = " + str(faktorial))
else:
   print("Nebylo zadáno celé kladné číslo.")

   """
   zde je důležité mít určité odsazení od kraje, co se týče funkce "if" - při učebním materiálu byly všechny řádky
   zarovnány na stejné úrovni. - to mi ukazovalo chybu a kod byl nefunkční
   """