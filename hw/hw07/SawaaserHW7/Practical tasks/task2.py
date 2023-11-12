def area_rectangle(side1, side2):
    """Count the area of rectangle
    Args:
        side1, side2: integer above 0
    Return:
        The area of rectangle"""
    return side1*side2


def area_triangle(side1, side2, side3):
    """Count the area of a triangle
    Args:
        side1, side2, side3: integer above 0
    Return:
        The area of triangle"""
    p = 1/2 * (side1+side2+side3)
    return (p*(p-side1)*(p-side2)*(p-side3))**(1/2)


def area_circle(r):
    """Count the area of a circle
    Arg:
        r (radius): integer above 0
    Return:
        The area of circle"""
    return 3.14*r**2


def area():
    """Function asks What figure do you want the area of
       You can choose a rectangle, triangle, or circle
    Print:
        The area of your figure"""
    type_figure = int(input("What figure do you want the area of \n(if rectangle write '1', "
                            "if triangle write '2', if circle write '3'): "))
    if type_figure == 1:
        sides = []
        for i in range(1, 3):
            sides.append(int(input(f"Write side {i} of your rectangle: ")))
        print("Area rectangle is {}".format(area_rectangle(*sides)))
    elif type_figure == 2:
        sides = []
        for i in range(1, 4):
            sides.append(int(input(f"Write side {i} of your triangle: ")))
        print("Area triangle is {}".format(area_triangle(*sides)))
    elif type_figure == 3:
        print("Area circle is {}".format(area_circle(int(input("Write radius of your circle: ")))))
    else:
        print("Something goes wrong")


area()
