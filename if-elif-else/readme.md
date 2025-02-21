# if..elif...else

* Used for decision making
* Determine which block of code to execute based on a specific condition.
* Nested conditions

## syntax

```python
if condition:
    # code to be executed if the condition is True
else:
    # code to be executed if the condition is False
```

## example programs

* Check if given number is even or not

```python
age = 20
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

* Determine the grade based on the percentage

```python
percentage = float(input("Enter your percentage: "))

if percentage >= 90:
    grade = 'A'
elif 80 <= percentage < 90:
    grade = 'B'
elif 70 <= percentage < 80:
    grade = 'C'
elif 60 <= percentage < 70:
    grade = 'D'
else:
    grade = 'F'

print(f"Your grade is {grade}.")
```

## Nested if else

* Determine the category based on age and income

```python
age = int(input("Enter your age: "))
income = float(input("Enter your annual income: "))

if age >= 18:
    if income < 50000:
        category = "Low Income Adult"
    elif 50000 <= income < 100000:
        category = "Middle Income Adult"
    else:
        category = "High Income Adult"
else:
    if income < 20000:
        category = "Low Income Minor"
    elif 20000 <= income < 50000:
        category = "Middle Income Minor"
    else:
        category = "High Income Minor"

print(f"You are in the category: {category}")
```
