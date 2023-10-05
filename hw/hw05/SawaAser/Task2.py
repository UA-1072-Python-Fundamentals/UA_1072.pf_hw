# Task2
def fibonacci(number: int):
    """Calculate the Fibonacci sequence up to the given number.
    Args:
       The number is an integer.
    Returns:
       The list of Fibonacci's numbers.
       If number 0 returns 0.
    """
    top_number = 0

    if not number:
        return [0]
    elif number == 1:
        return [0, 1, 1]
    elif number == -1:
        return [0, -1, -1]
    elif number > 1:
        fibonacci_return = [0, 1, 1] 
        while number > top_number:
            i = len(fibonacci_return)
            top_number = fibonacci_return[i-2] + fibonacci_return[i-1]
            if number <  top_number:
                break
            fibonacci_return.append(top_number)
        return fibonacci_return
    elif number < -1:
        fibonacci_return = [0, -1, -1] 
        while number < top_number:
            i = len(fibonacci_return)
            top_number = fibonacci_return[i-2] + fibonacci_return[i-1]
            if number >  top_number:
                break
            fibonacci_return.append(top_number)
        return fibonacci_return
    else:
        return "Error"


x = int(input("What Fibonacci's number do you want: "))
print(fibonacci(x))

def test_fibonacci():
    print("test_fibonacci")
    A = -11
    B = [0, -1, -1, -2, -3, -5, -8]
    C = fibonacci(A)
    print("Ok" if C == B else "Fail")

    A = 0
    B = [0]
    C = fibonacci(A)
    print("Ok" if C == B else "Fail")

    A = 12
    B = [0, 1, 1, 2, 3, 5, 8]
    C = fibonacci(A)
    print("Ok" if C == B else "Fail")

    A = 144
    B = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    C = fibonacci(A)
    print("Ok" if C == B else "Fail")


test_fibonacci()