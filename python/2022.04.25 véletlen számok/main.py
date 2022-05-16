from asyncore import loop
import random

def diceRolling():

    firstDiceRoll = random.randint(1, 6)
    print(f'Első dobás: {firstDiceRoll}')

    if firstDiceRoll <= 2:
        print('\tVesztettxd')
    elif firstDiceRoll >= 5:
        print('\tNyert')
    else:
        secondDiceRoll = random.randint(1, 6)
        print(f'Második dobás: {secondDiceRoll}')
        if secondDiceRoll <= 4:
            print('\tNyert')
        else:
            print('\tVesztett')
#############################

#2.

def poker():
    color = random.randint(1, 4)
    if (color == 1):
        card = "Pikk"
    elif (color == 2):
        card = "Káró"
    elif (color == 3):
        card = "Kör"
    else:
        card = "Treff"

    figure = random.randint(1, 13) 
    if figure == 1:
        card = card + "A"
    elif figure <= 10:
        card = card + figure
    elif figure == 11:
        card = card + "J"
    elif figure == 12:
        card = card + "Q"
    else:
        card = card + "K"
    print(card)

        


print('1 - Kockadobás játék')
print('2 - Póker')

choice = int(input("Játék: "))
if choice == 1:
    diceRolling()
elif choice == 2:
    poker()    
else:
    print('Ilyen játék nálunk nincs!')
