"""
castiCisla.py
Vytvoř algoritmus, který dle zadaného desetinného čísla vypíše jeho celou a desetinnou část. Použij dvě řešení – s a bez funkce knihovny math.

vstup: desetinné číslo
výstup: celá a desetinná číst čísla

1.) vstup, př. 6.2
2.) výpočet bez funkce:
6 = int(6.2)
0.2 = 6.2 - 6
výpočet s funkcí:
math.modf()
3.) výpis výsledku, př. 6.2 = 6 + 0.2
"""
import math

cislo = float(input("Zadej desetinné číslo: "))

cele1 = int(cislo)
desetinne1 = cislo - cele1
print(cislo, "=", cele1, "+", round(desetinne1, 2))

desetinne2, cele2 = math.modf(cislo)
# uložení hodnot do více proměnných
# vznikají tím n-tice (datový typ tuple)
desetinne2 = round(desetinne2, 2)

print(cislo, "=", cele2, "+", desetinne2)