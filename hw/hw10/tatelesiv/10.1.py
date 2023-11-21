# 10.1
class Polygon:
    def __init__(self):
        pass


class Rect(Polygon):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


a = Rect(12, 4)
print(a.area())

