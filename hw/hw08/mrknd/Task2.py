import re


def check_pass(password) -> bool:
    if (re.search('[a-z]', password) and
            re.search('[A-Z]', password) and
            re.search('[0-9]', password) and
            re.search('[$#@]', password) and
            6 <= len(password) <= 16):
        return True

    return False


def create_pass():
    rules = """Your password must contain:
        - Minimum 6 characters
        - Maximum 16 characters
        - At least 1 letter between [a-z] and [A-Z]
        - At least 1 character between [0-9]
        - At least 1 character from [$#@]
        """
    while True:
        password = input("Enter your password: ")
        check_pass(password)
        if check_pass(password):
            print("Your password is good")
            break
        else:
            print(rules)


create_pass()

