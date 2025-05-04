p = float(input("Enter Principal Amount: "))
r = float(input("Enter Rate of Interest (%): "))
t = float(input("Enter Time (years): "))
CI = p * ((1 + r / 100) **t) -p
print("Compound Interest:", CI)
