from calculates import *
from math import pi, pow


def choice():
    print(f"What do you want to calculate?\n"
          f"Rectangle area - enter 1\n"
          f"Triangle area  - enter 2\n"
          f"Circle area    - enter 3\n")
    answer = int(input("Enter you choice: "))

    if answer == 1:
        x, y = eval(input("Enter the length of two sides separated by a comma: "))
        return round(area_of_a_rectangle(x, y), 2)
    elif answer == 2:
        x, y = eval(input("Enter height and side separated by a comma: "))
        return round(area_of_a_triangle(x, y), 2)
    elif answer == 3:
        x = eval(input("Enter the radius: "))
        return round(area_of_a_circle(x, pow, pi), 2)
    else:
        print(f"Bad choice! Lets star again!\n")
        return choice()


print(choice())
