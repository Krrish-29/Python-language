data = {"a": 10, "b": 5, "c": 25, "d": 15}

max_key = max(data, key=data.get)
min_key = min(data, key=data.get)

print(f"Max value key: {max_key}, Min value key: {min_key}")
