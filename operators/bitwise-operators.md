# Bitwise Operators in Python

Bitwise operators in Python allow us to manipulate individual bits of numbers. These operators work at the binary level (0s and 1s).
Let's explore them with simple examples.

---

## 1. Bitwise AND (`&`)

- The `&` operator compares two numbers bit by bit and returns `1` if both bits are `1`.
- Otherwise, it returns `0`.

### Example:
```python
x = 5  # Binary: 0101
y = 3  # Binary: 0011
result = x & y  # 0101 & 0011 = 0001 (Decimal: 1)
print(result)  # Output: 1
```

---

## 2. Bitwise OR (`|`)

- The `|` operator compares two numbers bit by bit and returns `1` if at least one of the bits is `1`.

### Example:
```python
x = 5  # Binary: 0101
y = 3  # Binary: 0011
result = x | y  # 0101 | 0011 = 0111 (Decimal: 7)
print(result)  # Output: 7
```

---

## 3. Bitwise XOR (`^`)

- The `^` (XOR) operator returns `1` if the bits are different and `0` if they are the same.

### Example:
```python
x = 5  # Binary: 0101
y = 3  # Binary: 0011
result = x ^ y  # 0101 ^ 0011 = 0110 (Decimal: 6)
print(result)  # Output: 6
```

---

## 4. Bitwise NOT (`~`)

- The `~` operator inverts all the bits of a number.
- In Python, `~x` is the same as `-(x + 1)`.

### Examples:
```python
x = 5  # Binary: 0000 0101
result = ~x  # Binary: 1111 1010 (Decimal: -6)
print(result)  # Output: -6

x = 1  # Binary: 0000 0001
result = ~x  # Binary: 1111 1110 (Decimal: -2)
print(result)  # Output: -2

x = 0  # Binary: 0000 0000
result = ~x  # Binary: 1111 1111 (Decimal: -1)
print(result)  # Output: -1
```

---

## 5. Left Shift (`<<`)

- The `<<` operator shifts bits to the left, effectively multiplying by powers of 2.

### Example:
```python
x = 5  # Binary: 0101
result = x << 1  # 0101 << 1 = 1010 (Decimal: 10)
print(result)  # Output: 10
```

---

## 6. Right Shift (`>>`)

- The `>>` operator shifts bits to the right, effectively dividing by powers of 2.

### Example:
```python
x = 5  # Binary: 0101
result = x >> 1  # 0101 >> 1 = 0010 (Decimal: 2)
print(result)  # Output: 2
```

---

## Summary Table

| Operator | Name           | Example  | Result  |
|----------|---------------|----------|---------|
| `&`      | AND           | `5 & 3`  | `1`     |
| `\|`      | OR            | `5 \| 3`  | `7`     |
| `^`      | XOR           | `5 ^ 3`  | `6`     |
| `~`      | NOT           | `~5`     | `-6`    |
| `<<`     | Left Shift    | `5 << 1` | `10`    |
| `>>`     | Right Shift   | `5 >> 1` | `2`     |


