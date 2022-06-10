import random

def dobas():
    ertek = random.randint(1, 20)
    if random.randint(1, 10) == 1:
        ertek = ertek * 3
    elif random.randint(1, 5) == 1:
        ertek = ertek * 2
    print(f'\tDobás: {ertek}')
    return ertek

def sorozat(pontszam):
    dobas_1 = dobas()
    if pontszam - dobas_1 == 0:
        return dobas_1
    if pontszam - dobas_1 < 0:
        return 0

    dobas_2 = dobas()
    if pontszam - dobas_1 - dobas_2 == 0:
        return dobas_1 + dobas_2
    if pontszam - dobas_1 - dobas_2 < 0:
        return 0

    dobas_3 = dobas()
    if pontszam - dobas_1 - dobas_2 - dobas_3 < 0:
        return 0
    return dobas_1 + dobas_2 + dobas_3

pontszam = 501
i = 1
while pontszam > 0:
    print(f'{i}. sorozat')
    print(f'\tInduló pontszám: {pontszam}')
    dobasok = sorozat(pontszam)
    pontszam = pontszam - dobasok
    print(f'\tBefejezés: {pontszam}')
    print('')
    i = i + 1