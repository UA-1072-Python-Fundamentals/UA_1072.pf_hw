class Polygon:
    def __init__(self, num_of_sides):
        self.num = num_of_sides
        self.sides = [0 for i in range(num_of_sides)]

    def inputSides(self):
        self.sides = [float(input(f"Enter side {str(i+1)}: ")) for i in range(self.num)]

    def dispSides(self):
        for i in range(self.num):
            print(f"Side {i+1} is {self.sides[i]}")

class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 2)

    def findArea(self):
        a, b = self.sides
        area = a * b
        print(f"Area of your rectangle is: {area}")

r = Rectangle()
r.inputSides()
r.dispSides()
r.findArea()
