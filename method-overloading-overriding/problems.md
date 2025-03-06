### **Basic Overloading**
1. **Create a class `Calculator`** with a method `add()` that adds:
   - Two numbers if two arguments are provided.
   - Three numbers if three arguments are provided.
   - Any number of numbers using `*args`.

2. **Create a class `Person`** with a method `introduce()` that:
   - Prints just the name if only the name is given.
   - Prints name and age if both are given.
   - Prints name, age, and profession if all three are provided.

3. **Create a class `Shape`** with a method `area()` that calculates:
   - Area of a square if one argument (side) is provided.
   - Area of a rectangle if two arguments (length & breadth) are provided.
   - Area of a circle if one argument (radius) is provided and specified as `circle`.

4. **Create a class `Formatter`** with a method `format_text()` that:
   - Returns uppercase text if no additional arguments are given.
   - Returns text in title case if a `title=True` argument is passed.
   - Returns text in reverse if `reverse=True` is passed.

5. **Create a class `Multiplier`** with a method `multiply()` that:
   - Multiplies two numbers if two arguments are given.
   - Multiplies all numbers in a list if a list is given as an argument.

### **Intermediate Overloading**
6. **Create a class `Vehicle`** with a method `describe()` that:
   - Prints details if only the vehicle type is given.
   - Prints details with engine capacity if both type and engine are given.
   - Prints full specifications if all parameters (type, engine, fuel, model) are provided.

7. **Create a class `Logger`** with a method `log_message()` that:
   - Logs messages in normal format if only the message is given.
   - Adds a timestamp if `timestamp=True` is provided.
   - Logs in uppercase if `uppercase=True` is provided.

8. **Create a class `Student`** with a method `calculate_grade()` that:
   - Calculates grade based on marks in one subject.
   - Calculates average grade if multiple subjects are passed as arguments.

9. **Create a class `BankAccount`** with a method `deposit()` that:
   - Deposits a fixed amount if only the amount is provided.
   - Deposits with interest if both amount and interest rate are provided.

10. **Create a class `Converter`** with a method `convert()` that:
    - Converts kilometers to miles if `km` is passed.
    - Converts Celsius to Fahrenheit if `C` is passed.
    - Converts kilograms to pounds if `kg` is passed.


## **Method Overriding Problems**
(Overriding is achieved by defining a method in a subclass that replaces a method from its parent class.)

### **Basic Overriding**
11. **Create a base class `Animal`** with a method `sound()` that prints `"Some generic animal sound"`.  
    - Override it in `Dog` to print `"Bark"`.  
    - Override it in `Cat` to print `"Meow"`.  

12. **Create a base class `Shape`** with a method `area()` that prints `"Calculating area"`.  
    - Override it in `Rectangle` to calculate length × breadth.  
    - Override it in `Circle` to calculate π × r².  

13. **Create a base class `Employee`** with a method `calculate_salary()` that prints a base salary.  
    - Override it in `Manager` to add a bonus.  
    - Override it in `Intern` to apply an hourly rate.  

14. **Create a base class `Vehicle`** with a method `fuel_type()`.  
    - Override it in `Car` to return `"Petrol or Diesel"`.  
    - Override it in `ElectricCar` to return `"Electric"`.  

15. **Create a class `Bird`** with a method `fly()`.  
    - Override it in `Eagle` to print `"Eagle flies high"`.  
    - Override it in `Penguin` to print `"Penguins can't fly"`.

### **Intermediate Overriding**
16. **Create a class `BankAccount`** with a method `withdraw()`.  
    - Override it in `SavingsAccount` to ensure minimum balance rules.  
    - Override it in `BusinessAccount` to allow overdraft.  

17. **Create a class `Person`** with a method `greet()`.  
    - Override it in `Student` to print `"Hello, I am a student"`.  
    - Override it in `Professor` to print `"Hello, I am a professor"`.  

18. **Create a class `Payment`** with a method `process_payment()`.  
    - Override it in `CreditCardPayment` to include credit card processing.  
    - Override it in `PayPalPayment` to include PayPal processing.  

19. **Create a base class `GameCharacter`** with a method `attack()`.  
    - Override it in `Warrior` to use `"Sword Attack"`.  
    - Override it in `Mage` to use `"Magic Attack"`.  

20. **Create a class `Computer`** with a method `compute()`.  
    - Override it in `Laptop` to display `"Computing on a laptop"`.  
    - Override it in `Supercomputer` to display `"Performing high-speed calculations"`.  
