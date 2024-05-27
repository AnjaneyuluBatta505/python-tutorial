# Python - Unit testing

* Unit testing is a software testing technique where individual units or components of the software are tested in isolation from the rest of the application.
* The primary goal is to validate that each unit of the software performs as expected.
* Unit testing is a critical practice to ensure code reliability, catch bugs early, and facilitate maintenance.
* Python has built-in module `unittest` module to perform unit testing.
* External python packages like pytest, nose2, etc. are also available.


## Factorial - Unit test

> fact.py

```python
def factorial(num):
  output = 1
  for index in range(1, num+1):
    output = output * index
  return output
```

* Lets write the unittest for factorial.

```python
import unittest

from fact import factorial

class TestFactorial(unittest.TestCase):
    
    def test_factorial_of_zero(self):
        self.assertEqual(factorial(0), 1)
    
    def test_factorial_of_one(self):
        self.assertEqual(factorial(1), 1)
    
    def test_factorial_of_five(self):
        self.assertEqual(factorial(5), 120)
    
    def test_factorial_of_ten(self):
        self.assertEqual(factorial(10), 3628800)
    
    def test_large_input(self):
        self.assertEqual(factorial(20), 2432902008176640000)
    
    def test_factorial_of_large_number(self):
        self.assertEqual(factorial(15), 1307674368000)

if __name__ == '__main__':
    unittest.main()
```

## Common assertion methods

|Assertion Method|Description|Example|
|--- |--- |--- |
|assertEqual(a, b)|Checks that a is equal to b.|self.assertEqual(1 + 1, 2)|
|assertNotEqual(a, b)|Checks that a is not equal to b.|self.assertNotEqual(1 + 1, 3)|
|assertTrue(x)|Checks that x is True.|self.assertTrue(3 > 2)|
|assertFalse(x)|Checks that x is False.|self.assertFalse(2 > 3)|
|assertIs(a, b)|Checks that a is b (they are the same object).|self.assertIs(a, a)|
|assertIsNot(a, b)|Checks that a is not b (they are not the same object).|self.assertIsNot(a, b)|
|assertIsNone(x)|Checks that x is None.|self.assertIsNone(None)|
|assertIsNotNone(x)|Checks that x is not None.|self.assertIsNotNone(3)|
|assertIn(a, b)|Checks that a is in b.|self.assertIn(3, [1, 2, 3])|
|assertNotIn(a, b)|Checks that a is not in b.|self.assertNotIn(4, [1, 2, 3])|
|assertIsInstance(a, b)|Checks that a is an instance of b.|self.assertIsInstance(3, int)|
|assertNotIsInstance(a, b)|Checks that a is not an instance of b.|self.assertNotIsInstance(3, str)|
|assertRaises(exc, fun, *args, **kwds)|Checks that fun(*args, **kwds) raises exc.|self.assertRaises(ValueError, int, 'a')|
|assertAlmostEqual(a, b)|Checks that a is almost equal to b (for floating point numbers).|self.assertAlmostEqual(1.0000001, 1.0000002, places=6)|
|assertNotAlmostEqual(a, b)|Checks that a is not almost equal to b.|self.assertNotAlmostEqual(1.0001, 1.0002, places=4)|
|assertGreater(a, b)|Checks that a is greater than b.|self.assertGreater(5, 3)|
|assertGreaterEqual(a, b)|Checks that a is greater than or equal to b.|self.assertGreaterEqual(5, 5)|
|assertLess(a, b)|Checks that a is less than b.|self.assertLess(3, 5)|
|assertLessEqual(a, b)|Checks that a is less than or equal to b.|self.assertLessEqual(3, 3)|
|assertRegex(s, r)|Checks that the regular expression r matches string s.|self.assertRegex('hello world', r'hello')|
|assertNotRegex(s, r)|Checks that the regular expression r does not match string s.|self.assertNotRegex('hello world', r'world!')|
|assertCountEqual(a, b)|Checks that a and b have the same elements, regardless of order.|self.assertCountEqual([1, 2, 3], [3, 1, 2])|
