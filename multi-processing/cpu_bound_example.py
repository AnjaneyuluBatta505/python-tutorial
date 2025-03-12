import multiprocessing
import time

# Function to compute the sum of squares in a given range
def sum_of_squares(start, end):
    return sum(i * i for i in range(start, end))

# Sequential Execution
def sequential_execution(n):
    start_time = time.time()
    result = sum_of_squares(0, n)
    end_time = time.time()
    print(f"Sequential Execution Result: {result}")
    print(f"Sequential Execution Time: {end_time - start_time:.2f} seconds\n")

# Multiprocessing Execution
def multiprocessing_execution(n, num_processes):
    start_time = time.time()
    chunk_size = n // num_processes
    pool = multiprocessing.Pool(processes=num_processes)

    # Divide the task into chunks
    ranges = [(i * chunk_size, (i + 1) * chunk_size) for i in range(num_processes)]
    
    # Perform parallel computation
    results = pool.starmap(sum_of_squares, ranges)
    
    pool.close()
    pool.join()

    total_result = sum(results)
    end_time = time.time()
    
    print(f"Multiprocessing Execution Result: {total_result}")
    print(f"Multiprocessing Execution Time: {end_time - start_time:.2f} seconds\n")

if __name__ == "__main__":
    N = 10**7  # Large number to simulate heavy computation
    NUM_PROCESSES = multiprocessing.cpu_count()  # Use all available CPU cores

    print("Running Sequential Execution...")
    sequential_execution(N)

    print(f"Running Multiprocessing Execution with {NUM_PROCESSES} processes...")
    multiprocessing_execution(N, NUM_PROCESSES)
