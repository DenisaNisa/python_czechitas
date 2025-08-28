"""
inicialy.py
Do jedné proměnné načti jméno a příjmení. Vypiš iniciály uživatele. Vypiš jméno a příjmení malými písmeny (minuskule, mínusky), velkými písmeny (majuskule, verzálky), vyzkoušej různé kombinace. Načti věk uživatele jako řetězec. Když bude obsahovat číslice, převeď jej na celé číslo, jinak vypiš chybovou hlášku. Věk vypiš na monitor spolu s datovým typem.
Vyzkoušej si metody center(), ljust(),
zfill(), rjust()
"""
celeJmeno = "Jan Novák"
jmeno, prijmeni = celeJmeno.split(" ")
# print(jmeno)
# print(prijmeni)

inicialy = jmeno[0] + prijmeni[0]
print(f"Iniciály: {inicialy}")

print(f"Minuskule: {jmeno.lower()} {prijmeni.lower()}")
print(f"Majuskule: {jmeno.upper()} {prijmeni.upper()}")

vek = input("Zadej věk uživatele: ")

if vek.isdigit():
    vek = int(vek)
    print(f"Věk: {vek}, datový typ: {type(vek)}")
else:
    print("Nebylo zadáno číslo.")

print(celeJmeno.center(30))
print(celeJmeno.rjust(30))