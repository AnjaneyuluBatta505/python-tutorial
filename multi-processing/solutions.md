# Multiprocessing

## 1. Creating and Running a Process
Problem: Write a Python program that creates and starts a new process that prints numbers from 1 to 10.

```python
import multiprocessing

def print_numbers():
    for i in range(1, 11):
        print(i)

if __name__ == "__main__":
    process = multiprocessing.Process(target=print_numbers)
    process.start()
    process.join()
```
---

## 2. Using Process with Arguments
Problem: Modify the previous program so that the process takes a start and end number as arguments.

```python
import multiprocessing

def print_numbers(start, end):
    for i in range(start, end + 1):
        print(i)

if __name__ == "__main__":
    process = multiprocessing.Process(target=print_numbers, args=(1, 10))
    process.start()
    process.join()
```
---

## 3. Multiple Processes Execution
Problem: Create three separate processes, each printing a different message.
```python
import multiprocessing

def print_message(message):
    print(message)

if __name__ == "__main__":
    messages = ["Hello", "World", "Multiprocessing"]
    processes = []

    for message in messages:
        process = multiprocessing.Process(target=print_message, args=(message,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
```
---

## 4. Using join() to Wait for Processes
Problem: Modify a multiprocessing program to ensure all processes complete execution before the main process continues.

```python
import multiprocessing
import time

def worker(name):
    print(f"{name} started")
    time.sleep(2)
    print(f"{name} finished")

if __name__ == "__main__":
    processes = []

    for i in range(3):
        process = multiprocessing.Process(target=worker, args=(f"Process-{i+1}",))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print("All processes finished")
```
---

## 5. Using Pool for Process Management
Problem: Implement a program that uses multiprocessing.Pool to run a function with multiple sets of arguments in parallel.

```python
import multiprocessing

def square(x):
    return x * x

if __name__ == "__main__":
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(square, range(10))
    print(results)
```
---

## 6. Sharing Data Between Processes with Value
Problem: Create a program where two processes increment a shared counter using multiprocessing.Value.

```python
import multiprocessing

def increment_counter(counter):
    for _ in range(1000):
        counter.value += 1

if __name__ == "__main__":
    counter = multiprocessing.Value('i', 0)
    processes = []

    for _ in range(2):
        process = multiprocessing.Process(target=increment_counter, args=(counter,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(f"Final counter value: {counter.value}")
```
---

## 7. Sharing Data Between Processes with Array
Problem: Implement a program where multiple processes update a shared array and print the final result.
```python
import multiprocessing

def update_array(index, array):
    array[index] = array[index] * 2

if __name__ == "__main__":
    array = multiprocessing.Array('i', [1, 2, 3, 4, 5])
    processes = []

    for i in range(len(array)):
        process = multiprocessing.Process(target=update_array, args=(i, array))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(f"Final array: {list(array)}")
```
---

## 8. Inter-Process Communication (IPC) with Queue
Problem: Write a producer-consumer program where a producer process adds items to a multiprocessing.Queue, and a consumer process removes them.
```python
import multiprocessing
import time

def producer(queue):
    for i in range(5):
        print(f"Producing {i}")
        queue.put(i)
        time.sleep(1)

def consumer(queue):
    while True:
        item = queue.get()
        if item is None:  # Sentinel value to stop the consumer
            break
        print(f"Consuming {item}")

if __name__ == "__main__":
    queue = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=producer, args=(queue,))
    p2 = multiprocessing.Process(target=consumer, args=(queue,))

    p1.start()
    p2.start()

    p1.join()
    queue.put(None)  # Signal the consumer to stop
    p2.join()
```
---

## 9. Process Synchronization Using Lock
Problem: Implement a program where multiple processes try to update a shared resource, but use a multiprocessing.Lock to prevent race conditions.

```python
import multiprocessing

def worker(lock, shared_value):
    with lock:
        shared_value.value += 1

if __name__ == "__main__":
    lock = multiprocessing.Lock()
    shared_value = multiprocessing.Value('i', 0)
    processes = []

    for _ in range(10):
        process = multiprocessing.Process(target=worker, args=(lock, shared_value))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(f"Final value: {shared_value.value}")
```
---

## 10. Process Synchronization Using Semaphore
Problem: Implement a program where only three processes can access a shared resource at the same time using multiprocessing.Semaphore.

```python
import multiprocessing
import time

def worker(semaphore, name):
    with semaphore:
        print(f"{name} is accessing the resource")
        time.sleep(2)
        print(f"{name} is releasing the resource")

if __name__ == "__main__":
    semaphore = multiprocessing.Semaphore(3)
    processes = []

    for i in range(10):
        process = multiprocessing.Process(target=worker, args=(semaphore, f"Process-{i+1}"))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
```
---

## 11. Using Manager to Share Complex Data Structures
Problem: Create a program where multiple processes update a shared list using multiprocessing.Manager().list().

```python
import multiprocessing

def update_list(index, shared_list):
    shared_list[index] = shared_list[index] * 2

if __name__ == "__main__":
    with multiprocessing.Manager() as manager:
        shared_list = manager.list([1, 2, 3, 4, 5])
        processes = []

        for i in range(len(shared_list)):
            process = multiprocessing.Process(target=update_list, args=(i, shared_list))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()

        print(f"Final list: {list(shared_list)}")
```
---

## 12. Using Condition for Process Synchronization
Problem: Implement a scenario where a consumer process waits for a producer to produce an item before consuming it.

