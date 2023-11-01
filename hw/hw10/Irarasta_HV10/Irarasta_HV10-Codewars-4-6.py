## 4- Classy Classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def info(self):
        return f"{self.name}s age is {self.age}"

## 5- Sphere
import math

class Sphere:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        return round((4/3) * math.pi * (self.radius ** 3), 5)

    def get_surface_area(self):
        return round(4 * math.pi * (self.radius ** 2), 5)

    def get_density(self):
        return round(self.mass / self.get_volume(), 5)


## 6-Python's Dynamic Classes
import re

def class_name_changer(cls, new_name):
    if re.match(r'^[A-Z][a-zA-Z0-9-_]*$', new_name):
        cls.__name__ = new_name
    else:
        raise Exception('Invalid Class Name')
