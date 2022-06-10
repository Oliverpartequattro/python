from tkinter import N


def etil_alcohol_weight(dl, percentage):
    return dl * (percentage) * 0.8

def menu():
    choice = 'n'
    while choice != '0' and choice != '1' and choice != '2' and choice != '3':
        print('Amivan')
        print('\t1...Sör') #5%
        print('\t2...Bor') #12%
        print('\t3...Pálinka') #52%
        print('\t0...Elég volt he') #0%
        choice = input('Mit iszuknk?:')

    if choice == '1':
        return 5
    if choice == '2':
        return 12
    if choice == '3':
        return 52
    if choice == '0':
        return 0

type = 1
alcohol_gramm = 0
while type != 0:
    type = menu()
    if type != 0:
        dl = int(input('Mennyiség (dl): '))
        alcohol_gramm = alcohol_gramm + etil_alcohol_weight(dl, type)

weight = int(input('Testsúly (kg):'))
alcohol_level = alcohol_gramm / weight
print(f'Véralkohol százalék: {alcohol_level}')


if alcohol_level < 0.3:
    print('majdnem józan')
elif alcohol_level < 0.5:
    print('jókedvű')
elif alcohol_level < 1.5:
    print('ittas')
elif alcohol_level < 2.5:
    print('részeg')
elif alcohol_level > 2.5:
    print('mekhalé')

