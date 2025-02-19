# Number Data Types in Python

Numbers are an essential part of programming, and Python provides several number data types to work with different kinds of numerical values.
In this article, we will explore the different number data types in Python and how to use them.

## Types of Numbers in Python
Python has three main numerical data types:
1. **Integers (`int`)**
2. **Floating-Point Numbers (`float`)**
3. **Complex Numbers (`complex`)**

Let's go through each one with examples.

### 1. Integers (`int`)
Integers are whole numbers, positive or negative, without a decimal point.
```python
x = 10
y = -5
z = 1000000
print(x, y, z)  # Output: 10 -5 1000000
```
Python automatically determines the size of an integer, so you don’t need to worry about limitations.

### 2. Floating-Point Numbers (`float`)
Floats are numbers that have a decimal point or are written in exponential form.
```python
a = 10.5
b = -3.14
c = 2.5e3  # 2.5 * 10^3 = 2500.0
print(a, b, c)  # Output: 10.5 -3.14 2500.0
```
Floats are commonly used in calculations that require precision, such as scientific computations.

### 3. Complex Numbers (`complex`)
Complex numbers have a real and an imaginary part, written as `a + bj` where `j` represents the imaginary unit.
```python
c1 = 2 + 3j
c2 = 5 - 4j
print(c1, c2)  # Output: (2+3j) (5-4j)
```
Complex numbers are mainly used in advanced mathematics and engineering applications.

## Type Conversion Between Numbers
Python allows conversion between different number types using `int()`, `float()`, and `complex()`.
```python
x = 5
print(float(x))   # Output: 5.0

y = 7.9
print(int(y))    # Output: 7

z = 3
print(complex(z))  # Output: (3+0j)
```

## Arithmetic Operations with Numbers
Python supports basic arithmetic operations with numbers:
```python
a = 10
b = 3
print(a + b)   # Addition: 13
print(a - b)   # Subtraction: 7
print(a * b)   # Multiplication: 30
print(a / b)   # Division: 3.3333...
print(a // b)  # Floor Division: 3
print(a % b)   # Modulus: 1
print(a ** b)  # Exponentiation: 1000
```
