# Regular Ball Super Ball
class Ball:
    def __init__(self, ball_type="regular"):
        self.type = ball_type

    def get_ball_type(self):
        return self.type


ball1 = Ball()
ball2 = Ball("super")

print(ball1.get_ball_type())
print(ball2.get_ball_type())


# Color Ghost
import random

class Ghost:
    def __init__(self):
        colors = ["white", "yellow", "purple", "red"]
        self.color = random.choice(colors)


ghost1 = Ghost()
print(ghost1.color)

ghost2 = Ghost()
print(ghost2.color)


# Basic subclasses - Adam and Eve
class Human:
    def __init__(self, name):
        self.name = name


class Woman(Human):
    def __init__(self, name):
        super().__init__(name)


class Man(Human):
    def __init__(self, name):
        super().__init__(name)


def create():
    adam = Man("Adam")
    eve = Woman("Eve")
    return [adam, eve]


adam, eve = create()
print(adam.name)
print(eve.name)


# Classy Classes

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.information = f"{self.name}'s age is {self.age}"


john = Person("John", 34)
print(john.information)


# Building Spheres
from math import pi


class Sphere:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        volume = (4/3) * pi * self.radius**3
        return round(volume, 5)

    def get_surface_area(self):
        surface_area = 4 * pi * self.radius**2
        return round(surface_area, 5)

    def get_density(self):
        density = self.mass / ((4/3) * pi * self.radius**3)
        return round(density, 5)


ball = Sphere(2,50)
print(ball.get_radius())
print(ball.get_mass())
print(ball.get_volume())
print(ball.get_surface_area())
print(ball.get_density())


# Python's Dynamic Classes


def rename_class(old_class, new_name):
    if not new_name.isidentifier() or not new_name[0].isupper():
        raise ValueError("Invalid class name")
    new_class = type(new_name, old_class.__bases__, dict(old_class.__dict__))
    return new_class


class MyClass:
    pass


RenamedClass = rename_class(MyClass, "UsefulClass")
print(RenamedClass.__name__)

