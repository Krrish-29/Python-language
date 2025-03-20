#find max in a list
nums = list(map(int, input().split()))
if not nums:
    print("Error: The list is empty.")
else:
    print(max(nums)) 
