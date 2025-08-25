"""
ctverec.py
Vytvoř program pro výpočet obvodu a obsahu čtverce.
Délku strany čtverce zadá uživatel na začátku programu.  

vstup: délka strany čtverce
výstup: obvod a obsah čtverce

1.) načtení dat od uživatele
2.) výpočet
3.) výstup výsledku na monitor
"""

#vložíme vstupy od uživatele
a = input("Zadej délku strany čtverce: ")
#int = integer = celé číslo
# je třeba převést string -> integer
# float = desetinná čísla, zapisujeme s desetinnou tečkou

a = float(a)

o = a * 4 # výpočet obvodu
S = a ** 2 # výpočet obsahu

print("Obvod čtverce: ", o)
print("Obsah čtverce: ", S)