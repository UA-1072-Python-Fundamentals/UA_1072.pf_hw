num = int(input("Write your number: "))
def sum_num(num):
    numbers_list = list(range(1, num))
    if num < 0:
        return 0
    list_2 = []
    for i in numbers_list:
        if i % 3 == 0 or i % 5 == 0:
             list_2.append(i)
        sum_of_numbers = sum(list_2)
    return sum_of_numbers


print("The sum of multiples of 3 or 5 below number is:", sum_num(num))