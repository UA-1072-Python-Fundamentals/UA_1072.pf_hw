class Polygon():
    pass

class Rectangle(Polygon):
    def __init__(self, a = 1, b = 1):
        self.a = a
        self.b = b

    def __str__(self):
        return (f"The len of A: {self.a}\n"
                f"The len of B: {self.b}\n"
                f"The area of rectangle is {self.area()}")

    def area(self):
        return self.a * self.b

user_input01 = int(input("Please enter A: "))
user_input02 = int(input("Please enter B: "))
x = Rectangle(user_input01, user_input02)

print(x)