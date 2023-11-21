# TASK_Regular Ball Super Ball
# class Ball(object):
#     def __init__(self, ball_type="regular"):
#         self.ball_type = ball_type

# TASK_Color Ghost
from random import randint
#
# class Ghost(object):
#
#     def __init__(self):
#         colors = ["white", "yellow", "purple", "red"]
#         color_num = randint(0, 3)
#         self.color = colors[color_num]
#
# TASK_Basic subclasses - Adam and Eve
# def God():
#     return [Man(), Woman()]
# class Human:
#     pass
# class Man(Human):
#     pass
# class Woman(Human):
#     pass

# TASK_Classy Classes
# class Person:
#     def __init__(self, name, age):
#         self.info = f"{name}s age is {age}"
#
#     def getInfo(self):
#         return self.info

# TASK_Building Spheres
# import math
#
# class Sphere:
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
#         volume = (4/3) * math.pi * (self.radius ** 3)
#         return round(volume, 5)
#
#     def get_surface_area(self):
#         surface_area = 4 * math.pi * (self.radius ** 2)
#         return round(surface_area, 5)
#
#     def get_density(self):
#         density = self.mass / ((4/3) * math.pi * (self.radius ** 3))
#         return round(density, 5)


# TASK_Python's Dynamic Classes #
class MyClass:
    pass


# def class_name_changer(cls, new_name):
#
#     if not new_name.isalnum() or not  new_name[0].isupper():
#         raise Exception
#     else:
#         cls.__name__ = new_name
#
# if __name__ == "__main__":
#     myObject = MyClass();
#     print(MyClass.__name__)
#     class_name_changer(MyClass, 'NewClass')
#     print(MyClass.__name__)
#     class_name_changer(MyClass, 'newClass')
