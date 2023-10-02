def product(num):
    count = 0
    result = sum([count + int(i) for i in num])
    return result

def reverse(num):
    return num[::-1]


def user_sort(num):
    result = list(num)
    result.sort(reverse=False) 
    return ''.join(result)


some_number = input("Enter four digit number ")

print(f'Product - {product(some_number)}')
print(f'Reverse - {reverse(some_number)}')
print(f'Sorting - {user_sort(some_number)}')