num = int(input("Enter number:"))
f = 0
s = 1
while f+s <= num:
    third = f + s
    print(third)
    f,s=s,third