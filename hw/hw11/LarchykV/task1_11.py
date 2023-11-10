def check_age():
    try:
        age = int(input("Enter your age, please: "))
        if age <= 0:
            raise ValueError("Your age must be a positive number.")
        elif (age % 2) == 0:
            return f"The number {age} is even."
        else:
            return f"The number {age} is odd."
    except ValueError as e:
        return e


if __name__ == "__main__":
    print(check_age())
