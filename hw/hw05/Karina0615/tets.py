#1
#my_list = [2,4,5,6,7,3333,22,333]
#for i in my_list:
#    print(float(i))


#2
#last_number = int(input("Please enter a last number for sequences of Fibonacci"))
#x,y = 0,1

#while x+y <= last_number:
 #   fib = x+y
 #   print(fib)
 #   x = y
  #  y = fib

#3
num = int(input("Please enter a number"))

x = 0
fact = 1
for x in range(1, num+1):
    fact = fact *x
    x +=1
print(f"Factotial {num} is {fact}")


n=int(input("Factorial number: "))
f=0
sum_f=1
for f in range(1,n+1):
    sum_f=sum_f*f
    f+=1
print(f"{n}!=",sum_f)
