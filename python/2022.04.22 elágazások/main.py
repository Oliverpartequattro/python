#1. Abs() függvény -> abszolút értéket számol
#2. Megadott értékek alapján számoljuk ki, 
#hogy a vizsgázók hány százaléka felelt meg.
##########################################################

#1.
from cProfile import run
import math


def abs(number):
    if (number >= 0):
        return number
    return number * -1

def abs_test():
    x = float (input('Kérem a számot!'))
    print('A megadott szám abszolút értéke:', abs(x))
##########################################################

#2.
def success_test(): 
    candidates = int(input('Kérema vizsgázók számát:'))
    success = int(input('Sikeresen vizsgázottak száma:'))
    if success > candidates or success == 0 or candidates == 0:
        print('Szerencsétlen') 
    else:
        print(f'Sikerességi ráta: { (success / candidates) * 100 }  %')
##########################################################

#3.

def triangle_test():
    a = float( input("a = "))
    b = float( input("b = "))
    c = float( input("c = "))
    if a + b > c and a + c > b and b + c > a:
        print("A háronszög szerkeszthetőxd")
    else:
        print("Hamiságot kaptunk")
##########################################################

#4.

def grading_test():
    totalPoints = int( input("A dolgozat összpontszáma: "))
    minPointsFor5 = math.floor(totalPoints * 0.85 + 0.5)
    minPointsFor4 = math.floor(totalPoints * 0.70 + 0.5)
    minPointsFor3 = math.floor(totalPoints * 0.55 + 0.5)
    minPointsFor2 = math.floor(totalPoints * 0.40 + 0.5)
    print('Ponthatárok: ')
    print(f'\tJeles:     {minPointsFor5} - {totalPoints}')
    print(f'\tJó:        {minPointsFor4} - {minPointsFor5 - 1}')
    print(f'\tKözepes:   {minPointsFor3} - {minPointsFor4 - 1}')
    print(f'\tElégséges: {minPointsFor2} - {minPointsFor3 - 1}')
    print(f'\tElégtelen: 0 - {minPointsFor2 - 1}')

    points = int( input('Pistike pontszáma: ') )
    if points > minPointsFor5:
        print('\tJeles')
    elif points > minPointsFor4:
        print('\tJó')
    elif points > minPointsFor3:
        print('\tKözepes')
    elif points > minPointsFor2:
        print('\tElégséges')
    else:   
        print('\tElégtelen')


print('1. Abszolútérték számítás')
print('2. Százalék számítás')
print('3. Háronszög szerkeszthetőseég')
print('4. Dolgozat osztályzása')
choice = int(input('Válaszá: '))
if choice == 1:
    abs_test()
elif choice == 2:
    success_test()
elif choice == 3:
    triangle_test()
elif choice == 4:
    grading_test()
else:
    print('Ijen nics xd')

"""
if choice == 1:
    abs_test()
else:
    if choice == 2:
        percent_test()
    else:       
        print('Nem létező funkció!')
"""
