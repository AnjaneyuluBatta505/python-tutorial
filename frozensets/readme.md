# Frozenset Data Type in Python

* Python provides several built-in data structures to store and manage collections of data.
* One such data type is the **frozenset**.
* A **frozenset** is similar to a **set**, but it is **immutable**, meaning that once it is created, its elements cannot be changed, added, or removed.
* This makes frozensets useful for situations where a fixed set of unique values is needed.

## What is a Frozenset?
* A **frozenset** is an unordered collection of unique elements, just like a set.
* However, unlike sets, frozensets are **immutable**, meaning they cannot be modified after creation.
* This makes them hashable, allowing them to be used as dictionary keys or elements of other sets.

## Creating a Frozenset

* A frozenset can be created using the `frozenset()` function.

### Example:
```python
numbers = [1, 2, 3, 4, 5, 2, 3]  # A list with duplicate values
fset = frozenset(numbers)  # Convert list to frozenset
print(fset)  # Output: frozenset({1, 2, 3, 4, 5})
```

* Since frozensets are immutable, they do not support adding or removing elements.

## Accessing Elements in a Frozenset

* Since frozensets are unordered, elements cannot be accessed using an index like lists or tuples.
* However, you can check for membership using the `in` keyword.

### Example:

```python
fruits = frozenset(["apple", "banana", "cherry"])
print("apple" in fruits)  # Output: True
print("orange" in fruits) # Output: False
```

## Frozenset Operations

Although frozensets are immutable, they support various set operations, such as union, intersection, and difference.

### 1. Union (`|` or `.union()`)

Combines two sets and returns a new frozenset with all unique elements.
```python
a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])
print(a | b)  # Output: frozenset({1, 2, 3, 4, 5})
```

### 2. Intersection (`&` or `.intersection()`)

Returns a new frozenset with elements common to both sets.
```python
a = frozenset([1, 2, 3])
b = frozenset([2, 3, 4])
print(a & b)  # Output: frozenset({2, 3})
```

### 3. Difference (`-` or `.difference()`)

Returns elements present in the first frozenset but not in the second.
```python
a = frozenset([1, 2, 3, 4])
b = frozenset([3, 4, 5, 6])
print(a - b)  # Output: frozenset({1, 2})
```

### 4. Symmetric Difference (`^` or `.symmetric_difference()`)

Returns elements that are in either set but not in both.
```python
a = frozenset([1, 2, 3, 4])
b = frozenset([3, 4, 5, 6])
print(a ^ b)  # Output: frozenset({1, 2, 5, 6})
```

## Using Frozensets as Dictionary Keys

Since frozensets are immutable, they can be used as dictionary keys, unlike normal sets.

### Example:

```python
data = {frozenset(["apple", "banana"]): "fruit set"}
print(data)  # Output: {frozenset({'apple', 'banana'}): 'fruit set'}
```

## When to Use Frozensets?

- When you need an immutable set of unique values.
- When you want to use a set as a dictionary key.
- When you want to ensure that a set remains unchanged throughout the program.
