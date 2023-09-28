#   ## Input a four-digit number:
# num = int(input("Give me  a four-digit number: "))
#
# if 1000 <= num and num <= 9999:
#     print('So, here it is... ')
#   ## Find the product of the given digits:
#     digit_1 = (num // 1000) % 10
#     digit_2 = (num // 100) % 10
#     digit_3 = (num // 10) % 10
#     digit_4 = (num % 10)
#     product = digit_1 * digit_2 * digit_3 * digit_4
#
#
#   ## Write the given number in reverse order:
#     reverse_num = digit_1 + digit_2 * 10 + digit_3 * 100 + digit_4 *1000
#   ## Write the given  number in ascending order:
#     ascending_order = ''.join(sorted(str(num)))
#   ## Output the results:
#     print(f"Product of digits = {product}")
#     print(f"Number in reverse order - {reverse_num}")
#     print(f"Number in ascending order - {ascending_order}")
#   ## Check if the input is a four-digit number
# else:
#     print("Please, give me a  valid four-digit number.")

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


