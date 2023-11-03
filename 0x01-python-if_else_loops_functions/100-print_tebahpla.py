#!/usr/bin/python3
for char_code in range(ord('z'), ord('a') - 1, -1):
    char = chr(char_code)
    if (char_code - ord('z')) % 2 == 0:
        # Print lowercase character
        print(char, end='')
    else:
        # Print uppercase character
        print(char.upper(), end='')
print()
