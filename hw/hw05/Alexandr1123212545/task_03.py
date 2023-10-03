some_num = int(input('Enter the factorial of number '))
result = step = 1
while step <= some_num:
    result *= step
    step += 1
print(result)