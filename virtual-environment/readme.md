# Python Virtual Environment


## **1. Introduction to Virtual Environments**  
A **Python virtual environment** is an isolated environment that allows you to install packages **without affecting** the global Python installation. It helps in **dependency management** by ensuring that different projects can have their own libraries.  

---

## **2. Why Use Virtual Environments?**  
✅ **Avoid Dependency Conflicts** – Each project can have different versions of the same library.  
✅ **Prevents Global Installation Issues** – Keeps the system clean from unnecessary installations.  
✅ **Ensures Reproducibility** – The project can be shared with others using `requirements.txt`.  
✅ **Allows Multiple Python Versions** – Different projects can use different Python versions.  

---

## **3. Creating a Virtual Environment**  
Python provides the built-in `venv` module to create virtual environments.  

### **3.1 Creating a Virtual Environment in Windows**  
```bash
python -m venv myenv
```
This creates a folder named **`myenv`** containing the virtual environment.  

### **3.2 Creating a Virtual Environment in macOS/Linux**  
```bash
python3 -m venv myenv
```
If `python3` is not found, install it using:  
```bash
sudo apt install python3
```

---

## **4. Activating and Deactivating the Virtual Environment**  
### **4.1 Activating the Virtual Environment**  

#### **Windows (CMD/PowerShell)**
```bash
myenv\Scripts\activate
```
For PowerShell, use:  
```powershell
myenv\Scripts\Activate.ps1
```

#### **macOS/Linux**
```bash
source myenv/bin/activate
```

When activated, the shell prompt changes to:  
```bash
(myenv) $
```

### **4.2 Deactivating the Virtual Environment**  
To exit the virtual environment, simply run:  
```bash
deactivate
```

---

## **5. Installing Packages in a Virtual Environment**  
Once the virtual environment is activated, you can install packages using `pip`:  
```bash
pip install requests
pip install flask
```

To check installed packages:  
```bash
pip list
```

To check a specific package version:  
```bash
pip show flask
```

---

## **6. Freezing and Recreating Environments (`requirements.txt`)**  
### **6.1 Freezing Installed Packages**  
To share your environment, create a `requirements.txt` file:  
```bash
pip freeze > requirements.txt
```

### **6.2 Installing Dependencies from `requirements.txt`**  
To recreate the environment on another system:  
```bash
pip install -r requirements.txt
```

---

## **7. Managing Multiple Virtual Environments**  
If you work on multiple projects, you can store all virtual environments in one directory using `WORKON_HOME`:  

```bash
export WORKON_HOME=~/virtualenvs
mkdir -p $WORKON_HOME
python3 -m venv $WORKON_HOME/project1
source $WORKON_HOME/project1/bin/activate
```

To list all environments:  
```bash
ls ~/virtualenvs
```

---

## **8. Deleting a Virtual Environment**  
Simply delete the virtual environment folder:  
```bash
rm -rf myenv  # macOS/Linux
rd /s /q myenv  # Windows
```

---

## **9. Virtual Environment vs Global Python Installation**  

| Feature | Virtual Environment | Global Python Installation |
|---------|---------------------|---------------------------|
| Scope | Project-specific | System-wide |
| Package Isolation | Yes | No |
| Prevents Conflicts | Yes | No |
| Requires Activation | Yes | No |
| Best for Production | Yes | No |

---

## **10. Using `venv` vs `virtualenv`**  
Python provides `venv`, but an alternative package called `virtualenv` also exists.

| Feature | `venv` | `virtualenv` |
|---------|--------|-------------|
| Comes with Python | Yes | No (needs `pip install virtualenv`) |
| Performance | Slower | Faster |
| Cross-version Support | No | Yes |

To install and use `virtualenv`:  
```bash
pip install virtualenv
virtualenv myenv
```

---

## **11. Using `pipenv` for Virtual Environments**  
`pipenv` is a modern tool for managing virtual environments and dependencies.  

### **Installing `pipenv`**  
```bash
pip install pipenv
```

### **Creating and Activating a Virtual Environment with `pipenv`**  
```bash
pipenv install
pipenv shell
```

### **Installing Packages with `pipenv`**  
```bash
pipenv install flask
```

To remove an environment:  
```bash
pipenv --rm
```

---

## **12. Virtual Environments in IDEs (PyCharm, VSCode)**  
### **12.1 PyCharm**  
1. Open PyCharm.  
2. Go to **Settings > Project > Python Interpreter**.  
3. Click **Add Interpreter > Virtual Environment**.  
4. Select `myenv` and apply.  

### **12.2 VSCode**  
1. Open **Command Palette** (`Ctrl+Shift+P`).  
2. Search **"Python: Select Interpreter"**.  
3. Choose the virtual environment (`myenv`).  

---

## **13. Best Practices for Virtual Environments**  
✅ Always use a virtual environment for each project.  
✅ Store virtual environments **inside the project folder** or a central directory.  
✅ Use `requirements.txt` or `pipenv` for dependency management.  
✅ Activate the virtual environment before running scripts.  
✅ Regularly clean up unused environments.  
