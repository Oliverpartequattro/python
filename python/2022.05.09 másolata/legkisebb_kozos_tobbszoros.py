print('Legkisebb közös többszörös meg6ározása')

a = int(input('a = '))
b = int(input('b = '))
if a > b:
    nagyobb = a
    kisebb = b
else:
    nagyobb = b 
    kisebb = a

osztando = nagyobb
while osztando % kisebb != 0:
    osztando = osztando + nagyobb