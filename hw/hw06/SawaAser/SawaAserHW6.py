# Task 1

def list_of_divisibe_2_and_3(list_number: list):
    """Generate lists which divisible and not divisible by 2 and 3 
    Args:
       The list of integers
    Returns:
       The list of even numbers that are divisible by 2
       The list of odd nublers, which are divisible by 3
       The list of numbers that are not divisible by 2 and 3   
    """
    list_div_2 = []
    list_div_3 = []
    list_not_div_2_3 = []
    for i in list_number:
        if not i % 2:
            list_div_2.append(i)
        if not i % 3:
            list_div_3.append(i)
        if i % 2 and i % 3:
            list_not_div_2_3.append(i)
    print("divisibe by 2: {}\ndivisible by 3: {}\nnot divisible by 2 and 3:{}".format(list_div_2, list_div_3, list_not_div_2_3))


x = range(1, 11)
list_of_divisibe_2_and_3(x)


# Task 2
def checkin(login: str):
    """Check login
    Args:
       The login is string
    Return:
       If login is right return greet.
       If login isn't right return error message
    """
    right_login = "First"
    while True:
        return "Hi! Welcome! What's up?" if login == right_login else "Sorry! I don't know ye!"


log = input("Write your login, please: ")
print(checkin(log))