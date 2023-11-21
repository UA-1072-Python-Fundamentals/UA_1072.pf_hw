def largest_number_of_two(num1, num2):
    """A function that returns the largest number of two
numbers """
    if num1 == num2:
        res = f"The numbers are equal!"
    else:
        res = num1 if num1 > num2 else num2
    return res