def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be a negative number.")
    elif age % 2 == 0:
        return "Even"
    else:
        return "Odd"


def main():
    try:
        user_age = int(input("Enter your age: "))
        result = check_age(user_age)
        print(f"Your age is {result}.")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
