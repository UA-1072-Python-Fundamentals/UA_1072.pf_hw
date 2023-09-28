# a = 5
# b = 10
# print(a == b)
# print(a > b)
# print(a < b)
# c = 7
# print(a < c < b)
# print(not True)
# print(not False)

# a = True
# b = False
# print(a and b)
# print(a or b)
# print(a and a and a and b)
# print(b or b or b or a)
# print(15 and "test" and 1.3 and [1, 2, 3])
# print(15 and "test" and 0 and False and[1, 2, 3])
# print([] or "" or 0)
# print([] or "a" or 10)
is_false = [False, 0, None, [], (), {}, ""]
# l1 = [1]
# l2 = [1]
# print(l1 == l2)
# print(l1 is l2)
# l = [15, "test", 33.3, (1, 2, 3)]
# print(15 in l)
# print("test" in l)
# print((1, 2, 3) in l)
# print([1, 2, 3] in l)
# print(1 in l)
#
# score = 2
# if score > 8:
#     print("You have passed the exam")
#     print("end if")
#
# print("Exam was finished.")


# temperature = float(input('What is the temperature? '))
#
# if temperature >= 30:
#     print('Wear shorts.')
# else:
#     print('Wear long pants.')
#
# print('Get some exercise outside.')
# if temperature >= 30:
#     print('Wear shorts.')
#
#
# if temperature <= 30:
#     print('Wear long pants.')
# age = int(input("my age: "))
# if age < 12:
#     print('kid')
# elif age < 18:
#     print('teenager')
# elif age < 50:
#     print('adult')
# else:
#     print('you are not old')
#
# print("="*8)
# if age < 12:
#     print('kid')
# if age < 18:
#     print('teenager')
# if age < 50:
#     print('adult')
#
# print("="*8)
# if age < 12:
#     print('kid')
# else:
#     if age < 18:
#         print('teenager')
#     else:
#         if age < 50:
#             print('adult')
#         else:
#             print('you are not old')
#
#
# if age < 12:
#     print('kid')
# elif age < 18:
#     print('teenager')
# elif age < 50:
#     print('adult')
#
# age = int(input("my age: "))
#
# if age >= 35 and age <= 65:
#     print("is warrior!")
# elif 0 < age < 18:
#     print("yong")
# elif 18 <= age < 35:
#     print("student")
#
# l = [1,2,3]
# if len(l) > 0:
#     print(l)
# if l:
#     print(l)
# a = age < 18 ? "kids" : "old"

# a = "kids" if age < 18 else "old"
# print(a)
# a = None
# if age < 18:
#     a = "kids"
# else:
#     a = "old"
# print(a)
#
# status = int(input("http status code:"))
# match status:
#     case 400:
#         print("Bad request")
#     case 401:
#         print("Unauthorized")
#     case 403:
#         print("Forbidden")
#     case 404:
#         print("Not found")
#     case 418 | 420 as value:
#         print("i'm tea pot", value)
#     case _:
#         print("Other error")


# print("enter n")
# n = int(input())
# print("enter m")
# m = int(input())
# if n > m:
#     print("n is more than m")
# elif n < m:
#     print("n is less than m")
# elif n == m:
#     print("n is equal m")
#
# a = input("Enter a: ")
# b = input("Enter b: ")
# x = int(a)
# y = int(b)
# z = x-y
# print(z)
# if z == 0:
#     print("numbers are equal")
# elif z > 0:
#     print("a is larger than b")
# else:
#     print("a is less than b")
#
# a, b = int(input('Enter number "a" ')), int(input('Enter number "b" '))
# match a, b:
#   case a, b if a > b:
#     print('"a" more "b"')
#   case a, b if a < b:
#     print('"b" more "a"')
#   case _:
#     print('"a" and "b" are equal')
#

# print("enter k")
# k = int(input("enter k"))
# if k % 2 == 0:
#     print("k is even")
# else:
#     print("k is odd")
#
#
_k = k/2-k//2
print(k/2, _k, type(_k))
if _k:
    print("k is odd")
else:
    print("k is even")


s = "ytdfvbk;jxfbvkfxnlvjdbsfkj"

t = s.replace("y", "88")

print(s)
print(t)
# a == b
# a != b => not a == b
