from email.mime import image


primek = [2, 3, 5, 7, 11, 13, 17, 19, 4444444444444444]

for i in primek:
    print(i)

print (f'A 3. primszam: {primek[2]}')

primek[7] = 19
print(primek[7])

primek.append(23)
print(primek[9])

print(f'A lista hossza: {len(primek)}')

print('Prsizmasmm ellentzrozes kezdo modon')
szam = int(input('Szám ='))
if (szam > 23):
    print('idkxd')
elif szam in primek:
    print('Prim ja')
else:
    print('nm prim')