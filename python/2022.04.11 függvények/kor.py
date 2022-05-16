import math

def InputNumber(text11):
    data = input(text11)
    number = float(data)
    return number

# def Kerület(r,):
#     s = (a + b + c) / 2
 
#     return math.sqrt(x)


print('Oldalai:')
r = InputNumber('r=')

print('K =' , 2 * r * 3.14)
print('T =' , 3.14 * r * r) 