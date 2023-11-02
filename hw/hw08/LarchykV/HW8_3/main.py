from formulas import*


def result():
    area_type = input("Enter the area you'd like to find: rectangle, triangle or circle: ").lower()

    if area_type == "rectangle":
        length = float(input("Enter the length, please: "))
        width = float(input("Enter the width, please: "))
        print("The rectangle area is", s_rectangle(length, width))

    if area_type == "triangle":
        base = float(input("Enter the base, please: "))
        height = float(input("Enter the height, please: "))
        print("The triangle area is", (s_triangle(base, height)))

    if area_type == "circle":
        radius = float(input("Enter the radius, please: "))
        print("The circle area is", s_circle(radius))


result()