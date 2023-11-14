def get_day_of_week(number):
    if not isinstance(number, int):
        return "Invalid input. Please enter a numerical value."

    if 1 <= number <= 7:
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return days_of_week[number - 1]
    elif number >= 8:
        return "The number corresponds to a day of the week, but beyond the standard 7-day week"
    else:
        return "Invalid input. Please enter a positive integer"


def main():
    try:
        user_input = input("Enter a number to get the corresponding day of the week: ")
        user_number = int(user_input)
        result = get_day_of_week(user_number)
        print(f"The corresponding day of the week is: {result}")
    except ValueError:
        print("Invalid input. Please enter a valid numerical value")


if __name__ == "__main__":
    main()
