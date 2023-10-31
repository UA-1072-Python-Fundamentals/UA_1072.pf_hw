#Task 5.1
myList = [1, 2, 3, 22, 45, 95]

for i in range(len(myList)):
    myList[i] = float(myList[i])

print(myList)

#Task 5.2
def fibonacci():
    x = int(input("Please enter the number: "))
    num01, num02 = 0, 1
    while num01 <= x:
        print(num01)
        num03 = num01 + num02
        num01 = num02
        num02 = num03

#Task 5.3
import math

x = int(input("Please enter the number: "))
print("The factorial of the given number is", math.factorial(x))