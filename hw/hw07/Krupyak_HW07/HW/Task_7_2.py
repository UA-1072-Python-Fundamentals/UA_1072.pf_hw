def calculate_rectangle_area(length, width):
    return length * width
def calculate_triangle_area(base, height):
    return 0.5 * base * height
def calculate_circle_area(radius):
    return 3.14 * (radius ** 2)
while True:
    print("Choose a shape to calculate the area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")


    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = calculate_rectangle_area(length, width)
        print(f"The area of the rectangle is {area}")
    elif choice == '2':
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = calculate_triangle_area(base, height)
        print(f"The area of the triangle is {area}")
    elif choice == '3':
        radius = float(input("Enter the radius of the circle: "))
        area = calculate_circle_area(radius)
        print(f"The area of the circle is {area:.2f}")
        break
    else:
        print("Invalid choice. Please select 1, 2 or 3")