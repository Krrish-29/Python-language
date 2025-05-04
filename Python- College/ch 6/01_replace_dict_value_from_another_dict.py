dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 20, "c": 30}
for key in dict2:
    if key in dict1:
        dict1[key] = dict2[key]
print(f"Dictionary 1 : {dict1}")  