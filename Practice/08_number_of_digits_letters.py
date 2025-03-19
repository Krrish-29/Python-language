#write a program that accepts a string and calculate the number of  digits and letters
x=input("Enter a string:")
digitcount=lettercount=0
for i in x:
    if i>='1' and i<='9':
        digitcount+=1
    elif (i>='a' and i<='z')or(i>='A' and i<='Z'):
        lettercount+=1
print(f"The number of letters are {lettercount} and digits {digitcount}")
