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
    tax = 5  # in percent

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

