celsius = float(input("Enter temperature in Celsius"))

if celsius >= -273.15:
    F = (celsius * 9/5) + 32
    print(f"{celsius}°C is equal to {F:.2f}°F")
else:
    print("Error - temperature is below absolute zero")