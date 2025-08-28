"""
smenarna.py
Příklad pro výpočet poplatku za směnu z CZK na EUR. Poplatek činí 1 % ze směňované částky, 
minimální výše poplatku je 50 Kč. Stanovte pevný kurz pro převod. Výstupem bude výše poplatku a počet EUR.

Př.:
vstup: částka = 3000 Kč
výpočet:
1 % ze 3000 = 30 Kč, ale min. výše poplatku je 50 Kč,
tzn. poplatek bude 50 Kč
převod 3000 / 25 = 120 €
výstup:
poplatek 50 Kč, po směně 120 €
"""


castka = float(input("Zadej částku v Kč: "))

poplatek = castka * 0.01
if poplatek < 50:
    poplatek = 50
kurz = 25
eura = (castka - poplatek) / kurz
print(f"Poplatek: {poplatek} Kč")
print(f"Po směně dostanete: {eura:.2f} €")

