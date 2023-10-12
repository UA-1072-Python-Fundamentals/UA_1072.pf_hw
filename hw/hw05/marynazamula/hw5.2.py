num = int(input("Enter your number\n"))
a = 0
b = 1
step = 0
while a < num:
    a, b = b, a + b
    step += 1
    print(a, end=' ')