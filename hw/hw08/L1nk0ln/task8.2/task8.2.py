def validation(password):
    symbols = ["[", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", ",", ".", "?", ":", "{", "}", "|", "<", ">", "]",'"']
    val = True

    if len(password) < 6:
        print('length should be at least 6')
        val = False

    if len(password) > 16:
        print('length should be not be greater than 16')
        val = False

    if not any(char.isdigit() for char in password):
        print('Password should have at least one numeral')
        val = False

    if not any(char.isupper() for char in password):
        print('Password should have at least one uppercase letter')
        val = False

    if not any(char.islower() for char in password):
        print('Password should have at least one lowercase letter')
        val = False

    if not any(char in symbols for char in password):
        print('Password should have at least one of the symbols $@#')
        val = False
    if val:
        return "Your password is valid"

password = input()

if (validation(password)):
    print("Password is valid")
else:
    print("Invalid Password !!")



