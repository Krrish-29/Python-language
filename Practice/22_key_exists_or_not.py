#wap to check if  the given key already exists in a dictionary or not
dict={}
if dict.get('key1', 'not_found') == 'not_found':
    print("Key 'key1' does not exist.")
else:
    print("Key 'key1' exists.")
    
dict['new_key']
print(dict)
