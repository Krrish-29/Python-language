#write a program to find the multiplication table of a given number
x=int(input("Enter a number to get its multiplication table:"))
for i in range (1,11):
    print(f"{x} X {i} = {x*i}")
