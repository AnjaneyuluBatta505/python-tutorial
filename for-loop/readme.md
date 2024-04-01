# python - `for` loop

* A `for` loop is used for iterating over a sequence
  * `list`, `tuple`, `set`, `dict`, `string`, etc.
  * it executes fixed number of times

## example

```python
names = ["Anji", "Shiva", "John"]
for x in names:
  print(x)
```

## `break` statement

* exit the loop if condition is evaluated to true

```python

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    print(f"Current number: {number}")

    if number == 7:
        print("Found the number 7, breaking out of the loop")
        break
```

## `continue` statement

* skips the interation of the loop if condition is evaluated to true

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number % 2 == 0:
        # Skip even numbers
        print(f"Skipping even number: {number}")
        continue

    # Process only odd numbers
    print(f"Processing odd number: {number}")
```

## `range()` function

* `range` is bultin function which generates a sequence.
* we can use it with for loop

```python
for i in range(1, 10, 2):
    print(i)
```

## nested loops

* a loop inside another loop is called nested loop

```python
for i in range(3):
    for j in range(2):
        print(f"({i}, {j})")
```

## python programs

* print first 10 natural numbers
* find numbers divisible by 3 in the list [1, 5, 6, 9, 10, 12]
* print first 10 fibonacci numbers

  * 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
* print the following pattern

  ```
  1 
  1 2 
  1 2 3 
  1 2 3 4 
  1 2 3 4 5
  ```
