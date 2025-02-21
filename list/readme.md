# List Data Type in Python

* Python provides various data structures to store and manage collections of data.
* One of the most commonly used is the **list**.
* A **list** is an ordered collection of elements that can hold different data types and is **mutable**, meaning its elements can be changed after creation.

## What is a List?
A **list** is a collection of elements enclosed in square brackets `[]`, separated by commas.

### Example:
```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

print(fruits)  # Output: ['apple', 'banana', 'cherry']
print(numbers)  # Output: [1, 2, 3, 4, 5]
print(mixed)  # Output: [1, 'hello', 3.14, True]
```

## List Operations
Lists support various operations, including indexing, slicing, and iteration.

### Accessing Elements
```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: apple
print(fruits[-1])  # Output: cherry
```

### Slicing Lists
```python
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])  # Output: [20, 30, 40]
```

### Modifying Lists
```python
fruits[1] = "orange"
print(fruits)  # Output: ['apple', 'orange', 'cherry']
```

## List Methods
Python provides several built-in methods to manipulate lists efficiently.

| Method | Description | Example | Result |
|--------|-------------|---------|--------|
| `append(x)` | Adds an element to the end of the list | `fruits.append("grape")` | `['apple', 'banana', 'cherry', 'grape']` |
| `insert(i, x)` | Inserts an element at a specified index | `fruits.insert(1, "orange")` | `['apple', 'orange', 'banana', 'cherry']` |
| `remove(x)` | Removes the first occurrence of a value | `fruits.remove("banana")` | `['apple', 'cherry']` |
| `pop(i)` | Removes and returns an element at index `i` | `fruits.pop(1)` | `'banana'`, `['apple', 'cherry']` |
| `index(x)` | Returns the index of the first occurrence of `x` | `fruits.index("cherry")` | `2` |
| `count(x)` | Returns the number of occurrences of `x` | `fruits.count("apple")` | `1` |
| `sort()` | Sorts the list in ascending order | `numbers.sort()` | `[1, 2, 3, 4, 5]` |
| `reverse()` | Reverses the order of the list | `numbers.reverse()` | `[5, 4, 3, 2, 1]` |
| `copy()` | Returns a shallow copy of the list | `new_list = numbers.copy()` | `new_list` contains `[1, 2, 3, 4, 5]` |
| `clear()` | Removes all elements from the list | `fruits.clear()` | `[]` |

## When to Use Lists?
- When you need an **ordered** collection of items.
- When elements **may change** after creation.
- When **fast access** to elements using an index is required.
