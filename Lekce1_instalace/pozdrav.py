"""
pozdrav.py
Vytvoř program, který uživateli vypíše pozdrav včetně jeho jména.
Jméno a příjmení uživatel zadá na začátku programu.  

vstupy: jméno, příjmení
výstupy: pozdrav včetně jména

1.) načtení dat od uživatele
2.) zpracování dat
3.) výpis pozdravu
"""

#jmeno = "Anička"
#prijmeni = 'Nováková'

jmeno = input("Zadej své jméno: ")
prijmeni = input("Zadej své příjmení: ")

celejmeno = jmeno + '' + prijmeni
pozdrav = "Ahoj " + celejmeno

print(pozdrav)

print(pozdrav * 3)
print(pozdrav / 3)
# řetězce = string (str)
# povolené operace: "+" (řetězení), "*" (znásobení)