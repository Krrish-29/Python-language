#calculate the number of digits in a number
y=x=int(input("Enter a number:"))
z=0
while y>0:
    y=int(y/10)
    z+=1 
print(f"The number {x} has {z} digits in it")
