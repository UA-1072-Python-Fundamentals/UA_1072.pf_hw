import math

from Calculation import *
from math import pow, pi

#defining the object.
user_input = input("Which specify the area of which object you would like to calculate: ").lower()
PI = math.pi

if user_input == "rectangle":
    result = round(rectangle(),2)
    print(f"The area of rectangle is {result}")
elif user_input == "triangle":
    result = round(triangle(), 2)
    print(f"The area of triangle is {result}")
elif user_input == "circle":
    result = round(circle(), 2)
    print(f"The area of circle is {result}")
else:
    print("Sorry, there is no such object.")
