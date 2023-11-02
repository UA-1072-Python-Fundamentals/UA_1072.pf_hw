a = input("Enter username: ")

username = ["Oleg", "Petro", "Denys"]
while a in username:
    print('Welcome:' + a)
    break
else:
    print('Access denied. Try again.')