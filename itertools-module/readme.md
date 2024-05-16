# Python - Itertools Module

* `itertools` is a built-in module
* It provides fast, memory-efficient way of looping through iterables

## Infinite iterators

1. count(start, step)
2. cycle(sequence)
3. repeat(element, n_times)

### count(start, step)

* count is a infinite iterator

```python
from itertools import count

counter = count(start=1)
for num in counter:
    print(num)
    if num == 10:
        break
```

### cycle(sequence)

* cycle() function accepts an iterable and generates an infinite iterator

```python
from itertools import cycle

iter = cycle([1, 2, 3])
count = 0
for num in iter:
    print(num)
    count += 1
    if count == 5:
        break
```

### repeat(element, n_times)

* it repeats the given element n number of times if defined otherwise it will repeat it endlessly.

```python
from itertools import repeat

iter = repeat(2, 10)
for num in iter:
    print(num)
```

## Functions

1. accumulate(iterabe, function)
2. chain(iter1, iter2, ...)
3. chain.from_iterable([iter1, iter2, ...])
4. compress()
5. dropwhile()
6. filterfalse()
7. groupby()
8. islice()
9. pairwise()
10. starmap()
11. takewhile()
12. tee()

### accumulate(iterable, func)

* It accumulates the given iterable with operator.add or any other function if provided.

```python
from itertools import accumulate

iterator = accumulate([1,2,3,4,5], lambda x, y: x + y)
for item in iterator:
    print(item)
```

### chain(iter1, iter2, ...)

* `itertools.chain` is a generator function which accepts iterables as arguments.

```python
from itertools import chain

alphabets = ['a', 'b', 'c']
numbers = [1,2,3]
iterator = chain(alphabets, numbers)
for item in iterator:
    print(item)
```

### chain.from_iterable([iter1, iter2, ...])

* it's an alternate constructor for `itertools.chain`.

```python
from itertools import chain

iterator = chain.from_iterable([[1,2], {3,4}, 'ABC'])
for item in iterator:
    print(item)
```

### compress(data, selectors)

* Make an iterator that filters elements from data returning only those that have a corresponding element in selectors that evaluates to True.

```python
from itertools import compress

data = 'ABCDEF'
selectors = [1, 0, 1, 0, 1, 1]

result = compress(data, selectors)

for item in result:
    print(item)
```

### dropwhile(predicate, iterable)

* Make an iterator that drops elements from the iterable as long as the predicate is `True`;

```python
from itertools import dropwhile

def predicate(x):
    return x < 5

data = [1, 4, 6, 4, 1]

result = dropwhile(predicate, data)

for item in result:
    print(item)
```

### filterfalse(predicate, iterable)

* Make an iterator that filters elements from iterable returning only those for which the predicate is `False`.

```python
from itertools import filterfalse

def predicate(x):
    return x % 2 == 0

data = [1, 2, 3, 4, 5, 6]

result = filterfalse(predicate, data)

for item in result:
    print(item)
```

### group_by(iterable, key)

* Make an iterator that returns consecutive keys and groups from the iterable.

```python
from itertools import groupby

data = [
    {'name': 'satyajit', 'address': 'btm', 'pin': 560076},
    {'name': 'Preetam', 'address': 'btm', 'pin': 560076},
    {'name': 'Mukul', 'address': 'Silk board', 'pin': 560078},
]

iterator = groupby(data, lambda x: x['pin'])
for key, group in iterator:
    print(key, list(group))
```

### islice(iterable, start, stop, step)

* Make an iterator that returns selected elements from the iterable.

```python
from itertools import islice

iterator = islice("hello python", 0, 8, 2)
for item in iterator:
    print(item)
```

### pairwise(iterable)

* Return successive overlapping pairs taken from the input iterable.

```python
from itertools import pairwise

iterator = pairwise('ABCD')
for pair in iterator:
    print(pair)
```

### starmap(function, iterable)

* Make an iterator that computes the function using arguments obtained from the iterable.

```python
from itertools import starmap

def add(x, y):
    return x + y

arguments = [(1, 2), (3, 4)]

result = starmap(add, arguments)

for item in result:
    print(item)
```

### takewhile(predicate, iterable)

* Make an iterator that returns elements from the iterable as long as the predicate is true.

```python
from itertools import takewhile

def less_than_6(num):
    return num < 6

data = [1, 2, 3, 6, 4, 1]

result = takewhile(less_than_6, data)

for item in result:
    print(item)
```

### tee(iterator, n)

* Return n independent iterators from a single iterable.

```python
from itertools import tee

items = [1,2,3,4]

iterables = tee(items, 2)
for item in iterables[0]:
    print(item)

for item in iterables[1]:
    print(item)
```

### zip_longest(iter1, iter2, fillvalue)

* Make an iterator that aggregates elements from each of the iterables.

```python
from itertools import zip_longest

students = ["A", "B", "C", "D"]
grades = [1, 2]
iterator = zip_longest(students, grades, fillvalue="-")

for item in iterator:
    print(item)
```

## Combinatoric iterators

### product(*iterables, repeat=1)

* Cartesian product of input iterables.

```python
from itertools import product

s1 = 'AB'
s2 = 'DE'
iterator = product(s1,s2)

for item in iterator:
    print(item)
```

### permutations(iterable, r=None)

* Return r length subsequences of elements from the input iterable.

```python
from itertools import permutations

data = [1, 2, 3]

result = permutations(data, 2)

for perm in result:
    print(perm)
```

### combinations(iterable, r)

* Return r length subsequences of elements from the input iterable.

```python
from itertools import combinations

numbers = [1,2,3]
iterator = combinations(numbers, r=2)

for item in iterator:
    print(item)
```

### combinations_with_replacement(iterable, r)

* Return r length subsequences of elements from the input iterable allowing individual elements to be repeated more than once.

```python
from itertools import combinations_with_replacement

iterator = combinations_with_replacement(numbers, r=2)

for item in iterator:
    print(item)
```






.
