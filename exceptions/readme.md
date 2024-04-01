# Python3 - exceptions

* `exception` - an error detected during execution
* when an exception occurs then the program stops the execution

## built-in exceptions

1. **`SyntaxError`** : Raised when there is a syntax error in the code.
2. **`IndentationError`** : Occurs when there is incorrect indentation in the code.
3. **`NameError`** : Raised when a local or global name is not found.
4. **`TypeError`** : Occurs when an operation or function is applied to an object of an inappropriate type.
5. **`ValueError`** : Raised when a built-in operation or function receives an argument with the correct type but an inappropriate value.
6. **`FileNotFoundError`** : Raised when an attempt is made to open a file that does not exist.
7. **`IOError`** : Generally raised for I/O-related errors.
8. **`IndexError`** : Raised when a sequence subscript is out of range.
9. **`KeyError`** : Raised when a dictionary key is not found.
10. **`ZeroDivisionError`** : Raised when division or modulo by zero is encountered.
11. **`AttributeError`** : Raised when an attribute reference or assignment fails.
12. **`ImportError`** : Raised when an import statement fails to find the specified module.
13. **`RuntimeError`** : Raised when an error is detected that doesn't fall into any of the other categories.
14. **`MemoryError`** : Raised when an operation runs out of memory.
15. **`OverflowError`** : Raised when the result of an arithmetic operation is too large to be represented.

* **`Exception`**  - is the base class for all python exceptions

## example

```python
# syntax error
a = 10
a++
# zero division error
result = 10/0
```

## handling the exceptions

```python
try:
    ...
except Exception:
    ...
else:
    ...
finally:
    ...
```

### **Basic Try-Except Block**

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Can't divide number by zero")
```

### Handling Multiple Exceptions

```python
num = input("Number: ")
try:
    value = int(num)
    result = 100 / value
except (ValueError, ZeroDivisionError):
    print("Error: Invalid value")
```

### `else`  clause with `try...except...`

```python
num1 = input("Number1: ")
num2 = input("Number1: ")
try:
    result = float(num1) / float(num2)
except (ValueError, ZeroDivisionError):
    print("Error: Invalid value")
else:
    print("result: ", result)

```

### `finally`  clause with `try...except...`

```python
import sqlite3

database_file = 'database.db'

try:
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()
    result = cursor.execute("select 1+1;")
    print(result.fetchone())
except sqlite3.Error as e:
    print(f"Database Error: {e}")
finally:
    if connection:
        connection.close()
        print("Database connection closed.")
```

## Custom Exceptions

* base class for custom exception is Exception

```python
class GradeError(Exception):
    pass

def validate_grade(value):
    if not (0 <= value <= 100):   
        raise GradeError("Grade value should be between 0 and 100")
    return value
```
