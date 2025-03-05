# Setters and Getters in Python

* Encapsulation is a fundamental concept in object-oriented programming (OOP) that helps to restrict direct access to an object's data.
* In Python, **setters and getters** are methods used to **access** and **modify** private attributes while maintaining control over their values.
* The `@property` decorator provides a `Pythonic` way to define these methods.

## What are Setters and Getters?

### **Getter Method**
A **getter** method is used to **retrieve** the value of a private attribute. It allows controlled access without exposing the internal representation of the attribute.

### **Setter Method**
A **setter** method is used to **update** the value of a private attribute. It allows validation before modifying the attribute's value.

---

## Why Use Setters and Getters?

- **Encapsulation**: Protects direct access to attributes.
- **Validation**: Ensures valid data is assigned.
- **Readability**: Makes the code more structured and manageable.
- **Flexibility**: Allows changes to internal implementation without affecting external code.

---

## Traditional Approach: Using Explicit Getter and Setter Methods
In languages like Java and C++, getters and setters are explicitly defined as `get_variable()` and `set_variable(value)`. In Python, we can also follow this approach:

### **Example: Using Explicit Methods**
```python
class Student:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute
    
    def get_age(self):
        return self.__age  # Getter method
    
    def set_age(self, new_age):
        if new_age > 0:
            self.__age = new_age  # Setter method
        else:
            raise ValueError("Age must be positive!")

# Creating an object
student = Student("Alice", 20)
print(student.get_age())  # Access age using getter

student.set_age(25)  # Update age using setter
print(student.get_age())
```

### **Output:**
```
20
25
```

Though this works, Python provides a more elegant way using the `@property` decorator.

---

## Pythonic Approach: Using `@property`
The `@property` decorator allows defining **getter** and **setter** methods in a more readable way, making attributes behave like regular variables.

### **Example: Using `@property`**
```python
class Student:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute
    
    @property
    def age(self):  # Getter method
        return self.__age
    
    @age.setter
    def age(self, new_age):  # Setter method
        if new_age > 0:
            self.__age = new_age
        else:
            raise ValueError("Age must be positive!")

# Creating an object
student = Student("Alice", 20)
print(student.age)  # Calls the getter

student.age = 25  # Calls the setter
print(student.age)
```

### **Output:**
```
20
25
```

---

## Understanding `@property`

1. **`@property` (Getter)**: Defines a method that can be accessed like an attribute.
2. **`@setter` (Setter)**: Allows controlled modification of an attribute.
3. **`@deleter` (Optional)**: Defines behavior for deleting an attribute.

---

## Example with a Deleter (`@deleter`)
```python
class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
    
    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, new_salary):
        if new_salary >= 30000:
            self.__salary = new_salary
        else:
            raise ValueError("Salary must be at least 30000!")
    
    @salary.deleter
    def salary(self):
        print("Deleting salary...")
        del self.__salary

# Creating an object
emp = Employee("John", 50000)
print(emp.salary)  # Calls getter

emp.salary = 60000  # Calls setter
print(emp.salary)

# Deleting salary
del emp.salary
```

### **Output:**
```
50000
60000
Deleting salary...
```

---

## When to Use `@property`
- When you want to **encapsulate** data but allow controlled access.
- When you need **computed properties** (e.g., returning a derived value).
- When attribute validation is required.

---

## Advantages of `@property`
| Feature | Benefit |
|---------|---------|
| Readability | No need for explicit `get_` or `set_` methods |
| Encapsulation | Protects private attributes while allowing controlled access |
| Validation | Ensures data integrity before modification |
| Flexibility | Allows changing the internal representation without affecting usage |

---

## Conclusion
- **Getters and setters** provide controlled access to private attributes.
- **Pythonic approach (`@property`)** improves readability and encapsulation.
- **Best practice**: Use `@property` for better structure and maintainability.

> Using `@property` makes Python code more elegant and easier to maintain while enforcing good OOP principles.
