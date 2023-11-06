week_days = {
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday',
    7: 'Sunday'
}


def what_day():
    while True:
        try:
            number_of_day = int(input('To know the day of the week: '))
            if not 0 < number_of_day < 8:
                raise IndexError('Enter a number between 1 and 7\n')
            print('Your day is', week_days[number_of_day])
            break
        except IndexError as i:
            print(i)
        except Exception:
            print("You have invalid data\n")


if __name__ == "__main__":
    what_day()
