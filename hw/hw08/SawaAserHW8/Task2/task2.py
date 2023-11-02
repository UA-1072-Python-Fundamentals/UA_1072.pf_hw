import re


def validity_of_a_password(password: int) -> int:
    if not re.findall("[a-z]", password):
        print("write at least 1 lower letter")
    elif not re.findall("[A-Z]", password):
        print("write at least 1 upper letter")
    elif not re.findall("[0-9]", password):
        print("write at least 1 number")
    elif not re.findall("[$#@]", password):
        print("write at least 1 character from [$#@]")
    elif not 6 <= len(password):
        print("Minimum length 6 characters")
    elif not len(password) <= 16:
        print("Maximum length 16 characters")
    else:
        print("Your password is accepted")


def create_password():
    x = input("Create your password ")
    validity_of_a_password(x)


create_password()
