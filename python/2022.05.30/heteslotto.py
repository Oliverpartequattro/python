import random

Kihuzott_Szamok = [] #ureslista 

while len(Kihuzott_Szamok) < 7:
    huzas = random.randint(1, 35)
    if huzas not in Kihuzott_Szamok:
        Kihuzott_Szamok.append(huzas)




for szam in Kihuzott_Szamok:
    print(szam, end=' ')
   