def get_day_of_week(number):
    if not isinstance(number, int):
        raise ValueError("Invalid input. Please enter a numerical value.")

    if number < 1:
        raise ValueError("Invalid input. Number should be 1 or greater.")
    elif number > 7:
        print("Reminder: The number should be between 1 and 7 for a day of the week.")

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    if number <= 7:
        print(f"The corresponding day of the week for {number} is {days[number - 1]}.")


try:
    user_input = input("Enter a number to determine the day of the week: ")
    user_number = int(user_input)
    get_day_of_week(user_number)
except ValueError as ve:
    print(f"Error: {ve}")

