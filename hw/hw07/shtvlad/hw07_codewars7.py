num=int(input("Input number: "))
lst=[]
if num <0:
    print(0)
else:
    for i in range(1,num):
        if (i%3==0) or (i%5==0):
            lst.append(i)
    print(f"List all the natural numbers below {num} that are multiples of 3 or 5: {lst}")
    print(f"The sum of these multiples is: {sum(lst)}")




