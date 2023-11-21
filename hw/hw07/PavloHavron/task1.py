def the_largest(a,b):
    """This function compare two numbers, that user enter"""
    if a>b:
        print(a ,"the largest number.")
    else:
        print(b ,"the largest number.")
print(the_largest(a = int(input("Please enter number:")),
    b = int(input("Another one, please:"))))