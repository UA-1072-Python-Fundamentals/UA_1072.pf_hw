# Task3
def factorial(number: int):
    """Calculate the factorual of the given number.
    Args:
       The number is an integer.
    Returns:
       The factorual of the input number.   
       If number 0 returns 1.
       If a number lesser  than 0 returns an 'Error'.
    """
    result = 1
    if number < 0:
        return "Error"
    if not number:
        return 1
    for every_number in range( 1, number + 1):
        result *= every_number
    return result


x = int(input("Enter an integer to calculate its factorial: "))
print(factorial(x))

def test_factorial():
    print("test_factorial")
    A = 5
    B = 120
    C = factorial(A)
    print("Ok" if C == B else "Fail")

    A = 0
    B = 1
    C = factorial(A)
    print("Ok" if C == B else "Fail")

    A = 11
    B = 39_916_800
    C = factorial(A)
    print("Ok" if C == B else "Fail")

    A = -11
    B = "Error"
    C = factorial(A)
    print("Ok" if C == B else "Fail")


test_factorial()