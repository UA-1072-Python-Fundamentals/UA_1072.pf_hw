def weekday(num):
    name_of_days = ["Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday"]
    if 1 <= num <= 7:
        return name_of_days[num - 1]
    else:
        return "Invalid day"

def main():
    try:
        num = int(input("Enter a number (1-7) to get the day of the week: "))
        day = weekday(num)
        print(f"Day of the week: {day}")
    except ValueError:
        print("Invalid input. Please enter a valid number (1-7).")

if __name__ == "__main__":
    main()