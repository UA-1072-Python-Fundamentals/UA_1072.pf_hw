c = float(input("Enter the temperature in Celsius:"))
if c<(-273.15):
    print("ERROR the temperature is below absolute 0")
else:
    f = (c * 9/5) + 32
    print(f"{c}°C is equivalent to {f}°F")