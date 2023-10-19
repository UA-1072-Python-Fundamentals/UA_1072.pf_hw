num = int(input("Enter a number: "))
f1, f2 = 0, 1

while f1 <= num:
    print(f1, end=' ')
    f1, f2 = f2, f1 + f2