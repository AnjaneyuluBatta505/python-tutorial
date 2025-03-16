# Multiprocessing

## **Problem 1: Creating a Simple Process**

### **Solution:**
```python
from multiprocessing import Process

def hello():
    print("Hello from process")

if __name__ == "__main__":
    p = Process(target=hello)
    p.start()
    p.join()
```

---

## **Problem 2: Passing Arguments to Process**
```python
from multiprocessing import Process

def greet(name):
    print(f"Hello, {name}")

if __name__ == "__main__":
    p = Process(target=greet, args=("Alice",))
    p.start()
    p.join()
```

---

## **Problem 3: Multiple Processes**
```python
from multiprocessing import Process

def print_msg(msg):
    print(msg)

if __name__ == "__main__":
    messages = ["Process 1", "Process 2", "Process 3"]
    processes = [Process(target=print_msg, args=(msg,)) for msg in messages]

    for p in processes:
        p.start()

    for p in processes:
        p.join()
```

---

## **Problem 4: Daemon Processes**
```python
from multiprocessing import Process
import time

def background_task():
    while True:
        print("Daemon process running...")
        time.sleep(1)

if __name__ == "__main__":
    p = Process(target=background_task)
    p.daemon = True
    p.start()
    time.sleep(3)
    print("Main process exits")
```

---

## **Problem 5: Terminating a Process**
```python
from multiprocessing import Process
import time

def task():
    while True:
        print("Running...")
        time.sleep(1)

if __name__ == "__main__":
    p = Process(target=task)
    p.start()
    time.sleep(3)
    p.terminate()
    print("Process terminated")
```

---

## **Problem 6: Shared Memory with Value**
```python
from multiprocessing import Process, Value

def increment(shared_val):
    shared_val.value += 1

if __name__ == "__main__":
    num = Value('i', 0)
    p1 = Process(target=increment, args=(num,))
    p2 = Process(target=increment, args=(num,))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    print(f"Final value: {num.value}")
```

---

## **Problem 7: Shared Memory with Array**
```python
from multiprocessing import Process, Array

def update_array(arr):
    for i in range(len(arr)):
        arr[i] += 1

if __name__ == "__main__":
    shared_arr = Array('i', [1, 2, 3, 4, 5])
    p = Process(target=update_array, args=(shared_arr,))
    p.start()
    p.join()
    print(list(shared_arr))
```

---

## **Problem 8: Using Locks**
```python
from multiprocessing import Process, Lock

def critical_section(lock, msg):
    with lock:
        print(msg)

if __name__ == "__main__":
    lock = Lock()
    p1 = Process(target=critical_section, args=(lock, "Process 1"))
    p2 = Process(target=critical_section, args=(lock, "Process 2"))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
```

---

## **Problem 9: Using Queue for Inter-Process Communication**
```python
from multiprocessing import Process, Queue

def producer(q):
    q.put("Hello from producer")

def consumer(q):
    print(q.get())

if __name__ == "__main__":
    q = Queue()
    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=consumer, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
```

---

## **Problem 10: Using Pipe for Communication**
```python
from multiprocessing import Process, Pipe

def send_msg(conn):
    conn.send("Hello from child process")
    conn.close()

if __name__ == "__main__":
    parent_conn, child_conn = Pipe()
    p = Process(target=send_msg, args=(child_conn,))
    
    p.start()
    print(parent_conn.recv())  
    p.join()
```

---

## **Problem 11: Using Manager for Shared Dictionary**
```python
from multiprocessing import Process, Manager

def update_dict(shared_dict):
    shared_dict["key"] = "value"

if __name__ == "__main__":
    with Manager() as manager:
        shared_dict = manager.dict()
        p = Process(target=update_dict, args=(shared_dict,))
        
        p.start()
        p.join()
        
        print(shared_dict)
```

---

## **Problem 12: Using Pool for Parallel Execution**
```python
from multiprocessing import Pool

def square(n):
    return n * n

if __name__ == "__main__":
    with Pool(4) as p:
        print(p.map(square, [1, 2, 3, 4, 5]))
```

---

## **Problem 13: Using Condition for Synchronization**
```python
from multiprocessing import Process, Condition
import time

def task(cond):
    with cond:
        print("Waiting for condition...")
        cond.wait()
        print("Condition met, resuming task!")

if __name__ == "__main__":
    cond = Condition()
    p = Process(target=task, args=(cond,))
    
    p.start()
    time.sleep(2)
    
    with cond:
        cond.notify()
    
    p.join()
```

---

## **Problem 14: Using Event for Process Synchronization**
```python
from multiprocessing import Process, Event
import time

def worker(event):
    print("Worker waiting for event...")
    event.wait()
    print("Worker received event signal!")

if __name__ == "__main__":
    event = Event()
    p = Process(target=worker, args=(event,))
    p.start()
    
    time.sleep(2)
    event.set()
    
    p.join()
```

---

## **Problem 15: Using Barrier for Synchronization**
```python
from multiprocessing import Process, Barrier

def worker(barrier):
    print("Waiting at barrier...")
    barrier.wait()
    print("Barrier passed!")

if __name__ == "__main__":
    barrier = Barrier(2)
    p1 = Process(target=worker, args=(barrier,))
    p2 = Process(target=worker, args=(barrier,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
```

---

## **Problem 16: Using Semaphore for Controlling Access**
```python
from multiprocessing import Process, Semaphore
import time

def task(sem):
    sem.acquire()
    print("Task started")
    time.sleep(2)
    print("Task completed")
    sem.release()

if __name__ == "__main__":
    sem = Semaphore(2)
    processes = [Process(target=task, args=(sem,)) for _ in range(4)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()
```

---

## **Problem 17: Using Manager for Shared List**
```python
from multiprocessing import Process, Manager

def modify_list(shared_list):
    shared_list.append("new item")

if __name__ == "__main__":
    with Manager() as manager:
        shared_list = manager.list()
        p = Process(target=modify_list, args=(shared_list,))
        
        p.start()
        p.join()
        
        print(shared_list)
```

---

## **Problem 18: Using Pool Apply**
```python
from multiprocessing import Pool

def cube(n):
    return n ** 3

if __name__ == "__main__":
    with Pool(4) as p:
        print(p.apply(cube, (3,)))
```

---

## **Problem 19: Using Queue for Producer-Consumer Model**
```python
from multiprocessing import Process, Queue
import time

def producer(q):
    for i in range(5):
        q.put(i)
        time.sleep(1)

def consumer(q):
    while not q.empty():
        print(q.get())

if __name__ == "__main__":
    q = Queue()
    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=consumer, args=(q,))

    p1.start()
    p1.join()
    p2.start()
    p2.join()
```

## **Problem 20: Using Process Pool Executor**

```python
from concurrent.futures import ProcessPoolExecutor

def square(n):
    return n * n

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(square, numbers))

    print("Squared numbers:", results)
```
