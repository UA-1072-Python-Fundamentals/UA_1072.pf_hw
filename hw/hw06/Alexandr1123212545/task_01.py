def division(lst: list):
    result ={'even_divisible by 2':[],
             'odd_divisible by 3': [],
             'not_divisible by 2 & 3': []
            }
    for num in lst:
        if not num % 2:
            result['even_divisible by 2'].append(num)
        elif not num % 3:
            result['odd_divisible by 3'].append(num)
        else:
            result['not_divisible by 2 & 3'].append(num)
    return result


ready_dict = division(list(range(1, 10)))
for key, value in ready_dict.items():
    print(f'{key} -> {value}')