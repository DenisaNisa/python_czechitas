"""
automat.py
Vytvoř program, který rozdělí částku na vstupu na mince nominálních hodnot 50, 20, 10, 5, 2, 1. 
Na stejném principu fungují automaty vracející zbývající částku po nákupu s tím rozdílem, že pracují v cyklu.

vstup: částka
výstup: počty minci CZK měny

1.) načtení vstupu
2.) postupné celočíselné dělení, zmenšování čísla o podělenou část
3.) výstupy počtu mincí
"""
castka = int(input("Zadej celočíselnou částku k rozdělení: "))
padesat = castka // 50
castka = castka % 50
dvacet = castka // 20
castka = castka % 20
deset = castka // 10
castka = castka % 10
pet = castka // 5
castka = castka % 5
dva = castka // 2
castka = castka % 2

print("50 *", padesat)
print("20 *", dvacet)
print("10 *", deset)
print("5 *", pet)
print("2 *", dva)
print("1 *", castka)