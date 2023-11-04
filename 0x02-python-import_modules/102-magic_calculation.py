#!/usr/bin/python3
def magic_calculation(a, b):
    if a < b:
        add = a + b
        for i in range(4, 6):
            add += i
        return add
    else:
        sub = a - b
        return sub
