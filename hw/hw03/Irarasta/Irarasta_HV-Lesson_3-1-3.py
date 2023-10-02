  ##  Input two variable from the user
print('Watch my little trick!')
num_1 = int(input("Enter 1st number: "))
num_2 = int(input("Enter 2nd number: "))
if num_1 != num_2:

  ## Swap the values of the variables
    num_1 = num_1 + num_2
    num_2 = num_1 - num_2
    num_1 = num_1 - num_2

  ## Output the result
    print("Hocus Pocus:")
    print("1st number is now:", num_1)
    print("2nd number is now:", num_2)
else:
    print('Enter 2 DIFFERENT numbers, please.')

