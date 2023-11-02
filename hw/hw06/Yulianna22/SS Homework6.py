#Task1
numbers=list(range(1,11))
even_numbersd2=[]
odd_numbersd3=[]
other_numbers=[]
for digit in numbers:
    if digit%2==0:
        even_numbersd2.append(digit)
        result1=','.join(map(str,even_numbersd2))
    elif digit%3==0:
        odd_numbersd3.append(digit)
        result2=','.join(map(str,odd_numbersd3))
    else:
        other_numbers.append(digit)
        result3=','.join(map(str,other_numbers))
print(f'Even numbers that are divisible by 2 are: {result1}')
print(f'Even numbers that are divisible by 3 are: {result2}')
print(f'Even numbers that are divisible by 3 are: {result3}')
#Task2
user_name=input('What is your name?')
user_login=input('What is your login?')
while user_login=='First':
    print(f'Hello, dear {user_name}')
    break
if user_login!='First':
    print('Error!')

