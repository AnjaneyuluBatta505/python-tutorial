# Python - collections module

* It implements additional data structures over built-in data type `list`, `dict` , `set` , `tuple`

| [`namedtuple()`](https://docs.python.org/3/library/collections.html#collections.namedtuple "collections.namedtuple")  | factory function for creating tuple subclasses with named fields                                 |
| ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| [`deque`](https://docs.python.org/3/library/collections.html#collections.deque "collections.deque")                   | list-like container with fast appends and pops on either end                                     |
| [`ChainMap`](https://docs.python.org/3/library/collections.html#collections.ChainMap "collections.ChainMap")          | dict-like class for creating a single view of multiple mappings                                  |
| [`Counter`](https://docs.python.org/3/library/collections.html#collections.Counter "collections.Counter")             | dict subclass for counting[hashable](https://docs.python.org/3/glossary.html#term-hashable) objects |
| [`OrderedDict`](https://docs.python.org/3/library/collections.html#collections.OrderedDict "collections.OrderedDict") | dict subclass that remembers the order entries were added                                        |
| [`defaultdict`](https://docs.python.org/3/library/collections.html#collections.defaultdict "collections.defaultdict") | dict subclass that calls a factory function to supply missing values                             |
| [`UserDict`](https://docs.python.org/3/library/collections.html#collections.UserDict "collections.UserDict")          | wrapper around dictionary objects for easier dict subclassing                                    |
| [`UserList`](https://docs.python.org/3/library/collections.html#collections.UserList "collections.UserList")          | wrapper around list objects for easier list subclassing                                          |
| [`UserString`](https://docs.python.org/3/library/collections.html#collections.UserString "collections.UserString")    | wrapper around string objects for easier string subclassing                                      |

## namedtuple

* Named fields
* Immutable
* Efficient & convenient to create simple classes

```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p1 = Point(1, 2)
```

## dequeue

* doubly ended queue
* It's faster than list & supports operations on both ends

```python
from collections import deque

queue = deque(['apple','banana', 500])
```

* methods:
  * Add
    * `append(item)` - add item to right
    * `appendleft(item)` - add item to left
    * `insert(index, item)` - add item at an index
    * `extend(items)` - add multiple items to right
    * `extendleft(items)` - add multiple items to left
  * Remove
    * `pop()` - remve item from right
    * `popleft()` - remove item from left
    * `remove(item)` - remove first occurence of the item
    * `clear()` - remove all items
  * Other
    * `copy()` - shallow copy of dequeue
    * `count(item)` - number of elements equal to item
    * `index(item, start, stop)` - returns position of item
    * `reverse()` - Reverse the items of the deque in-place and then return None.
    * `rotate(n)` - Rotate the deque *n* steps to the right. If *n* is negative, rotate to the left.
    * `maxlen` - Maximum size of a deque or  `None` if unbounded.

## ChainMap

* `ChainMap` combines multiple dictionaries into one.

```python
from collections import ChainMap

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}

chainmap = ChainMap(d1, d2, d3)
```

* methods

  * `maps()` - Returns a list of all the mappings in the ChainMap
  * `parents` - Returns a new ChainMap containing all but the first mapping from the current ChainMap.
  * `new_child(m)` - Returns a new ChainMap with a new mapping followed by all the mappings from the current ChainMap.
  * `update(*maps)` - Updates the first mapping in the ChainMap with the key-value pairs from the provided mappings.
  * `clear()` - Removes all the mappings from the ChainMap.
  * `copy()`: Returns a shallow copy of the ChainMap.
  * `get(key, default=None)`: Returns the value associated with the key or the default value if the key is not present.
  * `items()`: Returns a new view of the ChainMap's items (key-value pairs).
  * `keys()`: Returns a new view of the ChainMap's keys.
  * `values()`: Returns a new view of the ChainMap's values.
  * `pop(key, default=None)`: Removes and returns the value associated with the key or the default value if the key is not present.
  * `popitem()`: Removes and returns an arbitrary key-value pair from the ChainMap.

## Counter

* subclass of `dict`  and unordered
* used to keep the count of the elements present in an iterable

```python
from collections import Counter

c1 = Counter(['a', 'b', 'a', 'b', 'c'])
c2 = Counter({'a': 2, 'b': 3}})
c3 = Counter(a=2, b=3)
```

* methods:

  * `elements()` - get all elements as iterator
  * `most_common(n)` - returns `n`  number of most common elements
  * `subtract(counter)` - subtracts two counters
  * `total()` - returns sum of all counts
  * `update([iterable-or-mapping])`: Elements are counted from an iterable or added-in from another mapping (or counter).
  * `copy()`: Returns a shallow copy of the counter.
  * `clear()`: Resets all counts to zero. This is equivalent to initializing a Counter object with no arguments.
  * `get(key)`: Returns the count of the element with the specified key. If the key does not exist, returns the default value (which defaults to None).
  * `items()`: Returns a view of the dictionary's (key, count) pairs.
  * `keys()`: Returns a view of the dictionary's keys.
  * `values()`: Returns a view of the dictionary's values.
  * It supports operators like  `+, -, &, |, ==`

## OrderedDict

* Its a sub class of dict that maintains the order of inserted keys
  ```python
  from collections import OrderedDict

  d = OrderedDict([('apple', 100), ('grapes', 200), ('oranges', 300)])
  ```
* Methods:
  * `clear()` : Removes all items from the dictionary.
  * `copy()` : Returns a shallow copy of the dictionary.
  * `fromkeys(iterable)` : Creates a new `OrderedDict` with keys from iterable and values set to value.
  * `items()` : Returns a view object that displays a list of a dictionary's `(key, value)` tuple pairs.
  * `keys()` : Returns a view object that displays a list of the dictionary's keys.
  * `move_to_end(key, last=True)` : Moves the specified key to either end of an ordered dictionary. By default, the key is moved to the last position. If `last` is set to `False`, the key is moved to the beginning.
  * `pop(key)` : Removes the specified key and returns the corresponding value. If the key is not found, the `default` value is returned if given, otherwise a `KeyError` is raised.
  * `popitem(last=True)` : Removes and returns the last inserted `(key, value)` pair. If `last` is `False`, the first inserted pair is removed and returned.
  * `setdefault(key, default=None)` : Returns the value of the specified key. If the key does not exist, inserts the key with the specified default value.
  * `update([other])` : Updates the dictionary with the key-value pairs from `other`, overwriting existing keys if present.
  * `values()` : Returns a view object that displays a list of the dictionary's values.

## defaultdict

## UserDict

## UserList

## UserString
