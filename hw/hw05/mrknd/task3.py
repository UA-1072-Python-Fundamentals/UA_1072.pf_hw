x = int(input("Enter number: "))
f = 1

for i in range(1, x+1):
    f *= i

print(f"{x}!={f}")