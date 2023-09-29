
def convert_celsius (celsius: float):
    ABSOLUTE_ZERO = -273.15
    celsius = float(input("Enter the temperature in Celsius: "))
    if celsius < ABSOLUTE_ZERO:
        return "Error!!\nTemperature below absolute zero (-273.15°C)"
    else:
        fahrenheit = (celsius * 9 / 5) + 32
        return f"{celsius}°C is equivalent to {fahrenheit}°F"
celsius = None
print(convert_celsius(celsius))