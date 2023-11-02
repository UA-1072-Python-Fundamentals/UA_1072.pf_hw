## Get name of the week by its number
## Check if negative integer, zero or text is entered, then Raise Error.
def name_weekday(num):
    week = [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday',
    ]

    if 1 <= num <= 7:
        return week[num - 1]
    else:
        raise IndexError('Enter a number in  the correct range 1 to 7.')

try:
    num = input('To know the day of the week\n'
            'Enter a number between 1 and 7: ')
    try:
        num = int(num)
        if num < 1:
            if num == 0:
                print('Error: Number cannot be ZER0.\n'
                      'Please enter a correct number between 1 and 7.')
            else:
                print('Error: Number cannot be negative.\n'
                      'Please enter a positive number between 1 and 7.')
        else:
            day_name = name_weekday(num)
            print(f'{num} is {day_name}')
    except ValueError:
        print('Error: NO text allowed! Enter a valid number between 1 and 7.')
    except IndexError as ie:
        print('Error:', ie)
    except Exception as e:
        print('Error:', e)
except Exception as e:
    print('Error: Enter a valid number or text.')









