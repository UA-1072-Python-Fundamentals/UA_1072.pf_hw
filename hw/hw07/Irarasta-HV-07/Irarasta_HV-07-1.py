def largest_number(a, b):
    """TASK:
        compare TWO numbers and return the largest.
        Variables to compare:
        float 'a' and float 'b'. We compare them by mathematical subtraction.
        Int the code we check , if the input is numbers.
        Result:
        output with the message for the user with indication of the largest
        number or identification, if the numbers are equal"""

    comparison =  a - b
    if comparison == 0:
        return 'Numbers are equal'
    elif comparison < 0:
        return f'{b} is the largest'
    else:
        return f'{a} is the largest'
print('Enter TWO NUMBERS to determine the largest of them.')
    # get_input
a_str = input('Enter 1st number, a =  ')
b_str = input('Enter 2nd number, b =  ')
if not a_str.isnumeric() or not b_str.isnumeric():
    print('Input ERROR, enter numbers')
else:
    a = float(a_str)
    b = float(b_str)


    result = largest_number(a, b)
    print(result)

