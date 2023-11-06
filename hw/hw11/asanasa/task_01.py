
def check_age(age):
    if age <= 0:
        raise ValueError('Your age cannot be less than 0 or equal to zero.')
    elif not age % 2:
        return f"Your age is even!"
    else:
        return f"Your age is odd!"

def enter(age_1):
    try:
        user_age = int(age_1)
        check = check_age(user_age)
        print(f'{check}')
    except ValueError as err:
        print(err)
    except Exception as err:
        print(err)

if __name__ == "__main__":
    a = input("Enter your age: ")
    enter(a)