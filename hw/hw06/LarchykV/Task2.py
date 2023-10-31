
def login_checker():
    correct_log = "First"
    user_log = input("Enter your login, please: ")
    while user_log == "First":
        print("Hey, First!")
        break
    else:
        print("Error! The user login is incorrect.")
login_checker()