class Poligon:
    def __init__(self):
        pass


class Rectangle(Poligon):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area_rectangle(self):
        return self.length*self.width
    
a = Rectangle(3,5)
print(a.area_rectangle())
