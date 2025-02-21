# Dictionary (dict) Data Type in Python

* A **dictionary** in Python is an unordered collection of key-value pairs.
* Unlike lists or tuples, which are indexed by numerical positions, dictionaries are indexed by unique **keys**.
* Dictionaries are highly efficient for retrieving values based on their keys, making them a fundamental data structure in Python.

## What is a Dictionary?
A dictionary is defined using **curly braces `{}`** with keys and values separated by colons `:`. The general syntax is:

```python
dict_name = {key1: value1, key2: value2, key3: value3}
```

### Example of Creating a Dictionary:
```python
student = {
    "name": "Alice",
    "age": 17,
    "grade": "A"
}
print(student)
# Output: {'name': 'Alice', 'age': 17, 'grade': 'A'}
```

## Accessing Dictionary Elements
You can access dictionary values using their keys:

```python
print(student["name"])  # Output: Alice
print(student.get("age"))  # Output: 17
```

## Adding and Modifying Dictionary Elements
You can add new key-value pairs or update existing ones:

```python
student["school"] = "High School"  # Adding a new key-value pair
student["grade"] = "A+"  # Modifying an existing value
print(student)
# Output: {'name': 'Alice', 'age': 17, 'grade': 'A+', 'school': 'High School'}
```

## Removing Elements from a Dictionary
You can remove elements using the `del` statement or dictionary methods:

```python
del student["age"]  # Removes the 'age' key
print(student)
# Output: {'name': 'Alice', 'grade': 'A+', 'school': 'High School'}
```

## Dictionary Methods
Python provides various built-in methods to work with dictionaries efficiently.

| Method | Description | Example | Result |
|--------|-------------|---------|--------|
| `keys()` | Returns all keys in the dictionary | `student.keys()` | `dict_keys(['name', 'grade', 'school'])` |
| `values()` | Returns all values in the dictionary | `student.values()` | `dict_values(['Alice', 'A+', 'High School'])` |
| `items()` | Returns key-value pairs as tuples | `student.items()` | `dict_items([('name', 'Alice'), ('grade', 'A+'), ('school', 'High School')])` |
| `get(key, default)` | Retrieves a value by key, returns `default` if key is missing | `student.get('age', 'N/A')` | `'N/A'` |
| `pop(key, default)` | Removes key and returns its value; returns `default` if missing | `student.pop('grade', 'Not Found')` | `'A+'` |
| `popitem()` | Removes and returns the last inserted key-value pair | `student.popitem()` | `('school', 'High School')` |
| `update(dict2)` | Updates dictionary with another dictionary | `student.update({'age': 18})` | `{'name': 'Alice', 'grade': 'A+', 'age': 18}` |
| `clear()` | Removes all elements from the dictionary | `student.clear()` | `{}` |
| `copy()` | Returns a shallow copy of the dictionary | `student.copy()` | `{'name': 'Alice', 'grade': 'A+', 'school': 'High School'}` |

## When to Use Dictionaries?
- When you need to store **key-value pairs**.
- When you need **fast lookups** based on unique keys.
- When data is **unordered** but needs to be structured and easily accessible.
