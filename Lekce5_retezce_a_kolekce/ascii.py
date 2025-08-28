"""
ascii.py
Vypiš na monitor znaky standardní 7bitové ASCII tabulky; vedle čísla pozice bude znak.
Tip: výpis bez zalomení řádku:
print(a, end = '')
"""
for i in range(0, 128):
    print(f"{i}: {chr(i)}\t", end = "")