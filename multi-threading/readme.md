# Multi-threading

* Python's multi-threading allows a program to execute multiple threads (smaller units of a process) concurrently.
* It is useful for tasks like I/O operations, network requests, and GUI applications.
* However, due to Python's Global Interpreter Lock (GIL), multi-threading is not ideal for CPU-bound tasks.

## **1. Understanding Threads**
* A thread is the smallest unit of execution in a process.
* Multi-threading allows running multiple threads simultaneously, improving efficiency for I/O-bound tasks.

### **1.1 When to Use Multi-threading**
Multi-threading is useful when:
- Performing multiple I/O-bound operations simultaneously
- Running network calls without blocking the main program
- Handling multiple user interactions in GUI applications

However, for CPU-bound tasks (e.g., mathematical computations), multiprocessing is preferred due to the GIL.

### **1.2 Global Interpreter Lock (GIL)**
The GIL is a mutex in CPython that allows only one thread to execute Python bytecode at a time. This means that even in multi-threaded programs, Python executes only one thread at a time per process.

To overcome this limitation for CPU-bound tasks, use the `multiprocessing` module instead.

---

## **2. Creating and Running Threads**
Python provides the `threading` module for handling threads.

### **2.1 Creating a Basic Thread**
```python
import threading

def print_hello():
    print("Hello from thread!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()  # Wait for the thread to complete
```

### **2.2 Creating Multiple Threads**
```python
def print_numbers():
    for i in range(5):
        print(f"Number: {i}")

threads = []
for _ in range(3):  # Creating 3 threads
    t = threading.Thread(target=print_numbers)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
```

---

## **3. Using Thread Class (Extending `Thread`)**
Threads can be created by subclassing `threading.Thread`.
```python
class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            print(f"Thread {self.name}: {i}")

thread1 = MyThread()
thread2 = MyThread()
thread1.start()
thread2.start()
thread1.join()
thread2.join()
```

---

## **4. Synchronization and Locks**
To prevent race conditions, Python provides `threading.Lock()`.

### **4.1 Using Locks**
```python
lock = threading.Lock()
counter = 0

def increment():
    global counter
    with lock:  # Ensures only one thread modifies the variable at a time
        counter += 1

threads = [threading.Thread(target=increment) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print("Final counter value:", counter)
```

---

## **5. Thread Communication with Queues**
Threads can communicate safely using the `queue` module.

```python
import queue

def worker(q):
    while not q.empty():
        item = q.get()
        print(f"Processing {item}")
        q.task_done()

q = queue.Queue()
for i in range(5):
    q.put(i)

threads = [threading.Thread(target=worker, args=(q,)) for _ in range(2)]
for t in threads:
    t.start()
q.join()
```

---

## **6. Daemon Threads**
Daemon threads run in the background and exit when the main program terminates.
```python
def background_task():
    while True:
        print("Running in background")

thread = threading.Thread(target=background_task, daemon=True)
thread.start()
```

---

## **7. Thread Pooling with `concurrent.futures`**
The `ThreadPoolExecutor` makes managing multiple threads easier.
```python
from concurrent.futures import ThreadPoolExecutor

def square(n):
    return n * n

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(square, range(10))
    print(list(results))
```

---

## **8. Handling Exceptions in Threads**
```python
def faulty_function():
    raise ValueError("An error occurred!")

def thread_function():
    try:
        faulty_function()
    except Exception as e:
        print(f"Caught an exception: {e}")

thread = threading.Thread(target=thread_function)
thread.start()
thread.join()
```

---

## **Conclusion**

* Python's multi-threading is a powerful tool for handling I/O-bound tasks but is limited by the GIL for CPU-bound tasks.
* For CPU-intensive tasks, consider using the `multiprocessing` module. 🚀

