# Python - CSV Module

* CSV - Comma Seperated Values
* CSV is most common import and export format for spreadsheets and databases

## Read data as list of rows

* `csv.reader(file, delimiter)`

```python
import csv

file_path = "cities.csv"
with open(file_path, 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        print(row)
```

### Read data as dict of rows

* `csv.DictReader(file)`

```python
import csv

file_path = "cities.csv"
with open(file_path, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
```


### Write list of data to csv

* `csv.writer(file)`
  * `writer.writerow(row)`
  * `writer.writerows(rows)`

```python
import csv

file_path = "students.csv"
with open(file_path, 'w') as file:
    header = ["first_name", "last_name"]
    rows = [
        ["John", "B"],
        ["Shiva", "D"],
        ["Radha", "M"],
        ["Krishna", "D"]
    ]
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(rows)
```

### Write dict data to csv

* `csv.DictWriter(file, header)`
  * `writer.writeheader()`
  * `writer.writerow(row_dict)`
  * `writer.writerows(rows_dict)`

```python
import csv

file_path = "students.csv"
with open(file_path, 'w') as file:
    header = ["first_name", "last_name"]
    row = {"first_name": "Anji", "last_name": "B"}
    rows = [
        {"first_name": "Shiva", "last_name": "D"},
        {"first_name": "John", "last_name": "M"},
        {"first_name": "Krishna", "last_name": "R"}
    ]
    writer = csv.DictWriter(file, header)
    writer.writeheader()
    writer.writerow(row)
    writer.writerows(rows)
```
