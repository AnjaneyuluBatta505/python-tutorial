# **Pthon - File handling**

### Why file handling?

* storing application logs
* image handling to convert RGB to Gray scale, etc.
* Invoice PDF generation
* uploading files to cloud i.e AWS, GCP, Azure, etc.
* importing and exporting the data to/from db servers
* much more....

### Open - built-in function

* `open` is python built-in function to read and write data from/to files on the disk.
* File opening modes
  * `r` - read
  * `a` - append
  * `w` - write
  * `x` - create
  * `t` - text
  * `b` - binary
* Can use multiple modes at the same time like `rw`, `ra` , `rb` , etc.

### Read contents of file

example:

```python
file = open("story.txt", "r")
contents = file.read()
print(contents)
file.close()
```

* Reading methods
  * read()
  * readlines()

### Write contents to file

```python
file = open("file-handling/hello.txt", "w")
text = "Once upon a time there lived a lion king."
file.write(text)
file.close()
```

* Writing methods
  * write(text)
  * writelines(iterable)
    * list, set, tuple, etc
  * flush() - writes the contents to the disk.

### File attributes

* name - Returns the name of the file.
* mode - Returns the I/O mode for the file.
* encoding - Returns the encoding of the file.
* closed - Returns a Boolean stating whether the file is closed.
* errors - Returns the Unicode error handler used along with the encoding.
* newlines - Return type of newlines encountered while reading the file.

example:

```python
file = open("story.txt", "r")
contents = file.read()
print("File attributes")
print("name", file.name)
print("mode", file.mode)
print("encoding", file.encoding)
print("closed", file.closed)
print("errors", file.errors)
print("newlines", file.newlines)
file.close()
```

### **Appending to files**

```python
file = open("file-handling/hello.txt", "a")
text = "Once upon a time there live a lion king."
file.write(text)
file.close()
```

### **Working with binary files**

```python
file = open('file-handling/learnbatta-logo.png', 'rb')
data = file.read()
print(data)
file.close()
```

### Other file methods

* close() - close the opened file
* tell() - return file cursor current position
* seek(position) - Sets the file cursor's current position.

### using `with` keyword

```python
with open("file-handling/hello.txt", "r") as file:
    content = file.read()
    print(content)
```

### Questions

* Read the `sample_products.csv` file and print the all product name
* Add new product info `90,variation,woo-hoodie-blue-logo,Hoodie-Blue Yes` to the above file.
* Create new file `students.csv` and add names "Anji", "John", "Shiva", "Jimmy", "David" to it.
