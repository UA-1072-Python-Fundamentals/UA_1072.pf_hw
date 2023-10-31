class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def find_area(self):
        pass

class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__(4)  # for 4 sides of the figure - rectangle
        self.length = length
        self.width = width

    def find_area(self):
        return self.length * self.width


figure_rectanle = Rectangle(15, 20)


area = figure_rectanle.find_area()
print(f'The area of the Rectangle is: {area} Units Of Measurement².')
