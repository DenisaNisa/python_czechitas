"""
obdelnik.py
Vytvoř program pro výpočet obvodu a obsahu obdélníka.
Délky stran obdélníka zadá uživatel na začátku programu.  

vstupy: délka stran obdélníka (a, b)
výstup: obvod a obsah obdélníka

1.) načtení dat ze vstupu
2.) výpočet
3.) výstup dat na monitor
"""

a = input("Zadej délku strany a: ")
b = input("Zadej délku strany b: ")

a = float(a)
b = float(b)

o = 2 * (a + b)
S = a * b 

print("Obvod:", o, "\tObsah:", S)

# zalomení řádku: \n
# tabulátor: \t