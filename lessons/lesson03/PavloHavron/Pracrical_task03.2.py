#Task 3.02
n = str(input("Enter four-digit number:"))
def Sum(n):
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum
print(Sum(n))
print(n[::-1])

def SortedNumber(n):
    number = str(n)
    number = ''.join(sorted(number))
    number = int(number)
    return number
print(SortedNumber(n))
