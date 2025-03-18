#Factorial
print("Enter a number to get its factorial")
i=int(input("Number:"))
fact=1
for x in range (i,0,-1):
    fact*=x
print(f"The factorial of {i} is : {fact}")
