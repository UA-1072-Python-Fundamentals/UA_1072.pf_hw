# a = 1
# print(type(a), a)
#
# a = ()
# print(type(a), a)
# a = []
# print(type(a), a)
# a = "1"
# print(type(a), a)
# моє = 23
# print(моє)
# v = True
# v = False
from time import sleep

# i = 13
# print(i, id(i))
# i = 14
# print(i, id(i))
# i = i + 5
# print(i, id(i))
# i = "i + 5"
# print(i, id(i))
# # i[2]='a' #error
# i += "55"
# print(i, id(i))
# i = ["55"]
# print( id(i), i)
# i.append("test")
# print( id(i), i)
# i.append("foo")
#
# print( id(i), i)
#
# a = 1
# print(type(a) is int)
# print(type(a) is float)
# print(isinstance(a, int))
# print(isinstance(a, float))
# class Test1: pass
# class Test2 (Test1): pass
# t2 = Test2()
# print(type(t2) is Test1)
# print(type(t2) is Test2)
# print(isinstance(t2, Test1))
# print(isinstance(t2, Test2))

# a = 3 + 6 + \
#     7 * 8 / 69 \
#     / 5 * 1
# print(a)
# a = (3 + 6
#      + 7 * 8 / 69
#      / 5 * 1)
# print(a)

# a = 1
# b = 2
# c = 3
# a, b, c = 1, 2, 3
# l = ["test", "value", 35, (1, 2, 3)]
# a1, a2, a3, a4 = l
# print(a1, a2, a3, a4)
# for i in range(5):
#     a = 1
#     b = 1
#
# MY_CONST = 33
# print(MY_CONST)
# MY_CONST = 66
# print(MY_CONST)

# a = 513
# print(a)
# a = 513e2
# print(a)
# a = 513e-2
# print(a)
# a = 5.35
# print(a)
# a = 5
# print(a, type(a))
# a = float(5)
# print(a, type(a))
# a = 5.0
# print(a, type(a))
# a = 5.
# print(a, type(a))
# a = 0.5
# print(a, type(a))
# a = .5
# print(a, type(a))
# a = 10000000000000
# print(a, type(a))
# a = 10_000_000_000_000
# print(a, type(a))
# a = 10000000000000
# print(0b10101)
# print(0b01)
# print(0o17)
# print(0o01234567)
# print(0x17)
# print(0x0123456789abcdef)
# a = 9999**9999
# import sys
# sys.set_int_max_str_digits(999999999)
# print(len(str(a)))
# print(a.__sizeof__())
# print(a)
# print(True == 1)
# print(True == 12)
# print(True == 0)
# print(False == 0)
# print(False == 1)
# print(4 + True)
# a = None, # null
#
# l = [1, 2, 3, 4]
# print(l)
# l[2] = "test"
# print(l)
#
# s = {1, 2, 3, 1, 2, 3, 2, 2, 2, 2, 3, 4}
# print(s)
zen = """
The Zen of Python, by Tim Peters

1 - Yevhen Malyna, Capylyn
2 - Anna Poshyta asanasa
3 - Markiian Dmytruk mrknd
4 - Aleksandr Shevchenko, Alexandr1123212545
5 - Kostiantyn Yasinskyi YasinKostya
6 - Tetiana Lesiv tatelesiv
7 - Valeria Larchyk - LachykV
8 - Special cases aren't special enough to break the rules.
9 - Yulianna Drok Yulianna22
10 - Oleg Krupyak, Krupyak
11 - Matvii Lukin - Cawa123qwe
12 - Olha Moroz olha-moroz
13 - Dmytro Shpak, shpakdmitriy
14 - Maksym Shylov , shyma66
15 - MorpheusFR Kirill Suprun
16 - Although never is often better than *right* now.
17 - PavloHavron Pavlo Havron
18 - If the implementation is easy to explain, it may be a good idea.
19 - Namespaces are one honking great idea -- let's do more of those!
20 - shtvlad, Vladislav Shtanhei
21 - andrii2323
22 - Nadiia Illiushyna, somniumtx
23 - Spectrvq (Maksym Oposhnii)
24 - user01
25 - user02
26 - user03
27 - user04
28 - user05
29 - user06
30 - user07
31 - user08
32 - Iryna Iasko - nickname:  Irarasta
33 - Yevhen Malyna, Capylyn
34 - Anna Poshyta asanasa
35 - Markiian Dmytruk mrknd
36 - Aleksandr Shevchenko, Alexandr1123212545
37 - Kostiantyn Yasinskyi YasinKostya
38 - Tetiana Lesiv tatelesiv
39 - Valeria Larchyk - LachykV
40 - Simple is better than complex 
41 - Yulianna Drok Yulianna22
42 - Oleg Krupyak, Krupyak
43 - Matvii Lukin - Cawa123qwe
44 - Olha Moroz olha-moroz
45 - Dmytro Shpak, shpakdmitriy
46 - Maksym Shylov , shyma66
47 - MorpheusFR Kirill Suprun
48 - Unless explicitly silenced.
49 - PavloHavron Pavlo Havron
50 - There should be one-- and preferably only one --obvious way to do it.
51 - Although that way may not be obvious at first unless you're Dutch.
52 - shtvlad, Vladislav Shtanhei
53 - andrii2323
54 - Nadiia Illiushyna, somniumtx
55 - Spectrvq (Maksym Oposhnii)
56 - user01
"""
# print(set(zen))
# d = {}
# for key in set(zen):
#     d[key] = zen.count(key)
# print(d)
# for key in d:
#     print(key, d[key], ord(key))
# for i in range(255):
#     print(f"{i} - {chr(i)}")
# print(int(2.1))
# print(int(2.9))
# print(int("23"))
# print(int("01010101", 2))
# print(int("01010101", 8))
# print(int("01010101", 16))
# print(int("90za", 36))
# # print(int("01010101", 37)) # error
# print("I'm,  Liubomyr")
# print('I\'m,  Liubomyr\\')
# print('test1\ntest2\rtest3\ttest4')
# c = "\|/-"
# step = 0
# for i in range(100):
#
#
#     print(f"\r{c[step%4]}", end="")
#     step += 1
#     sleep(0.1)

# name = "John"
# template = "Hello, %s!"
# print(template % name)
# print("Hello, %s!" % "Test")
# print("Hello, %.3f -!" % 2.12395)
#
# name = "John"
# template = "Hello, {}!"
# print(template.format(name))
# print(template.format("Test"))
# print(template.format(2.12395))
#
#
# print(f"Hello, {name}!")
# print(f"Hello, {name}!")


s = 'programiz'
# print(s)
# print(s[0])
# print(s[len(s) - 1])
# print(s[-1])
# print(s[1:5])
# print(s[1:-1])
print(s[5::-1])


# print(dir(str))
print([method for method in dir(str) if not method.startswith("__")])