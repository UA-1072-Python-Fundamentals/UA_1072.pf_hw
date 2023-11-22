class Polygon():
    def __init__(self, num_sides):
        self.num=num_sides
        self.sides=[0 for i in range(num_sides)]

    def input_sides(self):
        self.sides=[input(f"Input '{str(i+1)}' side:") for i in range(self.num)]

class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,2)
    def area_of_rectangle(self):
        width,height=self.sides
        area=int(width)*int(height)
        print(f"Area of rectangle '{width}x{height}' = {area}")

r=Rectangle()
r.input_sides()
r.area_of_rectangle()