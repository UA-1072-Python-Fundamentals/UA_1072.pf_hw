import math
def rectangle():
    a = int(input("Please enter rectangle width: "))
    b = int(input("Please enter rectangle length: "))
    area_rectangle = a * a + b * b
    return area_rectangle


def triangle():
    b = int(input("Please enter length of triangle's base: "))
    h = int(input("Please enter length of triangle's height: "))
    area_triangle = (b * h) / 2
    return area_triangle


def circle():
    PI = math.pi
    r = int(input("Please enter the radius' length: "))
    area_circle = PI * (r * r)
    return area_circle
