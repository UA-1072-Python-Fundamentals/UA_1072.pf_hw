#Task01

# my_list = ['21', 321, '03', '324', '0.55', '4', '9', 3 , 0.4]
#
# for i in my_list:
#     print(float(i))

#Task02

# n = int(input("Please write your number"))
#
# x, y = 0, 1
# count = 0
#
# if n <= 0:
#    print("Please enter a positive integer")
#
# elif n == 1:
#    print("Fibonacci sequence upto",n,":")
#    print(x)
#
# else:
#    print("Fibonacci sequence:")
#    while count < n:
#        print(x , end=" ")
#        nth = x + y
#        x = y
#        y = nth
#        count += 1


#Task03

# from math import factorial
factor = int(input("Your number >> " ))

# print("Factorial is", factorial(factor))
def factorial(n):
    return 1 if (n ==1 or n==0) else n * factorial(n -1)

print("Factorial of ", factor ,"is", factorial(factor))



