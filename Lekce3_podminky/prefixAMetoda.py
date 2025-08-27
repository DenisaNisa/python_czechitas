"""
prefixAMetoda.py
Vyzkoušej si různé možnosti formátování hodnoty s prefixem f / metodou format. Pracuj s různými proměnnými pro text, celé a desetinné číslo, logickou hodnotu.
"""
import math

pi = math.pi
text = "Ahoj"
cislo = 123

# print("{0:2.2f} {1} {2:2.2f}".format (pi, text, cislo))
# print(f"{pi:2.2f} {text} {cislo:2.2f}")
print(f"{cislo:>010.2f}")
print(f"{cislo:>010.3f}")
print(f"{cislo:>010.4f}")

pravda = True
nepravda = False

print(f"{pravda:>10}")
print(f"{nepravda:>10}")