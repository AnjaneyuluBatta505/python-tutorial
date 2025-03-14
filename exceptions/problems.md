# Exception Handling

## 1. Basic Exception Handling
**Problem:** Write a Python program that catches a division by zero exception and prints an appropriate message.  
**Use Case:** In any calculator or mathematical application, users might try to divide a number by zero, leading to a crash. Handling this prevents the program from terminating unexpectedly.

## 2. Handling Multiple Exceptions
**Problem:** Create a program that handles both `ZeroDivisionError` and `ValueError` when taking user input for division.  
**Use Case:** When taking numerical input from users, they might enter invalid data (like text instead of a number), leading to `ValueError`, or attempt division by zero, causing `ZeroDivisionError`.

## 3. Using `try` with `else`
**Problem:** Write a program that attempts to open a file and reads its content. If successful, print the content; otherwise, handle the exception.  
**Use Case:** File reading operations often fail due to incorrect paths or missing files. The `else` block ensures that successful operations proceed without unnecessary exception handling code.

## 4. Using `finally`
**Problem:** Modify the previous program to ensure that the file is always closed, regardless of whether an exception occurs.  
**Use Case:** In file handling, not closing a file after reading/writing can cause memory leaks or lock files, making them inaccessible.

## 5. Raising Exceptions
**Problem:** Create a function that takes a number as input and raises a `ValueError` if the number is negative.  
**Use Case:** Some mathematical functions, like calculating square roots or logarithms, require non-negative numbers. Raising exceptions early prevents incorrect operations.

## 6. Custom Exceptions
**Problem:** Define a custom exception `NegativeNumberError` and raise it when a user enters a negative number.  
**Use Case:** When building domain-specific applications, predefined exceptions may not fully describe an error condition. Custom exceptions improve clarity and debugging.

## 7. Exception Handling in Loops
**Problem:** Write a program that continuously asks for user input until a valid integer is provided.  
**Use Case:** In applications requiring user input (like ATM PIN entry or form filling), we must ensure users enter valid data before proceeding.

## 8. Handling `FileNotFoundError`
**Problem:** Try opening a non-existent file and catch the `FileNotFoundError`, displaying an appropriate message.  
**Use Case:** Applications like text editors or log analyzers often work with files. Missing files should be handled gracefully to prevent crashes.

## 9. Handling `IndexError`
**Problem:** Write a program that attempts to access an index out of range in a list and handles the `IndexError`.  
**Use Case:** Data processing applications often work with lists and arrays. Accessing an invalid index without handling can lead to crashes.

## 10. Handling `KeyError`
**Problem:** Create a dictionary and attempt to access a non-existent key, handling the `KeyError` properly.  
**Use Case:** In API responses or configuration files, missing keys are common. Handling `KeyError` ensures robust data processing.

## 11. Using `assert` Statements
**Problem:** Write a function that uses assertions to ensure a parameter is positive.  
**Use Case:** Assertions are useful in debugging and testing, ensuring that functions receive correct input before execution.

## 12. Nested `try-except` Blocks
**Problem:** Create a program that has nested `try-except` blocks to handle different types of errors in a complex operation.  
**Use Case:** Some operations involve multiple steps, each with different failure points. Nested `try-except` blocks allow for handling each failure specifically.

## 13. Logging Exceptions
**Problem:** Modify any of the previous programs to log exceptions using the `logging` module instead of printing messages.  
**Use Case:** In production applications, logging exceptions is preferred over printing to track issues systematically and debug later.

## 14. Using `sys.exc_info()`
**Problem:** Write a program that captures exception details using `sys.exc_info()` and prints the exception type and message.  
**Use Case:** Debugging complex applications often requires detailed exception tracking, including stack traces and exact error messages.

## 15. Exception Handling in Class Methods
**Problem:** Create a class with a method that handles an exception raised within it.  
**Use Case:** Object-oriented applications often encapsulate logic inside class methods. Handling exceptions inside methods ensures class integrity.

## 16. Handling `AttributeError`
**Problem:** Write a program that attempts to access a non-existent attribute of an object and handles the `AttributeError`.  
**Use Case:** Working with dynamic objects or deserializing JSON data may lead to missing attributes. Handling `AttributeError` prevents unexpected failures.

## 17. Handling `TypeError`
**Problem:** Write a function that takes two numbers and handles the `TypeError` if a non-numeric value is passed.  
**Use Case:** Type errors are common in dynamic languages like Python. Validating input types before operations prevents unexpected crashes.

## 18. Using `contextlib.suppress()`
**Problem:** Use `contextlib.suppress(FileNotFoundError)` to handle missing file errors gracefully.  
**Use Case:** In situations where missing files are not critical (e.g., optional configuration files), `contextlib.suppress()` allows for clean, readable error handling.

## 19. Exception Chaining
**Problem:** Demonstrate exception chaining using `raise from` when catching an exception and raising a new one.  
**Use Case:** When handling exceptions, it’s sometimes necessary to convert one type of error into another while preserving the original traceback for debugging.

