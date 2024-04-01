class GradeError(Exception):
    pass


def validate_grade(value):
    if not (0 <= value <= 100):   
        raise GradeError("Grade value should be between 0 and 100")
    return value


result = validate_grade(200)
print(result)
