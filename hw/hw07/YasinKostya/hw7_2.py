import math


def calculate_rectangle_area(length, width):
    return length * width


def calculate_triangle_area(base, height):
    return 0.5 * base * height


def calculate_circle_area(radius):
    return math.pi * radius ** 2


def program_calculate_area():
    while True:
        print(
            "Enter action:\n1 - Calculate Rectangle\n2 - Calculate Triangle\n3 - Calculate - Circle\n4 - Exit\n5 - "
            "Return")
        value = int(input())
        match value:
            case 1:
                length = float(input("Enter lenght: "))
                width = float(input("Enter width: "))
                area = calculate_rectangle_area(length, width)
                print(f"Area Rectangle = ", area)
            case 2:
                base = float(input("Enter base: "))
                height = float(input("Enter height: "))
                area = calculate_triangle_area(base, height)
                print(f"Area Triangle = ", area)
            case 3:
                radius = float(input("Enter radius: "))
                area = calculate_circle_area(radius)
                print(f"Area Circle = ", area)
            case 4:
                exit()
            case 5:
                return


program_calculate_area()

# OR
rectangle_are = calculate_rectangle_area(5, 78)
triangle_area = calculate_triangle_area(7.6, 8)
circle_area = calculate_circle_area(45)
print(f"calculate_rectangle_area = ", rectangle_are)
print(f"calculate_triangle_area = ", triangle_area)
print(f"calculate_circle_area = ", circle_area)
