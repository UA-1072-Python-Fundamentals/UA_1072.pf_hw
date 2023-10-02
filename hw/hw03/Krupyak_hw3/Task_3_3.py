a=int(input("Enter value : "))
b=int(input("Enter value : "))

print("Before swapping a :",a)
print("Before swapping b :",b)
#logic to swap without using third variable
a=a+b
b=a-b
a=a-b


print("After swapping a becomes :",a)
print("After swapping b becomes :",b)