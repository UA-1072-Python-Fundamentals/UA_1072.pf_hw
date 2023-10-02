# # Task 1 at calass:
# def determine(number1, number2):
#     if number1 > number2:
#         return "{number1} is more than {number2}"
#     elif number2 > number1:
#         return "{number2} is more than {number1}"
#     else:
#         return "equal"
    

# a = int(input("number1 = "))
# b = int(input("number2 = "))

# print(determine(a, b))



# Task 2 at calass:
# def even_or_odd(number):
#     number = number % 2
#     if number:
#         return "Your number is odd"
#     else:
#         return "Your number is even"

# number = int(input("Write your number and you know number is even or odd: "))
# print(even_or_odd(number))



# Task1 HW4:
def Temperature_Converter(celsious):
    fahrenheit = round((celsious * 9/5) + 32, 2)
    
    if celsious < -273.15:
        return "Error: Temperature below absolute zero (-273.15°С)"
    else:
        return "{0}°С is equivalent to {1}°F".format(celsious, fahrenheit)

celsius = int(input("Write Celsius: "))
print(Temperature_Converter(celsius))
