import re
def password_validity(password):
    pattern=r"^(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[$#@]).{6,16}$"
    if re.search(pattern,password):
        return True
    else:
        return False
user_password=str(input('What is your password?'))

if password_validity(user_password):
    print('Your password is valid')
else:
    print('Your password is not valid')