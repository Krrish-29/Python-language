def uppercase_half(s):
    half = len(s) // 2
    return s[:half].lower() + s[half:].upper()

s = input("Enter a string: ")
print("Modified string:", uppercase_half(s))
