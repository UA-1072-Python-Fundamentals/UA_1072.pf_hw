import math
class Sphere():
    def __init__(self,radius,mass):
        self.radius=radius
        self.mass=mass

    def get_radius(self):
        print("radius of the Sphere=",self.radius)
    def get_mass(self):
        print("mass of the Sphere=",self.mass)
    def get_volume(self):
        print("volume of the Sphere=",round(4/3*math.pi*self.radius**3,5))
    def get_surface_area(self):
        print("surface area of the Sphere=", round(4 * math.pi * self.radius ** 2,5))
    def get_density(self):
        print("density of the Sphere", round(self.mass/(4/3*math.pi*self.radius**3),5))

ball = Sphere(2,50)
ball.get_radius()
ball.get_mass()
ball.get_volume()
ball.get_surface_area()
ball.get_density()