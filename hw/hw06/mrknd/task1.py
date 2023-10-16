def divisible(num):
    even_divisible_2 = []
    odd_divisible_3 = []
    not_2_and_3 = []

    for i in num:
        if i % 2 == 0:
            even_divisible_2.append(i)
        elif i % 3 == 0:
            odd_divisible_3.append(i)
        else:
            not_2_and_3.append(i)

    return f"Even numbers divisible by 2: {even_divisible_2}\nOdd numbers divisible by 3: {odd_divisible_3}\nNumbers not divisible by 2 and 3: {not_2_and_3} "

num = range(1, 11)
res = divisible(num)
print(res)