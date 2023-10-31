import re

pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$]).{6,}')

def valid_passwod() -> str:
    """This function checks the password for validity.

    :return: result of checking
    :rtype: str
    """
    while True:
        password = input('Create a password!  ')        
        if bool(re.match(pattern, password)) and len(password) < 17:
            return f'{password} - Good password'
        print('Does not meet the requirements! Try again...\n')
        continue

    return password


print(valid_passwod())
