# Network Programming

* Network programming involves writing programs that communicate over a computer network.
* Python provides a rich set of libraries for handling network-related tasks, such as socket programming, HTTP requests, and working with protocols like FTP and SMTP.

## Basics of Networking
Before diving into Python’s network programming capabilities, it's essential to understand some fundamental networking concepts:
- **IP Address**: A unique identifier for a device on a network.
- **Port**: A numerical label assigned to a specific process/service on a device.
- **Socket**: An endpoint for communication between two devices.
- **Protocol**: A set of rules that govern network communication (e.g., TCP, UDP, HTTP, FTP).

## Python’s Networking Modules
Python provides several modules for network programming, including:
- `socket` – Low-level networking interface.
- `http.client` – HTTP protocol handling.
- `urllib` – Fetching data across the web.
- `requests` – Simplified HTTP requests.
- `ftplib` – FTP protocol handling.
- `smtplib` – Email sending via SMTP.
- `paramiko` – SSH handling.
- `asyncio` – Asynchronous networking.

## Socket Programming
The `socket` module in Python provides an interface for network communication using sockets.

### Creating a Simple Server
```python
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 12345))
server_socket.listen(5)
print("Server is listening on port 12345...")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Connection established with {addr}")
    client_socket.send(b"Hello from server!")
    client_socket.close()
```

### Creating a Simple Client
```python
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 12345))
message = client_socket.recv(1024)
print("Received from server:", message.decode())
client_socket.close()
```

## Working with HTTP
Python provides the `requests` module for working with HTTP requests.

### Sending an HTTP GET Request
```python
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.json())
```

### Sending an HTTP POST Request
```python
import requests

data = {"title": "Hello", "body": "This is a test", "userId": 1}
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)
print(response.json())
```

## FTP File Transfer
The `ftplib` module allows working with FTP servers.

### Uploading a File to an FTP Server
```python
from ftplib import FTP

ftp = FTP("ftp.dlptest.com")
ftp.login("dlpuser", "rNrKYTX9g7z3RgJRmxWuGHbeu")
with open("test.txt", "rb") as file:
    ftp.storbinary("STOR test.txt", file)
ftp.quit()
```

## Sending Emails using SMTP
The `smtplib` module allows sending emails.

### Sending an Email
```python
import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("your_email@gmail.com", "your_password")
server.sendmail("your_email@gmail.com", "recipient@example.com", "Subject: Test\n\nHello, this is a test email!")
server.quit()
```

## Secure Communication with Paramiko (SSH)
Paramiko allows handling SSH connections in Python.

### Connecting to a Remote Server via SSH
```python
import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect("your_ssh_server", username="user", password="pass")
stdin, stdout, stderr = client.exec_command("ls")
print(stdout.read().decode())
client.close()
```

## Asynchronous Network Programming with Asyncio
Asyncio allows handling multiple network tasks asynchronously.

### Asynchronous HTTP Requests
```python
import asyncio
import aiohttp

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    data = await fetch("https://jsonplaceholder.typicode.com/posts/1")
    print(data)

asyncio.run(main())
```
