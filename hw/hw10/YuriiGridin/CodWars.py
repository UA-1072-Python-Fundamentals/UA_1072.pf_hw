# # I. Ball-super-ball
# class Ball(object):
#     def __init__(self, t = "regular"):
#         self.ball_type = t
#
#
# # II. Color-ghost
#
# from random import randint
#
# class Ghost(object):
#
#     def __init__(self):
#         colors = ["white", "yellow", "purple", "red"]
#         color_num = randint(0, 3)
#         self.color = colors[color_num]
#
#
# # III. Basic-subclasses-Adam-and-Eve
# def God():
#     return [Man(), Woman()]
#
#
# class Human:
#     pass
#
#
# class Man(Human):
#     pass
#
#
# class Woman(Human):
#     pass
#
# # IV. Classy-classes
# class Person:
#     def __init__(self, name, age):
#         self.info = f"{name}s age is {age}"
#
#     def getInfo(self):
#         return self.info
#
#
# # V. Building Spheres
# import math
#
#
# class Sphere:
#
#     def __init__(self, radius, mass):
#         self.radius = radius
#         self.mass = mass
#
#     def get_radius(self):
#         return self.radius
#
#     def get_mass(self):
#         return self.mass
#
#     def get_volume(self):
#         return round(4 / 3 * math.pi * (self.radius ** 3), 5)
#
#     def get_surface_area(self):
#         return round(4 * math.pi * (self.radius ** 2), 5)
#
#     def get_density(self):
#         return round(self.mass / (4 / 3 * math.pi * (self.radius ** 3)), 5)


# VI. Dynamic Classes
class MyClass:
    pass


myObject = MyClass()


def class_name_changer(cls, new_name):
    if new_name.isalnum() and new_name[0].isupper():
        cls.__name__ = new_name
    else:
        raise Exception


class_name_changer(MyClass, "UsefulClass")
print(MyClass.__name__)
