print("Enter two number for comparison")
a=int(input("1ST Number:"))
b=int(input("2Nd Number:"))
c=int(input("3rd Number:"))
if a>b and a>c:
    print(f"a :{a} is greater than b:{b} and c:{c} both.")
elif b>c and b>a :
    print(f"b:{b} is greater than a:{a} and c:{c} both.")
else :
    print(f"c:{c} is greater than a:{a} and b:{b} both.")