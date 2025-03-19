#program to check if the given string is a palindrome or not
str=input("Enter a string to check if its a palindrome or not:")
for i in range (0,int(len(str)/2)):
    if str[i]!=str[len(str)-i-1]:
        i=-1
        break
if(i==-1):
    print("String is not a palindrome")
else:
    print("String is a palindrome")
'''
if str == str[::-1]:
    print("String is a palindrome")
else:
    print("String is a palindrome")
'''