```python
import multiprocessing
import time

def producer(condition, queue):
    for i in range(5):
        with condition:
            queue.put(i)
            print(f"Produced {i}")
            condition.notify()
        time.sleep(1)

def consumer(condition, queue):
    while True:
        with condition:
            while queue.empty():
                condition.wait()
            item = queue.get()
            if item is None:  # Sentinel value to stop the consumer
                break
            print(f"Consumed {item}")

if __name__ == "__main__":
    condition = multiprocessing.Condition()
    queue = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=producer, args=(condition, queue))
    p2 = multiprocessing.Process(target=consumer, args=(condition, queue))

    p1.start()
    p2.start()

    p1.join()
    queue.put(None)  # Signal the consumer to stop
    p2.join()
```
---

## 13. Using Event for Process Communication
Problem: Create a program where one process signals another process using multiprocessing.Event().

```python
import multiprocessing
import time

def worker(event):
    print("Worker is waiting for the event")
    event.wait()
    print("Worker received the event")

if __name__ == "__main__":
    event = multiprocessing.Event()
    process = multiprocessing.Process(target=worker, args=(event,))

    process.start()
    time.sleep(2)
    print("Main process is setting the event")
    event.set()
    process.join()
```
---

## 14. Using Barrier for Synchronization
Problem: Implement a program where multiple processes wait at a multiprocessing.Barrier before proceeding.

```python
import multiprocessing
import time

def worker(barrier, name):
    print(f"{name} is waiting at the barrier")
    barrier.wait()
    print(f"{name} passed the barrier")

if __name__ == "__main__":
    barrier = multiprocessing.Barrier(3)
    processes = []

    for i in range(3):
        process = multiprocessing.Process(target=worker, args=(barrier, f"Process-{i+1}"))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
```
---

## 15. Multiprocessing with Pipe
Problem: Implement a program where two processes communicate using multiprocessing.Pipe().

```python
import multiprocessing

def sender(conn):
    conn.send("Hello from sender")
    conn.close()

def receiver(conn):
    message = conn.recv()
    print(f"Received: {message}")
    conn.close()

if __name__ == "__main__":
    parent_conn, child_conn = multiprocessing.Pipe()

    p1 = multiprocessing.Process(target=sender, args=(child_conn,))
    p2 = multiprocessing.Process(target=receiver, args=(parent_conn,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
```
---

## 16. Handling Exceptions in Child Processes
Problem: Write a program where a child process raises an exception and ensure it is caught and logged properly.

```python
import multiprocessing
import traceback

def worker():
    try:
        raise ValueError("An error occurred in the child process")
    except Exception as e:
        print(f"Caught exception: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    process = multiprocessing.Process(target=worker)
    process.start()
    process.join()
```
---

## 17. Comparing Single-Process vs Multiprocessing Execution
Problem: Compare the execution time of a CPU-bound operation (e.g., calculating prime numbers) using both a single process and multiple processes.

```python
import multiprocessing
import time

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(start, end):
    return [n for n in range(start, end) if is_prime(n)]

def single_process():
    start_time = time.time()
    find_primes(1, 100000)
    print(f"Single-process time: {time.time() - start_time}")

def multi_process():
    start_time = time.time()
    with multiprocessing.Pool(processes=4) as pool:
        pool.starmap(find_primes, [(1, 25000), (25000, 50000), (50000, 75000), (75000, 100000)])
    print(f"Multiprocessing time: {time.time() - start_time}")

if __name__ == "__main__":
    single_process()
    multi_process()
```
---

## 18. Using multiprocessing.Queue for Parallel File Processing
Problem: Write a program that reads multiple files in parallel using separate processes and merges the content into a single output file.

```python
import multiprocessing

def read_file(file, queue):
    with open(file, 'r') as f:
        content = f.read()
    queue.put(content)

if __name__ == "__main__":
    files = ["file1.txt", "file2.txt", "file3.txt"]
    queue = multiprocessing.Queue()
    processes = []

    for file in files:
        process = multiprocessing.Process(target=read_file, args=(file, queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    with open("output.txt", 'w') as f:
        while not queue.empty():
            f.write(queue.get())
```
---

## 19. Creating a Multithreading + Multiprocessing Hybrid Program
Problem: Implement a program that uses both multiprocessing and multithreading for a task, such as downloading files using processes and processing data using threads.

```python
import multiprocessing
import threading
import time

def download_file(url):
    print(f"Downloading {url}")
    time.sleep(2)
    print(f"Finished downloading {url}")

def process_data(data):
    print(f"Processing {data}")
    time.sleep(1)
    print(f"Finished processing {data}")

def worker(url):
    download_file(url)
    threads = []
    for i in range(3):
        thread = threading.Thread(target=process_data, args=(f"Data-{i}",))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    urls = ["url1", "url2", "url3"]
    processes = []

    for url in urls:
        process = multiprocessing.Process(target=worker, args=(url,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
```
---

## 20. Building a Multiprocessing Web Scraper
Problem: Write a program where multiple processes fetch data from different URLs in parallel and store the results in a shared list.

```python
import multiprocessing
import requests

def fetch_url(url, shared_list):
    response = requests.get(url)
    shared_list.append(response.text[:100])  # Store first 100 characters

if __name__ == "__main__":
    urls = ["https://example.com", "https://example.org", "https://example.net"]
    with multiprocessing.Manager() as manager:
        shared_list = manager.list()
        processes = []

        for url in urls:
            process = multiprocessing.Process(target=fetch_url, args=(url, shared_list))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()

        print(f"Fetched data: {list(shared_list)}")

```
