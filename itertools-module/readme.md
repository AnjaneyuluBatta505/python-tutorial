# Python - Itertools Module

* `itertools` is a built-in module
* It provides fast, memory-efficient way of looping through iterables

## Infinite iterators

1. count(start, step)
2. cycle(sequence)
3. repeat(element, n_times)

### count(start, step)

```python
from itertools import count

def count_10():
    counter = count(start=1)
    for num in counter:
        print(num)
        if num == 10:
            break
```

### cycle(sequence)

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

```python
from itertools import accumulate

total = accumulate([1,2,3,4,5], lambda x, y: x + y)
print(total)
```

### chain(iter1, iter2, ...)

```python
from itertools import chain

alphabets = ['a', 'b', 'c']
numbers = [1,2,3]
iterator = chain(alphabets, numbers)
for item in iterator:
    print(item)
```

### chain.from_iterable([iter1, iter2, ...])

```python
from itertools import chain

iterator = chain.from_iterable([[1,2], {3,4}, 'ABC'])
for item initerator:
    print(item)
```

### compress(data, selectors)

```python
from itertools import compress

data = 'ABCDEF'
selectors = [1, 0, 1, 0, 1, 1]

result = compress(data, selectors)

for item in result:
    print(item)
```

### dropwhile(predicate, iterable)

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

```python
from collections import islice

iterator = islice("hello python", 0, 8, 2)
for item in iterator:
    print(item)
```

## Combinatoric iterators

