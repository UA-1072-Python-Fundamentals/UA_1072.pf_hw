#1
def larg(a, b):
    """
    Function for finding the largest of two numbers
    :param a: The first number for finding
    :param b: The second number for finding
    :return: Printing largest number or equal if numbers are equal
    """
    if a>b:
        return a
    elif b>a:
        return b
    else:
        return "equal"
print(larg(12,11))

#2

def sofrec(a,b):
    return a*b
def softrian(c, h):
    return 1/2*c*h
def sofcirc(r):
    pi = 3.14
    return pi * r * r
choice = input("Area of what you want to know?\n Rectangle - 1 \n Triangle - 2 \n Circle - 3 \n")
if int(choice) == 1:
    a = int(input("Enter the first base of rectangle: "))
    b = int(input("Enter the second base of rectangle: "))
    print("Your result is ", sofrec(a,b))
elif int(choice) == 2:
    c = int(input("Enter the base of triangle: "))
    h = int(input("Enter the height of rectangle: "))
    print("Your result is", softrian(c,h))
elif int(choice) == 3:
    r = int(input("Enter a radius of your circle: "))
    print("Your result is", sofcirc(r))

#3
def nocis():
    a = input("Enter a word: ")
    dicti = {}
    for char in a:
        if char in dicti.keys():
            dicti[char] += 1
        else:
            dicti[char] = 1
    return dicti
print(nocis())



