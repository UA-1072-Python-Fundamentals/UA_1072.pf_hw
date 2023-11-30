check=True
while check:
    try:
        number = int(input("Enter the number of day: "))
        match number:
            case 1:
                print("Monday")
            case 2:
                print("Tuesday")
            case 3:
                print("Wednesday")
            case 4:
                print("Thursday")
            case 5:
                print("Friday")
            case 6:
                print("Saturday")
            case 7:
                print("Sunday")
            case other:
                raise ValueError
        check=False
    except:
        ValueError
        print("You entered incorrect number. Try again")
