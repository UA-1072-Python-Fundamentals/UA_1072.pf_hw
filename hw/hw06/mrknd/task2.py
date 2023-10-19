while True:
    login = 'first'
    login_input = input("Enter your login: ")
    login_input = login_input.lower()

    if login_input == login:
        print('Congratulation!')
        break
    else:
        print("Incorrect login")