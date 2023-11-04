# task1

even_numbers_devisible_by_2 = []
odd_numbers_devisible_by_3 = []
numbers_not_divisible_by_2_and_3 = []

for i in range(1, 11):
  if i % 2 == 0 and i % 3 != 0:
      even_numbers_devisible_by_2.append(i)
  elif i% 2 != 0 and i % 3 !=0:
      odd_numbers_devisible_by_3.append(i)
  else:
      numbers_not_divisible_by_2_and_3.append(i)

print("Even numbers divisible by 2:",even_numbers_devisible_by_2)
print("Odd numbers divisible by 3:", odd_numbers_devisible_by_3)
print("Numbers not divisible by 2 and 3:",numbers_not_divisible_by_2_and_3)