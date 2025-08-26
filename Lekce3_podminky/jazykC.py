"""
jazykC.py
Vyzkoušej si různé možnosti formátování hodnoty pí.
S pomocí lektora vytvoř program, který v cyklu vypíše 0. až 10. mocninu čísla 10 formátovaně zarovnanou vpravo.
"""
import math
"""
pi = math.pi

print("%f" % pi)
print("%.2f" % pi)
print("%10.2f" % pi)
print("%10.3f" % pi)
print("%10.4f" % pi)
"""

for i in range(0, 11):
 mocnina = pow(10, i)
print("%012.0f" % mocnina)