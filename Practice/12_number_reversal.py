#write a program that reverses user defined value using function
def reverse_number(number):
    x=str(number)
    return x[::-1]
num=int(input("Enter a number:"))
print(reverse_number(num))
