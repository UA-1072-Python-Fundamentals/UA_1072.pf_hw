def product_of_digits(number):
    product = 1
    for digit in str(number):
        product *= int(digit)
    return product

# Example
number = 2000
result_product = product_of_digits(number)
print(f"Product of digits: {result_product}")

def reverse_number(number):
    return int(str(number)[::-1])

# Example
reversed_number = reverse_number(number)
print(f"Reversed number: {reversed_number}")

def sort_digits_ascending(number):
    sorted_number = int(''.join(sorted(str(number))))
    return sorted_number

# Example
sorted_ascending_number = sort_digits_ascending(number)
print(f"Sorted in ascending order: {sorted_ascending_number}")

number = 2000

result_product = product_of_digits(number)
reversed_number = reverse_number(number)
sorted_ascending_number = sort_digits_ascending(number)

print(f"Product of digits: {result_product}")
print(f"Reversed number: {reversed_number}")
print(f"Sorted in ascending order: {sorted_ascending_number}")
