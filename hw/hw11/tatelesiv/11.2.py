# Task 11.2
def main():
    try:
        day = int(input("Enter a number (1-7) to get the day of the week: "))
        if day < 1 or day > 7:
            raise ValueError("Invalid input. Please enter a number between 1 and 7.")
        else:
            days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            print(f"Day of the week: {days[day - 1]}")
    except ValueError:
        print("Invalid input. Please enter a number FROM 1 TO 7.")


if __name__ == "__main__":
    main()
