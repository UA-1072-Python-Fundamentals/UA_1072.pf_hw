
from math import pow, pi as PI


def area_rectangle(a:float, b:float) -> float:
    """This function calculates the area of ​​a rectangle.

    :param a: short side of rectangle
    :type a: float
    :param b: long side of rectangle
    :type b: float
    :return: area of rectangle
    :rtype: float
    """
    return float(a) * float(b)


def area_triangle(h:float, base:float) -> float:
    """This function calculates the area of ​​a rectangle.
    :param h: hight of triangle
    :type h: float
    :param base: base of rectangle
    :type base: float
    :return: area of triangle
    :rtype: float
    """
    s = 0.5 * base * h
    return s


def area_circle(r):
    """This function calculates the area of ​​a rectangle.
    :param r: radius of circle
    :type r: float
    :return: area of circle
    :rtype: float
    """
    s = PI * pow(r, 2)
    return s

