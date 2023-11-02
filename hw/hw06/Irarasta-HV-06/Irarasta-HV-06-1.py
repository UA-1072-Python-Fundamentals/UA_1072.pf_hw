
def divisibility(numbers):
    divisible_by_2 = []
    divisible_by_3 = []
    non_divisible_by_2_or_3 = []
    for num in numbers:
        if num % 2 == 0:
            divisible_by_2.append(num)
        elif num % 3 == 0:
            divisible_by_3.append(num)
        else:
            non_divisible_by_2_or_3.append(num)
    return divisible_by_2, divisible_by_3, non_divisible_by_2_or_3

numbers = [1,2,3,4,5,6,7,8,9,10]
divisible_by_2, divisible_by_3, non_divisible_by_2_or_3 = divisibility(numbers)

print("EVEN, divisible by 2, are:", divisible_by_2)
print("ODD, divisible by 3, are :", divisible_by_3)
print("Non_divisible by 2 or 3:", non_divisible_by_2_or_3)







