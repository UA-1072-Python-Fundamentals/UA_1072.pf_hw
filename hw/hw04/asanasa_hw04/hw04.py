#Task1. "Temperature Converter"

celsius_temperature = float(input("Enter temperature in Celsius: "))

if celsius_temperature >= -273.15:
    fahrenheit_temperature = (celsius_temperature * 9/5) + 32
    print(f"{celsius_temperature}°C is equal to {fahrenheit_temperature:.2f}°F")

else:
    print("Error: Temperature below absolute zero (-273.15°C)")