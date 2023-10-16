def exam(name: str):
    result = False
    if name not in users:
        users.append(name)
        result = True
    return result


users = ['Aleksandr', 'Maria', 'Elena', 'Vladimir']
while True:
    login = input('Enter your login ')
    if exam(login):
        print(f'Welcome {login}!\n')
        break
    else:
        print('Error: Same name already exists! Try again...\n')
        continue