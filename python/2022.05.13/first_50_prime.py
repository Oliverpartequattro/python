import math
from multiprocessing.dummy import current_process

def is_prime(number):
    for divider in range(2, int(math.sqrt(number)) + 1):
        if number % divider == 0:   # '%' jel maradékos osztásnál a maradék
            return False
    return True

count = 0
current_number = 2
while count < 5000:
    if is_prime(current_number):
        print(current_number, end=', ')
        count += 1
    current_number += 1
    

