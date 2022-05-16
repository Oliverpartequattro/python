#Feladat: kérje be egy háromszög 3 oldalának hosszát
#Feltételezheti, hogy a 3szög szeekszthető
#T,K kiszámolása

import math

def InputNumber(text11):
    data = input(text11)
    number = float(data)
    return number

def heron(a, b ,c):
    s = (a + b + c) / 2
    x = s * (s - a) * (s - b) * (s - c)    
    return math.sqrt(x)


print('Oldalai:')
a = InputNumber('a=')
b = InputNumber('b=')
c = InputNumber('c=')
print('K =' , a + b + c)
print('T =' , heron(a, b, c)) 