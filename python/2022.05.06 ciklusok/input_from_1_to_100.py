def input_number_from_1_to_100():
    number = int(input('Szám (1-100):'))
    while number < 1 or number > 100:
        number = int(input('Szám (1-100):'))
    
    return number
    
number = input_number_from_1_to_100()
print (f'A megadott szám: {number}')

