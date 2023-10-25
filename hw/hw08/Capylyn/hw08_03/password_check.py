import re
def password_check(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@]).{6,16}$"
    return re.match(pattern, password)

while True:
    password = input("Please enter your password: ")

    if password_check(password):
        print("The entered password is valid")
        break
    else:
        print("Password is not valid. Please try again.")