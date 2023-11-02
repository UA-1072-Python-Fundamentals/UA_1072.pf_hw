# main_program.py
import geometry  # Import your "geometry" module

print("Choose a shape to calculate the area:")
print("1. Rectangle")
print("2. Triangle")
print("3. Circle")

choice = int(input("Enter your choice (1/2/3): "))

if choice == 1:
    a = float(input("Enter the length of the rectangle (a): "))
    b = float(input("Enter the width of the rectangle (b): "))
    area = geometry.rectangle_area(a, b)
elif choice == 2:
    a = float(input("Enter the base of the triangle (a): "))
    h = float(input("Enter the height of the triangle (h): "))
    area = geometry.triangle_area(a, h)
elif choice == 3:
    r = float(input("Enter the radius of the circle (r): "))
    area = geometry.circle_area(r)
else:
    print("Invalid choice")
    area = None

if area is not None:
    print(f"The area of the selected shape is: {area}")


