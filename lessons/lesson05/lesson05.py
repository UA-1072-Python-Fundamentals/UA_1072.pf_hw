import random

# a = int(input("a: "))
# while a < 5:
#     print(a)
#     a += 1
# print("__main__")
# for i in "test0":
#     print(i)
# for i in [1, 2, 3.5, "test ", [1, 2]]:
#     print(i)

#
# start = 0
# finish = 10
# while start < finish:
#     print(start)
#     start += 1
# print("The end")

# for j in [0, 1, 2, 3, 4]:
#     print(j)
# else:
#     print(j, "- is the last")

# for j in 1:
#     print(j)
# print(j, "- is the last")
# l = [0, 1, 2, 3, 4]
# for j in l:
#     print(j)
#     j = 55
# print(l)

# r = range(5)
# print(r)
# print(list(r))
# r = list(range(-5))
# print(r)
# r = list(range(3, 7))
# print(r)
# r = list(range(-3, -7))
# print(r)
# r = list(range(-7, -3))
# print(r)
# r = list(range(-3, -7, -1))
# print(r)
# r = list(range(-3, 7, 3))
# print(r)
# l = [10, 11, 12, 13, 14]
# for i in range(len(l)):
#     print(i, l[i])
#     if l[i] % 2:
#         l[i] = str(l[i])
#     elif l[i] % 3:
#         l[i] = l[i] ** i
# print(l)

# i = 0
# while i < 10:
#     print("before ", i, end="\t")
#     i += 1
#     if i % 2:
#         print()
#         continue
#     print("after ", i)

# for element in [1, 2, "text", (1, 2, 3), 23.4, {1, 2}, 99]:
#     if type(element) in (int, float):
#         continue
#     print(element)
# i = 0
# while True:
#     if i == 3:
#         break
#     print(i)
#     i += 1
# for i in range(10):
#     if i == 3:
#         break
#     print(i)

#
# i = 0
# while True:
#     if i == 3:
#         break
#     print(i)
#     i += 1
# else:
#     print("end while")
# print("="*10)
# i = 0
# while i<5:
#     i += 1
#     if i == 3:
#         continue
#     print(i)
# else:
#     print("end while")
# print("="*10)
# i = 0
# while i<5:
#     i += 1
#     print(i)
# else:
#     print("end while")
# for i in range(5):
#     if i == 3:
#         break
#     print(i)
# else:
#     print("end for")
# print("end")
# print("="*10)
# for i in range(5):
#     if i == 3:
#         continue
#     print(i)
# else:
#     print("end for")
# print("end")
# print("="*10)
# for i in range(5):
#     print(i)
# else:
#     print("end for")
# print("end")
# print("="*10)
#
# l = [4, 3, 4, 6, 8, 3]
# result = []
# for size in l:
#     row = []
#     for i in range(size):
#         e = random.randint(0, 100)
#         print(e, end=" ")
#         if e < 50:
#             continue
#         row.append(e)
#     print()
#     result.append(row)
# for row in result:
#     print(row)
#
# print(f"{e=}")
# print(f"{size=}")
# print(dir())
# sequence = {'p', 'a', 's', 's'}
# for val in sequence:
#     pass
#     #ToDo


# Code_1
# 'while' version
x = 0
while x < 101:
    if not x % 2:
        print(x)
    x += 1
i = 0
while i < 100:
    i = i + 2
    print(i)

i = 0
while i < 100:
    i += 1
    if i % 2:
        continue
    print(i)
# 'for' version
for i in range(101):
    if not i % 2:
        print(i)
for i in range(0, 100, 2):
    print(i)

# Code_2
# 'continue' version
x = 0
while True:
  x += 1
  if x > 100:
    break
  elif x % 2:
    print(x)
  else:
    continue
# ' ' version
x = 0
while x < 100:
  if x % 2:
    print(x)
  x+= 1


# Code_3
x = [1, 3, 5, 6, 8, 9]
for i in x:
  if not i % 2:
    print('Yes')
    break
