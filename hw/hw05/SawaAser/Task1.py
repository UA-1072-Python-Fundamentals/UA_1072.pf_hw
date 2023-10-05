# Task1
def change_int_to_float(list_of_int: list):
    """Change a list of integers to a list of float
    Args:
       The list of integers
    Returns:
       The list of float
    """
    list_of_float = []
    for i in range(len(list_of_int)):
        list_of_float.append(float(list_of_int[i]))
    return list_of_float


x = input("Enter your list of integers(split' '): ").split(" ")
print(change_int_to_float(x))

def test_change_int_to_float():
    print("test_change_int_to_float")
    A = [1, 2, 3, 4, 5, 7, 8, 9, 10]
    B = [1.0, 2.0, 3.0, 4.0, 5.0, 7.0, 8.0, 9.0, 10.0]
    C = change_int_to_float(A)
    print("Ok" if C == B else "Fail")

    A = [1, 0, 0, 0,]
    B = [1.0, 0.0, 0.0, 0.0]
    C = change_int_to_float(A)
    print("Ok" if C == B else "Fail")

    A = [-1, -2, -3, 0,]
    B = [-1.0, -2.0, -3.0, 0.0]
    C = change_int_to_float(A)
    print("Ok" if C == B else "Fail")


test_change_int_to_float()