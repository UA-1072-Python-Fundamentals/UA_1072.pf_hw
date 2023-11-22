def odd_or_even():
    user_input = int(input("Please enter your age: "))
    try:
        if user_input < 0:
            raise ValueError
        elif not user_input % 2:
            print("Your age is even")
        else:
            print("Your age is odd")
    except ValueError:
        print("Your age cannot be lower than 0!")


odd_or_even()