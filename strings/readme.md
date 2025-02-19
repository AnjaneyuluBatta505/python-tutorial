# String Data Type in Python

* Strings are an essential part of programming, allowing us to store and manipulate text.
* In Python, a **string** is a sequence of characters enclosed in either single quotes (`'`), double quotes (`"`), or triple quotes (`'''` or """).
* Strings are widely used in applications such as text processing, data analysis, and user interactions.

## Creating Strings
We can create strings using different types of quotes:
```python
# Using single quotes
string1 = 'Hello'

# Using double quotes
string2 = "World"

# Using triple quotes for multi-line strings
string3 = '''This is 
a multi-line string.'''

print(string1)  # Output: Hello
print(string2)  # Output: World
print(string3)  # Output: This is a multi-line string.
```

## Accessing Characters in a String
Each character in a string has an index, starting from 0 for the first character.
```python
text = "Python"
print(text[0])  # Output: P (first character)
print(text[-1]) # Output: n (last character)
```

## String Slicing
We can extract parts of a string using slicing.
```python
word = "Programming"
print(word[0:4])  # Output: Prog (characters from index 0 to 3)
print(word[:5])   # Output: Progr (first 5 characters)
print(word[5:])   # Output: amming (characters from index 5 to end)
```

## String Concatenation
Strings can be combined using the `+` operator.
```python
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)  # Output: John Doe
```

## String Repetition
Strings can be repeated using the `*` operator.
```python
print("Hello " * 3)  # Output: Hello Hello Hello
```

## String Methods
Python provides many built-in methods to manipulate strings.
```python
text = "python programming"
print(text.upper())     # Output: PYTHON PROGRAMMING
print(text.lower())     # Output: python programming
print(text.title())     # Output: Python Programming
print(text.replace("python", "Java"))  # Output: Java programming
print(text.split())     # Output: ['python', 'programming']
```

## Checking String Length
Use `len()` to get the length of a string.
```python
message = "Hello, World!"
print(len(message))  # Output: 13
```

## String Formatting
Python provides different ways to format strings.
```python
name = "Alice"
age = 16
print(f"My name is {name} and I am {age} years old.")  # Output: My name is Alice and I am 16 years old.
```

## String Methods
Python provides various built-in string methods. The table below summarizes common string methods with examples:

| Method | Description | Example |
|--------|-------------|---------|
| `upper()` | Converts string to uppercase | `'hello'.upper()` → `'HELLO'` |
| `lower()` | Converts string to lowercase | `'HELLO'.lower()` → `'hello'` |
| `title()` | Capitalizes first letter of each word | `'hello world'.title()` → `'Hello World'` |
| `capitalize()` | Capitalizes the first letter of the string | `'python'.capitalize()` → `'Python'` |
| `strip()` | Removes whitespace from both ends | `' hello '.strip()` → `'hello'` |
| `lstrip()` | Removes whitespace from the left | `' hello '.lstrip()` → `'hello '` |
| `rstrip()` | Removes whitespace from the right | `' hello '.rstrip()` → `' hello'` |
| `replace()` | Replaces a substring with another | `'hello world'.replace('world', 'Python')` → `'hello Python'` |
| `split()` | Splits a string into a list | `'a,b,c'.split(',')` → `['a', 'b', 'c']` |
| `join()` | Joins elements of a list into a string | `'-'.join(['a', 'b', 'c'])` → `'a-b-c'` |
| `find()` | Finds the first occurrence of a substring | `'hello'.find('l')` → `2` |
| `count()` | Counts occurrences of a substring | `'hello'.count('l')` → `2` |
| `startswith()` | Checks if string starts with a given substring | `'hello'.startswith('he')` → `True` |
| `endswith()` | Checks if string ends with a given substring | `'hello'.endswith('lo')` → `True` |
| `isalpha()` | Checks if string contains only letters | `'Hello'.isalpha()` → `True` |
| `isdigit()` | Checks if string contains only digits | `'123'.isdigit()` → `True` |
| `isalnum()` | Checks if string contains only letters and numbers | `'Hello123'.isalnum()` → `True` |
| `isspace()` | Checks if string contains only whitespace | `'   '.isspace()` → `True` |
