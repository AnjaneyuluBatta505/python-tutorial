# Python - Operators

## What Are Operators?
Operators are special symbols in Python that help us do math and other cool things with numbers, words, and more!

Think of them like magic tools that help you add, subtract, compare, and even make decisions in your programs.

---

## 1. Arithmetic Operators (Math Operators)
These operators help us do basic math!

| Operator | Symbol | Example | Answer |
|----------|--------|---------|--------|
| Addition | `+` | `3 + 2` | `5` |
| Subtraction | `-` | `7 - 4` | `3` |
| Multiplication | `*` | `5 * 2` | `10` |
| Division | `/` | `8 / 2` | `4.0` |
| Modulus (Remainder) | `%` | `10 % 3` | `1` |
| Exponentiation (Power) | `**` | `2 ** 3` | `8` |
| Floor Division | `//` | `9 // 2` | `4` |

**Example Code:**
```python
print(3 + 2)  # 5
print(7 - 4)  # 3
print(5 * 2)  # 10
print(8 / 2)  # 4.0
print(10 % 3) # 1
print(2 ** 3) # 8
print(9 // 2) # 4
```

---

## 2. Comparison Operators (Telling Differences)
These operators help us compare two things!

| Operator | Meaning | Example | Answer |
|----------|---------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `10 > 5` | `True` |
| `<` | Less than | `3 < 8` | `True` |
| `>=` | Greater than or equal to | `6 >= 6` | `True` |
| `<=` | Less than or equal to | `4 <= 5` | `True` |

**Example Code:**
```python
print(5 == 5)  # True
print(5 != 3)  # True
print(10 > 5)  # True
print(3 < 8)   # True
print(6 >= 6)  # True
print(4 <= 5)  # True
```

---

## 3. Assignment Operators (Storing Values)
These operators help us store values in variables.

| Operator | Example | Same As |
|----------|---------|---------|
| `=` | `x = 5` | `x is 5` |
| `+=` | `x += 3` | `x = x + 3` |
| `-=` | `x -= 2` | `x = x - 2` |
| `*=` | `x *= 4` | `x = x * 4` |
| `/=` | `x /= 2` | `x = x / 2` |
| `%=` | `x %= 3` | `x = x % 3` |
| `**=` | `x **= 2` | `x = x ** 2` |
| `//=` | `x //= 2` | `x = x // 2` |

---

## 4. Logical Operators (Making Decisions)
Logical operators help us combine multiple conditions.

| Operator | Meaning | Example | Answer |
|----------|---------|---------|--------|
| `and` | Both must be True | `(5 > 3) and (8 > 2)` | `True` |
| `or` | At least one must be True | `(5 > 3) or (2 > 8)` | `True` |
| `not` | Opposite (True becomes False) | `not (5 > 3)` | `False` |

---

## 5. Bitwise Operators (Working with Bits)
Bitwise operators work at the binary level.

| Operator | Meaning | Example |
|----------|---------|---------|
| `&` | AND | `5 & 3` (1) |
| `\|` | OR | `5 \| 3` (7) |
| `^` | XOR | `5 ^ 3` (6) |
| `~` | NOT | `~5` (-6) |
| `<<` | Left Shift | `5 << 1` (10) |
| `>>` | Right Shift | `5 >> 1` (2) |

---

## 6. Membership Operators (Checking if Something is Inside a List)
| Operator | Example | Meaning | Answer |
|----------|---------|---------|--------|
| `in` | `"apple" in fruits` | Is "apple" inside the list? | `True` |
| `not in` | `"banana" not in fruits` | Is "banana" NOT inside the list? | `True` |

---

## 7. Identity Operators (Checking if Two Things Are the Same)
| Operator | Example | Meaning | Answer |
|----------|---------|---------|--------|
| `is` | `a is b` | Are they the same? | `True` or `False` |
| `is not` | `a is not b` | Are they different? | `True` or `False` |

---
