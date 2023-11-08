# def bigger_num(num_1, num_2):
#     """Find the largest number between two input numbers."""
#     if num_1 > num_2:
#         return f"{num_1} > {num_2}"
#     else:
#          return f"{num_2} > {num_1}"
# num_1 = int(input("Please write your first number: "))
# num_2 = int(input("Please write your second  number: "))
# result = bigger_num(num_1,num_2)
# print(result)



# TAsk_2
# def calculate_rectangle_area(length, width):
#     return length * width
#
#
# def calculate_triangle_area(base_1, base_2, base_3):
#     p = (base_1 + base_2 + base_3) / 2
#     s = (p * (p - base_1) * (p - base_2) * (p - base_3)) ** (1 / 2)
#     return print(f"Triangle area = {s}")
#
#
# def calculate_circle_area(radius):
#     return 3.14159265358979323846 * (radius ** 2)
#
#
# print("Choose a shape to calculate the area:")
# print("1. Rectangle")
# print("2. Triangle")
# print("3. Circle")
#
# choice = int(input("Enter your choice (1/2/3):"))
#
# if choice == 1:
#     length = float(input("Enter the length of the rectangle: "))
#     width = float(input("Enter the width of the rectangle: "))
#     area = calculate_rectangle_area(length, width)
#     print(f"The area of the rectangle is: {area}")
# elif choice == 2:
#     base_1 = float(input("Enter the a of the triangle: "))
#     base_2 = float(input("Enter the b of the triangle: "))
#     base_3 = float(input("Enter the c of the triangle: "))
#     area = calculate_triangle_area(base_1, base_2, base_3)
#     print(f"The area of the triangle is: {area}")
# elif choice == 3:
#     radius = float(input("Enter the radius of the circle: "))
#     area = calculate_circle_area(radius)
#     print(f"The area of the circle is: {area}")
# else:
#     print("Invalid choice. Please choose 1, 2, or 3.")

# TASK_3
# def count_characters(input_string):
#     count_characters = {}
#     for character in input_string:
#         if character in count_characters:
#             count_characters[character] += 1
#         else:
#             count_characters[character] = 1
#     return count_characters
#
# input_str = "hello"
# result = count_characters(input_str)
# print(result)



