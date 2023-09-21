def user_calculate(a: int, b: int):
    result =  {
        'sum..............': a + b, 
        'difference.......': a - b, 
        'multiplication...': a * b, 
        'division.........': a / b, 
        'exponent.........': a ** b, 
        'integer division.': a // b, 
        'modulus  ........': a % b
        }
    for name, action in result.items():
        print(name, action, end='\n')


num_1, num_2 = list(input('Enter 2 values ​​separated by a space ').split())
user_calculate(int(num_1), int(num_2))
