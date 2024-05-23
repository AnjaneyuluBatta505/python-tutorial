# Python - Collections Module

## namedtuple
1. Create a namedtuple called `Point` to represent a 2D point with `x` and `y` coordinates. Instantiate it and print the coordinates.
2. Extend the `Point` namedtuple to a 3D point by adding a `z` coordinate.
3. Write a function that calculates the distance between two `Point` namedtuples.
4. Create a namedtuple called `Rectangle` to represent a rectangle with `width` and `height` attributes. Write a method to compute the area.
5. Write a function to check if a given point is inside a rectangle defined by two points (bottom-left and top-right corners).
6. Create a namedtuple called `Student` with `name`, `age`, and `grade`. Write a function to return students with grades above a certain threshold.
7. Write a function to sort a list of `Student` namedtuples by their grades in descending order.
8. Create a namedtuple called `Car` with `make`, `model`, and `year`. Write a function to filter cars older than a given year.
9. Write a function to convert a list of dictionaries to a list of `namedtuple` objects.
10. Create a namedtuple called `Employee` with `name`, `position`, and `salary`. Write a method to give a raise to an employee.

## dequeue

11.  Create a `deque` of integers from 1 to 10. Perform and print the results of basic operations: append, appendleft, pop, and popleft.
12.  Write a function to rotate a `deque` n steps to the right.
13.  Implement a queue using a `deque`. Provide methods for enqueue and dequeue.
14.  Implement a stack using a `deque`. Provide methods for push and pop.
15.  Write a function to reverse the elements in a `deque`.
16.  Write a function to find the maximum and minimum elements in a `deque`.
17.  Implement a sliding window maximum function using a `deque`.
18.  Write a function to remove all instances of a given value from a `deque`.
19.  Create a `deque` and perform insert operations at both ends. Print the final `deque`.
20.  Write a function to merge two deques into one.

## Counter

21.  Count the occurrences of each character in a string using `Counter`.
22.  Write a function to count the frequency of words in a given text using `Counter`.
23.  Write a function to find the most common element in a list using `Counter`.
24.  Write a function to find the least common element in a list using `Counter`.
25.  Use `Counter` to count the number of each type of item in a list of tuples representing items and their types.
26.  Write a function to find elements that appear more than n times in a list using `Counter`.
27.  Write a function to compare two `Counter` objects and return the elements that are common.
28.  Write a function to subtract counts of one `Counter` from another.
29.  Write a function to merge two `Counter` objects by adding their counts.
30.  Write a function to convert a `Counter` object to a dictionary.

## OrderedDict

31.  Create an `OrderedDict` and perform basic operations like setting, getting, and deleting items. Print the results.
32.  Write a function to check if two `OrderedDict` objects are equal.
33.  Write a function to move a specified item to the end of an `OrderedDict`.
34.  Write a function to pop the first item from an `OrderedDict`.
35.  Write a function to sort an `OrderedDict` by keys.
36.  Write a function to sort an `OrderedDict` by values.
37.  Write a function to convert a dictionary to an `OrderedDict`.
38.  Write a function to merge two `OrderedDict` objects.
39.  Write a function to reverse the order of items in an `OrderedDict`.
40.  Create an `OrderedDict` to count the occurrences of elements in a list while maintaining their order of first occurrence.

## defaultdict

41.  Create a `defaultdict` with default type `int`. Perform basic operations like setting and getting items. Print the results.
42.  Write a function to group words by their first letter using a `defaultdict` of lists.
43.  Write a function to count the frequency of characters in a string using `defaultdict`.
44.  Write a function to create a nested dictionary using `defaultdict`.
45.  Write a function to merge two `defaultdict` objects.
46.  Write a function to create a `defaultdict` of sets and demonstrate adding items.
47.  Write a function to convert a regular dictionary to a `defaultdict`.
48.  Write a function to remove all entries from a `defaultdict`.
49.  Write a function to find the longest list in a `defaultdict` of lists.
50.  Create a `defaultdict` to store the index positions of each element in a list.

## ChainMap

51.  Create two dictionaries and merge them using `ChainMap`. Access values from the merged map.
52.  Write a function to update a key-value pair in a `ChainMap`.
53.  Write a function to add a new dictionary to an existing `ChainMap`.
54.  Write a function to remove the first dictionary from a `ChainMap`.
55.  Write a function to check if a key exists in a `ChainMap`.
56.  Write a function to find the length of a `ChainMap`.
57.  Write a function to iterate over all key-value pairs in a `ChainMap`.
58.  Write a function to convert a `ChainMap` to a regular dictionary.
59.  Write a function to filter `ChainMap` items based on a condition.
60.  Write a function to access nested dictionaries using `ChainMap`.
