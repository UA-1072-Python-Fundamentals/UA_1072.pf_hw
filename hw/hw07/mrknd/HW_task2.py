def area_recrangle(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("All values must be greater than 0")
    return a * b


def area_triangle(b, h):
    if b <= 0 or h <= 0:
        raise ValueError("All values must be greater than 0")
    return 0.5 * b * h


def area_circle(r):
    if r <= 0:
        raise ValueError("All values must be greater than 0")
    return round(3.1415 * (r**2), 3)


def result():
    while True:
        ask_area = input("Enter the area you want to find [rectangle, triangle, circle],"
                         " or 'exit' to finish the program: ").lower()

        if ask_area == 'exit':
            break

        if ask_area == "triangle":
            ask_base = float(input("Enter the base: "))
            ask_height = float(input("Enter the height: "))
            print(f"Area of triangle is {area_triangle(ask_base, ask_height)}")

        if ask_area == "rectangle":
            ask_length = float(input("Enter the lenght: "))
            ask_width = float(input("Enter the width: "))
            print(f'Area of rectangle is {area_recrangle(ask_length, ask_width)}')

        if ask_area == "circle":
            ask_radius = float(input("Enter the radius: "))
            print(f"Area of circle is {area_circle(ask_radius)}")


result()
