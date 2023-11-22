#Task1
class Ball:
    def __init__(self,ball_type='regular'):
        self.ball_type=ball_type

regular_type=Ball()
user_type=Ball('super')

print(regular_type.ball_type)
print(user_type.ball_type)

#Task2
import random

class Ghost:
    def __init__(self):
        color_list=['white','yellow','purple','red']
        self.color=random.choice(color_list)

ghost1=Ghost()
ghost1.color

print(ghost1.color)

#Task3
class Human:
    def __init__(self, name):
        self.name=name
class Woman(Human):
    def __init__(self, name):
        super().__init__(name) 
class Man(Human):
    def __init__(self, name):
        super().__init__(name) 

def first_people():
    adam=Man('Adam')
    eve=Woman('Eve')
    return adam,eve

adam, eve=first_people()
print(adam.name)
print(eve.name)

#Task4
class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    @property
    def get_info(self):
        return f'{self.name} age is {self.age}'

person=Person('John\'s','34')
print(person.get_info)
    
#Task5
from math import pi

class Sphere:
    def __init__(self, radius, mass):
        self.radius=radius
        self.mass=mass
    
    def get_radius(self):
        return self.radius
    
    def get_mass(self):
        return self.mass
    
    def get_volume(self):
        return round((4/3)*pi*pow(self.radius,3),5)
    
    def get_surface_area(self):
        return round(4*pi*pow(self.radius,2),5)
    
    def get_density(self):
        return round(self.get_mass()/self.get_volume(),5)
    
ball=Sphere(2,50)
ball.get_radius()
ball.get_mass()
ball.get_volume()
ball.get_surface_area()
ball.get_density()

#Task6
class MyClass:
    pass
def class_name_changer(cls, new_name):
    if not new_name[0].isupper() and new_name.isalnum:
        raise ValueError
    cls.__name__=new_name

class_name_changer(MyClass, "UsefulClass")
print(MyClass.__name__)