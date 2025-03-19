#write a program to check the validity of a password input by the user len>=8,len<=16, 1 lowercase and 1 uppercase alphabet 1 digit and 1 special symbol
x=input("Enter a password:")
uppercount=lowercount=specialcount=digitcount=0
for i in x:
    if i>='A' and  i<='Z':
        uppercount+=1
    elif i>='a' and i<='z':
        lowercount+=1
    elif i>='1' and  i<='9':
        digitcount+=1
    else:
        specialcount+=1
if uppercount>=1 and lowercount>=1 and digitcount>=1 and specialcount>=1 and len(x)>=8 and len(x)<=16:
    print("Valid Password")
else:
    print("Invalid Password")
    
