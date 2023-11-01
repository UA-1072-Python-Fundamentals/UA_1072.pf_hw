def get_day(num):
    week = [
        'Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday'
    ]
    try:
        if week[int(num)]:
            return week[int(num)]
    except IndexError as error:
        return f'{num} out of range! Numer must by from 1 to 7!'
    except ValueError as error:
        return f'{num} - is not a number! It should only be a number!'

if __name__ == "__main__":
    test_lst = [1, 3, 5, 8, 'asdDFs', '3', '54sdf']
    for el in test_lst:
        print(f'{el} -> {get_day(el)}')

