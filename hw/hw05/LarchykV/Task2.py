#Task2
num = int(input("Please, enter the last Fibonacci number: "))


def fibonacci(num):
    n1 = 0
    n2 = 1
    next_num = n2

    while n1 <= num:
        print(n1, end=" ")
        n1, n2 = n2, next_num
        next_num = n1 + n2


print("The result would be: ")
fibonacci(num)
