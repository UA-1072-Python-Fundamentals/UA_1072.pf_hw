from area import *
from math import pi, pow

def up_to_choice():
    print(f"Which area do you want to know?\n"
          f"The area of a rectangle - enter 1\n"
          f"The area of a triangle - enter 2\n"
          f"The area of a circle - enter 3\n")

    choice = input("Enter your choice: ")

    if choice == "1":
        a = float(input("Enter the length of the rectangle: "))
        b = float(input("Enter the width of the rectangle: "))
        result = area_of_rectangle(a, b)
        print(f"The area of the rectangle is: {result}")
    elif choice == "2":
        b = float(input("Enter the base of the triangle: "))
        h = float(input("Enter the height of the triangle: "))
        result = area_of_triangle(b, h)
        print(f"The area of the triangle is: {result}")
    elif choice == "3":
        r = float(input("Enter the radius of the circle: "))
        result = area_of_circle(r)
        print(f"The area of the circle is: {result}")
    else:
        print("Invalid choice. Please select 1, 2, or 3.")


print(up_to_choice())

print()