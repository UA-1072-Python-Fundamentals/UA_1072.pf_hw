#Task 2
import math


def s_rectangle(a, b):
    if a <= 0 or b <= 0:
        return "impossible to calculate, all numbers must be greater than 0"
    else:
        return a * b


def s_triangle(a, h):
    if a <= 0 or h <= 0:
        return "impossible to calculate, all numbers must be greater than 0"
    else:
        return 0.5 * a * h


def s_circle(r):
    if r <= 0:
        return "impossible to calculate, all numbers must be greater than 0"
    else:
        return round(math.pi * r**2)


def result():
    area_type = input("Enter the area you'd like to find: rectangle, triangle or circle: ").lower()

    if area_type == "rectangle":
        length = float(input("Enter the length, please: "))
        width = float(input("Enter the width, please: "))
        print("The rectangle area is ", s_rectangle(length, width))

    if area_type == "triangle":
        base = float(input("Enter the base, please: "))
        height = float(input("Enter the height, please: "))
        print("The triangle area is ", (s_triangle(base, height)))

    if area_type == "circle":
        radius = float(input("Enter the radius, please: "))
        print("The circle area is ", s_circle(radius))


result()


