"""
trida.py
Ve třídě je x dívek a y chlapců; vytvoř algoritmus pro vyjádření procentuálního podílu dívek a chlapců.""" 

x = int(input("Zadej počet dívek: "))
y = int(input("Zadej počet chlapců: "))

celkem = x + y
podil_d = (x/celkem) * 100
podil_ch = (y/celkem) * 100

print(f"Podíl dívek je {podil_d}%")
print(f"Podíl chlapců je {podil_ch}%")