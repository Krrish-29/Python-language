n=int(input(("Enter the number to get fibonacci seires till the number:")))
y=1
z=1
while 1:
    if n<=0:
        n=int(input(("Enter a Valid number to get fibonacci seires till the number:")))
    else :
        for i in range (0,n):
            temp=y
            print(temp)
            y=z
            z+=temp
        break