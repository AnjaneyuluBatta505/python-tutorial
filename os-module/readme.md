# OS Module

* The `os` module in Python provides a way to interact with the operating system.
* It allows performing tasks such as handling files, managing directories, executing system commands, and retrieving system-related information.
* This guide covers all major functionalities of the `os` module with examples.

## **1. Importing the os Module**
Before using the `os` module, it must be imported:
```python
import os
```

## **2. Working with Directories**
The `os` module provides functions to create, delete, and navigate directories.

### **2.1 Get Current Working Directory**
Use `os.getcwd()` to get the current working directory.
```python
import os
print(os.getcwd())  # Output: Current working directory path
```

### **2.2 Change Directory**
Use `os.chdir(path)` to change the current directory.
```python
os.chdir("/path/to/directory")  # Change to a specific directory
print(os.getcwd())  # Verify the new current working directory
```

### **2.3 List Directory Contents**
Use `os.listdir(path)` to list all files and directories.
```python
print(os.listdir("."))  # Lists contents of the current directory
```

### **2.4 Create Directories**
Use `os.mkdir(path)` to create a single directory.
```python
os.mkdir("new_folder")  # Creates a new folder in the current directory
```
Use `os.makedirs(path)` to create nested directories.
```python
os.makedirs("parent/child/grandchild")  # Creates all missing directories
```

### **2.5 Remove Directories**
Use `os.rmdir(path)` to remove an empty directory.
```python
os.rmdir("new_folder")  # Deletes an empty directory
```
Use `os.removedirs(path)` to remove nested directories.
```python
os.removedirs("parent/child/grandchild")  # Removes directories in reverse order
```

## **3. Working with Files**
### **3.1 Rename a File**
```python
os.rename("old_file.txt", "new_file.txt")
```
### **3.2 Remove a File**
```python
os.remove("new_file.txt")  # Deletes the specified file
```

## **4. Environment Variables**
### **4.1 Get Environment Variables**
```python
print(os.environ["HOME"])  # Get the value of the HOME variable
```
Use `os.getenv()` to retrieve an environment variable safely.
```python
print(os.getenv("HOME", "Default Value"))  # Returns 'Default Value' if HOME is not set
```
### **4.2 Set Environment Variables**
```python
os.environ["MY_VAR"] = "Hello"
print(os.getenv("MY_VAR"))  # Output: Hello
```

## **5. Running System Commands**
### **5.1 Execute Shell Commands**
```python
os.system("ls")  # Linux/Mac: List files in the current directory
os.system("dir") # Windows: List files in the current directory
```
### **5.2 Get Output of a System Command**
```python
output = os.popen("ls").read()
print(output)
```

## **6. Working with Paths**
### **6.1 Get Absolute Path**
```python
print(os.path.abspath("example.txt"))
```
### **6.2 Check if Path Exists**
```python
print(os.path.exists("example.txt"))  # Returns True if file exists
```
### **6.3 Check if Path is a File or Directory**
```python
print(os.path.isfile("example.txt"))  # True if it's a file
print(os.path.isdir("example_folder"))  # True if it's a directory
```

## **7. Getting System Information**
### **7.1 Get the Operating System Name**
```python
print(os.name)  # Output: 'posix' (Linux/Mac), 'nt' (Windows)
```
### **7.2 Get System-Specific Path Separator**
```python
print(os.sep)  # Output: '/' (Linux/Mac), '\\' (Windows)
```
### **7.3 Get Line Separator**
```python
print(os.linesep)  # Output: '\n' (Linux/Mac), '\r\n' (Windows)
```

## **8. Walking Through Directory Trees**
Use `os.walk()` to iterate over all files and folders.
```python
for root, dirs, files in os.walk("."):
    print(f"Directory: {root}")
    for file in files:
        print(f"File: {file}")
```
