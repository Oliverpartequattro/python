
print('1 1', end=' ')
count = 2
previous = 1
before_previous = 1
while count < 400:
    next = previous + before_previous
    count = count + 1
    print (next, end=' ')
    before_previous = previous
    previous = next