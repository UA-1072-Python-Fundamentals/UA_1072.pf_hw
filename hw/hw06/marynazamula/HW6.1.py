divis_2 = [num for num in range(1, 11) if num % 2 == 0]
print("Even num divisible by 2:", divis_2)
divis_3 = [num for num in range(1, 11) if num % 3 == 0]
print("Even num divisible by 3:", divis_3)
not_divis_2_3 = [num for num in range(1, 11) if num % 2 != 0 and num % 3 != 0]
print("Even num divisible by 2:", not_divis_2_3)