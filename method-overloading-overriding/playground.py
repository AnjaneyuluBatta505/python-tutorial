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


print("Rectangle")
rect = Rectangle(10, 20)
print("area:", rect.area())
print("perimeter:", rect.perimeter())

print("Square")
square = Square(10)
print("area:", square.area())
print("perimeter:", square.perimeter())
