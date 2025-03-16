# Multiprocessing

## 1. Creating and Running a Process
**Problem:** Write a Python program that creates and starts a new process that prints numbers from 1 to 10.  
**Use Case:** Used in applications where independent tasks can run in parallel, like handling multiple user requests.

## 2. Using `Process` with Arguments
**Problem:** Modify the previous program so that the process takes a start and end number as arguments.  
**Use Case:** Useful for batch processing tasks where each process works on different data ranges.

## 3. Multiple Processes Execution
**Problem:** Create three separate processes, each printing a different message.  
**Use Case:** Ideal for multi-tasking scenarios, such as handling multiple clients in a server.

## 4. Using `join()` to Wait for Processes
**Problem:** Modify a multiprocessing program to ensure all processes complete execution before the main process continues.  
**Use Case:** Ensures dependent tasks execute in the correct order, such as generating reports after data collection.

## 5. Using `Pool` for Process Management
**Problem:** Implement a program that uses `multiprocessing.Pool` to run a function with multiple sets of arguments in parallel.  
**Use Case:** Used in image/video processing applications where multiple files need to be processed simultaneously.

## 6. Sharing Data Between Processes with `Value`
**Problem:** Create a program where two processes increment a shared counter using `multiprocessing.Value`.  
**Use Case:** Useful in scenarios where a global counter is required, like counting website visits.

## 7. Sharing Data Between Processes with `Array`
**Problem:** Implement a program where multiple processes update a shared array and print the final result.  
**Use Case:** Helps in parallel numerical computations, like matrix operations.

## 8. Inter-Process Communication (IPC) with `Queue`
**Problem:** Write a producer-consumer program where a producer process adds items to a `multiprocessing.Queue`, and a consumer process removes them.  
**Use Case:** Used in logging systems where multiple processes log data, and another process writes logs to a file.

## 9. Process Synchronization Using `Lock`
**Problem:** Implement a program where multiple processes try to update a shared resource, but use a `multiprocessing.Lock` to prevent race conditions.  
**Use Case:** Used in banking transactions where multiple processes modify account balances.

## 10. Process Synchronization Using `Semaphore`
**Problem:** Implement a program where only three processes can access a shared resource at the same time using `multiprocessing.Semaphore`.  
**Use Case:** Helps manage resource constraints, like controlling access to a database.

## 11. Using `Manager` to Share Complex Data Structures
**Problem:** Create a program where multiple processes update a shared list using `multiprocessing.Manager().list()`.  
**Use Case:** Used in distributed systems where multiple processes need shared data storage.

## 12. Using `Condition` for Process Synchronization
**Problem:** Implement a scenario where a consumer process waits for a producer to produce an item before consuming it.  
**Use Case:** Helps in workflow automation, ensuring one step completes before another starts.

## 13. Using `Event` for Process Communication
**Problem:** Create a program where one process signals another process using `multiprocessing.Event()`.  
**Use Case:** Useful for triggering background tasks when an event occurs, such as auto-saving a file when changes are detected.

## 14. Using `Barrier` for Synchronization
**Problem:** Implement a program where multiple processes wait at a `multiprocessing.Barrier` before proceeding.  
**Use Case:** Used in parallel computing tasks where processes must synchronize at certain checkpoints.

## 15. Multiprocessing with `Pipe`
**Problem:** Implement a program where two processes communicate using `multiprocessing.Pipe()`.  
**Use Case:** Helps in inter-process communication, such as data exchange between microservices.

## 16. Handling Exceptions in Child Processes
**Problem:** Write a program where a child process raises an exception and ensure it is caught and logged properly.  
**Use Case:** Critical for debugging and monitoring systems running multiple processes.

## 17. Comparing Single-Process vs Multiprocessing Execution
**Problem:** Compare the execution time of a CPU-bound operation (e.g., calculating prime numbers) using both a single process and multiple processes.  
**Use Case:** Helps understand performance improvements in CPU-intensive tasks like cryptography and machine learning.

## 18. Using `multiprocessing.Queue` for Parallel File Processing
**Problem:** Write a program that reads multiple files in parallel using separate processes and merges the content into a single output file.  
**Use Case:** Speeds up log analysis and data aggregation from multiple sources.

## 19. Creating a Multithreading + Multiprocessing Hybrid Program
**Problem:** Implement a program that uses **both** multiprocessing and multithreading for a task, such as downloading files using processes and processing data using threads.  
**Use Case:** Enhances efficiency in scenarios like web scraping and data extraction.

## 20. Building a Multiprocessing Web Scraper
**Problem:** Write a program where multiple processes fetch data from different URLs in parallel and store the results in a shared list.  
**Use Case:** Used for large-scale data collection from websites, APIs, or social media.

