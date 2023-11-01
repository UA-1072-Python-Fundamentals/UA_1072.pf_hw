# Task 01
def largest_number_of_two(num1, num2):
    """A function that returns the largest number of two
        numbers """
    if num1 == num2:
        res = f"The numbers are equal!"
    else:
        res = num1 if num1 > num2 else num2
    return res


# Task 02
def choice():
    print(f"What do you want to calculate?\n"
          f"Rectangle area - enter 1\n"
          f"Triangle area  - enter 2\n"
          f"Circle area    - enter 3\n")
    answer = int(input("Enter you choice: "))

    if answer == 1:
        x, y = eval(input("Enter the length of two sides separated by a comma: "))
        return rectangle_area(x, y)
    elif answer == 2:
        x, y, z = eval(input("Enter the length of three sides separated by a comma: "))
        return triangle_area(x, y, z)
    elif answer == 3:
        x = eval(input("Enter the radius: "))
        return circle_area(x)
    else:
        print(f"Bad choice! Lets star again!\n")
        return choice()


def rectangle_area(a, b):
    s = round(a*b, 2)
    return print(f"Rectangle area = {s}")


def triangle_area(a, b, c):
    p = (a + b + c) / 2
    s = round((p * (p - a) * (p - b) * (p - c)) ** (1 / 2), 2)
    return print(f"Triangle area = {s}")


def circle_area(r):
    pi = 3.14
    s = round(pi*r**2, 2)
    return print(f"Circle area = {s}")


choice()


# Task03
def number_of_characters():
    txt = "hello"
    d = {}
    for i in set(txt):
        d[i] = txt.count(i)
    return print(d)


number_of_characters()
