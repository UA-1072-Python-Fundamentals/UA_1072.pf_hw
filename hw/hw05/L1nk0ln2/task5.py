# task 5.1
l = [1, 2 ,3, 4]
a = []
for i in l:
    p = float(i)
    a.append(p)
print(a)


# task 5.2

f = [0, 1]
number = int(input("Enter the number for Fibonacci sequence: "))
for i in range(2, number):
    i2 = f[i-1] + f[i-2]
    f.append(i2)

for num in f:
    print(num)

# task 5.3

factor = int(input("Enter the number for factorial: "))
a = b = 1
while a <= factor:
    b = a * b
    a += 1
print(b)