from math import factorial


num = int(input("Enter a number whose factorial you want: "))  

if num < 0:  
   print("Factorial does not exist for negative numbers!")  
elif num == 0:  
   print("The factorial of 0 is 1")  
else:  
   print("The factorial of",num,"is", factorial(num))