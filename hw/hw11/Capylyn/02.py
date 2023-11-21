def week_day():
    user_input = input("Please enter a number: ")
    dict = {1: "Monday",
            2: "Tuesday",
            3: "Wednesday",
            4: "Thursday",
            5: "Friday",
            6: "Saturday",
            7: "Sunday"}

    try:
        user_input = int(user_input)
        if user_input > 7 :
            raise ValueError
        else:
            print(dict[user_input])
    except ValueError:
        print("The input is incorrect!")

week_day()