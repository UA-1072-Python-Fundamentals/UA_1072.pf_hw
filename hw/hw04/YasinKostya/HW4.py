
def convert_celsius(celsius: float):
    absolute_zero = -273.15
    celsius_inp = float(input("Enter the temperature in Celsius: "))
    if celsius_inp < absolute_zero:
        return "Error!!\nTemperature below absolute zero (-273.15°C)"
    else:
        fahrenheit = (celsius_inp * 9 / 5) + 32
        return f"{celsius_inp}°C is equivalent to {fahrenheit}°F"
celsius = float()
# print(convert_celsius(celsius))
convert_celsius(celsius)