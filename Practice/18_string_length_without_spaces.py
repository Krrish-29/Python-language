#write a program to find the len of the string which avoids spaces
def string_length(string):
    return len(string)-string.count(" ")
x=input("Enter a string:")
print(f"The string length without any spaces is:{string_length(x)}")
