# Practice Problems

## 1. Public Members
Define a class `Person` with a public attribute `name` and a public method `greet()`.  
Create an object and access these members from outside the class.

## 2. Protected Members
Modify the `Person` class to include a protected attribute `_age`.  
Create a subclass `Student` that accesses `_age` within the subclass.

## 3. Private Members
Define a class `BankAccount` with a private attribute `__balance`.  
Try to access `__balance` outside the class and observe the result.

## 4. Private Methods
Create a class `Secret` with a private method `__hidden_message()`.  
Call it indirectly from a public method `reveal_message()`.

## 5. Name Mangling
Modify the `BankAccount` class to include a getter method for `__balance`.  
Try accessing `__balance` using name mangling (`_ClassName__attribute`).

## 6. Protected Variables in Inheritance
Create a class `Vehicle` with a protected attribute `_speed`.  
Inherit it in a class `Car` and access `_speed` inside the subclass.

## 7. Restricting Direct Access
Define a class `User` with a private variable `__password`.  
Provide a method `set_password(new_password)` and `get_password()` to modify and access it.

## 8. Mixing Access Modifiers
Create a class `Employee` with:
- Public attribute: `name`
- Protected attribute: `_salary`
- Private attribute: `__bonus`
Instantiate an object and access all attributes correctly.

## 9. Encapsulation with Getters and Setters
Define a class `Student` with a private attribute `__grade`.  
Use getter and setter methods to access and modify `__grade` safely.

## 10. Checking Accessibility
Write a program to test access to:
- Public variables (`.var`)
- Protected variables (`._var`)
- Private variables (`.__var`)
Try accessing them inside and outside the class.
