print('árpilis' , 8 , sep=' - ')

print('alma','fa' , sep='')

print('----------------------')
#típusok

x = 'szoveg'
print(x, type(x))
x = 12
print(x, type(x))
x = 3.14
print(x, type(x))
x = True    #False
print(x, type(x))

print('----------------------')
#műveletek

a = 1
b = 2
print(a + b, a / b,)

a = 'egy'
b = 'kettő'
print(a + b)
#print(a - b, a * b, a / b) --> nem tánogatott

a = 'egy'
b = 2
#print(a + b) #string és int között nem működik --> konvertálni kell
print(a + str(b))
#Konverzió másik oldalról

a = '1'
b = 2
print( int(a) + b)

print('----------------------')
#escape karakterek

print('tabulátorral elválasztva: 1\t2\t3\t4')
print('Könyvtár neve: C:\\Windows\\times')
print('Első sor\nMásodik sor')


