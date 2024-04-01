# python3 - inheritance

## definition

* aquiring the properties [i.e attributes, methods] from the parent class.
* mostly used for code re-usability and maintainability

## example

```python
class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_info(self):
        return f"Employee: {self.name}\nID: {self.employee_id}\nSalary: ${self.salary}"


class Manager(Employee):
    def __init__(self, name, employee_id, salary, team_size):
        super().__init__(name, employee_id, salary)
        self.team_size = team_size

    def display_info(self):
        return f"Manager: {self.name}\nID: {self.employee_id}\nSalary ${self.salary}\nTeam Size: {self.team_size}."

```

## Types of inheritance

* Single inheritance
* Multi-level inheritance
* Multiple inheritance
* Hierarchical Inheritance
* Hybrid inheritance

## Single inheritance

```python
class A:
    pass

class B(A):
    pass
```

## Multi-level inheritance

```python
class A:
    pass

class B(A):
    pass

class C(B):
    pass
```

## Multiple inheritance

```python
class A:
    pass

class B:
    pass

class C(A, B):
    pass
```

## Hierarchical Inheritance

```python
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B):
    pass

class E(B):
    pass
```

## Hybrid inheritance

* it may be a combination of `Multilevel` and `Multiple` or `Hierarchical` and `Multilevel` or `Hierarchical`, `Multilevel` and `Multiple` inheritances.
* Try avoid this kind of inheritance.
* Keep your code simple and loosely coupled.

Method Resolution Order - MRO

> child class > first inherited class > next inherited class > ...

```python
class A:
    def who_are_you(self):
        print("I'm A")

class B:
    def who_are_you(self):
        print("I'm B")

class C:
    def who_are_you(self):
        print("I'm C")

class D(B, C, A):
    pass

class E(B, C, A):
    def who_are_you(self):
        print("I'm E")

class F(A, B, C):
    pass

print("class D")
d = D()
d.who_are_you()
# ouput: I'm B
print("class E")
e = E()
e.who_are_you()
# ouput: I'm E
print("class F")
f = F()
f.who_are_you()
# ouput: I'm A
```
