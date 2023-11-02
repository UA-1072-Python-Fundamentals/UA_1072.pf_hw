#1

a = 3545
a_str = str(a)
product = int(a_str[0]) * int(a_str[1]) * int(a_str[2]) * int(a_str[-1])
print(product)

#2
reversed_number = int(a_str[::-1])
print(reversed_number)

#3

sorted_numbers = sorted(a_str)
print(sorted_numbers)