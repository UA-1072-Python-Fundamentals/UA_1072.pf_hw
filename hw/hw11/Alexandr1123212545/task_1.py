def user_error(age):
    try:
        if age > 0:
            return True
    except ValueError:
        return False


def validate_age(age):
    even = f'{age} is even'
    odd = f'{age} is odd'
    if user_error(age):
        if age >= 0 and age % 2 == 0:
            return f'{age} is even'
        else:
            return f'{age} is odd'
    else:
        return f'{age} is not the correct age! Age must not be negative or equal to zero..'


if __name__ == "__main__":
    test_lst = [18, 53, 17, 1, 3, 0, -6, -12]
    for age in test_lst:
        print(validate_age(age))
