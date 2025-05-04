s = input("Enter a string: ")
letters, digits = 0, 0
for char in s:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1

print(f"Letters: {letters}, Digits: {digits}")
