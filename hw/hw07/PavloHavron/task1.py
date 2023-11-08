def the_largest(a,b):
    if a>b:
        print(a ,"the largest number.")
    else:
        print(b ,"thelargest number.")
print(the_largest(a = int(input("Please enter number:")),
    b = int(input("Another one, please:"))))