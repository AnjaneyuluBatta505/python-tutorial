# Network Programming

## **Socket Programming**

### **1. Create a simple TCP server that listens on a specific port and echoes back messages from clients.**

```python
import socket

# Create a TCP server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)
print("Server listening on port 12345...")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")
    message = client_socket.recv(1024).decode('utf-8')
    print(f"Received: {message}")
    client_socket.send(message.encode('utf-8'))
    client_socket.close()
```

---

### **2. Write a Python TCP client that connects to a server, sends a message, and prints the response.**

```python
import socket

# Create a TCP client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

message = "Hello, Server!"
client_socket.send(message.encode('utf-8'))
response = client_socket.recv(1024).decode('utf-8')
print(f"Server response: {response}")
client_socket.close()
```

---

### **3. Implement a UDP server that receives messages from clients and prints them.**

```python
import socket

# Create a UDP server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 12345))

print("UDP Server listening on port 12345...")

while True:
    message, addr = server_socket.recvfrom(1024)
    print(f"Received from {addr}: {message.decode('utf-8')}")
```

---

### **4. Develop a UDP client that sends a message to a UDP server and waits for a response.**

```python
import socket

# Create a UDP client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = "Hello, UDP Server!"
client_socket.sendto(message.encode('utf-8'), ('localhost', 12345))

response, addr = client_socket.recvfrom(1024)
print(f"Server response: {response.decode('utf-8')}")
client_socket.close()
```

---

### **5. Create a simple chat application using Python sockets that allows two users to communicate.**

```python
# Server Code
import socket
import threading

def handle_client(client_socket):
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        if not message:
            break
        print(f"Received: {message}")
        client_socket.send(message.encode('utf-8'))
    client_socket.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)
print("Chat server listening on port 12345...")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")
    threading.Thread(target=handle_client, args=(client_socket,)).start()

# Client Code
import socket
import threading

def receive_messages(client_socket):
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        print(f"Received: {message}")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

threading.Thread(target=receive_messages, args=(client_socket,)).start()

while True:
    message = input("Enter message: ")
    client_socket.send(message.encode('utf-8'))
```

---

### **6. Write a multi-threaded TCP server that can handle multiple clients simultaneously.**

```python
import socket
import threading

def handle_client(client_socket):
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        if not message:
            break
        print(f"Received: {message}")
        client_socket.send(message.encode('utf-8'))
    client_socket.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)
print("Multi-threaded server listening on port 12345...")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")
    threading.Thread(target=handle_client, args=(client_socket,)).start()
```

---

### **7. Implement a simple file transfer system using sockets to send and receive files.**

```python
# Server Code
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)
print("File server listening on port 12345...")

client_socket, addr = server_socket.accept()
print(f"Connection from {addr}")

file_name = client_socket.recv(1024).decode('utf-8')
with open(file_name, 'wb') as file:
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        file.write(data)
print(f"File {file_name} received.")
client_socket.close()

# Client Code
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

file_name = "example.txt"
client_socket.send(file_name.encode('utf-8'))

with open(file_name, 'rb') as file:
    while True:
        data = file.read(1024)
        if not data:
            break
        client_socket.send(data)
print(f"File {file_name} sent.")
client_socket.close()
```

---

### **8. Write a program to resolve a domain name to its IP address using Python's `socket` module.**

```python
import socket

domain = "www.google.com"
ip_address = socket.gethostbyname(domain)
print(f"IP Address of {domain}: {ip_address}")
```

---

### **9. Develop a network scanner using sockets to check which ports are open on a given IP address.**

```python
import socket

def scan_ports(ip, start_port, end_port):
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()

scan_ports("127.0.0.1", 1, 1024)
```

---

### **10. Build a Python script that fetches the public IP address of the system using an external service.**

```python
import requests

response = requests.get("https://api.ipify.org?format=json")
public_ip = response.json()['ip']
print(f"Public IP Address: {public_ip}")
```

---

## **Requests Module (HTTP Programming)**

### **11. Write a Python script that sends a GET request to a URL and prints the response.**

```python
import requests

response = requests.get("https://www.example.com")
print(response.text)
```

---

### **12. Implement a script to send a POST request with JSON data to an API and print the response.**

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts"
data = {"title": "foo", "body": "bar", "userId": 1}
response = requests.post(url, json=data)
print(response.json())
```

---

### **13. Develop a web scraper that fetches and displays all links from a given webpage.**

```python
import requests
from bs4 import BeautifulSoup

url = "https://www.example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))
```

---

### **14. Create a Python program to download an image from a URL and save it to disk.**

```python
import requests

url = "https://www.example.com/image.jpg"
response = requests.get(url)

with open("image.jpg", "wb") as file:
    file.write(response.content)
print("Image downloaded.")
```

---

### **15. Implement an API client that fetches weather information using an external weather API.**

```python
import requests

api_key = "your_api_key"
city = "London"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
response = requests.get(url)
weather_data = response.json()
print(weather_data)
```

---

## **SMTP and Email Handling**

### **16. Write a Python script using `smtplib` to send an email using an SMTP server.**

```python
import smtplib

sender = "your_email@example.com"
receiver = "receiver_email@example.com"
password = "your_password"

message = """Subject: Hello
This is a test email."""

with smtplib.SMTP("smtp.example.com", 587) as server:
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, receiver, message)
print("Email sent.")
```

---

### **17. Modify the email sender script to attach a file and send it via email.**

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

sender = "your_email@example.com"
receiver = "receiver_email@example.com"
password = "your_password"

msg = MIMEMultipart()
msg['Subject'] = "Email with Attachment"
msg['From'] = sender
msg['To'] = receiver

attachment = open("example.txt", "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="example.txt"')
msg.attach(part)

with smtplib.SMTP("smtp.example.com", 587) as server:
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, receiver, msg.as_string())
print("Email with attachment sent.")
```

---

### **18. Develop an email automation script that sends periodic reminders using SMTP.**

```python
import smtplib
import time

def send_reminder():
    sender = "your_email@example.com"
    receiver = "receiver_email@example.com"
    password = "your_password"

    message = """Subject: Reminder
This is a reminder email."""

    with smtplib.SMTP("smtp.example.com", 587) as server:
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, message)
    print("Reminder sent.")

while True:
    send_reminder()
    time.sleep(3600)  # Send every hour
```

---

### **19. Implement an IMAP email client that reads unread emails from a Gmail inbox.**

```python
import imaplib
import email

mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login("your_email@gmail.com", "your_password")
mail.select("inbox")

status, messages = mail.search(None, "UNSEEN")
for msg_id in messages[0].split():
    status, msg_data = mail.fetch(msg_id, "(RFC822)")
    for response_part in msg_data:
        if isinstance(response_part, tuple):
            msg = email.message_from_bytes(response_part[1])
            print(f"From: {msg['from']}")
            print(f"Subject: {msg['subject']}")
            print(f"Body: {msg.get_payload()}")
```

---

### **20. Create a simple email validation program that checks if an email address is properly formatted and exists.**

```python
import re
import smtplib

def validate_email(email):
    # Check format
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False
    # Check existence
    try:
        domain = email.split('@')[1]
        smtp_server = smtplib.SMTP(domain)
        smtp_server.quit()
        return True
    except:
        return False

email = "test@example.com"
if validate_email(email):
    print(f"{email} is valid.")
else:
    print(f"{email} is invalid.")
```

---
