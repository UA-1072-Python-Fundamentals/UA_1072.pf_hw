def largest_number(number1: int, number2: int):
    """Takes 2 numbers and returns the largest one
    Args:
        Number1, number2 are integer
    Return:
        The largest number of 2 numbers"""
    if type(number1) is int and type(number2) is int:
        if number1 > number2:
            return number1
        elif number2 > number1:
            return number2
        elif number1 == number2:
            return "numbers are equal"
    else:
        return "something goes wrong"

def correct_tail(body,tail):
    if body[-1]==tail:
        return True
    else:
        return False
body="Fox"
tail="x"
print(correct_tail(body,tail))
