A = 1234567891234
Astr = str(A)
Alist = list(Astr)
product = 1
print(f"{A = }")
for i in range(len(Alist)):
    product *= int(Alist[i])
    print(Alist[-(i + 1)], sep='', end='')
print("\n product of the digits",product)
Alist.sort()
print(Alist)

