# Task 3. Custom Exception: Age Validator
class InvalidAgeError(Exception):
    pass
def check_age(age):
    if (1 > age or age > 120):
        raise InvalidAgeError("Age must be between 1 and 120")
    return 
try:
    age = int(input("Enter your age: "))
    check_age(age)
except InvalidAgeError as e:
    print(e)