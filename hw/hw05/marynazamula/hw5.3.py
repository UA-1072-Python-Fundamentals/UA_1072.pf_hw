num = int(input("Enter your number\n"))
a = 1
step = 1
while step <= num:
    a *= step
    step += 1
print(a)