def fibonacci(n):
    fib1 = 0
    fib2 = 1
    while fib1 <= n:
        print(fib1, end=", ")
        fib1, fib2 = fib2, fib1 + fib2


n = int(input("Please enter your  Fibonacci number (n): "))


print("Fibonacci numbers up to", n, "are:")
fibonacci(n)