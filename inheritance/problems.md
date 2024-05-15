# Python - Inheritance

1. You are tasked with creating a system to manage inventory and products for a retail store. The system should allow adding, removing, and displaying products, as well as calculating the total cost of all products in the inventory.

   Possible classes

    1. Product(name, price, quantity)
    2. ElectronicsProduct(name, price, quantity, warranty_period)
    3. ClothingProduct(name, price, quantity, size)
    4. Inventory

2. Implement a system to manage customers and accounts in a bank where a base class Account defines common functionalities like deposit, withdraw, and balance inquiry, and subclasses like SavingsAccount and CheckingAccount inherit from Account and implement specific interest calculation methods or transaction rules.

    Possible classes

    1. Account(account_number, balance)
    2. SavingsAccount(account_number, balance, interest_rate)
    3. CheckingAccount(account_number, balance, overdraft_limit)

3. Develop a system to manage food delivery orders for a restaurant. Create a hierarchy with a base class FoodItem and subclasses like MainCourse, Appetizer, Dessert, etc. Each subclass can represent different categories of food items offered by the restaurant.

    Possible classes

    1. FoodItem(name, price)
    2. MainCourse(name, price, gst)
    3. Appetizer(name, price, gst)
    4. Dessert(name, price, gst)
    5. Order

    Note: User can add the food item to the order and expects order info to be displayed
  
