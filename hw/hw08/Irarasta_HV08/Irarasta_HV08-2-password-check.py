
  ## Write a password validation program
  ## Variant - 1: correct password requirements are named AFTER input

import re

def valid_pass(password):
    if 6 <= len(password) <= 16 and re.search(r'[a-z]', password) and re.search(r'[A-Z]', password)\
            and re.search(r'[0-9]', password) and re.search(r'[$#@]', password):
        return True
    else:
        return False
while True:
    password = input('Enter  password: ')
    print('****************************')

    if valid_pass(password):
        print('Password accepted!')
        break
    else:
        print('Invalid password.\n'
              '***********************\n'
              'Password must contain:\n'
              'Upper and Lowercase,\n'
              'numbers 0-9, symbols $#@,\n'
              'min 6 to max 16 symbols.')
        print('****************************')



  ## Write a password validation program
  ## Variant - 2: correct password requirements are named BEFORE input

# import re
#
# def valid_pass(password):
#     if 6 <= len(password) <= 16 and re.search(r'[a-z]', password) and re.search(r'[A-Z]', password)\
#             and re.search(r'[0-9]', password) and re.search(r'[$#@]', password):
#         return True
#     else:
#         return False
# while True:
#     password = input('Enter password.\n'
#                  'Password must contain - \n'
#                  'Upper and Lowercas,\n'
#                  'numbers 0-9, symbols $#@,\n'
#                  'min 6 to max 16 symbols: ')
#     print('****************************')
#     if valid_pass(password):
#         print('Password accepted!')
#         break
#     else:
#         print('Invalid password.')
#         print('****************************')




