
def login_ckecked():
    valid_login = "First"

    while True:
        user_login = input('Enter the LOGIN: ')
        if user_login == valid_login:
            print('Welcome, First!')
            break
        else:
            print('ValueError')
login_ckecked()

