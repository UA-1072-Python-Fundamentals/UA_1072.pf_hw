from def_area import calculate_rectangle_area, calculate_triangle_area, calculate_circle_area

name = input("choose a geometric shape: rectangle, triangle or circle:")

if name == "rectangle":
    a = int(input("input value of a = "))
    b = int(input("input value of b = "))
    print("rectangle area is = ", calculate_rectangle_area(a, b))

if name == "triangle":
    a1 = int(input("input value of a1 = "))
    h = int(input("input value of h = "))

    print("triangle area is = ", calculate_triangle_area(a1, h))

if name == "circle":
    r = int(input("input value of r = "))
    print("circle area is = ", calculate_circle_area(r))
