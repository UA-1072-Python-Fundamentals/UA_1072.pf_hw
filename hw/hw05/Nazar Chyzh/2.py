f_n = int(input("n: "))
f1, f2 = 0, 1

for i in range(f_n):
    print(f1, end= " ")
    f1, f2 = f2, f1 + f2