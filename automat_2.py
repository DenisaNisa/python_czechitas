castka = int(input("Zadej částku k rozdělení: "))

mince = [50, 20, 10, 5, 2, 1]   # nominály mincí v Kč
for m in mince:
    pocet = castka // m         # kolik mincí tohoto druhu
    castka = castka % m         # kolik peněz zbývá rozměnit
    if pocet > 0:               # vypíšeme jen když něco použijeme
        print(m, "Kč *", pocet)
