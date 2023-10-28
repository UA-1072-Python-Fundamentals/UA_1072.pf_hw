#task 2

#2.1
number = int(input("Write your 4-digits number: "))
m = 1
while number > 0:
  m = m * (number % 10)
  number = number // 10
  print("Product of the digits of your number is", m)

#2.2
reverse_number = str(input ("Write the second number for the reverse order:"))
print(str(reverse_number [::-1]))

#2.3
a_number = 548291
number_str = str(a_number)
sorted_str = ''.join(sorted(number_str))
sorted_number = int(sorted_str)

print("Sorted number in ascending order:", sorted_number)