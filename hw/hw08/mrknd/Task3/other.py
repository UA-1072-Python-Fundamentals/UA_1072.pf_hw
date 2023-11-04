from math import pow, pi


def area_rectangle(a, b):
    area = a * b
    return area


def area_triangle(h, a):
    area = 0.5 * h * a
    return area


def area_circle(r):
    area = pi * pow(r, 2)
    return area
