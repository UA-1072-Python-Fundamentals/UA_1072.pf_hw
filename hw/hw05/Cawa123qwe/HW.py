#TASK01.
#l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#for i in l:
#    print(float(i))

#TASK2.

#fib = int(input("Enter number"))
#rise = 1
#trib = 0
#for num in range(8):
#    trib = trib
#    print(trib)
#    prev = trib
#    new = rise
#    rise += trib
#    trib = new




#TASK3
def calculate_factorial(num):
    factorial = 1

    for i in range(1, num + 1):
        factorial *= i

    return factorial

try:
    num = int(input("Enter a number to calculate its factorial: "))

    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = calculate_factorial(num)
        print(f"The factorial of {num} is {result}")

except ValueError:
    print("Invalid input. Please enter a valid number.")
