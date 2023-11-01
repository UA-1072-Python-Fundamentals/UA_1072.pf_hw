def find_largest_number(num1, num2):
    """
    This function takes two numbers as input and returns the largest of the two.

    Parameters:
    - num1 (int or float): The first number.
    - num2 (int or float): The second number.

    Returns:
    - int or float: The largest number among num1 and num2.
    """
    if num1 > num2:
        return num1
    else:
        return num2


number1 = 15
number2 = 23
result = find_largest_number(number1, number2)
print(f"The largest number between {number1} and {number2} is: {result}")
