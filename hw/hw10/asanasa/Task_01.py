class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def perimeter(self):
        return sum(self.sides)

class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__([length, width, length, width])
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def is_square(self):
        return self.length == self.width


rectangle = Rectangle(4, 4)

print(f"Rectangle Perimeter: {rectangle.perimeter()}")
print(f"Rectangle Area: {rectangle.area()}")
print(f"Is it a square? {rectangle.is_square()}")


non_square_rectangle = Rectangle(6, 3)

print(f"Non-Square Rectangle Perimeter: {non_square_rectangle.perimeter()}")
print(f"Non-Square Rectangle Area: {non_square_rectangle.area()}")
print(f"Is it a square? {non_square_rectangle.is_square()}")
