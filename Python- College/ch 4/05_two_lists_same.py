list1 = input("Enter elements for first list (space-separated): ").split()
list2 = input("Enter elements for second list (space-separated): ").split()
print("True" if any(item in list2 for item in list1) else "False")
