def check_week(num_day):
    weeks = {1: "Monday", 
               2: "Thuesday", 
               3: "Wednesday", 
               4: "Thursday",
               5: "Friday",
               6: "Saturday",
               7: "Sunday"}
    try:
        
        if not num_day.isnumeric():
            raise ValueError("Incorrect day")
        elif int(num_day) not in weeks.keys():
            raise ValueError("Incorrect day")
        else:
            return (f'This is {weeks[int(num_day)]}')
    except ValueError as err:
        return err
    
if __name__ == "__main__":
    num_day_enter = input("Enter a day number of the week:  ")
    print(check_week(num_day_enter))

        
        
    
