# Task 1. "Temperature Converter"
temperature_in_celsius = float(input("Enter the temperature in Celsius: "))
if temperature_in_celsius >= -273.15:
    temperature_in_fahrenheit = temperature_in_celsius * 9/5 + 32
    print(f"{temperature_in_celsius}°c is equivalent {temperature_in_fahrenheit}°F")
else:
    print("Error, you entered a temperature below -273.15")
