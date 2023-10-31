def solution(number):
    list_of_numbers = []
    for one_number in range(number):
        if not one_number % 3 or not one_number % 5:
            list_of_numbers.append(one_number)
    return sum(list_of_numbers)


print(solution(1000))  # 9168
print(solution(20))  # 78
