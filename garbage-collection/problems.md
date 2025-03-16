# Garbage Collection

## **Basic Concepts**
1. What is garbage collection in Python, and why is it needed?
2. How does Python's memory management system handle object allocation and deallocation?
3. What are reference counting and cyclic garbage collection?
4. How can you manually trigger garbage collection in Python?
5. What happens when `gc.collect()` is called?

## **Working with the `gc` Module**
6. How do you enable and disable automatic garbage collection in Python?
7. What is the purpose of `gc.get_stats()`? How can it be used to monitor memory usage?
8. How do you check which objects are currently being tracked by the garbage collector?
9. What is the difference between `gc.get_objects()` and `gc.get_referrers()`?
10. How can you manually free up memory using the `gc` module?

## **Understanding Reference Counting**
11. How does Python's reference counting mechanism work?
12. How can you check the reference count of an object?
13. What happens if an object has circular references? How does Python handle it?
14. What is the impact of circular references on memory management?
15. Why might manually managing memory using `del` not always be effective?

## **Advanced Garbage Collection Control**
16. How does `gc.set_debug()` help in debugging memory leaks?
17. What are the different garbage collection generations in Python?
18. How can you tune the garbage collector using `gc.set_threshold()`?
19. How do weak references (`weakref` module) help in avoiding cyclic garbage collection issues?
20. What are some real-world scenarios where manually managing garbage collection can improve performance?

