
   ##BELOW IS THE BEST VARIANT
   ## Get input from the User
num = input("Enter 4-digit number: ")
   ## Check if the entered nember is made of 4  digits
if len(num) == 4 and num.isdigit():
    digit_1 = int(num[0])
    digit_2 = int(num[1])
    digit_3 = int(num[2])
    digit_4 = int(num[3])
    product = digit_1 * digit_2 * digit_3 * digit_4
    print('The product of all digits is:', product)

    reverse = int(num[3] + num[2] + num[1] + num[0])
    print('The reverse order is:', reverse)
    ascend = sorted(num)
    print('The ascending order is:', ''.join(ascend))
   ## Asking user to enter a CORRECT 4-digits number
else:
     print("Please, give me a  valid four-digit number.")


