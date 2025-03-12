import threading
import time
import requests

# List of real-world URLs to download
URLS = [
    "https://www.python.org",
    "https://www.wikipedia.org",
    "https://www.nytimes.com",
    "https://www.bbc.com",
    "https://www.cnn.com",
]

def download_file(url):
    """Function to download content from a given URL."""
    print(f"Downloading from {url}...\n")
    response = requests.get(url, timeout=10)  # 10 seconds timeout
    print(f"Finished downloading {url}: {len(response.content)} bytes\n")

# Sequential execution
def sequential_download():
    start_time = time.time()
    for url in URLS:
        download_file(url)
    end_time = time.time()
    print(f"Sequential Execution Time: {end_time - start_time:.2f} seconds\n")

# Multi-threaded execution
def threaded_download():
    start_time = time.time()
    threads = []
    
    for url in URLS:
        thread = threading.Thread(target=download_file, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"Threaded Execution Time: {end_time - start_time:.2f} seconds\n")

if __name__ == "__main__":
    print("Starting Sequential Download...")
    sequential_download()

    print("Starting Multi-threaded Download...")
    threaded_download()
