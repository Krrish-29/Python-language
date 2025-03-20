#write a program that takes two lists and return true if they have atleast one common number
def has_common_element(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    for element in set1:
        if element in set2:
            return True
    return False
list1 = [1, 3, 5, 7]
list2 = [2, 3, 6, 8]
print(has_common_element(list1, list2)) 
list1 = [1, 3, 5, 7]
list2 = [3, 9, 15, 21]
