"""
dedictvi.py
Vytvoř algoritmus pro rozdělení majetku mezi libovolný počet potomků. Hodnota majetku bude zadána v CZK. 
Výstupem programu bude celočíselná částka v CZK připadající na 1 potomka, a nerozdělený zbytek v CZK.
"""

majetek = int(input("Zadej hodnotu majetku v CZK: "))
potomci = int(input("Zadej počet potomků: "))

na_potomka = majetek // potomci # kolik dostane každý potomkem (jen celé Kč)
zbytek = majetek % potomci # co se už nerozdělí rovnoměrně

print("Na jednoho potomka připadá:", na_potomka, "CZK")
print("Nerozdělený zbytek je:", zbytek, "CZK")