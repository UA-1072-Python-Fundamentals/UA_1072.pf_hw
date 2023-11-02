import re

def product_of_digits(number):
    product = 1
    for digit in str(number):
        product *= int(digit)
    return product

def reverse_number(number):
    return number[::-1]

def sort_digits_ascending(number):
    return ''.join(sorted(str(number)))

while True:
    number = input("Enter a four-digit natural number: ")
    if re.match(r'^[1-9]\d{3}$', number):
        print("You entered a four-digit natural number:", number)
        break
    else:
        print("Please enter a valid four-digit natural number.")

print(f'Product - {product_of_digits(number)}')
print(f'Reverse - {reverse_number(number)}')
print(f'Sorting - {sort_digits_ascending(number)}')