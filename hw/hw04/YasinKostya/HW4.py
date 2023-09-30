
while True:
    print("Please Enter action")
    print("1 - Convert Celsius to Fahrenheit\n0 - Exit")
    value = int(input())
    match value:
        case 1:
            def convert_celsius(celsius_inp: float):
                absolute_zero = -273.15
                celsius_inp = float(input("Enter the temperature in Celsius: "))
                if celsius_inp < absolute_zero:
                    return "Error!!\nTemperature below absolute zero (-273.15°C)"
                else:
                    fahrenheit = (celsius_inp * 9 / 5) + 32
                    return f"{celsius_inp}°C is equivalent to {fahrenheit}°F"


            celsius = float()
            print(convert_celsius(celsius))
        case 0:
            exit()
        case _:
            print("Error Action\nPlease Enter Current Action!")
