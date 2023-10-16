for num in range(1,11):
    if num % 2 == 0 and  num % 3 == 0:
        print(f"{num} - This number is divisible by 2 and 3 ")
    elif num % 2 == 0:
        print(f'{num} - Number is  divisible by 2')
    elif num % 3 == 0:
        print(f'{num}  - Number is divisible by 3')
    else:
        print(f"{num} - Number are not divisible  by 2 and 3 ")
