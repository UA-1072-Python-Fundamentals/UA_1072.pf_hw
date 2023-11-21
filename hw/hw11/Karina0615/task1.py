def check_age(age):
    if age <= 0:
        raise ValueError(f"Incorrect age {age}")
    elif age % 2 == 0:
        return ("Your age is even")
    else:
        return ("Your age is odd")


def enter_age():
    try:
        user_age = int(input("Enter your age:  "))
        return(check_age(user_age))
    except ValueError as err:
        print(err)
    except Exception as err:
        print(err)

if __name__ == "__main__":
    print(enter_age())