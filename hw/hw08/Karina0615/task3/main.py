
from calculation import *

def area_calculation():

    shape = input("Please, chose a geometric shape. Rectangle or triangle or circle? ")
    if shape.lower() == "rectangle":
        return area_rectangle(1,1)
    elif shape.lower() == 'triangle':
        return area_triangle(1,1)
    else:
        return area_circle(1)

print(area_calculation())

