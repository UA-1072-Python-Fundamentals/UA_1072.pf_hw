def get_day():
    while True:
        try:
            user_input = int(input('Enter the day number: '))
            x = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            if 1 <= user_input <= 7:
                print(f"{user_input} is {x[user_input - 1]}")
            elif user_input > 7:
                print("The week has only 7 days")
            else:
                print("Unknown command")
        except ValueError:
            print("Enter only numbers(from 1 to 7)")


if __name__ == "__main__":
    get_day()