fact = int(input("Enter factorial of number "))
res = num = 1
while num <= fact:
    res *= num
    num += 1
print(res)