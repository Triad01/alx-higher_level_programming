#!/usr/bin/python3
def remove_char_at(s, n):
    if n < 0 or n >= len(s):
        return s  # No change if n is out of range

    # Use slicing to remove the character at position n
    result = s[:n] + s[n+1:]
    return result
