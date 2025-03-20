#write a function to print the factorial of a given number using recusion
def factorial(number):
    if(number==0):
        return 1
    return factorial(number-1)*number
x=int(input("Enter the Number to get its Factorial"))
print(f"Factorial of number {x} is {factorial(x)}")
