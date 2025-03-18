# Python – MySQL Database

* MySQL is one of the most popular relational database management systems (RDBMS).
* Python provides several libraries to interact with MySQL databases, with **MySQL Connector/Python** being the official MySQL driver.
* This document covers everything you need to know about working with MySQL in Python.

## Installing MySQL Connector
Before working with MySQL in Python, install the **mysql-connector-python** package:
```sh
pip install mysql-connector-python
```

If you are using an alternative MySQL library, install it using:
```sh
pip install pymysql  # Alternative MySQL library
```

---

## Connecting to MySQL Database
To establish a connection with a MySQL database, use the `mysql.connector` module:

```python
import mysql.connector

# Establish connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="test_db"
)

if conn.is_connected():
    print("Connected to MySQL database")

conn.close()
```

### Connection Parameters
- `host`: The MySQL server address (e.g., `localhost` or `127.0.0.1`)
- `user`: MySQL username
- `password`: MySQL password
- `database`: Name of the database to connect to

---

## Creating a Database
To create a database in MySQL using Python:

```python
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password"
)

cursor = conn.cursor()
cursor.execute("CREATE DATABASE mydatabase")
print("Database created successfully")

conn.close()
```

---

## Creating Tables
To create a table in MySQL:
```python
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="mydatabase"
)

cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100),
        age INT
    )
""")
print("Table created successfully")

conn.close()
```

---

## Inserting Data into MySQL
To insert data into a table:
```python
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="mydatabase"
)

cursor = conn.cursor()
sql = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
values = ("John Doe", "john@example.com", 30)

cursor.execute(sql, values)
conn.commit()
print("Record inserted successfully")

conn.close()
```

### Inserting Multiple Records
```python
values = [
    ("Alice", "alice@example.com", 25),
    ("Bob", "bob@example.com", 28),
    ("Charlie", "charlie@example.com", 32)
]

cursor.executemany(sql, values)
conn.commit()
print(cursor.rowcount, "records inserted")
```

---

## Retrieving Data from MySQL
To fetch data from a table:
```python
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)
```

### Fetching Specific Columns
```python
cursor.execute("SELECT name, email FROM users")
rows = cursor.fetchall()
for row in rows:
    print(f"Name: {row[0]}, Email: {row[1]}")
```

### Fetching a Single Record
```python
cursor.execute("SELECT * FROM users WHERE id = 1")
row = cursor.fetchone()
print(row)
```

---

## Updating Data in MySQL
To update an existing record:
```python
sql = "UPDATE users SET age = %s WHERE name = %s"
values = (35, "John Doe")

cursor.execute(sql, values)
conn.commit()
print(cursor.rowcount, "record(s) updated")
```

---

## Deleting Data from MySQL
To delete a record:
```python
sql = "DELETE FROM users WHERE name = %s"
values = ("John Doe",)

cursor.execute(sql, values)
conn.commit()
print(cursor.rowcount, "record(s) deleted")
```

To delete all records:
```python
cursor.execute("DELETE FROM users")
conn.commit()
```

---

## Handling Errors in MySQL
Use exception handling to manage database errors:
```python
try:
    conn = mysql.connector.connect(host="localhost", user="root", password="wrong_password")
    print("Connected to MySQL")
except mysql.connector.Error as e:
    print("Error:", e)
```

---

## Using Connection Pooling
Connection pooling improves performance by reusing database connections.
```python
from mysql.connector import pooling

pool = pooling.MySQLConnectionPool(
    pool_name="mypool",
    pool_size=3,
    host="localhost",
    user="root",
    password="your_password",
    database="mydatabase"
)

conn = pool.get_connection()
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())
conn.close()
```
