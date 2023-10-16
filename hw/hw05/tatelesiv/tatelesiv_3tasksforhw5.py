# task1
l = [1, 2, 3, 4, 5]
for i in range(len(l)):
    if type(l[i]) == int:
        l[i] = float(l[i])
print(l)

# task2
n = int(input("Enter a number: "))
f1, f2 = 0, 1

while f1 <= n:
    print(f1, end=" ")
    f1, f2 = f2, f1 + f2

# task3
n = int(input("Enter a number: "))
factorial = 1
if n < 0:
    print("Factorial is not defined for negative numbers.")
elif n == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, n + 1):
        factorial *= i
    print(f"The factorial of {n} is {factorial}.")
