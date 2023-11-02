# Task 7.1
def larger_num(n1, n2):
    """
    This function returns the largest number of two numbers
    """
    if n1 > n2:
        return n1
    elif n2 > n1:
        return n2
    else:
        return print("Entered numbers are equal")


print(larger_num(4, 7))
print(larger_num(44, 9))
print(larger_num(11, 11))
