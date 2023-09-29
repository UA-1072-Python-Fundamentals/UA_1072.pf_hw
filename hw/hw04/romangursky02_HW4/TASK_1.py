celsius = int(input("Please write temperature in Celsius:"))

if celsius >= -273.15:
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} °C is equivalent to {fahrenheit} F")

else:
    print("Error:\nTemperature below absolute zero (-273.15°C)")