# Task 7.2
import math


def calculate_rectangle_area(length, width):
    return length * width


def cal_tri_ar(b, h):
    return 0.5 * b * h


def cal_circ_ar(r):
    return math.pi * r * r

while True:
    print("Choose a shape to calculate its area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = calculate_rectangle_area(length, width)
        print(f"The area of the rectangle is {area}\n")
    elif choice == '2':
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = cal_tri_ar(base, height)
        print(f"The area of the triangle is {area}\n")
    elif choice == '3':
        radius = float(input("Enter the radius of the circle: "))
        area = cal_circ_ar(radius)
        print(f"The area of the circle is {area}\n")
    elif choice == '4':
        print("The end")
        break
    else:
        print("Invalid choice. Please enter a valid option.\n")

