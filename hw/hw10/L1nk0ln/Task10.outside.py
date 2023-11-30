1. Ball-super-ball
class Ball(object):
    def __init__(self, ball_type = "regular"):
        self.ball_type = ball_type

2. Color-ghost
import random
class Ghost(object):
    def __init__(self):
        colors = ["white", "yellow", "purple", "red"]
        self.color = random.choice(colors)

3. Basic-subclasses-Adam-and-Eve
def God():
    adam = Man("Adam")
    eve = Woman("Eve")
    return [adam, eve]

class Human:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Man(Human):
    def __init__(self, name):
        super().__init__(name, "male")

class Woman(Human):
    def __init__(self, name):
        super().__init__(name, "female")
4. Classy-classes

class Person:
    def __init__(self, name,age):
        self.info=f"{name}s age is {age}"
5. Building Spheres
import math
class Sphere(object):
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
    def get_radius(self):
        return self.radius
    def get_mass(self):
        return self.mass
    def get_volume(self):
        return round(float(4/3 * math.pi * self.radius**3),5)
    def get_surface_area(self):
        return round(float(4*math.pi*self.radius**2),5)
    def get_density(self):
        return round(float(self.mass/(4/3 * math.pi * self.radius**3)), 5)
6. Dynamic Classes
def class_name_changer(cls, new_name):
    if not new_name[0].isupper() or not new_name.isalnum():
        raise exception
    else:
        cls.__name__ = new_name