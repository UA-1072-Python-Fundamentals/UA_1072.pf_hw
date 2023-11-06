def get_day_of_week():
    try:
        number = int(input("Enter a number (1-7): "))
        if number >= 1 and number <= 7:
            days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            day = days[number - 1]
            print(f"The day of the week for {number} is {day}.")
        elif number >= 8:
            print("Number is greater than 7. Please enter a number from 1 to 7.")
        else:
            print("Invalid input. Please enter a number from 1 to 7.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    get_day_of_week()
