# Task01
def change_type(list_f):
    for i in range(len(list_f)):
        list_f[i] = float(list_f[i])
    return list_f


l = [2, 4, 8, 10]
print(change_type(l))

# # Task02
# def fibonacci(x):
#     i = 0
#     fib = 0
#     prew = 0
#     new = 1
#     mess = ""
#     while i <= x:
#         if not i:
#             mess += f"{fib} "
#             i += 1
#         fib = new + prew
#         new = prew
#         prew = fib
#         i += 1
#         mess += f"{fib} "
#     return mess
#
#
# num = int(input("Input number: "))
# print(fibonacci(num))

# # Task03
# def factorial(x):
#
#     fact = 1
#     mess = "0!=1"
#     if x:
#         for i in range(fact, x+1):
#             fact *= i
#             mess += f" {i}!={fact}"
#         return mess
#     else:
#         return mess
#
#
# num  = int(input("Input number: "))
# print(factorial(num))