def week_check():

    week_list = {1: "Monday",
                 2: "Tuesday",
                 3: "Wednesday",
                 4: "Thursday",
                 5: "Friday",
                 6: "Saturday",
                 7: "Sunday"}

    user_num = input("Please, enter a number: ")

    try:
        user_num = int(user_num)

        if user_num not in week_list:
            raise IndexError
        else:
            return f"The corresponding day is: {week_list[user_num]}"
    except ValueError:
        return "You must enter numbers only."
    except IndexError:
        return "The input is incorrect. Please, enter a number(1-7)"


if __name__ == "__main__":
    print(week_check())
