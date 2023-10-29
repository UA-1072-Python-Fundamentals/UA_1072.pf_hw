from math import pi as PI
class Sphere(object):
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
        self.PI = PI
#     @property    
    def get_radius(self):
        return self.radius
    def get_mass(self):
        return self.mass
    def get_volume(self):
        self.volume = round((4/3*self.PI*pow(self.radius,3)),6)
        return self.volume
    def get_surface_area(self):
        self.surface_area = round((4*self.PI*pow(self.radius,2)),6)
        return self.surface_area
    def get_density(self):
        self.density = round((self.mass/self.volume),6)
        return self.density
        