"""
hexadec.py
S pomocí lektora vytvoř program, který v cyklu vypíše 0. až 15. hodnotu hexadecimální číselné soustavy.
Bude se jednat o čísla 0–9 a písmena A–F, tedy obsazenost 4 bitů (24 = 16, tzn. 16 možností variant, tj. hodnoty 0 až 15).
"""

for i in range(0, 16):
    print("%X " % i, end = "")