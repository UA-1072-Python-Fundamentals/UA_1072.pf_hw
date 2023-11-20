import math
def area_of_rectangle():
    a = float(input("Enter first side of a rectangle:"))
    b = float(input("Enter second side of a rectangle:"))
    S = a*b
    print("Area of a rectangle ",S)


def area_of_triangle():
    h = float(input("Enter height of a triangle:"))
    a = float(input("Enter value of the base of the triangle:"))
    S_tri =0.5*h*a
    print("Area of a triangle ",S_tri)

def area_of_cicle():
    r = float(input("Enter the radius "))
    s_cicle = math.sqrt(math.pi * r)
    print("Area of cicle is ", s_cicle)