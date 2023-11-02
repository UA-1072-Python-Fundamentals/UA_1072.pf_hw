name = input("choose a geometric shape: rectangle, triangle or circle:")

def calculate_rectangle_area(a,b):
    S = a*b
    return S
if name == "rectangle":
    a = int(input("input value of a = "))
    b = int(input("input value of b = "))
    print("rectangle area is = ", calculate_rectangle_area(a,b))


def calculate_triangle_area(a1,b1,c1):
    s = (a1 + b1 + c1) / 2
    area = (s * (s - a1) * (s - b1) * (s - c1)) ** 0.5
    return area
if name == "triangle":
    a1 = int(input("input value of a1 = "))
    b1 = int(input("input value of b1 = "))
    c1 = int(input("input value of c1 = "))
    print("triangle area is = ", calculate_triangle_area(a1,b1,c1))

def calculate_circle_area(r):
    area = 3.14159 * r ** 2
    return area

if name == "circle":
    r = int(input("input value of r = "))
    print("circle area is = ", calculate_circle_area(r))
