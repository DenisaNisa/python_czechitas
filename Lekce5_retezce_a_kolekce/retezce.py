"""
retezce.py
Ulož do proměnné řetězec, zjisti jeho délku, vypiš jeho první a poslední znak.
"""
import time

s = "řetězec"

delka = len(s)
print(f"Délka řetězce je {delka} znaků.")

print(f"První znak řetězce: {s[0]}")
print(f"Druhý znak řetězce: {s[1]}")
print(f"Třetí znak řetězce: {s[2]}")
print(f"Poslední znak řetězce: {s[delka - 1]}")

for i in range(0, delka):
    print(s[i])
    time.sleep(1)