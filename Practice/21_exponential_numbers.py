#wap to find a expontial of number
def exponent(base, exponent):
    return base**exponent
number = int(input("Enter the number : "))
power =int(input("Enter the power : "))
result = exponent(number, power)
print(f'The result is: {result}')
