# Task_1(3)
num_1 = int(input("Please write your first number: "))
num_2 = int(input("Please write your second  number: "))
if num_1 != num_2:
    num_sum = num_1 +num_2
    num_1 = num_sum - num_1
    num_2 = num_sum - num_2
    print(f"Now your first number is: {num_1}")
    print(f"Now your second  number is: {num_2}")

else:
    print("You wrote two identical numbers")