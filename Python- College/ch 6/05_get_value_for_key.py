data = {"a": 1, "b": 2, "c": 3}
value_to_find = int(input("Which dictionary value you require : "))
key_found = next((key for key, val in data.items() if val == value_to_find), None)

print(f"Key for value {value_to_find}: {key_found}")
