# def my_func():
#     print("start my_func")
#     print("my_func")
#     print("end my_func")


#
#
# my_func()
# my_func()
# my_func()


# def my_sum(a, b):
#     c = a + b
#     return c
#
#
# result = my_sum(1, 2)
# print(result)
# print(my_sum(5, 6))
# print(my_func())
#
#
# def my_sum(a, b):
#     c = a + b
#     if c > 0:
#         return c
#     else:
#         return "sum is negative"
#     print("end")
#
#
# print(my_sum(55, 6))
# print(my_sum(5, -6))
# def my_sum(a, b):
#     """
#     doc for my sum
#     :param a: int
#     :param b: int
#     :return: int or string
#     """
#     c = a + b
#     print(f"{a}+{b}")
#     if c > 0:
#         return c
#     else:
#
#         return "sum is negative"
#
# #
# # print(my_sum(1, 2))
# # my_sum(11, 21)
# # print(my_sum(1, 21))
# print(type(my_sum), my_sum)
# print(my_sum.__doc__)
# help(my_sum)


# def my_f(name, age):
#     print(f"args {name=} {age=}")
#
#
# my_f("Liubomyr", 37)
# my_f(37, "Liubomyr")
# my_f(37, "Liubomyr", 5) #error
# my_f(37) #error
# my_f() #error

# def my_f(name, age=18):
#     print(f"args {name=} {age=}")
#
#
# my_f("Liubomyr", 37)
# my_f(37, "Liubomyr")
# # my_f(37, "Liubomyr", 5) #error
# # my_f() #error
# my_f("Andrii")
# def my_f(name, r, age=18, g):
#     pass
#
# def f(con=[]):
#     con.append(1)
#     print(con)
#
#
# f()
# f()
# f()
# f()
# f([2, 3, 4])
# f()
# def my_f(name, age=18):
#     print(f"args {name=} {age=}")
#     print(1)
#     a = 1
#
#
# my_f(name="Taras", age="44")
# my_f(age="44", name="Taras")
#
# print("a", "b", "c", sep="->", end="END")
# print("a", sep="->", end="END")
#
# def my_f(*args):
#     print(f"{args=}")
#
#
# my_f(1, 2, 3, 4, 5)
# my_f(1, 2, 3)
#
#
# def my_f(a, b, *args, c=3, d=4, **kwargs):
#     if len(args) > 10:
#         raise Exception
#     print(f"{a=} {b=} {args=} {c=} {d=} {kwargs}")
#     # print(type(args), type(kwargs))
#
#
# my_f(1, 2, 3, 4, 5)
# my_f(1, 2, 3)
# my_f(1, 2, 3, 4, c=5, f=55)
# my_f(1, 2, 3, 4, c=5, f=55, m=33)
# # my_f(1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 13, 4, c=5, f=55, m=33) #error
# l = (1, 2, 3, 4, 5)
# d = {
#     "c": 588,
#     "f": 555,
#     "m": 3355,
#     "d": 99
# }
# my_f(l[0], l[1], l[2], l[3], l[4], c=d["c"], f=d["f"], m=d["m"], d=d["d"])
# my_f(*l, **d)
# # my_f(*l, *d)

# x = 20
# print(locals())
#
#
# def scope_func():
#     print(locals())
#     x = 10
#     print(locals())
#     print("Value inside function:", x)
#
#
# scope_func()
# print(locals())
# print("Value outside function:", x)


# y = 20
#
#
# def scope_func():
#     x = 10
#     print("Value inside function:", x, f"{y=}")
#
#
# scope_func()
# print("Value outside function:", y)
# x = 20
#
#
# def scope_func():
#     print(f"{x=}")
#     x = 10
#     print(f"{x=}")

# scope_func()
# x = 20
#
#
# def scope_func():
#     global x
#     print(f"{x=}")
#     x = 10
#     print(f"{x=}")
#
# scope_func()
# print(x)
#
# x = "global"
#
#
# def outer():
#     x = "local"
#
#     def inner():
#         nonlocal x
#         x = "non local"
#         print(x)
#     inner()
#     print(x)
#
#
# outer()
# print(x)
#
# print("="*20)
#
# x = "global"
#
#
# def outer():
#     x = "local"
#
#     def inner():
#         global x
#         x = "non local"
#         print(x)
#     inner()
#     print(x)
#
#
# outer()
# print(x)
#
#
#
# print("="*20)
#
# x = "global"
#
#
# def outer():
#     x = "local"
#
#     def inner():
#         nonlocal x
#         x = "non local"
#         print(x)
#     inner()
#     print(x)
#
#
# outer()
# print(x)

# import sys
# sys.setrecursionlimit(2000)
# def rec(in_param):
#     print(in_param)
#     rec(in_param+1)
#
#
# rec(1)

def fibo1(n):
    f = [1, 1]
    i = 2
    while n >= len(f):
        f.append(f[i - 1] + f[i - 2])
        i += 1
    return f[n]


# for i in range(10):
#     print(i, fibo(i))
#
# def fibo2(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return fibo2(n - 1) + fibo2(n - 2)
#
#
# for i in range(10):
#     print(f"{i}\t{fibo1(i)}\t{fibo2(i)}")


l = [1, "5", 3, "76", 89, "2", 6, 9]
print(l)


def str_to_int(n):
    return int(n)


l.sort(key=str_to_int)
print(l)
l.sort(key=lambda x: -int(x))
print(l)

f = lambda a, b: a+b; print("end")
print(f)
f(1,2)

