#wap to print the sum of key value pair in the dictionary.
my_dict = {'5': 10, '15': 20}
def sum(dictionary):
    total = 0
    for key, value in dictionary.items():
        total +=( value+(int(key)))    
    return total
print(sum(my_dict))
