"""
sinusCosinus.py
Na samostatném algoritmu si vyzkoušej funkce sinus a cosinus pro hodnoty úhlu ve stupních, které zadá uživatel na vstupu.

vstup: úhel ve stupních
výstup: sinus a cosinus

1.) vstup
2.) výpočty
3.) výstup
"""
import math

uhel = float(input("Zadej úhel ve stupních: "))

# trigonometrické funkce pracují s úhly v radiánech!
uhelRadiany = math.radians(uhel)

# úhel v radiánech výpočtem -- trojčlenka:
# 180 stupňů ........ pi radiánů
# x stupňů .......... ? radiánů
# ? = (x * pi) / 180

uhelVypoctem = (uhel * math.pi) / 180
print(uhelVypoctem)
print("Úhel v radiánech:", uhelRadiany)
sinus = math.sin(uhelRadiany)
cosinus = math.cos(uhelRadiany)

print("Sinus:", sinus)
print("Cosinus:", round(cosinus, 2))