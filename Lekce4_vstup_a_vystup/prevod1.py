"""
prevody1.py
Vytvoř algoritmus pro převod hodnoty zadané v GB na MB, KB, B a bity (dle SI).
"""

gb = float(input("Zadej velikost v GB: "))

mb = gb * 1000
kb = mb * 1000
B = kb * 1000
bity = B * 8

print(f"{gb} GB = {mb} MB")
print(f"{gb} GB = {kb} KB")
print(f"{gb} GB = {B} B")
print(f"{gb} GB = {bity} bitů")

