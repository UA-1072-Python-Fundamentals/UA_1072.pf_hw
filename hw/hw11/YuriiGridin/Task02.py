def day_of_week(day):
    week = {1: "Monday",
            2: "Tuesday",
            3: "Wednesday",
            4: "Thursday",
            5: "Friday",
            6: "Saturday",
            7: "Sunday"
            }

    try:
        if not day.isnumeric():
            raise ValueError("Entered non-numerical data!")
        elif not 0 < int(day) < 8:
            raise IndexError("Entered numbers is less 1 or more 7!")
        else:
            print(f"{int(day)} is {week[int(day)]}")
    except ValueError as err:
        print(err)
    except IndexError as err:
        print(err)
    except Exception as err:
        print(err)


if __name__ == "__main__":
    day_imp = input("Enter number of a day: ")
    day_of_week(day_imp)

    # day_imp = ["1", "2", "-3", "9", "10", "jhi", "7", "0"]
    # for i in day_imp:
    #     day_of_week(i)
