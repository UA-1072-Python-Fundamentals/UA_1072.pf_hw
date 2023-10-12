def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_number = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_number)
    return fib_sequence

number = int(input("Enter number fibonachi "))

fib_sequence = fibonacci(number)
print("Fibonacci sequence:")
for num in fib_sequence:
    print(num)