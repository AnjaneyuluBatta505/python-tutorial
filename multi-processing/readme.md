# Multiprocessing

* Python's **multiprocessing** module allows for parallel execution of tasks, leveraging multiple CPU cores to improve performance.
* Unlike threads, which suffer from the Global Interpreter Lock (GIL), **multiprocessing** spawns separate processes, each with its own memory space, allowing true parallel execution.

## Why Use Multiprocessing?
- **Bypasses GIL:** Enables true parallelism by utilizing multiple CPU cores.
- **Efficient for CPU-bound tasks:** Ideal for tasks involving heavy computations like data processing, image processing, etc.
- **Separate Memory Space:** Prevents memory corruption issues common in multi-threading.
- **Process-Based Parallelism:** Each process runs independently, reducing interference.

## Setting Up Multiprocessing
The `multiprocessing` module provides several components to manage parallel execution:
- `Process` for creating new processes
- `Queue` and `Pipe` for inter-process communication
- `Pool` for managing multiple worker processes efficiently
- `Manager` for shared objects

## 1. Creating and Running Processes
The `Process` class is used to create a new process.

```python
import multiprocessing

def worker_function(name):
    print(f"Hello from {name}")

if __name__ == "__main__":
    process = multiprocessing.Process(target=worker_function, args=("Process 1",))
    process.start()
    process.join()  # Wait for the process to finish
```

### Explanation:
- `Process(target=function, args=(arguments,))` creates a new process.
- `.start()` initiates execution.
- `.join()` ensures the main program waits for process completion.

## 2. Using Multiple Processes
```python
import multiprocessing

def worker(num):
    print(f"Worker {num} executing")

if __name__ == "__main__":
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()
```

## 3. Using a Process Pool
A `Pool` simplifies process management by creating a pool of worker processes.

```python
from multiprocessing import Pool

def square(num):
    return num * num

if __name__ == "__main__":
    with Pool(4) as p:  # Create a pool with 4 processes
        results = p.map(square, [1, 2, 3, 4, 5])
    print(results)
```

### Benefits:
- **`map()`** applies a function to multiple inputs in parallel.
- **Automatic worker management** ensures efficient CPU usage.

## 4. Inter-Process Communication (IPC)
Processes don’t share memory, so data exchange requires **Queues** or **Pipes**.

### Using a Queue:
```python
import multiprocessing

def worker(queue):
    queue.put("Hello from worker")

if __name__ == "__main__":
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=worker, args=(q,))
    p.start()
    print(q.get())  # Retrieve data from the queue
    p.join()
```

### Using a Pipe:
```python
import multiprocessing

def sender(pipe):
    pipe.send("Hello from sender")

def receiver(pipe):
    print(pipe.recv())

if __name__ == "__main__":
    parent_conn, child_conn = multiprocessing.Pipe()
    p1 = multiprocessing.Process(target=sender, args=(child_conn,))
    p2 = multiprocessing.Process(target=receiver, args=(parent_conn,))
    
    p1.start()
    p2.start()
    p1.join()
    p2.join()
```

## 5. Shared Memory
Using `multiprocessing.Value` or `multiprocessing.Array`, processes can share data safely.

```python
import multiprocessing

def increment(shared_value):
    shared_value.value += 1

if __name__ == "__main__":
    value = multiprocessing.Value('i', 0)  # 'i' stands for integer
    processes = [multiprocessing.Process(target=increment, args=(value,)) for _ in range(5)]
    
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    
    print("Final value:", value.value)
```

## 6. Process Synchronization
### Using Locks:
To prevent race conditions:
```python
import multiprocessing

def task(lock, counter):
    with lock:  # Lock acquired
        counter.value += 1

if __name__ == "__main__":
    lock = multiprocessing.Lock()
    counter = multiprocessing.Value('i', 0)
    
    processes = [multiprocessing.Process(target=task, args=(lock, counter)) for _ in range(5)]
    
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    
    print("Final counter value:", counter.value)
```

## 7. Multiprocessing vs Threading
| Feature | Multiprocessing | Threading |
|---------|---------------|----------|
| Memory Usage | Separate memory per process | Shared memory space |
| Performance | Ideal for CPU-bound tasks | Ideal for I/O-bound tasks |
| GIL Impact | Not affected (true parallelism) | Affected (GIL limits execution) |
| Context Switching | Higher overhead | Lower overhead |

## 8. When to Use Multiprocessing?
- **Heavy computation** (e.g., numerical simulations, image processing)
- **Parallel data processing** (e.g., large dataset operations, AI model training)
- **Avoiding GIL bottleneck** (e.g., multi-core CPUs performing independent tasks)

## 9. Common Pitfalls and Best Practices
- **Use `if __name__ == "__main__":`** → Required to avoid infinite process spawning.
- **Avoid sharing state between processes** → Prefer `Queue`, `Pipe`, or `Manager`.
- **Be cautious with `fork()` on macOS** → Python 3.8+ uses `spawn()` by default.
- **Limit the number of processes** → Avoid excessive overhead.
