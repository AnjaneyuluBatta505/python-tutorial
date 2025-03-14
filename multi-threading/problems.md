# Multithreading

## 1. Creating and Running a Thread
**Problem:** Write a Python program that creates and starts a thread to print numbers from 1 to 10.

## 2. Using `Thread` with Arguments
**Problem:** Modify the previous program so that the thread takes a start and end number as arguments.

## 3. Multiple Threads Execution
**Problem:** Create three threads, each printing a different message with a slight delay.

## 4. Thread Synchronization with `Lock`
**Problem:** Write a program where multiple threads try to update a shared counter, but use a `Lock` to prevent race conditions.

## 5. Using `RLock` for Reentrant Locking
**Problem:** Create a program where a function requires nested locking, and use `RLock` to handle it safely.

## 6. Threading with `join()`
**Problem:** Modify a multithreading program to ensure all threads complete execution before the main thread proceeds.

## 7. Daemon vs Non-Daemon Threads
**Problem:** Create a program where a daemon thread runs in the background, logging timestamps every second.

## 8. Using `ThreadPoolExecutor`
**Problem:** Use `ThreadPoolExecutor` to run a function with multiple sets of arguments in parallel.

## 9. Shared Resource Management with `Semaphore`
**Problem:** Implement a program where only three threads can access a shared resource at the same time.

## 10. Producer-Consumer Problem using `Queue`
**Problem:** Create a producer-consumer model where one thread produces items and another thread consumes them using `queue.Queue`.

## 11. Implementing a Thread-safe Singleton Class
**Problem:** Implement a thread-safe Singleton pattern using a `Lock` to ensure only one instance is created.

## 12. Thread Communication with `Event`
**Problem:** Write a program where one thread waits for a signal from another thread before continuing.

## 13. Using `Condition` for Synchronization
**Problem:** Implement a scenario where a consumer waits for a producer to produce an item before consuming it.

## 14. Using `Barrier` to Synchronize Threads
**Problem:** Create a program where multiple threads wait at a `Barrier` before proceeding further.

## 15. Using `Timer` for Delayed Execution
**Problem:** Create a function that runs after a specified delay using `threading.Timer`.

## 16. Using `local()` for Thread-local Data
**Problem:** Implement a scenario where different threads store different values using `threading.local()`.

## 17. Handling Exceptions in Threads
**Problem:** Create a program where a thread raises an exception and ensure it is caught and logged properly.

## 18. Implementing a Multithreaded Web Scraper
**Problem:** Write a program where multiple threads fetch data from different URLs in parallel.

## 19. Comparing Single-threaded vs Multithreaded Execution
**Problem:** Compare the execution time of a CPU-bound operation (e.g., computing Fibonacci numbers) using both a single thread and multiple threads.

## 20. Parallel File Processing
**Problem:** Write a program that reads multiple files in parallel using threads and merges the content into a single output file.

