#Task 1
def my_func():
    """""
    This function allows to enter two numbers and returns the larger of two.

    """""

    a = float(input("Please, enter the first number: "))
    b = float(input("Please, enter the second number: "))

    if a > b:
        return a
    elif a < b:
        return b
    else:
        return "none, the numbers are equal."

result = my_func()
print(f"The larger number is: {result}")






