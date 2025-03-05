# Access Modifiers in Python

* Access modifiers in Python control the visibility and accessibility of class members (variables and methods).
* Python, unlike languages such as Java and C++, does not enforce strict access control but follows a naming convention to indicate the intended level of accessibility.
* The three primary access modifiers in Python are:

1. **Public** – Accessible from anywhere.
2. **Protected** – Indicated by a single underscore (`_`), intended for internal use but still accessible.
3. **Private** – Indicated by double underscores (`__`), name-mangled to restrict access within the class.

Understanding these modifiers helps in designing better-structured, maintainable, and encapsulated code.

---

## 1. Public Members

* Public members are accessible from anywhere, both inside and outside the class.
* By default, all class attributes and methods in Python are public.

### Example:
```python
class PublicExample:
    def __init__(self, name):
        self.name = name  # Public attribute

    def display(self):  # Public method
        return f"Name: {self.name}"

# Creating an object
obj = PublicExample("Alice")
print(obj.name)  # Accessible
print(obj.display())  # Accessible
```
### Output:
```
Alice
Name: Alice
```

Public members should be used when there is no need to restrict access.

---

## 2. Protected Members

* Protected members are indicated by a single underscore (`_`).
* This signals to developers that these members are intended for internal use and should not be accessed directly from outside the class.
* However, they **are not strictly restricted** and can still be accessed if needed.

### Example:
```python
class ProtectedExample:
    def __init__(self, age):
        self._age = age  # Protected attribute

    def _show_age(self):  # Protected method
        return f"Age: {self._age}"

# Creating an object
obj = ProtectedExample(25)
print(obj._age)  # Accessible but discouraged
print(obj._show_age())  # Accessible but discouraged
```
### Output:
```
25
Age: 25
```

Even though `_age` and `_show_age()` are accessible, they are meant to be used within the class or subclasses rather than being accessed directly.

### Accessing Protected Members in a Subclass:
```python
class Derived(ProtectedExample):
    def get_age(self):
        return f"Accessing protected member: {self._age}"

obj2 = Derived(30)
print(obj2.get_age())
```
### Output:
```
Accessing protected member: 30
```

Protected members are useful when designing classes where attributes/methods should be accessible to subclasses but not necessarily to external code.

---

## 3. Private Members
Private members are indicated by **double underscores (`__`)**. Python performs **name mangling** on these members, making them harder to access outside the class. This provides a level of access restriction.

### Example:
```python
class PrivateExample:
    def __init__(self, salary):
        self.__salary = salary  # Private attribute

    def __get_salary(self):  # Private method
        return f"Salary: {self.__salary}"

    def show_salary(self):
        return self.__get_salary()  # Accessible within class

# Creating an object
obj = PrivateExample(50000)
# print(obj.__salary)  # This will raise an AttributeError
# print(obj.__get_salary())  # This will also raise an AttributeError

print(obj.show_salary())  # Indirect access via public method
```
### Output:
```
Salary: 50000
```

Attempting to access `__salary` or `__get_salary()` directly results in an `AttributeError`. However, we can still access private members using name mangling.

### Accessing Private Members using Name Mangling:
```python
print(obj._PrivateExample__salary)  # Works, but not recommended
```
### Output:
```
50000
```

Although name mangling allows access to private members, it is generally discouraged as it breaks the principle of encapsulation.

---

## Summary Table
| Access Modifier | Syntax | Accessibility |
|----------------|--------|--------------|
| **Public** | `self.var` | Accessible everywhere |
| **Protected** | `self._var` | Accessible within the class and subclasses (discouraged outside) |
| **Private** | `self.__var` | Accessible only within the class (Name mangling applies) |

---

## When to Use Which Modifier?
- **Public**: Use when there is no need to restrict access.
- **Protected**: Use when you want to indicate that a variable/method should not be accessed directly but can be used in subclasses.
- **Private**: Use when you want to enforce strong encapsulation within a class and prevent direct external access.

### Best Practices:
- Use getter and setter methods for controlled access to private attributes.
- Follow naming conventions to indicate intent rather than relying on enforcement.
- Avoid direct access to protected/private members unless absolutely necessary.

By following these principles, you can create well-structured, maintainable, and encapsulated Python programs.

