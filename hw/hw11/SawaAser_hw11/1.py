def age_is_odd_or_even():
    while True:
        try:
            user_age = int(input('Enter your age : '))
            if user_age < 0:
                raise Exception
            print('Your age is odd' if user_age % 2 else 'Your age is even')
            break
        except Exception:
            print("You have invalid data")


if __name__ == "__main__":
    age_is_odd_or_even()
