# Python - Modules and Packages

## Module

* Modules are reusable pieces of code containing functions, classes, and variables.
* in smple terms it's a python file
* Benefits:

  * Encapsulation
  * Code organization
  * Reusability
* python buit-in modules: `datetime`, `random` , `csv` , `os` , etc.

### Creating our own module

> basic.py

```python
PI = 22 / 7

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y
```

> advanced.py

```python
def celsius_to_fahrenheit(celsius):
      fahr = (float(celsius) * 1.8) + 32
      return fahr

def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9 * fahrenheit - 32)
    return celsius
```

## Packages

* Packages are a way of organizing related modules into directories.
* A package contains an `__init__.py` file and multiple modules.

```bash
├── calci
│   ├── __init__.py
│   ├── advanced.py
│   └── basic.py
└── main.py
```

## **Benefits of Modules and Packages**

* Code Organization: Structuring code for readability and maintainability.
* Reusability: Encouraging the reuse of code in different projects.
* Namespace Management: Avoiding naming conflicts through encapsulation.
