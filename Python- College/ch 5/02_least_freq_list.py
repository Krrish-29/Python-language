char_list = list(input("Enter characters (without spaces): "))
freq = {}
for char in char_list:
    freq[char] = freq.get(char, 0) + 1
least_frequent = min(freq, key=freq.get)
print(f"Least frequent character: {least_frequent}")