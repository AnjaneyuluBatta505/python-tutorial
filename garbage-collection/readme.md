# Garbage Collection

* Garbage collection (GC) in Python is the process of automatically managing memory by reclaiming unused objects.
* Python has an automatic garbage collector that deallocates memory occupied by objects that are no longer in use.
* This helps in efficient memory management and prevents memory leaks.

## Memory Management in Python
Python uses **reference counting** and **cyclic garbage collection** to manage memory. When an object's reference count drops to zero, it becomes eligible for garbage collection.

### Reference Counting
Every Python object has an associated reference count, which indicates the number of references pointing to that object. When the reference count reaches zero, Python automatically deallocates the memory occupied by the object.

#### Example of Reference Counting:
```python
import sys

x = [1, 2, 3]  # Creating a list
print(sys.getrefcount(x))  # Checking reference count

y = x  # Assigning x to another variable
print(sys.getrefcount(x))  # Reference count increases

del x  # Deleting one reference
print(sys.getrefcount(y))  # Still has references, so not collected
```

### Circular References and Cyclic Garbage Collection
A circular reference occurs when objects reference each other, making reference counting insufficient for garbage collection. Python’s **cyclic garbage collector** detects and removes such objects.

#### Example of Circular Reference:
```python
import gc

class Node:
    def __init__(self):
        self.reference = None

node1 = Node()
node2 = Node()
node1.reference = node2
node2.reference = node1  # Circular reference

del node1, node2  # Objects are not immediately garbage collected
print(gc.collect())  # Explicitly running garbage collector
```

## Python's Garbage Collection Mechanism
Python uses a **generational garbage collector** that classifies objects into three generations:
- **Generation 0**: Newly created objects.
- **Generation 1**: Survived one collection cycle.
- **Generation 2**: Long-lived objects.

Python collects garbage more frequently in younger generations than in older ones.

## Controlling Garbage Collection
The `gc` module in Python provides control over garbage collection.

### Checking and Forcing Collection
```python
import gc

gc.collect()  # Manually trigger garbage collection
```

### Enabling and Disabling GC
```python
gc.disable()  # Disable automatic garbage collection
gc.enable()   # Enable automatic garbage collection
```

### Setting Collection Thresholds
```python
gc.set_threshold(700, 10, 5)  # Adjusting GC thresholds
```

## Best Practices for Memory Management
- **Avoid circular references** by using weak references (`weakref` module).
- **Manually delete objects** when they are no longer needed.
- **Use context managers (`with` statement)** to manage resource cleanup.
- **Profile memory usage** with tools like `objgraph` and `memory_profiler`.
