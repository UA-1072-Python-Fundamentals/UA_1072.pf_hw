class Polygon():
    def __init__(self, w, l):
        self.width = w
        self.length = l
class Rectangle(Polygon):
    def area_of_rectangle(self):
        return self.width*self.length
area = Rectangle(10,20)
print(area.area_of_rectangle())