#write a  program to find the least frequent character in a string
def find_least_frequent_char(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    min_count = min(char_count.values())
    least_frequent_chars = [char for char, count in char_count.items() if count == min_count]
    return least_frequent_chars[0] if least_frequent_chars else None
string = "Hello, World!"
print(find_least_frequent_char(string))
