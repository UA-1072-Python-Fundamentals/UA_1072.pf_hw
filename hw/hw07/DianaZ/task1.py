def my_max(a, b):
    """"function accepts two numbers. returns largest number of them"""
    if a>b:
        return a
    else:
        return b
print(my_max.__doc__)
print(my_max(5,6))