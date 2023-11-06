# # l = [i for i in range(10)]
# # print(l)
# # l = [i for i in range(10) if i % 3]
# # print(l)
# #
# # l = {i: i ** i for i in range(10)}
# # print(l)
# # import random
# # l = [random.randint(1, 100) for i in range(20)]
# # print(l)
# #
# # i = iter("foo")
# # print(i)
# # print(next(i))
# # print(next(i))
# # print(next(i))
# # print(next(i))
# #
# # class MyNumbers:
# #     def __iter__(self):
# #         self.a = 1
# #         return self
# #     def __next__(self):
# #         x = self.a
# #         self.a += 1
# #         if x == 5:
# #             raise StopIteration
# #         return x
# #
# # # a = MyNumbers()
# # # print(a)
# # # a = iter(a)
# # # print(next(a))
# # # print(next(a))
# # # print(next(a))
# # for i in MyNumbers():
# #     print(i)
# #     # if i == 5:
# #     #     break
# #
# # class MyRange:
# #     def __init__(self, start, stop=None, step=1):
# #         if stop is None:
# #             self.start = 0
# #             self.stop = start
# #         else:
# #             self.start = start
# #             self.stop = stop
# #         self.step = step
# #     def __str__(self):
# #         return f"({self.start}, {self.stop}, {self.step})"
# #     def __iter__(self):
# #         print(self)
# #         self.current = self.start
# #         return self
# #
# #     def __next__(self):
# #         x = self.current
# #         self.current += self.step
# #         if x > self.stop:
# #             print(x)
# #             raise StopIteration
# #         return x
# #
# #
# # print([i for i in MyRange(5)])
# # print([i for i in MyRange(-5, 5)])
# # print(3, [i for i in MyRange(-30, 30, 7)])
# # print("end")
# # l1 = [i for i in range(10000)]
# # # print(l)
# # l2 = (i for i in range(10000))
# # # print(l)
# # # print(next(l))
# # # print(next(l))
# # for i in range(1, 6):
# #     n = 10**i
# #     l1 = [i for i in range(n)]
# #     l2 = (i for i in range(n))
# #     print(f"{n}\t{l1.__sizeof__()}\t{l2.__sizeof__()}")
#
#
# # def f():
# #     pass
# # print(f)
# # def f():
# #     yield 1
# # print(f())
#
# def my_f(n):
#     print("func start")
#     count = 0
#     while count <3:
#         print(f"in while {count}")
#         yield count
#         print(f"in while {count} after")
#         count += 1
#
# #
# # f = my_f(5)
# # print("="*20)
# # print(next(f))
# # print("="*20)
# # print(next(f))
# # print("="*20)
# # print(next(f))
# # print("="*20)
# # print(next(f))
# # print("="*20)
# # print(next(f))
# # print("="*20)
#
# for i in my_f(5):
#     pass
#
#
# # def get_all_users():
# #     i = 1
# #     while True:
# #         sql = """ limit {i}"""
# #         data = con.execut(sql)
# #         yield data
# #         i += 10
#
# def dec_star(func):
#     print(func.__name__, id(func))
#     def wrap(*args, **kwargs):
#         print("*" * 10)
#         func(*args, **kwargs)
#         print("*" * 10)
#
#     print("wrap: ", id(wrap))
#     return wrap
# def dec_eq(func):
#     print(func.__name__, id(func))
#     def wrap(*args, **kwargs):
#         print("=" * 10)
#         func(*args, **kwargs)
#         print("=" * 10)
#
#     print("wrap: ", id(wrap))
#     return wrap
#
#
# @dec_star
# def my_print(text):
#     print(text)
#
# print("my_print: ", id(my_print))
#
# @dec_star
# @dec_eq
# @dec_star
# def print_sum(a, b):
#     print(f"a+b={a}+{b}={a + b}")
#
# print("print_sum: ", id(print_sum))
# # my_print("text")
#
# # my_print(3)
# # my_print([1, 2, 3, 4])
# # print_sum(1, 3)
# print_sum(8, 7)
#
# from log_conf import log_param
#
# @log_param
# def fibo1(n):
#     f = [1, 1]
#     i = 2
#     while n >= len(f):
#         f.append(f[i - 1] + f[i - 2])
#         i += 1
#     return f[n]
#
#
# fibo1(4)
# fibo1(6)
# fibo1(6)
#
#
#
# class Point:
#     @log_param
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"(x:{self.__x}, y:{self.__y})"
#
#     @log_param
#     def __get_x(self):
#         print("get_x", self.__x)
#         return self.__x
#
#     @log_param
#     def __set_x(self, x):
#         print("set_x: ", x)
#         if x < 0:
#             self.__x = 0
#         elif x > 1000:
#             self.__x = 1000
#         else:
#             self.__x = x
#     x = property(__get_x, __set_x)
#
#
#     @property
#     @log_param
#     def y(self):
#         print("get_y", self.__y)
#         return self.__y
#
#     @y.setter
#     @log_param
#     def y(self, y):
#         print("set_y", y)
#         self.__y = y
#
#
# p = Point(1,1)
# print(p)
# print(p.x)
# p.x = 568
# print(p)
# p.x = 5689
# print(p)
# p.y = 857
# print(p.y)

def dec_w(symbol, count=10):
    def dec(func):
        def wrap(*args, **kwargs):
            print(symbol * count)
            func(*args, **kwargs)
            print(symbol * count)

        return wrap

    return dec


@dec_w("*", 15)
@dec_w("=")
@dec_w("*", 5)
def print_sum(a, b):
    print(f"a+b={a}+{b}={a + b}")


print_sum(4, 56)
