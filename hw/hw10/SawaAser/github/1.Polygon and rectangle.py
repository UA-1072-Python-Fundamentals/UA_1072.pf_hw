class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def input_sides(self):
        self.sides = [float(input(f"Enter side {str(i + 1)}: "))
                      for i in range(self.n)]

    def disp_sides(self):
        for i in range(self.n):
            print(f"Side {i + 1} is {self.sides[i]}")


class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 2)

    def find_area(self):
        """
        Calculate the area of a rectangle.
        Parameters:
            length (int): The length of the rectangle.
            width (int): The width of the rectangle.
        Returns:
            int: The area of the rectangle.
        """
        length, width = self.sides
        area = length * width
        print(f"The area of the rectangle is {area}")


simple_rectangle = Rectangle()
simple_rectangle.input_sides()
simple_rectangle.find_area()
