# Python - `while` loop

* use it when we need repetitive execution of block of code until the given condition is met
* can be called as "indefinite"

## syntax

```python
while condition:
    # code block
    # ...
```

## example

```python
num = 1
while num <= 10:
  print(num)
  num += 1
```

## iterate over - list, dict, etc

```python
names = ["Anji", "John", "Ahmed"]
index = 0
while index < names.length:
  print(names[0])
```

## `break` - statement

```python
while True:
  exp = input("Exp: ")
  if exp == "stop":
     break
  print("output", eval(exp))
```

## `continue` - statement

```python
numbers = range(1, 11)
index = 0
while index < len(numbers):
  number = numbers[index]
  index = index + 1
  if number % 2 == 0:
    continue
  print(number)
```

## `else` - statement

```python
index = 0
while index < 3:
  print(index)
  i += 1
else:
  print(f"else >> index={index}")
```

## nested while loop

```python
base = 1
while base <= 3:
    multiply = 1
    while multiply <= 5:
        print(base, "*", multiply, '=', base * multiply)
        multiply += 1
    base += 1
    print("\n")
```

## problem solving

* guess the number
* find factorial of the given number
* sum of digits of the given number
* table of a number
* check if given number is prime or not
