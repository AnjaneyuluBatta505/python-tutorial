# SQLAlchemy

* SQLAlchemy is a powerful SQL toolkit and Object Relational Mapper (ORM) for Python.
* It allows developers to interact with databases in a more Pythonic way while maintaining flexibility and efficiency.


Install SQLAlchemy using:
```sh
pip install sqlalchemy
```

---

## Step 1: Understanding Core Concepts
SQLAlchemy consists of two main components:
1. **SQLAlchemy Core**: Provides a SQL abstraction layer for constructing and executing raw SQL queries.
2. **SQLAlchemy ORM**: Allows mapping of Python classes to database tables and provides an interface for working with database records as objects.

---

## Step 2: Setting Up SQLAlchemy
### Create a Database Connection
```python
from sqlalchemy import create_engine

# SQLite example
db_url = 'sqlite:///example.db'
engine = create_engine(db_url, echo=True)
```
- `create_engine()` creates a connection to the database.
- `echo=True` enables logging of SQL queries for debugging.

### Creating a Session
```python
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()
```
- `sessionmaker()` is used to create a session to interact with the database.

---

## Step 3: Defining Tables and Models
### Using SQLAlchemy Core
```python
from sqlalchemy import Table, Column, Integer, String, MetaData

metadata = MetaData()
users = Table(
    'users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('age', Integer)
)
metadata.create_all(engine)  # Creates the table
```

### Using SQLAlchemy ORM
```python
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

Base.metadata.create_all(engine)  # Creates the table
```

---

## Step 4: Performing CRUD Operations
### Insert Data
```python
new_user = User(name="John Doe", age=30)
session.add(new_user)
session.commit()
```

### Query Data
```python
users = session.query(User).all()
for user in users:
    print(user.name, user.age)
```

### Update Data
```python
user = session.query(User).filter_by(name="John Doe").first()
user.age = 31
session.commit()
```

### Delete Data
```python
user = session.query(User).filter_by(name="John Doe").first()
session.delete(user)
session.commit()
```

---

## Step 5: Relationships Between Tables
### One-to-Many Relationship
```python
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    email = Column(String)
    user = relationship("User", back_populates="addresses")

User.addresses = relationship("Address", back_populates="user")
Base.metadata.create_all(engine)
```

---

## Step 6: Using Advanced Features
### Transactions
```python
try:
    session.add(new_user)
    session.commit()
except:
    session.rollback()
```

### Asynchronous SQLAlchemy (Using Asyncio)
```python
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

async_engine = create_async_engine("sqlite+aiosqlite:///example.db")
async_session = AsyncSession(async_engine)
```

---

## Step 7: Working with Alembic for Migrations
Alembic is a migration tool for SQLAlchemy.
```sh
pip install alembic
alembic init alembic
```
Modify `alembic.ini` and `env.py` to connect to the database, then generate migrations:
```sh
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```

---

## Step 8: Best Practices
- Use **scoped_session** for handling sessions in multi-threaded applications.
- Enable **lazy loading** for relationships to optimize queries.
- Use **bulk inserts** for large datasets.
- Apply **indexing** and **foreign keys** for better performance.
