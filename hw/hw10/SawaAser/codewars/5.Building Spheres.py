import math


class Sphere(object):
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
        self.volume = None
        self.surface_area = None
        self.density = None

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        self.volume = round((4/3) * math.pi * (self.radius ** 3), 5)
        return self.volume

    def get_surface_area(self):
        self.surface_area = round(4 * math.pi * (self.radius ** 2), 5)
        return self.surface_area

    def get_density(self):
        self.density = round(self.mass / self.volume, 5)
        return self.density


ball = Sphere(2,50)
print(ball.get_radius())  # ->       2
print(ball.get_mass())  # ->         50
print(ball.get_volume())  # ->       33.51032
print(ball.get_surface_area())  # -> 50.26548
print(ball.get_density())
