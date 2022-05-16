from tkinter import N


def fibonacci(count):
    if count ==1:
        return 1
    if count ==2:
        return 1
    previous = fibonacci(count - 1)
    before_previous = fibonacci(count - 2)
    return previous + before_previous

print(fibonacci(10))