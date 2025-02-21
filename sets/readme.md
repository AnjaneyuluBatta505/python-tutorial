# Set Data Type in Python

* Python provides various built-in data structures to store and manage collections of data.
* One such data structure is the **set**.
* A **set** is an **unordered** collection of **unique** elements and is **mutable**, meaning elements can be added or removed.

## What is a Set?
A **set** is a collection of unique elements enclosed in curly brackets `{}` and separated by commas.

### Example:

```python
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}

fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}
mixed = {1, "hello", 3.14, True}

print(A, B)  # Output: {1, 2, 3, 4, 5} {3, 4, 5, 6, 7}
print(fruits)  # Output: {'apple', 'banana', 'cherry'}
print(numbers)  # Output: {1, 2, 3, 4, 5}
print(mixed)  # Output: {1, 3.14, 'hello'}
```
(Note: The order of elements may change as sets are unordered.)

## Set Operations
Sets support mathematical operations like union, intersection, and difference.

### Accessing Elements
Since sets are unordered, elements **cannot** be accessed using an index. Instead, we check for membership using the `in` keyword.
```python
fruits = {"apple", "banana", "cherry"}
print("apple" in fruits)  # Output: True
```

### Adding and Removing Elements
```python
fruits.add("orange")  # Adds 'orange' to the set
print(fruits)  # Output: {'apple', 'banana', 'cherry', 'orange'}

fruits.remove("banana")  # Removes 'banana'
print(fruits)  # Output: {'apple', 'cherry', 'orange'}
```

## Set Methods
Python provides several built-in methods to manipulate sets efficiently.

| Method | Description | Example | Result |
|--------|-------------|---------|--------|
| `add(x)` | Adds an element `x` to the set | `fruits.add("grape")` | `{'apple', 'banana', 'cherry', 'grape'}` |
| `remove(x)` | Removes `x` from the set (raises error if not found) | `fruits.remove("banana")` | `{'apple', 'cherry'}` |
| `discard(x)` | Removes `x` from the set (no error if not found) | `fruits.discard("banana")` | `{'apple', 'cherry'}` |
| `pop()` | Removes and returns a random element | `fruits.pop()` | Returns a random element and modifies the set |
| `clear()` | Removes all elements from the set | `fruits.clear()` | `{}` |
| `union(set2)` | Returns a set containing all unique elements from both sets | `A.union(B)` | `{1, 2, 3, 4, 5}` |
| `intersection(set2)` | Returns a set of common elements | `A.intersection(B)` | `{3, 4}` |
| `difference(set2)` | Returns elements present in `A` but not in `B` | `A.difference(B)` | `{1, 2}` |
| `symmetric_difference(set2)` | Returns elements that are in `A` or `B` but not both | `A.symmetric_difference(B)` | `{1, 2, 5, 6}` |
| `copy()` | Returns a shallow copy of the set | `new_set = fruits.copy()` | `new_set` contains `{'apple', 'cherry'}` |

## When to Use Sets?
- When you need an **unordered** collection of unique elements.
- When you need to **eliminate duplicates** from a list.
- When you require **fast membership checking** (`in` operator is faster in sets than lists).
