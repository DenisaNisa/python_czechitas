"""
prevody2.py
Vytvoř algoritmus pro převod hodnoty zadané v m na mm, dm, km (dle SI).
Použij výpis čísla v exponenciálním tvaru.
"""

m = float(input("Zadej délku v m: "))

mm = m * 1000
dm = m * 10
km = m / 1000

print(f"{m} M = {mm} mm")
print(f"{m} M = {dm} dm")
print(f"{m} M = {km} km")