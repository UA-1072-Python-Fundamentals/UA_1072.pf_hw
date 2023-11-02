def check(age):
    if age <= 0:
        raise ValueError("Entered age is negative or 0")
    elif not age % 2:
        return f"Your age is even"
    else:
        return f"Your age is odd"


def enter_age(age_imp):
    try:
        user_age = int(age_imp)
        print(check(user_age))
    except ValueError as err:
        print(err)
    except Exception as err:
        print(err)


if __name__ == "__main__":
    a = input("Enter your age: ")
    enter_age(a)


# if __name__ == "__main__":
#     l = [10, -10, 25, "uguy", 99]
#     for i in l:
#         enter_age(i)
