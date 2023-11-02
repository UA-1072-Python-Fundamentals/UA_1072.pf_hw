n = int(input("Enter a number: "))
a, b = 0, 1
print(a)
print(b)
while a + b <= n:
    c = a + b
    if c <= n:
      print(c)
    a, b = b, c