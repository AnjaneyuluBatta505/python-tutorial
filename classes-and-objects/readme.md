# python3 - classes and objects

## why to use `class` ?

* combine data and functions
* code reusability - oops
* better maintainability

## object

* `object` is a thing in a real world
* examples: Book, Dog, Task, ToDoList, etc.

## class

* `class` is a blueprint or a template for creating the objects.
* An `object` is an instance of a class

## class syntax

```python
class ClassName:
    attr = "value"

    def method(self):
        ...
```

## example

```python
class TeaCup:
    is_empty = True

    def fill_tea(self):
        print("Filled Tea")
        self.is_empty = False
  
    def drink_tea(self):
        print("Drinked Tea")
        self.is_empty = True
```

## terminology of a class

* `class` keyword
* Class Name
* Attributes / Data Members
* Methods / Member Functions
* `__new__` - constructor method
* `__init__` - initializer method
* `self` keyword
* instance - class object

## `__new__` vs `__init__`

## class methods

* instance method
* @classmethod - class method
* @staticmethod - static method

## problems

### Library Catalog:

* Design a Book class with attributes like title and author
* Create a Library class to manage a collection of books, allowing for add, find and borrow books.
