class Polygon:
    def __init__(self, height, width):
        self.height = height
        self.width = width


class Rectangle(Polygon):
    def calculate_square(self):
        return self.height * self.width


user_height = float(input("Please, enter the height: "))
user_width = float(input("Please, enter the width: "))

rectangle_square = Rectangle(user_height, user_width)

print(f"The square of the rectangle is: {rectangle_square.calculate_square()}")
