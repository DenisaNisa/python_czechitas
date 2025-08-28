"""
zamena.py
Vytvoř příklad pro záměnu obsahu dvou proměnných. Vstupem jsou dvě celočíselné hodnoty, výstupem totéž. 
Řešení: s využitím pomocné proměnné, nebo postupným odečítáním.

Př.:
vstup: a = 5, b = 2
výstup: a = 2, b = 5
"""

a = 5
b = 2

a, b = b, a # prohození hodnot

print("a =", a, "b =", b)