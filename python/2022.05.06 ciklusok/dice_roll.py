# Anna és Béla társasoznak, az lép először, aki először 6-ost dob
# Feladat: szimuláljuk le a kockadábást, 
# kérdés ki lép először

import random

Anna = random.randint(1, 6)
Bela = random.randint(1, 6)
print(f'1. dobás: Anna: {Anna}, Béla: {Bela}')
count = 1

while Anna != 6 and Bela != 6:
    count += 1
    Anna = random.randint(1, 6)
    Bela = random.randint(1, 6)
    print(f'1. dobás: Anna: {Anna}, Béla: {Bela}')

if Anna == 6 and Bela == 6:
    print('Mindketten 6-ost dobtak')
elif Anna == 6:
    print('Csak Anna dobott 6-ost')
else:
    print('Csak Béla dobott 6-ost')