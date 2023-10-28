def calculate_factorial(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return factorial
n = int(input("Please write your number:"))
if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = calculate_factorial(n)
    print(f"{n}! = {result}")