import random

guess = int(input('Adj meg egy random számot: '))
number = random.randint(1, 100)


while guess != number:
    if number > guess:
        print('nagyobb')
    else:
        print('kisebb')
    guess = int(input('Adj meg egy random számot: '))
else:
    print('nyertél')
    print (f'A gondolt szám: {number}')
