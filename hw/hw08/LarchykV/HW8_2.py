import re


password = input("Please, enter the password: ")
x = re.search("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@]).{6,16}$", password)


if x:
    print("The password is correct!")
else:
    print("The password is incorrect. Please, check the rules to create a valid one.\nThe password must contain:\n-At least 1 letter between [a-z] and 1 letter between [A-Z].\n-At least 1 character from [$#@].\n-Minimum length 6 characters.\n-Maximum length 16 characters.")