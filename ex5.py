class AgeError(Exception):
    pass


def get_age():
    try:
        age = int(input("Enter your age: "))
        if age < 0 or age > 150:
            raise AgeError("Invalid age. Age must be between 0 and 150.")
        return age

    except ValueError:
        raise AgeError("Invalid age. Age must be a valid integer.")


try:
    age = get_age()
    print("Your age is:", age)

except AgeError as e:
    print("Error:", str(e))