from math import pi, pow

def s_rectangle(a, b):
    if a <= 0 or b <= 0:
        return "impossible to calculate, all numbers must be greater than 0."
    else:
        return a * b


def s_triangle(a, h):
    if a <= 0 or h <= 0:
        return "impossible to calculate, all numbers must be greater than 0."
    else:
        return 0.5 * a * h


def s_circle(r):
    if r <= 0:
        return "impossible to calculate, all numbers must be greater than 0."
    else:
        return round(pi*pow(r, 2))

