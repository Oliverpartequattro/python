import math

def is_prime(number):
    divider = 2
    while divider <= math.sqrt(number):
        if number % divider == 0: #%jel: a maradékos osztásnál a maradék
            print('nme prime')
            return False
        divider += 1
    print('Prime')
    return True

number = int(input('Kérekegy egész számot:'))
is_prime(number)