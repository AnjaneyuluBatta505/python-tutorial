# Python Getters and Setters

1. **Create a `Person` class**:
   - **Private attributes**: `__name`, `__age`
   - Implement **getter** and **setter** methods for both attributes.
   - Ensure `age` cannot be negative.

2. **Modify attributes safely**:
   - Create an object of `Person`.
   - Use setter methods to update values.
   - Print attributes using getter methods.

3. **Encapsulation with getters and setters**:
   - Create a `Car` class with:
     - **Private attribute** `__speed`
     - Getter method `get_speed()`
     - Setter method `set_speed(new_speed)` (only allow positive values)

4. **Using `property()` function**:
   - Create a `Laptop` class with a **private** `__price`.
   - Use `property()` to define a getter and setter.

5. **Temperature conversion using properties**:
   - Create a `Temperature` class.
   - **Private attribute**: `__celsius`
   - Define `fahrenheit` as a **computed property** (`fahrenheit = celsius * 9/5 + 32`).
   - Allow setting temperature in Fahrenheit, converting it to Celsius.

6. **Using `@property` and `@setter` decorators**:
   - Convert the `Car` class's getter and setter to use `@property` and `@speed.setter`.

7. **Bank Account system**:
   - **Private attributes**: `__balance`
   - `deposit(amount)`: Add amount to balance.
   - `withdraw(amount)`: Deduct amount if sufficient balance.
   - Use `@property` to access balance.

8. **Validating email input**:
   - Create a `User` class.
   - **Private attribute**: `__email`
   - Setter should **validate** the email format before setting.

9. **Student grading system**:
   - **Private attributes**: `__marks`
   - Getter method: Returns grade based on marks.
   - Setter method: Ensures marks are between 0 and 100.

10. **Product discount system**:
    - **Private attributes**: `__price`, `__discount`
    - Getter should return the final price after applying discount.
    - Setter should validate discount percentage (0 to 50%).

11. **Read-only property**:
    - Create a `Circle` class.
    - **Private attribute**: `__radius`
    - Define a **read-only** property `area` (computed as `π * radius²`).

12. **Restrict attribute modification**:
    - Modify `BankAccount` so that **balance cannot be directly set** but can be updated using deposit/withdraw.

13. **Implement lazy evaluation**:
    - Create a `Rectangle` class.
    - **Private attributes**: `__length`, `__width`
    - Compute `area` only when needed.

14. **Using properties with validation**:
    - Create a `PasswordManager` class.
    - **Private attribute**: `__password`
    - Setter should enforce a **minimum length**.

15. **Encapsulation in an Employee class**:
    - **Private attributes**: `__salary`
    - Setter should ensure salary is not set below minimum wage.

16. **Prevent deletion of a property**:
    - Modify `BankAccount` so that `balance` cannot be deleted.

17. **Temperature conversion with caching**:
    - Modify `Temperature` to **store last computed Fahrenheit value** and update only when Celsius changes.

18. **Product stock tracking**:
    - **Private attribute**: `__stock`
    - Setter should prevent negative stock.
    - Getter should return "Out of Stock" if stock is 0.

19. **Automated Tax Calculation**:
    - **Private attribute**: `__income`
    - Define `tax` as a computed property (e.g., 10% of income).
    - Allow updating `income` while automatically updating `tax`.

20. **Creating a Singleton using Properties**:
    - Implement a `Logger` class where only **one instance** can exist.
