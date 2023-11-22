import area
def select_choice():
    print("Choose a shape to calculate the area:")
    print("1 Rectangle")
    print("2. Triangle")
    print("3. Circle")
choice = input("Enter your choice (1, 2, or 3): ")

if choice == "1":
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = area.calculate_rectangle_area(length, width)
        print(f"The area of the rectangle is {area:.2f}")
elif choice == '2':
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = area.calculate_triangle_area(base, height)
        print(f"The area of the triangle is {area:.2f}")
elif choice == '3':
        radius = float(input("Enter the radius of the circle: "))
        area = area.calculate_circle_area(radius)
        print(f" {area:.2f}")
else:
        print("Invalid choice. Please select 1, 2 or 3.")