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
