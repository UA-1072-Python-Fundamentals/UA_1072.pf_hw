class Polygon:
    def __init__(self):
        pass

class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self)
    def arearec(self, a,b):
        return a*b

rec = Rectangle()
a = int(input("Enter the first base of rectangle: "))
b = int(input("Enter the second base of rectangle: "))
print(rec.arearec(a, b))

