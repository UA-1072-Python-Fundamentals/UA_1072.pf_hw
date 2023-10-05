# 2nd task

#2.1
my_number = int(input("write your 4-digits number: "))

m = 1

while my_number > 0:
  m = m * (my_number % 10)
  my_number = my_number // 10
print("Product of the digits of your number is", m)

#2.2

reverse_number = str(input ("second number to be reversed:"))
print(str(reverse_number [::-1]))

#2.3
some_number = 2334566
sorted_digits = "".join(sorted(str(some_number)))

print("Sorted digits in number :", sorted_digits)