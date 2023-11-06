#!/usr/bin/python3
for char in range(ord('z'), ord('A') - 1, -1):
    if char % 2 == 0:
        print(chr(char), end='')
    else:
        print(chr(char).upper(), end='')
