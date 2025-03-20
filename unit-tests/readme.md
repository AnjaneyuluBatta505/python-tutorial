# **Unit Testing**  

## 1. Introduction
* Unit testing is a software testing method where **individual components (units)** of a program are tested to determine if they work as expected.
* These tests are typically **automated** and help catch bugs early in the development cycle.  

---

## **2. Importance of Unit Testing**  
- Ensures code correctness  
- Helps in **early bug detection**  
- Makes code **maintainable and scalable**  
- Facilitates **refactoring without breaking functionality**  
- Supports Test-Driven Development (**TDD**)  

---

## **3. Python’s `unittest` Module**  
Python comes with a **built-in testing** framework called **`unittest`**, inspired by Java’s JUnit.  

### **Key Features of `unittest`**  
✅ Based on **object-oriented testing**  
✅ Uses **test discovery** mechanism  
✅ Supports **test fixtures (`setUp` & `tearDown`)**  
✅ Provides **mocking capabilities**  

**To use `unittest`, first import the module:**
```python
import unittest
```

---

## **4. Writing Your First Unit Test**  
A simple example of a test case using `unittest`:  

```python
import unittest

def add(x, y):
    return x + y

class TestMathOperations(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == "__main__":
    unittest.main()
```

---

## **5. Assertions in `unittest`**  
Assertions check whether conditions hold true. Common assertion methods:  

| Assertion Method | Description |
|-----------------|-------------|
| `assertEqual(a, b)` | Check if `a == b` |
| `assertNotEqual(a, b)` | Check if `a != b` |
| `assertTrue(x)` | Check if `x` is `True` |
| `assertFalse(x)` | Check if `x` is `False` |
| `assertIsNone(x)` | Check if `x is None` |
| `assertIsNotNone(x)` | Check if `x is not None` |
| `assertIn(a, b)` | Check if `a in b` |
| `assertNotIn(a, b)` | Check if `a not in b` |

**Example:**
```python
def is_even(num):
    return num % 2 == 0

class TestNumbers(unittest.TestCase):
    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(5))
```
---

## **6. Test Fixtures (`setUp` and `tearDown`)**  
Test fixtures are setup and teardown methods that **run before and after each test**.

```python
class TestExample(unittest.TestCase):
    def setUp(self):
        print("Setting up...")

    def tearDown(self):
        print("Cleaning up...")

    def test_sample(self):
        print("Running test")
        self.assertEqual(1 + 1, 2)
```

### **Execution Order:**  
1. `setUp()` runs before each test.  
2. The test method runs.  
3. `tearDown()` runs after each test.  

---

## **7. Running and Discovering Tests**  
### **Running Tests from the Command Line**  
Save the test file as `test_math.py` and run:  
````bash
python -m unittest test_math.py
````

### **Running All Tests in a Directory**  
````bash
python -m unittest discover
````

---

## **8. Mocking in Unit Testing (`unittest.mock`)**  
Mocking is used to replace real objects with fake ones.  

```python
from unittest.mock import MagicMock

class Service:
    def fetch_data(self):
        return "Real Data"

service = Service()
service.fetch_data = MagicMock(return_value="Mocked Data")

print(service.fetch_data())  # Output: Mocked Data
```

---

## **9. Parameterized Testing**  
Use `subTest()` to test multiple cases within a single test method.  

```python
class TestMath(unittest.TestCase):
    def test_addition(self):
        test_cases = [(1, 2, 3), (2, 2, 4), (3, 5, 8)]
        for x, y, expected in test_cases:
            with self.subTest(x=x, y=y):
                self.assertEqual(add(x, y), expected)
```

---

## **10. Handling Expected Failures**  
To test expected failures, use `assertRaises()`.  

```python
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

class TestDivision(unittest.TestCase):
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(5, 0)
```

---

## **11. Skipping Tests**  
Skip tests using `@unittest.skip` decorators.  

```python
class TestExample(unittest.TestCase):
    @unittest.skip("Skipping this test")
    def test_skip(self):
        self.assertEqual(1 + 1, 2)
```

---

## **12. Code Coverage and Best Practices**  
### **Measuring Code Coverage**
Use `coverage.py` to check test coverage.  

````bash
pip install coverage
coverage run -m unittest discover
coverage report -m
````

### **Best Practices**
✅ Keep tests **small and isolated**  
✅ Use **descriptive test names**  
✅ Run tests **frequently**  
✅ Use **mocking for dependencies**  
✅ Ensure **high code coverage**  

---

## **13. Alternative Testing Frameworks**
Besides `unittest`, other popular testing frameworks include:  

### **1. `pytest` (Recommended)**
- Simpler and more powerful than `unittest`.  
- Supports fixtures and parameterized tests.  
- Run tests using:  
  ````bash
  pytest test_file.py
  ````

### **2. `nose2`**
- Extension of `unittest`.  
- Supports plugins for enhanced testing.  
