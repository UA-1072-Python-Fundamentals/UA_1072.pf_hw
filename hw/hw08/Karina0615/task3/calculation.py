from math import pow, pi
PI = pi


def area_rectangle(length=1,width=1):

    length = int(input("Please, enter a length of rectangle "))
    width = int(input("Please, enter a width of rectangle  "))
    a_rect = length*width
    return (f"The area of rectangle is {a_rect}")


def area_triangle(base=1, hight=1):

    base = int(input("Please, enter a base of triangle "))
    hight = int(input("Please, enter a hight of triangle "))
    a_t = 0.5*base*hight
    return (f"The area of triangle is {a_t}")


def area_circle(radius=1):

    radius = int(input("Please, enter a radius of circle "))
    a_circ = round((PI * pow(radius, 2)),2)
    return (f"The area of circle is {a_circ}")