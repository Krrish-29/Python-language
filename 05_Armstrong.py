x=input("Enter a number to check whether it is a Armstrong Number or not:")
armstrong=0
for i in x:
    armstrong+=int(i)**len(x)
if armstrong==int(x):
    print(f"{x} is a Armstrong Number")
else:
    print(f"{x} is not a Armstrong Number")
'''
for  n in range (0,100000):
    armstrong=0
    x=str(n)
    for i in x:
        armstrong+=int(i)**len(x)
    if armstrong==int(x):
        print(f"{x} is a Armstrong Number")
'''
