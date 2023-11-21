def check_age(age):
    if age < 0:
        raise ValueError("Your age cannot be less than 0")
    elif age % 2 == 0:
        return "Your age is even"
    else:
        return "Your age is odd"

def enter_age():
    try:
        age = int(input("Enter you age: "))
        print(check_age(age))
    except ValueError as e:
        print(e)


enter_age()