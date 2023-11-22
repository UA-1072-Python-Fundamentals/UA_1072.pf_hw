class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def perimeter(self):
        return sum(self.sides)


class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__([length, width, length, width])

    def area(self):
        return self.sides[0] * self.sides[1]
# rectangle = Rectangle(8, 10)
# print("Perimeter:", rectangle.perimeter())
# print("Area:", rectangle.area())