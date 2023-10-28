#TASKS FROM THE LESSON
#Task 1
#n=0
#while n<100:
#    n+=1
#    if n%2:
#        continue
#    else:
#        print(n)

#n=list(range(100))
#for n in list(range(100)):
#    if n%2:
#        continue
#    else:
#        print(n)

#Task2 (without continue)
#n=0
#while n<100:
#    n+=1
#    if n%2:
#        print(n)

#with continue
#n=0
#while n<100:
#    n+=1
#    if n%2==0:
#        continue
#    else:
#        print(n)

#l=[32,33,38,40,50]
#for odd in l:
#    if odd%2:
#        print(odd)
#        break


#HOMEWORK
#Task1
#l=[1,2,3,4,5,6,7,8,9,10]
#for digit in l:
#    print(float(digit))

#Task2
#def fibonacci(n):
#    a=0
#    b=1
#    while a<n:
#        print(a, )
#        a,b=b,a+b
#n=int(input('What is the last number in Fibonacci sequence?'))
#fibonacci(n)

#Task3
fact=int(input('What is your number for calculating the factorial?'))
if fact<0:
    print('Your number must be positive')
else:
    def factorial(n):
        if n==0:
            return 0
        else:
            result=1
            for digit in range(1, n+1):
                result*=digit
            return result
    user_result=factorial(fact)
    print(user_result)
        




                          