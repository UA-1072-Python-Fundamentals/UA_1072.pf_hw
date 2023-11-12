import re


def is_valid_password(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@]).{6,16}$"

    if re.match(pattern, password):
        return True
    else:
        return False


while True:
    password = input("Enter a password: ")
    if is_valid_password(password):
        print("Valid password")
        break
    else:
        print("Invalid password. Please try again.")
