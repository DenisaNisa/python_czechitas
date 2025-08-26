"""
jablka.py
Vytvoř program, který rozdělí daný počet jablek mezi daný počet dětí. Jablka lze dávat pouze celá, nikoliv jejich části (poloviny, čtvrtiny…).

vstup = počet jablek, počet dětí (celá čísla)
výstup = počet jablek / 1 dítě, zbytek

1.) načtení vstupů
2.) výpočet
3.) výstup výsledků
"""

jablka = int(input("Zadej počet jablek: "))
deti = int(input("Zadej počet dětí: "))

#podíl = jablka // deti
#zbytek = jablka % deti

podil, zbytek = jablka // deti, jablka % deti
# Python dokáže ukládat více hodnot do více proměnných
# vznikají tím tzv. n-tice (datový typ tuple)

print()
print("Na 1 dítě vychází", podil, "jablek.")
print("Zůstane mi", zbytek, "jablek.")