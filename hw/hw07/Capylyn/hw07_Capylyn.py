# Task 7.1
def larger(a, b):
    """"
    This function will return the largest number of 2 numbers.
    :param a: the first number
    :param b: the second number
    :return: Depending on check, will return the larger number.
    """
    if a > b:
        return a
    elif a < b:
        return b


# Task 7.2
def rectangle():
    a = int(input("Please enter rectangle width: "))
    b = int(input("Please enter rectangle length: "))
    area_rectangle = a * a + b * b
    return area_rectangle


def triangle():
    b = int(input("Please enter length of triangle's base: "))
    h = int(input("Please enter length of triangle's height: "))
    area_triangle = (b * h) / 2
    return area_triangle


def circle():
    r = int(input("Please enter the radius' length: "))
    PI = 3.14
    area_circle = PI * (r * r)
    return area_circle


userInput = input(
    "Please choose the area of which object you would like to calculate, rectangle, triangle, or circle?: ").lower()

if userInput == "rectangle":
    try:
        result = rectangle()
        print(f"The area of the rectangle is: {result}")
    except ValueError:
        print("Sorry, the entered value is not correct. Please try again.")

elif userInput == "triangle":
    try:
        result = triangle()
        print(f"The area of the triangle is {result}")
    except ValueError:
        print("Sorry, the entered value is not correct. Please try again.")

elif userInput == "circle":
    try:
        result = circle()
        print(f"The area of the circle is {result}")
    except ValueError:
        print("Sorry, the entered value is not correct. Please try again.")

else:
    print("It does not exist. Please choose wisely next time.")


# Task 7.3

def number_of_characters():
    user_input = input("Please enter a word: ")
    d = {}
    for char in user_input:
        if char in d.keys():
            d[char] += 1
        else:
            d[char] = 1

