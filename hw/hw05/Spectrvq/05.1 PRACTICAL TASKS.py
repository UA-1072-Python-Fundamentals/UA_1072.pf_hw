# Task1. Create a list that contains elements of integer type, then use
# the loop to change the type of these elements to a floating type.
int_list = [1, 2, 3, 4, 5]
float_list = []
for num in int_list:
    float_list.append(float(num))
print(float_list)


# Task2. Print Fibonacci numbers up to the entered number n,
# using cycles.
fibonacci_n = int(input("Enter a positive integer: "))
if fibonacci_n <= 0:
    print("Please enter a positive integer.")
else:
    fibonacci_list = [0, 1]
    while fibonacci_list[-1] <= fibonacci_n:
        next_number = fibonacci_list[-1] + fibonacci_list[-2]
        fibonacci_list.append(next_number)
    fibonacci_list.pop()
    print(fibonacci_list)


# Task3. Write a script that will calculate the factorial of the entered
# number without using recursion.
factorial = int(input("Type a factorial: "))
result = 1
if factorial <= 0:
    print("0")
else:
    for num in range(1, factorial + 1):
        result = result * num
print(result)
