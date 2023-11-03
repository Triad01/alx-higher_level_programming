def uppercase(s):
    result = ""
    for char in s:
        # Check if the character is a lowercase letter (ASCII values between 97 and 122).
        if ord('a') <= ord(char) <= ord('z'):
            # Convert the lowercase character to uppercase (ASCII value difference is 32).
            result += chr(ord(char) - 32)
        else:
            result += char
    print(result)
