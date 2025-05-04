from collections import Counter

char_list = list(input("Enter characters (without spaces): "))
freq = Counter(char_list)
least_frequent = min(freq, key=freq.get)

print(f"Least frequent character: {least_frequent}")
