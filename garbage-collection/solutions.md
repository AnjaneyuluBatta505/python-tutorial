# Garbage Collection

## **Basic Concepts**

### **1. What is garbage collection in Python, and why is it needed?**
**Solution:**  
Garbage collection in Python is the process of automatically identifying and deallocating unused objects to free memory. It is needed to manage memory efficiently and prevent memory leaks.

---

### **2. How does Python's memory management system handle object allocation and deallocation?**
**Solution:**  
Python uses automatic memory management that relies on reference counting and cyclic garbage collection. Objects are deallocated when their reference count drops to zero.

---

### **3. What are reference counting and cyclic garbage collection?**
**Solution:**  
- **Reference Counting:** Each object keeps track of the number of references to it. When the reference count reaches zero, the object is deleted.
- **Cyclic Garbage Collection:** Python detects and removes cyclic references where objects reference each other but are no longer needed.

---

### **4. How can you manually trigger garbage collection in Python?**
**Solution:**  
You can manually trigger garbage collection using:
```python
import gc
gc.collect()
```

This forces Python to perform garbage collection immediately.

---

### **5. What happens when `gc.collect()` is called?**
**Solution:**  
`gc.collect()` forces Python's garbage collector to check for unreachable objects and free up memory. It returns the number of objects collected.

---

## **Working with the `gc` Module**

### **6. How do you enable and disable automatic garbage collection in Python?**
**Solution:**  
- To disable garbage collection:
  ```python
  import gc
  gc.disable()
  ```

- To enable garbage collection:
  ```python
  gc.enable()
  ```

---

### **7. What is the purpose of `gc.get_stats()`? How can it be used to monitor memory usage?**
**Solution:**  
`gc.get_stats()` returns statistics about Python's garbage collection system, useful for monitoring memory allocation:
```python
import gc
print(gc.get_stats())
```

---

### **8. How do you check which objects are currently being tracked by the garbage collector?**
**Solution:**  
Use `gc.get_objects()` to list all objects currently tracked:
```python
import gc
print(gc.get_objects())
```

---

### **9. What is the difference between `gc.get_objects()` and `gc.get_referrers()`?**
**Solution:**  
- `gc.get_objects()`: Returns all objects tracked by the garbage collector.
- `gc.get_referrers(obj)`: Returns all objects that reference `obj`.

Example:
```python
import gc
obj = []
print(gc.get_referrers(obj))
```

---

### **10. How can you manually free up memory using the `gc` module?**
**Solution:**  
Call `gc.collect()` to free unused memory:
```python
import gc
gc.collect()
```

---

## **Understanding Reference Counting**

### **11. How does Python's reference counting mechanism work?**
**Solution:**  
Each object in Python has a reference count that tracks how many references point to it. When the count reaches zero, Python deletes the object.

---

### **12. How can you check the reference count of an object?**
**Solution:**  
Use `sys.getrefcount(obj)`:
```python
import sys
obj = []
print(sys.getrefcount(obj))  # Includes an extra reference from getrefcount itself
```

---

### **13. What happens if an object has circular references? How does Python handle it?**
**Solution:**  
Python's reference counting cannot detect cyclic references. The garbage collector periodically detects and removes them.

---

### **14. How do weak references help in garbage collection?**
**Solution:**  
Weak references allow objects to be referenced without increasing their reference count. The `weakref` module is used for this purpose:
```python
import weakref

class Example:
    pass

obj = Example()
weak_obj = weakref.ref(obj)
print(weak_obj())  # Access the object
del obj
print(weak_obj())  # Returns None since object is deleted
```

---

### **15. How do you check the current garbage collection thresholds?**
**Solution:**  
Use `gc.get_threshold()`:
```python
import gc
print(gc.get_threshold())
```

---

### **16. How can you modify garbage collection thresholds?**
**Solution:**  
Adjust thresholds using `gc.set_threshold()`:
```python
import gc
gc.set_threshold(700, 10, 5)
```

---

### **17. How can you disable garbage collection for performance reasons?**
**Solution:**  
Use `gc.disable()`:
```python
import gc
gc.disable()
```

This can be useful in performance-critical applications where manual memory management is preferred.

---

### **18. How do you collect only a specific generation in garbage collection?**
**Solution:**  
You can specify a generation (0, 1, or 2) in `gc.collect()`:
```python
import gc
gc.collect(0)  # Collect only the youngest generation
```

---

### **19. How do you debug memory leaks using the `gc` module?**
**Solution:**  
Enable debugging with:
```python
import gc
gc.set_debug(gc.DEBUG_LEAK)
```

This will print details about unreachable objects.

---

### **20. How do you list all objects that are part of a reference cycle?**
**Solution:**  
Use `gc.garbage` after a collection:
```python
import gc
gc.collect()
print(gc.garbage)
```

---
