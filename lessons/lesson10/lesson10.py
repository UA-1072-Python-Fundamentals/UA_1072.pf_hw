# class User:
#     """
#     class User
#     """
#     count_print = 0
#
#     def my_print(self):
#         print(self, "User", self.count_print)
#
#
# print(User, type(User))
# user1 = User()
# user2 = User()
# print(user1, type(user1))
# print(user2, type(user2))
# user1.my_print()
# User.my_print(user1)
# user2.my_print()
# print(user1.my_print)
# print(User.my_print)
# print(User.__dict__)
# print(user1.__dict__)
#
#
# def my_func(obj):
#     print(f"my_func{__name__} {obj}")
# my_func(user1)
#
# User.func = my_func
# user1.func()
#
# print(User.__dict__)
#
# i = User.my_print
#
# i(user1)

# class MyClass:
#     cm = [1]
#     ci = 10
#     def __init__(s):
#         s.im = [10]
#         s.ii = "inst"
#
# obj1 = MyClass()
# obj2 = MyClass()
#
# print(MyClass.cm, MyClass.ci, MyClass.__dict__)
# print(obj1.cm, obj1.ci, obj1.im, obj1.ii, obj1.__dict__)
# print(obj2.cm, obj2.ci, obj2.im, obj2.ii, obj2.__dict__)
# obj1.ii = "22"
# obj2.im.append("33")
# obj1.cm.append("test")
# print(MyClass.cm, MyClass.ci, MyClass.__dict__)
# print(obj1.cm, obj1.ci, obj1.im, obj1.ii, obj1.__dict__)
# print(obj2.cm, obj2.ci, obj2.im, obj2.ii, obj2.__dict__)

# class User:
#     def __init__(self, name, age=18):
#         self.name = name
#         self.age = age
#
# user1 = User("Oleh")
# user2 = User("Liubomyr", 37)
# print(user1.name, user1.age)
# print(user2.name, user2.age)
#
# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"(x:{self.x}, y:{self.y})"
#
#     def __repr__(self):
#         return f"({self.x}, {self.y})"
#
#     # def __del__(self):
#     #     print(f"del {self}")
#     def __add__(self, other):
#         p = Point()
#         p.x = self.x + other.x
#         p.y = self.y + other.y
#         return p
#
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
#
#
# p1 = Point()
# p2 = Point(1, 10)
# p3 = Point(7, -3)
# print(p1, p2, p3)
# p4 = p2 + p3
# print(p4)
# print([p1, p2, p3, p4])
# p2.x = 0
# p2.y = 0
# print(p1, p2)
# print(p1 == p2)
# p5 = p1
# print(p1 == p5)
#
#
# class Point3D(Point):
#     def __init__(self, x=0, y=0, z=0):
#         super().__init__(x, y)
#         self.z = z
#     def __str__(self):
#         return f"(x:{self.x}, y:{self.y}, z:{self.z})"
#
#
#
# pd1 = Point3D(1, 2)
# print(pd1.__dict__)
# print(pd1)
# print([pd1])

# #
# class A():pass
# class B(A):
#     def f(self):print("B")
# class C(A):
#     def f(self): print("C")
# class D(C):pass
# class E(D,B):pass
# class F(C):pass
# class G(F,E):pass
#
# g = G()
# print(G.__mro__)
# g.f()
# e = E()
# print(isinstance(e, G))
# print(isinstance(e, E))
# print(isinstance(e, C))

# class A:
#     def foo(self):
#         pass
#     # def foo(self, x,y):
#     #     pass
# class B(A):
#     def foo(self):
#         pass
#
# a = A()
# a.foo()
#
# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def to_str(self):
#         print(self)
#         return f"x={self.x} y={self.y}"
#     @classmethod
#     def class_mrthod(cls):
#         print(cls)
#
#     @staticmethod
#     def static_m():
#         print(dir())
#
#
#
# p = Point(1,1)
# print("class: ", Point)
# print("inst: ", p)
# p.to_str()
# # Point.to_str() #error
#
# p.class_mrthod()
# Point.class_mrthod()
#
# p.static_m()
# Point.static_m()
#
# class Encapsulation:
#     def __init__(self, a, b, c):
#         self.public = a
#         self._protected = b
#         self.__private = c
# e = Encapsulation(1,2,3)
# print(e.public)
# print(e._protected)
# print(e._Encapsulation__private)


class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"(x:{self.__x}, y:{self.__y})"

    def __get_x(self):
        print("get_x", self.__x)
        return self.__x

    def __set_x(self, x):
        print("set_x: ", x)
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x
    x = property(__get_x, __set_x)

    @property
    def y(self):
        print("get_y", self.__y)
        return self.__y
    @y.setter
    def y(self, y):
        print("set_y", y)
        self.__y = y


p = Point(1,1)
print(p)
print(p.x)
p.x = 568
print(p)
p.x = 5689
print(p)
p.y = 857
print(p.y)
