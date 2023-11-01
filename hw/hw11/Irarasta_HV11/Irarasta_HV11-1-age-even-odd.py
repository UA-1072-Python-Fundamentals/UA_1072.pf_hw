## Check if the User`s age is Even or Odd, raise ValueError for negative input
def even_or_odd(user_age):
    if user_age < 0:
        raise ValueError('Your age cannot be less than 0 years old.')
    if user_age % 2 == 0:
        return 'EVEN'
    else:
        return 'ODD'


def main() -> None:
    try:
        user_age = int(input('Enter your age here: '))
        check = even_or_odd(user_age)
        print(f'Your age is {check}.')
    except ValueError as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    main()
