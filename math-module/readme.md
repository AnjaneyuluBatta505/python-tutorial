# Python3 - Math Module

* It's used for mathmatical comupations
* It is used for `Mathematical Functions`  , `Trigonometric Functions `  and  `Statistical Functions`  and more

## Constants

| Constant     | Description                   | Example Usage       |
| ------------ | ----------------------------- | ------------------- |
| `math.pi`  | Mathematical constant π (pi) | `print(math.pi)`  |
| `math.e`   | Euler's number e              | `print(math.e)`   |
| `math.tau` | Tau (τ), a circle constant   | `print(math.tau)` |
| `math.inf` | Positive infinity             | `print(math.pi)`  |
| `math.nan` | Not a Number (NaN)            | `print(math.nan)` |

## Trignomerty functions

| Function             | Description                                | Example Usage             |
| -------------------- | ------------------------------------------ | ------------------------- |
| `math.sin(x)`      | Returns the sine of x (in radians).        | `math.sin(math.pi/2)`   |
| `math.cos(x)`      | Returns the cosine of x (in radians).      | `math.cos(math.pi)`     |
| `math.tan(x)`      | Returns the tangent of x (in radians).     | `math.tan(math.pi/4)`   |
| `math.asin(x)`     | Returns the arcsine of x (in radians).     | `math.asin(0.5)`        |
| `math.acos(x)`     | Returns the arccosine of x (in radians).   | `math.acos(0.5)`        |
| `math.atan(x)`     | Returns the arctangent of x (in radians).  | `math.atan(1)`          |
| `math.atan2(y, x)` | Returns the arctangent of y/x (in radians) | `math.atan2(1, 1)`      |
| `math.degrees(x)`  | Converts angle x from radians to degrees.  | `math.degrees(math.pi)` |
| `math.radians(x)`  | Converts angle x from degrees to radians.  | `math.radians(180)`     |

## number-theoretic functions

| Function                | Description                                   | Example usage                          |
| ----------------------- | --------------------------------------------- | -------------------------------------- |
| `math.gcd(a, b)`      | Greatest common divisor of integers a and b   | `math.gcd(12, 15)`=>`3`            |
| `math.lcm(a, b)`      | Least common multiple of integers a and b     | `math.lcm(12, 15)`=>`60`           |
| `math.isqrt(n)`       | Integer square root of non-negative integer n | `math.isqrt(16)`=>`4`              |
| `math.isfinite(x)`    | Checks if x is a finite number                | `math.isfinite(10)`=>`True`        |
| `math.isinf(x)`       | Checks if x is positive or negative infinity  | `math.isinf(float('inf'))`=>`True` |
| `math.isnan(x)`       | Checks if x is NaN (not a number)             | `math.isnan(float('nan'))`=>`True` |
| `math.factorial(n)`   | Factorial of non-negative integer n           | `math.factorial(5)`=>`120`         |
| `math.perm(n, k)`     | Permutations of n items taken k at a time     | `math.perm(5, 2)`=>`20`            |
| `math.comb(n, k)`     | Combinations of n items taken k at a time     | `math.comb(5, 2)`=>`10`            |
| `math.prod(iterable)` | Product of all elements in the iterable       | `math.prod([1, 2, 3, 4])`=>`24`    |

## Power and logarithmic functions

| Function                | Description                            | Example Usage                                          |
| ----------------------- | -------------------------------------- | ------------------------------------------------------ |
| `math.pow(x, y)`      | Returns x raised to the power of y     | `math.pow(2, 3)` returns `8.0`                     |
| `math.sqrt(x)`        | Returns the square root of x           | `math.sqrt(9)` returns `3.0`                       |
| `math.exp(x)`         | Returns e raised to the power of x     | `math.exp(1)` returns `2.718281828459045`          |
| `math.log(x)`         | Returns the natural logarithm of x     | `math.log(10)` returns `2.302585092994046`         |
| `math.log(x, b)`      | Returns the logarithm of x with base b | `math.log(100, 10)` returns `2.0`                  |
| `math.log2(x)`        | Returns the base-2 logarithm of x      | `math.log2(8)` returns `3.0`                       |
| `math.log10(x)`       | Returns the base-10 logarithm of x     | `math.log10(100)` returns `2.0`                    |
| `math.pow(math.e, x)` | Equivalent to `math.exp(x)`          | `math.pow(math.e, 2)` returns `7.3890560989306495` |

## **pip packages for calculations & data analysis**

* NumPy, SciPy, math, pandas, scikit-learn, Keras, PyTorch, and TensorFlow.

**References:**

* [https://docs.python.org/3/library/math.html](https://docs.python.org/3/library/math.html "Open math module")
