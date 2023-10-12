# task 01
l = [2, 5, 8, 10 ,12]
for i in l:
    print(float(i))

# task 02
fib1 = 0
fib2 = 1

n = int(input("Write Fibonacci series element number:"))

i = 0
while i < n - 2:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1

print("The value of this element:", fib2)

# task 03
n = int(input("enter the number:"))
factorial = 1
while n > 1:
    factorial *= n
    n -= 1
print("Factorial of number =", factorial)