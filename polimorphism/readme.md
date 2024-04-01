# python - polymorphism

* Polymorphism is *the ability of objects behave in different ways* depending on the context in which they are used.
* In simple terms
  * objects of different types acts differently for same interface.
* uses: code reusability, maintainability

example1: operator polymorphism

```python
print(5 + 8)
print("5" + "8")
```

example2: function polimorphism

```python
def find_length(item):
    return len(item)
```

example3: class polimorphism [i.e includes method overloading & overriding]

```python
 class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price


class Table(Product):
    pass


class Chair(Product):
    discount_amount = 10

    def get_price(self):
        return self.price - self.discount_amount


class Computer(Product):
    tax = 3 # in percent

    def get_price(self):
        return self.price + (self.price * self.tax/100)


table = Table("white table", 20)
chair = Chair("Office Chair", 25)
computer = Computer("Dell Inspiron", 500)

cart_items = [table, chair, computer]


def calculate_cart_price(products):
    total = 0
    for product in products:
        total = total + product.get_price()
    return total


total = calculate_cart_price(cart_items)

print("Total:", total)

```
