# Python – Tkinter & Turtle

Python provides two powerful libraries for creating GUI applications and graphical drawings:

- **Tkinter**: A standard Python library for building graphical user interfaces (GUIs).
- **Turtle**: A simple drawing library that helps visualize programming concepts.

This document covers everything about Tkinter and Turtle, including their usage, features, and examples.

---

# Part 1: Tkinter – GUI Programming

## What is Tkinter?
Tkinter is Python’s standard GUI library. It allows developers to create windows, buttons, text boxes, and other widgets easily.

### Installing Tkinter
Tkinter comes pre-installed with Python. However, if it is missing, install it using:
```sh
pip install tk
```

### Creating a Simple Tkinter Window
```python
import tkinter as tk

root = tk.Tk()
root.title("Simple Tkinter Window")
root.geometry("400x300")

label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 14))
label.pack()

root.mainloop()
```

### Basic Tkinter Widgets
1. **Label** – Displays text.
2. **Button** – Executes a function when clicked.
3. **Entry** – Accepts user input.
4. **Text** – Multiline text input.
5. **Frame** – Container for widgets.
6. **Canvas** – Used for graphics.

#### Example: Tkinter Button & Entry
```python
import tkinter as tk

def greet():
    name = entry.get()
    label.config(text=f"Hello, {name}!")

root = tk.Tk()
root.title("Greeting App")

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Greet", command=greet)
button.pack()

label = tk.Label(root, text="Enter your name")
label.pack()

root.mainloop()
```

### Tkinter Layout Managers
1. **pack()** – Arranges widgets vertically or horizontally.
2. **grid()** – Places widgets in a grid layout.
3. **place()** – Positions widgets at exact coordinates.

#### Example: Grid Layout
```python
import tkinter as tk

root = tk.Tk()

label1 = tk.Label(root, text="Row 0, Column 0")
label1.grid(row=0, column=0)

label2 = tk.Label(root, text="Row 0, Column 1")
label2.grid(row=0, column=1)

label3 = tk.Label(root, text="Row 1, Column 0")
label3.grid(row=1, column=0)

root.mainloop()
```

### Tkinter Message Box
```python
import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Message", "Hello, Tkinter!")

root = tk.Tk()
button = tk.Button(root, text="Show Message", command=show_message)
button.pack()
root.mainloop()
```

---

# Part 2: Turtle – Graphics Programming

## What is Turtle?
Turtle is a Python module that allows for simple drawing using a virtual pen (turtle). It is useful for teaching programming concepts visually.

### Installing Turtle
Turtle comes pre-installed with Python. No additional installation is required.

### Basic Turtle Example
```python
import turtle

t = turtle.Turtle()
t.forward(100)
t.right(90)
t.forward(100)
turtle.done()
```

### Turtle Commands
1. **forward(x)** – Moves turtle forward by x units.
2. **backward(x)** – Moves turtle backward by x units.
3. **right(deg)** – Turns turtle right by specified degrees.
4. **left(deg)** – Turns turtle left by specified degrees.
5. **penup()** – Lifts the pen (no drawing).
6. **pendown()** – Puts the pen down (starts drawing).
7. **goto(x, y)** – Moves turtle to coordinates (x, y).

### Drawing a Square
```python
import turtle

t = turtle.Turtle()
for _ in range(4):
    t.forward(100)
    t.right(90)

turtle.done()
```

### Drawing a Circle
```python
import turtle

t = turtle.Turtle()
t.circle(50)
turtle.done()
```

### Changing Pen Color and Size
```python
import turtle

t = turtle.Turtle()
t.pensize(5)
t.pencolor("red")
t.forward(100)
turtle.done()
```

### Drawing a Star
```python
import turtle

t = turtle.Turtle()
for _ in range(5):
    t.forward(100)
    t.right(144)

turtle.done()
```
