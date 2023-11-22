import re
print("Create a password.")
print(""" Validation :
At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters. """)
password = input("Please, enter your password: ")

pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@]).{6,16}$"
re.match(pattern, password)

while True:
    if password:
        print("The entered password is valid.")
        break
    else:
        print("Password is not valid. Please, try again.")