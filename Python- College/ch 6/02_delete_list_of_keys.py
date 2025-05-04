data = {"a": 10, "b": 20, "c": 30, "d": 40}
keys_to_delete = ["b", "c"]
for key in keys_to_delete:
    data.pop(key, None)
print(f"Deleted data : {data}") 
