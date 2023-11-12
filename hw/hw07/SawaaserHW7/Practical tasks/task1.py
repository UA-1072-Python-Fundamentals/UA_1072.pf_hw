def largest_number(number1: int, number2: int):
    """Takes 2 numbers and returns the largest one
    Args:
        Number1, number2 are integer
    Return:
        The largest number of 2 numbers"""
    if number1 > number2:
        return number1
    elif number2 > number1:
        return number2
    elif number1 == number2:
        return "numbers are equal"
    else:
        return "something goes wrong"


def test_largest_nuber():
    print("test_largest_nuber:")

    a = b = 0
    c = largest_number(a, b)
    print("test: OK" if c == "numbers are equal" else "test: Fail")

    a, b = 5, 10
    c = largest_number(a, b)
    print("test: OK" if c == 10 else "test: Fail")

    a, b = 6, 5
    c = largest_number(a, b)
    print("test: OK" if c == 6 else "test: Fail")


test_largest_nuber()
