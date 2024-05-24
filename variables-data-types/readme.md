# Python - Variable and data types

#### Variables in Python

* A variable in Python is a named location used to store data in memory.
* It's a fundamental concept that allows developers to store, modify, and retrieve data.
* Unlike some programming languages, Python does not require explicit declaration of variable types, making it dynamically typed.

##### Creating Variables

To create a variable in Python, you simply assign a value to a variable name using the equals sign (`=`). For example:

```python
x = 5
name = "Alice"
pi = 3.14
is_valid = True
```

In the examples above:

*   `x` is an integer variable.
*   `name` is a string variable.
*   `pi` is a floating-point variable.
*   `is_valid` is a boolean variable.

##### Naming Conventions

Variable names in Python should follow certain rules:

*   They must start with a letter or an underscore (`_`).
*   They can be followed by letters, numbers, or underscores.
*   They are case-sensitive (`Age`, `age`, and `AGE` are different variables).

It's also good practice to use descriptive names for variables to make the code more readable. For example, `student_name` is more informative than `sn`.

#### Data Types in Python

Data types specify the type of data that a variable can hold. Python provides several built-in data types, and it also allows for custom data types. Let's explore some of the primary built-in data types.

##### Numeric Types

1.  **Integers (`int`)**: Integers are whole numbers, positive or negative, without decimals. Examples include `-10`, `0`, and `42`.
    
    ```python
    age = 30
    ```
2.  **Floating-Point Numbers (`float`)**: Floating-point numbers are numbers with decimal points. Examples include `3.14`, `-0.001`, and `2.0`.
    ```python
    temperature = 98.6
    ```
3.  **Complex Numbers (`complex`)**: Complex numbers have a real part and an imaginary part, denoted by `j` in Python.

    ```python
    z = 2 + 3j
    ```

##### Sequence Types

1.  **Strings (`str`)**: Strings are sequences of characters enclosed in single, double, or triple quotes.
    
    ```python
    message = "Hello, World!"
    ```
    
3.  **Lists (`list`)**: Lists are ordered collections of items, which can be of different data types. They are mutable, meaning they can be changed after creation.
    
    ```python
    fruits = ["apple", "banana", "cherry"]
    ```
    
5.  **Tuples (`tuple`)**: Tuples are similar to lists but are immutable, meaning they cannot be changed after creation.
    
    ```python
    coordinates = (10, 20)
    ```

##### Mapping Type

*   **Dictionaries (`dict`)**: Dictionaries are unordered collections of key-value pairs. They are mutable and indexed by keys.
    
    ```python
    student = {"name": "Alice", "age": 23, "grade": "A"}
    ```

##### Set Types

1.  **Sets (`set`)**: Sets are unordered collections of unique items. They are mutable.
    
    ```python
    unique_numbers = {1, 2, 3, 4}
    ```
    
2.  **Frozen Sets (`frozenset`)**: Frozen sets are immutable sets.
    
    ```python
    immutable_set = frozenset([1, 2, 3, 4])
    ```
    

##### Boolean Type

*   **Booleans (`bool`)**: Booleans represent one of two values: `True` or `False`.
    
    ```python
    is_active = True
    ```

##### None Type

*   **NoneType**: This type has a single value, `None`, used to represent the absence of a value.
    
    ```python
    result = None
    ```

#### Type Conversion

Python allows for type conversion, also known as typecasting. This is useful when you need to convert a value from one data type to another. Here are some common type conversions:

```python
x = 5         # int
y = float(x)  # convert int to float
z = str(x)    # convert int to string
a = "123"
b = int(a)    # convert string to int`
