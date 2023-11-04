def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age % 2 == 0:
        return "even"
    else:
        return "odd"


def main():
    try:
        age = int(input("Enter your age: "))
        result = check_age(age)
        print(f"Your age is {result}.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main":
    main()

(main())
