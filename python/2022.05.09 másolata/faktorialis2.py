for i in range(2, 11, 2):
    print(i)
print('kész')    

###############################
print('Faktoriális számítás')
n = int(input ('n = '))
faktor = 1
for i in range (2, n + 1):
    faktor = faktor * i #faktor *= i

print (f'{n}! = {faktor}')

