import json

data = {"name": "John", "age": 30.5, "fruits": ["apple", "banana"]}

json_str = json.dumps(data)

print(json_str)
print(type(json_str))
