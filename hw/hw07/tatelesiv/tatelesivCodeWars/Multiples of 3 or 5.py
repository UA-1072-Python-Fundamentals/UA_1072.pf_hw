def multiples_of_3_or_5(number):
    if number < 0:
        return 0

    total_sum = 0

    for num in range(1, number):
        if num % 3 == 0 or num % 5 == 0:
            total_sum += num

    return total_sum


result = multiples_of_3_or_5(10)
print(result)
