# Python lists are containers to store a set of values of any data type.Mutable and not hashable
l1 = [7,9,"harry"]
l1[0] # 7
l1[1] # 9
l1[70] # error
l1[0:2] # [7,9] #list slicing
'''l1.sort(): updates the list to [1,2,7,8,15,21]
l1.reverse(): updates the list to [15,21,2,7,8,1]
l1.append(8): adds 8 at the end of the list
l1.insert(3,8): This will add 8 at 3 index
l1.pop(2): Will delete element at index 2 and return its value.
l1.remove(21): Will remove 21 from the list. '''