#write a program  that takes a character and return true if it is a vowel ,false other wise using function
def vowel(string):
    if 'a' in string or 'e'  in string or 'i' in string or 'o' in string or 'u' in string:
        return 1
    return 0
x=input("Enter a String:")
if len(x)!=1:
    print("Enter a single character")
else:
    print(f"{vowel(x.lower())}")
