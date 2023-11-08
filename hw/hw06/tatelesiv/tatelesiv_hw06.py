# Task 6.1
n_two = []
n_three = []
n_n = []
for i in range(1, 11):
    if i % 2 == 0:
        n_two.append(i)
    if i % 3 == 0:
        n_three.append(i)
    if i % 2 != 0 and i % 3 != 0:
        n_n.append(i)

print(n_two)
print(n_three)
print(n_n)

# Task 6.2
login = input('Enter your login, please: ')

while login != 'First':
    print("An error has occurred")
    login = input('Enter your login, please: ')

print('Welcome back')
