# Task01 version_01

def division_v1():
    l1 = []
    l2 = []
    l3 = []
    for i in range(1,10):
        if not i%2:
            l1.append(i)
        elif not i%3 and i%2:
            l2.append(i)
        else:
            l3.append(i)
    return (f"List of even numbers that are divisible by 2: {l1}\n"
            f"List of odd numbers, which are divisible by 3: {l2}\n"
            f"List of numbers that are not divisible by 2 and 3: {l3}\n")


print(division_v1())

# Task01 version_02
def division_v2():
    l1 = [i for i in range(1, 10) if not i % 2]
    l2 = [i for i in range(1, 10) if not i % 3 and i % 2]
    l3 = [i for i in range(1, 10) if not i in l1 and not i in l2]

    return (f"List of even numbers that are divisible by 2: {l1}\n"
            f"List of odd numbers, which are divisible by 3: {l2}\n"
            f"List of numbers that are not divisible by 2 and 3: {l3}\n")


print(division_v2())


# Task 02
def checks():
    login_checked = "First"
    login = input("Enter your login: ")
    while not login == "First":
        login = input("Wrong login!!! Enter your login: ")
    else:
        print("Login is correct!")


checks()