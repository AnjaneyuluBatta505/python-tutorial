with open("file-handling/students.csv", "w") as file:
    students = (
        "Anji", "John", "Shiva", "Jimmy", "David"
    )
    for student in students:
        file.write(student+"\n")
