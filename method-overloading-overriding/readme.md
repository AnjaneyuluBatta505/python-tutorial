## Python - method overloading & method overriding

##### definition: method overloading

* A method with same name behaves differently based on the number of parameters or  data types of parameters
* Python does not support the declaring the multiple methods with same name

example:

```python
class Package:
    def __init__(self, product):
        self.product = product

    def pack_product(self, is_gift=None):
        if is_gift:
            return f"Your '{self.product}' is packed as a gift"
        else:
            return f"Your '{self.product}' is packed."
```

##### definition: method overriding

* method overriding allows child class to define the same method name as parent class and replace or modify the behaviour of the method.

example:

```python
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
	return 2 * (self.length + self.breadth)

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
```
