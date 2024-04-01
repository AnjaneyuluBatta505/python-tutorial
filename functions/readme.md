# python3 - function

* a piece of code that performs a specific task
* it can be reused

## syntax

```python
def func_name(param1, param2):
    # code
    # ....
```

## example

```python
def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact = fact * i
    return fact
```

## function params

* no params
* single or multiple params
* default params

## variable scopes

* global scope
* local scope

## return - statement

* return values from functions
* multile return values

## *args, **kwargs

* *args - args collector
* **kwargs - keyword args collector

## lambda - function

* one liner functions
* used in - `map`, `filter`, `reduce` 

## problems

* palindrome check
* sum of numbers
* Game: Rock, Paper, Scissors
