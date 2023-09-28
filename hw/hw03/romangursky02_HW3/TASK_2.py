# TASK_1(2)a

number  = int((input("Please write your four-digit number: ")))

if 1000 <= number <= 9999:
    digit_1 = number // 1000
    digit_2 = (number // 100) % 10
    digit_3 = (number // 10) % 10
    digit_4 = number % 10

    #product of the digits
    product_of_digits = digit_1 * digit_2 * digit_3 *digit_4

    #reverved order

    reserved_order = [digit_1, digit_2, digit_3, digit_4]
    reserved_order.reverse()

    # in ascending order
    number_sorted = [digit_1, digit_2, digit_3, digit_4]
    number_sorted.sort()

    print(f"Product of tour number is: {product_of_digits}")
    print(f"Numbers in reverse order: {reserved_order}")
    print(f'Digits in ascending order: {number_sorted}')

else:
    print('Please enter a valid four-digit natural number.')

