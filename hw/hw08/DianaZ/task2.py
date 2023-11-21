import re

pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$]).{6,16}')

while True:
    password = input("Please, write password \n")
    if bool(re.match(pattern, password)):
        print(f'{password} - Good password')
    else: print('Does not meet the requirements! Try again...\n')
