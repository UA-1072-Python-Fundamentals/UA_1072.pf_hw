"""module for calculating the area of simple shapes"""
from math import pow, pi


def rectangle(a, b):
    return round(a * b, 2)


def triangle(a, h):
    return round(0.5 * a * h, 2)


def circle(r):
    return round(pi * 2 * pow(r, 2), 2)
if __name__ == '__main__': print('hi')